ℹ️ Reddit Promo - 2026-09-23

*Reddit Promo - 2026-09-23*
4d since last promo · 3 subs drafted

_Story:_ A community builder shipped "claim-audit," an open Aeon skill pack that re-verifies agent claims against source (gh api/gitlab/HTTP) instead of trusting summaries, grading evidence E0-E4 - registry PR open, CI green - https://x.com/ai2humannetwork/status/2102702154410799131

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* Aeon skills are just markdown files - someone in the community just proved it by shipping a claim-verifier
*Body:*
been building aeon (open source agent framework, skills defined as markdown files that run on cron via GitHub Actions) and the best proof it works isn't anything we shipped - it's what other people build on top without asking permission.

a builder (ai2humannetwork on X) just opened a registry PR for "claim-audit" - a new skill that re-verifies what other agents claim. it checks claims against source (gh api, gitlab, plain HTTP) and grades the evidence E0 through E4 instead of trusting the agent's own summary. we already have skills that repair themselves and skills that prove their own output, but nothing that audits a *different* agent's claims - this fills that gap and we didn't have to build it.

every skill in the framework has the same shape - a frontmatter block plus a markdown body the agent reads as instructions each run. real example from one of our own skills:

```yaml
---
type: Skill
name: BD Radar
description: Business-development radar across your product family...
requires: [TWITTER_API_KEY, XAI_API_KEY?, GH_READ_PAT?]
---
```

then plain english describing the job. no plugin API, no SDK - if you can write markdown you can write a skill. claim-audit's PR is open against the registry, CI's green.

repo if you want to see the pattern: https://github.com/aeonfun/aeon

happy to answer questions about how the skill/cron/repair loop works.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=Aeon%20skills%20are%20just%20markdown%20files%20-%20someone%20in%20the%20community%20just%20proved%20it%20by%20shipping%20a%20claim-verifier)
_notes: disclose as builder in the first line (done); no flair required as of last check, but confirm before posting._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* I built an open source (AGPL) agent framework and someone extended it without asking permission
*Body:*
aeon is an open source (AGPL) agent framework - the whole thing runs as "skills," which are just markdown files with instructions, dispatched on a cron via GitHub Actions. no approval loop, no central plugin store you have to publish through.

that design means people can extend it without going through us. this week a community builder (ai2humannetwork) opened a PR adding a new skill called "claim-audit" - it re-verifies what other agents claim by checking the actual source (github api, gitlab, plain http requests) instead of trusting the agent's own summary, and grades the evidence E0 through E4. registry PR is open, CI's green.

we didn't design for this specific use case. the framework being fully open and markdown-native meant someone could just build it and submit it - that's the actual test of "open source," not just the license file.

repo, if you want to look at how skills are structured or fork it yourself: https://github.com/aeonfun/aeon

I work on Aeon - happy to answer questions about the cron/skill/self-repair loop.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=I%20built%20an%20open%20source%20%28AGPL%29%20agent%20framework%20and%20someone%20extended%20it%20without%20asking%20permission)
_notes: disclose as builder in the first line (done); keep to the one link, skip hype language - this sub tends to welcome show-your-work OSS posts but not sales copy._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* The real test for an agent framework: can someone else extend it without you in the loop
*Body:*
most "agent framework" claims fall apart the second someone outside the core team tries to build on it - undocumented internals, a plugin API that's really a private API, a PR queue that never moves.

aeon's version of that test just passed. a community builder (ai2humannetwork) shipped "claim-audit" - a new skill that re-verifies other agents' claims against source (gh api / gitlab / http) instead of trusting their own summaries, grading evidence E0-E4. it fills a real gap - we have skills that repair themselves and skills that prove their own output, nothing that audits a *different* agent's claims. PR's open against the registry, CI green, no back-and-forth needed from us to make it work.

that's the actual autonomy test for a framework, not just "can it run a loop unattended" (it can - cron + GitHub Actions, no approval gate) but "can someone else's agent extend it without you in the loop." skills are markdown plus a frontmatter block, so the barrier to contributing one is close to zero.

repo: https://github.com/aeonfun/aeon

genuinely curious what this sub thinks the right bar for "extensible agent framework" should be.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=The%20real%20test%20for%20an%20agent%20framework%3A%20can%20someone%20else%20extend%20it%20without%20you%20in%20the%20loop)
_notes: disclose as builder in the first line (done); this sub is more debate-friendly - keep the closing question genuine, not a growth-hack CTA._