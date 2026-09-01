#!/usr/bin/env python3
"""Apply the two skills deferred in prior runs (needs-eyebrowlock-scan):
fetch upstream@HEAD blobs, preserve modes. The pinned eyebrow binary is
available this run, so the lock rescan below will cover them."""
import os, subprocess

HEAD = "3b4c5a3ff1d9846530e02ed5e6796a4a409d2674"
ROOT = os.getcwd()
FILES = ["skills/rightstack/SKILL.md", "skills/rightstack/run.mjs",
         "skills/skill-article/SKILL.md"]

for f in FILES:
    dest = os.path.join(ROOT, f)
    assert not os.path.exists(dest), f"collision: {dest} already exists"
    blob = subprocess.run(["git", "show", f"{HEAD}:{f}"], capture_output=True, cwd=ROOT)
    assert blob.returncode == 0, f"cannot fetch {f}"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(blob.stdout)
    mode = subprocess.run(["git", "ls-tree", HEAD, "--", f],
                          capture_output=True, cwd=ROOT).stdout.decode().split()
    os.chmod(dest, 0o755 if mode and mode[0] == "100755" else 0o644)
    print("applied", f, oct(os.stat(dest).st_mode & 0o777), len(blob.stdout), "bytes")
