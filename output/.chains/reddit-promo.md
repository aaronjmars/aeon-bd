*Reddit Promo — 2026-08-15*

_Story:_ Aeon shipped Buzz (Jack Dorsey's open-source group chat app) as a supported channel this week, alongside an ADK explainer repositioning Aeon as embeddable infra — https://x.com/aeonframework/status/2088225133529882938

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Shipped support for Buzz (Jack Dorsey's open-source group chat app) in my agent framework this week
*Body:*
I build Aeon (AGPL, repo below) — an agent framework that runs unattended on GitHub Actions instead of a chat window you babysit. This week we added Buzz as a supported channel, so agents can post into Buzz group chats the same way they already do on Telegram/Discord/Slack.

Mechanically it's simple: each "channel" in Aeon is just a notify adapter — read the message, format it, send it. Adding Buzz was writing one more adapter, not a rearchitecture. That's the actual argument for skills-as-markdown: new integration surfaces stay cheap because the core loop (cron → skill → notify) never changes.

Same week we pushed an explainer repositioning Aeon as embeddable infra rather than a standalone bot — the pitch is "wire autonomous agents into whatever you're already building," not "come use our bot." A builder outside the team independently made a similar comparison this week, unprompted — always a better signal than us saying it about ourselves.

Repo: https://github.com/aeonfun/aeon — AGPL, skills are literally markdown files. Happy to answer questions on the Buzz integration or the harness itself.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Shipped%20support%20for%20Buzz%20%28Jack%20Dorsey%27s%20open-source%20group%20chat%20app%29%20in%20my%20agent%20framework%20this%20week)
_notes: post as "I built this" (disclosure), not a neutral discoverer — r/OpenSourceAI is fine with self-promo when it's substantive, keep it that way._

---
*r/LovingAI* · archetype: open-source
*Title:* An AI agent framework that runs itself - no chat window, no babysitting
*Body:*
Most AI tools still need you sitting there typing prompts. Aeon runs on a schedule (GitHub Actions, cron) and just does stuff — ships features, watches for issues, posts updates — without anyone approving each step along the way.

This week it picked up support for Buzz (Jack Dorsey's new open-source group chat app) as a place it can post into, alongside Telegram/Discord/Slack it already had. Small thing on its own, but it's part of a bigger push this week to make Aeon plug into whatever tools you're already using instead of being a separate app you have to go check.

If "AI that acts before you check on it" sounds interesting rather than scary: https://aeon.fun — I'm the builder, ask me anything about how it stays unattended without going off the rails.
*Link in post:* https://aeon.fun
*Post here:* [Open r/LovingAI composer](https://www.reddit.com/r/LovingAI/submit?title=An%20AI%20agent%20framework%20that%20runs%20itself%20-%20no%20chat%20window%2C%20no%20babysitting)
_notes: disclose as builder ("I built this"); keep jargon low, this sub is general AI-enthusiast, not technical._

---
*r/Ollama* · archetype: open-source
*Title:* Self-hosted agent framework that runs on GitHub Actions cron, no local server required
*Body:*
If you're into owning your AI stack, Aeon's worth a look — it's the opposite of a hosted SaaS agent. You fork the repo, it runs on your own GitHub Actions cron, and nothing about it depends on a company staying up. No approval-loop chat interface either — configure skills once and it runs.

Shipped a couple things this week: Buzz (Jack Dorsey's open-source group chat app) as a new output channel, and an explainer on wiring Aeon's agents into other products as infra rather than running it as a standalone bot. The harness is provider-agnostic, so if you're already serving local models it'll point at whatever you're running.

Repo: https://github.com/aeonfun/aeon — AGPL, skills are markdown files you can read in five minutes. Happy to talk through the self-hosting setup.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=Self-hosted%20agent%20framework%20that%20runs%20on%20GitHub%20Actions%20cron%2C%20no%20local%20server%20required)
_notes: disclose as builder; lead with own-your-stack framing — this sub skews self-hosting-first, already reflected above._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - autonomous agent framework that ships features on GitHub Actions with no approval loop
*Body:*
What it is: an agent framework that runs unattended on cron via GitHub Actions — no chat window, no human approving each step. Skills are just markdown files.

Why it's cool: this week it shipped support for Buzz (Jack Dorsey's open-source group chat app) as a new output channel — one more adapter added to the same notify loop it already uses for Telegram/Discord/Slack. Same week, pushed a doc positioning the whole thing as embeddable infra you can wire into your own product, not just a standalone bot.

Stack: GitHub Actions + Claude Code, AGPL license, public run traces — you can watch it work instead of just trusting that it worked.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20autonomous%20agent%20framework%20that%20ships%20features%20on%20GitHub%20Actions%20with%20no%20approval%20loop)
_notes: disclose as builder; follow the sub's strict "Aeon - <one-line desc>" title rule exactly (done above) — don't deviate._