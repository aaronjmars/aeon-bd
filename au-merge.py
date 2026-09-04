#!/usr/bin/env python3
import subprocess, os, tempfile

BASE = "3b4c5a3ff1d9846530e02ed5e6796a4a409d2674"
HEAD = "bf33365164c5a8b50d49a0ed64a45521dbe96771"

FILES = [
 ".github/dependabot.yml",
 ".github/workflows/aeon.yml",
 ".github/workflows/ci-skill-integrity.yml",
 ".github/workflows/ci-tests.yml",
 ".github/workflows/messages.yml",
 "CHANGELOG.md",
 "scripts/llm-gateway.sh",
 "skills/feature/SKILL.md",
 "skills/pr-review/SKILL.md",
 "skills/skill-health/SKILL.md",
 "skills/vuln-scanner/SKILL.md",
]

def blob(ref, path):
    r = subprocess.run(["git","show",f"{ref}:{path}"], capture_output=True)
    return r.stdout  # bytes

WORK = tempfile.mkdtemp(prefix="au-merge-")
for f in FILES:
    base = blob(BASE, f)
    head = blob(HEAD, f)
    with open(f,"rb") as fh: local = fh.read()
    bp=os.path.join(WORK,"base"); hp=os.path.join(WORK,"head"); lp=os.path.join(WORK,"local")
    open(bp,"wb").write(base); open(hp,"wb").write(head); open(lp,"wb").write(local)
    # git merge-file -p --diff3 local base head  (writes merged to stdout, exit 0=clean)
    r = subprocess.run(["git","merge-file","-p","--diff3",lp,bp,hp], capture_output=True)
    if r.returncode==0:
        outp = f + ".AUMERGED"
        os.makedirs(os.path.dirname(outp) or ".", exist_ok=True)
        open(outp,"wb").write(r.stdout)
        print(f"CLEAN-MERGE  {f}  -> {outp} ({len(r.stdout)} bytes)")
    else:
        # count conflict hunks
        n = r.stdout.count(b"<<<<<<<")
        print(f"CONFLICT({n})  {f}")
print("WORK="+WORK)
