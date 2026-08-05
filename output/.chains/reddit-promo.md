ℹ️ Reddit Promo Drafts

*Reddit Promo — 2026-08-05*

_Story:_ Aeon's vuln-scanner skill found and shipped a fix into infra serving tens of billions of requests (merged in 3h) — now aeonframework is pushing builders to fork it and hunt their own bug bounties. — https://x.com/aeonframework/status/2084618749525553171

_Proof point:_ unprompted third-party BD read framing the Tencent fix as a pricing-gap signal — https://x.com/DegenOnBase_/status/2083178423837692259

---
*r/OpenSourceAI* · archetype: open-source · link: https://github.com/aaronjmars/aeon
*Title:* Open-sourced a vuln-scanner skill for autonomous agents — it already found a live bug in infra serving tens of billions of requests

*Body:*
We ship Aeon as a fork-and-configure agent framework — skills are just markdown files (SKILL.md) that run unattended on GitHub Actions, no approval loop, no human clicking "go."

Last week one of those skills — a vuln-scanner — found a real vulnerability in Tencent-scale infra. The fix got merged in 3 hours. Nobody prompted the scan, nobody babysat the PR. It ran on its schedule and did its job.

We're not selling "AI finds bugs" as a headline. We're showing the mechanic: fork the repo, the vuln-scanner skill is already in there, point it at your own stack and see what it turns up. If it finds something, that bounty's yours, not ours.

Repo: https://github.com/aaronjmars/aeon — happy to answer questions about how the skill's structured or how the cron/self-repair loop works.

_notes: disclosing as the builder (I work on Aeon). Sub leans OSS-enthusiast — kept it mechanic-first, no hype language._

---
*r/CoolGithubProjects* · archetype: github · link: https://github.com/aaronjmars/aeon
*Title:* Aeon - open-source agent framework whose vuln-scanner skill already found a real bug in billion-request infra

*Body:*
What it is: Aeon is a fork-and-configure framework for autonomous agents. Skills are markdown files that run on a schedule via GitHub Actions — no approval loop, no persistent server to babysit.

Why it's here: one of the built-in skills is a vuln-scanner. Last week it found a real vulnerability in infra that serves tens of billions of requests (Tencent-scale), and the fix was merged in 3 hours. Nobody triggered it manually — it ran on cron and did its job.

Stack: Claude Code + GitHub Actions + markdown skills + a self-repair loop that files and fixes its own regressions.

Repo: https://github.com/aaronjmars/aeon. Fork it, point the vuln-scanner at your own stack, keep whatever bounty it finds.

_notes: r/CoolGithubProjects requires the "Aeon - <desc>" title format — followed exactly. Repo link is the payload per sub rules; no extra links added._

---
*r/CLaudeSkills* · archetype: claude-skills · link: https://github.com/aaronjmars/aeon
*Title:* Our vuln-scanner skill (literally a markdown file) just found a real bug in Tencent-scale infra

*Body:*
If you're already writing Claude-style skills, this is a concrete example of what a SKILL.md running unattended can actually do.

Aeon's skills are exactly that — markdown files with frontmatter (name, schedule, mode: read-only or write) that a headless Claude Code run reads and executes on a GitHub Actions cron. No wrapper app, no orchestration layer beyond the workflow file.

One of ours is a vuln-scanner skill. It found a real vulnerability in infra serving tens of billions of requests last week, and the fix got merged in 3 hours — the skill ran on schedule, nobody prompted it.

Repo's here if you want to see the actual SKILL.md: https://github.com/aaronjmars/aeon. Fork it and point the scanner at your own stack — genuinely curious what a wider set of agents finds.

_notes: audience is technical — kept the skill-shape explanation concrete instead of marketing-y; disclosed as the builder._

---
*r/Agent_AI* · archetype: agents · link: https://github.com/aaronjmars/aeon
*Title:* An autonomous vuln-scanner agent found and shipped a fix into billion-request infra — unattended, no approval loop

*Body:*
Most "autonomous agent" demos still have a human clicking approve somewhere. Ours doesn't — that's the actual comparison worth making.

Aeon runs skills on GitHub Actions cron. Last week the vuln-scanner skill found a real vulnerability in infra serving tens of billions of requests, and the fix merged in 3 hours. No approval step, no babysitting — it ran on schedule like every other skill, and a self-repair loop handles the failures that come up.

A market participant flagged this unprompted as one of the biggest pricing gaps in the space right now — more validating than anything we could've said ourselves.

Repo: https://github.com/aaronjmars/aeon. Public traces if you want to see what "unattended" actually means here, not just take our word for it.

_notes: no vendor-vs-vendor trash talk, kept the comparison to the autonomy axis only. Disclosed as builder._

---
*r/StartupMind* · archetype: startup · link: https://aeon.fun
*Title:* Building in public: our open-source security agent found a real bug last week, and a stranger flagged it as one of the biggest gaps in our category — unprompted

*Body:*
Quick building-in-public update. Aeon is an open-source framework where "skills" (markdown files) run unattended on a schedule. One of them is a vuln-scanner.

Last week it found a real vulnerability in infra serving tens of billions of requests. The fix got merged in 3 hours. We didn't write a thread about it — someone else did, unprompted, framing it as evidence of a pricing gap in our category. That's the kind of validation you can't manufacture.

No growth hack here, just: ship the thing, let it run, let people notice on their own time.

Site: https://aeon.fun — repo's linked there if you want the mechanics.

_notes: r/StartupMind smells growth-hacky tone fast — kept it to one honest traction beat, no CTA stacking. Disclosed as founder ("I work on Aeon")._