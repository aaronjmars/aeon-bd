ℹ️ Reddit Promo - 2026-09-10

*Reddit Promo - 2026-09-10*
3d since last promo · 4 subs drafted

_Story:_ Aeon ships the Hook Marketplace - aeon.fun/hooks live with 12 Uniswap v4 hooks, registry (aeonfun/univ4-hooks) accepting deploys on 7 chains - https://x.com/aeonframework/status/2097997668601544919

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - open-source agent framework that just shipped a Uniswap v4 hook registry deploying to 7 chains
*Body:*
Aeon is an open-source (AGPL) framework where every "agent" is a folder of markdown files run on a schedule via GitHub Actions - no long-running process, no approval loop between one run and the next.

This week it shipped aeon.fun/hooks: 12 ready-to-use Uniswap v4 hooks, backed by a registry (the univ4-hooks repo) that takes deploys across seven chains. Not a demo - a live marketplace anyone can submit a hook to.

Why it's relevant here: the whole thing runs through the same skill-as-markdown mechanic as everything else in the framework - a scheduled job reads a spec, writes the hook, opens a PR. No separate infra for "hooks" vs. everything else Aeon does.

Repo's linked below if you want to see the actual skill files, not just the pitch.

I built this - happy to answer questions about the deploy pipeline or the framework itself.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20open-source%20agent%20framework%20that%20just%20shipped%20a%20Uniswap%20v4%20hook%20registry%20deploying%20to%207%20chains)
_notes: strict title-format sub ("Aeon - <one-line desc>") - don't edit the title post-submit; post as the builder, not anonymously._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Shipped a multi-chain hook marketplace with a framework that has no approval loop between runs - here's how the pipeline works
*Body:*
Aeon (AGPL, github.com/aeonfun/aeon) runs "skills" - plain markdown files with a frontmatter block for schedule/permissions - through GitHub Actions. No daemon, no approval step between one run and the next; whatever the skill decides to do (open a PR, post a draft, deploy something) just happens on the next scheduled tick.

Case in point from this week: it shipped aeon.fun/hooks, 12 ready Uniswap v4 hooks, with a registry accepting deploys on seven chains. That's not a one-off feature - it's the same scheduled-skill mechanic that runs the rest of the framework, just pointed at hook deploys instead of, say, a changelog update or a security scan.

If "open source" for you means you actually want to read the thing that ships code on its own, the repo's below - it's all just .md files and a couple of shell scripts underneath.

I work on Aeon, ask me anything about the internals.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Shipped%20a%20multi-chain%20hook%20marketplace%20with%20a%20framework%20that%20has%20no%20approval%20loop%20between%20runs%20-%20here%27s%20how%20the%20pipeline%20works)
_notes: enthusiast OSS crowd, self-promo tolerated if mechanic-first - disclose "I work on Aeon"._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* An agent framework where shipping a feature means a scheduled markdown file writes code and opens a PR
*Body:*
Been building on Aeon - the interesting bit for this sub is the loop: a "skill" is a markdown spec (frontmatter: schedule, required secrets, read-only vs. write mode) that Claude Code executes headless on GitHub Actions. No long-lived agent process, no human approval gate per run - each dispatch reads memory, does the work, and either writes files/opens a PR or reports back.

This week's proof that loop actually produces something real: aeon.fun/hooks went live with 12 Uniswap v4 hooks, and the registry backing it takes deploys on seven chains. Same skill-dispatch mechanic that runs everything else in the framework, this time pointed at deploying hooks instead of, say, drafting a PR review.

There's also a self-repair loop on top of it - a health skill scores runs, a repair skill opens fix PRs against skills that degrade. If you're building agents that need to survive unattended for weeks, the failure-mode handling is worth a read even if you never touch Aeon itself.

Repo's linked - happy to talk through the architecture, I'm one of the people building it.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=An%20agent%20framework%20where%20shipping%20a%20feature%20means%20a%20scheduled%20markdown%20file%20writes%20code%20and%20opens%20a%20PR)
_notes: technical audience, don't oversimplify - disclose builder status._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* A skill whose entire job is drafting Reddit promo posts from another skill's output - here's the shape
*Body:*
Aeon skills are exactly what this sub is about - markdown files with a frontmatter block, executed by Claude Code on a cron via GitHub Actions. No wrapper app, no special skill-runtime beyond what Claude Code already does.

Concrete example - this one drafted the post you're reading:
```
type: Skill
name: Reddit Promo
description: Draft copy-paste-ready Reddit posts that promote Aeon - read the
  daily fetch-tweets output, pull what shipped or got endorsed, write
  value-first per-subreddit drafts. Drafts only - never auto-posts.
var: ""
commits: false
```
That frontmatter plus a numbered list of steps is the whole "program." No code, no separate runtime - Claude Code just executes the instructions.

Same mechanic ships real things, not just social copy - this week a different skill in the same framework shipped aeon.fun/hooks, 12 Uniswap v4 hooks with a registry that deploys across seven chains. Scheduled markdown files writing code and opening PRs, unattended.

Repo's below if you want to see the other skills in the catalog. I work on this, ask away.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=A%20skill%20whose%20entire%20job%20is%20drafting%20Reddit%20promo%20posts%20from%20another%20skill%27s%20output%20-%20here%27s%20the%20shape)
_notes: technical crowd will check the repo - keep every claim literally checkable; disclose "I work on Aeon."_