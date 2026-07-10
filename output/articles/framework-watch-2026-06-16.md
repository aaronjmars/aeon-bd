---
type: Article
---

# AI Framework Watch — 2026-06-16

**Verdict:** RELEASE WEEK: 4 frameworks shipped — langgraph, crewai, mastra, pydantic-ai *(COLD START — deltas baseline from next run)*

**Tracked:** 9 of 9 frameworks  ·  **Unreachable:** 0  ·  **Anchor:** aaronjmars/aeon

---

## Ranked table

(First run — no prior state, so all 7d/30d deltas are baseline `—`. Anchor pinned to top; remaining sorted by absolute stars desc since deltas are unavailable this run.)

| Framework | Stars | 7d Δ | 30d Δ | Releases (7d) | Breaking? | Headline |
|-----------|-------|------|-------|---------------|-----------|----------|
| aaronjmars/aeon | 514 | — | — | 0 | — | — (ships via continuous `main` commits, not tagged releases) |
| microsoft/autogen | 58,994 | — | — | 0 | — | — (last tagged release python-v0.7.5, 2025-09-30; repo pushed 2026-04-15) |
| crewAIInc/crewAI | 53,673 | — | — | 5 | — | 1.14.7 — pluggable memory/knowledge/rag/flow backends + native Snowflake Cortex provider + chat API |
| run-llama/llama_index | 50,166 | — | — | 0 | — | — (last GitHub release v0.14.22, 2026-05-14) |
| stanfordnlp/dspy | 35,060 | — | — | 0 | — | — (last stable 3.2.1, 2026-05-05; 3.3.0b1 beta 2026-05-28) |
| langchain-ai/langgraph | 34,907 | — | — | 3 | — | 1.2.5 — config-metadata + state bug fixes; migrated type checking to `ty`; CLI 0.4.29 |
| huggingface/smolagents | 27,882 | — | — | 0 | — | — (last release v1.26.0, 2026-05-29) |
| mastra-ai/mastra | 25,123 | — | — | 1 | — | @mastra/core@1.42.0 — trusted "system actor" execution + SignalProvider framework + native tool suspension |
| pydantic/pydantic-ai | 17,781 | — | — | 2 | — | v1.107.0 (security fix) + v2.0.0b7 *(major bump — review changelog)* |

---

## Releases (7-day window)

(Window: 2026-06-09 → 2026-06-16. Pre-releases tagged `[PRE]`. Sorted by `published_at` desc, grouped by framework.)

### mastra-ai/mastra
- **@mastra/core@1.42.0** (2026-06-12) — Trusted "system actor" execution lets server-side/background work (cron, schedulers, queues) run as a trusted `actor` across `workflow.execute()`, `tool.execute()`, `agent.generate()/stream()` and memory FGA checks while preserving tenant-scoped auth. Adds a `SignalProvider` framework (webhooks/polling/subscriptions, incl. `WebhookSignalProvider`/`TaskSignalProvider`) and agent-agnostic interactive tools via native tool suspension (`ask_user`, `submit_plan`).

### langchain-ai/langgraph
- **langgraph==1.2.5** (2026-06-12) — Patch: merge `lc_versions` config metadata, fix `updateState` deltaChannel bug on empty thread, migrate Python type checking to `ty`, minor-and-patch dep group bump (14 updates).
- **langgraph-cli==0.4.29** (2026-06-11) — CLI maintenance release.
- **langgraph-cli==0.4.28** (2026-06-10) — CLI maintenance release.

### crewAIInc/crewAI
- **1.14.7** (2026-06-11) — Pluggable default backends for memory/knowledge/rag/flow; native Snowflake Cortex LLM provider; chat API for conversational flows; surfaces real `finish_reason`, sampling params, and `response.id` on LLM events; per-run runtime state scoping; pip-audit CVE fixes (aiohttp, docling). Feature-heavy despite the patch version.
- **1.14.7rc2** (2026-06-11) `[PRE]` — Release candidate for 1.14.7.
- **1.14.7rc1** (2026-06-11) `[PRE]` — Release candidate for 1.14.7.
- **1.14.7a4** (2026-06-09) `[PRE]` — Alpha for 1.14.7.
- **1.14.7a3** (2026-06-09) `[PRE]` — Alpha for 1.14.7.

### pydantic/pydantic-ai
- **v1.107.0** (2026-06-10) — Security: handles `UploadedFile` consistently with `FileUrl` in UI adapters, fixing a `VercelAIAdapter` confused-deputy file-read advisory (GHSA-h7p7-w5gc-xj3w). Affects apps exposing the Vercel AI adapter.
- **v2.0.0b7** (2026-06-10) `[PRE]` *(major bump — review changelog)* — V2 Beta 7. Per the maintainers, adds no new breaking/v2-specific changes; pulls in the v1.107.0 security fix. The v2.0.0 line is in active beta — worth tracking for anyone pinning pydantic-ai before the major lands.

---

## Momentum picks

No momentum signals fired — this is the first run, so no week-over-week star deltas exist yet to measure spikes against. Baseline is now recorded; momentum picks become computable from next week's run onward.

---

## Anchor position

aeon sits at the bottom of the table by absolute stars (514) — expected, and not a like-for-like comparison. The cohort is nine mature, multi-thousand-star Python/TypeScript *libraries* (17k–59k stars) that developers import; aeon is a far younger, structurally different project — a GitHub-Actions-native autonomous-agent runtime where skills are markdown, not a pip/npm import. It ships no tagged GitHub releases (continuous `main` commits instead — last push 2026-06-15), so the "Releases (7d)" column reads 0 for aeon by design, not from inactivity. With no prior state this run, there's no star delta to position aeon's trajectory against the cohort yet; that comparison opens up next week once the baseline rolls forward.

---

## Source status

`gh_api: ok · reachable: 9/9 · releases_lookup: 9/9 · breaking_signals_fired: 0`
