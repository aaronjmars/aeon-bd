---
type: Article
title: AI Framework Watch — 2026-07-14
description: Weekly competitive-intelligence digest on the AI agent framework space — momentum, releases, breaking changes across 9 tracked frameworks.
tags: [framework-watch, agents, ai, weekly]
timestamp: 2026-07-14T00:00:00Z
---

# AI Framework Watch — 2026-07-14

**Verdict:** RELEASE WEEK: 5 frameworks shipped — aeon ⭐, langgraph, crewai, mastra, pydantic-ai

**Tracked:** 9 of 9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

---

## Ranked table

*(Sorted by 7d star delta — anchor pinned top regardless of delta)*

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|------:|-----:|------:|:-------------:|:---------:|---------|
| aaronjmars/aeon | 574 | +4 | +60 | 1 | — | v0.1.0 — first public release |
| langchain-ai/langgraph | 37,263 | +587 | +2,356 | 2 | — | 1.2.9 + cli 0.4.31 — steady weekly cadence |
| crewAIInc/crewAI | 55,490 | +433 | +1,817 | 1 | — | 1.15.2 stable point release |
| mastra-ai/mastra | 26,149 | +258 | +1,026 | 1 | — | @mastra/core@1.50.0 — weekly TypeScript cadence |
| pydantic/pydantic-ai | 18,504 | +250 | +723 | 5 | — | v2.9.0/v2.9.1 + legacy v1.107.1 — dual-track active |
| stanfordnlp/dspy | 36,114 | +215 | +1,054 | 0 | — | — |
| microsoft/autogen | 59,720 | +172 | +726 | 0 | — | — (10 months release-dark) |
| run-llama/llama_index | 50,831 | +130 | +665 | 0 | — | — |
| huggingface/smolagents | 28,343 | +112 | +461 | 0 | — | — |

---

## Releases (7-day window: 2026-07-07 → 2026-07-14)

### aaronjmars/aeon
- **v0.1.0** (2026-07-09) — First public GitHub release. Announces the framework's skills-as-markdown, self-repair, and 197-skill architecture to the ecosystem. This is the anchor tagging itself.

### langchain-ai/langgraph
- **langgraph==1.2.9** (2026-07-10) — Incremental stability patch; changes since 1.2.8.
- **langgraph-cli==0.4.31** (2026-07-10) — CLI tooling patch; changes since 0.4.30.

### crewAIInc/crewAI
- **1.15.2** (2026-07-08) — Stable point release (What's Changed format; prior 1.15.2 pre-releases absorbed).

### mastra-ai/mastra
- **@mastra/core@1.50.0** (2026-07-08) — Weekly release covering July 6, 2026 highlights. Mastra's TypeScript cadence remains the most consistent in the cohort — ~1 minor per week.

### pydantic/pydantic-ai
- **v2.9.1** (2026-07-14) — Patch on v2.9.0; auto-generated release notes.
- **v2.9.0** (2026-07-11) — Minor release on the v2 track.
- **v1.107.1** (2026-07-11) — Legacy v1 track maintenance (parallel to v2 line). Pydantic AI is now maintaining dual release tracks — v2.x as the active development line and v1.x as a stability branch. This is the clearest signal yet that they're treating v2 as production-stable rather than experimental.
- **v2.8.0** (2026-07-10) — Minor feature release on v2 track.
- **v2.7.0** (2026-07-09) — Minor feature release on v2 track.

---

## Anchor position

aeon shipped its first public GitHub release this week — v0.1.0, tagged 2026-07-09. For context: the framework has been running live, self-repairing, and fielding hundreds of forks since before this watch log started, but v0.1.0 is the first formal release artifact. Stars at 574, +4 in 7 days — smallest absolute weekly delta in the cohort, which is expected for a framework whose growth comes from builder DMs and ecosystem compounding rather than viral library mentions. The anchor sits 9/9 in the ranked table by 7d delta, but it's the only framework in the cohort that tagged itself for the first time this week. Six other forks pushed code in the same window (bd-radar 07-07); the star number undercounts the signal.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 0`
