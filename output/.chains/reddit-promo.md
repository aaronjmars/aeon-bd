ℹ️ Reddit Promo

*Reddit Promo — 2026-08-12*

_Story:_ Aeon's 10-day shiplog recap — a Uniswap v4 hook merged by an unattended agent, native Google A2A support, both repos "blossoming" on stars/PRs — https://x.com/aeonframework/status/2086813421807231311

---
*r/lovingopensourceAI* · archetype: open-source
*Title:* What I've been building: an open-source agent framework that merged a Uniswap v4 hook with no human approving the diff

*Body:*
I work on Aeon, an AGPL agent framework, and wanted to share something concrete instead of another "AI agents are the future" post.

Last week one of our skills — which is just a markdown file describing a task, nothing fancier — wrote, tested, and merged a Dynamic Fee Hook for Uniswap v4. No PR review gate, no human clicking approve. It runs on a GitHub Actions cron, the same way the rest of the framework does: skills fire on a schedule, read/write the repo, and log what they did to a plain markdown memory folder you can audit after the fact.

The same 10-day stretch also added native support for Google's A2A protocol, so any skill in the framework is independently callable as its own agent by other agents — not just a webhook you have to reverse-engineer.

It's not perfect and there's stuff that still needs a human (anything genuinely irreversible is gated), but the "no approval loop for routine work" part is real and you can read the exact commit history that proves it. Repo's here: https://github.com/aeonfun/aeon — happy to answer questions about how the skill/cron/memory pieces fit together.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=What%20I%27ve%20been%20building%3A%20an%20open-source%20agent%20framework%20that%20merged%20a%20Uniswap%20v4%20hook%20with%20no%20human%20approving%20the%20diff)
_notes: disclose as builder ("I work on Aeon") in the post itself, not just implied — this sub is welcoming to "what I built" posts but still expects the disclosure up front._

---
*r/aiecosystem* · archetype: agents
*Title:* Where we've landed on the autonomy axis for agent frameworks, after 10 days of shipping

*Body:*
There's a spectrum in agent tooling right now: on one end, frameworks that need a human to approve every meaningful action; on the other, frameworks that just... run. We've been building toward the second end with Aeon, and the last 10 days is a useful data point either way you land on that debate.

In that window: an agent independently shipped and merged a Uniswap v4 fee hook (real on-chain code, not a demo repo), and we added native support for Google's A2A protocol so individual skills are callable as standalone agents by other systems — not locked into our own runtime. Both product repos also kept growing on stars/PRs through the same stretch, which at least suggests the unattended-run model isn't quietly breaking things.

Not claiming this is the only valid design — plenty of good reasons to keep humans in the loop for high-stakes actions, and we still gate anything irreversible. But if you're mapping the agent-framework landscape, "runs unattended on a cron with public traces" is a real point on it now, not just a pitch. More at https://aeon.fun if you want to see how the skill/cron/memory pieces work — glad to go deeper on any of it.

*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=Where%20we%27ve%20landed%20on%20the%20autonomy%20axis%20for%20agent%20frameworks%2C%20after%2010%20days%20of%20shipping)
_notes: no vendor-vs-vendor comparisons in the body — keep it descriptive, not competitive; disclose as builder up top._

---
*r/StartupMind* · archetype: startup
*Title:* 10 days of building in public: what actually shipped, no vanity metrics

*Body:*
Founder update, kept honest: over the last 10 days across our two products (Aeon, an agent framework, and Miroshark, a swarm-simulation engine), the concrete stuff that shipped was — an agent independently wrote, tested, and merged a Uniswap v4 fee hook end to end; we added native Google A2A protocol support so individual skills act as standalone agents; and both repos kept climbing on stars and PRs through the stretch, without a single coordinated marketing push behind it.

I say "no vanity metrics" because the part I actually care about reporting is the shipped-feature list, not the star count — the stars are a byproduct, not the goal. The interesting bet here is that most of this ran unattended: scheduled runs, no human approving each diff, self-repair when something breaks. That's the actual product thesis, and this week is one more data point for or against it.

If you're building something adjacent — agent tooling, on-chain automation, simulation — happy to compare notes. https://aeon.fun has the detail if you want to dig in.

*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=10%20days%20of%20building%20in%20public%3A%20what%20actually%20shipped%2C%20no%20vanity%20metrics)
_notes: StartupMind is quick to smell growth-hacky tone — keep the framing honest/founder-voiced, disclose as builder, no growth-hack language._

---
*r/MiroFish* · archetype: community
*Title:* Miroshark rode the same 10-day wave as Aeon — quick update for the community

*Body:*
Quick one for folks already tracking Miroshark: the last 10 days were good on both sides of the house. While the Aeon side of the team was busy getting an agent to independently ship and merge a Uniswap v4 fee hook (yes, really — no human approving that diff) and rolling out native Google A2A support, Miroshark kept climbing on stars and PRs through the same window.

Nothing revolutionary to report on the swarm-sim side specifically this week — no new feature drop — but the sustained growth without a coordinated push is worth flagging, since it usually means people are finding the "$1, hundreds of agents, under 10 minutes" pitch and actually trying it rather than just reading about it.

If you're running sims and hitting rough edges, or have ideas for what the engine should simulate next, drop them here or open an issue — that's still the fastest way to get something prioritized. Repo: https://github.com/miroshark/miroshark

*Link in post:* https://github.com/miroshark/miroshark
*Post here:* [Open r/MiroFish composer](https://www.reddit.com/r/MiroFish/submit?title=Miroshark%20rode%20the%20same%2010-day%20wave%20as%20Aeon%20%E2%80%94%20quick%20update%20for%20the%20community)
_notes: home community, insider tone is fine here — still sign off as team ("I work on Miroshark"), no strict flair requirement known but check sub rules before posting._