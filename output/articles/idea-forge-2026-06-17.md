---
type: Article
---

# idea-forge — 2026-06-17

first run. the weekly forced-collision: this week's zeitgeist × what aeon ⭐ + miroshark 🦈 can ship now. 5 wedges, ranked by timing + fit + edge. not a brainstorm dump — defensible, shippable-now, with a kill-criterion each.

## zeitgeist this week

- **self-evolving agents went from thesis to category — this month.** AgentFactory, Memento-Skills, VenusFactory2, a VentureBeat piece on "agents that rewrite their own skills without retraining." the moat aeon's been claiming is now everyone's claim. when everyone says self-improvement, the moat moves to *proof*.
- **world models are the hottest academic lane — and it's all pixels.** 400-paper surveys, Genie 3, MultiWorld, Waymo. the papers openly admit world models "can't support strategic planning in multi-agent systems" (non-stationary, adaptive, heterogeneous goals). the *social/belief* world model is empty. that's miroshark's literal spec.
- **x402 went institutional.** Linux Foundation took custody (Apr), Foundation now includes Google + Visa, V2 shipped reusable sessions + multi-chain + **automatic service discovery**. the agent-payments rail is real now, not a demo.
- **PM trading agents are live.** Polystrat on Polymarket — 4,200 trades in a month, 37% positive PnL (2-3x the human rate). they trade on current odds, not on how belief *moves*.
- **ambient/proactive is now consensus.** "death of the chatbot," Gartner $14.8B observational-AI market by 2027. aeon shipped proactive-on-cron a year ago. this is a timing window, not a build.
- **state of the house:** miroshark cooking — 1,297★, +40/7d, ~3 from 1,300, PR backlog cleared. aeon flat at 517★. bottleneck per bd-radar is *closing* the warm book, not discovery.

---

## 1. proof of self-repair — the ledger ⭐ · T5 F5 E5 = 15

**every framework now claims self-improvement. only a public repo can prove it. ship the receipt.**

- **why now:** the self-evolving-agent category formed *this month* — and every entrant claims the moat aeon's been claiming for a year. when the claim commoditizes, the differentiator becomes verification. aeon is the only one where every self-repair is already a public git commit. nobody else can produce the receipt.
- **smallest shippable cut:** a `self-repair-ledger` skill that scans aeon's own git history + skill-run state and emits a public, dated ledger — every skill it wrote / reviewed / merged / squash-deleted, the failing run that triggered it, the green run after. one auto-updated page, linkable. v0 this week.
- **kill-criterion:** post it; if nobody clicks or cites it in the self-evolving-agents discourse within 2 weeks, the receipt is vanity, not a wedge. (falsifier = referral traffic + a single external citation.)
- **fit:** aeon.

## 2. counterfactual launch simulator 🦈 · T4 F5 E4 = 13

**the unit of competition is the timing window. so simulate the window before you spend it.**

- **why now:** Aaron's own thesis — figure out the zeitgeist, then ultra-accelerate. miroshark already has director mode + counterfactual branching ("git for strategic decisions"). nobody's pointed it at the one call every builder makes blind: *when and where to launch.*
- **smallest shippable cut:** a miroshark template `launch-window` — feed it a launch (tweet / PH copy / Show HN title) + 2-3 candidate windows, it forks the timeline per window, runs the swarm, returns which travels + why. dogfood on aeon/miroshark's own next launch. ~$1/run, x402-metered.
- **kill-criterion:** run it on 3 *past* launches with known outcomes; if its predicted-best window doesn't beat a coin flip vs what actually traveled, it's not calibrated — retune or kill.
- **fit:** miroshark (dogfooded by this war room).

## 3. miroshark as the social world model 🦈 · T5 F4 E4 = 13

**the world-models wave is all pixels. the missing world model is social — belief, not physics.**

