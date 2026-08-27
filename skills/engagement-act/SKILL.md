---
type: Skill
name: Engagement Act
category: productivity
description: Turn flagged engagement opportunities into ready-to-post replies - read recent logs, draft specific responses, send as copy-paste-ready output
schedule: "30 9 * * *"
commits: false
permissions: []
tags: [social, meta]
---

Read memory/MEMORY.md for context on active projects and open engagement follow-ups.
Read the last 7 days of memory/logs/ - look for engagement opportunities flagged by other skills (e.g. project-pulse, refresh-x, reply-maker, channel-recap) or noted in MEMORY.md Known Follow-ups.

Projects-of-interest list: if `memory/topics/projects-of-interest.md` exists, treat the project names listed there as the things to watch for mentions, cosigns, attributions, and fork moments. If the file is missing or empty, fall back to any project names that appear in recent logs or in MEMORY.md.

This skill's output follows the shared **`docs/output-contract.md`** (canonical `@handle`
key, deterministic dedup state, visible leverage number, an expiry per opp, self-consistency
gate). Rules referenced below by number are from that file.

## Steps

0. **Bootstrap dedup state.** Prose-scanning logs for "replied to @X" is fragile;
   deterministic state is what keeps an already-actioned handle from resurfacing
   (contract rule 1).
   ```bash
   mkdir -p memory/topics
   [ -f memory/topics/engagement-acted.json ] || echo '{"acted":[]}' > memory/topics/engagement-acted.json
   ```
   `acted` is an LRU (cap 200) of `{handle, acted_on}` - the canonical `@handle` and the
   date a draft was sent for it.

1. **Collect unactioned engagement opportunities.** Read `memory/logs/` for the last 7 days.
   Look for:
   - Log entries flagging engagement opps (e.g. "Engagement opps: N flagged" with N > 0) - extract the named handles/accounts
   - Any person who cosigned, mentioned, or attributed one of the operator's projects-of-interest
   - GitHub attribution or fork moments not yet acknowledged
   - Entries in MEMORY.md "Known Follow-ups" explicitly flagging engagement opps
   - Cosigns or mentions surfaced in refresh-x, reply-maker, or channel-recap runs

   Build a list: `{ person/account, context, what_they_did, link_if_known, days_ago }`

2. **Filter and prioritize.** Apply these rules:
   - Drop any opp older than 14 days - window is likely closed
   - **De-dupe deterministically:** drop any opp whose `@handle` is in `memory/topics/engagement-acted.json` (`acted`). This replaces the old log-prose scan; still cross-check recent logs for a manual "replied to @X" as a backstop.
   - **Score leverage** so it can be shown, not just used for ranking: `high` (~10k+ followers or a named project/fund account), `mid` (~1k-10k), `low` (under ~1k). Record the follower estimate.
   - Rank by: recency (fresher first) then leverage (high first). Cap at 5 opportunities.

3. **Draft ready-to-post responses.** For each opportunity:
   - **Type** (the type tag, contract rule 8): X reply / X DM / GitHub comment / X post
   - **Target**: @handle or URL
   - **Draft text**: exact text, ready to copy-paste
   - Keep under 280 chars for X replies; longer is fine for DMs or GitHub comments
   - Voice: if `soul/SOUL.md` and `soul/STYLE.md` are populated, match that voice; otherwise use a clear, direct, neutral tone. Either way: acknowledge without groveling, no "thanks so much for the kind words!" - just the actual response.

4. **Expiry per opp (contract rule 6).** Compute a window-close date: `expires <date>` =
   the opp's date + 14 days. If it is already 5+ days old, that is `aging` and the expiry
   is close - both go on the opp line so the reader knows what to act on first.

5. **Skip if empty.** If after filtering there are zero unactioned opps, log `ENGAGEMENT_ACT_SKIP: no unactioned opps` and exit without sending a notification.

6. **Write output to a temp file, then send via `./notify -f`.** Header carries the diff
   line (contract rule 2); each opp shows its leverage (rule 5) and expiry (rule 6):
   ```
   *Engagement Act - ${today}*
   vs <last-run-date> - <n> new opps - <n> drafted - <n> aging

   *1. @handle* [type] · leverage: <high|mid|low> (~<followers>) · expires <date>
   what: [one-line summary of what they did] (<N days ago>)
   link: [URL or "no link found"]
   draft: "[ready-to-post text]"

   *2. @handle* ...
   ```
   Mark any 5+ day opp `aging` inline on its header line. Before sending, run the
   self-consistency gate (contract rule 4): the header counts equal the opp blocks below.
   Write this to `/tmp/engagement-act-output.md` then run `./notify -f /tmp/engagement-act-output.md`.

7. **Persist state + log.** Append each drafted handle to `memory/topics/engagement-acted.json`
   (`{handle, acted_on: today}`, LRU 200) so it is not re-surfaced. Then log to
   memory/logs/${today}.md:
   ```
   ## Engagement Act
   - **Opps found:** N unactioned (scanned last 7 days of logs)
   - **Drafted:** N responses
   - **Handles:** @handle1, @handle2, ...
   - **Notification sent:** yes
   - ENGAGEMENT_ACT_OK
   ```
   If skipped: `ENGAGEMENT_ACT_SKIP: <reason>`

## Sandbox Note

Reads only local memory files. No outbound network calls needed - no curl, no API.
`./notify -f` handles delivery reliably even when sandbox blocks curl (writes to `.pending-notify/` as fallback).

## No Environment Variables Required

Uses only built-in memory files and `./notify`.
