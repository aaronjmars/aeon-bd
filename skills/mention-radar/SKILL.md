---
type: Skill
name: Mention Radar
category: productivity
description: Monitor external web and social mentions of the operator's active projects - surface what people are discovering, where they're confused, and where to engage
schedule: "25 7 2/2 * *"
commits: false
permissions: []
var: ""
tags: [social, dev]
requires: [TWITTER_API_KEY, XAI_API_KEY?]
---
> **${var}** - Comma-separated project names to track (e.g. "MyApp, my-lib"). If empty, derives targets from MEMORY.md and memory/topics/projects.md.

Read memory/MEMORY.md for current project status.
Read the last 3 days of memory/logs/ to avoid re-surfacing already-noted mentions.

This skill's output follows the shared **`docs/output-contract.md`** (diffable canonical
keys, header diff line, self-consistency gate, `run:` footer, QUIET-vs-DROPPED). The
rules referenced below by number are from that file.

## Steps

0. **Bootstrap dedup state.** Mention state is what makes the run diffable (contract
   rules 1, 2, 9) - without it the skill re-surfaces the same posts every cycle and
   tomorrow cannot tell new from old.
   ```bash
   mkdir -p memory/topics
   [ -f memory/topics/mention-radar-seen.json ] || echo '{"mentions":[],"quiet_streak":{}}' > memory/topics/mention-radar-seen.json
   ```
   `mentions` is an LRU (cap 300) of objects `{key, project, category, first_seen, last_seen}`
   where **`key`** is the canonical id (rule 1): for X, `x:<posturl>`; for the web,
   `<surface>:<url>` (e.g. `reddit:<permalink>`). `quiet_streak` maps each project to its
   consecutive-quiet run count (rule 9).

1. **Define the targets.**
   - If `${var}` is set: parse it as a comma-separated list of project names.
   - Otherwise: scan `memory/MEMORY.md` (goals, active topics) and `memory/topics/projects.md` (if it exists) for the operator's active projects. A target needs at least a name; collect a site/domain and a GitHub `owner/repo` too when known.
   - Cap at 6 targets - prefer the most active ones.
   - If zero targets can be derived: log `MENTION_RADAR_SKIP: no projects configured - set var or add projects to memory/topics/projects.md` and stop. No notification.

   For each target, build search terms:
   - The exact project name in quotes (e.g. `"MyApp" site:x.com OR site:reddit.com OR site:news.ycombinator.com`)
   - The domain if known (e.g. `"myapp.xyz"`)
   - The repo if known (e.g. `site:github.com owner/myapp`)

