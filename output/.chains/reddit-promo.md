ℹ️ Reddit Promo - 2026-09-07

*Reddit Promo - 2026-09-07*
1d since last promo · 4 subs drafted

_Story:_ Capminal ($CAPU) credits @aeonframework with a private security review that caught and fixed a live mint-curve pricing bug, shipped on Base with zero downtime - https://x.com/Capminal/status/2096968349028872581

---
*r/OpenSourceAI* · archetype: open-source
*Title:* An agent framework audited a live DeFi contract and shipped the fix - here is the actual mechanic
*Body:*
last week a project called Capminal had aeon run a private security review on their $CAPU vault contracts. it found a mint-curve pricing bug, fixed it, shipped live on Base - no storage changes, no downtime.

what's interesting isn't the fix, it's how it happened: aeon's "review a contract" capability is a skill - a markdown file with instructions, running unattended on a cron via GitHub Actions. no approval loop, no human babysitting each step. the whole framework works this way: skills-as-markdown, self-repair when something breaks, public run traces so you can see what it actually did instead of trusting a changelog.

aeon is MIT-licensed, on GitHub: https://github.com/aeonfun/aeon. if you want to see what a skill file actually looks like, the repo has real examples, not toy ones.

happy to answer questions about how the review skill is structured or how the cron/dispatch model works.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=An%20agent%20framework%20audited%20a%20live%20DeFi%20contract%20and%20shipped%20the%20fix%20-%20here%20is%20the%20actual%20mechanic)
_notes: post as the builder ("I built this"), not anonymously - r/OpenSourceAI tolerates self-promo when it's substantive/technical, keep the ratio in check._

---
*r/aiecosystem* · archetype: agents
*Title:* A security-review agent skill just landed its first named audit-partner credit
*Body:*
Capminal ($CAPU) had aeon run a private security review on their vault contracts this week. the review caught a mint-curve pricing issue, aeon shipped the fix live on Base, no storage changes, no downtime.

worth flagging for this sub specifically: this wasn't a one-off script someone wrote for Capminal. it's the same general-purpose skill running on a schedule for anyone who asks - autonomous review, unattended execution on GitHub Actions, self-repair if a step fails, a public trace of what it did. that's the axis aeon competes on vs most agent frameworks - not "smarter model," but "actually runs unattended and you can audit what it did after."

site's at https://aeon.fun if you want the transparency dashboard + how the skill system works.

curious what this sub's take is on autonomy vs. supervised-agent tradeoffs for something with real financial stakes like a contract audit.
*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=A%20security-review%20agent%20skill%20just%20landed%20its%20first%20named%20audit-partner%20credit)
_notes: disclose as the builder ("I work on Aeon"), not a neutral observer - check the sub's self-promo flair requirement before posting._

---
*r/StartupMind* · archetype: startup
*Title:* We just landed our first named security-audit credit as a startup
*Body:*
small traction update. a DeFi project (Capminal) had our framework run a private security review on their vault contracts. it found a real pricing bug, we fixed it, they shipped it live on Base with zero downtime - and credited us publicly, unprompted.

that's the first time a paid-for-real-stakes product used aeon for something that mattered and told people about it. not a testimonial we asked for, not a case study we wrote - they just tweeted it.

been building aeon in public for a while (skills-as-markdown, self-healing agent framework, all open on GitHub) and this is the kind of proof point that actually moves the needle vs another feature announcement. site: https://aeon.fun

happy to talk through how we structured the review skill if anyone's building something adjacent.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=We%20just%20landed%20our%20first%20named%20security-audit%20credit%20as%20a%20startup)
_notes: founder-voice disclosure ("I'm the builder") - keep it a traction story, not a pitch; StartupMind smells growth-hacky tone fast._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* My agent found and fixed a live contract bug this week, wild to watch
*Body:*
so I run an open-source agent framework (aeon) and one of its skills is "run a security review." this week a project called Capminal actually used it on their $CAPU vault contracts. it found a mint-curve pricing issue, fixed it, shipped live on Base, no downtime. and they just... tweeted about it, unprompted.

the whole thing is a markdown file that runs on a schedule. no me sitting there approving each step. that part still feels a little unreal even though I built it.

repo's here if you want to see what the skill file looks like: https://github.com/aeonfun/aeon. it's genuinely just markdown + a cron.

anyone else vibe-coded something that ended up doing real work like this? curious what other people are running unattended.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=My%20agent%20found%20and%20fixed%20a%20live%20contract%20bug%20this%20week%2C%20wild%20to%20watch)
_notes: disclose you're the builder - keep it casual, this sub wants a "look what happened" story, not a pitch._

---
_run: story 0d old, expires 2026-09-17 (10d promo window); Capminal's audit claim taken as-stated from their own tweet, no independent verification channel for the private-review detail (same sourcing caveat as prior partner-announcement stories); aeonfun/aeon verified live via gh api = 717★/257 forks/MIT. cadence note: 1d since last REDDIT_PROMO_OK (2026-09-06) - reddit-promo has run daily/near-daily since 08-20, flagging per the standing cadence-watch item in MEMORY.md._

🔗 https://x.com/Capminal/status/2096968349028872581