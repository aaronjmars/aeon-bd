Ran `reddit-promo` for 2026-09-21 — result: **skip, no fresh promotable item.**

## Scan

**Input:** today's `fetch-tweets` output (`memory/logs/2026-09-21.md` + `apps/dashboard/outputs/fetch-tweets-2026-09-21T17-08-02Z.json` for full tweet text) plus 7 days of `memory/logs/` (09-14 → 09-21), every unseen URL checked against `memory/reddit-promo-seen.txt` (98 entries).

**Today's crop — all 4 items rejected:**

| item | engagement | why rejected |
|---|---|---|
| [x.com/svector_eth](https://x.com/svector_eth/status/2102031245156745399) | 0/0/0 | Third-party praise for an **unreleased** "Riva" capability ("been using it for a while before the release... excited for people to finally see what riva can do") — matches today's aeon-update sync note on mcp-server Riva isolation, and it's the same lead who pitched Aeon to Jesse Pollak on 09-18. But Riva hasn't shipped publicly — building a Reddit post around a stranger's private-beta comment would announce an unannounced feature, not something Aeon can stand behind yet. This is a BD/engagement-act signal, not a promo anchor. |
| [x.com/thecultos](https://x.com/thecultos/status/2102035448453317061) | 3/2/0 | The recurring CultOS x402aff pitch ($0.20 vuln-audit, 10% commission) — same beat rejected nearly every run since 09-10 as an "overused supporting point," no new information this time. |
| [x.com/based_elnen](https://x.com/based_elnen/status/2102048727250714934) + [bankrbot](https://x.com/bankrbot/status/2102025399433925011) | 20/4/6, 1/0/0 | $AEON price/market chatter (a "load up, undervalued" pump post + automated price-bot readout) — brushes the no-financial-advice/no-buy-sell-calls hard constraint, excluded outright. |

**Prior-week check (09-14→09-20):** all already used (09-15 Hayden Adams/0xProject, 09-16 Miroshark bankrbot x402, 09-17 Musebook agentic-payment story, 09-19 CultOS usage-receipt numbers) or already judged and held (CultOS pitch, SmartSentinels_, carlosjmelgar, weaponheadsNFT, 0xNurstar — all feature-asks or market chatter). Nothing unseen and fresh in the 7-day window.

**Cadence clock:** 2 days since last promo (prior `REDDIT_PROMO_OK` 2026-09-19, CultOS usage-receipt story).

Per the skill's rule, silence beats a filler post — no `./notify` sent.

## Summary
- Read `fetch-tweets` output (logs + json-render + seen-file) for candidates; found none promotable today.
- Logged `### reddit-promo` block (`REDDIT_PROMO_SKIP: no fresh promotable items`) to `memory/logs/2026-09-21.md`.
- No files other than the log touched; `memory/reddit-promo-seen.txt` unchanged (nothing new promoted).
- Follow-up: none required — re-check tomorrow's fetch-tweets crop; Riva is worth watching once it's officially announced (it'd make a strong `shipped`-kind promo story then).
