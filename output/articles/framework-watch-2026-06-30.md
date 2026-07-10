---
type: Article
---

# AI Framework Watch — 2026-06-30

**Verdict:** BREAKING WEEK: 1 framework shipped breaking releases — pydantic-ai (v1→v2 major)

**Tracked:** 9 of 9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

---

## Ranked table

Anchor pinned top; remainder sorted by 7d star delta desc. 30d Δ not yet available (baseline <21 days old).

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|-------|------|-------|---------------|-----------|----------|
| aaronjmars/aeon | 560 | +17 | — | 0 | — | — |
| langchain-ai/langgraph | 36,121 | +622 | — | 1 | — | 1.2.7 — patch on main line |
| crewAIInc/crewAI | 54,612 | +405 | — | 5 | — | 1.15.1 stable — 1.14→1.15 minor bump landed |
| stanfordnlp/dspy | 35,668 | +351 | — | 0 | — | — |
| mastra-ai/mastra | 25,607 | +253 | — | 1 | — | @mastra/core@1.46.0 — Highlights |
| run-llama/llama_index | 50,531 | +224 | — | 1 | — | v0.14.23 — Release Notes |
| microsoft/autogen | 59,373 | +190 | — | 0 | — | — |
| pydantic/pydantic-ai | 18,094 | +167 | — | 3 | [BREAKING] | v2.0.0 — Pydantic AI V2.0 is here! (v1→v2) |
| huggingface/smolagents | 28,108 | +131 | — | 0 | — | — |

---

## Releases (7-day window)

### pydantic/pydantic-ai
- **v2.1.1** (2026-06-30) — Auto-generated patch on the v2 line.
- **v2.1.0** (2026-06-29) — Feature release on the v2 line.
- **v2.0.0** (2026-06-23) [BREAKING] — "🎉 Pydantic AI V2.0 is here!" — major version bump from v1→v2; prior stable was v1.107.0. Review the v2 migration guide before upgrading.

### langchain-ai/langgraph
- **1.2.7** (2026-06-30) — Changes since 1.2.6.

### crewAIInc/crewAI
- **1.15.1** (2026-06-27) — Stable follow-up to 1.15.0.
- **1.15.1a1** (2026-06-26) [PRE] — Pre-release test build.
- **1.15.0** (2026-06-25) — New minor version; first stable 1.15.x. Body: "What's Changed" (no explicit breaking markers; 1.14→1.15 minor bump — review changelog).
- **1.14.8a5** (2026-06-25) [PRE] — Pre-release build.
- **1.14.8a4** (2026-06-24) [PRE] — Pre-release build.

### run-llama/llama_index
- **v0.14.23** (2026-06-24) — Release Notes (first llamaindex release since v0.14.22 on 2026-05-14 — 40-day gap).

### mastra-ai/mastra
- **@mastra/core@1.46.0** (2026-06-24) — Highlights (weekly cadence continuing).

---

## Anchor position

aeon: 560 stars (+17 this week, 9th by 7d delta in the cohort). No formal releases — repo pushed 2026-06-29. Forks ticked from 188→196, open issues 2→3. The weekly delta gap vs. langgraph (+622) and crewai (+405) is a size story — those repos have 60–90× more stars. Relative to its stage, aeon is tracking steadily. The story this week isn't aeon's star count; it's that pydantic-ai just shipped v2 while aeon's skills already handle type-safe agent patterns without the framework dependency.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 1`
