## Upstream sync: `aeonfun/aeon` `b7a909a..8b8d719`

**25 commits** (2026-08-24 → 2026-08-25) · **50 applied** · **5 manual** · **2 skills deferred** · baseline → `8b8d719`.

The bulk is the **`fx` (Vercel) seventh-harness** rollout, the **`./notify` post-run delivery dispatcher** (#912 Phase 2), **egress-audit hardening**, and CI lint gates (eslint + shellcheck). Most conflicts are your fork-local docs colliding with upstream's "six → seven harnesses" rename and skill-count bumps.

### Applied cleanly
- **Scripts / harness:** `scripts/cron-due.sh`, `scripts/resolve-harness.sh`, `scripts/run-grok.sh`, `scripts/skill-scan.sh`, `scripts/skill_mode.sh`, `scripts/tests/test_cron_due.sh`, `harness-adapter/README.md`
- **Workflows:** `.github/workflows/ci-apps.yml`, `.github/workflows/ci-harnesses-json.yml`
- **Auto-merged (3-way):** `.github/workflows/messages.yml`, `apps/dashboard/lib/skill-icons.data.ts`, `harness-adapter/lib/otel-span.sh`, `harness-adapter/lib/sandbox.sh`  _(your local customization kept; upstream's disjoint changes applied — review the merged hunks)_
- **Apps / dashboard:** `apps/dashboard/{app/api/skills,app/api/upload,lib/constants,lib/gateway,lib/github,lib/harness-auth,lib/secrets-catalog,lib/types,package,package-lock}`, `apps/cli/package.json`, `apps/webhook/{package,package-lock}.json`, `apps/mcp-server/src/skill-executor.ts`
- **New (adds):** `package.json` (root task aggregator), `apps/{cli,dashboard,webhook}/eslint.config.mjs`, `apps/dashboard/lib/github.test.ts`, `plugin/plugin.json`, `plugin/.minimax-plugin/plugin.json`, `plugin/icon.png`, `docs/assets/mcp-logo-400.png`
- **Docs / plugin:** `docs/{CAPABILITIES,ECOSYSTEM,harnesses,mcp-oauth}.md`, `docs/assets/{harnesses-aeon.jpg,hero-animated.svg}`, `plugin/{README,.claude-plugin/plugin.json,skills/aeon/**}`

### 🔒 New skills deferred — need a local `eyebrow` scan (CI would go red without it)
Two brand-new upstream skills were **not** installed this run: the `eyebrow` binary isn't available in the Actions runner, so `eyebrowlock.json` can't be regenerated to cover them, and `ci-skill-integrity` would fail a PR that ships a skill with no lock entry. They arrive as a one-line manual step:

- **`skill-article`** (Basics — turn any skill into a launch article, #945) and **`rightstack`** (web3 advisor, #961).

To land both, on a checkout of this branch run:
```bash
bin/add-skill aeonfun/aeon skill-article
bin/add-skill aeonfun/aeon rightstack
eyebrow scan --path . --lockfile eyebrowlock.json
git add -A && git commit -m "add skill-article + rightstack (eyebrowlock scanned)"
```
(Or fetch the two `skills/<slug>/` dirs from upstream `8b8d719`, then run the `eyebrow scan`.) The upstream `eyebrowlock.json` already carries both entries — they'll regenerate identically.

### Needs manual review (conflicts — your local copy diverges from upstream)
All five are fork-local customizations that overlap upstream's edits, so they weren't auto-applied. In every case the upstream change is the **six → seven harnesses (`fx`)** rename plus skill-count bumps (`75 → 77`); reconcile by hand, keeping your fork's content.

- `.github/README.md` — your fork's README; upstream bumped harness/skill counts (`9ea2a08`, `b494610`, `9e48e6a`).
- `.github/workflows/aeon.yml` — you narrowed the secrets/env block; upstream added the **link-local/metadata egress block** + opt-in **egress-audit (iron-proxy)** steps and a `seven` comment (`90a4d34`, `f72f823`, `0b1dfde`). Worth pulling the two egress hardening steps in by hand.
- `.github/workflows/ci-tests.yml` — carried-forward conflict (operator-customized; upstream's test-matrix changes still unmerged).
- `CHANGELOG.md` — append-region divergence; upstream added the fx / notify-dispatcher / egress entries (`b1d9079..8b8d719`).
- `docs/skill-packs.md` — your fork's pack roster; upstream bumped counts and added `skill-article` + `rightstack` (`3c0ba70`, `846cc73`).
- `llms.txt` — fork-local; upstream changed `six → seven` CLIs (`9e48e6a`, `86ffd45`).

Full upstream diffs for these are in the run output.

### Operator config changed upstream (not auto-applied — reconcile by hand)
- `aeon.yml` — upstream added a **`skill-article`** registry line (`enabled: false` default). Add it if/when you install the skill above; keep your enable/schedule choices.
- `catalog/{skills,packs,skill-icons}.json`, `eyebrowlock.json` — upstream regenerated these for the two new skills. **Not applied** (they regenerate from your synced skill sources); they'll update automatically when you install `skill-article` + `rightstack` and rerun the generators.

### Also (informational — kept as-is)
- `.claude/skills/aeon/**` (SKILL.md + 3 references) modified upstream, but this fork doesn't track that directory — **kept absent**, consistent with prior syncs.
- `skills/deploy-uni-hook/**` modified upstream, but that skill is removed locally (not enabled) — **kept removed**.

### Upstream commits
| SHA | Summary |
|-----|---------|
| 90a4d34 | feat(security): egress audit hardening (iron-proxy), opt-in |
| 3494f2f | Merge #947 security/egress-audit-hardening |
| 360e711 | fix(dashboard): lock aeon.yml read-modify-write to stop config races (#944) |
| df7b57f | fix(dashboard): fx never showed up in the harness picker (#943) |
| 9ea2a08 | docs(ecosystem): add AgentOS (#946) |
| 3a80957 | feat(skills): add skill-article (#945) |
| 3c0ba70 | docs: sync PRs #926-#947 (#948) |
| 4bcc4be | fix(scorer): grade the sent notify card, not the harness .result summary (#949) |
| b494610 | docs: seven-engine harness banner (fx) (#950) |
| f72f823 | fix(secrets): stop binding dead channel creds into every skill run (#951) |
| 9e48e6a | docs: normalize harness count to seven (#952) |
| 6d48d7b | fix(mcp-server): dispatch fx harness (#953) |
| 0b1dfde | feat(notify): move channel delivery to a post-run dispatcher (#955) |
| d0a30a5 | fix(dashboard): capture kimi auth config correctly (#956) |
| 846cc73 | docs: sync PRs #948-#956 (#958) |
| 86ffd45 | docs: fix stale harness/MCP counts (#960) |
| e35fe9c | chore(plugin): prep operator-console plugin for OpenAI submission (#959) |
| e59c52b | fix macos cron date portability (#957) |
| 3da3b73 | add rightstack web3 advisor (#961) |
| d157fcb | style(rightstack): strip em dashes to house-rule hyphens |
| 64790e3 | chore(ci): add eslint + shellcheck lint gates + root task aggregator (#962) |
| 0dd3ebb | chore: silence two shellcheck false positives (#963) |
| faf131b | feat(plugin): Agent Plugins plugin.json + privacy/support for Kiro Powers (#964) |
| c0f671c | Add MiniMax plugin manifest for the aeon operator console (#965) |
| 8b8d719 | Add 400x400 MCP server logo for Cline marketplace listing (#966) |

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