2. **Search for external mentions.** X/Twitter is fetched via twitterapi.io (**primary**), with the xAI Responses API as the fallback; the rest of the public web (Reddit, Farcaster, blogs, newsletters, GitHub Discussions, HN, Product Hunt) goes through WebSearch, which is also the **last-resort fallback** for X itself. Derive the operator's handle from `soul/SOUL.md` if present (call it `$OPERATOR`) so you can exclude their own posts.

   **Path A - twitterapi.io (primary, X/Twitter mentions).** Fast (~700ms), returns structured ground-truth tweet objects with exact engagement counts and real permalinks - no fabrication risk. `TWITTER_API_KEY` is injected (declared in `requires:`). For each target, build an `advanced_search` query - `("${NAME}" OR url:${DOMAIN}) since:${FROM_DATE}` (omit the `url:` term when `$DOMAIN` is empty), `queryType=Latest`. Use a unique tmp filename per target if you loop (e.g. `/tmp/tw-mr-$SLUG.json`). `$NAME`/`$DOMAIN` come from the target built in step 1:
   ```bash
   FROM_DATE=$(date -u -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d)
   Q='("'"${NAME}"'" OR url:'"${DOMAIN}"') since:'"${FROM_DATE}"   # drop the url: term when $DOMAIN is empty
   HTTP=$(./secretcurl -s -o /tmp/tw-mr.json -w '%{http_code}' -G "https://api.twitterapi.io/twitter/tweet/advanced_search" \
     --data-urlencode "query=$Q" --data-urlencode "queryType=Latest" \
     -H "X-API-Key: {TWITTER_API_KEY}")
   echo "twitterapi http=$HTTP bytes=$(wc -c </tmp/tw-mr.json)"
   ```
   On `HTTP=200` with tweets, parse the structured objects and feed the X mentions into categorization (step 4):
   ```bash
   jq -r '.tweets[] | [.id, .author.userName, .text, .createdAt, .likeCount, .retweetCount, .replyCount, .url] | @tsv' /tmp/tw-mr.json
   ```
   Each row is a real tweet: `author.userName`, `text`, `createdAt`, exact `likeCount`/`retweetCount`/`replyCount`, and the real `.url` permalink; `author.isBlueVerified` gauges reach. Exclude posts by `@${OPERATOR}` and by the project's own accounts. Paginate with `&cursor=<next_cursor>` while `.has_next_page` if you need more. Record `X_SOURCE=twitterapi`. If HTTP is non-2xx, the body carries no tweets, or the call times out, record the reason (`http-<code>`/`empty`/`timeout`) and fall to Path B.

   **Path B - xAI Grok x_search (X/Twitter fallback).** Only if Path A returned non-2xx, empty, or timeout. For each target, ask Grok's `x_search` who is talking about the project on X. See the **Fetching** contract below - set the Bash tool `timeout` to ≥180000, and capture the HTTP status. Use a unique tmp filename per target if you loop (e.g. `/tmp/xai-mr-$SLUG.json`). `$NAME`/`$DOMAIN`/`$REPO` come from the target built in step 1 (`$DOMAIN`/`$REPO` may be empty - leave them out if so):
   ```bash
   FROM_DATE=$(date -u -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d)
   TO_DATE=$(date -u +%Y-%m-%d)
   PROMPT="Search X for posts by OTHER people mentioning the project \"${NAME}\" (also its site ${DOMAIN} and repo ${REPO} when given), posted between ${FROM_DATE} and ${TO_DATE}. Exclude posts by the operator @${OPERATOR} and by the project's own accounts. For each mention return: @handle, the full post text, date, exact engagement counts (likes, retweets, replies; 0 if unknown), the poster's approximate follower count if visible, and the direct link https://x.com/handle/status/ID. Prioritize people discovering it for the first time, asking confused questions, hitting friction (setup/docs/missing feature), comparing it to a competitor, or requesting a feature. Return a numbered list; if nobody is talking about it, say so explicitly."
   jq -n --arg p "$PROMPT" --arg fd "$FROM_DATE" --arg td "$TO_DATE" \
     '{model:"grok-4-1-fast", input:[{role:"user",content:$p}], tools:[{type:"x_search",from_date:$fd,to_date:$td}]}' \
     > /tmp/xai-mr-payload.json
   HTTP=$(./secretcurl -s -o /tmp/xai-mr.json -w '%{http_code}' --max-time 150 -X POST "https://api.x.ai/v1/responses" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer {XAI_API_KEY}" \
     -d @/tmp/xai-mr-payload.json)
   echo "xai http=$HTTP bytes=$(wc -c </tmp/xai-mr.json)"
   ```
   On `HTTP=200` with a non-empty body, parse `/tmp/xai-mr.json` with `jq -r '.output[] | select(.type == "message") | .content[] | select(.type == "output_text") | .text'` and feed the X mentions into categorization (step 4). Record `X_SOURCE=api`.

   **Path C - WebSearch (broader web + X last resort).** Always use WebSearch for the non-X surfaces - Reddit, Farcaster, personal blogs, newsletters, GitHub Discussions, HN, Product Hunt:
   - Try both brand name and URL variants
   - Time-box to last 7 days where the search engine supports it
   - Skip results from the operator's own accounts and the project's own repos

   WebSearch is **also** the last-resort fallback for X/Twitter, but only when **both** Path A and Path B failed (`key-unset`, `http-<code>`, `empty`, or `timeout` - record the real reason per the **Fetching** contract, never blaming a key that was set). On the X fallback query `site:x.com "<project name>" after:${FROM_DATE}`; note in the log that X results came from WebSearch (lower quality) and set `X_SOURCE=websearch`.

