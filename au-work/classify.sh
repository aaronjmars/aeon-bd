#!/usr/bin/env bash
# aeon-update S6: 3-way classify every changed file (baseline 8b8d719 -> head 3b4c5a3)
BASE=8b8d719715ec9bb68fb858a1e334d23209047d82
HEAD=3b4c5a3ff1d9846530e02ed5e6796a4a409d2674
W="$(mktemp -d)"
OUT="$PWD/au-work/classification.tsv"
: > "$OUT"

sha() { sha256sum 2>/dev/null | cut -d' ' -f1; }

# status|filename  (renames would carry previous_filename after a second |)
LIST='modified|.claude/skills/aeon/SKILL.md|INFO-untracked-dir
modified|.claude/skills/aeon/references/layout.md|INFO-untracked-dir
modified|.claude/skills/aeon/references/mcp.md|INFO-untracked-dir
modified|.claude/skills/aeon/references/secrets.md|INFO-untracked-dir
modified|.claude/skills/aeon/references/skill-anatomy.md|INFO-untracked-dir
modified|.github/CONTRIBUTING.md|
modified|.github/README.md|
modified|.github/workflows/aeon.yml|
modified|.github/workflows/chain-runner.yml|
modified|.github/workflows/ci-tests.yml|
modified|.github/workflows/messages.yml|
modified|CHANGELOG.md|
modified|aeon.yml|OPERATOR
modified|apps/cli/src/commands/auth.ts|
modified|apps/cli/src/index.ts|
added|apps/dashboard/app/api/github-auth/route.ts|
modified|apps/dashboard/app/page.tsx|
modified|apps/dashboard/components/AuthModal.tsx|
modified|apps/dashboard/components/GrokAuthModal.tsx|
modified|apps/dashboard/components/HarnessAuthModal.tsx|
modified|apps/dashboard/components/SecretsPanel.tsx|
modified|apps/dashboard/lib/constants.ts|
modified|apps/dashboard/lib/gateway-registry.ts|
added|apps/dashboard/lib/github-auth.test.ts|
added|apps/dashboard/lib/github-auth.ts|
added|apps/dashboard/lib/harness-auth.test.ts|
modified|apps/dashboard/lib/harness-auth.ts|
modified|apps/dashboard/lib/secrets-catalog.ts|
modified|apps/dashboard/lib/security/api-gate.test.ts|
modified|apps/dashboard/lib/security/api-gate.ts|
modified|apps/dashboard/lib/service-icon.test.ts|
modified|apps/dashboard/lib/service-icons.ts|
modified|apps/dashboard/lib/skill-icons.data.ts|
modified|apps/dashboard/lib/types.ts|
modified|apps/mcp-server/src/index.ts|
modified|apps/mcp-server/src/skill-executor.ts|
modified|bin/add-skill|
modified|catalog/packs.json|OPERATOR
modified|catalog/skill-icons.json|OPERATOR
modified|catalog/skill-packs.json|OPERATOR
modified|catalog/skills.json|OPERATOR
modified|docs/CAPABILITIES.md|
modified|docs/CONFIGURATION.md|
modified|docs/ECOSYSTEM.md|
modified|docs/assets/harnesses-aeon.jpg|
modified|docs/assets/hero-animated.svg|
added|docs/assets/skill-icons/rightstack.svg|
modified|docs/community-skill-packs.md|
modified|docs/harnesses.md|
modified|docs/skill-packs.md|
modified|docs/telegram-commands.md|
modified|eyebrowlock.json|OPERATOR
modified|harness-adapter/README.md|
modified|harness-adapter/adapters/claude.sh|
added|harness-adapter/adapters/cursor.sh|
modified|harness-adapter/adapters/grok.sh|
added|harness-adapter/adapters/hermes.sh|
modified|harness-adapter/adapters/vibe.sh|
modified|harness-adapter/harnesses.json|
modified|harness-adapter/lib/envelope.sh|
modified|harness-adapter/run-harness|
modified|llms.txt|
modified|plugin/skills/aeon/SKILL.md|
modified|plugin/skills/aeon/references/layout.md|
modified|plugin/skills/aeon/references/mcp.md|
modified|plugin/skills/aeon/references/secrets.md|
modified|plugin/skills/aeon/references/skill-anatomy.md|
modified|scripts/health_issue.sh|
modified|scripts/install-harness.sh|
modified|scripts/llm-gateway.sh|
modified|scripts/notify-deliver.sh|
modified|scripts/notify_format.py|
modified|scripts/resolve-harness.sh|
modified|scripts/secretcurl.sh|
added|scripts/skill-health-routing.mjs|
modified|scripts/stage-vuln-scanner.sh|
modified|scripts/state_store.sh|
added|scripts/tests/fixtures/curl|
added|scripts/tests/test_chain_runner.sh|
modified|scripts/tests/test_community_skill_install.sh|
added|scripts/tests/test_cursor_adapter.sh|
modified|scripts/tests/test_generate_harnesses_json.sh|
modified|scripts/tests/test_harness_envelope.sh|
modified|scripts/tests/test_health_issue.sh|
added|scripts/tests/test_hermes_adapter.sh|
modified|scripts/tests/test_notify.sh|
modified|scripts/tests/test_notify_format.py|
modified|scripts/tests/test_resolve_harness.sh|
added|scripts/tests/test_secretcurl_xai_retry.sh|
added|scripts/tests/test_skill_health_routing.sh|
modified|scripts/tests/test_state_store.sh|
added|scripts/tests/test_workflow_harness_choices.sh|
modified|skills/changelog/SKILL.md|
added|skills/cortx-reliability/SKILL.md|
modified|skills/deploy-uni-hook/SKILL.md|INFO-removed-locally
modified|skills/deploy-uni-hook/hook-deploy.sh|INFO-removed-locally
modified|skills/deploy-uni-hook/templates/DeployHook.s.sol|INFO-removed-locally
modified|skills/deploy-uni-hook/templates/DynamicFeeHook.sol|INFO-removed-locally
modified|skills/deploy-uni-hook/templates/Hook.sol|INFO-removed-locally
modified|skills/deploy-uni-hook/templates/HookFeeHook.sol|INFO-removed-locally
modified|skills/deploy-uni-hook/templates/NoOpHook.sol|INFO-removed-locally
modified|skills/skill-health/SKILL.md|
modified|skills/skill-repair/SKILL.md|'

