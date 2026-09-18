---
type: Skill
name: Reddit Scorecard
category: productivity
description: Retrospective on Reddit promo posts - re-measures each live post at day 7 and day 14 against a kept baseline, scores reach, reports conservative earned-media value, and logs removals separately (never as a zero). Closes the measurement loop for reddit-playbook / reddit-promo. Report only - never posts.
var: ""
commits: false
permissions: []
tags: [social, review, meta]
requires: []
---

Today is ${today}. This skill is the **measurement half** of the Reddit promo loop. `reddit-playbook` and `reddit-promo` draft posts; nothing tracks what actually got posted or how it accrued. Reddit posts keep gaining views for **1-2+ weeks** - a week-old snapshot undercounts (in the source data one post grew +23% untouched, another went 35 to 2,900 views after its measurement day). So this skill keeps a per-post baseline, re-measures at **day 7 and day 14**, and treats every number as a **floor**.

Reddit's per-post view/insight numbers are **not exposed by any public API** - they live in the poster's own post-insights UI. So this skill never fetches them; the operator feeds recorded numbers in through `var` (or by editing the state file), and the skill does the bookkeeping, scoring, and reminders. Zero network, zero secrets.

Read `memory/MEMORY.md` and `STRATEGY.md` for positioning. If `soul/SOUL.md` + `soul/STYLE.md` are populated, match that voice in the report; otherwise a plain, direct builder tone.

This skill's report follows the shared **`docs/output-contract.md`** (windows on every number, self-consistency gate, `run:` footer). Every reach number carries its measurement date and is stated as a floor.

## Var

`${var}` (all optional; multiple clauses separated by `;`):
- **empty** - report the current scorecard and list every post **due** for a day-7 or day-14 re-measure (with its insights URL to fill in). No numbers change.
- `add: <url-or-title> | r/Sub | <A-E> | posted:YYYY-MM-DD` - register a post that actually went live (the agent can only *draft*, so it does not know what the operator posted until told). `link:comment` instead of an archetype letter registers a comment placement.
- `measure: <url-or-title> = <views>[/<comments>] @YYYY-MM-DD` - record a re-measurement. Repeatable in one clause, comma-separated. The date defaults to `${today}`.
- `removed: <url-or-title>[ @YYYY-MM-DD]` - mark a post removed by moderation. Removals report **no view data**; they are logged separately and **never counted as a zero**.
- `dry-run` - compute and log, but skip the notification.

## State - `memory/topics/reddit-scorecard-state.json`

The kept baseline ledger. **Un-kept baselines make week-over-week growth unrecoverable**, so this file is the point of the skill. Shape:

```json
{
  "posts": [
    {
      "key": "unique url or slugified title",
      "title": "the posted title",
      "subreddit": "r/artificial",
      "archetype": "A",
      "kind": "post",
      "posted": "2026-09-14",
      "status": "live",
      "measurements": [
        { "date": "2026-09-21", "views": 4200, "comments": 9, "day": 7 },
        { "date": "2026-09-28", "views": 5400, "comments": 11, "day": 14 }
      ],
      "removed_on": null,
      "source_story": "the promoted story url"
    }
  ],
  "removals": [
    { "key": "...", "subreddit": "r/devsecops", "posted": "2026-09-10", "removed_on": "2026-09-11", "reason": "no-self-promo sub" }
  ]
}
```

## Steps

### 0. Bootstrap
```bash
mkdir -p memory/topics
[ -f memory/topics/reddit-scorecard-state.json ] || echo '{"posts":[],"removals":[]}' > memory/topics/reddit-scorecard-state.json
```

### 1. Parse `var`
Split on `;`. Apply `add:` / `measure:` / `removed:` clauses to the state (below). `dry-run` sets the notify skip. Empty var is a pure report.

### 2. Seed candidates from the promo logs (unconfirmed)
Scan the last 21 days of `memory/logs/*.md` for `### reddit-playbook` and `### reddit-promo` blocks. Each carries the drafted `story`, `subreddits`, `archetype`, and date. For any (story, subreddit) pair **not already in the ledger**, add it with `status: "unconfirmed"` - a draft is not proof it was posted. Unconfirmed rows appear in the report under **"awaiting confirmation"** with a one-line `add:`-clause hint, and are **excluded** from all reach totals and earned-media math until an `add:` promotes them to `live`. This keeps the ledger honest: only operator-confirmed live posts count.

### 3. Apply ledger mutations
- **`add:`** - find the matching candidate (by url or title) or create a row; set `status: "live"`, `posted:`, `subreddit:`, `archetype:`/`kind:`.
- **`measure:`** - append a `{date, views, comments}` measurement to the matching **live** post; set its `day` field to the rounded (measured_date - posted) in days. Ignore a measurement on a `removed` post (log `RS_MEASURE_ON_REMOVED` and skip).
- **`removed:`** - set `status: "removed"`, `removed_on:`, and move a summary into `removals[]`. Do not delete the row.

