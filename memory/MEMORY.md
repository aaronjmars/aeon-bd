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
| product-pulse | daily 07:15 | state of both products — repo-family health + X deltas |
| bd-radar | daily 07:20 | who's building/forking/integrating/mentioning → ranked leads + next move |
| war-room | daily 07:45 | the standup brief — state · talk-to · decide — for Aaron + Nurstar |
| sim-watch | Sun weekly | Miroshark category intel — sim competitors, papers, clones |
| idea-forge | Wed weekly | business-idea engine — zeitgeist × capabilities → scored wedges |

- The war room runs as **3 staggered standalone daily skills** (07:15 → 07:20 → 07:45), NOT a chain — `chain-runner.yml` is brittle under `bash -e` (a transient `gh` non-zero hard-kills the job before `on_error:continue` reaches the capstone). war-room reads the morning's committed product-pulse + bd-radar digests. All live + `enabled: true`.

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.
- `chain-runner.yml` runs under `bash -e` → transient `gh` failures hard-kill the job before `on_error:continue`. Prefer staggered standalone skills + committed-file reads over chains.
- X data on the runner: use the xAI prefetch cache (`scripts/prefetch-xai.sh` → `.xai-cache/`), not x-mcp (x-mcp is local-only). product-pulse reads `.xai-cache/product-pulse-x.json`.
- The runner's `GITHUB_TOKEN` only covers `aeon-nur`; private MiroShark repos 404 until a PAT (`repo` scope) is added.

## Next Priorities
1. **Private MiroShark repos** — add a PAT secret (`repo` scope) so product-pulse/bd-radar can read the 4 private repos, or accept public-only. (Pending operator call.)
2. Tune schedules + lead-scoring after the first week of real output.
3. Configure a second notification channel (Discord/Slack) if Telegram isn't enough. (Telegram already wired.)
