# Watched Repos

Repos the monitoring skills sweep. `builder-map`, `bd-radar`, and `product-pulse`
read this file. Public repos drive "who's building on top" (default `gh api`);
private product repos are read via the read-only `GH_READ_PAT` prefetch
(`scripts/prefetch-private-repos.sh` → `.xai-cache/private-repos.json`) for the
internal health view — never expose their contents.

| Repo | Keywords | Notes |
|------|----------|-------|
| aaronjmars/aeon | aeon, "aeon framework", aeonframework, "just aeon it" | ⭐ flagship — most autonomous agent framework |
| aaronjmars/MiroShark | miroshark, "swarm intelligence", "simulate anything" | 🦈 universal swarm simulation engine |
| aaronjmars/aeon-agent | aeon-agent | public automation of aeon (verifiable runs) |
| aaronjmars/miroshark-aeon | miroshark-aeon | public automation of miroshark |
| aaronjmars/minitor | minitor | monitor-anything product (an Aeon product) |
| aaronjmars/soul-aaronjmars | soul.md, "soul file", "ai soul" | the soul framework this instance runs on |

## Private product repos (read-only, via `GH_READ_PAT` prefetch — never expose contents)
In the PAT's scope → monitored by product-pulse:
- aaronjmars/aeon-website — ⭐ aeon marketing site
- aaronjmars/aeon-wc — ⭐ private aeon repo
- aaronjmars/miroshark-website — 🦈 marketing site
- aaronjmars/MiroShark-x402 — 🦈 x402 payments layer

Out of the PAT's scope → not monitored (add them to the fine-grained PAT to include):
- aaronjmars/MiroShark-api — API to run MiroShark
- aaronjmars/miroshark-x — X bot, runs sims from @mentions

## Social handles
- @aeonframework (Aeon) ⭐
- @miroshark_ (Miroshark) 🦈
- @aaronjmars (operator)
