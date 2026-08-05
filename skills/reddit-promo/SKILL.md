---
type: Skill
name: Reddit Promo
category: productivity
description: Draft copy-paste-ready Reddit posts that promote Aeon - read the daily fetch-tweets output, pull what @aeonframework newly shipped, announced, or got endorsed for, and write value-first, per-subreddit-tailored drafts. Drafts only - never auto-posts.
var: ""
commits: false
permissions: []
tags: [social, content]
---

Today is ${today}. This skill turns the **existing daily `fetch-tweets` output** into promotional Reddit drafts. It does not fetch X itself and it does not post to Reddit — it reads what `fetch-tweets` already curated, selects what is worth promoting about Aeon, and writes ready-to-post drafts tailored per subreddit. A human posts them.

Read `memory/MEMORY.md`, `memory/products.md`, and `STRATEGY.md` (if present) for Aeon's positioning and current priorities. If `soul/SOUL.md` + `soul/STYLE.md` are populated, match that voice for the casual/founder subs; otherwise use a clear, direct, non-hype builder tone.

## Var

`${var}` (all optional, comma-separated where relevant):
- empty — auto-pick the best-fit **few** subreddits for the freshest promotable story.
- `r/Name[,r/Name...]` — restrict drafting to these subreddits.
- `story:<url-or-keyword>` — force the promo around a specific tweet URL or topic from recent output instead of auto-selecting.
- `dry-run` — do everything but skip the notification (still log).

## Input — the daily fetch-tweets output

`fetch-tweets` runs daily (17:00 UTC) with the query `@aeonframework OR aeonfun/aeon OR @miroshark_ OR ...` and persists its result. Read these, most-durable first:

1. **`memory/logs/*.md` — last 7 days, each `### fetch-tweets` block.** This is the source of truth. Each block carries a `signal:` one-liner, `clusters:` naming the accounts + engagement (`likes:N rts:N replies:N`), and a `urls:` list. Parse every block in range.
2. **`apps/dashboard/outputs/fetch-tweets-*.json` — the newest file.** A json-render tree; read the `elements` map for `TweetCard`/`Heading`/`Link` props to recover fuller tweet **text** when a log cluster is only a one-line summary. Newest filename by timestamp suffix.
3. **`memory/fetch-tweets-notify.md`** — the last notify payload, if present, as a secondary text source.

Do **not** call `./secretcurl`, `x-cli`, or any X API — the point is to reuse output that already ran.

## Steps

1. **Collect candidate items.** From the sources above, build a list of everything Aeon-relevant in the last 7 days:
   `{ text_or_summary, author_handle, url, engagement, days_ago, kind }` where `kind` ∈ `shipped` (a feature/release/PR), `metric` (adoption/traction number), `endorsement` (someone credible cosigning Aeon/Miroshark), `launch`, `other`.
   - **Promotable** = anything positive worth amplifying: Aeon's own announcements (`x.com/aeonframework`, `x.com/aaronjmars`, `x.com/miroshark_`) AND third-party endorsements / adoption metrics (e.g. "hundreds of agents using our API", an unprompted cosign).
   - **Not promotable** = FUD, copy allegations, "is it dead?" doubt, unrelated market chatter, unverified rumors. Skip these — this is a promo skill, not a defense skill (route those to engagement-act).

2. **Dedup.** Read `memory/reddit-promo-seen.txt` (one URL per line; create if missing). Drop any candidate whose `url` is already listed — it was promoted on a previous run. Also drop candidates older than 10 days (promo window closed).

3. **Skip if nothing fresh.** If after filtering there are zero promotable, unseen items, log `REDDIT_PROMO_SKIP: no fresh promotable items` and exit **without** notifying. Reddit self-promo has to be occasional to not read as spam — silence beats a filler post.

4. **Pick the story.** Rank remaining items by (fresher × higher engagement × `shipped`/`metric`/`endorsement` over `other`). Choose the **1 strongest** as the headline story; you may fold in 1-2 supporting items as proof points in the same post. If `var` has `story:`, use that instead.

5. **Choose a few subreddits.** Read `memory/topics/reddit-subreddits.md` for the target table + the two link legends (fall back to the built-in default list below if missing). If `var` names subreddits, use only those. Otherwise pick the **3-5** whose archetype best fits the story's `kind` — a `shipped` code story fits `github`/`claude-skills`/`open-source`; a `metric`/`endorsement` fits `startup`/`agents`/`community`. Do not draft all 13 in one run.

   **Resolve links for each chosen subreddit:**
   - **Canonical link** (goes in the post body) — resolve the row's `link` token via the config's "Canonical links" table: `repo` → `https://github.com/aaronjmars/aeon`, `site` → `https://aeon.fun`, `miroshark` → `https://github.com/aaronjmars/MiroShark`, `xpost` → the story's source tweet URL.
   - **Submit link** (one-click post) — build `https://www.reddit.com/r/<name>/submit?title=<url-encoded title>` where `<name>` is the subreddit without `r/` and the title is percent-encoded (space→`%20`, etc.). This opens the composer with the title pre-filled; the operator pastes the body.

