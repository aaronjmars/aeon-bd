Committed. Now the final output message as required by CLAUDE.md — must carry the substance, not just a pointer.

## memory-flush — 2026-08-22

**Promoted to MEMORY.md:**
- Fixed stale canonical repo names in "The two products": `aaronjmars/aeon` → `aeonfun/aeon`, `aaronjmars/MiroShark` → `MiroShark/MiroShark` (org renames surfaced by bd-radar 2026-08-21, old paths just 301-redirect). Also fixed a broken reference to a nonexistent `memory/watched-repos.md` → correct file is `memory/products.md`.
- Rewrote the "War-room skills" table, which was badly out of date (last touched 2026-06-11): it listed `sim-watch` (skill directory no longer exists — fully retired) and `idea-forge` as active weekly skills, but `idea-forge` is `enabled: false` in `aeon.yml` and `sim-watch` isn't there at all. Replaced with the 8 skills actually running today: bd-radar, mention-radar, fetch-tweets, reddit-promo, engagement-act, heartbeat, aeon-update, memory-flush — with real cadences pulled from `aeon.yml`.
- Added `666ghj/MiroFish` (71,299★ competitor with near-identical positioning to Miroshark, flagged by bd-radar 2026-08-21) to a new watch-list line.
- Added two Lessons Learned: (1) star-count/funding claims from X threads are frequently wrong or ticker-collisions — verify against `gh api` before reporting (two false claims caught 2026-08-20/21: "51,000 stars", "2.2M stars"); (2) sandbox blocks `jq`/`cp`/`rm` against `/tmp` in some runs — write scratch files to the repo working dir instead (from mention-radar 2026-08-22).
- Refreshed Next Priorities: dropped the stale "tune schedules after first week" (odd/even day cadences are already live and working), added investigating `aeon-update`, which heartbeat has flagged three days running as never-dispatched (`last_run: null` in `aeon-update-state.json` despite being enabled weekly).

**Pruned:** checked for an "Open Improvement PRs" section — none existed, and `gh pr list`/`gh issue list` both return empty, so nothing to remove there.

**Result:** MEMORY.md is 44 lines (within the ~50-line budget), committed as `e37a22e`.

## Summary
- Modified `memory/MEMORY.md` (repo names, skills table, lessons, priorities) and `memory/logs/2026-08-22.md` (flush log entry).
- Committed directly to `main` (memory-only change, not code).
- Follow-up: someone should look at why `aeon-update` has never dispatched despite being enabled weekly — that's now the top Next Priority.
