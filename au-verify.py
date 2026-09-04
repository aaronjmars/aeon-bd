#!/usr/bin/env python3
import subprocess, sys

MERGED = [
 ".github/workflows/ci-skill-integrity.yml",
 "scripts/llm-gateway.sh",
 "skills/feature/SKILL.md",
 "skills/skill-health/SKILL.md",
]

print("=== marker check + parse ===")
for f in MERGED:
    p=f+".AUMERGED"
    data=open(p,"rb").read()
    markers = data.count(b"<<<<<<<")+data.count(b">>>>>>>")+data.count(b"=======\n")
    note=""
    if f.endswith(".yml"):
        try:
            import yaml; yaml.safe_load(data.decode()); note="yaml-ok"
        except Exception as e: note="YAML-ERR:"+str(e)[:80]
    elif f.endswith(".sh"):
        r=subprocess.run(["bash","-n",p],capture_output=True,text=True)
        note="sh-ok" if r.returncode==0 else "SH-ERR:"+r.stderr[:80]
    print(f"  {f}: markers={markers} {note}")

print("\n=== llm-gateway.sh: what operator customization the merge preserved (merged vs upstream HEAD) ===")
HEAD="bf33365164c5a8b50d49a0ed64a45521dbe96771"
r=subprocess.run(["git","show",f"{HEAD}:scripts/llm-gateway.sh"],capture_output=True)
open("/tmp/lg-head","wb").write(r.stdout)
d=subprocess.run(["git","diff","--no-index","/tmp/lg-head","scripts/llm-gateway.sh.AUMERGED"],capture_output=True,text=True)
print(d.stdout[:3000] if d.stdout else "(identical to upstream HEAD)")
