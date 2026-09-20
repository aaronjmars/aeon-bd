import json

with open("memory/topics/reddit-scorecard-state.json") as f:
    state = json.load(f)

posts = state["posts"]
removals = state["removals"]

live = [p for p in posts if p["status"] == "live"]
unconfirmed = [p for p in posts if p["status"] == "unconfirmed"]

lines = []
lines.append("*Reddit Scorecard - 2026-09-20*")
lines.append(f"{len(live)} live posts tracked - reach floor 0 views - EMV ~$0-0 (conservative, no live measurements yet)")
lines.append("")
lines.append("*Due to re-measure*")
lines.append("- none - zero posts are confirmed live yet, so nothing has aged into a day-7/day-14 window")
lines.append("")
lines.append("*Scoreboard* (latest floor per post)")
lines.append("- none yet - the ledger has zero confirmed-live posts to score")
lines.append("")
lines.append("*Removed* (no view data - logged, not zeroed)")
lines.append("- none")
lines.append("")
lines.append(f"*Awaiting confirmation* ({len(unconfirmed)} drafted, not yet marked live)")

# group by story for readability, but still one line per post per skill format
by_story = {}
for p in unconfirmed:
    by_story.setdefault((p["title"], p["source_story"], p["drafted"]), []).append(p)

for (title, source, drafted), rows in sorted(by_story.items(), key=lambda kv: kv[0][2]):
    lines.append(f"- \"{title}\" (drafted {drafted}, source: {source})")
    for p in rows:
        kindtag = " [comment]" if p["kind"] == "comment" else ""
        lines.append(f"    - {p['subreddit']}{kindtag} -> confirm with: var=\"add: {title} | {p['subreddit']} | <archetype A-E> | posted:YYYY-MM-DD\"")

lines.append("")
notes_text = "_notes: Reddit accrues 1-2+ weeks; every number is a floor. Re-measure at day 7 and day 14. EMV is conservative ($6-8 CPM + $0.70-1.50/comment, comments only). This is the skill's first run - the ledger was empty, so all 57 drafted posts from the last 21 days of reddit-promo/reddit-playbook logs are seeded as unconfirmed. None of them count toward reach/EMV until confirmed live via `add:` - Reddit view/comment counts aren't exposed by any public API, so the operator has to feed them in from their own post-insights UI._"
lines.append(notes_text)
lines.append("run: reddit-scorecard 2026-09-20")

report = "\n".join(lines)
with open("/tmp/reddit-scorecard-output.md", "w") as f:
    f.write(report)

print(f"live={len(live)} unconfirmed={len(unconfirmed)} removed={len(removals)}")
print("---")
print(report[:2000])