3. **Also check GitHub network signals** for each target with a known repo:
   ```bash
   gh api repos/OWNER/REPO --jq '{stars: .stargazers_count, forks: .forks_count, watchers: .watchers_count}'
   ```
   Skip any repo that 404s (private or not yet public). Compare to the last log entry to compute deltas. If no prior data, record as baseline.

4. **Key, dedup, categorize.** For each mention, compute its canonical `key` (step 0),
   then look it up in `memory/topics/mention-radar-seen.json`:
   - **Already in `mentions`**: it is **still-open**, not new. Refresh its `last_seen`
     to today; carry its `first_seen` forward (contract rule 1). Keep it only if it is
     still worth acting on; otherwise let it age out of the digest (it stays in state).
   - **Not in `mentions`**: it is **new**. Add `{key, project, category, first_seen:
     today, last_seen: today}`.
   Then assign a **category** (the type tag, contract rule 8):
   - **Discovery** - person found the project for the first time, sharing it, impressed ("this is cool", star notification, share)
   - **Confusion** - person unclear on what it does, asking questions, mischaracterizing it
   - **Friction** - person ran into a problem (setup, docs, missing feature)
   - **Competitor comparison** - mentioned alongside or against a competing project
   - **Feature request / wish** - explicit ask for something missing
   - **Press / newsletter** - cited in a publication or digest

5. **Identify engagement opportunities.** Flag any mention where:
   - The person is confused and a 1-tweet clarification would help
   - A feature request aligns with what's being built
   - A competitor comparison is wrong or incomplete
   - A high-follower account discovered the project (high-leverage reply opportunity)

6. **Format the output** (under 4000 chars). Header states the discipline + the diff
   (contract rule 2); new mentions are marked `NEW`, carried ones show `since <first_seen>`
   (rule 1); every number carries its window (rule 5); diagnostics go in the `run:`
   footer only (rule 7):
   ```
   *Mention Radar - ${today}*
   vs <last-run-date> - <n> new - <n> still-open - <n> quiet

   {PROJECT NAME, uppercased}
   - NEW [category] @handle/source: [what they said] - [link]
   - [category] @handle/source (since <first_seen>): [what they said] - [link]
   ...
   (one section per target)

   ENGAGEMENT OPPORTUNITIES
   - @handle: [why worth replying] - [link]

   QUIET: [project] - no mentions this run (covered: <X_SOURCE>/web) - re-check <next-run-date>

   run: X_SOURCE=<twitterapi|api|websearch> · <any source miss> · stars <project> <delta>/<since date>
   ```
   **QUIET vs DROPPED (rule 9):** a project with zero mentions this cycle is `QUIET` -
   name the source that covered it and a re-check date, and increment its `quiet_streak`.
   Only drop a project's tracking after **two consecutive full-coverage quiet runs**
   (`quiet_streak >= 2` with `X_SOURCE` = `twitterapi` or `api`, the real X paths); a thin
   run (`X_SOURCE=websearch`) does not count toward the streak. On any fresh mention, reset
   that project's `quiet_streak` to 0.
   Skip a GitHub star delta under 5 - only surface notable jumps, and always with the window.

7. **Self-consistency + notify gate.** Before sending, verify the header counts equal
   the body rows (contract rule 4). Skip notification if ALL projects are quiet and no
   GitHub delta clears +5 stars; log `MENTION_RADAR_QUIET` instead.

8. **Send via `./notify`** if there's anything worth surfacing.

9. **Persist state + log.** Write the updated `memory/topics/mention-radar-seen.json`
   (new + refreshed mentions, LRU-capped at 300; updated `quiet_streak`). Then log to
   memory/logs/${today}.md:
   ```
   ## Mention Radar
   - **{project}:** [N new / N still-open / QUIET (streak M)]
   (one line per target)
   - **Top find:** [best mention in one line, or "none"]
   - **Engagement opps:** [N flagged, or 0]
   - **Dropped:** [projects hitting quiet_streak >= 2, or none]
   - **Notification sent:** yes/no
   ```

