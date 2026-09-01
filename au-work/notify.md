*aeon-update — 2026-09-01*
synced 34 commits → PR #77

Upstream `aeonfun/aeon` moved 8b8d719..3b4c5a3 (the window Monday's incident ate). 80 files applied clean, 8 need you — plus 2 old carryovers (heartbeat, memory-flush), unchanged.

The one that matters: **`scripts/llm-gateway.sh`**. Upstream shipped its own GLM routing — a80f70f (Claude AI Gateway arm) + 47d1a56 (tiered `GLM_MODEL_SONNET/OPUS/HAIKU` — flash for sonnet-tier, full model for opus-pinned). Your 04d56d5 pin is the same feature's other half: the effort-pinning. Merge = take their tiering, keep your effort exports. Five minutes, diff's in the PR body.

Also landed clean: api-gate exact-origin fix (#986, security), mcp-server single-flight queue (#973), telegram reply-to-previous-run (#995), xAI search retry (#989), envelope hard-fail (#987), new `cortx-reliability` skill.

Two loose ends closed: `rightstack` + `skill-article` are in — the SHA-pinned eyebrow binary downloaded + verified this run, one rescan locked everything (0 criticals). `skill-health` merged 3-way clean, your scorer edits kept. Pending conflicts 11 → 10.

(one for the canon backlog: upstream added cortx-reliability to skills.json but forgot its glyph — their own generate-skill-icons fails at HEAD. placeholder added here.)

PR: https://github.com/aaronjmars/aeon-bd/pull/77
