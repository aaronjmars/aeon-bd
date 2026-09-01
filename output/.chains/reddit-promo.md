**Reddit Promo - 2026-09-01**
**0d since last promo** · 4 subs drafted

⚠️ **cadence flag: same-day second dispatch.** An earlier run today already promoted the Miroshark x402aff story (r/MiroFish, r/Agent_AI, r/aiecosystem). Subs below are fully disjoint from that batch, but if the feed feels heavy, hold this one for tomorrow — Reddit self-promo only works when it stays occasional.

_Story:_ Aeon's vuln-scanner skill ran responsible disclosure end-to-end, unattended — flagged an issue in synthetic-sciences/openscience (3.3k★ OSS research workbench), filed a private advisory + fix PR, asked the maintainer for feedback in public - [the tweet](https://x.com/aeonframework/status/2094047486222442924)

---

**r/OpenSourceAI** · archetype: open-source
**Title:** Responsible disclosure when the reporter is an autonomous agent

**Body:**

This week our agent flagged a vulnerability in synthetic-sciences/openscience, a 3.3k-star open-source research workbench. It wrote a private advisory, opened a fix PR, and posted a public reply asking the maintainer for feedback. Nobody on our team touched it — the whole sequence ran on a schedule.

The etiquette is the interesting part, because the reporter being an agent changes nothing about the courtesy owed: private first, never public-shame, include a fix attempt, leave the maintainer the final say. Those rules live in the same markdown file as the scan rules. When your policy is text, you can read it before you trust the agent.

We got here because point-in-time audits stopped matching the threat. Audit after audit didn't save Balancer from a $128M exploit — attackers iterate continuously, annual audits don't. Compute got cheap enough that scanning 24/7 now costs less than one audit, so the scanner is a cron job: pick a repo, read the code, write it up, disclose politely, attempt a patch.

Disclosure: I built Aeon. Run logs are public on GitHub so you can watch it work — and watch it fail, it does that too. Open source, MIT: https://github.com/aeonfun/aeon

Honest question for maintainers: would you want an agent-filed advisory in your inbox? If you'd say yes-but-only-if to a human researcher, tell me the rules and I'll put them in the skill.

**Link in post:** https://github.com/aeonfun/aeon
**Post here:** [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Responsible%20disclosure%20when%20the%20reporter%20is%20an%20autonomous%20agent)
_notes: check self-promo rules + required flair; post as the builder (disclosure line is in the body). Do NOT state severity or claim the issue is fixed — advisory was private-first, fix awaits maintainer review. Reply to comments as the author._

---

**r/CLaudeSkills** · archetype: claude-skills
**Title:** The vulnerability scanner is a markdown file on a cron schedule

**Body:**

People expect a security scanner to be a service with dashboards. Ours is a markdown file. Frontmatter declares what it needs — API keys, a cron entry. The body is a runbook: pick a target repo, read the relevant code paths, write findings in the maintainer's format, file the advisory privately, attempt a patch, ask for feedback. The framework schedules it on GitHub Actions and gets out of the way.

This week it ran against synthetic-sciences/openscience (3.3k stars): flagged an issue, private advisory, fix PR, public reply asking the maintainer for feedback. The disclosure rules sit in the same markdown as the scan rules — private first, no shaming, patch attempt included. That's the part I'd highlight for this crowd: when the etiquette is just text, you can audit the policy before the agent ever runs.

The shape is identical to the Claude-style skills you already write. What the framework adds is the scheduler, persistent memory, and a self-repair loop, so the skill keeps running unattended instead of dying quietly the second week.

Not just our own opinion: a third-party team (CultOS) just stamped "powered by an Aeon framework skill" on their paid PR-review service — agents built on these skills are earning real money per review.

Repo (MIT), skill format readable in a minute: https://github.com/aeonfun/aeon — happy to walk through the SKILL.md anatomy if anyone wants it. I work on Aeon.

**Link in post:** https://github.com/aeonfun/aeon
**Post here:** [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=The%20vulnerability%20scanner%20is%20a%20markdown%20file%20on%20a%20cron%20schedule)
_notes: skills subs often require a specific flair/tag — check before posting; post as the builder; 9:1 self-promo ratio applies. Don't claim the openscience issue is fixed._

