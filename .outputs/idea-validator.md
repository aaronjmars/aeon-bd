`IDEA_VALIDATOR_SKIP: no backlog at memory/topics/startup-ideas.md` — the file doesn't exist so there's nothing to screen.

To activate this skill, create `memory/topics/startup-ideas.md` with a table like:

```markdown
| Date Added | Name | One-liner | Theme |
|------------|------|-----------|-------|
| 2026-06-12 | Example Idea | one sentence description | crypto/AI/consumer |
```

Once that file has entries, the next `idea-validator` run will pick up the oldest unscreened batch, research competition + timing, score them, and send a ranked notification.

## Summary

- Read skill spec, soul files, and memory context
- Found `memory/topics/startup-ideas.md` does not exist
- Logged `IDEA_VALIDATOR_SKIP` to `memory/logs/2026-06-12.md`
- **Follow-up needed:** populate the ideas backlog file to enable future screening runs
