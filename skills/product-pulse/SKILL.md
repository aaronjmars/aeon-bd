---
name: product-pulse
description: Daily "state of aeon + miroshark" — GitHub health across the repo family plus X follower/engagement deltas, with week-over-week deltas. The single "how are we doing" read.
var: ""
tags: [meta, dev, ecosystem]
---

> **${var}** — Optional. `dry-run` skips notify (state still updates, article still writes). Empty = normal run.

Today is ${today}. Read `STRATEGY.md` and `memory/MEMORY.md` for context. If `soul/SOUL.md` + `soul/STYLE.md` are populated, read them and write in Aaron's voice; otherwise neutral tone.

## Why this exists

Aaron + Nurstar ship two products — Aeon ⭐ and Miroshark 🦈 — across a sprawl of repos (public framework + agent automations, private API/X-bot/site/x402). The health picture is scattered: stars here, CI there, a release nobody announced, a follower bump no one clocked. `product-pulse` is the one daily read that answers **"how are the two products doing, vs yesterday and vs last week?"** It is the data spine the `war-room` brief consumes — so it stays factual and delta-driven, no narrative padding.

## Config

Reads `memory/watched-repos.md` for the repo list (public framework repos + the private product repos under the dedicated section). GitHub via authed `gh api`; X follower/post counts via the xAI prefetch cache (`scripts/prefetch-xai.sh` → `.xai-cache/product-pulse-x.json`, needs `XAI_API_KEY`) with a keyless WebSearch fallback. Reads/writes:

- `memory/topics/product-pulse-state.json` — yesterday's + last-week's snapshot, for deltas (LRU `history` capped at 30 daily entries).
- `articles/product-pulse-${today}.md` — the daily state digest.
- `memory/logs/${today}.md` — one `### product-pulse` log block per run.

## Steps

### 0. Bootstrap
```bash
mkdir -p memory/topics articles
[ -f memory/topics/product-pulse-state.json ] || echo '{"last_run":null,"snapshot":null,"history":[]}' > memory/topics/product-pulse-state.json
```

### 1. Parse var
- `${var}` starts with `dry-run` → `MODE=dry-run` (compute + write, skip notify). Else `MODE=execute`.

### 2. Gather GitHub health
For each **public** repo in `memory/watched-repos.md`, use `gh api` (default token, auth internal, works in the sandbox):
```bash
gh api repos/{owner}/{repo} --jq '{stars:.stargazers_count, issues:.open_issues_count, pushed:.pushed_at}'
gh api repos/{owner}/{repo}/commits --jq 'length' -f per_page=1   # latest commit date
gh api repos/{owner}/{repo}/releases/latest --jq '{tag:.tag_name, published:.published_at}' 2>/dev/null || echo "no-release"
gh api repos/{owner}/{repo}/pulls -f state=open --jq 'length'
```
For the **automation repos** (`aeon-agent`, `miroshark-aeon`) also pull recent Actions health — these are the public verifiable-run surface:
```bash
gh api repos/{owner}/{repo}/actions/runs -f per_page=20 --jq '[.workflow_runs[]|{name:.name, status:.status, concl:.conclusion, at:.created_at}]'
```
Record per repo: stars, open issues, open PRs, last-commit age (days), latest release tag/date, and (for automations) last-24h run pass/fail counts. If any `gh api` call fails, log `PRODUCT_PULSE_GH_MISS: {repo} (<reason>)` and continue — never abort on one repo.

**Private repos** — the default `gh api` token can't read them, so don't call `gh api` on them. Instead read `.xai-cache/private-repos.json`, prefetched outside the sandbox by `scripts/prefetch-private-repos.sh` using the read-only `GH_READ_PAT`. Each entry is `{repo, private, issues, open_prs, pushed, latest_release}` (no `stars` — private repos report 0). Fold them into the digest under their product: `aeon-website` / `aeon-wc` → Aeon ⭐, `miroshark-website` / `MiroShark-x402` → Miroshark 🦈. The PAT's scope determines which appear; any out-of-scope repo is simply absent (that's expected, not an error). If the file is missing/empty, log `PRODUCT_PULSE_PRIVATE_MISS` and proceed public-only.

### 3. Gather X signal (followers + post count for @aeonframework and @miroshark_)
xAI/grok owns X data, so use it. The workflow pre-fetches it **outside the sandbox** via `scripts/prefetch-xai.sh` (the `product-pulse` case), so the in-sandbox skill never curls with the secret. Resolve in this order:
- **Path A — prefetch cache (preferred):** read `.xai-cache/product-pulse-x.json` and pull the model text, which is two `handle|followers|posts` lines:
  ```bash
  jq -r '.output[]|select(.type=="message")|.content[]|select(.type=="output_text")|.text' .xai-cache/product-pulse-x.json
  ```
- **Path B — direct XAI (fallback, cache empty + `XAI_API_KEY` set):** `POST https://api.x.ai/v1/responses` with `{"model":"grok-4-1-fast","input":[{"role":"user","content":"<same handle|followers|posts prompt>"}],"tools":[{"type":"x_search"}]}`, parse the same way. Sandbox may block curl-with-secret — prefer Path A.
- **Path C — WebSearch (keyless fallback):** WebSearch `@aeonframework followers` and `@miroshark_ followers`; take the most recent figure. Log `X counts via WebSearch — approximate`.
- **Local mode only:** the x-mcp `get_user_profile` tool, if present (it is NOT on the Actions runner).

Capture `followers` + `posts` per handle. `posts` may come back as `unknown` (xAI couldn't resolve the lifetime count) — render it as `N/A` and skip its delta; `followers` is the metric that drives notables either way. If every path fails, log `PRODUCT_PULSE_X_MISS` and proceed GitHub-only — never fail the run over X data.

### 4. Compute deltas
Load `product-pulse-state.json`. Compute Δ vs the most recent prior snapshot (≈1 day) and vs the snapshot closest to 7 days ago. For every metric show: value, Δ1d, Δ7d. Flag **notables**:
- new release tag on any repo (not seen in history)
- any automation repo with ≥1 failed run in last 24h (CI red)
- star Δ7d ≥ +25 on aeon or MiroShark (momentum) or a crossed 100-multiple star milestone
- follower milestone crossed (next 500-multiple) on either handle
- a repo with last-commit age > 14d that was previously active (stall signal)

### 5. Write the digest
`articles/product-pulse-${today}.md`: a compact table per product (Aeon row-group, Miroshark row-group) with value / Δ1d / Δ7d, then a 2–4 bullet **"what changed"** list pulling only the notables. No filler. If nothing notable: say so in one line.

### 6. State + log
Append today's snapshot to `history` (drop entries older than 30 days), set `snapshot` + `last_run`. Append a `### product-pulse` log block: notable count, CI status, star/follower deltas.

### 7. Notify (gated)
This skill is primarily consumed by `war-room`, so it is **quiet by default**. Only self-notify (`./notify`) when `MODE=execute` AND a **red-flag** notable fired (CI red on an automation repo, or a previously-active repo stalled >14d). One line, Aaron's voice, lead with the flag. Otherwise no notification — the digest + state are enough.

## Sandbox note
GitHub data uses `gh api` (auth internal). X data comes from the `scripts/prefetch-xai.sh` cache (`.xai-cache/product-pulse-x.json`) — fetched outside the sandbox by the workflow before Claude starts — with WebSearch as the keyless fallback; x-mcp is local-mode only. No raw curl with `$ENV_VAR` headers inside the skill.

## Summary
Ends by writing the digest + state + log. The `## Summary` in the log block lists notables and deltas; no human-facing message unless a red-flag fired.