## Guidelines

- This is signal filtering, not a metrics report. One real conversation > ten impressions.
- Prioritize quality of mention over quantity. A thoughtful Reddit post or HN comment matters more than a retweet.
- Don't manufacture urgency. If there's nothing worth acting on, say so.
- Be specific - link the source, quote the key line, name the person if identifiable.
- The point is engagement opportunity and awareness, not vanity numbers.

## Fetching

`TWITTER_API_KEY` and `XAI_API_KEY` are **injected into your environment** for this skill (declared in `requires:`). **The primary fetch path for X/Twitter mentions is a direct `curl` to twitterapi.io's `advanced_search` with `X-API-Key: {TWITTER_API_KEY}`** (step 2, Path A) - fast (~700ms), returning structured ground-truth tweet objects with exact engagement counts and real permalinks (no fabrication risk). The xAI Responses API (`XAI_API_KEY`, Path B) is the fallback. There is no network sandbox blocking either; earlier versions of this skill claimed there was - that is stale and wrong. Just make the call.

**You MUST attempt Path A (twitterapi.io) before any X fallback.** The rules:

1. **Check, don't assume.** Run `[ -n "$TWITTER_API_KEY" ] && echo KEY_PRESENT || echo KEY_UNSET`. If `KEY_PRESENT` (it will be), you are required to try Path A.
2. **Allow enough time.** twitterapi.io usually answers in ~700ms; the xAI `x_search` fallback (Path B) typically takes 30-120s (it searches X live), so on that call **set the Bash tool `timeout` to at least 180000 (180s)** and keep **`--max-time 150`** on the curl so it fails cleanly rather than hanging. A curl that is slow is **not** a missing key - do not treat a timeout as "key unavailable".
3. **Capture the HTTP status** so the fallback decision is based on fact, not assumption. Every `./secretcurl` command must stay 100% literal (no `$VAR`); the query var `$Q` is not a secret, so it is fine:
   ```bash
   HTTP=$(./secretcurl -s -o /tmp/tw-mr.json -w '%{http_code}' -G "https://api.twitterapi.io/twitter/tweet/advanced_search" \
     --data-urlencode "query=$Q" --data-urlencode "queryType=Latest" -H "X-API-Key: {TWITTER_API_KEY}")
   echo "twitterapi http=$HTTP bytes=$(wc -c </tmp/tw-mr.json)"
   ```
   Then parse `/tmp/tw-mr.json` with `jq -r '.tweets[] | ...'`. `HTTP=200` with tweets → use it (`X_SOURCE=twitterapi`).
4. **Fall back only on a real failure**, and **record the true reason** - never blame a key that was set. Use one of: `key-unset` (only if step 1 said `KEY_UNSET`), `http-<code>` (non-2xx), `empty` (200 but no mentions parsed), `timeout` (curl exceeded `--max-time`). Path A failing → Path B (xAI); both failing → Path C (WebSearch).

**WebSearch / WebFetch are last-resort fallbacks only** for X - lower quality (WebSearch favours old high-engagement tweets). They remain the primary tool for the non-X web surfaces (Reddit, HN, blogs, etc.). Never reach for the X WebSearch fallback while a key works.

## Environment Variables

- `TWITTER_API_KEY` - twitterapi.io API key, sent as the `X-API-Key` header. Declared in `requires:`, so it is **injected into this skill's environment** and is the primary path for X/Twitter mentions (structured tweet objects with exact engagement counts + real permalinks).
- `XAI_API_KEY` - X.AI API key for Grok's `x_search` tool. Declared in `requires:` (optional `?`), so it is **injected into this skill's environment** and is the X/Twitter fallback (Path B) when twitterapi.io returns non-2xx/empty/timeout. If both keys are unset, X mentions degrade to the WebSearch fallback at lower quality; the broader-web search is unaffected.
- `gh` CLI - pre-authenticated in GitHub Actions; used for the GitHub network-signal check (step 3). Not an env var you set here.
