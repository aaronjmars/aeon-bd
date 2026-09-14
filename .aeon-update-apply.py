#!/usr/bin/env python3
import subprocess, os, json

UP = "aeonfun/aeon"
HEAD = "95142d19705ca379815e7fc9493a497ee0504e8d"
WORK = ".aeon-update-work"

def fetch(path, ref):
    r = subprocess.run(["gh","api",f"repos/{UP}/contents/{path}?ref={ref}",
        "-H","Accept: application/vnd.github.raw"], capture_output=True)
    return r.stdout if r.returncode==0 else None

results = json.load(open(".aeon-update-results.json"))
applied = {"added":[], "updated":[], "merged":[]}

# skip the brand-new skill until eyebrow scan passes (handled separately)
DEFER = {"skills/miroshark-matchday/SKILL.md"}

for r in results:
    p, disp = r["path"], r["disp"]
    if p in DEFER:
        continue
    if disp == "CLEAN-ADD":
        b = fetch(p, HEAD)
        assert b is not None, f"fetch failed {p}"
        os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
        open(p,"wb").write(b)
        applied["added"].append(p)
    elif disp == "CLEAN-UPDATE":
        b = fetch(p, HEAD)
        assert b is not None, f"fetch failed {p}"
        open(p,"wb").write(b)
        applied["updated"].append(p)
    elif disp == "CLEAN-MERGE":
        mf = f"{WORK}/{p.replace('/','__')}.merged"
        b = open(mf,"rb").read()
        open(p,"wb").write(b)
        applied["merged"].append(p)

json.dump(applied, open(".aeon-update-applied.json","w"), indent=2)
print("ADDED:", len(applied["added"]))
for x in applied["added"]: print("  +", x)
print("UPDATED:", len(applied["updated"]))
for x in applied["updated"]: print("  ~", x)
print("MERGED:", len(applied["merged"]))
for x in applied["merged"]: print("  M", x)
