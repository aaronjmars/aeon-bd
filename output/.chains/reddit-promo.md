ℹ️ Reddit Promo — 2026-08-18

*Reddit Promo — 2026-08-18*

_Story:_ Aaron reworked Aeon + Miroshark's GitHub repo visuals so the architecture reads at a glance instead of requiring a docs dig, paired with this week's shipped skill-update digest feature (instances now push what changed straight to the operator) — https://x.com/aaronjmars/status/2088095553649528979

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - open-source agent framework that runs unattended on GitHub Actions (skills are just markdown)
*Body:*
just reworked the repo's README/visuals so you can see how it actually works at a glance instead of digging through docs.

what it is: skills are markdown files (SKILL.md), each one runs on a cron via GitHub Actions - no dashboard to babysit, no approval loop. add a skill, it ships. write access is scoped (write vs read-only mode per skill), and every run leaves a public trace in the repo so you can see exactly what it did and when.

shipped this week: instances can now push daily/weekly skill-update digests straight to you, so you're not manually diffing the repo to see what changed.

open source, AGPL. repo: https://github.com/aeonfun/aeon

built and maintain this - happy to answer anything about the architecture.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20open-source%20agent%20framework%20that%20runs%20unattended%20on%20GitHub%20Actions%20%28skills%20are%20just%20markdown%29)
_notes: strict sub rule — title must stay "Aeon - <one-line desc>", nothing added. Post as builder ("I built this"), not anonymously._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* reworked our agent framework's repo so "how it works" is legible at a glance (AGPL, skills-as-markdown)
*Body:*
most open-source agent repos make you read the whole codebase to understand the architecture. we just went through and fixed that for Aeon — visuals + structure now show the skill/cron/chain model up front instead of burying it in prose docs.

the actual mechanic: every capability is a SKILL.md file (plain markdown), scheduled via GitHub Actions cron. no standing server, no approval loop — it just runs on schedule and commits/PRs the result. write-mode skills can open PRs; read-only skills can't touch the repo at all, enforced by the sandbox, not just convention.

shipped alongside this: instances can now push you a digest of what skills changed, so following an actively-developed fork doesn't mean re-reading the diff yourself.

repo (AGPL, fork and configure it yourself): https://github.com/aeonfun/aeon

I work on Aeon — ask me anything about the design, or where it breaks.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=reworked%20our%20agent%20framework%27s%20repo%20so%20%27how%20it%20works%27%20is%20legible%20at%20a%20glance%20%28AGPL%2C%20skills-as-markdown%29)
_notes: disclose builder status up top, watch the sub's self-promo ratio (mix in non-Aeon comments before/after)._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* our skill-update digest is itself just a SKILL.md — shipped this week, here's the shape
*Body:*
if you're already writing Claude-style markdown skills, this might be useful: we just shipped a feature in Aeon where any instance can push you a daily/weekly digest of what skills changed — new ones added, existing ones edited — without you having to diff the repo by hand.

it's built the same way every Aeon capability is: a self-contained SKILL.md with frontmatter (name, mode: write/read-only, schedule) and a body of plain-English instructions. the agent reads the file and executes it headless via GitHub Actions — no orchestration code, no framework glue, just markdown the agent follows.

we also just reworked the repo layout/visuals so the skill model reads clearly from the README instead of requiring a dig through the codebase.

repo: https://github.com/aeonfun/aeon — happy to share the actual digest skill's markdown if anyone wants the real thing, not just the pitch.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=our%20skill-update%20digest%20is%20itself%20just%20a%20SKILL.md%20-%20shipped%20this%20week%2C%20heres%20the%20shape)
_notes: technical audience — lead with the mechanic, not the pitch; disclose "I work on Aeon."_

---
*r/Ollama* · archetype: open-source
*Title:* self-hosted agent framework, just made the repo actually legible if you're evaluating it
*Body:*
posting here because the self-hosting crowd usually asks the right questions before adopting something. Aeon is an open-source (AGPL) agent framework — you fork it, configure skills, and it runs entirely on your own GitHub Actions. no vendor API sitting in the middle deciding what you can/can't automate, no approval loop gating each run.

just went through and reworked the repo's visuals/README so the actual architecture — skills as markdown files, cron scheduling, write vs read-only sandboxing — is visible on the repo page instead of buried three docs deep. also shipped a feature this week where your instance can push you a digest of what skills changed, useful if you're tracking upstream after forking.

repo: https://github.com/aeonfun/aeon — if you're already running local models, curious what you'd want an unattended agent to actually do for you.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=self-hosted%20agent%20framework%2C%20just%20made%20the%20repo%20actually%20legible%20if%20youre%20evaluating%20it)
_notes: not Ollama-specific — keep the ask genuinely open-ended (local-model use case) so it doesn't read as off-topic self-promo; disclose builder status._