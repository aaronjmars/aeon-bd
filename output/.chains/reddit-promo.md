ℹ️ Reddit Promo

*Reddit Promo — 2026-08-09*

_Story:_ you.com (~$1B AI search company) shipped an official "you-web-search" skill into Aeon, first-party — https://x.com/aeonframework/status/2085717364893478994

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* a billion-dollar startup just shipped a skill into my open-source agent framework - here's the actual markdown file
*Body:*
you.com (~$1B valuation, the AI search engine) just shipped an official skill into Aeon, the open-source agent framework I run. not a partnership announcement, not a press release — an actual `you-web-search` SKILL.md sitting in the repo, contributed and merged like every other skill.

that's the whole pitch of aeon skills: they're just markdown files. no plugin API, no SDK to learn. a skill file has frontmatter (name, schedule, required env vars) and then plain instructions for what the agent should do when it runs. the agent reads it and executes — no approval loop, no human in the middle. that's what let you.com ship theirs without needing anything special from us.

the skill runs on a cron schedule via GitHub Actions, pulls you.com's search API, and formats results back into whatever the calling skill needs. same shape as every other skill in the repo — reddit-promo, bd-radar, the one that's writing this post.

repo's here if you want to see the actual file: https://github.com/aeonfun/aeon — happy to answer questions on how the skill/cron/chain system works.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=a%20billion-dollar%20startup%20just%20shipped%20a%20skill%20into%20my%20open-source%20agent%20framework%20-%20here%27s%20the%20actual%20markdown%20file)
_notes: technical crowd, self-promo fine if concrete — post as the builder ("I built Aeon"), not a neutral discoverer._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* you.com (the search engine) just contributed an official skill to my open-source agent framework
*Body:*
quick one: you.com, the ~$1B AI search company, shipped a first-party integration into Aeon — the AGPL agent framework I've been building. they wrote a skill (`you-web-search`), submitted it, it's merged into the repo now.

worth flagging because it's the kind of signal that's hard to fake. companies don't usually spend eng time integrating with a project unless something about the architecture made it easy, or worth it. in this case: aeon skills are markdown files that run unattended on GitHub Actions cron — no SDK, no plugin system to learn. you write the skill, it runs.

it's the second or third outside integration to land this way in the past couple weeks (a security auto-verification layer and an on-chain wallet integration both showed up the same way). not one company's worth of validation, a pattern.

repo, AGPL, all public: https://github.com/aeonfun/aeon — down to answer questions on how the skill system or the self-repair loop works.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=you.com%20%28the%20search%20engine%29%20just%20contributed%20an%20official%20skill%20to%20my%20open-source%20agent%20framework)
_notes: respect the ~9:1 value-to-promo norm — lead with the mechanic before the link; disclose you're the builder._

---
*r/Agent_AI* · archetype: agents
*Title:* what it looks like when a real company integrates with your agent framework instead of just tweeting about it
*Body:*
there's a difference between "we love what you're building 🔥" replies and someone actually opening a PR. this week it was you.com — the AI search company — shipping an official `you-web-search` skill into Aeon, the autonomous agent framework I run.

on the autonomy axis specifically: aeon skills run unattended on GitHub Actions cron, no approval loop, and the framework self-repairs when a skill breaks (a health-scoring loop files issues, a repair skill fixes them by PR). that unattended-by-default posture is apparently what made it low-friction enough for an outside team to just ship into it instead of asking for an API key and building their own wrapper.

not claiming this makes aeon "better" than other agent frameworks — just sharing what actual third-party integration looks like versus the more common "cool project, following" pattern.

repo if you want to look at the skill they shipped: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=what%20it%20looks%20like%20when%20a%20real%20company%20integrates%20with%20your%20agent%20framework%20instead%20of%20just%20tweeting%20about%20it)
_notes: no vendor-bashing, this sub polices comparison posts — keep it factual, disclose builder status._

---
*r/StartupMind* · archetype: startup
*Title:* a billion-dollar startup shipped a first-party integration into what I'm building
*Body:*
building-in-public update: you.com (AI search, ~$1B valuation) shipped an official skill contribution into Aeon this week — an open-source autonomous agent framework I've been heads-down on. not a partnership deck, not a quote for a press release. an engineer wrote a skill, it got merged, it runs.

context for why this matters more than it might look: aeon runs entirely on GitHub Actions, public repo, public run logs — every skill execution is a verifiable trace, not a claim. that's been the design bet: if you can't show your work publicly, the "autonomous" claim is unfalsifiable. this is the first time it paid off as inbound instead of outbound — someone else decided integrating was worth their eng time, unprompted.

same week: a security-auditing integration and an on-chain wallet integration both landed the same way. three unprompted integrations in a matter of days is the actual traction signal, not the follower count.

site: https://aeon.fun — happy to talk about what building unattended-by-default actually looks like day to day.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=a%20billion-dollar%20startup%20shipped%20a%20first-party%20integration%20into%20what%20I%27m%20building)
_notes: founder-story framing expected, but still disclose "I built this" explicitly — skip growth-hacky language, StartupMind smells it fast._