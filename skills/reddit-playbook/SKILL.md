---
type: Skill
name: Reddit Playbook
category: productivity
description: Draft copy-paste-ready Reddit posts the evidence-backed way - pick a content archetype (news-hook / question / milestone / contrarian / observer) before writing, keep the product out of the title, back every claim with a third-party link, and route strict subs to comments. Reads the daily fetch-tweets output. Drafts only - never auto-posts.
var: ""
commits: false
permissions: []
tags: [social, content]
---

Today is ${today}. This skill turns the **existing daily `fetch-tweets` output** into promotional Reddit drafts, using a playbook measured from 54 real posts across two accounts (~294k combined views, Aug 2026). It does not fetch X itself and it does not post to Reddit - it reads what `fetch-tweets` already curated, picks the strongest promotable story, chooses the right **content archetype** for it, and writes ready-to-post drafts. A human reviews and posts.

The one rule above all: **the product is supporting material, never the subject.** Every brand-as-subject post in the data capped under 1k views; the two posts that carried a week (102k + 66k views) both led with a news hook or an analytical question and carried the product only as evidence. So the title sells the story, not Aeon.

Read `memory/MEMORY.md`, `memory/products.md`, and `STRATEGY.md` (if present) for positioning and current priorities. If `soul/SOUL.md` + `soul/STYLE.md` are populated, match that voice for the casual/founder subs; otherwise use a clear, direct, non-hype builder tone.

This skill's output follows the shared **`docs/output-contract.md`**. The one that bites here is the **cadence clock**: Reddit self-promo has to stay occasional (fewer better-placed posts beat volume - 7 posts beat 13 by 6.5x in the data), so the digest surfaces how long it has been since the last promo.

## Var

`${var}` (all optional, comma-separated where relevant):
- empty - auto-pick the freshest promotable story, the best-fit archetype, and a **few** green subreddits.
- `r/Name[,r/Name...]` - restrict drafting to these subreddits.
- `story:<url-or-keyword>` - force the promo around a specific tweet URL or topic from recent output instead of auto-selecting.
- `archetype:A|B|C|D|E` - force a content archetype instead of letting the decision tree pick.
- `dry-run` - do everything but skip the notification (still log).

## Input - the daily fetch-tweets output

`fetch-tweets` runs daily (17:00 UTC) and persists its result. Read these, most-durable first:

1. **`memory/logs/*.md` - last 7 days, each `### fetch-tweets` block.** Source of truth. Each block carries a `signal:` one-liner, `clusters:` (accounts + `likes:N rts:N replies:N`), and a `urls:` list. Parse every block in range.
2. **`apps/dashboard/outputs/fetch-tweets-*.json` - the newest file.** A json-render tree; read the `elements` map for `TweetCard`/`Heading`/`Link` props to recover fuller tweet **text** when a log cluster is only a one-line summary.
3. **`memory/fetch-tweets-notify.md`** - the last notify payload, if present, as a secondary text source.

Do **not** call `./secretcurl`, `x-cli`, or any X API - the point is to reuse output that already ran.

## Steps

1. **Collect candidate items.** From the sources above, build a list of everything Aeon/Miroshark-relevant in the last 7 days:
   `{ text_or_summary, author_handle, url, engagement, days_ago, kind }` where `kind` is one of `shipped` (feature/release/PR), `metric` (adoption/traction number), `endorsement` (a credible cosign), `launch`, `newshook` (an external agent/AI/market news event this ties to), `other`.
   - **Promotable** = anything positive worth amplifying: our own announcements (`x.com/aeonframework`, `x.com/aaronjmars`, `x.com/miroshark_`) AND third-party endorsements / adoption metrics.
   - **Not promotable** = FUD, copy allegations, "is it dead?" doubt, unrelated market chatter, unverified rumors. Route those to `engagement-act`, not here.

2. **Dedup + read the cadence clock.** Read `memory/reddit-promo-seen.txt` (one URL per line; create if missing - shared with the `reddit-promo` skill so the two never double-post the same story). Drop any candidate whose `url` is already listed. Drop candidates older than 10 days (promo window closed). Compute **`days_since_last_promo`**: scan the last 30 days of `memory/logs/` for the most recent `### reddit-playbook` or `### reddit-promo` block with an `OK` status; today minus that date (if none, `first promo`). It does not gate the run - it makes over-frequent promo visible.

3. **Skip if nothing fresh.** If after filtering there are zero promotable, unseen items, log `REDDIT_PLAYBOOK_SKIP: no fresh promotable items` and exit **without** notifying. Silence beats a filler post.

