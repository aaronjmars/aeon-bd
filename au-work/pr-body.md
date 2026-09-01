## Upstream sync: `aeonfun/aeon` `8b8d719..3b4c5a3`

**34 commits** (2026-08-26 → 2026-08-31) · **80 applied** (19 added, 57 updated, 4 three-way merged) · **8 manual** · baseline → `3b4c5a3`.

### Applied cleanly
- **New skills:** `cortx-reliability` (x402 endpoint reliability check, #954) — plus **recovered:** `rightstack`, `skill-article`, deferred since 08-25 because the `eyebrow` binary wasn't available to lock them. The pinned v0.4.1 binary downloaded + SHA256-verified this run, so all three are locked in one rescan. _(catalogs + AGENTS.md + skill-icons regenerated)_
- **Modified skills:** `changelog` (em/en-dash scrub, #1000), `skill-repair` (#997)
- **Auto-merged (3-way):** `skills/skill-health/SKILL.md` — **resolves a standing conflict from 08-25**: your scorer customization is kept and upstream's changes (don't auto-resolve an issue when the repair PR is only *opened*, #997; harness-routing support) merged around it. Also `skills/changelog/SKILL.md`, `skills/skill-repair/SKILL.md`, `apps/dashboard/lib/skill-icons.data.ts` (then superseded by regeneration).
- **Scripts / harness:** `scripts/notify-deliver.sh` (bounded telegram chunks + reply-to-previous-run, #970/#995), `notify_format.py`, `secretcurl.sh` (**xAI search retry**, #989), `resolve-harness.sh`, `state_store.sh`, `health_issue.sh`, `install-harness.sh`, `stage-vuln-scanner.sh`, **new** `skill-health-routing.mjs`; harness-adapter: `lib/envelope.sh` (fail on unparseable adapter output, #987), `run-harness`, claude/grok/vibe adapters, `harnesses.json`, **new** `cursor.sh` + `hermes.sh` adapters (#967); 13 test files + `tests/fixtures/curl`
- **Workflows:** `.github/workflows/chain-runner.yml` (#982 fx dispatch + correlation input)
- **Apps:** dashboard — **api-gate exact-origin-match fix** (#986, security), Connect→`GH_GLOBAL` token copy (#993), GitHub-auth lib + tests, harness-picker labels, gateway-registry, secrets-catalog; mcp-server — **async single-flight skill queue** (#973); cli auth
- **Docs / other:** `docs/harnesses.md` (ten-engine banner), `telegram-commands.md` (reply-to-previous), CAPABILITIES/CONFIGURATION/ECOSYSTEM/community-skill-packs/CONTRIBUTING, `plugin/skills/aeon/*` (5 files), assets
- **Regenerated (never copied):** `catalog/skills.json` (62 skills), `catalog/packs.json`, `catalog/skill-icons.json` (+3 glyph lines — see note), `eyebrowlock.json` (64 `discoveredFrom` entries, all three new skills covered; scan findings: 0 critical), `apps/dashboard/lib/skill-icons.data.ts`, 80 skill-icon SVGs. `AGENTS.md` regenerated (no net diff).

> **Note — upstream bug worked around:** upstream added `cortx-reliability` to `catalog/skills.json` but **forgot its glyph** in `catalog/skill-icons.json`, so their own `bin/generate-skill-icons` fails at `3b4c5a3`. This PR adds a placeholder pulse glyph locally; drop it if canon adds one. (`rightstack`/`skill-article` glyph lines adopted verbatim from upstream.)

### Needs manual review (conflicts — your local copy diverges from upstream)
- **`scripts/llm-gateway.sh`** — ⚠️ **the one that matters.** Your 08-31 incident fix (`04d56d5`, native `glm` arm + reasoning-effort pinning, field-verified on api.z.ai) overlaps upstream's own GLM work (#990 `a80f70f` "move GLM from harness to Claude AI Gateway" + #998 `47d1a56` tiered `GLM_MODEL_SONNET/OPUS/HAIKU` mapping). The two are **complementary halves**: upstream brings per-tier model mapping (fast flash for sonnet-tier skills, full model for opus-pinned, fallback `glm-5.2`); yours brings the effort-pinning. Recommended merge: take upstream's tiered `case "${MODEL:-}"` mapping, keep your `CLAUDE_CODE_EFFORT_LEVEL`/`ALWAYS_ENABLE_EFFORT` exports. Upstream diff:
  ```diff
   # Two routing tiers:
  -#   NATIVE (no proxy): bankr, openrouter, usepod, grok  -> set base URL + auth, done.
  +#   NATIVE (no proxy): bankr, openrouter, usepod, grok, glm  -> set base URL + auth, done.
  @@ aeon_present()
       grok)       [ -n "${XAI_API_KEY:-}" ] ;;
  +    glm)        [ -n "${GLM_API_KEY:-${ZAI_API_KEY:-}}" ] ;;
  @@ auto candidates loop
  -  for provider in ${GATEWAY_ORDER:-claude anthropic openrouter bankr usepod venice surplus grok}; do
  +  for provider in ${GATEWAY_ORDER:-claude anthropic openrouter bankr usepod venice surplus grok glm}; do
  +  glm)  # NATIVE — Z.AI's Anthropic-compatible API (Claude Code → api.z.ai)
  +    ... export ANTHROPIC_BASE_URL=...api.z.ai/api/anthropic ...
  +    # Tiered mapping: per-tier var wins over GLM_MODEL; fallback glm-5.2
  +    case "${MODEL:-}" in
  +      *opus*)  glm_model="${GLM_MODEL_OPUS:-${GLM_MODEL:-glm-5.2}}" ;;
  +      *haiku*) glm_model="${GLM_MODEL_HAIKU:-${GLM_MODEL:-glm-5.2}}" ;;
  +      *)       glm_model="${GLM_MODEL_SONNET:-${GLM_MODEL:-glm-5.2}}" ;;
  +    esac
  ```
- **`.github/workflows/messages.yml`** *(new conflict)* — your narrowed env block (dropped `AI_GATEWAY_API_KEY`/`VERCEL_OIDC_TOKEN`, restructured `HOOK_MAINNET_OK`) collides with upstream adding `HERMES_AUTH`/`CURSOR_API_KEY`/`GLM_API_KEY`/`ZAI_API_KEY` to the same blocks (8cc45e4, a80f70f). Easy hand-merge: add the four new keys to your narrowed blocks.
- **`.github/workflows/aeon.yml`** — carryover from 08-25 (your narrowed secrets env / egress-block divergence vs upstream's GLM+CORS+audit work this range). Upstream: 47d1a56, d28801b, a10fd0f, a80f70f, 71fad7a, a59b691, 8cc45e4, 8cff4d0.
- **`.github/workflows/ci-tests.yml`** — upstream added 7 test steps (hermes/cursor adapters, workflow-harness choices, skill-health routing, chain-runner correlation, secretcurl xai retry). Add the new steps to your variant:
  ```diff
  +      - name: hermes adapter tests
  +        run: bash scripts/tests/test_hermes_adapter.sh
  +      - name: cursor adapter tests
  +        run: bash scripts/tests/test_cursor_adapter.sh
  +      - name: workflow harness choice tests
  +        run: bash scripts/tests/test_workflow_harness_choices.sh
  +      - name: skill-health harness routing tests
  +        run: bash scripts/tests/test_skill_health_routing.sh
  +      - name: chain-runner dispatch correlation tests
  +        run: bash scripts/tests/test_chain_runner.sh
  +      - name: secretcurl xai retry tests
  +        run: bash scripts/tests/test_secretcurl_xai_retry.sh
  ```
- **`.github/README.md`** — carryover; upstream added founder credit (#985), eyebrow ecosystem entry (#976), pack listings (#974/#977/#978).
- **`CHANGELOG.md`** — carryover (your append region); upstream added 67 lines through #1000. Append upstream's new entries to your local head.
- **`docs/skill-packs.md`** — carryover; upstream re-titled the pack-membership line (6a03d1c).
- **`llms.txt`** — carryover (fork-local file, upstream added it later); upstream bumped descriptions (bb8211f, a80f70f). Diff yours against upstream's if you want their wording.
- **Still pending from before (upstream untouched this range):** `skills/heartbeat/SKILL.md`, `skills/memory-flush/SKILL.md` — your local variants vs upstream's `0776bbb` scorer rewrite. Reconcile or adopt whenever; they don't block anything.

### Operator config changed upstream (not auto-applied — reconcile by hand)
- **`aeon.yml`** — comments only: the gateway provider list now documents `glm` (priority chain ends `… grok → glm → direct`; "PIN one explicitly" gains `glm`; `glm` = Z.AI Anthropic endpoint via `GLM_API_KEY`/`ZAI_API_KEY`). Your file already pins `gateway.provider: glm`, so nothing functional to merge — optionally sync the comment lines.
- `soul/`, `STRATEGY.md`, `.mcp.json` — unchanged upstream this range.

### Upstream commits
| SHA | Summary |
|-----|---------|
| 8cff4d0 | add machine-readable vuln scanner execution evidence (#968) |
| 8cc45e4 | add cursor hermes and glm harnesses (#967) |
| c648040 | fix(mcp-server): run skills async with a single-flight queue (#973) |
| 252947e | fix: support default repo in macos issue stores (#971) |
| d90a104 | fix dashboard auth rows for new harnesses (#975) |
| 00951ad | fix add-skill commit provenance (#972) |
| 935965d | feat: list CultOS Aeon skill pack (#974) |
| b2238dd | docs: add eyebrow to ecosystem (#976) |
| fa11d48 | fix: bound rendered telegram chunks (#970) |
| 8ea76be | docs: list Farcaster Pack in the community skill-pack registry (#977) |
| a59b691 | add recommend-only harness comparison (#969) |
| af2c44b | Add Spoolis Outcome Gate community pack (#978) |
| 867e4d9 | docs: remove Amper from ecosystem list (#979) |
| bb8211f | docs: sync PRs #957-#979 to aeon docs (#980) |
| fd25871 | docs: re-render ten-engine harness banner (Cursor/Hermes/GLM) (#981) |
| 71fad7a | allow fx workflow dispatches (#982) |
| 6a03d1c | feat: add cortx-reliability skill — x402 endpoint reliability check (#954) |
| 792a880 | trust cursor workspaces in headless runs (#983) |
| 1924c4f | fail hermes runs on api errors (#984) |
| 1a67ffb | Add founder credit and link to aaronjmars.com (#985) |
| e42f963 | fix(dashboard): require exact origin host match (#986) |
| a80f70f | feat: move GLM from harness to Claude AI Gateway (#990) |
| 9d5c519 | teach deploy-uni-hook Labs routing classes (#991) |
| b99d6ae | teach deploy-uni-hook the fleet audit rules (#992) |
| a4e1e1e | style(dashboard): shorten harness picker labels (#994) |
| 4738f27 | feat(dashboard): Connect copies gh token into GH_GLOBAL (#993) |
| a10fd0f | fix(chains): correlate dispatched skill runs uniquely (#988) |
| 8fcce1e | retry transient xai search failures (#989) |
| d28801b | fix(envelope): fail on unparseable adapter output (#987) |
| 6738690 | feat(notify): reply Telegram to previous skill run (#995) |
| bb13088 | docs: Telegram reply-to-previous (#996) |
| 760a809 | don't mark an issue resolved when the repair PR is only opened (#997) |
| 47d1a56 | Add tiered GLM model mapping (GLM_MODEL_SONNET/OPUS/HAIKU) (#998) |
| 3b4c5a3 | fix(changelog-skill): scrub em/en dashes from generated changelog output (#1000) |

*Not tracked here (kept absent/removed, unchanged from prior runs): `.claude/skills/aeon/**` (dir not tracked in this fork), `skills/deploy-uni-hook/**` (removed locally, not enabled — upstream taught it Labs routing + fleet audit rules this range).*
