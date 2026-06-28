# Launch Radar — 2026-06-28

**Ideas scanned:** 10 | **Active competition:** 0 | **Prior art:** 8 | **Open:** 2

---

## Active Competition (Watch / Differentiate)

*None this scan.*

---

## Prior Art (Exists, No Traction)

### miroshark-social-world-model
**What exists:** SocialCompute (local LLM social simulation engine, HN ~2026, no upvote count); Agentarium (social sims, Jan 2025); AI-town (Aug 2023)
**Posture:** Adjacent products exist but they're all research/toy sims — none ship as an MCP/A2A `simulate(decision)` API. The funded world-models race (LeCun €500M, Genie 3) is all pixels. Social world model as a callable tool is still unclaimed.
**Call:** still worth building — the timing window is right and the MCP/A2A framing is the wedge the others miss

### proof-of-self-repair
**What exists:** Polarity, Helix (Apr 2026), 4-tier self-healing agent (Feb 2026), HyperFlow (Apr 2026) — the category is active with multiple recent Show HN launches
**Posture:** Self-healing agents went mainstream in early 2026 but every implementation is internal/enterprise — nobody ships a *public, verifiable* self-repair ledger. The category is crowded on the engineering side; the proof/transparency angle is unclaimed.
**Call:** still worth building — execution is free (aeon already runs it on public GitHub traces, proof costs nothing to ship)

### counterfactual-launch-sim
**What exists:** Societies.io (YC W25, June 2025 — AI simulations of target audience); ProductHunt Chaos Generator (Apr 2026 — single-LLM PH launch chaos sim)
**Posture:** Societies.io owns "simulate your audience" but it's a human-centric survey replacement, not a social-swarm counterfactual of a timing window. The PH Chaos Generator is a gimmick. Neither does the "what happens to narrative drift if we launch this week vs next month" calculation.
**Call:** still worth building — the swarm-based timing-window angle is distinct from what's live

### conway-claim
**What exists:** Phantom (open-source AI agent on own VM, Mar 2026); Crnd (cron for AI agents, Feb 2026); Trigger.dev (YC W23, Sep 2025); SuperPowers AI (always-on agents)
**Posture:** Background AI infrastructure proliferates. But this idea is a GTM play, not a new build — the "aeon shipped open ambient on public traces first" priority claim is still unclaimed as a *narrative*. Every competitor hides its traces. That's the wedge.
**Call:** claim the category the day Conway drops — cheapest execution of any idea in the backlog

### ambient-aeon
**What exists:** SuperPowers AI, Onpilot, AirJelly on ProductHunt; "Turn Claude Code into proactive 24/7 AI agents" Show HN (Feb 2026, >60 days ago)
**Posture:** The "proactive/ambient AI" category is fully VC-backed and crowded (Moveworks, Akira AI, Ambient.ai). No breakout launch in the current 60-day window. The "shipped first, verifiable on public traces" claim is still unclaimed — but the window narrows as Anthropic's Conway approaches.
**Call:** needs sharper angle — lean into conway-claim as the sharpened version of this idea

### skill-attest
**What exists:** SkillShield (security directory, 0–100 trust score), SkillFortify (formal verification), AcidTest, Clawned.io, Agentsec — wave of Jan–Mar 2026 Show HN launches; NVIDIA/CertiK/Capsule ($7M)/Copperhelm ($7M) funded
**Posture:** The AI-skill security category exploded after the ClawHavoc campaign (Jan 2026) and has since cooled. All the scanners use static analysis; the "tokenize the scanner, let agents fund the defense" angle is unclaimed. But the space is funded and out of aeon's GTM lane (security → aaeron).
**Call:** park it — surface to aaeron as a potential play, don't build here

### x402-skill-meter
**What exists:** CrowPay (Mar 2026), X402 Agent Starter Kit (Feb 2026), Zero.xyz (14K x402 tools), Delegare, P402.io, Agora — x402 infrastructure ecosystem is complete
**Posture:** The generic x402 metering layer commoditized. CrowPay and the Agent Starter Kit (both now >60 days old) already do "add x402 in a few lines." Skill-specific metering hasn't shipped as a standalone but the primitives make it trivial to add.
**Call:** ship it as a free aeon feature (inference self-funds), not a company — confirmed by screened analysis

### pm-presim
**What exists:** AI agent that trades Polymarket (Mar 2026); Prediction Hunt API (Apr 2026); Marx Finance (AI agents debate markets)
**Posture:** PM trading agent tooling is active but narrowly focused on execution, not pre-trade simulation. The belief-drift pre-sim wedge is unclaimed. However, this cuts against Aaron's PM skepticism and a funded direct player (Semantic 42) is already in the space.
**Call:** park it — survives as a Miroshark layer (sim-as-infrastructure) not a standalone product

---

## Open (No Launches Found)

- **compute-price-sim** — nobody forward-simulates AI-race narrative drift (compute index, model-of-the-month) before traders size bets; Polymarket has the markets live with real volume, nobody simulates ahead of them
- **agent-pay-sim** — the forward-simulation wedge (what does the agent payment network do under load before it fails?) is genuinely unclaimed; weakest demand signal of the two open ideas

---

*Source: ProductHunt + HN Show HN search | Ideas from memory/topics/startup-ideas.md | Generated by launch-radar*
