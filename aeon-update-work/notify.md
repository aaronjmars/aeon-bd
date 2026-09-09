**aeon-update — 2026-09-09**
synced 9 upstream commits → PR [#99](https://github.com/aaronjmars/aeon-bd/pull/99)

11 files applied clean. harness egress + read-only-sandbox fixes (#1038/#1042), competitor-monitor table-row diffing (#1043), the eyebrow-version-from-CI fix for this very skill (#1037). last week's `aeon.yml` conflict finally merges clean — dropped from pending.

one decision for you: **2 new upstream skills — `compute-resell` + `submit-hook` — are NOT auto-installed.** each needs an eyebrowlock entry (binary isn't in the run) + a catalog glyph. deferred rather than ship a red PR. install steps are in the PR body; or just leave them.

12 conflicts still pending (README, CHANGELOG, skill-packs re-hit this run). baseline advances to `c28ab4c` when you merge.