---

**r/lovingopensourceAI** · archetype: open-source (enthusiast)
**Title:** I built an agent framework that files security advisories on open-source repos while I sleep

**Body:**

True story from this week: an agent I configured found an issue in an open-source science workbench (3.3k stars), sent the maintainers a private advisory, opened a suggested fix, and asked politely whether the patch was useful. I was asleep. There was no step where I clicked approve.

I built Aeon because "set up a bot" usually means babysitting a bot. This is the opposite: skills are plain markdown files, they run on GitHub Actions on a schedule, and everything the agent does lands in public run logs — so you can check on it any time, and so can everyone else. If it breaks, it repairs itself and you read about it in the log after.

The security part matters to me because open-source maintainers are outnumbered. Attackers iterate for free; defenders get an audit a year, if that. A cheap scanner that runs every night and behaves itself — private disclosure first, never naming-and-shaming, patch included — feels like the least we owe the commons.

It's open source and yours to run: https://github.com/aeonfun/aeon

Questions welcome — I'm the person who built it. What would you want an agent like this to do (or never do) on your repos?

**Link in post:** https://github.com/aeonfun/aeon
**Post here:** [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=I%20built%20an%20agent%20framework%20that%20files%20security%20advisories%20on%20open-source%20repos%20while%20I%20sleep)
_notes: builder posts fine but disclose — disclosure line is in the body; answer replies as the author. No severity/fixed claims on the openscience advisory._

---

**r/CoolGithubProjects** · archetype: github
**Title:** Aeon - an open-source agent framework that runs unattended on GitHub Actions and files its own security advisories

**Body:**

**What:** Aeon turns plain markdown "skills" into scheduled autonomous agents. Each skill is a SKILL.md file (runbook + required keys), scheduled via GitHub Actions cron, with chains for multi-step workflows, memory that persists across runs, and self-repair — when a run fails, the agent debugs and fixes itself, on the record.

**Why:** every agent framework I tried needed a server, a dashboard, and a human approval loop. Aeon runs on GitHub Actions with public run traces, so you can verify what your agent actually did — and so can anyone auditing it. No approval loop is the feature: it ships, it breaks, it fixes itself.

**Recent:** a 14-feature drop including score-gated chains (a step only proceeds if the previous output clears a quality bar — quality as control flow), a soul gallery (personality files so agents write like you), and a gateway cascade (auto-failover across model providers so runs survive an outage). This week one scheduled skill filed a private security advisory + fix PR against a 3.3k-star OSS repo, end to end, unattended.

**Stack:** runs on GitHub Actions free tier, MIT, 712★ · drives Claude Code, Codex, Grok and other harnesses under one scheduler.

Repo: https://github.com/aeonfun/aeon — I'm the author, feedback and questions welcome.

**Link in post:** https://github.com/aeonfun/aeon
**Post here:** [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20an%20open-source%20agent%20framework%20that%20runs%20unattended%20on%20GitHub%20Actions%20and%20files%20its%20own%20security%20advisories)
_notes: strict title format here ("Project - description") — title above already follows it, don't reword; use the sub's project flair if required; builder disclosure is in the body. Don't claim the openscience vuln is fixed._

---

**skipped this run:** svector_eth hire announcement (94 likes, loudest post of the window) — team news, weak Reddit material; eyebrowCC's unsolicited-PR courtship (31 likes) — BD thread, engagement-act's lane; BaseHubHB Base-ecosystem watchlist (7 likes) — genuine third-party validation but crypto-framed, held fresh for an ecosystem story; Miroshark-on-Locus (unseen, 4d) — Miroshark was today's earlier headline, left for its own run; "Aeon vs bot" comparison thread — standing vendor-vs-vendor skip.

_run: source = today's two fetch-tweets runs (09-01 morning + 17:04, plus the 17:33 dispatch logs) · seen-file +3 URLs (story, 14-features tweet, CultOS stamp) · story 1d old, window closes 2026-09-11 · likes as-of fetch runs · verified live this run via gh api: aeonfun/aeon 712★/254 forks MIT, synthetic-sciences/openscience 3383★ TypeScript · unverified "Google/SpaceX/Alibaba" claim excluded per standing rule · drafts only — nothing posted_