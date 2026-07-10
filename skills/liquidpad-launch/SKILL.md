---
type: Skill
name: LiquidPad Launch
category: crypto
description: Deploy a LiquidPad token on Base in-run via its public API. Routes 80% fees to deployer, 15% to LPAD burn, 5% to LIQ buyback, contract-enforced.
var: ""
tags: [defi, base, launchpad, token-launch]
requires: [LIQUIDPAD_API_KEY]
capabilities: [external_api, writes_external_host, onchain_writes, sends_notifications]
---

> **${var}** — Token concept (free-form vibe ≥ 6 chars, or a JSON object with `{name, symbol, theme}`). If empty, the skill derives a vibe from `memory/MEMORY.md` and `memory/topics/`.
> Env: `LIQUIDPAD_API_KEY` (injected in-run via `requires:`; passed to `./secretcurl` only as the `{LIQUIDPAD_API_KEY}` placeholder — never a bare `$LIQUIDPAD_API_KEY`) and `LIQUIDPAD_DRY_RUN=1` (dry-run: run the policy, print the payload, deploy nothing).

Deploy a token on Base **in-run** through LiquidPad's public API (`./secretcurl` with the `{LIQUIDPAD_API_KEY}` placeholder). The skill decides *whether* to deploy (running the safety policy below) and, if every check passes, performs the deploy itself as its **final, fail-closed action** — there is no deferred/postprocess step.

The skill exists because every aeon agent that wants to ship a token shouldn't have to re-derive the deploy flow — LiquidPad's contract-enforced fee split (80/15/5) plus ERC-8004 stamping are the parts most agents reinvent badly.

Read `memory/MEMORY.md` and `memory/topics/` to ground the concept in the agent's current context.
Read the last 7 days of `memory/logs/` to avoid duplicate launches (same name or ticker).

## How the deploy runs (in-run)

1. **Resolve the concept.** If `${var}` is a JSON `{name, symbol, theme}`, use it. Else if `${var}` is a vibe string ≥ 6 chars, fetch a concept in-run via `POST /agent/concept` (`./secretcurl` with `{LIQUIDPAD_API_KEY}`). Else derive one deterministically from `memory/MEMORY.md` and `memory/topics/`.
2. **Run the safety policy** (below). Any failed check ⇒ log a specific `SKIP:<reason>` and stop. Nothing is deployed.
3. **Deploy in-run.** If every check passes (and `LIQUIDPAD_DRY_RUN` is not set), `POST /agent/run-once` via `./secretcurl` as the skill's final action, capture the result, persist state, and notify. `LIQUIDPAD_DRY_RUN=1` runs the whole policy and prints the payload but makes **no** deploy call.

A deploy is contract-enforced (fee split) and irreversible, so it is the skill's last action behind the fail-closed policy — never "deploy anyway" on a failed or unverifiable check.

## Safety policy

A deploy runs only when every one of the following holds:

- **Concept fields valid**: `name` (1–32 chars), `symbol` (2–10 alphanumeric, uppercased), `theme` (1 sentence, ≤ 200 chars). Reject empty / placeholder values.
- **No same-day duplicate**: search `memory/logs/` for an entry with the same `symbol` in the last 24h. Found → log `SKIP:duplicate-symbol:<TICKER>` and stop.
- **No banned-list match**: refuse if `name` or `symbol` matches any line in `memory/topics/liquidpad-banlist.md` (operator-curated list).
- **Owner wallet present**: `OWNER_WALLET` env, OR a single `0x[a-fA-F0-9]{40}` under a labeled `## Owner Wallet` section in `memory/watched-repos.md`. The deployed token's creator fees route to this address. The skill MUST NOT pick the first `0x` address it finds elsewhere in the file — only the `OWNER_WALLET` env or the `## Owner Wallet` section is honored. No wallet → log `SKIP:no-owner-wallet` and stop. Never deploy with a placeholder.
- **Daily cap**: `MAX_LAUNCHES_PER_DAY` (default 1). Count deploys in `memory/topics/liquidpad-state.json` for today. Cap reached → log `SKIP:daily-cap` and stop.

## Steps

