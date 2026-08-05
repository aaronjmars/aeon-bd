ℹ️ Reddit Promo — 2026-08-05

*Reddit Promo — 2026-08-05*

_Story:_ Aeon autonomously designed and deployed 5 new Uniswap v4 hooks overnight (ZigZagMandate, Volume Ladder, HeavierHand, PoliteTip, Block Echo) — no human in the loop, then got unprompted outside technical validation. — https://x.com/aaronjmars/status/2083681374708572451

---
*r/aiecosystem* · archetype: agents
*Title:* An unsupervised agent shipped 5 new Uniswap v4 hooks overnight
*Body:*
Aeon runs on a cron loop, no approval step. Last night it designed and deployed 5 new Uniswap v4 hooks on its own — ZigZagMandate, Volume Ladder, HeavierHand, PoliteTip, Block Echo. Not a demo, actual on-chain output while nobody was watching.

An outside dev pulled up the ZigZagMandate logic unprompted and called it "insane," flagged it as bot-resistant. First technical validation that wasn't us saying it.

Separately, a third-party team shipped an AeThree skill pack on top of Aeon — one call mints an avatar, deploys a token, opens its bonding curve. That's the part I actually care about more than the hooks: people building on it without us asking.

The mechanic underneath both: skills are markdown files, the agent runs unattended on GitHub Actions, self-repairs when a run breaks. No orchestration layer to babysit.

I work on Aeon. Repo + traces at aeon.fun if you want to see the actual runs, not just the highlight reel.
*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=An%20unsupervised%20agent%20shipped%205%20new%20Uniswap%20v4%20hooks%20overnight)
_notes: ecosystem/tooling sub, no flair requirement seen — disclose as builder in first paragraph, keep it fact-first not hype._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Skills are just markdown files, here's one that deployed 5 DeFi contracts on its own
*Body:*
The whole agent framework is: a `SKILL.md` file with frontmatter (schedule, permissions, required secrets) and a body the agent reads and executes. No custom DSL, no plugin API. If you can write a markdown checklist you can write a skill.

Concrete proof it's not a toy: overnight, one skill designed and deployed 5 new Uniswap v4 hooks unsupervised — ZigZagMandate, Volume Ladder, HeavierHand, PoliteTip, Block Echo. An outside dev looked at the logic afterward, unprompted, and called it "insane," bot-resistant. Nobody fed them that line.

The part that makes this durable instead of a one-off: there's a self-repair loop watching every run. A skill that breaks gets a health score and an issue filed against it, then a repair skill patches it by PR. Cron plus self-repair is doing more work here than the model.

I built this. Repo's linked below, skill format is documented, happy to answer questions on how the scheduling/permissions model works.
*Link in post:* https://github.com/aaronjmars/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Skills%20are%20just%20markdown%20files%2C%20here%27s%20one%20that%20deployed%205%20DeFi%20contracts%20on%20its%20own)
_notes: technical audience, respect it — lead with the mechanic not the pitch, disclose builder status up front._

---
*r/lovingopensourceAI* · archetype: open-source
*Title:* Open-sourced the agent that shipped 5 Uniswap v4 hooks while I was asleep
*Body:*
I work on Aeon, an open-source (AGPL) agent framework. It's fork-and-configure — you enable skills, schedule them, and it runs unattended on GitHub Actions. No approval loop between "agent decides" and "agent does."

Last night it proved that's not just a slogan: it designed and deployed 5 new Uniswap v4 hooks on its own, no human touching it. An outside dev found the code afterward and called it "insane" and bot-resistant — nobody prompted that, they just found the repo.

Separately, a third-party dev built an AeThree skill pack on top of it — mints an avatar, deploys a token, opens a bonding curve in one call. That's the actual point of open-sourcing it: people building things we didn't plan for.

Everything's public — the repo, the run traces, the skill files. Fork it if you want your own version. Happy to answer anything about the self-repair loop or how skills get scheduled.
*Link in post:* https://github.com/aaronjmars/aeon
*Post here:* [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=Open-sourced%20the%20agent%20that%20shipped%205%20Uniswap%20v4%20hooks%20while%20I%20was%20asleep)
_notes: enthusiast OSS crowd, "what I built + why it's open" framing lands well here — keep the AGPL/fork angle explicit._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* My agent shipped 5 DeFi contracts overnight without me touching anything
*Body:*
Set up an agent (Aeon) that runs on a cron schedule with no approval step. Went to sleep, woke up to 5 new Uniswap v4 hooks live — it designed and deployed all of them on its own overnight. Named them itself too (ZigZagMandate, Volume Ladder, HeavierHand, PoliteTip, Block Echo — no notes on the naming).

Best part: some rando dev found the code, didn't know me, called the logic "insane" and flagged it as bot-resistant. Free unprompted code review from a stranger.

It's just markdown files describing what to do plus a schedule. No custom framework to learn. Fork it, point it at your own repo, let it cook.

I built this, not shilling someone else's thing. Repo's below if you want to see how it's actually wired up.
*Link in post:* https://github.com/aaronjmars/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=My%20agent%20shipped%205%20DeFi%20contracts%20overnight%20without%20me%20touching%20anything)
_notes: casual sub, light self-promo tolerance but still disclose as builder — keep the tone first-person, no jargon dump._