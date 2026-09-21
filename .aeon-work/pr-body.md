## Upstream sync: `aeonfun/aeon` `95142d1..ba01e9f`

**19 commits** (2026-09-14 → 2026-09-18) · **31 applied** · **8 manual** · baseline → `ba01e9f`.

The window is upstream's **dev-loop** stack (proof-gated feature→review→repair loop), a new **sc-audit** smart-contract skill, security hardening (MCP OAuth XSS, Riva shadow-mode, vuln-scanner disclosure routing), and an always-on **CI Gate** aggregator. Everything that doesn't collide with this fork's narrowing was applied; the rest is surfaced below.

### Applied cleanly (31)
- **New (6):** `.github/workflows/ci-gate.yml` (aggregates path-filtered checks into one required status), `scripts/dev-loop-proof.sh`, `scripts/dev-loop-repair.sh`, `scripts/tests/test_dev_loop_proof.sh`, `scripts/tests/test_dev_loop_repair.sh`, `scripts/tests/test_idea_pipeline_dev_loop_offer.sh`.
- **Scripts / harness (updated):** `scripts/dev-loop-pr.sh`, `scripts/dev-loop-review.sh`, `scripts/install-harness.sh`, `scripts/resolve-riva-capabilities.sh`, `scripts/run-grok.sh`, `scripts/skill_mode.sh`, `scripts/telegram-route.sh`, `harness-adapter/adapters/codex.sh`, + tests (`test_chain_runner_no_action.sh`, `test_dev_loop_handoff.sh`, `test_dev_loop_review.sh`, `test_run_grok.sh`, `test_telegram_route.sh`).
- **Workflows:** `.github/workflows/chain-runner.yml` (routes a `[dev-loop::ship]` Telegram reply into the dev-loop chain).
- **Apps:** `apps/dashboard/app/api/mcp-auth/callback/route.ts` (escape OAuth callback HTML — reflected-XSS fix, #1066), `apps/mcp-server/src/skill-executor.ts` (Riva shadow-mode isolation on the MCP dispatch path, #1067).
- **Skill (updated):** `skills/aeon-update/SKILL.md` (extends the eyebrow fail-safe to prose-only edits of skills with pinned findings — the recurring red-PR fix; applied to this very run).
- **Auto-merged (3-way):** `.github/workflows/aeon.yml`, `skills/changelog/SKILL.md`, `skills/feature/SKILL.md` _(your local customization kept; upstream's disjoint changes applied — review the merged hunks)_.
- **Docs / plugin:** `docs/ECOSYSTEM.md` (refresh HivemindOS avatar, drop dead Spoon row), `plugin/skills/aeon/**` (4 files — the fork's `/aeon` setup-skill mirror).

### Needs manual review (conflicts — your local copy diverges from upstream)
Fork-narrowed files where the same regions changed on both sides. Your version is untouched; reconcile by hand.

- **`skills/idea-pipeline/SKILL.md`** _(new this run)_ — upstream added a `dev-loop offer:` entry point + renamed the log heading to `### idea-pipeline` (`73f660e`). Conflicts with the fork's flat frontmatter (`type: Skill`, inline `tags:`) and `## Idea Pipeline` heading. Take upstream's body edits, keep the fork's frontmatter shape.
- **`skills/vuln-scanner/SKILL.md`** — upstream hardened disclosure routing (SECURITY.md-first, PVR preflight) + rephrased curl-pipe mentions to clear the eyebrow RCE gate (`bdc2532`, `554097c`). The fork runs a simplified copy; skill is `enabled: false` here.
- **`.github/workflows/ci-tests.yml`** — upstream added dev-loop proof/repair + idea-pipeline-offer test steps (`094c10d`, `1d183dc`, `73f660e`). The referenced test files were synced clean; only the workflow wiring conflicts with the fork's narrowed test list.
- **`.github/README.md`** / **`docs/skill-packs.md`** / **`CHANGELOG.md`** — upstream doc/catalog churn (sc-audit rows, +90-line changelog append) overlapping the fork's narrowed README/pack tables and diverged changelog tail.

### New upstream skills — deferred (need an eyebrow scan to land green)
`ci-skill-integrity`'s coverage gate fails any `skills/<slug>/SKILL.md` with no `eyebrowlock.json` entry, and that entry is only produced by the `eyebrow` binary (not preinstalled in this run). So brand-new skills are surfaced, not auto-added, to keep the PR CI-green. To adopt either, from a clean checkout:

```
# (also add a glyph to catalog/skill-icons.json for the icon'd ones, then:)
eyebrow scan --path . --lockfile eyebrowlock.json
git add skills/<slug> eyebrowlock.json && git commit
```

- **`sc-audit`** (`#1072`, `1dbbfd9` + `554097c`) — deep smart-contract audit (Slither best-effort + agentic invariant/access-control/oracle pass + optional Echidna/Medusa fuzz), Opus-pinned. Ships with `fixtures/vault/`, `references/hook-checklist.md`, `scripts/stage-sc-audit.sh`, and its glyph SVG — **all deferred as one unit**. Needs a glyph in `catalog/skill-icons.json` + a lock entry. **Product-relevant** to this war room (Uniswap-hook security is a live BD thread) — worth adopting. `aeon.yml` upstream also gained an `sc-audit:` registry line (`enabled:false`, `workflow_dispatch`) — operator-owned, not written here.
- **`create-prove`** (`#1075`, `1d183dc`) — the dev-loop's behavioral-proof sub-skill (invoked directly by the chain, not scheduled → no glyph needed, just a lock entry).

### Operator config changed upstream (not auto-applied — reconcile by hand)
- **`aeon.yml`** — upstream added the `sc-audit` registry line (above) and bumped the `dev-loop` chain `max_dispatches` 2→5. Merge if you want them; your enable/schedule/model choices are preserved.
- **`catalog/*.json`, `eyebrowlock.json`** — upstream bumped counts/glyphs/lock for the new skills. Kept the fork's narrowed versions (regenerate-not-copy); no new slug entered the fork's catalog this run, so the drift gates stay green.
- **`.claude/skills/aeon/**`** — this fork doesn't carry the `/aeon` setup skill (`.gitignore` un-ignores it, but it was never committed here). Upstream's 4-file edit kept absent; the parallel `plugin/skills/aeon/**` copy WAS synced.

### Carried-forward conflicts (unchanged this window)
`.github/workflows/messages.yml`, `.github/dependabot.yml`, `llms.txt`, `skills/heartbeat/SKILL.md`, `skills/memory-flush/SKILL.md`, `skills/compute-resell/`, `skills/submit-hook/`, `skills/miroshark-matchday/` (upstream added a 9:16 render path this window; still absent locally).

### Upstream commits
| SHA | Summary |
|-----|---------|
| 38f0f88 | fix: close two aeon-update/changelog gaps that land sync PRs CI-red |
| 7e53f56 | fix(grok): don't claim auth staged after a failed oauth refresh |
| 030f646 | docs: sync PRs #1042-#1061 to aeon docs |
| 09dd581 | docs: add #1060 to changelog and correct skill-lead count |
| 2e9efdb | feat(miroshark-matchday): vertical 9:16 render path in the local video step |
| 172ae1c | ci: add always-on CI Gate to aggregate path-filtered checks |
| 5b08c24 | fix(dashboard): escape MCP OAuth callback HTML to prevent reflected XSS |
| f6546e9 | fix(mcp-server): close Riva shadow-mode isolation gap on the MCP dispatch path |
| bdc2532 | fix(vuln-scanner): rephrase curl-pipe-to-shell mentions to clear the eyebrow RCE gate |
| 7a7b98a | fix(feature): scope Aeon watermark to dev-loop test runs only |
| 094c10d | feat(dev-loop): add one verified repair pass |
| c5eaf63 | fix(ecosystem): refresh HivemindOS avatar, drop dead Spoon row |
| 1dbbfd9 | feat(sc-audit): add smart-contract audit skill |
| 554097c | feat(vuln-scanner): harden disclosure routing (A5.0 SECURITY.md-first, A5b.0 PVR preflight) |
| c2624e1 | docs: sync PRs #1062-#1073 to aeon docs |
| 1d183dc | feat(dev-loop): require live behavioral proof, not just review |
| 8fa449a | feat(telegram): route a [dev-loop::ship] reply into chain-runner.yml |
| 73f660e | feat(idea-pipeline): offer: entry point for dev-loop targets |
| ba01e9f | fix(dev-loop): close proof-guard gaps from the dev-loop PR stack |

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
