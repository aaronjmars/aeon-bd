ℹ️ Reddit Promo - 2026-09-03

*Reddit Promo - 2026-09-03*
1d since last promo · 3 subs drafted

_Story:_ Aeon's own account points agent builders at UsePodAI as a cheaper-inference option for their Aeon agents - one of the framework's existing auto-routed gateways, called out as a concrete cost lever - https://x.com/aeonframework/status/2095109716636577888

---
*r/Agent_AI* · archetype: agents
*Title:* Why we let our agent framework choose its own inference provider
*Body:*
Aeon is an open-source agent framework - skills are just markdown files, it runs unattended on GitHub Actions, no approval loop. One decision that's paid off: we never hard-locked it to a single model provider.

Aeon auto-routes inference across multiple gateways - Anthropic direct, OpenRouter, Bankr, Venice, and UsePodAI - picked by whichever agent needs to run and what it costs. This week we flagged UsePodAI directly to builders as the cheaper option for running Aeon agents - a concrete cost lever, not a partnership announcement.

The mechanic behind it: an agent's cost profile isn't static. A skill running once a day on cron doesn't need the same inference tier as one debugging a live PR. Routing lets the framework pick per-job instead of the builder eating one flat bill.

Repo's open, MIT: https://github.com/aeonfun/aeon

Happy to go deeper on how the routing logic works if useful.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=Why%20we%20let%20our%20agent%20framework%20choose%20its%20own%20inference%20provider)
_notes: r/Agent_AI - agent-framework audience, compare on mechanics not marketing; disclose as the builder ("I work on Aeon"), check current self-promo ratio/flair before posting._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Every skill in our agent framework is a markdown file - the runtime decides which model pays for it
*Body:*
Aeon is an open-source framework where each agent capability ("skill") is just a SKILL.md file - frontmatter for schedule/mode, then instructions in plain English. No SDK boilerplate per skill.

What's less obvious: the framework doesn't hardcode which model runs a skill. It auto-routes inference across gateways (Anthropic direct, OpenRouter, Bankr, Venice, UsePodAI) based on cost and availability. This week we called out UsePodAI specifically as a cheaper option for builders running Aeon agents at volume - cron jobs add up fast if every run hits the priciest tier.

Practical upshot: you write the skill once in markdown, the routing decides where the tokens actually get spent. You can still pin a specific gateway per skill if you want deterministic behavior.

Repo's here, MIT licensed, worth a look at the skills folder if you want to see the shape: https://github.com/aeonfun/aeon

Ask away if you're building something similar.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Every%20skill%20in%20our%20agent%20framework%20is%20a%20markdown%20file%20-%20the%20runtime%20decides%20which%20model%20pays%20for%20it)
_notes: r/AIPromptProgramming - technical audience, keep the skills-as-markdown mechanic front and center, not the cost pitch; disclose as the builder, check self-promo ratio before posting._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Open-source agent framework that lets you swap inference providers without touching code
*Body:*
Aeon's an open-source (MIT) framework for running autonomous agents - no approval loop, skills defined as markdown files, scheduled via GitHub Actions cron. 714 stars, still shipping weekly.

One thing that's easy to miss on first read: it doesn't lock you to one model provider. Aeon auto-routes inference across several gateways under the hood - Anthropic direct, OpenRouter, Bankr, Venice, and UsePodAI - so a skill can run on whichever is cheapest or fastest for that job. This week the team flagged UsePodAI directly to builders as a lower-cost option for running Aeon agents.

If you've hit the "every agent run costs real money" wall, this is the actual fix - not a discount code, routing at the framework level.

Code's here if you want to see how the gateway logic is wired: https://github.com/aeonfun/aeon

Open to questions on the routing setup or anything else in the repo.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Open-source%20agent%20framework%20that%20lets%20you%20swap%20inference%20providers%20without%20touching%20code)
_notes: r/OpenSourceAI - lead with open-source + how it works, not the sell; disclose as the builder, check current self-promo ratio/flair before posting._