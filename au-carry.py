#!/usr/bin/env python3
import subprocess, os
HEAD="bf33365164c5a8b50d49a0ed64a45521dbe96771"
carried=[".github/README.md","docs/skill-packs.md","llms.txt",
         "skills/heartbeat/SKILL.md","skills/memory-flush/SKILL.md"]
def gblob(ref,p):
    r=subprocess.run(["git","rev-parse",f"{ref}:{p}"],capture_output=True,text=True)
    return r.stdout.strip() if r.returncode==0 else "(absent-upstream)"
def lblob(p):
    if not os.path.exists(p): return "(absent-local)"
    return subprocess.run(["git","hash-object",p],capture_output=True,text=True).stdout.strip()
for p in carried:
    h=gblob(HEAD,p); l=lblob(p)
    print(f"{p}: local={l[:10]} head={h[:10]} -> {'DIVERGENT(keep)' if l!=h else 'RESOLVED(drop)'}")
