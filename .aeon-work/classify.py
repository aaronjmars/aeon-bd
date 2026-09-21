#!/usr/bin/env python3
import subprocess, hashlib, os, base64

UP = "aeonfun/aeon"
BASE = "95142d19705ca379815e7fc9493a497ee0504e8d"
HEAD = "ba01e9f3e4495c8f761ab483000639cc8d5f5221"
WORK = ".aeon-work"

os.makedirs(WORK + "/base", exist_ok=True)
os.makedirs(WORK + "/head", exist_ok=True)
os.makedirs(WORK + "/merged", exist_ok=True)

def fetch(path, ref, outfile):
    try:
        r = subprocess.run(["gh", "api", f"repos/{UP}/contents/{path}?ref={ref}",
                            "--jq", ".content"], capture_output=True, text=True, timeout=60)
        if r.returncode != 0 or not r.stdout.strip():
            return False
        data = base64.b64decode(r.stdout)
        with open(outfile, "wb") as f:
            f.write(data)
        return True
    except Exception:
        return False

def sh256(p):
    try:
        with open(p, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return None

results = []
with open(WORK + "/owned.tsv") as f:
    rows = [ln.rstrip("\n").split("\t") for ln in f if ln.strip()]

for st, path in rows:
    safe = path.replace("/", "_")
    bfile = f"{WORK}/base/{safe}"
    hfile = f"{WORK}/head/{safe}"
    if st == "added":
        fetch(path, HEAD, hfile)
        disp = "CONFLICT-ADDCOLLIDE" if os.path.exists(path) else "CLEAN-ADD"
    elif st in ("modified", "renamed"):
        ok_b = fetch(path, BASE, bfile)
        ok_h = fetch(path, HEAD, hfile)
        if not os.path.exists(path):
            disp = "ABSENT-LOCAL"
        else:
            lsha, hsha, bsha = sh256(path), sh256(hfile), sh256(bfile)
            if lsha == hsha:
                disp = "SKIP-SYNCED"
            elif lsha == bsha:
                disp = "CLEAN-UPDATE"
            else:
                mout = f"{WORK}/merged/{safe}"
                import shutil
                shutil.copy(path, f"{WORK}/local.tmp")
                with open(mout, "w") as mo:
                    rc = subprocess.run(["git", "merge-file", "-p", "--diff3",
                                         f"{WORK}/local.tmp", bfile, hfile],
                                        stdout=mo, stderr=subprocess.DEVNULL).returncode
                disp = "CLEAN-MERGE" if rc == 0 else "CONFLICT-3WAY"
    elif st == "removed":
        fetch(path, BASE, bfile)
        if not os.path.exists(path):
            disp = "SKIP-ALREADYGONE"
        else:
            disp = "CLEAN-DELETE" if sh256(path) == sh256(bfile) else "CONFLICT-DELETE"
    else:
        disp = "UNKNOWN"
    results.append((disp, st, path))
    print(f"{disp}\t{st}\t{path}")

with open(WORK + "/result.tsv", "w") as f:
    for disp, st, path in results:
        f.write(f"{disp}\t{st}\t{path}\n")
