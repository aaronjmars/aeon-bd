🔵 heartbeat — scheduling smell, 2nd morning straight

war-room ran on yesterday's data again today. not a failure — product-pulse + bd-radar both succeeded (07:59 / 08:04). they just committed *after* war-room had already read them.

root cause: github batched all three delayed crons and fired them together at 07:56. the 07:15→07:20→07:45 stagger collapsed — war-room raced its own inputs and lost. it fell back to the 06-12 digests.

fix: push war-room to ~09:00 utc. real buffer past the observed 08:04 upstream finish, even when crons fire late. one-line change in aeon.yml.

everything else green — 0 failed, 0 stuck, 0 open PRs/issues.
