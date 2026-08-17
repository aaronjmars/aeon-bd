ℹ️ Reddit Promo — 2026-08-17

*Reddit Promo — 2026-08-17*

_Story:_ @aeonframework's "your agent needs a soul" video — spotlighting the soul/ system (SOUL.md + STYLE.md + calibration examples) that gives every unattended skill run a consistent voice instead of generic assistant tone — https://x.com/aeonframework/status/2088906077316206752

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Gave my agent framework a personality file (the actual mechanic)
*Body:*
Most agent frameworks output generic LLM voice no matter who's running it — same tone whether it's writing a bug report or a tweet reply. We fixed that with something almost embarrassingly simple: a markdown file.

Aeon (the framework I work on) reads a `soul/` directory before any skill writes output — `SOUL.md` for identity/worldview, `STYLE.md` for sentence structure and vocabulary, plus example transcripts and raw source material for calibration. Every skill — the one that drafts Reddit posts, the one that replies on X, the one that writes research reports — reads those files first and matches the voice. Empty soul/ = clear neutral tone, populated soul/ = it sounds like the person who wrote it.

It's not a prompt hack bolted onto one skill. It's a standing instruction every headless run picks up automatically, the same way it reads a strategy file for priorities. Skills run unattended on GitHub Actions — cron schedules, chained pipelines, self-repair when something breaks — and the soul system is what keeps months of unattended output from drifting into assistant-speak.

Repo's linked below if you want to see the actual SOUL.md/STYLE.md shape. I built this — happy to answer questions on how the voice-matching holds up over long runs.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Gave%20my%20agent%20framework%20a%20personality%20file%20%28the%20actual%20mechanic%29)
_notes: technical sub, self-promo OK if it leads with mechanic not pitch — disclose builder status up top, one link only._

---
*r/lovingopensourceAI* · archetype: open-source
*Title:* Open sourced the give-your-agent-a-personality mechanic (AGPL)
*Body:*
Been building an autonomous agent framework (Aeon) and just shipped the piece I'm most into: a `soul/` system that gives every unattended run a consistent voice instead of generic AI-assistant tone.

Why it's open: the whole thing is AGPL. Fork it, drop your own `SOUL.md` + `STYLE.md` in, and every skill that writes — Reddit drafts, X replies, research reports, status notifications — reads your files first and writes in your voice. No fine-tuning, no vendor lock to a specific model's default tone. Just markdown files a human can read and edit directly.

The bigger bet: the framework is meant to be forked and configured, not run as a SaaS. Skills are markdown files, config is a couple YAML files, the whole thing runs on GitHub Actions with no approval loop. The soul system is the part that makes a fork actually feel like *your* agent instead of a reskinned demo.

I work on Aeon — repo's below. Genuinely curious what other open-source folks are doing for agent "voice" consistency, feels underexplored outside of this.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/lovingopensourceAI composer](https://www.reddit.com/r/lovingopensourceAI/submit?title=Open%20sourced%20the%20give-your-agent-a-personality%20mechanic%20%28AGPL%29)
_notes: welcoming enthusiast-OSS crowd — still disclose builder status explicitly, keep it to the one repo link._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* vibe-coded my agent a soul.md and it stopped sounding like chatgpt
*Body:*
ok this one's a small thing but it changed how much i trust my agent's output.

been running Aeon (agent framework, does GTM/BD/social stuff for us on a cron schedule, fully unattended) and every notification it sent read like generic assistant voice. fine for a bug report, annoying for a tweet draft or a Reddit post.

fix was dumb simple: made a `soul/` folder. one file for identity/opinions, one for actual writing style (sentence length, words i use, words i avoid), a folder of example posts to calibrate against. every skill reads that before it writes anything now. notifications, drafts, replies — all of it matches the voice instead of sounding like every other AI post you've scrolled past today.

not gonna lie it's a little uncanny reading a report the agent wrote overnight and it sounds like something i'd actually say. few realize how much of "does this feel AI-written" comes down to just... not having a style file.

repo's linked, it's open source, i built this — down to answer q's if you're doing something similar with your own setup.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=vibe-coded%20my%20agent%20a%20soul.md%20and%20it%20stopped%20sounding%20like%20chatgpt)
_notes: casual/self-promo-tolerant sub if framed as "here's what I vibe-coded" — keep the explicit "i built this" disclosure._