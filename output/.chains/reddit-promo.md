*Reddit Promo — 2026-08-11*

_Story:_ An Aeon skill wrote, tested, and merged a Dynamic Fee Hook for Uniswap v4 with no human approving a step — a concrete on-chain demo, not a claim — https://x.com/aeonframework/status/2087181769124589960

---
*r/Agent_AI* · archetype: agents
*Title:* My agent framework's own agent shipped a working Uniswap v4 hook, unsupervised
*Body:*
Been building Aeon — an agent framework that runs on GitHub Actions, no local box, no approval loop. This week one of its skills wrote, tested, and shipped a Dynamic Fee Hook for Uniswap v4 on its own. Not a code suggestion a human then deployed — the agent's commit, the agent's PR, merged.

What makes this different from most "autonomous agent" frameworks I've seen: there's no supervisor loop waiting on a human click between steps. Skills are markdown files, each schedulable via cron, and there's a self-repair loop that files and fixes its own bugs. We also just wired every skill up as an independently callable agent over Google's A2A protocol, so other agents can call a single Aeon skill directly instead of hitting a monolith.

Repo's open source (AGPL): https://github.com/aeonfun/aeon — genuinely curious how others are handling the supervision-loop problem, happy to compare notes.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=My%20agent%20framework%27s%20own%20agent%20shipped%20a%20working%20Uniswap%20v4%20hook%2C%20unsupervised)
_notes: general self-promo tolerance if substantive/technical — disclose you're the builder up top._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Skill (markdown file) to agent's own PR to live Uniswap v4 hook. No human in the loop.
*Body:*
A skill in Aeon is just a markdown file — frontmatter for schedule/permissions, then plain instructions. This week the skill that watches our DeFi surface wrote a Dynamic Fee Hook for Uniswap v4, tested it, opened its own PR, and merged — the whole loop ran on a GitHub Actions cron, no one approved a step.

The part that's more interesting than the hook itself: skills can chain (one skill's output feeds the next), and there's a self-repair skill that reads failure logs and files fixes against other skills. It's markdown orchestrating markdown.

Also just shipped native A2A (Agent-to-Agent protocol) support — every skill is independently callable as its own agent now, not just internally.

Repo (AGPL, open source): https://github.com/aeonfun/aeon — if you're prompt-engineering agent pipelines, the skill format might be useful even outside our stack.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Skill%20%28markdown%20file%29%20to%20agent%27s%20own%20PR%20to%20live%20Uniswap%20v4%20hook.%20No%20human%20in%20the%20loop.)
_notes: keep it concrete (skill format, not hype) — this sub filters hard on genuine tool-share vs ad; disclose you built it._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* A markdown skill shipped a Uniswap v4 hook on its own - here's the skill shape
*Body:*
Aeon skills are Claude-style markdown skills (SKILL.md, frontmatter + instructions) scheduled via cron on GitHub Actions. This week one of them — the DeFi-ops skill — wrote a Dynamic Fee Hook for Uniswap v4, tested it, and merged its own PR without a human clicking approve.

Rough shape of a skill file:

```
---
name: uniswap-hooks
mode: write
schedule: cron
---
Watch [pools/params]. If [condition], draft a hook contract,
write tests, open a PR. Log outcome to memory/.
```

That's genuinely most of it — the agent does the rest (write code, run tests, open PR, self-repair if something breaks). We also just gave every skill a Google A2A endpoint, so other agents can call one directly.

Repo's open, AGPL: https://github.com/aeonfun/aeon. Would love feedback from people running Claude-style skills elsewhere — how are you handling write-mode approval gates?
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=A%20markdown%20skill%20shipped%20a%20Uniswap%20v4%20hook%20on%20its%20own%20-%20here%27s%20the%20skill%20shape)
_notes: most skills-literate audience here — lead with mechanics, they'll spot hand-wave fast; disclose you built it._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - autonomous agent framework whose own skill just shipped a live Uniswap v4 hook
*Body:*
What: Aeon, an agent framework that runs unattended on GitHub Actions — skills are markdown files, cron-scheduled, self-repairing.

Why post: this week a skill wrote, tested, and merged a Dynamic Fee Hook for Uniswap v4 with no human approving a step — the PR is the agent's own. Just added Google A2A protocol support too, so every skill is independently callable as its own agent.

Stack: GitHub Actions + Claude Code/other harnesses under the hood, markdown skill definitions, git-backed memory.

Repo: https://github.com/aeonfun/aeon (AGPL, open source)
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20autonomous%20agent%20framework%20whose%20own%20skill%20just%20shipped%20a%20live%20Uniswap%20v4%20hook)
_notes: strict title format enforced ("Aeon - <desc>") — keep body factual/stack-focused, no fluff; disclose in body ("I built this")._