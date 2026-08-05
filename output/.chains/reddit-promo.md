ℹ️ Reddit Promo — 2026-08-05

*Reddit Promo — 2026-08-05*

_Story:_ Aeon shipped multi-model support (Kimi Moonshot as a selectable model — same skills/schedules/Telegram control, different LLM underneath) — https://x.com/aeonframework/status/2082801981467373635

_Note: two other stories (Tencent vuln-scanner fix, Uniswap v4 hooks) already ran through 5+4 subreddits earlier today. Only 4 subs are untouched today (r/LovingAI, r/Ollama, r/MiroFish, r/OpenClawInstall) — of those, only the first two fit this story's archetype (open-source/self-host), so this run is 2 drafts, not 3-5, to avoid same-day duplicate submissions to the same sub._

---
*r/LovingAI* · archetype: open-source
*Title:* Built an AI agent framework that runs itself, just added support for swapping the LLM underneath
*Body:*
been building an agent framework that just runs — cron on github actions, no approval loops, no babysitting. set it up once, it works unattended.

this week added multi-model support. same skills, same schedules, same telegram control — just pick a different LLM underneath (kimi moonshot is the newest option). no rewrite, no re-config. the harness doesn't care what's powering it.

someone already forked it and plugged the framework's soul.md prompts into their own project to build persona clones off a different corpus — not us talking about ourselves, a random builder actually using it for something we didn't build (https://x.com/dev0xx_/status/2084050680616996896).

it's open source (AGPL): https://aeon.fun

i built this. happy to answer questions about the setup or the model-swapping bit specifically.
*Link in post:* https://aeon.fun
*Post here:* [Open r/LovingAI composer](https://www.reddit.com/r/LovingAI/submit?title=Built%20an%20AI%20agent%20framework%20that%20runs%20itself%2C%20just%20added%20support%20for%20swapping%20the%20LLM%20underneath)
_notes: general AI enthusiast sub, keep jargon low — lead with the mechanic not the pitch, disclose "i built this."_

---
*r/Ollama* · archetype: open-source
*Title:* Self-hosted agent framework that swaps LLMs without touching your setup (runs on GitHub Actions, no server needed)
*Body:*
if you're the type running local models because you don't want to be locked into one provider — built something adjacent. an agent framework that runs unattended on github actions (no server to babysit, no approval loop), and this week it went model-agnostic: same skills/schedules, different LLM underneath, kimi moonshot is the latest add.

own your stack is the whole point — you're not welded to one model provider, and the "skills" are just markdown files you can read/fork/edit yourself.

a third-party builder already forked the repo and used it plug-and-play — wired the project's own soul.md prompts into their build to generate persona clones from a different corpus. real usage, not us hyping ourselves (https://x.com/dev0xx_/status/2084050680616996896).

repo's open source (AGPL): https://github.com/aeonfun/aeon

i work on this, happy to answer setup questions.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=Self-hosted%20agent%20framework%20that%20swaps%20LLMs%20without%20touching%20your%20setup%20%28runs%20on%20GitHub%20Actions%2C%20no%20server%20needed%29)
_notes: self-hosting crowd respects "own your stack" framing — keep it repo-first, disclose "i work on this."_