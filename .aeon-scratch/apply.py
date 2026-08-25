#!/usr/bin/env python3
import json, subprocess, os, base64
UPSTREAM="aeonfun/aeon"
HEAD="8b8d719715ec9bb68fb858a1e334d23209047d82"
SCRATCH=".aeon-scratch"
def sh(a): return subprocess.run(a,capture_output=True,text=True)
def fetch_bytes(path,ref):
    r=sh(["gh","api",f"repos/{UPSTREAM}/contents/{path}?ref={ref}","--jq",".content"])
    if r.returncode!=0 or not r.stdout.strip(): return None
    try: return base64.b64decode(r.stdout)
    except: return None

results=json.load(open(os.path.join(SCRATCH,"results.json")))
written=[]
for r in results:
    p=r["path"]; disp=r["disp"]
    if disp in ("CLEAN-ADD","CLEAN-UPDATE"):
        b=fetch_bytes(p,HEAD)
        if b is None:
            print("FETCH-FAIL",p); continue
        os.makedirs(os.path.dirname(p) or ".",exist_ok=True)
        open(p,"wb").write(b)
        written.append((disp,p))
    elif disp=="CLEAN-MERGE":
        mp=r["merged"]
        b=open(mp,"rb").read()
        os.makedirs(os.path.dirname(p) or ".",exist_ok=True)
        open(p,"wb").write(b)
        written.append((disp,p))
    elif disp=="CLEAN-DELETE":
        written.append((disp,p))
print(f"WROTE {len(written)} files")
# quick YAML/JSON parse check on written .yml/.json/.mjs-adjacent
import sys
bad=[]
for disp,p in written:
    if p.endswith(".json"):
        try: json.load(open(p))
        except Exception as e: bad.append((p,str(e)))
if bad:
    print("PARSE-FAIL:",bad)
else:
    print("json parse checks OK")
for disp,p in written: print(" ",disp,p)