4. **Pick the story.** Rank remaining items by (fresher x higher engagement x `shipped`/`metric`/`endorsement`/`newshook` over `other`). Choose the **1 strongest** as the headline; fold in 1-2 supporting items as proof points. If `var` has `story:`, use that.

5. **Pick the archetype with the decision tree** (before writing a word). This is the core of the playbook - archetype is chosen by story TYPE, not by subreddit.

   ```
   Is there agent/AI/market news from the LAST 24-48H the story ties to?
   |- YES -> Archetype A (news-hook commentary). Timely beats evergreen ~10:1. Post same day.
   |- NO
      |- Did the product just cross a number worth saying?      -> C (milestone)
      |- Do we have third-party-verifiable proof of something?  -> E (observer report)
      |- Is there a metric/assumption everyone gets wrong?      -> D (contrarian)
      |- Default                                                -> B (domain-native question)
   ```

   If `var` has `archetype:`, use that instead.

6. **Choose a few subreddits from the tiered map** (`memory/topics/reddit-playbook-subreddits.md`; fall back to the built-in tiers below if missing). Three tiers, from actual moderation outcomes:
   - **Green** - post any archetype. Pick the **3-5** whose audience fits the story.
   - **Question-only** - allowed only as a pure Archetype B question; a direct promo gets removed. Reframe or skip.
   - **Comment-only** - do NOT draft a post. 12/12 post removals in the data were in blanket no-self-promotion subs, and reframing never changed that. Zero comment removals in three weeks. If one of these fits the story, emit a **comment draft** (value + a link only if asked in-thread), flagged as a comment, not a post.

   Do not draft all subs in one run. Stagger real placements 48-72h; never crosspost the same title/link.

   **Resolve links per subreddit:**
   - **Third-party proof links** (in the body): every checkable claim links to a third-party source - an issue tracker, a commit, a dashboard, the original tweet. NOT our own site. This is why observer-style posts survive moderation.
   - **Product link** (the one canonical link): resolve the row's `link` token - `repo` -> `https://github.com/aeonfun/aeon`, `site` -> `https://aeon.fun`, `miroshark` -> `https://github.com/miroshark/miroshark`, `xpost` -> the source tweet URL. Place it **once, at the bottom, after the value**. Omit it entirely in no-link subs.
   - **Submit link** (one-click): `https://www.reddit.com/r/<name>/submit?title=<url-encoded title>` (`<name>` without `r/`, title percent-encoded).

