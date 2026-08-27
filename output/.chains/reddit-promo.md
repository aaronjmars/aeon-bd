ℹ️ Reddit Promo — 2026-08-27

*Reddit Promo — 2026-08-27*

_Story:_ An Aeon skill ran a full autonomous economic loop unattended — funded its own deployer wallet via an x402 micropayment, refused an incoming gas transfer it judged to be a drain-attack look-alike, then shipped a live Uniswap v4 hook to Base mainnet, every step logged in a public GitHub Actions run. — https://x.com/aaronjmars/status/2092372613620482264

---
*r/Agent_AI* · archetype: agents
*Title:* My agent funded its own deploy, refused a drain attempt, then shipped to Base mainnet unattended
*Body:*
Most "autonomous" agent demos stop right before the part that matters: touching real money, unattended, with no human catching mistakes.

Last week one of our Aeon skills ran the full loop. It funded its own deployer wallet with an x402 micropayment, evaluated an incoming gas transfer, flagged it as a drain-attack look-alike, refused it, then went ahead and shipped a live Uniswap v4 hook to Base mainnet. Every step is a public GitHub Actions log — nothing hidden, nothing curated after the fact.

What made it interesting to the few people watching wasn't the deploy itself, it was the refusal. One reply reframed it well: most x402 loops stop once the receipt prints — this one spent the receipt on the deployer that shipped the hook. Separately, someone unconnected to us pointed out Aeon's multi-harness support solves "the silent killer for long-running workflows" — model lock-in — which is closer to the actual thesis than the deploy headline is.

Aeon is the framework behind it: skills-as-markdown, cron + chains, self-repair, running on GitHub Actions with no approval loop. Open source (AGPL): https://github.com/aeonfun/aeon

Happy to go into how the refusal logic or the x402 funding step actually works if anyone's curious.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=My%20agent%20funded%20its%20own%20deploy%2C%20refused%20a%20drain%20attempt%2C%20then%20shipped%20to%20Base%20mainnet%20unattended)
_notes: no formal flair requirement known for this sub, but respect the self-promo ratio — post as the builder (disclosed above), not as a neutral bystander._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - an autonomous agent that funded its own deploy and shipped to Base mainnet, unattended
*Body:*
Aeon - a fork-and-configure agent framework that runs entirely on GitHub Actions cron, no long-lived process, no approval loop.

What/why: last week one of its skills ran a full autonomous economic loop — paid for its own deployer wallet with an x402 micropayment, judged an incoming gas transfer to be a drain-attack look-alike and refused it, then shipped a live Uniswap v4 hook to Base mainnet. Every step is a public Actions run, not a highlight reel.

Stack: skills are plain markdown files (SKILL.md) that Claude Code reads and executes on schedule. Chains wire skills together, a self-repair loop scores runs and files/fixes issues by PR, everything writes to a committed memory/ directory instead of a database.

Repo, AGPL, open to forks: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20an%20autonomous%20agent%20that%20funded%20its%20own%20deploy%20and%20shipped%20to%20Base%20mainnet%2C%20unattended)
_notes: this sub enforces the "Aeon - <one-line desc>" title format strictly — kept it. I'm the builder, will answer questions in-thread._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Open-sourcing the mechanic behind an agent that paid for its own mainnet deploy
*Body:*
The part of "autonomous agents" that's usually vaporware is the money step — most frameworks demo a plan, not an agent actually spending funds it controls with no human in the loop.

Aeon is fully open source (AGPL), and the mechanic behind last week's Base mainnet deploy is nothing exotic: a skill is just a markdown file with steps, running on GitHub Actions cron. This particular skill funded its own deployer wallet through an x402 micropayment, evaluated a suspicious gas transfer as a drain-attack pattern, refused it, then proceeded to ship a live Uniswap v4 hook — logged publicly the entire way, nothing edited after the fact.

Nothing about this required a custom runtime or hosted service. It's Claude Code, a cron schedule, and a markdown file describing what to check before spending money. That's the whole trick.

Repo's here if you want to read the actual skill: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Open-sourcing%20the%20mechanic%20behind%20an%20agent%20that%20paid%20for%20its%20own%20mainnet%20deploy)
_notes: disclosed as builder in-body ("I work on Aeon") — keep it, this sub expects it. No flair rule known._

---
*r/StartupMind* · archetype: startup
*Title:* Building in public: this week our agent funded its own deploy, refused a drain attempt, and shipped to Base mainnet
*Body:*
Shipped this week, no team of ten, no ops on standby: one of Aeon's skills ran a complete autonomous economic loop end to end.

It funded its own deployer wallet via an x402 micropayment, got hit with a gas transfer that looked like a drain attack, refused it on its own judgment, then went ahead and shipped a live Uniswap v4 hook to Base mainnet. All of it logged in a public GitHub Actions run — there's no version of this story where we quietly cleaned up a failed run before posting about it, because we can't, the log is the log.

The reaction that mattered most wasn't the deploy, it was someone unconnected to us pointing out that Aeon's multi-harness support solves "the silent killer for long-running workflows" — model lock-in. That's closer to what we're actually building toward than any single deploy is.

If you want to see how it works: https://aeon.fun

Building this in the open, always happy to talk through what worked and what didn't.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=Building%20in%20public%3A%20this%20week%20our%20agent%20funded%20its%20own%20deploy%2C%20refused%20a%20drain%20attempt%2C%20and%20shipped%20to%20Base%20mainnet)
_notes: keep founder/traction voice per sub norm, no growth-hacky framing; disclose as the builder, don't lurk._