🚨 4 skills down — one root cause

🔴 FLEET: 4 skills down this morning — one root cause, already fixed

bd-radar, heartbeat, engagement-act, aeon-update all failed 08:51–11:47 UTC. Identical signature: zero input/output tokens, instant die. Not four bugs. One.

**Claude sub was exhausted.** Fix landed 12:13 UTC — gateway hop to GLM (`04d56d5`). This heartbeat is the first run on the new route. It's alive.

- bd-radar — 3 consec fails (07:20 slot missed) → [#71](https://github.com/aeon-bd/aeon-bd/issues/71)
- heartbeat — 3 consec fails (08:00 slot missed) → [#72](https://github.com/aeon-bd/aeon-bd/issues/72)
- engagement-act — 3 consec fails (09:30 slot missed) → [#73](https://github.com/aeon-bd/aeon-bd/issues/73)
- aeon-update — 2 consec fails, Monday 11:00 slot lost → [#74](https://github.com/aeon-bd/aeon-bd/issues/74)

🟡 Monday's aeon-update run is gone — upstream sync watermark still `8b8d719`, 11 local conflicts still pending your call (unchanged since 08-25). Next shot is Monday 11:00 UTC.

🟢 Everything else green: mention-radar, fetch-tweets, reddit-promo, memory-flush all succeeded. No stuck skills, no chronic failures.

**Watch:** tonight 17:00 UTC (fetch-tweets) is GLM's first scheduled prove-it run. If it fails, the gateway fix didn't take — check `scripts/llm-gateway.sh` routing.

`STATUS_PAGE=DEGRADED` — [status page](https://aeon-bd.github.io/aeon-bd/status/)

🔗 https://github.com/aeon-bd/aeon-bd/blob/main/docs/status.md