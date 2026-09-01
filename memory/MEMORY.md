---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-08-30*
## About This Instance
- **aeon + miroshark war room** — an Aeon run by Aaron (@aaronjmars).
- Job: watch the state of both products, surface who to talk to (BD), generate timing-window ideas.
- North-star + priorities live in `STRATEGY.md` (read every run). Voice lives in `soul/` (Aaron's).

## The two products
- **Aeon ⭐** (@aeonframework, `aeonfun/aeon` canonical — org renamed from `aaronjmars/aeon`, old path 301-redirects) — most autonomous agent framework; skills-as-markdown on GitHub Actions, cron, chains, self-repair, public traces.
- **Miroshark 🦈** (@miroshark_, `MiroShark/MiroShark` canonical — org renamed from `aaronjmars/MiroShark`, old path 301-redirects) — universal swarm simulation engine; hundreds of grounded agents argue on X/Reddit + trade a simulated AMM, belief drift, director mode, ~$1/<10min, x402-native.
- Product config (repos/handles/terms) tracked in `memory/products.md`.
- Watch-list: `666ghj/MiroFish` (71,299★, separate project, near-identical "swarm intelligence engine" positioning to Miroshark) flagged 2026-08-21 for category-intel follow-up.
- Ecosystem highlight: CultOS (@thecultos) built a paid agent entirely on Aeon skills — hireable via x402 for PR evals/repo analysis/audits, publicly declared "we choose Aeon" (2026-08-27, corroborated by a live fork `cultosdev/aeon` + a dedicated pack repo `thesmithdao/cultos-aeon-skills`) — strongest ecosystem-growth proof point of the week; worth a direct check-in, same as Sparkleware (known partner, quietly shipped 7 more Aeon skill repos incl. a registry, 2026-08-27).

## War-room skills (this instance)
| Skill | Cadence | Does |
|-------|---------|------|
| bd-radar | odd days 07:20 UTC | who's building/forking/integrating/mentioning → ranked leads + next move |
| mention-radar | even days 07:25 UTC | external web/social mentions — discovery/confusion/friction/competitor taxonomy |
| fetch-tweets | daily 17:00 UTC | X search digest for both products |
| reddit-promo | daily 17:45 UTC | drafts value-first subreddit posts from fetch-tweets stories |
| engagement-act | odd days 09:30 UTC | turns flagged engagement opps into copy-paste-ready replies |
| heartbeat | daily 08:00 UTC | fallback health check + status page |
| aeon-update | Mon 11:00 UTC | pulls framework updates from aeonfun/aeon canon (active since 08-24; watermark + open conflicts — see Next Priorities) |
| memory-flush | Sun 18:00 UTC | this skill |

- bd-radar runs as a **standalone** skill, not a chain (`chain-runner.yml` is brittle under `bash -e`: a transient `gh` non-zero hard-kills the job). **war-room (the 07:45 standup capstone for Aaron) was retired 2026-07-26** and stays retired — this instance is public now, so no private standup. `sim-watch` and `idea-forge` (weekly category-intel/idea skills) are **not currently active** — sim-watch's skill dir is gone entirely; idea-forge exists but is `enabled: false` in `aeon.yml`.

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.
- `chain-runner.yml` runs under `bash -e` → transient `gh` failures hard-kill the job before `on_error:continue`. Prefer staggered standalone skills + committed-file reads over chains.
- Star-count/funding claims seen in the wild (X posts, third-party threads) are frequently wrong or ticker-collisions — always verify against `gh api repos/<owner>/<repo>` before reporting; discard unverified (e.g. 2026-08-20/21's "51,000 stars"/"2.2M stars" claims, both false vs. actual counts). Same rule applies when a third party amplifies *our own* content and adds unverified specifics — e.g. 2026-08-23's MCGlive repost of Aaron's thread added an unverified "running inside companies like SpaceX" detail; reddit-promo correctly used only the organic-amplification signal and omitted the claim itself.
- Sandbox blocking is session-variable and has widened beyond `jq`/`cp`/`rm`/`/tmp`: some runs also block `>` shell redirection (even to repo-root files, not just `/tmp`) and `${VAR}`-brace expansion / `[ -n "$VAR" ]` presence checks for plain (non-secret) shell vars. Workaround is consistent across all variants: use the `Write` tool for scratch files under the repo working dir (not `/tmp`), skip presence-checks and go straight to the real call (`secretcurl`/`gh api`), and use plain `$VAR` (no braces) when a local var is unavoidable. Stray untracked scratch files may linger (no `rm` in the read-only allowlist) — harmless, not committed.

## Next Priorities
1. **PR #77 open — review + merge:** 34 upstream commits `8b8d719..3b4c5a3` synced (80 files applied, 10 manual). The merge that matters: `scripts/llm-gateway.sh` — our 08-31 incident pin (`04d56d5`, GLM native + effort pinning) vs upstream's own GLM routing (#990 gateway + #998 tiered `GLM_MODEL_*`); recommended take in PR body (upstream's tiering + our effort pinning). Also new: `cortx-reliability` skill, cursor/hermes adapters, api-gate exact-origin fix (#986), notify reply-to-previous (#995). Recovered this run: `rightstack`, `skill-article` (SHA-pinned eyebrow scan worked), `skill-health` 3-way merge. Watermark `3b4c5a3` advances on merge. Remaining conflicts + repo noise: `.aeon-scratch/` and `au-work/` scratch dirs keep landing on `main` via auto-commit — worth a one-line `.gitignore` PR.
2. Configure a second notification channel (Discord/Slack) if Telegram isn't enough. (Telegram already wired.)