7. **Draft one post per chosen green/question sub** using the archetype's title formula + the body skeleton. Each draft is independent copy-paste-ready text - **never identical across subs** (Reddit's spam filter flags duplicates). Vary title and opening per sub.

   **Title formulas (with receipts):**
   - **A news-hook** - `[Move 1]. [Move 2]. [One-line thesis].` Product absent. ("Stripe bought OpenRouter. Nvidia is buying Hugging Face. The plumbing layer has owners now" - 16k views.)
   - **B domain-native question** - a question the sub already argues about; product absent. ("Anyone else running Claude Code in a more set-and-forget way?" - 4k, in a sub that had removed a direct post.) Question posts win comments.
   - **C milestone** - `[thing] just hit [concrete number]`. The **only** archetype where the product may appear in the title. ("A community-built AI agent just hit 2,500 contributors" - 17k.)
   - **D contrarian** - name the wrong assumption flatly. ("We keep ranking AI agents by the wrong number" - 6.5k.)
   - **E observer report** - third person, as if reporting on the agent, every claim linked to a receipt. Highest moderation survival. ("An agent found a vulnerability in Google's official agent CLI, and Google shipped the fix" - survived because every claim linked to Google's own tracker.)

   **Body skeleton (all archetypes):**
   ```
   [1-3 sentences: the hook - the news, the question, the number. NO product yet.]
   [The substance: what happened / what the data shows, with concrete numbers.
    Every checkable claim links to a THIRD-PARTY source, not our site.]
   [The product enters as evidence, ONE sentence: "the agent that found it runs on <X>".]
   [Close with a genuine question to the room.]
   [Optional: ONE product link, at the bottom, after value. Never in no-link subs.]
   ```

8. **Never use crypto framing outside crypto-native subs.** In the data, all crypto-framed titles were removed where the technical framing of the same story survived. For a Miroshark/onchain story going to a general/tech sub, frame it as agents/simulation/tooling, not tokens.

9. **Emit output to a temp file, then send via `./notify -f`:**
   ```
   *Reddit Playbook - ${today}*
   <days_since_last_promo>d since last promo - archetype <X> - <n> drafts

   _Story:_ [one-line what we're promoting] - [url]
   _Archetype:_ <letter + name> - <one-line why the tree picked it>

   ---
   *r/SubredditName* - tier: green - archetype: <letter>
   *Title:* <title>          (product absent unless archetype C)
   *Body:*
   <body text, ready to paste - third-party links inline, one product link at the bottom>
   *Proof links:* <the third-party URLs used>
   *Product link:* <resolved canonical url, or "none - no-link sub">
   *Post here:* [Open r/SubredditName composer](<submit url, title pre-filled>)
   _notes: <rule/flair/disclosure reminder + re-measure day 7 and 14>_

   ---
   *r/CommentOnlySub* - tier: comment-only
   *Comment draft:* <value-first comment, no unsolicited link>
   _notes: place as a COMMENT, not a post - this sub removes self-promo posts._
   ```
   Every post draft carries its **Proof links**, its single **Product link** (or "none"), and a one-click **Post here** submit link. Write to `/tmp/reddit-playbook-output.md`, then run `./notify -f /tmp/reddit-playbook-output.md`. Skip on `dry-run`.

10. **Update the seen-file.** Append the promoted story URL (and supporting-item URLs used) to `memory/reddit-promo-seen.txt`, one per line, so neither this skill nor `reddit-promo` re-promotes them.

11. **Log to `memory/logs/${today}.md`:**
    ```
    ### reddit-playbook
    - status: REDDIT_PLAYBOOK_OK
    - story: [one-line] - [url]
    - archetype: <letter + name>
    - subreddits: r/A (green), r/B (green), r/C (comment)
    - drafted: N posts, M comments
    - notified: yes|dry-run
    ```
    If skipped: `- status: REDDIT_PLAYBOOK_SKIP: <reason>`.

## Pre-post checklist (put this in the notes so the operator can gate each draft)

- Archetype chosen via the tree (news beats everything if it exists today).
- Product absent from the title (unless Archetype C milestone).
- Every checkable claim links to a third-party source.
- Sub is on the green list - or reframed as a pure question, or demoted to a comment.
- No crypto framing outside crypto-native subs.
- Max one product link, at the bottom.
- Title reworded vs any other sub getting the same story.
- Re-measure reminder: Reddit posts accrue for 1-2+ weeks; check at day 7, re-check at day 14, treat every number as a floor. Log removals separately (they report no view data), never as a zero.

## Reddit rules to bake into every draft

- **Value first, ad second.** The post must be interesting even to someone who never clicks the link.
- **Disclose.** Post as the builder - "I built / I work on Aeon." Never pretend to be a neutral discoverer. The notes must remind the operator of any required self-promo flair or disclosure line.
- **One link, native, at the bottom.** No UTM spam, no wall of links.
- **No duplicate text across subs** - each draft is rewritten, not templated.
- **Respect the 9:1 / sub-specific self-promo ratio.** Flag strict subs in the notes.
- **Drafts only.** This skill never posts to Reddit and needs no Reddit credentials.

## Default tiered subreddit map (fallback if config missing)

**Green (post archetypes A-E):** r/artificial, r/ArtificialInteligence, r/LLMDevs, r/AI_Agents, r/AgentsOfAI, r/AIAgentsInAction, r/coolgithubprojects, r/automation, r/nocode, r/ethdev, r/googlecloud, r/cursor, r/nvidia, r/OpenSourceAI. (Miroshark: r/footballtactics, r/EventMarkets, r/PredictionMarkets, r/sportsanalytics, r/Kalshi.)

**Question-only (Archetype B framing only):** r/ClaudeCode, r/Polymarket.

**Comment-only (place comments, never posts):** r/programming, r/devsecops, r/cybersecurity, r/vibecoding, r/aiagents, r/LovingOpenSourceAI, r/homelab, r/soccer, r/dataisbeautiful.

## Archetype angle notes (keep positioning honest)

Aeon: *the most autonomous agent framework - skills-as-markdown on GitHub Actions, cron + chains + self-repair, public traces, self-evolving on fork; open-source (AGPL).* Miroshark: *universal swarm-simulation engine, hundreds of grounded agents, ~$1 in <10min, x402-native.* Whatever the archetype, the product is one honest sentence of evidence, never the headline.

## Sandbox Note

Reads only local files (`memory/`, `apps/dashboard/outputs/`, `soul/`). No outbound network calls, no API keys, no `curl`. `./notify -f` handles delivery and falls back to `.pending-notify/` if the sandbox blocks the send.

## No Environment Variables Required

Reuses the committed `fetch-tweets` output already on disk plus `./notify`.
