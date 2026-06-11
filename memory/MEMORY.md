# Long-term Memory
*Last consolidated: 2026-06-11*

## About This Instance
- **aeon + miroshark war room** — a shared Aeon run by Aaron (@aaronjmars) + coworker Nurstar.
- Job: watch the state of both products, surface who to talk to (BD), generate timing-window ideas.
- North-star + priorities live in `STRATEGY.md` (read every run). Voice lives in `soul/` (Aaron's).

## The two products
- **Aeon ⭐** (@aeonframework, `aaronjmars/aeon`) — most autonomous agent framework; skills-as-markdown on GitHub Actions, cron, chains, self-repair, public traces.
- **Miroshark 🦈** (@miroshark_, `aaronjmars/MiroShark`) — universal swarm simulation engine; hundreds of grounded agents argue on X/Reddit + trade a simulated AMM, belief drift, director mode, ~$1/<10min, x402-native.
- Repo families + handles tracked in `memory/watched-repos.md`.

## War-room skills (this instance)
| Skill | Cadence | Does |
|-------|---------|------|
| product-pulse | daily (chain) | state of both products — repo-family health + X deltas |
| bd-radar | daily (chain) | who's building/forking/integrating/mentioning → ranked leads + next move |
| war-room | daily (chain) | the standup brief — state · talk-to · decide — for Aaron + Nurstar |
| sim-watch | Tue weekly | Miroshark category intel — sim competitors, papers, clones |
| idea-forge | Fri weekly | business-idea engine — zeitgeist × capabilities → scored wedges |

- Daily `war-room` **chain** (in `aeon.yml`) is the single switch: product-pulse + bd-radar (parallel) → war-room. Currently `enabled: false` / chain defined but pending notification-channel setup.

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.

## Next Priorities
1. Configure a notification channel (Telegram / Discord / Slack secret) so the war-room brief can send.
2. Dry-run product-pulse + bd-radar (`var: dry-run`) to seed state files, then enable the war-room chain.
3. Tune schedules + lead-scoring after the first week of real output.
