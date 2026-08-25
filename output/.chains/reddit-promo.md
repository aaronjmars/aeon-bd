ℹ️ Reddit Promo Drafts

*Reddit Promo — 2026-08-25*

_Story:_ Aeon's own security-scanning skill found a high+medium severity vuln in `google/agents-cli`; Google acknowledged and shipped the fix — top-engagement item of the day (216 likes / 39 RTs / 24 replies). — https://x.com/aaronjmars/status/2092006674697437256

_Supporting proof point (not linked directly, folded into "unattended, verifiable" framing):_ AgentOS opened a PR to merge into the Aeon ecosystem the same window — a second concrete, public artifact of unprompted ecosystem integration. — https://x.com/useAgentOS/status/2091906407927042421

---
*r/OpenSourceAI* · archetype: open-source
*Title:* An autonomous agent we run found (and got fixed) a real vuln in Google's own agents-cli
*Body:*
We build Aeon — an open-source (AGPL) agent framework that runs unattended on GitHub Actions, no human approving each step. One of the ~200 skills is a vuln-scanner: it reads a target repo, looks for real exploitable bugs, and opens a PR if it finds one.

This week it flagged a high+medium severity issue in google/agents-cli. Google reviewed it, agreed, and shipped the fix. No bug-bounty back-and-forth, no scope negotiation — an agent found a real problem in a repo it doesn't own, and the maintainers fixed it.

The mechanic behind it is boring on purpose: a "skill" is just a markdown file with instructions plus a cron schedule. This one happens to be pointed at security. The same harness that writes a blog post can read code for exploitable patterns if that's what you tell it to do.

Repo's here if you want to see how the skill is structured: https://github.com/aeonfun/aeon. Happy to answer questions on the scanning loop or the PR flow.

— builder of Aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=An%20autonomous%20agent%20we%20run%20found%20%28and%20got%20fixed%29%20a%20real%20vuln%20in%20Google%27s%20own%20agents-cli)
_notes: r/OpenSourceAI may require a self-promo flair — check before posting; disclose as builder, single link only._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - the autonomous agent framework whose security skill just got a vuln fixed in Google's own repo
*Body:*
Aeon is an open-source (AGPL) framework where "skills" are just markdown files that run on a schedule via GitHub Actions — no approval loop, no human in the runtime path.

This week one of those skills (a vuln scanner) read google/agents-cli, found a high+medium severity bug, and opened a PR. Google confirmed it and shipped the fix. That's the whole pitch for the project in one data point: an unattended agent finding and getting a real fix landed on a repo it doesn't own.

Repo: https://github.com/aeonfun/aeon — skills are all readable there if you want to see how one's built before you'd trust it to run against your own code.

I built this, happy to answer anything.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20the%20autonomous%20agent%20framework%20whose%20security%20skill%20just%20got%20a%20vuln%20fixed%20in%20Google%27s%20own%20repo)
_notes: sub enforces a strict "Aeon - <one-line desc>" title format — don't drift from it; disclose as builder._

---
*r/Agent_AI* · archetype: agents
*Title:* What 'fully unattended' actually looks like: our agent found a real vuln, no human touched it until the PR was already open
*Body:*
A lot of "autonomous agent" claims fall apart once you ask what a human actually did in the loop. Wanted to share one that didn't.

We run Aeon — skills-as-markdown, cron-scheduled, on GitHub Actions, self-repairing when a skill breaks. One skill is a security scanner. This week it read google/agents-cli, found a high+medium severity vulnerability, and opened a PR. Google reviewed and shipped the fix. The only human step in the whole chain was Google's own review — ours ran cold, start to finish.

Not claiming this replaces audits or professional pentesting — it's one data point on what a scheduled, unattended agent can surface when you give it a narrow job and don't gate every step with a human. Separately, another agent team (AgentOS) opened a PR to integrate with our stack this same week — also unprompted, also just a public PR you can go read.

Repo + the skill's source: https://github.com/aeonfun/aeon. Curious what other agent-framework builders here are doing for unattended verification loops.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=What%20%27fully%20unattended%27%20actually%20looks%20like%3A%20our%20agent%20found%20a%20real%20vuln%2C%20no%20human%20touched%20it%20until%20the%20PR%20was%20already%20open)
_notes: keep tone comparative, not trash-talk (no vendor-vs-vendor); disclose as builder; check self-promo ratio before posting._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* One markdown skill just got a real vuln fixed on a Google repo - here's roughly what it looks like
*Body:*
If you're already deep in Claude Code skills, this is just a skill running unattended on a schedule — but the outcome was concrete enough to share.

Aeon runs ~200 skills, all just SKILL.md files plus a cron entry. One of them is a vuln scanner: reads a target repo, looks for exploitable patterns, opens a PR if it finds something real. This week it flagged a high+medium severity issue in google/agents-cli. Google reviewed it and merged the fix.

Roughly the shape (simplified):
```
name: vuln-scanner
schedule: cron
steps: clone target repo -> static + agentic review for exploitable patterns -> draft PR with repro + fix -> open on target
```
No custom infra beyond the harness — it's the same skill format you'd write for anything else, just pointed at security instead of content.

Repo (skills are all readable, it's AGPL) if anyone wants to see the real one: https://github.com/aeonfun/aeon.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=One%20markdown%20skill%20just%20got%20a%20real%20vuln%20fixed%20on%20a%20Google%20repo%20-%20here%27s%20roughly%20what%20it%20looks%20like)
_notes: technical audience, keep the skill snippet honest/short; disclose as builder; single link only._

🔗 https://x.com/aaronjmars/status/2092006674697437256