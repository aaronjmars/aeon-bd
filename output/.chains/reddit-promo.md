## reddit-promo — 2026-09-08

**Status: `REDDIT_PROMO_SKIP: no fresh promotable items`**

Today's `fetch-tweets` run came back `FETCH_TWEETS_EMPTY` (0 of 15 candidates survived curation — just @xNovichok troll noise off a quiet 24h window). Falling back to the full 7-day lookback, every strong story is already promoted and sitting in `memory/reddit-promo-seen.txt`:

- CultOS x402-relay cluster (09-02) → r/StartupMind, r/LovingAI
- UsePodAI cheaper-inference cost lever (09-03) → r/Agent_AI, r/AIPromptProgramming, r/OpenSourceAI
- CultOS 5-project stack naming (09-04) → r/MiroFish, r/aiecosystem, r/Ollama, r/CoolGithubProjects
- OpenAI Daybreak program acceptance (09-05) → r/StartupMind, r/Agent_AI, r/lovingopensourceAI, r/AskVibecoders
- AIonBase_ TaskMarket Delegate roundup + svector_eth dogfooding trace (09-06) → r/CLaudeSkills, r/AIPromptProgramming, r/LovingAI
- Capminal ($CAPU) audit-fix credit (09-07, the most recent) → r/OpenSourceAI, r/aiecosystem, r/StartupMind, r/AskVibecoders

The remaining unseen URLs from the week don't clear the promotable bar and were already explicitly rejected by this skill or its sibling `reddit-playbook`: two sub-2-like co-signs too thin to carry a citation, a speculative/unshipped GitHub-collab tease, two outside integration/docs asks (not endorsements), the CultOS x402aff "opens to any builder" beat repeated a 3rd/4th time (spam risk), an account with a standing repeat-shill flag, a routine bot mention, two no-new-claim low-engagement posts, and two zero-engagement FUD posts from @xNovichok.

Today's one genuine signal — `@itsnina_kapoor`'s clean-discovery vibe post ("aeon framework looking clean") — came from mention-radar, not fetch-tweets, and is out of this skill's input scope; mention-radar itself called it too thin even for an engagement reply.

**Cadence clock:** 1 day since the last promo (2026-09-07, Capminal story) — informational only, doesn't gate this decision. Per the skill's own rule, silence beats a filler post, so no drafts, no notification.

## Summary
- Scanned today's `fetch-tweets` output (empty) plus 7 days of logs/dashboard JSON; cross-checked every candidate against `memory/reddit-promo-seen.txt`.
- Found zero fresh, unseen, promotable items — logged `REDDIT_PROMO_SKIP: no fresh promotable items` to `memory/logs/2026-09-08.md` under `### reddit-promo`.
- No drafts written, no `./notify` sent, `memory/reddit-promo-seen.txt` unchanged.
- Follow-up: none required — next run (09-09) should re-scan once fetch-tweets produces fresh candidates.
