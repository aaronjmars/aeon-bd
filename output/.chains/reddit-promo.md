ℹ️ Reddit Promo

*Reddit Promo — 2026-08-22*

_Story:_ Third-party web3 security researcher (pashov) added Aeon to his curated GitHub list of AI-driven web3 security tools, unprompted, unpaid — https://x.com/0xFireFist/status/2090731542364438614

---
*r/OpenSourceAI* · archetype: open-source
*Title:* a security researcher added Aeon to a curated web3-security tools list, unprompted
*Body:*
pashov (well-known web3 security auditor) maintains a curated GitHub list of AI-driven web3 security tooling. this week Aeon showed up on it. nobody asked, nobody paid — it just got added as a real defensive project people are actually running.

context: Aeon has been running its own vuln-scanner fleets against real open-source repos (Vercel, Alibaba, Perplexity, OpenClaw) — agents that find exploits and open actual PRs to fix them. the thesis: audits alone don't scale (Balancer ran 11 audits and still got hacked for $128M), so tokenize the security work and let agents scan 24/7 instead of a point-in-time check.

Aeon itself is open source (AGPL) — the whole framework is "skills" written as plain markdown files that run on GitHub Actions cron, no approval loop, self-repairing when a skill breaks. the vuln-scanner is one skill among ~200.

repo's here if you want to see how a skill is actually structured: https://github.com/aeonfun/aeon

happy to answer questions on the self-repair loop or the scanner mechanics.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=a%20security%20researcher%20added%20Aeon%20to%20a%20curated%20web3-security%20tools%20list%2C%20unprompted)
_notes: disclose as the builder, not a neutral discoverer — check r/OpenSourceAI's self-promo flair/ratio rule before posting._

---
*r/aiecosystem* · archetype: agents
*Title:* where 'autonomous' agent frameworks actually diverge: got a data point this week
*Body:*
most "agentic framework" comparisons are marketing copy. here's an actual one: a third-party security researcher (pashov, does web3 audits) curates a list of AI-driven web3 security tools on GitHub. this week Aeon — a framework I built — got added, for running autonomous vuln-scanner agents that open real PRs on real repos, unattended.

the distinction that matters in this category isn't model quality, it's autonomy: does the agent need a human in the loop to act? Aeon's answer is cron + self-repair — skills run on GitHub Actions on a schedule, and when a skill breaks, another skill fixes it and reopens the PR. no approval gate. most agent frameworks are "you drive" — this is closer to "it drives, you watch the public traces."

site: https://aeon.fun if you want to see the shape of it.

curious what other frameworks people here have seen actually running unattended vs. needing a human to approve every loop.
*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=where%20%27autonomous%27%20agent%20frameworks%20actually%20diverge%3A%20got%20a%20data%20point%20this%20week)
_notes: keep the framing comparative, not salesy — disclose as the builder up front._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - the most autonomous agent framework, just got added to a curated web3-security tools list
*Body:*
what: Aeon is an open-source (AGPL) framework where every capability is a "skill" — a plain markdown file — that runs unattended on GitHub Actions cron. no approval loop, self-repairing (skills that break get fixed by other skills, PR'd automatically).

why this is here: this week a third-party web3 security researcher (pashov) added Aeon to his curated list of AI-driven security tooling, unprompted. context: one of Aeon's ~200 skills is a vuln-scanner fleet that finds exploits in real open-source repos (Vercel, Alibaba, Perplexity, OpenClaw) and opens real PRs to fix them.

stack: Claude Code / Codex / OpenClaw as the underlying harness, GitHub Actions for the runtime, markdown for the skill layer.

repo: https://github.com/aeonfun/aeon
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20the%20most%20autonomous%20agent%20framework%2C%20just%20got%20added%20to%20a%20curated%20web3-security%20tools%20list)
_notes: sub enforces a strict title format ("Aeon - <one-line desc>") — kept as-is; disclose as builder in a top comment if their rules require it._

---
*r/StartupMind* · archetype: startup
*Title:* small but real traction update: a third party added us to their curated list, unprompted
*Body:*
building-in-public update — nothing engineered, just logging it because it's the kind of signal that's hard to fake.

I built Aeon, an open-source autonomous agent framework. this week a web3 security researcher (pashov, does audits for a living) added Aeon to his curated GitHub list of AI-driven web3 security tools. we didn't submit it, didn't pay for placement, didn't know until someone tweeted it.

why it happened: one of Aeon's skills runs autonomous vuln-scanner fleets against real repos and opens actual fix PRs — turning the "audits don't scale" problem (see: Balancer, 11 audits, still hacked for $128M) into something that runs 24/7 instead of once. apparently different enough to get noticed by someone who reviews this space for a living.

site: https://aeon.fun

happy to talk through the mechanics if anyone's building something adjacent — not selling anything here, just sharing the traction beat.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=small%20but%20real%20traction%20update%3A%20a%20third%20party%20added%20us%20to%20their%20curated%20list%2C%20unprompted)
_notes: r/StartupMind values honest traction over growth-hacky tone — keep to "here's a real thing that happened," disclose as founder._