ℹ️ Reddit Promo - 2026-08-27 (run 2)

*Reddit Promo - 2026-08-27*
0d since last promo · **second run today** (earlier 2026-08-27 dispatch already promoted the autonomous-deploy story to r/Agent_AI, r/CoolGithubProjects, r/OpenSourceAI, r/StartupMind) · 4 subs drafted

_Story:_ Aeon shipped a native Cursor workflow - enable/schedule/edit skills, wire secrets + channels, mine old chats into new skills, no dashboard needed - https://x.com/aaronjmars/status/2092687201947554035

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* Aeon skills are literally markdown files - just showed off running/scheduling them from inside Cursor
*Body:*
If you're already writing Claude-style SKILL.md files, Aeon (an open-source agent framework) uses the exact same shape - frontmatter + markdown instructions, triggered by cron instead of a chat turn. This week the founder showed running a whole Aeon instance from inside Cursor: enabling/scheduling/editing skills, wiring up secrets and notification channels, and even mining past chat history into new scheduled skills - all without leaving the editor.

It's a genuinely new surface (previously GitHub-dashboard-only), so the whole lifecycle - write a skill, test it, schedule it, watch it run unattended on GitHub Actions - now happens in one place. Separately, an unaffiliated account wrote up a "pick Aeon if you want host-free, self-repairing cron" breakdown this week, which is close to how I'd describe the pitch myself.

I work on Aeon. Happy to show the actual skill file format if anyone's curious how close it maps to Claude Code skills.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=Aeon%20skills%20are%20literally%20markdown%20files%20-%20just%20showed%20off%20running%2Fscheduling%20them%20from%20inside%20Cursor)
_notes: technical sub, skip sales language, lead with the skill-file parity; disclose "I work on Aeon" per sub norms._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* An agent framework you can now fully manage from inside Cursor - schedule/edit/deploy skills without touching a dashboard
*Body:*
Been following Aeon (open-source agent framework, runs unattended on GitHub Actions via cron + markdown "skills") and this week they added a Cursor-native workflow - enable a skill, schedule it, edit its instructions, wire secrets and notification channels, even turn old chat history into a new scheduled skill, all from inside the editor instead of a web dashboard.

What's different from a lot of agent tooling: there's no daemon you have to keep running yourself - the agent's loop is a scheduled GitHub Actions job, self-repairing when a skill starts failing, with every run's trace public. An independent account wrote up when they'd reach for this over a hosted-daemon setup like Hermes, worth a read if you're weighing the tradeoff.

I built this - ask me anything about the Cursor integration or the skill format.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=An%20agent%20framework%20you%20can%20now%20fully%20manage%20from%20inside%20Cursor%20-%20schedule%2Fedit%2Fdeploy%20skills%20without%20touching%20a%20dashboard)
_notes: comparison mention should stay descriptive not a dunk on Hermes; disclose builder status; keep to one link._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* vibe-coded my agent's entire schedule from inside Cursor this week, no dashboard needed
*Body:*
Small but genuinely useful thing that shipped this week: I can now spin up and manage a whole Aeon agent (open-source, runs on GitHub Actions on a cron) from inside Cursor. Enable a skill, schedule it, tweak the instructions, hook up secrets/notifications - even feed it old chat logs and have it turn that into a new scheduled skill. Didn't touch the GitHub dashboard once.

Feels like the natural place for this kind of thing to live - you're already vibe-coding in the editor, now the "make this run itself forever" step is right there too.

I'm the builder, this is my own project - happy to answer questions or show the setup.

https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=vibe-coded%20my%20agent%27s%20entire%20schedule%20from%20inside%20Cursor%20this%20week%2C%20no%20dashboard%20needed)
_notes: casual/first-person tone fits the sub; still disclose it's your own project; keep self-promo to the one link, no repeat pushes._

---
*r/lovingopensourceAI* · archetype: open-source
*Title:* Open-source agent framework you can now run/schedule entirely from Cursor
*Body:*
Sharing because I like seeing open tools get easier to actually use: Aeon (AGPL, skills-as-markdown, cron + chains on GitHub Actions) shipped a Cursor-native workflow this week - manage the whole agent lifecycle (enable/schedule/edit skills, wire secrets and channels) without leaving the editor or touching a dashboard.

Nothing about it requires a hosted service - it's still just a repo, a schedule, and markdown files you can read end to end. The Cursor integration is just a friendlier way in.

I work on Aeon - happy to answer questions about the setup or the skill format.

Repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=Open-source%20agent%20framework%20you%20can%20now%20run%2Fschedule%20entirely%20from%20Cursor)
_notes: enthusiast OSS crowd, "what I built + why it's open" framing; disclose "I work on Aeon."_