0. **Bootstrap state** — per-day launch counter lives in `memory/topics/liquidpad-state.json`:
   ```bash
   mkdir -p memory/topics
   [ -f memory/topics/liquidpad-state.json ] || echo '{"launches":[]}' > memory/topics/liquidpad-state.json
   ```
   Schema:
   ```json
   {
     "launches": [
       {
         "ts": "2026-05-25T14:00:00Z",
         "symbol": "GMTC",
         "name": "Ghost Matcha",
         "req_id": "20260525T140000Z-GMTC",
         "owner": "0xWallet..."
       }
     ]
   }
   ```
   Cap to 100 most-recent entries (LRU by `ts`). Validate with `jq empty` after every write; restore from `.bak` on failure.

1. **Resolve concept** — three paths, in priority order:

   a. `${var}` is a JSON object with `{name, symbol, theme}` → use it directly.

   b. `${var}` is a vibe string ≥ 6 chars → fetch a concept **in-run** via `POST /agent/concept` (`./secretcurl` with the `{LIQUIDPAD_API_KEY}` placeholder — never a bare `$LIQUIDPAD_API_KEY`):
      ```bash
      VIBE="${var}"
      RESP=$(./secretcurl -sS --max-time 30 -w '\nhttp=%{http_code}' -X POST \
        "https://api.liquidpad.site/agent/concept" \
        -H "Authorization: Bearer {LIQUIDPAD_API_KEY}" -H "Content-Type: application/json" \
        -d "$(jq -n --arg vibe "$VIBE" '{vibe: $vibe}')")
      echo "$RESP" | tail -1                         # http=<code>
      BODY=$(echo "$RESP" | sed '$d')                # strip the trailing http= line
      NAME=$(echo "$BODY"   | jq -r '.name // empty'   2>/dev/null)
      SYMBOL=$(echo "$BODY" | jq -r '.symbol // empty' 2>/dev/null)
      THEME=$(echo "$BODY"  | jq -r '.theme // empty'  2>/dev/null)
      ```
      On a non-2xx / timeout / empty body, or any empty field, fall through to (c) — never block the run on the concept fetch.

   c. `${var}` is empty (or the concept fetch yielded nothing) → derive name/symbol/theme deterministically from `memory/MEMORY.md` and `memory/topics/`. If no concept can be derived, log `SKIP:no-concept-source` and stop.

2. **Validate concept** against the safety policy. Each rejection records a verdict with a specific reason — `SKIP:invalid-symbol:gmtc-too-short`, `SKIP:duplicate-symbol:GMTC` — never vague.

3. **Resolve owner wallet** (env wins; otherwise read ONLY the labeled `## Owner Wallet` section, never elsewhere in the file):
   ```bash
   if [[ -n "${OWNER_WALLET:-}" ]]; then
     OWNER="$OWNER_WALLET"
   else
     # Extract the section delimited by "## Owner Wallet" to the next "## " header,
     # then take the first 0x address inside that range. This pins fee routing to
     # the maintainer-pinned address — not any 0x that happens to appear above.
     OWNER=$(awk "/^## Owner Wallet[[:space:]]*$/{flag=1; next} /^## /{flag=0} flag" memory/watched-repos.md 2>/dev/null | grep -oE "0x[a-fA-F0-9]{40}" | head -1)
   fi
   if [[ -z "${OWNER:-}" ]]; then
     echo "SKIP:no-owner-wallet"; exit 0
   fi
   if ! [[ "$OWNER" =~ ^0x[a-fA-F0-9]{40}$ ]]; then
     echo "SKIP:invalid-owner-wallet"; exit 0
   fi
   ```

