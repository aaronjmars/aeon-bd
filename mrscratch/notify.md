**aeon-update — 2026-08-24**

First real framework sync since setup. 43 upstream commits → **PR #64**.

79 files applied clean. 24 new (Codex plugin, `fx`/Vercel 7th harness, audit log, dry-run gate, reactive+chain evaluators, memory_prep). 10 auto-merged 3-way — your local edits kept.

**7 conflicts, kept your version, need a call:**
- `heartbeat`, `memory-flush`, `skill-health` — collide with upstream's scorer rewrite (#921). Your war-room tuning vs their grading changes.
- `ci-tests.yml`, `messages.yml`, `CHANGELOG.md`, `llms.txt`.

`aeon.yml` untouched — upstream only changed commented docs, no new skills.

One decision: **review + merge PR #64.** Merging advances the sync watermark to `b7a909a`. The 3 skill conflicts are yours to reconcile by hand.

PR: https://github.com/aaronjmars/aeon-bd/pull/64
