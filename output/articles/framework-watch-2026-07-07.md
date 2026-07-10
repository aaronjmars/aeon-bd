---
type: Article
---

# AI Framework Watch — 2026-07-07

**Verdict:** RELEASE WEEK: 4 frameworks shipped — langgraph, crewai (pre), mastra, pydantic-ai

**Tracked:** 9 of 9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

---

## Ranked table

(Sorted by `star_delta_7d` desc · anchor pinned top · 7d window = 2026-06-30 → 2026-07-07)

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|-------|------|-------|---------------|-----------|----------|
| aaronjmars/aeon | 570 | +10 | +56 | — | — | — |
| langchain-ai/langgraph | 36,676 | +555 | +1,769 | 1 | — | Patch: bug fixes since 1.2.7 |
| crewAIInc/crewAI | 55,057 | +445 | +1,384 | 1 [PRE] | — | 1.15.2a2 alpha pre-release |
| mastra-ai/mastra | 25,891 | +284 | +768 | 3 | — | Three drops: 1.47.0 → 1.49.0 |
| stanfordnlp/dspy | 35,899 | +231 | +839 | — | — | — |
| microsoft/autogen | 59,548 | +175 | +554 | — | — | — |
| run-llama/llama_index | 50,701 | +170 | +535 | — | — | — |
| pydantic/pydantic-ai | 18,254 | +160 | +473 | 5 | — | v2.2.0 → v2.5.1: 5 releases in 7d |
| huggingface/smolagents | 28,231 | +123 | +349 | — | — | — |

*30d Δ uses 2026-06-16 baseline (21d ago — carries forward until 30d threshold reached).*

---

## Releases (7-day window)

### langchain-ai/langgraph
- **1.2.8** (2026-07-06) — Bug fixes since 1.2.7. Steady weekly patch cadence continues.

### crewAIInc/crewAI
- **1.15.2a2** (2026-07-01) [PRE] — Pre-release alpha; 1.15.1 stable shipped June 27.
- **1.15.2a1** (2026-06-30) [PRE] — Alpha precursor to 1.15.2.

### mastra-ai/mastra
- **@mastra/core@1.49.0** (2026-07-07) — July 3 feature drop; highlights not surfaced in first line.
- **@mastra/core@1.48.0** (2026-07-01) — July 1 feature drop.
- **@mastra/core@1.47.0** (2026-07-01) — June 26 feature drop (published July 1).

### pydantic/pydantic-ai
- **v2.5.1** (2026-07-07) — Patch on top of v2.5.0.
- **v2.5.0** (2026-07-04) — Minor feature release; part of rapid July iteration cycle.
- **v2.4.0** (2026-07-03) — Minor feature release.
- **v2.3.0** (2026-07-02) — Minor feature release.
- **v2.2.0** (2026-07-01) — Kicked off the week's release sprint.

---

## Anchor position

aeon sits at +10 stars this week vs. the cohort range of +123 (smolagents) to +555 (langgraph). No releases — consistent with the no-versioned-release pattern (the last recorded release date is null). Star pace is modest but steady: +56 over the 21-day window. Top-of-cohort by stars-per-line-of-code is not the game aeon plays — but it's the only framework in the table running on GitHub Actions natively, zero infra, purely markdown-defined skills. apples and oranges. the cohort ships library versions; aeon ships cron runs.

---

## Notable signals

**pydantic-ai velocity:** 5 releases in 7 days (v2.2.0 → v2.5.1) is an unusual sprint. Issue count dropped 138 in the same window (644 → 506) — suggests the sprint closed a significant backlog rather than pure feature adds. No breaking markers in release headers; changelog bodies not surfaced. Worth reading if you're on pydantic-ai.

**autogen drift:** Last release was python-v0.7.5 on 2025-09-30 — over 9 months ago. Repo still gets commits (`pushed_at` 2026-04-15) but no versioned releases. Either shipping under a different cadence model or in holding pattern. The 921 open issues (+6 this week) suggest it's not abandoned, just not packaging.

**dspy quiet period:** No release since 3.3.0b1 (2026-05-28, pre-release) and 3.2.1 (2026-05-05 stable). Steady star growth (+231 7d) without releases = organic demand, not launch-driven.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 0`
