#!/usr/bin/env python3
import os, shutil

WORK = ".aeon-work"

# CLEAN-ADD + CLEAN-UPDATE: write HEAD blob (fetched into .aeon-work/head/)
head_writes = [
    # CLEAN-ADD (new, non-skill / dev-loop harness)
    ".github/workflows/ci-gate.yml",
    "scripts/dev-loop-proof.sh",
    "scripts/dev-loop-repair.sh",
    "scripts/tests/test_dev_loop_proof.sh",
    "scripts/tests/test_dev_loop_repair.sh",
    "scripts/tests/test_idea_pipeline_dev_loop_offer.sh",
    # CLEAN-UPDATE (operator never touched)
    ".github/workflows/chain-runner.yml",
    "apps/dashboard/app/api/mcp-auth/callback/route.ts",
    "apps/mcp-server/src/skill-executor.ts",
    "docs/ECOSYSTEM.md",
    "harness-adapter/adapters/codex.sh",
    "plugin/skills/aeon/SKILL.md",
    "plugin/skills/aeon/references/layout.md",
    "plugin/skills/aeon/references/mcp.md",
    "plugin/skills/aeon/references/skill-anatomy.md",
    "scripts/dev-loop-pr.sh",
    "scripts/dev-loop-review.sh",
    "scripts/install-harness.sh",
    "scripts/resolve-riva-capabilities.sh",
    "scripts/run-grok.sh",
    "scripts/skill_mode.sh",
    "scripts/telegram-route.sh",
    "scripts/tests/test_chain_runner_no_action.sh",
    "scripts/tests/test_dev_loop_handoff.sh",
    "scripts/tests/test_dev_loop_review.sh",
    "scripts/tests/test_run_grok.sh",
    "scripts/tests/test_telegram_route.sh",
    "skills/aeon-update/SKILL.md",
]

# CLEAN-MERGE: write merged output (.aeon-work/merged/)
merge_writes = [
    ".github/workflows/aeon.yml",
    "skills/changelog/SKILL.md",
    "skills/feature/SKILL.md",
]

def safe(p):
    return p.replace("/", "_")

exec_bit = (".sh",)

for p in head_writes:
    src = f"{WORK}/head/{safe(p)}"
    if not os.path.exists(src):
        print(f"!! MISSING HEAD BLOB {p}")
        continue
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    shutil.copy(src, p)
    if p.endswith(exec_bit):
        os.chmod(p, 0o755)
    print(f"WROTE-HEAD  {p}")

for p in merge_writes:
    src = f"{WORK}/merged/{safe(p)}"
    if not os.path.exists(src):
        print(f"!! MISSING MERGED {p}")
        continue
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    shutil.copy(src, p)
    print(f"WROTE-MERGE {p}")

print("apply done")
