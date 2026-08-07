ℹ️ Reddit Promo — 2026-08-07

*Reddit Promo — 2026-08-07*

_Story:_ Aeon shipped support for Mistral's Vibe harness — no longer locked to a single harness/runtime — https://x.com/aeonframework/status/2083180505315291454

---
*r/OpenSourceAI* · archetype: open-source
*Title:* My open-source agent framework just stopped being harness-locked (added Mistral Vibe support)
*Body:*
Been building Aeon for a few months — it's a fork-and-configure agent framework, AGPL, skills are just markdown files (`SKILL.md`) that run on GitHub Actions cron. No approval loops, no babysitting, self-repairs its own skills.

Up to now every instance ran through one harness. That changed this week — Aeon added support for Mistral's Vibe harness alongside the original one. Same skill files, same cron/chain/self-repair machinery, different engine underneath running them. If you don't want to be locked into a single vendor's runtime to run an autonomous agent, that's now optional.

Still early — one additional harness, not a marketplace of them yet — but the architecture was built to make this swap possible instead of hard-coded.

Repo: https://github.com/aeonfun/aeon

Happy to answer questions about the skill/harness split or the self-repair loop.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=My%20open-source%20agent%20framework%20just%20stopped%20being%20harness-locked%20%28added%20Mistral%20Vibe%20support%29)
_notes: self-promo-friendly sub, but keep the 9:1 ratio in mind if posting again soon; disclose as the builder ("I built Aeon"), not a neutral discovery._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - an autonomous agent framework that just added a second supported harness (Mistral Vibe)
*Body:*
Aeon (https://github.com/aeonfun/aeon) is a fork-and-configure agent framework — skills are markdown files that run on a cron via GitHub Actions, no approval loop, self-repairs when a skill starts failing.

This week's shipped change: it's no longer locked to a single harness. Mistral's Vibe harness is now a supported runtime alongside the original — same skills, same scheduling, different engine.

Open source, AGPL. The repo has the skill format and setup docs if you want to see how the markdown-skill mechanic actually works.

https://github.com/aeonfun/aeon

Happy to answer questions in the comments.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20an%20autonomous%20agent%20framework%20that%20just%20added%20a%20second%20supported%20harness%20%28Mistral%20Vibe%29)
_notes: strict title-format sub — keep "Aeon - <desc>" exactly as posted; disclose as the builder in a comment if it's not obvious from the title._

---
*r/Agent_AI* · archetype: agents
*Title:* Multi-harness support landed in my agent framework this week — curious how others in this sub handle vendor lock-in
*Body:*
Posting as the person building Aeon — an agent framework built around three things: skills as markdown, unattended runs on GitHub Actions (cron/chains), and self-repair (a health skill scores runs, a repair skill fixes them by PR).

Until this week, every Aeon instance ran on one harness. That changed — Mistral's Vibe harness is now a supported runtime option next to the original. Doesn't change how skills are written, just what executes them.

Curious how other agent-framework builders here think about this axis — harness portability vs. going deep on one vendor's tooling. We went portable on purpose; the tradeoff is less deep integration with any single harness's specific features.

Repo, if useful: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=Multi-harness%20support%20landed%20in%20my%20agent%20framework%20this%20week%20-%20curious%20how%20others%20in%20this%20sub%20handle%20vendor%20lock-in)
_notes: frame as a discussion, not just an announcement — this sub notices vendor-vs-vendor pitches; disclose as the builder up front, no trash-talking other harnesses._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* Aeon skills are literally markdown files like this — and they now run under more than one harness
*Body:*
If you're into Claude Code skills, Aeon skills are the same idea taken further: a `SKILL.md` with frontmatter (`name`, `mode`, `requires`) plus instructions, scheduled by cron, chained into other skills, self-repaired when they start failing. Roughly:

```
---
name: reddit-promo
mode: write
requires: []
---
Turn today's fetch-tweets output into promo drafts...
```

That's the whole mechanic — no hidden orchestration layer, the skill file IS the instruction set the agent reads.

What's new this week: Aeon isn't locked to running these on a single harness anymore. Mistral's Vibe harness is now supported alongside the original — same skill files, different engine reading them.

Repo (skills + the harness-adapter code): https://github.com/aeonfun/aeon

Genuinely curious what skills people in this sub have written — happy to compare notes.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=Aeon%20skills%20are%20literally%20markdown%20files%20like%20this%20-%20and%20they%20now%20run%20under%20more%20than%20one%20harness)
_notes: technical audience, respect it — no oversimplifying; disclose as the builder, this sub is fine with show-your-work self-promo._