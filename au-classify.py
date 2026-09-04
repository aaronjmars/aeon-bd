#!/usr/bin/env python3
import subprocess, os

BASE = "3b4c5a3ff1d9846530e02ed5e6796a4a409d2674"
HEAD = "bf33365164c5a8b50d49a0ed64a45521dbe96771"

def sh(*args):
    return subprocess.run(args, capture_output=True, text=True)

def is_operator(f):
    if f in ("aeon.yml","STRATEGY.md",".mcp.json","aeon.db","skills.lock","eyebrowlock.json"):
        return True
    for p in ("soul/","memory/","output/",".env","apps/dashboard/outputs/"):
        if f.startswith(p): return True
    if f.startswith("catalog/") and f.endswith(".json"): return True
    if f.startswith(".claude/skills/aeon/"): return False   # exception -> OWNED
    if f.startswith(".claude/"): return True
    return False

def gblob(ref, path):
    r = sh("git","rev-parse",f"{ref}:{path}")
    return r.stdout.strip() if r.returncode==0 else ""

def lblob(path):
    if not os.path.exists(path): return ""
    r = sh("git","hash-object",path)
    return r.stdout.strip() if r.returncode==0 else ""

diff = sh("git","diff","--name-status",BASE,HEAD).stdout.strip().splitlines()
rows=[]
for line in diff:
    parts=line.split("\t")
    st=parts[0]; f=parts[-1]
    if is_operator(f):
        rows.append(("OPERATOR",st,f)); continue
    bsha=gblob(BASE,f); hsha=gblob(HEAD,f); lsha=lblob(f)
    if st=="A":
        rows.append(("CLEAN-ADD" if not lsha else "CONFLICT-addcollision",st,f))
    elif st=="M":
        if not lsha: rows.append(("ABSENT-LOCAL",st,f))
        elif lsha==hsha: rows.append(("SKIP-synced",st,f))
        elif lsha==bsha: rows.append(("CLEAN-UPDATE",st,f))
        else: rows.append(("THREEWAY",st,f))
    elif st=="D":
        if not lsha: rows.append(("SKIP-alreadygone",st,f))
        elif lsha==bsha: rows.append(("CLEAN-DELETE",st,f))
        else: rows.append(("CONFLICT-delete",st,f))
    elif st.startswith("R"):
        rows.append(("RENAME",st,f))
    else:
        rows.append(("UNKNOWN",st,f))

for disp,st,f in sorted(rows):
    print(f"{disp:24} {f}")
