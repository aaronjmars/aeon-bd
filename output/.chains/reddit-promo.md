ℹ️ Reddit Promo — 2026-08-24

*Reddit Promo — 2026-08-24*

_Story:_ Aeon shipped as a native Claude plugin (`/aeon` inside Claude Code manages schedules/skills/Strategy/Soul) — Aaron's own announcement, 71 likes/16 RTs/8 replies, plus two independent platforms (HivemindOS, AgentOS) built native integrations on top of it the same week, unprompted — https://x.com/aaronjmars/status/2091580744350978205

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* Aeon now ships as a Claude plugin: /aeon manages skills, schedules, and strategy from inside Claude Code
*Body:*
I build Aeon — an open-source agent framework where every capability is just a `SKILL.md` file: frontmatter + a runbook written in plain English. No custom DSL, no skill-authoring API to learn.

This week it shipped as an actual Claude plugin. Import the repo, type `/aeon`, and you get schedules/skills/Strategy/Soul management directly inside Claude Code — no separate dashboard required.

Here's the shape of one real skill, trimmed:

```
---
name: Reddit Promo
category: productivity
description: Draft copy-paste-ready Reddit posts that promote Aeon...
var: ""
commits: false
---

Today is ${today}. Read memory/MEMORY.md and products.md for positioning.
Steps:
1. Collect candidate items from the daily fetch-tweets output.
2. Dedup against memory/reddit-promo-seen.txt.
3. Pick the strongest story, draft per-subreddit posts...
```

That's genuinely it — the whole "skill" is markdown a model reads and executes. If you can write a runbook, you can add a skill.

Two things happened on top of the plugin surface this same week without anyone asking: HivemindOS wired a full `/aeon` control panel into their stack, and AgentOS shipped an Aeon Skill Hub natively in their Skills tab so you can install/run Aeon skills without leaving AgentOS.

Repo: https://github.com/aeonfun/aeon (AGPL, runs unattended on GitHub Actions, self-repairs). Happy to answer questions about the plugin or the skill format.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=Aeon%20now%20ships%20as%20a%20Claude%20plugin%3A%20/aeon%20manages%20skills%2C%20schedules%2C%20and%20strategy%20from%20inside%20Claude%20Code)
_notes: disclose as builder ("I built Aeon") in the post; check if this sub requires a self-promo flair before submitting._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Agent skills as plain markdown files - Aeon's plugin update and what two other agent platforms built on top of it
*Body:*
Been building Aeon, an agent framework where "prompt engineering" and "skill authoring" are the same file. A skill is a markdown doc: some frontmatter (name, schedule, required env vars) and a runbook written like you're briefing a smart colleague. The agent reads it and executes, unattended, on a cron.

The mechanic that makes this work at scale: skills can chain into each other, share a persistent `memory/` directory (also just markdown), and self-repair — a health skill scores runs and files issues, repair skills fix them by opening PRs. No human in the approval loop for routine operation.

This week Aeon shipped as a native Claude plugin — `/aeon` inside Claude Code drives schedules, skills, and the agent's "Strategy"/"Soul" config files directly. Within days, two unrelated platforms built on it without being asked: HivemindOS exposed a full `/aeon` control surface in their own product, and AgentOS shipped an "Aeon Skill Hub" natively in their Skills tab.

Not claiming this is the only way to structure agent prompts — but if you're prompt-programming and fighting a bespoke DSL, "the skill is just markdown, the agent is the interpreter" is worth stealing as a pattern even if you don't touch Aeon itself.

Repo (AGPL) if you want to see the actual skill files: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Agent%20skills%20as%20plain%20markdown%20files%20-%20Aeon%27s%20plugin%20update%20and%20what%20two%20other%20agent%20platforms%20built%20on%20top%20of%20it)
_notes: disclose as builder; this sub leans technical/no-nonsense — keep it mechanics-first, skip the promo framing entirely if replying to comments._

---
*r/Agent_AI* · archetype: agents
*Title:* What unattended, self-repairing agent orchestration looks like in practice (Aeon's new Claude plugin + ecosystem integrations)
*Body:*
Sharing a concrete example of the autonomy end of the agent-framework spectrum, since most things called "agents" here still route every action through a human approval step.

Aeon runs skills (markdown runbooks) on GitHub Actions cron, no approval loop — it can write, review, and merge its own skill updates, and a self-healing loop scores runs and opens repair PRs when something degrades. Every run is a public GitHub Actions trace, so "it works unattended" is checkable, not a claim you have to take on faith.

This week the surface got a new front door: Aeon now runs as a Claude plugin (`/aeon` inside Claude Code manages schedules/skills/config). What's interesting from an ecosystem-design angle is what happened next, organically — HivemindOS integrated a full `/aeon` control panel into their own product, and AgentOS shipped an Aeon Skill Hub natively in their Skills tab. Neither was solicited; both happened the same week the plugin shipped.

Not a knock on approval-loop frameworks — different tradeoff, different use case. Just flagging what "skills + MCP + soul + no approval loop + public traces" looks like when other platforms start building on top of it instead of you having to build the integrations yourself.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=What%20unattended%2C%20self-repairing%20agent%20orchestration%20looks%20like%20in%20practice%20%28Aeon%27s%20new%20Claude%20plugin%20%2B%20ecosystem%20integrations%29)
_notes: disclose as builder ("I work on Aeon"); no vendor-vs-vendor framing — state what's different, don't dunk on other frameworks._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Open-source agent framework where every skill is a markdown file - now ships as a Claude plugin too
*Body:*
Aeon is AGPL-licensed, and the whole point of open-sourcing it was so people could actually read how it works instead of trusting a pitch. Here's the real mechanic: every capability ("skill") is a single markdown file — frontmatter for config, then a plain-English runbook. There's no proprietary skill format to reverse-engineer; you can open any file in `skills/` and read exactly what the agent will do and why.

This week it shipped as a native Claude plugin: clone the repo, type `/aeon` in Claude Code, and manage schedules/skills/config without leaving the editor. What I like reporting on this sub specifically — because it's the part that actually validates the "open" bet — is that two other platforms (HivemindOS, AgentOS) built native integrations on top of the plugin surface within days, unprompted, because the format is open enough to build on without asking permission.

To be clear about what this is and isn't: it's a personal/small-team framework, not a funded platform with an SLA. It runs unattended on GitHub Actions, which is powerful but means you're trusting cron + your own skill files, not a hosted service. If that tradeoff fits what you're building, the repo's here.

https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Open-source%20agent%20framework%20where%20every%20skill%20is%20a%20markdown%20file%20-%20now%20ships%20as%20a%20Claude%20plugin%20too)
_notes: disclose as builder; keep the "what it isn't" paragraph in — this sub rewards honesty about limitations over polish._