4. **Build the payload and deploy in-run.** This is the skill's **final, fail-closed** action — run it only after every safety-policy check passes. Build the request:
   ```bash
   REQ_ID="$(date -u +%Y%m%dT%H%M%SZ)-${SYMBOL}"
   PAYLOAD=$(jq -n \
     --arg name "$NAME" \
     --arg symbol "$SYMBOL" \
     --arg theme "$THEME" \
     --arg owner "$OWNER" \
     --argjson mc "${MC_ETH:-5}" \
     '{
        ownerAddress: $owner,
        name: $name,
        symbol: $symbol,
        theme: $theme,
        mcEth: $mc,
        withImage: true,
        runImmediately: false
      }')
   ```

   **Dry-run.** If `LIQUIDPAD_DRY_RUN` is `1` (or `true`), print the payload, log `Result: dry-run <req_id>` (no deploy), and skip to step 5 — make **no** `/agent/run-once` call.

   **Deploy.** Otherwise POST it in-run (`{LIQUIDPAD_API_KEY}` placeholder — never a bare `$LIQUIDPAD_API_KEY`; the Bash permission layer refuses a secret on the command line, and plain `curl` must not carry the key):
   ```bash
   RESP=$(./secretcurl -sS --max-time 90 -w '\nhttp=%{http_code}' -X POST \
     "https://api.liquidpad.site/agent/run-once" \
     -H "Authorization: Bearer {LIQUIDPAD_API_KEY}" -H "Content-Type: application/json" \
     -d "$PAYLOAD")
   HTTP=$(echo "$RESP" | tail -1 | sed 's/^http=//')
   BODY=$(echo "$RESP" | sed '$d')
   ```
   Print `http=<code>`. On **200**: read `ADDR=$(echo "$BODY" | jq -r '.token.address // .address // empty')` and `TX=$(echo "$BODY" | jq -r '.txHash // .tx // empty')`, and notify success **once** via `./notify` (include name, symbol, address, tx). On any **non-2xx / timeout / empty body**: record the real reason (`http-<code>` / `timeout` / `empty`), notify the failure with the HTTP code, and do **not** retry blindly. Either way `REQ_ID` is the idempotency key — the same-day duplicate-symbol guard and the daily cap (safety policy) ensure a re-run can't redeploy the same token.

5. **Persist state** — append the launch entry to `memory/topics/liquidpad-state.json` (after the attempt, success or failure, so the 24h duplicate-symbol guard holds even when a deploy fails):
   ```json
   {
     "ts": "2026-05-25T14:30:00Z",
     "symbol": "GMTC",
     "name": "Ghost Matcha",
     "req_id": "20260525T143000Z-GMTC",
     "owner": "0xWallet..."
   }
   ```
   Validate with `jq empty`; restore `.bak` on failure.

6. **Log to memory/logs/${today}.md** under a `### liquidpad-launch` heading:
   - `Mode`: live | dry-run (read `LIQUIDPAD_DRY_RUN` env)
   - `Concept source`: var | fetched | derived
   - `Result`: deployed `<req_id>` (address, tx) | failed:`<http-code>` | dry-run:`<req_id>` | skipped:`<reason>`
   - `Owner`: 0xWallet... (last 4 chars only)
   - `Symbol`: GMTC

## Idempotency and re-runs

The deploy happens in-run and notifies exactly once, immediately. A re-run cannot redeploy the same token because the safety policy blocks it: the same-day duplicate-symbol guard (step 2, scanning `memory/logs/` and `memory/topics/liquidpad-state.json`) and the daily cap both reject a symbol already launched in the last 24h — even if the previous attempt failed. Never persist `LIQUIDPAD_API_KEY` to memory or logs; the launch entry stores only the owner (last 4 chars in the log), symbol, name, and `req_id`.

## Constraints

- **Never** deploy with `ownerAddress` set to a placeholder, the LiquidPad operator address, or any wallet not explicitly resolved from env or memory.
- **Always** call `api.liquidpad.site` via `./secretcurl` with the `{LIQUIDPAD_API_KEY}` placeholder — never a bare `$LIQUIDPAD_API_KEY` (the Bash permission layer refuses a secret on the command line) and never plain `curl`.
- **Never** redeploy the same `symbol` within 24h, even if the previous attempt failed — duplicate symbols on Uniswap V4 cause user confusion.
- **Never** deploy more than `MAX_LAUNCHES_PER_DAY` tokens per skill invocation.
- **Never** persist `LIQUIDPAD_API_KEY` to memory or logs — pass it only as the `{LIQUIDPAD_API_KEY}` placeholder to `./secretcurl`.

## Running this as part of the agent loop

To make autonomous-launch part of the agent's daily routine, add a `## Daily Routine` entry that invokes this skill conditionally — e.g. only on Mondays, only when `memory/topics/concept-queue.md` has unshipped entries. The daily cap (default 1) protects against runaway behavior; raise it via `MAX_LAUNCHES_PER_DAY` only after observing safe behavior.

## Reference

- LiquidPad public API: `https://api.liquidpad.site` (health, agent/status, agent/run-once, verify, agent/concept)
- Skill manifest (LLM-readable): `https://www.liquidpad.site/agent-owner-launch-skill.md`
- ERC-8004 agent record: `https://8004agents.ai/base/agent/50962`
- Ecosystem attribution + live contributions: `https://www.liquidpad.site/ecosystem`
- Telegram operator interface: `@liquidpadbot` (`/setaddress`, `/apikey`, `/fast Name SYMBOL`, `/ai <prompt>`)
