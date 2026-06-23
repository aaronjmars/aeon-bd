# AI Framework Watch — 2026-06-23

**Verdict:** RELEASE WEEK: 3 frameworks shipped — langgraph, crewai, mastra

**Tracked:** 9/9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

---

## Ranked table

*(Anchor pinned top · rest sorted by 7d star delta desc · 30d Δ unlocks at run-5, 2026-07-21+)*

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|-------|------|-------|---------------|-----------|---------|
| aaronjmars/aeon | 543 | +29 | — | 0 | — | Pushed 2026-06-22; no tagged release this week |
| langchain-ai/langgraph | 35,499 | +592 | — | 2 | — | Fixes nested subgraph checkpoint_ns regression; v3 stream abort cancel |
| crewAIInc/crewAI | 54,207 | +534 | — | 3 [PRE] | — | Alpha 1.14.8: single-agent actions in Flows, CEL validation at load |
| stanfordnlp/dspy | 35,317 | +257 | — | 0 | — | — |
| mastra-ai/mastra | 25,354 | +231 | — | 1 | — | Faster long-thread resume; improved state signal handling |
| microsoft/autogen | 59,183 | +189 | — | 0 | — | Last tagged release: Sep 2025 (9 months ago) |
| pydantic/pydantic-ai | 17,927 | +146 | — | 0 | — | v2 beta series ongoing (v2.0.0b7, Jun 10) |
| run-llama/llama_index | 50,307 | +141 | — | 0 | — | Last release: v0.14.22, May 14 |
| huggingface/smolagents | 27,977 | +95 | — | 0 | — | Last release: v1.26.0, May 29 |

---

## Releases (7-day window: 2026-06-16 → 2026-06-23)

### langchain-ai/langgraph
- **1.2.6** (2026-06-18) — Fixes nested subgraph checkpoint_ns regression introduced in 1.2.3; cancels running subgraphs on v3 stream abort. Tornado dep bumped 6.5.5→6.5.6.
- **cli==0.4.30** (2026-06-16) — Incremental CLI release bundled with 1.2.6 cycle.

### crewAIInc/crewAI
- **1.14.8a2** (2026-06-18) [PRE] — Adds single-agent action to Flow definitions; validates Flow CEL expressions at definition load time. Adds Datadog integration guide.
- **1.14.8a1** (2026-06-18) [PRE] — Incremental alpha (snapshot/changelog update).
- **1.14.8a** (2026-06-18) [PRE] — Initial 1.14.8 alpha drop.

### mastra-ai/mastra
- **@mastra/core@1.45.0** (2026-06-19) — Restores state signals without full message scan, making long-thread resumes significantly cheaper. Fixes agent signal drains so pending signals route through canonical transcript path with consistent response message ID rotation.

---

## Momentum picks

*(No momentum signals fired — 30d baseline requires ≥21 days of prior data; this run is 7 days from baseline. Unlocks 2026-07-07.)*

---

## Things to watch

**dspy +257 with no release.** Third-highest 7d delta in the cohort, no new release, repo last pushed 2026-06-18. Pure organic inbound — worth watching whether a paper citation or social moment drove this.

**autogen last tagged Sep 2025.** Repo was last pushed April 2026; the Python package likely ships via a different release mechanism or is moving to the AG2 fork. The 9-month release gap on GitHub is misleading — +189 stars/7d signals it's still getting attention — but it's a tracking gap. Flagging for future state review.

**pydantic-ai v2 beta series.** v2.0.0b7 dropped June 10 alongside the v1 track (v1.107.0 same day). They're running dual tracks. A v2.0.0 stable release is coming — when it lands it may fire a breaking signal (major version bump + potential API surface changes).

---

## Anchor position

aeon sits at 543★ this week, +29 in 7 days — lowest 7d absolute delta in the cohort. That gap is structural: aeon doesn't ship numbered GitHub releases the way a pip/npm package does; activity shows up as commits (pushed 2026-06-22) and skills-as-markdown, not `git tag`. The star base is 543 vs langgraph's 35k — a different cohort segment. What's interesting is the fork count: 188 forks vs mastra's 2,278 with 25k stars suggests different fork-to-star behavior. Worth tracking whether the bdradar fork signal (40+ active forks with own content) translates to ecosystem repos that would boost the GitHub star count over time.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 0`