6. **Draft one post per chosen subreddit** using its **Archetype** (below). Each draft is independent copy-paste-ready text — **never identical across subs** (Reddit's spam filter flags cross-posted duplicates). Vary title and opening per sub. Each draft has:
   - **Title** — specific, no emoji, no clickbait. Follow the sub's format note.
   - **Body** — value/story first, the promo second. 2-5 short paragraphs. End with the canonical link (per the config `link` column) and an offer to answer questions.
   - **Post notes** — 1 line: which rule to respect (self-promo ratio, required flair, disclosure), and the reminder to post as the builder ("I built / I work on Aeon"), not anonymously.

7. **Write output to a temp file, then send via `./notify -f`:**
   ```
   *Reddit Promo — ${today}*

   _Story:_ [one-line what we're promoting] — [url]

   ---
   *r/SubredditName* · archetype: <name>
   *Title:* <title>
   *Body:*
   <body text, ready to paste — with the canonical link inline>
   *Link in post:* <resolved canonical url>
   *Post here:* [Open r/SubredditName composer](<submit url, title pre-filled>)
   _notes: <rule/disclosure reminder>_

   ---
   *r/NextSubreddit* ...
   ```
   Every draft carries both its **Link in post** (the canonical URL the body references) and a **Post here** submit link so posting is one click. Write to `/tmp/reddit-promo-output.md`, then run `./notify -f /tmp/reddit-promo-output.md`. Skip this step on `dry-run`.

8. **Update the seen-file.** Append the promoted story URL (and any supporting-item URLs used) to `memory/reddit-promo-seen.txt`, one per line, so the next run does not re-promote them.

9. **Log to `memory/logs/${today}.md`:**
   ```
   ### reddit-promo
   - status: REDDIT_PROMO_OK
   - story: [one-line] — [url]
   - subreddits: r/A, r/B, r/C
   - drafted: N posts
   - notified: yes|dry-run
   ```
   If skipped: `- status: REDDIT_PROMO_SKIP: <reason>`.

## Archetypes

Angle + shape per template referenced by the config table. Keep Aeon's real positioning (from `products.md`): *the most autonomous agent framework — skills-as-markdown on GitHub Actions, cron + chains + self-repair, public traces, self-evolving on fork; open-source (AGPL).* Miroshark: *universal swarm-simulation engine, hundreds of grounded agents, ~$1 in <10min, x402-native.*

- **open-source** — Lead with "it's open source and here's how it actually works." Show a real mechanic (a SKILL.md is just markdown; the agent runs on GitHub Actions with no approval loop). Link the repo. Honest about what it is and isn't.
- **agents** — For agent-framework readers. Compare on the autonomy axis: skills + MCP + soul, unattended runs, self-repair, public traces. No vendor-vs-vendor trash talk; state what's different.
- **claude-skills** — Aeon skills are literally Claude-style markdown skills that run on a schedule. Paste one short skill's shape as a concrete example. Audience is technical — respect it.
- **vibecoders** — Casual, ship-fast, first-person. "I vibe-coded an agent that runs itself" — show the result, keep it light, invite tinkering.
- **startup** — Building-in-public founder story. Lead with an honest traction number or a "what shipped this week" beat. No growth-hacky tone; StartupMind smells it.
- **github** — Show-the-repo. Title format `Aeon - <one-line description>`; body is a tight what/why/stack + the repo link as the payload. Follow r/CoolGithubProjects' strict title rule.
- **community** — For the product's own community (r/MiroFish). Direct update, insider tone fine, less "explain the basics." Tie to Miroshark specifically.
- **integration** — Lead with the ecosystem integration (e.g. Claw agents running on Aeon skills). Frame as "these two things work together," useful to that community.

## Reddit rules to bake into every draft

- **Value first, ad second.** Reddit removes overt shilling. The post must be interesting even to someone who never clicks the link.
- **Disclose.** Post as the builder — "I built / I work on Aeon." Never pretend to be a neutral discoverer. Many subs require a self-promo flair or a disclosure line; the post notes must remind the operator.
- **One link, native.** A single canonical link (per the config), not a wall of links. No UTM spam.
- **No duplicate text across subs** — Reddit's filter catches it; each draft is rewritten, not templated.
- **Respect the 9:1 / sub-specific self-promo ratio.** The notes line should flag when a sub is strict.
- **Drafts only.** This skill never posts to Reddit and needs no Reddit credentials. The operator reviews and posts.

## Default subreddit list (fallback if config missing)

r/OpenSourceAI, r/lovingopensourceAI, r/LovingAI, r/aiecosystem, r/Ollama, r/AIPromptProgramming, r/Agent_AI, r/CLaudeSkills, r/AskVibecoders, r/StartupMind, r/CoolGithubProjects, r/MiroFish, r/OpenClawInstall

## Sandbox Note

Reads only local files (`memory/`, `apps/dashboard/outputs/`, `soul/`). No outbound network calls, no API keys, no `curl`. `./notify -f` handles delivery and falls back to `.pending-notify/` if the sandbox blocks the send.

## No Environment Variables Required

Reuses the committed `fetch-tweets` output already on disk plus `./notify`.