### 4. Compute the due list
For every `live` post, `age = today - posted` (days):
- `age >= 7` and no measurement with `day >= 7` yet -> **due: day-7**.
- `age >= 14` and no measurement with `day >= 14` yet -> **due: day-14**.
Emit each due post with its **insights URL** so the operator can read the number: `https://www.reddit.com/<post-permalink>` if the key is a permalink, else the title + subreddit and a note to open post insights. Past day 14, stop nagging (accrual has largely settled).

### 5. Score each measured post
Use the **latest** measurement per post as the current floor.
- **Reach:** latest `views`, tagged with its date and marked a floor.
- **Growth:** if two+ measurements exist, `(latest.views - earliest.views) / earliest.views` as a percent (this is why the baseline is kept). Never negative-alarm on a floor that only moved up.
- **Verdict** (mirrors `picks-tracker`'s W/H/L honesty): **W** (strong) latest views >= 10,000; **H** (held) 1,000-9,999; **L** (low) < 1,000. Comments are a second signal - a low-view, high-comment post is a **discussion win**, flag it as `L+disc`.

### 6. Earned-media value (report as conservative)
Per the source protocol - **$6-8 CPM on views + $0.70-1.50 per engagement, comments only.** For the totals across all live measured posts:
```
EMV_low  = sum(views)/1000 * 6  + sum(comments) * 0.70
EMV_high = sum(views)/1000 * 8  + sum(comments) * 1.50
```
Report the **range** and state plainly it is a **conservative** estimate (views are floors; only comments count as engagement). Never present EMV as revenue.

### 7. Removals - separate ledger, never zero
List every `removals[]` entry in its own section: subreddit, date, reason. Removed posts report no view data; they are **not** counted as zero views and **not** in reach or EMV totals. A cluster of removals in the same sub is a routing signal - note it (candidate for the comment-only tier in `memory/topics/reddit-playbook-subreddits.md`).

### 8. Skip when there is nothing to say
If there are zero live posts, zero due re-measures, and no mutations this run, log `REDDIT_SCORECARD_SKIP: nothing to score or re-measure` and exit **without** notifying.

### 9. Emit the scorecard, then send via `./notify -f`
Write to `/tmp/reddit-scorecard-output.md`, then `./notify -f /tmp/reddit-scorecard-output.md` (skip on `dry-run`):
```
*Reddit Scorecard - ${today}*
<N live> posts tracked - reach floor <sum> views - EMV ~$<low>-<high> (conservative)

*Due to re-measure*
- r/artificial - "<title>" - posted <date>, day 7 due - open insights: <url>
- r/LLMDevs - "<title>" - posted <date>, day 14 due - open insights: <url>

*Scoreboard* (latest floor per post)
| post | sub | arch | day | views (floor) | comments | growth | verdict |
|------|-----|------|-----|---------------|----------|--------|---------|
| <title> | r/artificial | A | 14 | 5,400 | 11 | +23% | H |
...

*Removed* (no view data - logged, not zeroed)
- r/devsecops - "<title>" - removed <date> (no-self-promo sub)

*Awaiting confirmation* (drafted, not yet marked live)
- r/nvidia - "<title>" (2026-09-16) -> confirm with:  var="add: <url> | r/nvidia | A | posted:2026-09-16"

_notes: Reddit accrues 1-2+ weeks; every number is a floor. Re-measure at day 7 and day 14. EMV is conservative ($6-8 CPM + $0.70-1.50/comment, comments only)._
run: reddit-scorecard ${today}
```

### 10. Persist state + log
Write the mutated ledger back to `memory/topics/reddit-scorecard-state.json`. Then append to `memory/logs/${today}.md`:
```
### reddit-scorecard
- status: REDDIT_SCORECARD_OK
- tracked: N live, M removed, K awaiting
- reach floor: <sum> views across N posts
- emv: $<low>-<high> (conservative)
- due: <n> day-7, <n> day-14 re-measures flagged
- notified: yes|dry-run
```
If skipped: `- status: REDDIT_SCORECARD_SKIP: <reason>`.

## Measurement discipline (bake into every report)

- **Every number is a floor.** Reddit posts accrue for 1-2+ weeks; a snapshot undercounts. Never report a view count as final.
- **Keep the baseline.** Record the earliest measurement so week-over-week growth is recoverable. This is the whole reason the state file exists.
- **Removals are not zeros.** A removed post reports no view data - log it separately, never as 0 views (that would poison averages).
- **Comments are the engagement signal**, not views - a high-comment post can outrank a high-view one for BD value.
- **Conservative EMV only.** State the assumption every time; never let the figure read as revenue.

## Sandbox Note

Reads only local files (`memory/`, `soul/`) and writes `memory/topics/reddit-scorecard-state.json` + `memory/logs/`. No outbound network calls, no API keys, no `curl`. `./notify -f` handles delivery and falls back to `.pending-notify/` if the sandbox blocks the send.

## No Environment Variables Required

Operator-fed numbers (via `var` or the state file) plus `./notify`. Nothing else.
