Committed. No notification fired — correct per the skill's gate (all 12 fresh leads are `forking`, which is below the `building`/`integrating` self-notify threshold; the `war-room` brief carries the roll-up).

## Summary

Re-ran `bd-radar` to process the `forking` signal that commit **#4** just lit up. The morning sweep had forks/issues **403-dark** and fell back to `gh search` alone; the `GH_READ_PAT` prefetch (`.xai-cache/bd-radar-github.json`) is now populated — **40 aeon forks + 40 MiroShark forks**. "fix the eyes" landed for bd-radar.

**What I found**
- **12 fresh `forking` leads** (none previously surfaced). Kept forks with their own commits (`pushed` > `created`); deduped owners already in `ECOSYSTEM.md`/`SHOWCASE.md` (Aeon City, AntFleet, Atrium, Echo Oracle, Hound Flow, Mneme, VIGIL) and skipped the operator's own fork (NurstarK).
- **Headline:** `swarm-ai-research/aeon-atlas` — likely the known **ResearchSwarm**, but escalating hard: renamed aeon → `aeon-atlas` with ~22MB of own content **and** forked MiroShark, both pushed today. The one lead worth a message; everything else is "watch."
- **Read:** the fork fleet is **two-sided** — ~40 forks each, and the same operators hold a fork of *both* products. One builder pool adopting the whole stack.
- `integrating` is a **true zero** this sweep (issues endpoint returned `[]`), not a source miss.

**Files**
- `articles/bd-radar-2026-06-11.md` — appended "Update — `forking` source now lit" section (top-10 forking table + read + source status)
- `memory/topics/bd-radar-leads.json` — 10 → 22 leads, surfaced LRU 10 → 22
- `memory/logs/2026-06-11.md` — `### bd-radar (re-run)` block
- Committed to `main` as `e7128ac`

**No notify** (forking-only, below the gate). 

**Follow-up:** the last dark source is **X** — wire a bd-radar X prefetch to light the `mentioning` class (x-mcp is local-only on the runner).
