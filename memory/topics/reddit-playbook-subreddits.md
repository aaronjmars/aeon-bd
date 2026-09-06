---
type: Reference
title: "reddit-playbook-subreddits"
---

# Reddit Playbook targets (tiered)

Config for the `reddit-playbook` skill. Tiers are from measured moderation outcomes
(54 posts across two accounts, ~294k views, Aug 2026). The skill picks a **content
archetype** (A news-hook / B question / C milestone / D contrarian / E observer) by
story type, then routes to a sub by tier. If this file is missing the skill falls
back to the built-in tiers in its SKILL.md.

Sibling of the older `reddit-subreddits.md` (used by `reddit-promo`). Both skills
share the dedup file `memory/reddit-promo-seen.txt` so they never double-post a story.

## Canonical / product links (one per post, at the bottom, after value)

| token | URL |
|-------|-----|
| repo | https://github.com/aeonfun/aeon |
| site | https://aeon.fun |
| miroshark | https://github.com/miroshark/miroshark |
| xpost | the source tweet URL for the story (from the fetch-tweets output) |

Omit the product link entirely in no-link subs. Every checkable claim in the body
links to a THIRD-PARTY source (issue tracker, commit, dashboard, original post),
never to our own site - that is what keeps observer-style posts through moderation.

## Submit links (one-click post)

`https://www.reddit.com/r/<name>/submit?title=<url-encoded title>`
(`<name>` without the `r/`; title percent-encoded. Old-reddit: swap host for
`https://old.reddit.com`. The operator pastes the drafted body.)

## Green - post any archetype (A-E)

| subreddit | link | notes |
|-----------|------|-------|
| r/artificial | xpost | Biggest single-post reach in the data (102k). News-hook or question leads. |
| r/ArtificialInteligence | site | Milestone-with-a-number does well (17k). |
| r/LLMDevs | repo | Technical; news-hook commentary on the agent/LLM stack. |
| r/AI_Agents | repo | Agent-framework readers; autonomy axis. |
| r/AgentsOfAI | repo | Agent audience; observer/report framing survives well. |
| r/AIAgentsInAction | repo | Agent builders; show a real mechanic. |
| r/coolgithubprojects | repo | Strict title: "Aeon - <one-line desc>". Show-the-repo. |
| r/automation | site | "What do you all use to automate X?" question framing. |
| r/nocode | site | Keep jargon low; set-and-forget angle. |
| r/ethdev | repo | Only with a genuine onchain/dev hook; technical framing, not token framing. |
| r/googlecloud | xpost | Observer report with vendor-tracker receipts (survived here). |
| r/cursor | repo | Coding-agent crowd; skills-as-markdown mechanic. |
| r/nvidia | xpost | Only on a real hardware/AI news hook. |
| r/OpenSourceAI | repo | Open-source (AGPL) + skills-as-markdown; show, don't sell. |
| r/footballtactics | xpost | Miroshark: domain question ("beating xG by 30, luck or finishing?" - 66k). |
| r/EventMarkets | xpost | Miroshark prediction-market angle. |
| r/PredictionMarkets | xpost | Miroshark; analytical, not promotional. |
| r/sportsanalytics | xpost | Miroshark simulation-as-analysis. |
| r/Kalshi | xpost | Miroshark; market-native framing. |

## Question-only - Archetype B framing only (a direct promo is removed)

| subreddit | link | notes |
|-----------|------|-------|
| r/ClaudeCode | repo | Removed a direct post; a pure question held. Ask, don't announce. |
| r/Polymarket | xpost | Question framing only; no product in title. |

## Comment-only - place comments, never posts (12/12 post removals here)

r/programming, r/devsecops, r/cybersecurity, r/vibecoding, r/aiagents,
r/LovingOpenSourceAI, r/homelab, r/soccer, r/dataisbeautiful. Value-first comment,
link only if asked in-thread. Zero comment removals in three weeks of data.

## Known trap

Crypto-framed titles were removed where the technical framing of the same story held.
For a Miroshark/onchain story going to a general or tech sub, frame it as
agents/simulation/tooling, never tokens.
