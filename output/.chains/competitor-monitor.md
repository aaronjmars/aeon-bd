## Competitor Monitor — 2026-09-09

**Watch list:** 1 page from `memory/competitors.md` — `https://www.nvidia.com/en-us/security/acknowledgements/`

**Fetch:** succeeded (HTTP 200). Real signals pulled from the live page:
- Title: "NVIDIA Product Security Acknowledgements"
- Meta description: "NVIDIA Product Security Acknowledgements"
- H1: "Product Security"
- Prices: none
- ~150 nav/footer links, 6294 words, no PSIRT-acknowledgement-list content visible server-side (the actual acknowledgee names likely render client-side, so this page is thin server-rendered signal regardless of the write issue — flagging per the skill's own guidance rather than inventing signal)

**Blocked:** could not persist the snapshot. `memory/`, `memory/logs/`, `memory/competitor-monitor/`, and `output/` are all mounted **EROFS** (read-only) in this session — verified directly (`fs.accessSync(..., W_OK)` throws `EROFS` on every path under the repo, `mkdir`/`node fs.writeFileSync` all fail the same way). This contradicts the documented contract in both `CLAUDE.md` ("read-only guard... preserves `memory/` and `output/`") and this skill's own `SKILL.md` ("read-only guard reverts writes to code/config paths but preserves `memory/` and `output/`"). No baseline could be saved, so no diff, no `CHANGES.md` update, no log append was possible from this run's own tools.

**This is a repeat, not a new finding.** The 18:32:58Z run today hit the identical EROFS wall (`memory/skill-health/competitor-monitor.json`: quality_score 3, "core functionality blocked by OS-level read-only mount") and already sent a Telegram notification about it (`memory/telegram-threads/competitor-monitor.json` shows a message was delivered). Sending another `./notify` ~26 minutes later for the same infra fact would be duplicate noise, so I did **not** re-notify — per the standing rule not to re-report an already-surfaced signal within the same window.

**Status code:** `COMPETITOR_MONITOR_ERROR reason=write-blocked (EROFS across memory/ and output/, not code/config-only as documented)`

## Summary
- Executed the skill's fetch step against the 1-page watch list; fetch succeeded, signals extracted cleanly.
- Could not write anything to disk (repo checkout is fully read-only this session, not just code/config paths) — no snapshot, diff, `CHANGES.md`, or log entry was produced by my own tools.
- Skipped `./notify` to avoid duplicating the alert already sent by the 18:32:58Z run today for the same underlying blocker.
- Follow-up needed (operator-side, outside this skill): the read-only sandbox for this repo needs to actually preserve write access to `memory/` and `output/` as documented, or `competitor-monitor` (and any other read-only skill relying on that guarantee) can never establish a baseline. Worth checking whether this is a fork-specific sandbox misconfiguration introduced/widened recently (memory already tracks a pattern of the sandbox scope "widening" over time — see `memory/MEMORY.md` Lessons Learned).
- Separately, worth a sanity check on whether `nvidia.com/security/acknowledgements` is the intended competitor watch entry — it's not a competitor of Aeon/Miroshark and carries no pricing/product signal, so even with writes working this page would rarely produce actionable BD signal.
