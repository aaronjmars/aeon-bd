## Upstream sync: `aeonfun/aeon` `21b82db..c28ab4c`

**9 commits** (2026-09-07 → 2026-09-09) · **11 applied** · **12 manual** · baseline → `c28ab4c`.

### Applied cleanly
- **Harness / egress:** `harness-adapter/lib/sandbox.sh` — stop iron-proxy MITM from redding artifact uploads (#1038) + keep `memory/` and `output/` writable in the read-only sandbox (#1042).
- **Scripts:** `scripts/competitor-monitor.mjs` — opt-in table-row diffing for list pages (#1043); `scripts/stage-deploy-uni-hook.sh`.
- **Skills (content):** `skills/aeon-update/SKILL.md` — derive eyebrow version from CI so sync PRs stop going red (#1037); `skills/competitor-monitor/SKILL.md` — table-row diffing (#1043).
- **Plugin skill copy:** `plugin/skills/aeon/SKILL.md` + 3 references (doc sync #1041).
- **Auto-merged (3-way):**
  - `.github/workflows/aeon.yml` — _your env-block narrowing kept; upstream's egress/expression edits applied to disjoint regions. Re-validated: YAML parses + `validate-config.js` PASS. This clears last week's `aeon.yml` conflict._
  - `skills/changelog/SKILL.md` — _your customization kept; upstream's disjoint edits merged._

### Needs manual review — new upstream skills not auto-installed
Two brand-new upstream skills were **deferred**, per the S7 fail-safe (never ship a red PR). Each needs two operator steps before it can land, so they are surfaced instead of half-installed:

- **`compute-resell`** (#1036, `3f3509c`) — multi-provider compute reselling on the Surplus marketplace.
- **`submit-hook`** (#1040, `0154c0e`) — publish a Uniswap v4 hook to the marketplace.

To install either one manually:
1. `bin/add-skill aeonfun/aeon <skill>` (or copy `skills/<skill>/` from upstream) — this also adds the `catalog/skill-icons.json` glyph the generator needs.
2. `eyebrow scan --path . --lockfile eyebrowlock.json` then `bin/generate-skills-json && bin/generate-packs-json && bin/generate-skill-icons`, and commit. (The `eyebrow` binary isn't preinstalled in the sync run, so the lock entry can't be produced here — this is the one step that keeps CI green.)
3. Enable it in `aeon.yml` when you want it scheduled (it ships `enabled: false`).

### Needs manual review (conflicts — your local copy diverges from upstream)
Your fork has customized these; upstream changed the same regions, so they weren't auto-applied. All carried forward in `memory/topics/aeon-update-state.json`:

- `.github/README.md` — doc sync (#1041, `63078b4`) + eyebrow-version note (`44ddb43`) overlap your fork's README edits.
- `CHANGELOG.md` — upstream changelog appends (`f96beb9`, `63078b4`) overlap your append region.
- `docs/skill-packs.md` — upstream added `compute-resell` + `submit-hook` rows and bumped the pack counts (`3f3509c`, `0154c0e`); overlaps your narrowed pack tables. (Resolves naturally once the two skills above are installed + catalogs regenerated.)
- `.github/workflows/ci-tests.yml`, `.github/workflows/messages.yml`, `.github/dependabot.yml`, `llms.txt`, `skills/heartbeat/SKILL.md`, `skills/memory-flush/SKILL.md`, `skills/vuln-scanner/SKILL.md` — unchanged upstream this run; still divergent from prior syncs, listed for completeness.

### Operator config changed upstream (not auto-applied — reconcile by hand)
- `aeon.yml` — upstream added one skill entry: `compute-resell: { enabled: false, schedule: "15 6,14,18 * * *", var: "" }` (crypto pack). Merge it if/when you install the skill; your enable/schedule/model choices are otherwise untouched.
- `catalog/skills.json` / `catalog/packs.json` / `catalog/skill-icons.json` / `eyebrowlock.json` — regenerated from local sources, never copied. No regen was needed this run: the skill *set* is unchanged and all catalog-relevant frontmatter is identical (only body text changed), so `ci-skills-json`/`ci-packs-json` (which ignore per-skill `sha`/`updated`) stay green.

### Kept absent (informational — not tracked in this fork)
- `.claude/skills/aeon/**` — the `.claude/` bundled skill copy isn't carried here (you ship `plugin/skills/aeon/`, which was synced clean). Upstream's doc-sync edits skipped.
- `skills/deploy-uni-hook/**` — AeonFee.sol + template changes (#1035, `487b23f`); skill dir isn't tracked locally (not enabled) — kept absent, consistent with prior runs.

### Upstream commits
| SHA | Summary |
|-----|---------|
| `f96beb9` | docs(changelog): run site formatter after edit so format:check passes (#1034) |
| `487b23f` | feat(deploy-uni-hook): enforce the mandatory 10 bps AeonFee on every deployed hook (#1035) |
| `3f3509c` | feat(skills): add compute-resell — multi-provider compute reselling on Surplus (#1036) |
| `162bf20` | fix(egress): stop iron-proxy MITM from redding artifact uploads (#1038) |
| `44ddb43` | fix(aeon-update): derive eyebrow version from CI so sync PRs stop going red (#1037) |
| `0154c0e` | Port submit-hook marketplace publish to canon (#1040) |
| `63078b4` | docs: sync PRs #1034-#1040 to aeon docs (#1041) |
| `51ccf0c` | fix(harness): keep memory/ and output/ writable in read-only sandbox (#1042) |
| `c28ab4c` | feat(competitor-monitor): opt-in table-row diffing for list pages (#1043) |

🤖 Generated with [Claude Code](https://claude.com/claude-code)
