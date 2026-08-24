---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-08-23*
## About This Instance
- **aeon + miroshark war room** — an Aeon run by Aaron (@aaronjmars).
- Job: watch the state of both products, surface who to talk to (BD), generate timing-window ideas.
- North-star + priorities live in `STRATEGY.md` (read every run). Voice lives in `soul/` (Aaron's).

## The two products
- **Aeon ⭐** (@aeonframework, `aeonfun/aeon` canonical — org renamed from `aaronjmars/aeon`, old path 301-redirects) — most autonomous agent framework; skills-as-markdown on GitHub Actions, cron, chains, self-repair, public traces.
- **Miroshark 🦈** (@miroshark_, `MiroShark/MiroShark` canonical — org renamed from `aaronjmars/MiroShark`, old path 301-redirects) — universal swarm simulation engine; hundreds of grounded agents argue on X/Reddit + trade a simulated AMM, belief drift, director mode, ~$1/<10min, x402-native.
- Product config (repos/handles/terms) tracked in `memory/products.md`.
- Watch-list: `666ghj/MiroFish` (71,299★, separate project, near-identical "swarm intelligence engine" positioning to Miroshark) flagged 2026-08-21 for category-intel follow-up.

## War-room skills (this instance)
| Skill | Cadence | Does |
|-------|---------|------|
| bd-radar | odd days 07:20 UTC | who's building/forking/integrating/mentioning → ranked leads + next move |
| mention-radar | even days 07:25 UTC | external web/social mentions — discovery/confusion/friction/competitor taxonomy |
| fetch-tweets | daily 17:00 UTC | X search digest for both products |
| reddit-promo | daily 17:45 UTC | drafts value-first subreddit posts from fetch-tweets stories |
| engagement-act | odd days 09:30 UTC | turns flagged engagement opps into copy-paste-ready replies |
| heartbeat | daily 08:00 UTC | fallback health check + status page |
| aeon-update | Mon 11:00 UTC | pulls framework updates from aeonfun/aeon canon (never dispatched yet — see Next Priorities) |
| memory-flush | Sun 18:00 UTC | this skill |

- bd-radar runs as a **standalone** skill, not a chain (`chain-runner.yml` is brittle under `bash -e`: a transient `gh` non-zero hard-kills the job). **war-room (the 07:45 standup capstone for Aaron) was retired 2026-07-26** and stays retired — this instance is public now, so no private standup. `sim-watch` and `idea-forge` (weekly category-intel/idea skills) are **not currently active** — sim-watch's skill dir is gone entirely; idea-forge exists but is `enabled: false` in `aeon.yml`.

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.
- `chain-runner.yml` runs under `bash -e` → transient `gh` failures hard-kill the job before `on_error:continue`. Prefer staggered standalone skills + committed-file reads over chains.
- Star-count/funding claims seen in the wild (X posts, third-party threads) are frequently wrong or ticker-collisions — always verify against `gh api repos/<owner>/<repo>` before reporting; discard unverified (e.g. 2026-08-20/21's "51,000 stars"/"2.2M stars" claims, both false vs. actual counts). Same rule applies when a third party amplifies *our own* content and adds unverified specifics — e.g. 2026-08-23's MCGlive repost of Aaron's thread added an unverified "running inside companies like SpaceX" detail; reddit-promo correctly used only the organic-amplification signal and omitted the claim itself.
- Sandbox blocks `jq`/`cp`/`rm` against `/tmp` in some runs — write scratch files under the repo working dir via `secretcurl -o` / `Write` instead of `/tmp`; clean up isn't guaranteed (no `rm` in allowlist for read-only skills), so stray untracked files may linger — harmless, not committed.

## Next Priorities
1. ~~`aeon-update` never-dispatched → PR #64~~ **FULLY RESOLVED 2026-08-24:** PR #64 (43 upstream commits `b1d9079..b7a909a`, 79 files) **merged to `main` at 13:08 UTC** — sync watermark now `b7a909a` on `main` (confirmed via `memory/topics/aeon-update-state.json`). Separately, PR #65 (`Egress audit hardening`, opt-in `EGRESS_AUDIT=1`) also merged 14:36 UTC same day. Remaining open item from the sync: **7 conflicts kept local, not yet decided** — notably `skills/heartbeat`, `skills/memory-flush`, `skills/skill-health` SKILL.md vs. upstream's `0776bbb` scorer rewrite (also `.github/workflows/ci-tests.yml`/`messages.yml`, `CHANGELOG.md`, `llms.txt`). Action for Aaron: decide whether to pull the upstream scorer rewrite into the 3 war-room skills. Full list in `memory/topics/aeon-update-state.json` → `pending_conflicts`.
2. Configure a second notification channel (Discord/Slack) if Telegram isn't enough. (Telegram already wired.)
