ℹ️ aeon-update: PR #91

*aeon-update — 2026-09-07* ⭐

synced 7 upstream commits → PR #91. 14 files landed clean, 3 need your call.

clean: dry-run explicit model selection, dev-loop verified-review receipts, send-email bounce preflight (`check_email_bounces.py`) + 5 tests. `pr-review` & `send-email` auto-merged 3-way — your fork edits kept. last week's `pr-review` conflict resolved itself.

manual (3):
- `aeon.yml` — upstream adds `RESEND_API_KEY` inject; only matters if you enable send-email
- `ci-tests.yml` — two new test steps; the test files they call already landed clean here
- `vuln-scanner` SKILL — bounded trufflehog scan vs our simplified fork; skill's disabled anyway

baseline moves to `21b82db` on merge. 11 old conflicts still parked.

PR: https://github.com/aaronjmars/aeon-bd/pull/91

🔗 https://github.com/aaronjmars/aeon-bd/pull/91