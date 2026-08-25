#!/usr/bin/env python3
import json, subprocess, hashlib, os, base64, sys

UPSTREAM="aeonfun/aeon"
BASELINE="b7a909aa412d8e654df15417fcff0682dac39682"
HEAD="8b8d719715ec9bb68fb858a1e334d23209047d82"
SCRATCH=".aeon-scratch"

def sh(args):
    return subprocess.run(args, capture_output=True, text=True)

# load compare
r = sh(["gh","api",f"repos/{UPSTREAM}/compare/{BASELINE}...{HEAD}"])
d = json.loads(r.stdout)
files = d.get("files",[])

def is_operator(p):
    ops = ["aeon.yml","STRATEGY.md",".mcp.json","aeon.db","skills.lock","eyebrowlock.json"]
    if p in ops: return True
    for pre in ["soul/","memory/","output/","apps/dashboard/outputs/"]:
        if p.startswith(pre): return True
    if p.startswith(".env"): return True
    if p.startswith("catalog/") and p.endswith(".json"): return True
    if p.startswith(".claude/"):
        if p.startswith(".claude/skills/aeon/"): return False  # exception -> OWNED
        return True
    return False

def fetch(path, ref):
    r = sh(["gh","api",f"repos/{UPSTREAM}/contents/{path}?ref={ref}","--jq",".content"])
    if r.returncode!=0 or not r.stdout.strip():
        return None
    try:
        return base64.b64decode(r.stdout)
    except Exception:
        return None

def sha(b):
    return hashlib.sha256(b).hexdigest() if b is not None else None

def local_bytes(p):
    if not os.path.exists(p): return None
    with open(p,"rb") as f: return f.read()

results=[]
for f in files:
    p=f["filename"]; st=f["status"]; prev=f.get("previous_filename")
    if is_operator(p):
        results.append({"path":p,"status":st,"class":"OPERATOR","disp":"SURFACE"})
        continue
    # OWNED
    lb = local_bytes(p)
    if st=="added":
        if lb is None:
            results.append({"path":p,"status":st,"class":"OWNED","disp":"CLEAN-ADD"})
        else:
            hb=fetch(p,HEAD)
            if sha(lb)==sha(hb):
                results.append({"path":p,"status":st,"class":"OWNED","disp":"SKIP","reason":"already-present-identical"})
            else:
                results.append({"path":p,"status":st,"class":"OWNED","disp":"CONFLICT","reason":"add-add-collision"})
    elif st=="modified":
        hb=fetch(p,HEAD); bb=fetch(p,BASELINE)
        if lb is not None and sha(lb)==sha(hb):
            results.append({"path":p,"status":st,"class":"OWNED","disp":"SKIP","reason":"already-synced"})
        elif lb is not None and sha(lb)==sha(bb):
            results.append({"path":p,"status":st,"class":"OWNED","disp":"CLEAN-UPDATE"})
        else:
            # 3-way merge
            if lb is None:
                results.append({"path":p,"status":st,"class":"OWNED","disp":"CONFLICT","reason":"local-missing-upstream-modified"})
                continue
            base_f=os.path.join(SCRATCH,"base.tmp"); head_f=os.path.join(SCRATCH,"head.tmp"); loc_f=os.path.join(SCRATCH,"local.tmp")
            with open(base_f,"wb") as x: x.write(bb or b"")
            with open(head_f,"wb") as x: x.write(hb or b"")
            with open(loc_f,"wb") as x: x.write(lb)
            m=sh(["git","merge-file","-p","--diff3",loc_f,base_f,head_f])
            if m.returncode==0:
                # store merged
                safe=p.replace("/","__")
                mp=os.path.join(SCRATCH,"merged__"+safe)
                with open(mp,"wb") as x: x.write(m.stdout.encode())
                results.append({"path":p,"status":st,"class":"OWNED","disp":"CLEAN-MERGE","merged":mp})
            else:
                results.append({"path":p,"status":st,"class":"OWNED","disp":"CONFLICT","reason":"operator-customized-overlap"})
    elif st=="removed":
        bb=fetch(p,BASELINE)
        if lb is None:
            results.append({"path":p,"status":st,"class":"OWNED","disp":"SKIP","reason":"already-gone"})
        elif sha(lb)==sha(bb):
            results.append({"path":p,"status":st,"class":"OWNED","disp":"CLEAN-DELETE"})
        else:
            results.append({"path":p,"status":st,"class":"OWNED","disp":"CONFLICT","reason":"local-diverged-upstream-removed"})
    elif st=="renamed":
        results.append({"path":p,"status":st,"class":"OWNED","disp":"RENAMED","prev":prev,"note":"handle-manually"})
    else:
        results.append({"path":p,"status":st,"class":"OWNED","disp":"UNKNOWN"})

with open(os.path.join(SCRATCH,"results.json"),"w") as x:
    json.dump(results,x,indent=1)

# summary
from collections import Counter
c=Counter(r["disp"] for r in results)
print("DISPOSITION COUNTS:",dict(c))
print()
for disp in ["CLEAN-ADD","CLEAN-UPDATE","CLEAN-MERGE","CLEAN-DELETE","CONFLICT","SKIP","OPERATOR","RENAMED","UNKNOWN"]:
    rs=[r for r in results if r["disp"]==disp]
    if rs:
        print(f"== {disp} ({len(rs)}) ==")
        for r in rs:
            extra=r.get("reason","") or r.get("note","")
            print("  ",r["path"], extra)