echo "$LIST" | while IFS='|' read -r st f tag; do
  [ -z "$f" ] && continue
  if [ "$tag" = "OPERATOR" ]; then
    printf '%s\t%s\tOPERATOR\n' "$st" "$f" >> "$OUT"; continue
  fi
  if [ "$tag" = "INFO-untracked-dir" ]; then
    printf '%s\t%s\tINFO-KEPT-ABSENT (dir not tracked in this fork)\n' "$st" "$f" >> "$OUT"; continue
  fi
  if [ "$tag" = "INFO-removed-locally" ]; then
    printf '%s\t%s\tINFO-KEPT-REMOVED (skill removed locally, not enabled)\n' "$st" "$f" >> "$OUT"; continue
  fi

  git show "$BASE:$f" > "$W/base" 2>/dev/null; base_rc=$?
  git show "$HEAD:$f" > "$W/uhead" 2>/dev/null; head_rc=$?
  if [ -e "$f" ]; then loc_rc=0; cp "$f" "$W/local"; else loc_rc=1; fi
  SHA_LOC=$([ $loc_rc -eq 0 ] && sha < "$W/local" || echo ABSENT)
  SHA_BASE=$([ $base_rc -eq 0 ] && sha < "$W/base" || echo ABSENT)
  SHA_HEAD=$([ $head_rc -eq 0 ] && sha < "$W/uhead" || echo ABSENT)

  case "$st" in
    added)
      if [ "$SHA_LOC" = "ABSENT" ]; then disp="CLEAN-ADD"
      else disp="CONFLICT"; reason="add-add collision (fork-local file exists)"; fi ;;
    modified)
      if [ "$SHA_LOC" = "$SHA_HEAD" ]; then disp="SKIP"; reason="already synced"
      elif [ "$SHA_LOC" = "$SHA_BASE" ]; then disp="CLEAN-UPDATE"
      elif [ "$SHA_LOC" = "ABSENT" ]; then disp="INFO-KEPT-ABSENT (path not tracked locally)"
      else
        if git merge-file -p --diff3 "$W/local" "$W/base" "$W/uhead" > "$W/merged" 2>/dev/null; then
          disp="CLEAN-MERGE"; cp "$W/merged" "$W/merge-$RANDOM"; mkdir -p "$PWD/au-work/merges"
          cp "$W/merged" "$PWD/au-work/merges/$(echo "$f" | tr '/' '_')"
        else
          disp="CONFLICT"; reason="operator-customized + overlapping upstream hunks"
        fi ;;
      fi ;;
    removed)
      if [ "$SHA_LOC" = "ABSENT" ]; then disp="SKIP"; reason="already gone"
      elif [ "$SHA_LOC" = "$SHA_BASE" ]; then disp="CLEAN-DELETE"
      else disp="CONFLICT"; reason="operator-customized vs upstream delete"; fi ;;
  esac
  if [ -n "${reason:-}" ]; then
    printf '%s\t%s\t%s\t%s\tloc=%s base=%s head=%s\n' "$st" "$f" "$disp" "$reason" "${SHA_LOC:0:12}" "${SHA_BASE:0:12}" "${SHA_HEAD:0:12}" >> "$OUT"
  else
    printf '%s\t%s\t%s\t\tloc=%s base=%s head=%s\n' "$st" "$f" "$disp" "${SHA_LOC:0:12}" "${SHA_BASE:0:12}" "${SHA_HEAD:0:12}" >> "$OUT"
  fi
  reason=""
done
echo "done -> $OUT"
grep -c . "$OUT"
