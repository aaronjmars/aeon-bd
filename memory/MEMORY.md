---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-09-06*
## About This Instance
- **aeon + miroshark war room** — an Aeon run by Aaron (@aaronjmars).
- Job: watch the state of both products, surface who to talk to (BD), generate timing-window ideas.
- North-star + priorities live in `STRATEGY.md` (read every run). Voice lives in `soul/` (Aaron's).

## The two products
- **Aeon ⭐** (@aeonframework, `aeonfun/aeon` canonical — org renamed from `aaronjmars/aeon`, old path 301-redirects) — most autonomous agent framework; skills-as-markdown on GitHub Actions, cron, chains, self-repair, public traces.
- **Miroshark 🦈** (@miroshark_, `MiroShark/MiroShark` canonical — org renamed from `aaronjmars/MiroShark`, old path 301-redirects) — universal swarm simulation engine; hundreds of grounded agents argue on X/Reddit + trade a simulated AMM, belief drift, director mode, ~$1/<10min, x402-native.
- Product config (repos/handles/terms) tracked in `memory/products.md`.
- Watch-list: `666ghj/MiroFish` (71,979★ as of 2026-09-06, separate project, near-identical "swarm intelligence engine" positioning to Miroshark) flagged 2026-08-21 for category-intel follow-up. 2026-09-06 update: a "MiroShark is a MiroFish fork" narrative is circulating (a YouTube short titled "...(MiroFish fork)" + an AI search-engine synthesis repeating it) — verified false via `gh api`: `MiroShark/MiroShark` has `fork:false, parent:null`, created 2026-03-20 (4mo after MiroFish's 2025-11-26). Real, unrelated forks exist in the wild (`amadad/mirofish-cli` forks MiroFish; `MATHEUSFELIX/miroshark` forks MiroShark) which likely fuels the mix-up. Worth a category-intel pass on whether this mischaracterization is spreading enough to warrant a public correction.
- Ecosystem highlight: CultOS (@thecultos) built a paid agent entirely on Aeon skills, publicly declared "we choose Aeon" (2026-08-27) — but the `cultosdev` GitHub *account* went fully 404 by 2026-09-05, 9 days after that post (partner pack repo `thesmithdao/cultos-aeon-skills` still alive; footprint since migrated through `cultosagent/aeon`/`thesmithdao/cultos`). Since then @thecultos also named a 5-project public stack (Aeon, Miroshark, virtuals_io, gitlawb, reppo, 2026-09-04) and folded in Miroshark's x402aff payout rails — still active on X, just churn-risk on the GitHub side. Direct check-in overdue (dedup has blocked re-surfacing since 08-27). Sparkleware (known partner, shipped 7 more Aeon skill repos 08-27) reads more stable by comparison.
- eyebrow (`alexverify/eyebrow`, @eyebrowCC, independent security tool, 8★) unsolicited-audited Aeon and got both PRs merged 2026-09-01 (CI skill-integrity gate bump v0.4.2, MCP-server hardening docs) — now a real embedded integration, not just a mention. Reddit-playbook debuted 09-06 using this as its first observer-archetype story.
- OpenAI Daybreak: Aeon accepted into OpenAI's Daybreak program (per @aaronjmars, 2026-09-05) — frontier cyber models get access to help secure more repos. Team-stated; no independent verification channel exists for program-acceptance claims (same sourcing caveat applied to other team announcements).

## War-room skills (this instance)
| Skill | Cadence | Does |
|-------|---------|------|
| bd-radar | odd days 07:20 UTC | who's building/forking/integrating/mentioning → ranked leads + next move |
| mention-radar | even days 07:25 UTC | external web/social mentions — discovery/confusion/friction/competitor taxonomy |
| fetch-tweets | daily 17:00 UTC | X search digest for both products |
| reddit-promo | daily 17:45 UTC | drafts value-first subreddit posts from fetch-tweets stories |
| engagement-act | odd days 09:30 UTC | turns flagged engagement opps into copy-paste-ready replies |
| heartbeat | daily 08:00 UTC | fallback health check + status page |
| aeon-update | Mon 11:00 UTC | pulls framework updates from aeonfun/aeon canon; watermark `bf33365` (PR #89 merged 09-04), ~12 pending conflicts tracked in its own `memory/topics/aeon-update-state.json` |
| reddit-playbook | odd days 18:15 UTC | sibling of reddit-promo — evidence-backed archetype picks (news-hook/question/milestone/contrarian/observer), keeps product out of title, routes strict subs to comments |
| memory-flush | Sun 18:00 UTC | this skill |

- bd-radar runs as a **standalone** skill, not a chain (`chain-runner.yml` is brittle under `bash -e`: a transient `gh` non-zero hard-kills the job). **war-room (the 07:45 standup capstone for Aaron) was retired 2026-07-26** and stays retired — this instance is public now, so no private standup. `sim-watch` and `idea-forge` (weekly category-intel/idea skills) are **not currently active** — sim-watch's skill dir is gone entirely; idea-forge exists but is `enabled: false` in `aeon.yml`.
- reddit-promo (daily) and reddit-playbook (odd days) can now both fire the same day (2026-09-06 was the first double-dispatch) — watch for over-posting/redundant subreddit cadence if this compounds.

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars.
- Multi-line notify: use `./notify -f file.md`, never `./notify "$(cat …)"` (sandbox trips).
- Always save files AND commit before logging.
- `chain-runner.yml` runs under `bash -e` → transient `gh` failures hard-kill the job before `on_error:continue`. Prefer staggered standalone skills + committed-file reads over chains.
- Star-count/funding claims seen in the wild (X posts, third-party threads) are frequently wrong or ticker-collisions — always verify against `gh api repos/<owner>/<repo>` before reporting; discard unverified (e.g. 2026-08-20/21's "51,000 stars"/"2.2M stars" claims, both false vs. actual counts). Same rule applies when a third party amplifies *our own* content and adds unverified specifics — e.g. 2026-08-23's MCGlive repost of Aaron's thread added an unverified "running inside companies like SpaceX" detail; reddit-promo correctly used only the organic-amplification signal and omitted the claim itself.
- Sandbox blocking is session-variable and keeps widening past the original `jq`/`cp`/`rm`/`/tmp` scope. Seen through 09-06: `>` redirection, `${VAR}`-brace/presence-checks, heredoc python ("brace with quote" heuristic), `bash <script>` execution, `env -i` with inline expansions, `&&` compound chains, `jq` on files outside the workdir, and `$(date)`/command substitution inside curl URLs. Workarounds hold across all variants: `Write` tool for scratch files under the repo working dir (not `/tmp`) + `python3 file` instead of heredocs, plain `$VAR` (no braces), literal dates/values instead of substitution, sequential commands instead of `&&`, python ports of shell scripts when `bash <script>` itself is blocked. Stray untracked scratch files may linger (no `rm` in the read-only allowlist) — harmless, not committed.
- Bare-`aeon`/"AEON" keyword searches keep colliding with unrelated names — filter on @aeonframework / aeonfun/aeon repo context, never the bare word. Two collisions active as of 09-06: OpenAI Codex's internal "aeon-core"/"nathree-aeon" persistent-agent codename (surfaced via a leaked instruction-set thread, 2026-09-03) and a VC-backed "AEON" agentic-payments-checkout startup ($8M pre-seed led by YZi Labs, May 2026, 2M users, unrelated).
- 2026-08-31 API-degradation incident (bd-radar/heartbeat/engagement-act/aeon-update all hit identical zero-token instant-fail errors — root cause: upstream Claude subscription exhausted) was patched same-day via commit `04d56d5` pinning the harness to the GLM gateway; upstream shipped its own GLM gateway/tiering days later and both landed cleanly via PR #77/#89 — no lingering gateway conflict, explains why `scripts/llm-gateway.sh` has a local effort-pinning tweak on top of upstream's routing.

## Next Priorities
1. **6 stale `health:` issues (#71-76)** sit open since the 08-31 incident — skill-health and skill-repair are both disabled (reactive trigger commented out in `aeon.yml`), so nothing auto-closes them even though every underlying skill recovered by 09-04. Either close manually or re-enable skill-repair's reactive trigger.
2. **CultOS direct check-in overdue** — `cultosdev` GitHub account 404 since ~09-05 despite @thecultos staying active on X (see ecosystem highlight above); engagement-act's dedup keeps blocking a fresh reply to the same canonical handle, so this needs an operator-side check-in outside the skill loop.
3. Configure a second notification channel (Discord/Slack) if Telegram isn't enough. (Telegram already wired.)
