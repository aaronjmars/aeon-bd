#!/usr/bin/env python3
import subprocess, hashlib, os, json, sys

UP = "aeonfun/aeon"
BASE = "c28ab4c2f529e39c250c0a440f5d2372b0e88e57"
HEAD = "95142d19705ca379815e7fc9493a497ee0504e8d"
WORK = ".aeon-update-work"
os.makedirs(WORK, exist_ok=True)

def sh(args):
    return subprocess.run(args, capture_output=True)

def fetch(path, ref):
    # raw content via gh api; returns bytes or None
    r = sh(["gh", "api", f"repos/{UP}/contents/{path}?ref={ref}",
            "-H", "Accept: application/vnd.github.raw"])
    if r.returncode != 0:
        return None
    return r.stdout

def sha(b):
    if b is None:
        return None
    return hashlib.sha256(b).hexdigest()

# files: list of (status, path)
files = json.load(open(".aeon-update-files.json"))

# OPERATOR-owned matcher
def is_operator(p):
    ops = ["aeon.yml","STRATEGY.md",".mcp.json","aeon.db","skills.lock","eyebrowlock.json"]
    if p in ops: return True
    if p.startswith("soul/") or p.startswith("memory/") or p.startswith("output/"): return True
    if p.startswith(".env"): return True
    if p.startswith("catalog/") and p.endswith(".json"): return True
    if p.startswith("apps/dashboard/outputs/"): return True
    if p.startswith(".claude/") and not p.startswith(".claude/skills/aeon/"): return True
    return False

results = []
for status, path, prev in files:
    if is_operator(path):
        results.append({"path":path,"status":status,"disp":"OPERATOR"})
        continue
    # OWNED
    if status == "added":
        if os.path.exists(path):
            results.append({"path":path,"status":status,"disp":"CONFLICT","reason":"add-add-collision"})
        else:
            results.append({"path":path,"status":status,"disp":"CLEAN-ADD"})
        continue
    if status == "modified":
        local = open(path,"rb").read() if os.path.exists(path) else None
        hb = fetch(path, HEAD)
        bb = fetch(path, BASE)
        ls, hs, bs = sha(local), sha(hb), sha(bb)
        if local is None:
            results.append({"path":path,"status":status,"disp":"CONFLICT","reason":"modified-upstream-absent-local"})
        elif ls == hs:
            results.append({"path":path,"status":status,"disp":"SKIP"})
        elif ls == bs:
            # save head blob for writing
            open(f"{WORK}/{path.replace('/','__')}.head","wb").write(hb)
            results.append({"path":path,"status":status,"disp":"CLEAN-UPDATE"})
        else:
            # 3-way merge
            lf = f"{WORK}/{path.replace('/','__')}.local"
            bf = f"{WORK}/{path.replace('/','__')}.base"
            hf = f"{WORK}/{path.replace('/','__')}.head"
            open(lf,"wb").write(local)
            open(bf,"wb").write(bb if bb else b"")
            open(hf,"wb").write(hb if hb else b"")
            mf = f"{WORK}/{path.replace('/','__')}.merged"
            m = subprocess.run(["git","merge-file","-p","--diff3",lf,bf,hf],capture_output=True)
            if m.returncode == 0:
                open(mf,"wb").write(m.stdout)
                results.append({"path":path,"status":status,"disp":"CLEAN-MERGE"})
            else:
                results.append({"path":path,"status":status,"disp":"CONFLICT","reason":"3way-overlap"})
        continue
    if status == "removed":
        local = open(path,"rb").read() if os.path.exists(path) else None
        bb = fetch(path, BASE)
        if local is None:
            results.append({"path":path,"status":status,"disp":"SKIP"})
        elif sha(local) == sha(bb):
            results.append({"path":path,"status":status,"disp":"CLEAN-DELETE"})
        else:
            results.append({"path":path,"status":status,"disp":"CONFLICT","reason":"removed-upstream-diverged-local"})
        continue
    results.append({"path":path,"status":status,"disp":"UNKNOWN"})

json.dump(results, open(".aeon-update-results.json","w"), indent=2)
for r in results:
    print(f"{r['disp']:14} {r['status']:9} {r['path']}  {r.get('reason','')}")
