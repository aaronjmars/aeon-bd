ℹ️ Reddit Promo - 2026-08-28

*Reddit Promo - 2026-08-28*
1d since last promo · 4 subs drafted

_Story:_ Aeon shipped a reusable soul/ voice-cloning pattern - feed an LLM your tweets/essays, get markdown files any model can load to write in your voice, pitched as standalone/adoptable outside Aeon itself - https://x.com/aaronjmars/status/2092385918770446339

---
*r/LovingAI* · archetype: open-source
*Title:* an agent framework that clones your writing voice from old tweets, then writes your Reddit posts for you (kinda)
*Body:*
been building an open-source agent framework (Aeon) and shipped something this week that's useful even if you never touch the rest of it: a "soul" system. you point it at your old tweets/essays, it distills a couple markdown files - tone, vocabulary, rhetorical habits, the stuff that makes your writing sound like *you* and not generic AI slop. any model can then load those files and write in your voice.

the mechanic is dumb simple on purpose - no fine-tuning, no vector DB, just structured markdown an LLM reads before it writes anything. that's the whole trick. we use it so the agent's automated posts/replies don't read like a bot.

same week we also added Vercel as a deploy target (it originally only ran on GitHub Actions), so it's got more places to actually live now.

repo's here if you want to see the pattern or rip it out for your own project: https://github.com/aeonfun/aeon - it's AGPL, runs unattended, no dashboard required. happy to answer questions on how the voice files get built.

*Link in post:* https://aeon.fun
*Post here:* [Open r/LovingAI composer](https://www.reddit.com/r/LovingAI/submit?title=an%20agent%20framework%20that%20clones%20your%20writing%20voice%20from%20old%20tweets%2C%20then%20writes%20your%20Reddit%20posts%20for%20you%20%28kinda%29)
_notes: r/LovingAI skews general-audience - keep jargon low (already done above); disclose as builder ("I work on Aeon") in the post/first comment, don't post as a neutral discoverer._

---
*r/Ollama* · archetype: open-source
*Title:* built a self-hosted agent that reads your old tweets and writes markdown files any local model can load to sound like you
*Body:*
posting here because this crowd cares about owning your stack, not renting someone else's API forever.

shipped a "soul" system in Aeon (open-source agent framework, AGPL, runs on GitHub Actions) this week: feed it your tweets/essays, it writes out plain markdown files describing your voice - sentence structure, vocab, what you'd never say. any model that can read a text file can load them, local or hosted. no vendor lock-in, no proprietary fine-tune you can't move.

paired with that, we added a second deploy surface (Vercel) alongside GitHub Actions, so the agent isn't tied to one host either.

whole thing's designed to run unattended - cron + self-repair - no approval loop babysitting it. repo: https://github.com/aeonfun/aeon. genuinely curious if anyone's running similar voice/persona files against local models already, would compare notes.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=built%20a%20self-hosted%20agent%20that%20reads%20your%20old%20tweets%20and%20writes%20markdown%20files%20any%20local%20model%20can%20load%20to%20sound%20like%20you)
_notes: self-hosting crowd - lead with own-your-stack framing (done); disclose as builder in-post, check current self-promo flair/ratio rules before posting._

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* a soul.md skill pack: feed it your tweets/essays, get a voice-clone any Claude Skill can load
*Body:*
Aeon skills are literally markdown files that run on a schedule via Claude Code - no custom runtime, just SKILL.md + frontmatter. this week we shipped a new pattern on top of that: a "soul" system for voice-cloning.

the shape: you dump your tweets/essays in, an LLM distills them into a few markdown files (SOUL.md for identity/opinions, STYLE.md for sentence-level habits, examples/ for calibration). every skill that writes human-facing output reads those files first. that's it - no fine-tune, no embeddings, just markdown a skill loads before it drafts a tweet, a reply, a report.

works standalone too - if you're already writing Claude Skills, you can lift the pattern without touching the rest of Aeon. same week we added Vercel as a deploy target next to GitHub Actions, if that's relevant to how you're running skills.

repo, if you want to see the actual files: https://github.com/aeonfun/aeon. happy to walk through the SOUL.md/STYLE.md split if useful.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=a%20soul.md%20skill%20pack%3A%20feed%20it%20your%20tweets/essays%2C%20get%20a%20voice-clone%20any%20Claude%20Skill%20can%20load)
_notes: technical audience, respect it - show the actual file shape, no oversell; disclose as the builder, not a neutral finder._

---
*r/aiecosystem* · archetype: agents
*Title:* Aeon shipped a portable voice-cloning pattern + a Vercel deploy target this week - notes from the framework side
*Body:*
quick one from the agent-framework side of things. Aeon (skills-as-markdown, runs unattended on GitHub Actions, self-repairs on fork) shipped two things this week worth noting for anyone tracking where agent tooling is headed:

1. a "soul" system - feed it your tweets/essays, get markdown files (voice/style/examples) any model can load before writing. solves the "agent output reads like a bot" problem without fine-tuning. built to be portable - works outside Aeon too.
2. Vercel joined GitHub Actions as a second place the agent can actually run.

neither is a huge feature on its own, but together they're a decent signal of where the framework's headed: more surfaces to run on, and a cheap way to make agent output not sound like a press release.

repo's open if you want to see the mechanics: https://github.com/aeonfun/aeon. curious what other frameworks in this space are doing for voice/persona consistency - most of what I've seen is either nothing or a full fine-tune, this sits in between.

*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=Aeon%20shipped%20a%20portable%20voice-cloning%20pattern%20%2B%20a%20Vercel%20deploy%20target%20this%20week%20-%20notes%20from%20the%20framework%20side)
_notes: position in the landscape, no vendor-vs-vendor trash talk (kept out); disclose as builder, standard self-promo ratio applies._