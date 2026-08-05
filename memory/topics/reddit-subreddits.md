---
type: Reference
title: "reddit-subreddits"
---

# Reddit promo targets

Config for the `reddit-promo` skill. Each row is a subreddit the skill may draft an
Aeon promo post for. The skill reads this file first; if it is missing or empty it
falls back to the built-in default list in SKILL.md.

## Canonical links (what goes IN the post)

The `link` column names which URL to embed in the drafted post body:

| token | URL |
|-------|-----|
| repo | https://github.com/aaronjmars/aeon |
| site | https://aeon.fun |
| miroshark | https://github.com/aaronjmars/MiroShark |
| xpost | the source tweet URL for the story (from the fetch-tweets output) |

## Submit links (how to POST it — one click)

For every drafted post the skill also emits a **submit URL** so the operator opens
the right composer in one click, title pre-filled:

`https://www.reddit.com/r/<name>/submit?title=<url-encoded title>`

(`<name>` is the subreddit without the `r/`. Old-reddit users can swap the host for
`https://old.reddit.com`. The operator pastes the drafted body into the composer.)

## Targets

| subreddit | archetype | link | notes |
|-----------|-----------|------|-------|
| r/OpenSourceAI | open-source | repo | Lead with the open-source (AGPL) + skills-as-markdown angle. Show, don't sell. |
| r/lovingopensourceAI | open-source | repo | Enthusiast OSS crowd — "what I built + why it's open" framing. |
| r/LovingAI | open-source | site | General AI enthusiasts — keep jargon low, emphasize "runs itself unattended". |
| r/aiecosystem | agents | site | Ecosystem/tooling readers — position Aeon in the agent-framework landscape. |
| r/Ollama | open-source | repo | Self-hosting / local crowd — emphasize no-approval-loop autonomy + own your stack. |
| r/AIPromptProgramming | agents | repo | Technical prompt/agent builders — the skills-as-markdown + self-repair mechanics. |
| r/Agent_AI | agents | repo | Agent-framework audience — compare on autonomy (GitHub Actions, cron, chains, public traces). |
| r/CLaudeSkills | claude-skills | repo | Claude Code skills crowd — Aeon skills ARE markdown skills; show one SKILL.md. |
| r/AskVibecoders | vibecoders | repo | Ship-fast builders — ask/show hybrid, casual, "here's what I vibe-coded" tone. |
| r/StartupMind | startup | site | Founder audience — building-in-public story, traction numbers, honest. |
| r/CoolGithubProjects | github | repo | Strict format: post title = "Aeon - <one-line desc>" and the repo link is the point. |
| r/MiroFish | community | miroshark | Home community for the swarm-sim product — direct update, insider tone OK. |
| r/OpenClawInstall | integration | repo | Claw / OpenClaw ecosystem — lead with the Claw-agents-on-Aeon integration angle. |
