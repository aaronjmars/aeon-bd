#!/usr/bin/env python3
import os, shutil

WORK = "aeon-update-work"

CLEAN_UPDATE = [
 "harness-adapter/lib/sandbox.sh",
 "plugin/skills/aeon/SKILL.md",
 "plugin/skills/aeon/references/layout.md",
 "plugin/skills/aeon/references/mcp.md",
 "plugin/skills/aeon/references/skill-anatomy.md",
 "scripts/competitor-monitor.mjs",
 "scripts/stage-deploy-uni-hook.sh",
 "skills/aeon-update/SKILL.md",
 "skills/competitor-monitor/SKILL.md",
]
CLEAN_MERGE = [
 ".github/workflows/aeon.yml",
 "skills/changelog/SKILL.md",
]

def mangle(f):
    return f.replace("/", "__")

for f in CLEAN_UPDATE:
    src = os.path.join(WORK, "head_" + mangle(f))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    shutil.copyfile(src, f)
    print("UPDATE", f)

for f in CLEAN_MERGE:
    src = os.path.join(WORK, "merged_" + mangle(f))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    shutil.copyfile(src, f)
    print("MERGE ", f)

print("done")
