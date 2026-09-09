#!/usr/bin/env python3
import subprocess, hashlib, base64, json, os

UPSTREAM = "aeonfun/aeon"
BASELINE = "21b82dbb7d4927515ec0ad6cbf36f7daac6cc225"
HEAD = "c28ab4c2f529e39c250c0a440f5d2372b0e88e57"
WORK = "aeon-update-work"
os.makedirs(WORK, exist_ok=True)

def fetch(path, ref):
    # returns bytes or None
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{UPSTREAM}/contents/{path}?ref={ref}", "--jq", ".content"],
            capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return None
        c = out.stdout.strip()
        if not c:
            return None
        return base64.b64decode(c)
    except Exception:
        return None

def sh(b):
    return hashlib.sha256(b).hexdigest() if b is not None else None

# (path, status)
MODIFIED = [
 ".claude/skills/aeon/SKILL.md",
 ".claude/skills/aeon/references/layout.md",
 ".claude/skills/aeon/references/mcp.md",
 ".claude/skills/aeon/references/skill-anatomy.md",
 ".github/README.md",
 ".github/workflows/aeon.yml",
 "CHANGELOG.md",
 "apps/dashboard/lib/skill-icons.data.ts",
 "docs/skill-packs.md",
 "harness-adapter/lib/sandbox.sh",
 "plugin/skills/aeon/SKILL.md",
 "plugin/skills/aeon/references/layout.md",
 "plugin/skills/aeon/references/mcp.md",
 "plugin/skills/aeon/references/skill-anatomy.md",
 "scripts/competitor-monitor.mjs",
 "scripts/stage-deploy-uni-hook.sh",
 "skills/aeon-update/SKILL.md",
 "skills/changelog/SKILL.md",
 "skills/competitor-monitor/SKILL.md",
]

ADDED = [
 "docs/assets/skill-icons/compute-resell.svg",
 "docs/assets/skill-icons/cortx-reliability.svg",
 "docs/assets/skill-icons/submit-hook.svg",
 "skills/compute-resell/SKILL.md",
 "skills/compute-resell/allocate_caps.py",
 "skills/compute-resell/bootstrap-siwe.mjs",
 "skills/compute-resell/claim_ledger.py",
 "skills/compute-resell/config.example.json",
 "skills/compute-resell/price_models.py",
 "skills/compute-resell/score_models.py",
 "skills/submit-hook/SKILL.md",
 "skills/submit-hook/submit-univ4.py",
]

results = {"skip": [], "clean_update": [], "clean_merge": [], "conflict": [], "clean_add": [], "clean_add_absent": []}
detail = {}

for f in MODIFIED:
    local_exists = os.path.exists(f)
    local = open(f, "rb").read() if local_exists else None
    head_blob = fetch(f, HEAD)
    base_blob = fetch(f, BASELINE)
    sl, sh_head, sh_base = sh(local), sh(head_blob), sh(base_blob)
    if not local_exists:
        detail[f] = "modified-upstream-but-local-absent"
        results["conflict"].append((f, "local-absent"))
        continue
    if sl == sh_head:
        results["skip"].append(f); detail[f]="skip-already-synced"; continue
    if sl == sh_base:
        # write head blob
        open(os.path.join(WORK, "head_"+f.replace("/","__")), "wb").write(head_blob)
        results["clean_update"].append(f); detail[f]="clean-update"; continue
    # 3-way merge
    lp = os.path.join(WORK, "local_"+f.replace("/","__"))
    bp = os.path.join(WORK, "base_"+f.replace("/","__"))
    hp = os.path.join(WORK, "head_"+f.replace("/","__"))
    open(lp,"wb").write(local)
    open(bp,"wb").write(base_blob if base_blob else b"")
    open(hp,"wb").write(head_blob if head_blob else b"")
    mp = os.path.join(WORK, "merged_"+f.replace("/","__"))
    r = subprocess.run(["git","merge-file","-p","--diff3",lp,bp,hp], capture_output=True)
    if r.returncode == 0:
        open(mp,"wb").write(r.stdout)
        results["clean_merge"].append(f); detail[f]="clean-merge"
    else:
        results["conflict"].append((f, "operator-customized"))
        detail[f]="conflict-overlap (merge-file rc=%d)"%r.returncode

for f in ADDED:
    local_exists = os.path.exists(f)
    head_blob = fetch(f, HEAD)
    if local_exists:
        # collision
        local = open(f,"rb").read()
        if sh(local) == sh(head_blob):
            results["skip"].append(f); detail[f]="skip-add-already-present-identical"
        else:
            results["conflict"].append((f,"add-add-collision")); detail[f]="add-collision"
    else:
        open(os.path.join(WORK,"head_"+f.replace("/","__")),"wb").write(head_blob if head_blob else b"")
        results["clean_add"].append(f); detail[f]="clean-add"

print(json.dumps({"results":results,"detail":detail}, indent=1))
