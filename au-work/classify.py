#!/usr/bin/env python3
"""aeon-update S6: 3-way classify every changed file (baseline 8b8d719 -> head 3b4c5a3)."""
import hashlib, os, subprocess, sys

BASE = "8b8d719715ec9bb68fb858a1e334d23209047d82"
HEAD = "3b4c5a3ff1d9846530e02ed5e6796a4a409d2674"
ROOT = os.getcwd()
MERGE_DIR = os.path.join(ROOT, "au-work", "merges")
os.makedirs(MERGE_DIR, exist_ok=True)

def run(args, **kw):
    return subprocess.run(args, capture_output=True, **kw)

def blob(rev, path):
    r = run(["git", "show", f"{rev}:{path}"])
    return r.stdout if r.returncode == 0 else None

def sha(data):
    return hashlib.sha256(data).hexdigest() if data is not None else "ABSENT"

# (status, filename, tag)
FILES = [
    ("modified", ".claude/skills/aeon/SKILL.md", "INFO-untracked-dir"),
    ("modified", ".claude/skills/aeon/references/layout.md", "INFO-untracked-dir"),
    ("modified", ".claude/skills/aeon/references/mcp.md", "INFO-untracked-dir"),
    ("modified", ".claude/skills/aeon/references/secrets.md", "INFO-untracked-dir"),
    ("modified", ".claude/skills/aeon/references/skill-anatomy.md", "INFO-untracked-dir"),
    ("modified", ".github/CONTRIBUTING.md", ""),
    ("modified", ".github/README.md", ""),
    ("modified", ".github/workflows/aeon.yml", ""),
    ("modified", ".github/workflows/chain-runner.yml", ""),
    ("modified", ".github/workflows/ci-tests.yml", ""),
    ("modified", ".github/workflows/messages.yml", ""),
    ("modified", "CHANGELOG.md", ""),
    ("modified", "aeon.yml", "OPERATOR"),
    ("modified", "apps/cli/src/commands/auth.ts", ""),
    ("modified", "apps/cli/src/index.ts", ""),
    ("added", "apps/dashboard/app/api/github-auth/route.ts", ""),
    ("modified", "apps/dashboard/app/page.tsx", ""),
    ("modified", "apps/dashboard/components/AuthModal.tsx", ""),
    ("modified", "apps/dashboard/components/GrokAuthModal.tsx", ""),
    ("modified", "apps/dashboard/components/HarnessAuthModal.tsx", ""),
    ("modified", "apps/dashboard/components/SecretsPanel.tsx", ""),
    ("modified", "apps/dashboard/lib/constants.ts", ""),
    ("modified", "apps/dashboard/lib/gateway-registry.ts", ""),
    ("added", "apps/dashboard/lib/github-auth.test.ts", ""),
    ("added", "apps/dashboard/lib/github-auth.ts", ""),
    ("added", "apps/dashboard/lib/harness-auth.test.ts", ""),
    ("modified", "apps/dashboard/lib/harness-auth.ts", ""),
    ("modified", "apps/dashboard/lib/secrets-catalog.ts", ""),
    ("modified", "apps/dashboard/lib/security/api-gate.test.ts", ""),
    ("modified", "apps/dashboard/lib/security/api-gate.ts", ""),
    ("modified", "apps/dashboard/lib/service-icon.test.ts", ""),
    ("modified", "apps/dashboard/lib/service-icons.ts", ""),
    ("modified", "apps/dashboard/lib/skill-icons.data.ts", ""),
    ("modified", "apps/dashboard/lib/types.ts", ""),
    ("modified", "apps/mcp-server/src/index.ts", ""),
    ("modified", "apps/mcp-server/src/skill-executor.ts", ""),
    ("modified", "bin/add-skill", ""),
    ("modified", "catalog/packs.json", "OPERATOR"),
    ("modified", "catalog/skill-icons.json", "OPERATOR"),
    ("modified", "catalog/skill-packs.json", "OPERATOR"),
    ("modified", "catalog/skills.json", "OPERATOR"),
    ("modified", "docs/CAPABILITIES.md", ""),
    ("modified", "docs/CONFIGURATION.md", ""),
    ("modified", "docs/ECOSYSTEM.md", ""),
    ("modified", "docs/assets/harnesses-aeon.jpg", ""),
    ("modified", "docs/assets/hero-animated.svg", ""),
    ("added", "docs/assets/skill-icons/rightstack.svg", ""),
    ("modified", "docs/community-skill-packs.md", ""),
    ("modified", "docs/harnesses.md", ""),
    ("modified", "docs/skill-packs.md", ""),
    ("modified", "docs/telegram-commands.md", ""),
    ("modified", "eyebrowlock.json", "OPERATOR"),
    ("modified", "harness-adapter/README.md", ""),
    ("modified", "harness-adapter/adapters/claude.sh", ""),
    ("added", "harness-adapter/adapters/cursor.sh", ""),
    ("modified", "harness-adapter/adapters/grok.sh", ""),
    ("added", "harness-adapter/adapters/hermes.sh", ""),
    ("modified", "harness-adapter/adapters/vibe.sh", ""),
    ("modified", "harness-adapter/harnesses.json", ""),
    ("modified", "harness-adapter/lib/envelope.sh", ""),
    ("modified", "harness-adapter/run-harness", ""),
    ("modified", "llms.txt", ""),
    ("modified", "plugin/skills/aeon/SKILL.md", ""),
    ("modified", "plugin/skills/aeon/references/layout.md", ""),
    ("modified", "plugin/skills/aeon/references/mcp.md", ""),
    ("modified", "plugin/skills/aeon/references/secrets.md", ""),
    ("modified", "plugin/skills/aeon/references/skill-anatomy.md", ""),
    ("modified", "scripts/health_issue.sh", ""),
    ("modified", "scripts/install-harness.sh", ""),
    ("modified", "scripts/llm-gateway.sh", ""),
    ("modified", "scripts/notify-deliver.sh", ""),
    ("modified", "scripts/notify_format.py", ""),
    ("modified", "scripts/resolve-harness.sh", ""),
    ("modified", "scripts/secretcurl.sh", ""),
    ("added", "scripts/skill-health-routing.mjs", ""),
    ("modified", "scripts/stage-vuln-scanner.sh", ""),
    ("modified", "scripts/state_store.sh", ""),
    ("added", "scripts/tests/fixtures/curl", ""),
    ("added", "scripts/tests/test_chain_runner.sh", ""),
    ("modified", "scripts/tests/test_community_skill_install.sh", ""),
    ("added", "scripts/tests/test_cursor_adapter.sh", ""),
    ("modified", "scripts/tests/test_generate_harnesses_json.sh", ""),
    ("modified", "scripts/tests/test_harness_envelope.sh", ""),
    ("modified", "scripts/tests/test_health_issue.sh", ""),
    ("added", "scripts/tests/test_hermes_adapter.sh", ""),
    ("modified", "scripts/tests/test_notify.sh", ""),
    ("modified", "scripts/tests/test_notify_format.py", ""),
    ("modified", "scripts/tests/test_resolve_harness.sh", ""),
    ("added", "scripts/tests/test_secretcurl_xai_retry.sh", ""),
    ("added", "scripts/tests/test_skill_health_routing.sh", ""),
    ("modified", "scripts/tests/test_state_store.sh", ""),
    ("added", "scripts/tests/test_workflow_harness_choices.sh", ""),
    ("modified", "skills/changelog/SKILL.md", ""),
    ("added", "skills/cortx-reliability/SKILL.md", ""),
    ("modified", "skills/deploy-uni-hook/SKILL.md", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/hook-deploy.sh", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/templates/DeployHook.s.sol", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/templates/DynamicFeeHook.sol", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/templates/Hook.sol", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/templates/HookFeeHook.sol", "INFO-removed-locally"),
    ("modified", "skills/deploy-uni-hook/templates/NoOpHook.sol", "INFO-removed-locally"),
    ("modified", "skills/skill-health/SKILL.md", ""),
    ("modified", "skills/skill-repair/SKILL.md", ""),
]

def merge3(local: bytes, base: bytes, uhead: bytes):
    """Real 3-way via git merge-file. Returns (clean, merged_bytes)."""
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p_local = os.path.join(td, "local"); p_base = os.path.join(td, "base")
        p_head = os.path.join(td, "head"); p_out = os.path.join(td, "out")
        for p, data in ((p_local, local), (p_base, base), (p_head, uhead)):
            with open(p, "wb") as fh: fh.write(data)
        r = run(["git", "merge-file", "-p", "--diff3", p_local, p_base, p_head])
        merged = r.stdout
        if r.returncode == 0:
            return True, merged
        return False, merged  # returncode>0 => conflicts; stdout has markers

rows = []
for st, f, tag in FILES:
    if tag == "OPERATOR":
        rows.append((st, f, "OPERATOR", "")); continue
    if tag:
        rows.append((st, f, "INFO-" + tag, "")); continue

    lp = os.path.join(ROOT, f)
    local = open(lp, "rb").read() if os.path.exists(lp) else None
    s_loc, s_base, s_head = sha(local), sha(blob(BASE, f)), sha(blob(HEAD, f))

    if st == "added":
        disp = "CLEAN-ADD" if local is None else "CONFLICT"
        reason = "" if local is None else "add-add collision (fork-local file exists)"
    elif st == "modified":
        if s_loc == s_head:   disp, reason = "SKIP", "already synced"
        elif s_loc == s_base: disp, reason = "CLEAN-UPDATE", ""
        elif local is None:   disp, reason = "INFO-KEPT-ABSENT", "path not tracked locally"
        else:
            clean, merged = merge3(local, blob(BASE, f), blob(HEAD, f))
            if clean:
                disp, reason = "CLEAN-MERGE", ""
                with open(os.path.join(MERGE_DIR, f.replace("/", "_")), "wb") as fh:
                    fh.write(merged)
            else:
                disp, reason = "CONFLICT", "operator-customized + overlapping upstream hunks"
    else:  # removed
        if local is None:   disp, reason = "SKIP", "already gone"
        elif s_loc == s_base: disp, reason = "CLEAN-DELETE", ""
        else:               disp, reason = "CONFLICT", "operator-customized vs upstream delete"
    rows.append((st, f, disp, reason))

with open(os.path.join(ROOT, "au-work", "classification.tsv"), "w") as out:
    for st, f, disp, reason in rows:
        out.write(f"{st}\t{f}\t{disp}\t{reason}\n")

from collections import Counter
for k, v in sorted(Counter(r[2] for r in rows).items()):
    print(f"{v:3d}  {k}")
print("---")
for st, f, disp, reason in rows:
    if disp in ("CONFLICT", "OPERATOR", "SKIP") or disp.startswith("INFO"):
        print(f"{disp:28s} {f}  {reason}")