- **why now:** the category is the hottest lane in AI research and the papers themselves admit world models can't do multi-agent strategic planning — adaptive behaviors, heterogeneous goals, partial observations. that's miroshark's spec verbatim. hot category, empty slice.
- **smallest shippable cut:** expose miroshark as an MCP / A2A `world-model` tool — an agent calls `simulate(decision)` and gets a belief-drift trajectory + AMM outcome *before* it acts. ship the MCP server + a one-line "give your agent a world model" README. any aeon / claude-code agent can now plan against a sim.
- **kill-criterion:** if no external agent calls the endpoint within 2 weeks (beyond ours), the "agents want a social world model to plan with" thesis is premature — sims stay a deep-research substitute (the bear case).
- **fit:** miroshark (consumed by aeon agents = both).

## 4. pm-presim — backtest the future 🦈 · T4 F4 E4 = 12

**PM trading agents bet blind. give them a sim of the belief drift before they size the bet.**

- **why now:** Polystrat & co. are live and winning at 2-3x human rate — but they trade on *current* odds, not on how belief will move. miroshark already trades a simulated AMM with belief drift across rounds. plug the two. this is the coordination-market lens made executable, and it meters per-sim over x402.
- **smallest shippable cut:** a miroshark template `pm-presim` — input a live Polymarket question, output the simulated belief-drift trajectory + a confidence band, as JSON a trading agent consumes. v0 reads one market, runs one sim, x402-metered.
- **kill-criterion:** backtest against 5 *resolved* markets; if drift direction doesn't beat the naive "current odds = final odds" baseline, it's not alpha — kill. (resolved markets = free ground truth.)
- **fit:** miroshark.

## 5. ambient aeon — claim "the prompt box is dead" ⭐ · T5 F4 E3 = 12

**2026 made "ambient AI" consensus. aeon shipped it a year ago — on public traces. claim the category, don't reinvent it.**

- **why now:** observational/ambient agents is *the* narrative now — Gartner $14.8B by 2027, everyone announcing background agents. aeon already runs unattended on cron and acts before asked. this is a timing/positioning wedge, not an infra build.
- **smallest shippable cut:** an `ambient-watch` skill that observes one surface (a repo, an org, a token, a market) continuously and only pings when something crosses a threshold — the literal "AI that acts before you think" demo — plus a Show HN / thread timed to the ambient wave, in Aaron's voice, public trace as proof.
- **kill-criterion:** post the positioning; if it doesn't beat a baseline aeon post on engagement (vibes = the only unfakeable metric), the category-claim doesn't land — the wedge is the product, not the narrative.
- **fit:** aeon.

---

**if i could only build one:** #1, proof of self-repair. the whole category just turned into "everyone claims self-improvement" overnight — and aeon is the single entrant that can drop a public, verifiable receipt nobody can fake. cheapest build, highest edge, rides a window that opened this week.

## sources
- self-evolving frameworks: [VentureBeat — agents rewrite their own skills](https://venturebeat.com/orchestration/new-framework-lets-ai-agents-rewrite-their-own-skills-without-retraining-the), [AgentFactory (arXiv)](https://arxiv.org/pdf/2603.18000)
- world models: [Agentic World Modeling survey (arXiv 2604.22748)](https://arxiv.org/abs/2604.22748), [MultiWorld (arXiv)](https://arxiv.org/html/2604.18564v1), [MetaMind (arXiv 2603.00808)](https://arxiv.org/pdf/2603.00808)
- x402: [The Block — what is x402](https://www.theblock.co/learn/391983/what-is-coinbases-x402-protocol), [Autheo — x402 + gasless stablecoins 2026](https://www.autheo.com/blog/x402-gasless-stablecoins-ai-agent-micropayments-batch-settlement-2026)
- PM agents: [Coindesk — AI agents rewriting PM trading](https://www.coindesk.com/tech/2026/03/15/ai-agents-are-quietly-rewriting-prediction-market-trading)
- ambient AI: [BuildBetter — observational AI 2026](https://blog.buildbetter.ai/ai-agents-that-watch-you-work-how-observational-ai-learns-in-2026/), [ProAgentBench (arXiv 2602.04482)](https://arxiv.org/pdf/2602.04482)
