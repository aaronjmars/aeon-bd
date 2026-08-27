# Output contract (digest skills)

Shared format rules for every skill that sends a human-facing digest to Telegram
(bd-radar, mention-radar, engagement-act, reddit-promo, and future ones). A skill's
own SKILL.md can add fields, but it may not drop a rule here. The goal is output you
can diff against yesterday, cannot self-contradict, and can act on without inventing
the missing half.

## The nine rules

1. **Canonical key per item, reused byte-identically.** Every item (lead, mention,
   opp, story) gets one stable key - a bare `@handle`, `owner/repo`, or a URL - and
   that exact string is reused across the header, the body, and the state file. A
   handle written three different ways cannot be matched to yesterday's run.

2. **Header states the discipline and the diff.** First line is the title + date.
   Second line is the diff vs the last run:
   `vs <last-run-date> - N new - N still-open - N dropped`.
   The reader learns the shape of the run before reading a single item.

3. **Field contract: every row carries all its fields.** No blanks, no dashes for a
   value you skipped. If you cannot fill a required field for an item, drop the item -
   a half-scored row is noise, not signal.

4. **Self-consistency gate before send.** The counts in the header must equal the rows
   in the body. No item may appear in two states that disagree (e.g. "dropped" up top
   and "still-open" below). Check this before calling `./notify`; if it fails, fix the
   output, do not send.

5. **Numbers carry their window.** `+3 forks/14d`, `~8k followers`, `+12 stars since
   08-25` - never a bare delta. A number without its window compares to nothing.

6. **Every call carries a falsifier or an expiry.** A next-move, a position, or a
   "reach out" gets one line naming either the single observable that reverses it
   (`flips if:`) or the date the window closes (`expires <date>`). A call with no
   falsifier is a vibe.

7. **Diagnostics live only in a `run:` footer.** Cache state, source misses,
   `key-unset`, `X_SOURCE=`, "Nth quiet run" streaks - none of that belongs inside an
   item line. One `run:` line at the bottom carries all of it.

8. **Type tag on every item.** Each item states its class up front (bd-radar `class`,
   mention-radar `category`, engagement-act `type`) so the reader can filter by the
   job it does.

9. **QUIET vs DROPPED.** An item missing from this run's signals is `QUIET`, not gone:
   name the source that went missing and give a re-check date. Only DROP an item after
   it is QUIET across two consecutive full-coverage runs. Never jump to DROP on one
   thin run.

## State files

Diffability (rules 1, 2, 9) requires committed state. Each skill keeps a small JSON
under `memory/topics/`, keyed by the canonical key (rule 1), with a `first_seen` date
and a `last_seen` date per item, plus an LRU cap so it cannot grow without bound. The
scheduler commits `memory/` after the run, so the next run can diff against it.
