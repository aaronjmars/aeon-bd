ℹ️ Reddit Promo - 2026-08-30

*Reddit Promo - 2026-08-30*
1d since last promo · 4 subs drafted

_Story:_ WebMCP ships — launch a Miroshark simulation or stand up an Aeon instance directly from ChatGPT desktop or Codex, no dashboard - https://x.com/aaronjmars/status/2093724185994346542

---
*r/StartupMind* · archetype: startup
*Title:* Shipped: you can now launch our agent framework and swarm-sim engine straight from ChatGPT desktop or Codex
*Body:*
We build two things: Aeon (an autonomous agent framework that runs unattended on GitHub Actions — skills as markdown, cron, self-repair) and Miroshark (spin up hundreds of grounded agents to simulate anything, ~$1 in under 10 minutes).

This week we shipped WebMCP — it exposes both as MCP tools, so you can launch a Miroshark simulation or stand up a fresh Aeon instance directly from ChatGPT desktop or Codex, no dashboard, no separate login. It's the highest-engagement post we've had this week, and the best proof point isn't ours — an outside builder used it to run an 18-agent Miroshark debate and then cut the recap video with one of Aeon's own skills, entirely outside anything we scripted.

Not a huge unlock in isolation, but it's the kind of "meet people where they already are" move that compounds — fewer steps between "I have an idea" and "it's running."

I work on Aeon/Miroshark — site's here: https://aeon.fun. Happy to answer questions about how the MCP wiring works.
*Link in post:* https://aeon.fun
*Post here:* [Open r/StartupMind composer](https://www.reddit.com/r/StartupMind/submit?title=Shipped%3A%20you%20can%20now%20launch%20our%20agent%20framework%20and%20swarm-sim%20engine%20straight%20from%20ChatGPT%20desktop%20or%20Codex)
_notes: disclosed as builder in-body ("I work on Aeon/Miroshark"); StartupMind reads growth-hack tone as spam fast, so kept the traction claim to our own verifiable engagement number, not a projected one._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Open-source agent framework now callable as an MCP tool from ChatGPT desktop and Codex
*Body:*
Aeon is an open-source (AGPL) framework for running autonomous agents unattended — each "skill" is just a markdown file with a prompt and a schedule, executed on GitHub Actions with no approval loop in between. No hosted backend required; fork it and it's yours.

We just shipped WebMCP, which wraps Aeon (and our sim engine Miroshark) as MCP tools — so ChatGPT desktop or Codex can call out and launch a real agent run or a swarm simulation directly, without leaving the chat. Under the hood it's the same skill-as-markdown model, just given a callable interface.

Repo: https://github.com/aeonfun/aeon — I work on this, so ask me anything about the internals or the MCP tool definitions specifically.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Open-source%20agent%20framework%20now%20callable%20as%20an%20MCP%20tool%20from%20ChatGPT%20desktop%20and%20Codex)
_notes: disclosed as builder; sub is receptive to "show the mechanic" posts but still enforces value-first, so led with the open-source model before the new feature._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* WebMCP: exposing agent skills and swarm sims as MCP tools for ChatGPT/Codex
*Body:*
If you've built anything with MCP, the interesting part isn't "we support MCP" — it's what gets exposed as a tool. We just shipped WebMCP for Aeon (our agent framework) and Miroshark (our swarm-sim engine): both are now callable as MCP tools, so ChatGPT desktop or Codex can trigger a real skill run or spin up a multi-agent simulation mid-conversation.

Aeon's skills are just markdown — a prompt block + a cron schedule — so the "tool" side of this is closer to invoking a script than hitting an opaque API. That's what let an outside builder run an 18-agent Miroshark debate and then generate the recap video with one of Aeon's own skills, in the same session, without touching either dashboard.

Repo (skills + MCP wiring both live here): https://github.com/aeonfun/aeon. I work on this — happy to get into the tool-definition/schema details if useful.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=WebMCP%3A%20exposing%20agent%20skills%20and%20swarm%20sims%20as%20MCP%20tools%20for%20ChatGPT%2FCodex)
_notes: technical audience, kept the pitch to mechanics not adjectives; disclosed as builder._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* I hooked my agent framework up to ChatGPT desktop via MCP - here's what it can do now
*Body:*
Been building Aeon (agents that run themselves on GitHub Actions, no server) and Miroshark (spin up a swarm of agents to simulate something, cheap and fast) for a while. This week I wired both up to MCP, so now I can ask ChatGPT desktop or Codex to launch a simulation or stand up an agent instance mid-chat, no tab-switching.

Best part: someone else immediately used it to run an 18-agent debate in Miroshark about renaming a lake, then made the recap video with one of Aeon's own skills. I didn't script that — they just found it.

If you want to poke at it: https://github.com/aeonfun/aeon. Ask me anything, I'll answer in-thread.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=I%20hooked%20my%20agent%20framework%20up%20to%20ChatGPT%20desktop%20via%20MCP%20-%20here%27s%20what%20it%20can%20do%20now)
_notes: disclosed as builder up front, casual tone fits the sub; kept to one link to respect self-promo ratio._