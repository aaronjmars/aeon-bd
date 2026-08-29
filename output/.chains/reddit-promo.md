ℹ️ Reddit Promo - 2026-08-29

*Reddit Promo - 2026-08-29*
1d since last promo · 4 subs drafted

_Story:_ Cult OS built a paid agent entirely on Aeon skills, hireable via x402 for PR evals/repo audits/code review - https://x.com/thecultos/status/2093467967807713472

---
*r/Agent_AI* · archetype: agents
*Title:* A third-party agent is now hireable via x402, built entirely on Aeon skills
*Body:*
someone built an agent on top of Aeon and it's already earning money without us doing anything.

Cult OS built "Cult OS agent" — runs PR evals, repo analysis, and code audits — entirely as Aeon skills (markdown files that fire on a cron via GitHub Actions). it's hireable via x402, so it gets paid per job, no subscription, no dashboard, no approval loop in the middle.

what's interesting isn't the specific product — it's that this is the actual shape of "autonomous agent" people keep talking about. skill = markdown + a schedule. self-repair if it breaks. public trace of every run. no human babysitting the loop. someone else just proved it's composable enough that a stranger can build a paid service on top without touching our code.

same pattern (x402-metered, no extra infra) just showed up on the Miroshark side too — an affiliate feature that pays out onchain per referral, one line to wire up. feels like x402 is becoming the default settlement layer for agent-to-agent value, not just a novelty.

repo: https://github.com/aeonfun/aeon

i work on Aeon — happy to answer questions about the skills/cron/x402 setup if anyone's building something similar.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=A%20third-party%20agent%20is%20now%20hireable%20via%20x402%2C%20built%20entirely%20on%20Aeon%20skills)
_notes: r/Agent_AI tolerates builder posts if they lead with substance — promo stays secondary, disclosure ("i work on Aeon") already in body._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - open-source framework where markdown skills run unattended on GitHub Actions
*Body:*
what it is: an agent framework where a "skill" is just a markdown file (SKILL.md) — no custom DSL. cron triggers it, it runs headless on GitHub Actions, and there's a self-repair loop that files and fixes its own issues when a skill degrades.

why it's on here today: a third party (Cult OS) just built a paid agent entirely out of Aeon skills — PR evals, repo audits, hireable via x402 per job. they didn't touch our code, just wrote skills and pointed a cron at them. that's the real test of whether a framework is composable vs. just marketed as one.

stack: Claude Code + GitHub Actions + markdown skills + x402 for agent-native payments. AGPL, public repo, public run traces.

repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20open-source%20framework%20where%20markdown%20skills%20run%20unattended%20on%20GitHub%20Actions)
_notes: r/CoolGithubProjects enforces the exact "Aeon - <one-line desc>" title format and bans hype language — body kept factual/tight, no sales language._

---
*r/aiecosystem* · archetype: agents
*Title:* x402 micropayments are becoming the default way agent frameworks monetize
*Body:*
two things happened in the Aeon/Miroshark ecosystem this week that point at the same thing: x402 (wallet-native, per-request agent payments) is quietly turning into the default rail, not a novelty.

first: a third-party team (Cult OS) built an agent entirely on Aeon skills and made it hireable via x402 — PR evals, repo analysis, audits, paid per job, no subscription tier, no dashboard.

second: Miroshark (our swarm-sim engine) shipped x402aff — one line makes any x402 endpoint affiliate-ready, 10% paid out onchain on Base automatically. an unaffiliated account flagged it unprompted, which is usually the better signal than us posting about our own feature.

the common thread: once an agent can hold and spend money natively, the economics of "build vs. rent an agent" change. you don't need a SaaS tier, you need an endpoint and a price.

Aeon: https://aeon.fun
*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=x402%20micropayments%20are%20becoming%20the%20default%20way%20agent%20frameworks%20monetize)
_notes: one link only (site) even though two products are mentioned — this sub is ecosystem-level discussion, lead with the pattern not the product; disclose "i work on Aeon/Miroshark" if asked in comments._

---
*r/MiroFish* · archetype: community
*Title:* Miroshark shipped x402aff: one line makes any endpoint affiliate-ready, paid onchain on Base
*Body:*
shipped x402aff this week — wire one line into any x402 endpoint and it becomes affiliate-ready. 10% of the payment routes onchain to whoever referred the call, automatically, no extra infra to run.

built it because we kept seeing the same ask: people wanted to promote Miroshark simulations and get paid in a way that didn't require us to build a whole referral backend. x402 already handles the payment rail, this just adds the split.

wasn't planning to post about it today but @svector_eth flagged it unprompted with a clean writeup of the mechanic — a better signal than us tweeting it ourselves: https://x.com/svector_eth/status/2093217883413164316

repo: https://github.com/miroshark/miroshark

i work on Miroshark — ask me anything about how the affiliate split works or what's next (director mode + belief-drift stuff still cooking).
*Link in post:* https://github.com/miroshark/miroshark
*Post here:* [Open r/MiroFish composer](https://www.reddit.com/r/MiroFish/submit?title=Miroshark%20shipped%20x402aff%3A%20one%20line%20makes%20any%20endpoint%20affiliate-ready%2C%20paid%20onchain%20on%20Base)
_notes: home community, insider tone fine — still disclose "i work on Miroshark" and mind the self-promo ratio, this is a maker post._