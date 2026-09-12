ℹ️ Reddit Promo - 2026-09-12

*Reddit Promo - 2026-09-12*
1d since last promo (prior OK 2026-09-11, MiroShark video-export story) · 4 subs drafted

_Story:_ Aeon ships a "Submit Hook" skill - hook builders submit to the Hooks Marketplace through their own agent - https://x.com/aeonframework/status/2098792766658535737

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* Aeon shipped a skill that lets an agent submit its own Uniswap v4 hook to a marketplace
*Body:*
Two days ago Aeon launched a Hooks Marketplace - aeon.fun/hooks live with 12 Uniswap v4 hooks, a registry (aeonfun/univ4-hooks) taking deploys across 7 chains. Today's follow-on: a skill so hook builders don't have to go through us to list one - their own agent submits it.

The mechanic is exactly what it sounds like. An Aeon skill is a markdown file (SKILL.md) that a scheduled agent reads and executes on GitHub Actions - no framework code, no approval loop. This one packages a hook and opens the PR into the registry itself. Point your agent at it, it runs unattended.

Posting here because it's a concrete example of a skill doing something with real infra consequence (submitting to a live marketplace) instead of just replying to a prompt.

I work on Aeon. Happy to answer anything on how the submission flow or the registry is wired.

Link: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=Aeon%20shipped%20a%20skill%20that%20lets%20an%20agent%20submit%20its%20own%20Uniswap%20v4%20hook%20to%20a%20marketplace)
_notes: technical crowd, no hype - show the mechanic, disclose "I work on Aeon" up top._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Aeon (AGPL, skills are just markdown) shipped a hook-submission skill for its Uniswap v4 marketplace
*Body:*
Aeon is open source (AGPL) - skills-as-markdown running unattended on GitHub Actions, no framework lock-in, no approval loop between a skill firing and it acting.

Two days ago we shipped a Hooks Marketplace: aeon.fun/hooks, 12 Uniswap v4 hooks live, registry on GitHub (aeonfun/univ4-hooks) accepting deploys on 7 chains. Today's ship closes the loop - a skill that lets hook creators submit through their own agent instead of a manual PR to us.

The open-source part that matters: that submission skill is a plain markdown file anyone can read, fork, or run themselves. Nothing hidden in the pipeline between "here's my hook" and "it's listed."

I built Aeon. Repo's linked below if you want to see how the skill's written - questions welcome.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Aeon%20%28AGPL%2C%20skills%20are%20just%20markdown%29%20shipped%20a%20hook-submission%20skill%20for%20its%20Uniswap%20v4%20marketplace)
_notes: OSS crowd, "what I built + why it's open" framing - disclose "I built Aeon," no shilling beyond the mechanic._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - the most autonomous agent framework, skills-as-markdown running unattended on GitHub Actions
*Body:*
What it is: Aeon runs "skills" - plain markdown files - on a cron schedule via GitHub Actions. No server, no approval loop between a skill firing and it acting.

Why post now: this week gave a real example instead of an abstract pitch. Two days ago Aeon shipped a Hooks Marketplace (aeon.fun/hooks, 12 Uniswap v4 hooks, a registry taking deploys on 7 chains). Today it shipped a skill that lets outside hook builders submit through their own agent instead of PRing us directly - the marketplace grows itself.

Stack: runs on Claude Code / OpenClaw / Codex under the hood, memory persisted straight into the git repo, a self-repair loop that patches its own broken skills without a human merging it.

Repo's the payload here, not this post.

I maintain this project - happy to answer anything.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20the%20most%20autonomous%20agent%20framework%2C%20skills-as-markdown%20running%20unattended%20on%20GitHub%20Actions)
_notes: strict title format enforced ("Aeon - <one-line desc>") - repo link is the point, keep body tight, disclose "I maintain this."_

---
*r/aiecosystem* · archetype: agents
*Title:* Two agent products just became payment and distribution rails for a third-party project
*Body:*
Where this fits in the landscape: Aeon (agent framework, skills-as-markdown on GitHub Actions) shipped a skill today letting Uniswap v4 hook builders submit to its marketplace through their own agent - a follow-on to the Hooks Marketplace launch two days ago (aeon.fun/hooks, 12 hooks live, 7-chain deploy registry).

Same week, a different signal: Miroshark's x402aff mechanic - a 10% USDC split paid via builder code - just became CultOS's core distribution rail for their own project. That's not us pitching x402aff as a feature, that's an outside team choosing to build their payout infra on top of it.

Worth flagging for anyone mapping agent tooling: both cases are the same pattern - a framework stops being "a tool you use" and starts being "infra someone else builds their business logic into." That's a different adoption curve than usage numbers.

I work on Aeon and Miroshark. Curious if others here are seeing the same shift with other agent frameworks.

*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=Two%20agent%20products%20just%20became%20payment%20and%20distribution%20rails%20for%20a%20third-party%20project)
_notes: ecosystem/tooling readers, no vendor-vs-vendor language - disclose "I work on Aeon and Miroshark."_