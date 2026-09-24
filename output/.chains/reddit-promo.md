ℹ️ Reddit Promo - 2026-09-24

*Reddit Promo - 2026-09-24*
1d since last promo · 4 subs drafted

_Story:_ Aeon's security skill reported a bug to ByteDance/TikTok in May, published the writeup after 134 days of silence, and ByteDance shipped a fix overnight - https://x.com/aaronjmars/status/2103149261663694866

---
*r/Agent_AI* · archetype: agents
*Title:* My autonomous agent framework's security skill got ByteDance to patch a live bug overnight
*Body:*
I work on Aeon, an open-source framework where every capability ("skill") is just a markdown file that runs unattended on a schedule via GitHub Actions - no human approving each run.

One of those skills does vulnerability research. It found a real bug in ByteDance/TikTok back in May, reported it responsibly, and then... silence. 134 days of it.

This week the skill published the writeup publicly (standard practice once a disclosure window closes with no fix). Overnight, ByteDance merged a patch and emailed back: "already known, fixed Aug 2." Writeup + patch are linked from the follow-up post.

What's interesting to me isn't the bug itself, it's that nobody was manually driving this. The skill ran on its own cadence, wrote its own findings, and the pressure of a public paper trail did the rest. That's the actual pitch of autonomous agents to me - not "chatbot that does research," but a process that keeps happening whether or not I'm watching it.

Repo's here if you want to see how the skill is structured: https://github.com/aeonfun/aeon. Happy to answer questions about the disclosure workflow or the framework itself.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=My%20autonomous%20agent%20framework%27s%20security%20skill%20got%20ByteDance%20to%20patch%20a%20live%20bug%20overnight)
_notes: r/Agent_AI tolerates project posts if substantive - keep the "I work on X" disclosure up front (already in body), don't let the ByteDance detail read as an anti-ByteDance callout._

---
*r/StartupMind* · archetype: startup
*Title:* What happened after I published a bug report ByteDance sat on for 134 days
*Body:*
Building in public update: I'm the founder behind Aeon, an open-source autonomous agent framework. Most weeks the traction news is small - a fork, a star, a PR. This week was different.

Back in May, a security skill running inside Aeon found and reported a bug to ByteDance/TikTok. No response for 134 days. This week I published the writeup on our security blog, as-is, with the disclosure timeline included.

ByteDance shipped a fix overnight and emailed back "already known, fixed Aug 2." Whether or not that timeline is exact, the fact that publishing forced movement within a day after 4+ months of silence is the actual story.

I'm not sharing this to dunk on ByteDance - this is a genuinely common pattern in vuln disclosure. I'm sharing it because it's the clearest proof I've had that an unattended process, not me personally emailing people, can move a large company. That's the bet behind the whole project: aeon.fun.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=What%20happened%20after%20I%20published%20a%20bug%20report%20ByteDance%20sat%20on%20for%20134%20days)
_notes: r/StartupMind wants the honest founder voice, not a growth-hacky spin - keep the "not dunking on ByteDance" caveat and the founder disclosure._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - open-source agent framework whose security skill just got ByteDance to ship a fix overnight
*Body:*
Aeon is an open-source, AGPL-licensed framework for running autonomous agents as GitHub Actions - each capability is a markdown "skill" file, scheduled by cron, with no per-run human approval.

What/why: one of the built-in skills does vulnerability research. It found and reported a bug to ByteDance/TikTok in May; after 134 days with no fix, it published the disclosure publicly this week per standard responsible-disclosure practice. ByteDance merged a patch overnight and confirmed it was "already known, fixed Aug 2."

Stack: Claude Code headless runs + GitHub Actions cron + one markdown skill file per capability + a memory dir committed to the repo for state. No always-on server.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20open-source%20agent%20framework%20whose%20security%20skill%20just%20got%20ByteDance%20to%20ship%20a%20fix%20overnight)
_notes: r/CoolGithubProjects requires the exact "Aeon - <description>" title format - keep as-is, disclose "I built this" in a top comment since the title has no room for it._

---
*r/lovingopensourceAI* · archetype: open-source
*Title:* The security researcher in my open-source agent framework is just a markdown skill on a cron job
*Body:*
I keep seeing "AI agent" used to mean a chatbot with tool access. Aeon (open-source, AGPL) is my attempt at the other definition: a process that keeps running without anyone watching it.

Concretely: one skill's whole job is vulnerability research. It's a markdown file with instructions, not code. It runs on a GitHub Actions schedule, does its own research, writes its own findings to the repo, and follows a disclosure timeline on its own.

This week that skill's May report to ByteDance/TikTok (134 days of silence) went public on schedule, and ByteDance shipped a fix overnight afterward. Nobody on our side timed that moment - the skill just did what the schedule said.

If you want to see what one of these skill files actually looks like: https://github.com/aeonfun/aeon. I work on this, not just found it - happy to answer questions about how the skills are structured.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=The%20security%20researcher%20in%20my%20open-source%20agent%20framework%20is%20just%20a%20markdown%20skill%20on%20a%20cron%20job)
_notes: r/lovingopensourceAI is enthusiast-friendly but still flags shills - keep the "I work on this, not just found it" disclosure line._