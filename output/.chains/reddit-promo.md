ℹ️ Reddit Promo - 2026-09-04

*Reddit Promo - 2026-09-04*
1d since last promo · 4 subs drafted

_Story:_ CultOS published its actual project stack this week - 5 projects, Aeon and Miroshark both named, alongside virtuals_io, gitlawb, reppo. Unprompted. - https://x.com/thecultos/status/2095901737345339655

---
*r/MiroFish* · archetype: community
*Title:* CultOS just published their stack. Miroshark's on it, unprompted.
*Body:*
CultOS runs a paid PR-review/audit service built entirely on Aeon skills. This week they published their actual stack — 5 projects total: Aeon, Miroshark, virtuals_io, gitlawb, reppo.

Nobody asked them to name it. Nobody paid them to. That's the whole signal.

Quick context if you're new here: Miroshark spins up hundreds of grounded agents that argue on X and Reddit while trading a simulated AMM in the same run — belief drift across rounds, director mode to inject breaking news mid-sim, counterfactual branching (fork the timeline like git for a strategic decision). Runs for about $1, under 10 minutes, x402-native so agents can pay for their own inference.

Still early, still shipping in public. Repo's below if you want to see how the sim engine works or run your own.

*Link in post:* https://github.com/miroshark/miroshark
*Post here:* [Open r/MiroFish composer](https://www.reddit.com/r/MiroFish/submit?title=CultOS%20just%20published%20their%20stack.%20Miroshark%27s%20on%20it%2C%20unprompted.)
_notes: this is Miroshark's own community — direct update is normal here, still disclose "I built this," and keep it to one post this cycle._

---
*r/aiecosystem* · archetype: agents
*Title:* Two unrelated groups catalogued the same agent stack this week - neither asked us
*Body:*
Two unrelated groups listed Aeon this week, days apart, no coordination between them.

BaseHubHB's weekly Base-ecosystem watchlist led with Aeon — their "700+ stars" figure checks out live via the GitHub API (715 stars, 256 forks as of today). Then CultOS — who already run a paid PR-review service on Aeon skills — published their full stack: 5 projects, Aeon and Miroshark both named, alongside virtuals_io, gitlawb, and reppo.

Neither post was solicited. That's the part worth flagging in an ecosystem sub — not virality, just two separate builders independently deciding Aeon belongs on their list.

For anyone who hasn't run into it: Aeon is skills-as-markdown running unattended on GitHub Actions — cron, chains, self-repair, no approval loop, MIT licensed. Site + repo below if you want to poke at how it's wired.

*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=Two%20unrelated%20groups%20catalogued%20the%20same%20agent%20stack%20this%20week%20-%20neither%20asked%20us)
_notes: cites third-party validation of my own project — disclose "I work on Aeon" up top so it doesn't read as a neutral roundup._

---
*r/Ollama* · archetype: open-source
*Title:* Own your agent stack: markdown skills + cron on GitHub Actions, no dashboard, no lock-in
*Body:*
If you're the type who'd rather run things yourself than trust a dashboard, the mechanic here might be interesting even if you never touch Aeon itself.

An Aeon "skill" is just a markdown file — SKILL.md, plain instructions plus frontmatter for the schedule. No proprietary DSL, no hosted-only runtime. You commit it to a repo, GitHub Actions runs it on cron, and the agent just runs — no approval loop sitting between the trigger and the action.

It self-repairs too: a health skill scores every run and files issues, repair skills open PRs to fix the broken ones. MIT licensed, 715 stars / 256 forks as of today.

Not selling a platform — closer to "here's a pattern for owning your automation stack." Repo's below if the skills-as-markdown idea is useful to you even outside Aeon.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=Own%20your%20agent%20stack%3A%20markdown%20skills%20%2B%20cron%20on%20GitHub%20Actions%2C%20no%20dashboard%2C%20no%20lock-in)
_notes: this sub skews self-hosting and is allergic to vendor pitches — keep the crypto/x402 stuff out, lead with the open-source mechanic, disclose as builder if asked._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - autonomous agent framework, skills are markdown files, runs on GitHub Actions cron
*Body:*
What it is: an agent framework where every capability is a single markdown file (SKILL.md) — frontmatter sets the schedule, the body is the instructions. No dashboard, no proprietary config format.

Why it's different: it runs unattended. GitHub Actions triggers each skill on cron, there's no approval loop between trigger and action, and a self-repair loop (health skill scores runs, repair skills open PRs) keeps things running without a human babysitting it.

Proof it's not just us using it: CultOS built a paid PR-review/audit service entirely on Aeon skills and named it in their public stack this week alongside Miroshark and a few other projects — none of that was solicited.

Stack: MIT licensed, 715 stars / 256 forks as of today. Repo's the whole pitch, linked below.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20autonomous%20agent%20framework%2C%20skills%20are%20markdown%20files%2C%20runs%20on%20GitHub%20Actions%20cron)
_notes: strict sub rule — title must stay "Aeon - <one-line description>", repo link is the entire point of the post, disclose as builder in the first comment if not obvious._

---
run: expires 2026-09-14 (story 0d old, 10d promo window); likes/star counts as of this run (aeonfun/aeon 715★/256 forks/MIT verified live via gh api); drafts only, nothing posted; seen-file +2 URLs.