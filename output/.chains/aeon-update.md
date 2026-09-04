ℹ️ aeon-update: 22 commits → PR #89

**aeon-update — 2026-09-04**
synced 22 upstream commits → PR #89. 27 files applied clean, 12 need your eyes.

the one that matters: **the GLM-gateway conflict is dead.** last week's headache — our incident pin vs upstream's own routing — resolved itself now #77 landed. upstream's new effort-pin was already in our copy. merge was a no-op.

other clean 3-ways: eyebrow gate v0.4.2, feature + skill-health body updates. new PoC-gate scripts + tests for vuln-scanner.

manual (low urgency — 4 of the conflicting skills are disabled here):
- `dependabot.yml` — you already applied the same holds, only a comment differs. skip it.
- workflow env blocks (aeon/ci-tests/messages) — upstream added `GLM_REASONING_EFFORT` + the block-style `model:` scheduler fix (#1024). that fix doesn't affect us — our model overrides are single-line.
- pr-review + vuln-scanner — disabled skills, deep divergence. take upstream if you ever enable them.

watermark advances to `bf33365` on merge.

PR: https://github.com/aaronjmars/aeon-bd/pull/89

🔗 https://github.com/aaronjmars/aeon-bd/pull/89