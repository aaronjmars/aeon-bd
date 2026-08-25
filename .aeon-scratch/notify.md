**aeon-update — 2026-08-25**
synced 25 upstream commits → [PR #68](https://github.com/aaronjmars/aeon-bd/pull/68)

`aeonfun/aeon` `b7a909a..8b8d719`. 50 files applied clean (9 add, 37 update, 4 auto-merged 3-way). Baseline moves to `8b8d719` on merge.

headline: **fx** is the 7th harness now (Vercel). notify moved behind a post-run delivery dispatcher. egress-audit hardening + eslint/shellcheck CI gates.

two calls for you:
- **`aeon.yml`** conflict — upstream added a link-local/metadata **egress block** to the run workflow. worth grabbing by hand.
- **2 new skills deferred** (`skill-article`, `rightstack`) — eyebrow binary isn't in the runner, so shipping them would redden `ci-skill-integrity`. one-line install+scan in the PR when you want them.

5 manual conflicts total, all fork-local docs vs the six→seven rename. prior `messages.yml` conflict auto-resolved this run.
