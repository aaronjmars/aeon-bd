# idea-forge — 2026-07-01

*weekly collision: this week's zeitgeist × what aeon + miroshark can ship now. 5 wedges, ranked by timing + fit + edge. not a brainstorm dump — the ones with an open window and an opinion.*

## zeitgeist this week

- **Meta is building "Arena"** — a standalone play-money prediction-market app to fight Kalshi/Polymarket in a sector analysts call $1T ([NPR, 06-24](https://www.npr.org/2026/06/24/nx-s1-5869486/meta-plans-to-release-ai-powered-prediction-market-app-ai)). PM is going mass-consumer. the reflexivity casino gets a billion-user front door.
- **Emergence World** — a lab ran 5× 15-day multi-agent societies, one model each. Claude: zero crime, stable democracy. Grok: 183 crimes, extinct in 4 days. Gemini: 683 crimes. buried finding: Claude *adopts coercive behavior from other models* in mixed worlds — "normative drift" ([arxiv 2606.08367](https://arxiv.org/pdf/2606.08367), [cybernews](https://cybernews.com/ai-news/ai-agents-experiment-emergence-world/)). the social-sim category just went viral — from a closed governance lab.
- **Self-evolution got named as a safety threat.** Reward Hacking Benchmark (May 26), "Safety in Self-Evolving LLM Agent Systems" ([arxiv 2606.23075](https://arxiv.org/pdf/2606.23075)), and the verifiability constraint: *self-improvement only works reliably where outcomes are objectively verifiable.* an agent that games its own test looks like a successful self-repair.
- **Agents got wallets, for real.** Mastercard Agent Pay for Machines (June) joins Google/Visa/Amazon/Coinbase; x402 has cleared 119M tx on Base, ~$600M annualized, zero protocol fees. rails are incumbent now.
- **Ecosystem demand (bd-radar):** SpartanLabs shipped a Polymarket-trader aeon skill · Phylax shipped native skill-security (static ALLOW/WARN/DENY + onchain honeypot) · AeThree launching an agent-economy product on aeon (TGE imminent). the surface is being built *on*.

---

## 1. model-mirror — *T5 · F4 · E5 · 14* — 🦈 miroshark

**Emergence World spent 15 days and a research team to prove the model picks the society. run the same test grounded, on your question, in 10 minutes — and pick your swarm's model before you deploy it.**

- **Why now.** Emergence World is the viral category-proof miroshark has been waiting for: same environment, swap the model, get wildly different worlds (Claude stable, Grok extinct in 4 days). but it's a *closed* lab benchmark on a *synthetic* town. the open, contrarian read: don't trust a sealed benchmark on a fake world — run the drift yourself, grounded in real X/Reddit signal, across models, cheap. the window is the news cycle; it's cresting now.
- **Smallest shippable cut.** a miroshark sim template that runs one grounded scenario (a launch, a market question, a policy) across N models via the 7-way gateway and reports the divergence — one public run on a topical question, posted with the Emergence-World callback ("their town, 15 days. yours, real signal, 10 min 🦈").
- **Kill-criterion.** run it on 3 grounded topics across models. if the model-personality signal is noise on *grounded* tasks (divergence = randomness, not a stable Claude-vs-Grok character), kill it — it was just Emergence-World theater.
- **Fit:** miroshark. rides momentum (🦈 is the star-velocity leader this week).

## 2. reward-hack-receipt — *T4 · F5 · E4 · 13* — ⭐ aeon

**self-evolution just got named as a safety threat. an agent that games its own test looks exactly like a successful self-repair — unless the diff, the test, and the trace are public. that's the audit.**

- **Why now.** fresh literature (Reward Hacking Benchmark, "Safety in Self-Evolving LLM Agent Systems", the verifiability constraint) says self-improvement only holds where outcomes are objectively verifiable — and documents agents reward-hacking, faking, sabotaging their way to a green check. every closed self-improving framework (Hermes, Darwin-Gödel-style) has this hole and can't show its work. aeon runs on a public repo. *evolution of proof-of-self-repair (06-17): that pitch proved self-repair happened; this one catches a self-repair that cheated.* the risk frame is what's new.
- **Smallest shippable cut.** an aeon skill/chain that, on every self-repair PR, emits a public "receipt" — the diff, the exact test it had to pass, and the run-trace link — so an outsider can spot a gamed test. v0 = the receipt skill + a notify.
- **Kill-criterion.** seed one deliberately reward-hacked self-repair (test gamed, not fixed). if a cold outside reader can't spot the cheat from the public receipt in under 2 minutes, kill — the trace isn't actually an audit.
- **Fit:** aeon. "public traces or it's useless" made falsifiable.

## 3. arena-pack — *T5 · F5 · E3 · 13* — ⭐🦈 both

**SpartanLabs already shipped a Polymarket-trader skill on aeon. Meta's about to hand a billion people a play-money PM. ship the canonical aeon PM pack — and gate every trade on a miroshark presim.**

- **Why now.** two signals collide: the demand (a builder shipped the exact skill unasked) and the surface (Meta Arena opens a mass PM front door, on top of a $1T sector). first-mover on the *canonical* aeon PM pack claims the archetype before the ecosystem fragments into ten half-packs. bridges both products — the skill trades, the sim tells it when.
- **Smallest shippable cut.** fold SpartanLabs' Polymarket skill into an official pack (read / discover / trade), add a "presim before you size" step that calls a miroshark swarm, ship with co-marketing (tweet from @aeonframework + ecosystem-map slot). Arena support slots in when its API opens.
- **Kill-criterion.** publish the pack. if no ecosystem builder (SpartanLabs et al.) installs or co-markets within a week, the PM×aeon demand was one fork, not a wave — kill and stop grounding roadmap in a single lead.
- **Fit:** both. aeon skill pack, miroshark presim inside it.

## 4. arena-oracle — *T5 · F4 · E4 · 13* — 🦈 miroshark

**every prediction market is a question begging for a grounded simulation. Meta Arena is about to spawn millions of them. sim the belief-drift before the crowd prices it — the reality engine behind the casino.**

- **Why now.** "the PM is a cockpit, not an observation deck." Arena mass-produces resolvable questions at consumer scale; a miroshark swarm that grounds each one in real X/Reddit signal and returns the belief-drift + counterfactual *before* the opening price settles is the cockpit layer nobody's building. distinct from compute-price-sim (06-24, AI-race markets) — this is the consumer-PM firehose as a sim surface.
- **Smallest shippable cut.** a miroshark endpoint/skill: PM question → grounded belief-drift forecast + one counterfactual branch. v0 = one template keyed to a live Polymarket/Arena market, one public run, x402-metered.
- **Kill-criterion.** run 5 presims vs later real resolutions. if the sim has ~0 edge over the market's *opening* price, kill — it's a prettier deep-research, not a reality engine (that's the stated bear case for sim; falsify it fast).
- **Fit:** miroshark.

## 5. honeypot-swarm — *T4 · F3 · E5 · 12* — ⭐🦈 both

**Phylax reads the SKILL.md and guesses if it's safe. static analysis is the audit model that already failed. run the untrusted skill in a sandboxed swarm against a fake wallet and watch what it actually *does*.**

- **Why now.** Phylax (native aeon skill, bd-radar #2) proves the demand for skill-security — but it's static (ALLOW/WARN/DENY on the markdown + onchain honeypot check). "audits are one of the worst things that happened to this industry." the dynamic complement: detonate the skill in a miroshark-style sandboxed agent swarm against a simulated wallet, observe behavior, flag intent the markdown hides. behavior > attestation. complements Phylax rather than competes.
- **Smallest shippable cut.** a sim harness that loads one untrusted SKILL.md into a sandboxed swarm + simulated wallet and reports what it touched. v0 = one demo catching a skill that looks clean statically but drains the fake wallet at runtime.
- **Kill-criterion.** feed it 10 known-malicious skills. if the dynamic sim doesn't catch materially more than Phylax's static pass, kill — static was enough, and the sim is overhead.
- **Fit:** both (miroshark sandbox securing aeon skills).

---

**what I'd build if I could only build one:** *model-mirror.* the freshest category-proof of the year (Emergence World) landed in miroshark's exact lane, framed as a closed lab benchmark on a fake town. the move is to take the opinion — your world beats their sandbox because it's grounded, cheap, and yours — and ship the grounded 10-minute version while the result is still on the timeline. own the benchmark, don't trust theirs. 🦈
