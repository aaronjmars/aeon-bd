
### aeon-update
- status: AEON_UPDATE_OK — PR #68 opened. Upstream `aeonfun/aeon` `b7a909a..8b8d719`, 25 commits (2026-08-24→08-25), 84 files in delta.
- applied cleanly (50): 9 added, 37 updated, 4 auto-merged 3-way (`messages.yml`, `skill-icons.data.ts`, `otel-span.sh`, `sandbox.sh`). 16 files SKIPped (already present/synced — egress-audit + notify-dispatcher already in fork).
- deferred (2 new skills): `rightstack`, `skill-article` — eyebrow binary unavailable in runner, so `eyebrowlock.json` can't be regenerated; `ci-skill-integrity` would go red. Surfaced as `needs-eyebrowlock-scan` with a one-line install+scan step in the PR.
- conflicts (5, manual): `.github/README.md`, `.github/workflows/aeon.yml` (upstream added link-local/metadata egress block + iron-proxy audit — worth pulling by hand), `CHANGELOG.md`, `docs/skill-packs.md`, `llms.txt`. Mostly fork-local docs vs upstream six→seven harness (fx) rename + skill-count bumps.
- carried pending re-verified, still divergent: `ci-tests.yml`, `heartbeat`/`memory-flush`/`skill-health` SKILL.md. Prior `messages.yml` conflict RESOLVED this run (now auto-merges).
- informational (kept as-is): `.claude/skills/aeon/**` not tracked in fork (kept absent); `skills/deploy-uni-hook/**` removed locally (kept removed).
- operator config surfaced not applied: `aeon.yml` (+skill-article registry line), `catalog/*.json` + `eyebrowlock.json` (regenerate on skill install).
- Baseline advances to `8b8d719` only when PR #68 merges (state committed to branch). Sandbox note: `bin/generate-*` and binary exec blocked by permission layer this run — fail-safe path taken.
- Notification sent: yes. PR: https://github.com/aaronjmars/aeon-bd/pull/68
