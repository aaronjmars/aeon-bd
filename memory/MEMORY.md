---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-06-11*

## About This Instance
- **aeon + miroshark war room** — an Aeon run by Aaron (@aaronjmars).
- Job: watch the state of both products, surface who to talk to (BD), generate timing-window ideas.
- North-star + priorities live in `STRATEGY.md` (read every run). Voice lives in `soul/` (Aaron's).

## The two products
- **Aeon ⭐** (@aeonframework, `aaronjmars/aeon`) — most autonomous agent framework; skills-as-markdown on GitHub Actions, cron, chains, self-repair, public traces.
- **Miroshark 🦈** (@miroshark_, `aaronjmars/MiroShark`) — universal swarm simulation engine; hundreds of grounded agents argue on X/Reddit + trade a simulated AMM, belief drift, director mode, ~$1/<10min, x402-native.
- Repo families + handles tracked in `memory/watched-repos.md`.

## War-room skills (this instance)
| Skill | Cadence | Does |
|-------|---------|------|
| bd-radar | daily 07:20 | who's building/forking/integrating/mentioning → ranked leads + next move |
| sim-watch | Sun weekly | Miroshark category intel — sim competitors, papers, clones |
| idea-forge | Wed weekly | business-idea engine — zeitgeist × capabilities → scored wedges |

- bd-radar runs as a **standalone daily skill** (07:20), not a chain (`chain-runner.yml` is brittle under `bash -e`: a transient `gh` non-zero hard-kills the job). **war-room (the 07:45 standup capstone for Aaron) was retired 2026-07-26** - its skill files are gone and this instance is now public, so the private standup is not re-added; treat any "war-room missing" drift alarm as expected, not a regression. (product-pulse retired 2026-07.)

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.
- `chain-runner.yml` runs under `bash -e` → transient `gh` failures hard-kill the job before `on_error:continue`. Prefer staggered standalone skills + committed-file reads over chains.

## Next Priorities
1. Tune schedules + lead-scoring after the first week of real output.
3. Configure a second notification channel (Discord/Slack) if Telegram isn't enough. (Telegram already wired.)
