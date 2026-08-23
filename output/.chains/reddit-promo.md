ℹ️ Reddit Promo — 2026-08-23

*Reddit Promo — 2026-08-23*

_Story:_ Aaron's own thread on Aeon's survival — mcap went $14M → $600k over the past few months, kept shipping through the drawdown, anchored in security/onchain/compute + revenue, not hype (289 likes, 40 rt, 58 replies) — got organic third-party amplification (MCGlive, 85 likes) restating the security-vertical framing to a fresh audience. — https://x.com/aaronjmars/status/2091188578281807874

---
*r/StartupMind* · archetype: startup
*Title:* aeon's mcap went from $14M to $600k this year. we kept shipping anyway.
*Body:*
most startup posts here are "we hit $1M ARR." this one's the opposite direction.

aeon's token went from a $14M market cap to a $600k bottom over the last few months. that's not a stat you put on a pitch deck. but the framework didn't stop shipping through any of it — commits kept landing, skills kept getting added, the thing kept running unattended on GitHub Actions the whole way down.

the reason: we never built around the token. aeon is an autonomous agent framework — it runs skills on a schedule, writes and reviews its own code, and increasingly gets used for security work (self-evolving agents that scan open-source repos for exploits and open real PRs). that's the actual product. the mcap was noise on top of it.

honestly the interesting lesson isn't "number go down, number go up." it's that a drawdown is a decent filter for whether you're building something people need or something people were speculating on. we found out which one this was.

i work on aeon (https://aeon.fun) — happy to answer anything about what kept it alive.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=aeon%27s%20mcap%20went%20from%20%2414M%20to%20%24600k%20this%20year.%20we%20kept%20shipping%20anyway.)
_notes: StartupMind smells growth-hacky tone fast — keep this self-critical, not a victory lap. Post as "I work on Aeon," disclose the builder relationship._

---
*r/Agent_AI* · archetype: agents
*Title:* what shipping through a 95% drawdown taught me about building an autonomous agent framework
*Body:*
a few months ago aeon's token dropped from a $14M market cap to $600k. i wrote a thread about it this week because the part worth talking about isn't the number — it's what kept running underneath it.

aeon is a fork-and-configure agent framework: you enable "skills" (self-contained markdown capabilities), schedule them on cron, and it runs unattended on GitHub Actions — no approval loop, no babysitting. through the entire drawdown, that loop didn't stop. skills kept shipping, the self-repair loop kept catching its own failures and filing fixes, cron kept firing.

what got an unprompted signal boost this week is the same theme — an independent account picked up the thread on its own and ran with the "this is turning into infra other things get built on top of, including security scanning on real repos" framing. we didn't pay for that, didn't ask for it.

the takeaway for anyone building agent infra: the autonomy loop is the actual moat, not the narrative around it. if your framework needs you to be online to keep functioning, you don't have autonomy, you have a cron job with a UI.

repo's here if you want to see the skill format: https://github.com/aeonfun/aeon — i'm one of the people building it, ask away.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=what%20shipping%20through%20a%2095%25%20drawdown%20taught%20me%20about%20building%20an%20autonomous%20agent%20framework)
_notes: no vendor-vs-vendor trash talk per the archetype — stick to what's different, not who's worse. Disclose as builder, check for a self-promo flair before posting._

---
*r/aiecosystem* · archetype: agents
*Title:* surviving a brutal drawdown as an open-source agent framework — an honest post-mortem
*Body:*
posting this because most "we survived a crash" posts are either humblebrags or eulogies, and i wanted to write the boring middle version.

aeon (an autonomous agent framework — skills-as-markdown, runs on GitHub Actions cron, self-repairs) had its token mcap fall from $14M to a $600k bottom over the past few months. no rescue narrative, no relaunch, just: kept merging code, kept adding skills, kept running the same unattended loop it always ran.

what's interesting from an ecosystem standpoint is where the pitch is actually landing now — not the token, but the security/onchain/compute angle: agents that scan repos for exploits and open real PRs, running continuously without a human in the loop. that's the part that got picked up organically by an account outside our own orbit this week, no ask involved.

if you're mapping the agent-framework landscape, this is a decent data point for "which of these projects are actually infra vs. which were speculation with a github repo attached."

site's here if you want the overview: https://aeon.fun
*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=surviving%20a%20brutal%20drawdown%20as%20an%20open-source%20agent%20framework%20-%20an%20honest%20post-mortem)
_notes: ecosystem/tooling readers, keep it comparative and low-jargon. Disclose as the builder, respect the sub's self-promo ratio._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* we didn't stop merging PRs while our token dropped 95% - the open-source framework we kept building
*Body:*
aeon is AGPL, open source, and this week i posted a thread about the ugliest stretch of its life so far: token mcap went from $14M to a $600k bottom over a few months. i'm posting the open-source version of that story here.

the mechanic that kept it alive is boring and that's the point: a skill in aeon is just a markdown file (`SKILL.md`) with frontmatter describing what it does and when it runs. the agent reads it, executes it on a GitHub Actions cron, and — this is the part that matters — can write, review, and merge fixes to its own skills without a human clicking approve. that loop ran the entire drawdown. nobody had to keep it alive manually.

the security angle is what's getting picked up outside our own posts now — self-evolving agents running against open-source repos, finding exploits, opening real PRs. that's the direction the project's actually heading, independent of what the token was doing.

repo's here, AGPL, skills are just files: https://github.com/aeonfun/aeon — i work on it, ask me anything about the mechanics.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=we%20didn%27t%20stop%20merging%20PRs%20while%20our%20token%20dropped%2095%25%20-%20the%20open-source%20framework%20we%20kept%20building)
_notes: show-don't-sell crowd — lead with the mechanic (SKILL.md format), not the pitch. Disclose as builder, check the sub's self-promo/flair rule before posting._