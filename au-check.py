#!/usr/bin/env python3
import subprocess, glob, os
# all files changed on the branch vs HEAD^ (staged/unstaged)
r=subprocess.run(["git","diff","--name-only"],capture_output=True,text=True)
changed=[f for f in r.stdout.split() ]
# also newly added (untracked) that we wrote
r2=subprocess.run(["git","status","--porcelain"],capture_output=True,text=True)
for line in r2.stdout.splitlines():
    st=line[:2]; f=line[3:]
    if "A" in st or "?" in st:
        changed.append(f)
changed=sorted(set(changed))
bad=0
for f in changed:
    if not os.path.isfile(f): continue
    try:
        data=open(f,"rb").read()
    except Exception: continue
    if b"<<<<<<<" in data or b">>>>>>>" in data:
        print("MARKER in",f); bad+=1
    if f.endswith((".yml",".yaml")):
        try:
            import yaml;
            list(yaml.safe_load_all(data.decode()))
        except Exception as e:
            print("YAML-ERR",f,str(e)[:80]); bad+=1
    if f.endswith(".json"):
        try:
            import json; json.loads(data.decode())
        except Exception as e:
            print("JSON-ERR",f,str(e)[:80]); bad+=1
print(f"checked {len(changed)} changed files; problems={bad}")
