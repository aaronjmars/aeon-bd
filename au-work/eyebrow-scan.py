#!/usr/bin/env python3
"""Run the eyebrow scan with a SCRUBBED environment (PATH + HOME only) —
same semantics as `env -i PATH=$PATH HOME=$HOME eyebrow scan ...`. The scan
is a local file-hasher: no secrets, no network."""
import os, subprocess, sys

eb = os.path.abspath("au-work/eb/x/eyebrow")
scrubbed = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "HOME": os.environ.get("HOME", "/home/runner")}
r = subprocess.run([eb, "scan", "--path", ".", "--lockfile", "eyebrowlock.json"],
                   env=scrubbed, capture_output=True, cwd=os.getcwd())
print("exit:", r.returncode)
out = (r.stdout or b"").decode(errors="replace")
err = (r.stderr or b"").decode(errors="replace")
print(out[-3000:])
if err.strip():
    print("stderr:", err[-2000:])
sys.exit(r.returncode)
