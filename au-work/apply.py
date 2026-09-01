#!/usr/bin/env python3
"""aeon-update S7: apply CLEAN-ADD / CLEAN-UPDATE / CLEAN-MERGE on the sync branch."""
import json, os, subprocess, sys

BASE = "8b8d719715ec9bb68fb858a1e334d23209047d82"
HEAD = "3b4c5a3ff1d9846530e02ed5e6796a4a409d2674"
ROOT = os.getcwd()
BR = "aeon-update/sync-3b4c5a3"
TSV = os.path.join(ROOT, "au-work", "classification.tsv")
MERGES = os.path.join(ROOT, "au-work", "merges")

def run(args, **kw):
    return subprocess.run(args, capture_output=True, cwd=ROOT, **kw)

r = run(["git", "checkout", "-b", BR])
if r.returncode != 0:
    # branch may exist from an aborted attempt; reuse if so
    r2 = run(["git", "rev-parse", "--verify", BR])
    if r2.returncode != 0:
        print("FATAL: cannot create branch:", r.stderr.decode()); sys.exit(1)
    run(["git", "checkout", BR])

added = updated = merged = 0
applied_paths = []
for line in open(TSV):
    st, f, disp, reason = (line.rstrip("\n").split("\t") + [""])[:4]
    dest = os.path.join(ROOT, f)
    if disp == "CLEAN-ADD" or disp == "CLEAN-UPDATE":
        blob = run(["git", "show", f"{HEAD}:{f}"])
        if blob.returncode != 0:
            print(f"UNREADABLE upstream blob for {f}"); continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(blob.stdout)
        # match upstream file mode (100755 vs 100644)
        mode = run(["git", "ls-tree", HEAD, "--", f]).stdout.decode().split()
        if len(mode) >= 1 and mode[0] == "100755":
            os.chmod(dest, 0o755)
        applied_paths.append(f)
        if disp == "CLEAN-ADD": added += 1
        else: updated += 1
    elif disp == "CLEAN-MERGE":
        flat = f.replace("/", "_")
        src = os.path.join(MERGES, flat)
        with open(src, "rb") as fh: data = fh.read()
        with open(dest, "wb") as fh: fh.write(data)
        applied_paths.append(f)
        merged += 1

print(f"applied: added={added} updated={updated} merged={merged}")
with open(os.path.join(ROOT, "au-work", "applied.json"), "w") as fh:
    json.dump({"added": added, "updated": updated, "merged": merged,
               "paths": applied_paths}, fh, indent=1)

# --- parse checks on written files (YAML/JSON) ---
import glob
bad = []
try:
    import yaml
    have_yaml = True
except ImportError:
    have_yaml = False
for f in applied_paths + ["skills/skill-health/SKILL.md", "skills/skill-repair/SKILL.md",
                          "skills/changelog/SKILL.md"]:
    p = os.path.join(ROOT, f)
    if not os.path.exists(p): bad.append(f + " (missing!)"); continue
    if f.endswith(".json"):
        try: json.load(open(p))
        except Exception as e: bad.append(f"{f}: {e}")
    elif f.endswith((".yml", ".yaml")) and have_yaml:
        try: yaml.safe_load(open(p))
        except Exception as e: bad.append(f"{f}: {e}")
    elif f.endswith("SKILL.md"):
        # frontmatter sanity: starts with ---, closing --- found, name: present
        text = open(p, encoding="utf-8", errors="replace").read()
        if not text.startswith("---") or "\n---" not in text[3:]:
            bad.append(f"{f}: broken frontmatter delimiters")
        else:
            fm = text[3:text.index("\n---", 3)]
            if "name:" not in fm: bad.append(f"{f}: no name: in frontmatter")
print("parse-check:", "ALL OK" if not bad else "FAILURES")
for b in bad: print("  BAD:", b)
