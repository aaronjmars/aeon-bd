---
type: Article
---

# idea-forge — 2026-06-24

> weekly collision: this week's zeitgeist × what aeon + miroshark can ship now. 5 wedges, ranked by timing+fit+edge. not a brainstorm dump.

## zeitgeist this week

- **agent payments went incumbent.** Mastercard launched Agent Pay for Machines in early June — joining Google, Visa, Amazon, Coinbase racing to give algorithms a wallet. x402 is past 100M cumulative txns on Base; Stripe, Cloudflare, Nous all wired in. the rails are validated. the question is who builds the demand on top, not whether they exist.
- **the skill supply chain became an attack surface.** a public audit of **22,511 AI coding skills** found vulns lurking in the markdown. NIST stood up an AI Agent Standards Initiative (Feb); Microsoft shipped an OWASP-agentic-10 Governance Toolkit (April). trust is the new wave — and aeon distributes skills as markdown.
- **self-repair went academic + default.** MAS² (self-generative / self-configuring / self-rectifying multi-agent systems) + "self-improving ecosystems are the new standard" in every 2026 framework roundup. the thesis is consensus now. the proof — public traces — is the only edge left.
- **ambient got a name.** Anthropic's **Conway** leaked — an always-on background agent with push notifications + GitHub subscriptions. the category aeon shipped a year ago now has a closed incumbent racing it. closed.
- **prediction markets went AI-native.** Polymarket settled its first on-chain institutional block trade on an AI-compute index (Ornn H100 rental price) on **June 2**, and a live "best AI model end of June" market sits at 96% Anthropic. reflexive markets that price the AI race itself — finally here.
- **social sim proliferated in the lab.** MASim (multilingual), SimWorld, GenSim — academia is crowding miroshark's lane. but they're papers. production, $1, <10min, x402-native is the moat — the mechanic isn't.

---

## 1. skill-attest — the trust layer for the skill supply chain `T5 F4 E5 = 14` · **aeon**

**one-liner:** 22,511 community skills, vulns lurking in the markdown, and you install them by trusting a stranger's repo — audits already failed this industry once; tokenize the scanner and let agents fund the defense instead.

**why now:** the supply-chain attack surface just went public (the 22,511-skill audit), NIST + Microsoft are scrambling governance toolkits, and aeon's own ecosystem is *actively installing third-party skills this week* — lens-scan, sparkleware's four, aeoncity's 72 projects. the trust gap is opening exactly as the install volume spikes. and it's aeon's home turf: vuln-scanner fleets + "audits are one of the worst things that happened to this industry, tokenize the repo, route fees to the finders."

**smallest shippable cut:** a `skill-attest` skill — point it at any aeon skill repo, it scans for the known kill-shots (prompt-injection in fetched-content handling, secret-exfil to external URLs, destructive bash, hidden network calls), emits a signed attestation + a one-line trust badge for the README. v0 is read-only and runs on a public trace, so the audit is itself verifiable. v1 routes a bounty to the scanner via x402/bankr.

**kill-criterion:** ship it, scan the 20 most-installed ecosystem skills, post the findings. if it surfaces zero real issues across 20 community skills, the attack surface is theoretical and the wedge is dead — move on.

**fit:** aeon

---

## 2. x402-skill-meter — pay-per-run skills, inference funded by the fee `T5 F4 E4 = 13` · **aeon**

**one-liner:** the payment rails just went incumbent — Mastercard, Stripe, Google all shipping machine wallets this month — so stop publishing skills for free: meter any aeon skill behind x402 and the inference pays for itself.

**why now:** ads → trading fees, everywhere. agents that pay their own inference via x402/bankr live forever instead of running out of credits — and this is the month the rails stopped being speculative (100M txns, Mastercard M2M, Stripe USDC on Base). bankr + x402 are *already in the aeon stack*. the registry is one primitive away from being a marketplace, and a builder publishing a skill that earns per invocation is the cleanest "agents as companies" demo we have.

**smallest shippable cut:** wrap one high-value skill (deep-research, or a miroshark sim run) in an x402 paywall — first run free, subsequent runs charge a few cents, fee streams to the inference wallet. publish the meter as a reusable skill-template so any builder can monetize their skill in one line. one working pay-per-run skill with a public receipt is the whole pitch.

**kill-criterion:** put it live, price one skill. if nobody pays for a single metered run in two weeks — not even the ecosystem builders already in the TG — then "agents pay for skills" is a thesis without demand. falsified.

**fit:** aeon

---

## 3. compute-price-sim — simulate the AI-native markets that just went live `T5 F4 E4 = 13` · **miroshark**

**one-liner:** Polymarket just listed reflexive markets that price the AI race itself — compute index, model-of-the-month — and the traders bet blind; spin a miroshark swarm on the narrative drift before they size the bet.

**why now:** June 2 was the first on-chain institutional block trade tied to an AI-compute index (Ornn H100), and a live "best model end of June" sits 96% Anthropic. these are *reflexive* markets — the belief moves the outcome — which is exactly miroshark's belief-drift + AMM + director-mode primitive, pointed at a market category that didn't exist a month ago. this is pm-presim from last week, but no longer generic: it's a sim template aimed at the AI-native PMs that just appeared, with director-mode = inject "Opus 4.9 drops" and watch the model-race market reprice.

**smallest shippable cut:** a miroshark sim template seeded with one live AI-native Polymarket question (the model-race market), agents grounded in the actual model-release zeitgeist, AMM trading the outcome, one director-mode branch ("frontier model X ships tomorrow"). output = a belief-drift report + a where-it-lands call, ~$1, <10 min. post it against the live market and let reality grade it.

**kill-criterion:** run it on three resolved AI-native markets. if the sim's pre-resolution call doesn't beat the market's own opening odds on 2 of 3, it's a better deep-research, not a reality engine — bear case confirmed, shelve.

**fit:** miroshark

---

## 4. conway-claim — own the open ambient category before Conway ships `T4 F4 E4 = 12` · **aeon**

**one-liner:** Conway is aeon with the traces cropped out — an always-on background agent, push + GitHub subs, except it's closed and Anthropic-owned; the move is to ship the open public-traces version and claim the category on the day it drops.

**why now:** this supersedes last week's ambient-aeon — back then the category was just "consensus," now it has a named, leaked, dated incumbent. 2026 is the death of the prompt box; OpenAI, Google, and now Anthropic (Conway) have all conceded proactive > active. aeon shipped ambient on GitHub Actions a year ago, and the one thing Conway *structurally cannot do* is show you the run. autonomy big labs can't cross + public-traces-or-it's-useless = the exact two axes Conway loses on.

**smallest shippable cut:** a one-command `ambient-watch` skill — observe a repo / X handle / inbox, intervene before you ask, every run a public verifiable trace. ship it now; hold a tight "Conway with the receipts" post in the chamber for the day Conway goes public. the build is the proof, the post is the timing.

**kill-criterion:** the post is the test. drop the public-traces framing the day Conway ships; if it doesn't travel (no credible builder repost, no "wait, aeon already does this"), the category claim isn't landing and ambient is a label not a wedge.

**fit:** aeon

---

## 5. agent-pay-sim — simulate the machine economy everyone's racing to bank `T4 F4 E3 = 11` · **miroshark**

**one-liner:** five incumbents just launched machine wallets this month and nobody can tell you what an actual agent-to-agent economy does under load — so simulate it: hundreds of agents transacting over x402, price discovery, congestion, who captures the fees.

**why now:** Mastercard / Google / Visa / Amazon / Coinbase are all building M2M rails on the assumption that agents will transact at scale — but "the first rule of the x402 club is not asking who's actually spending." a grounded swarm sim of the agent economy is the honest read nobody's selling: does demand show up, where do fees concentrate, does it congest. miroshark's swarm + simulated-market primitive points straight at it, and it doubles as x402-native marketing for the x402 crowd.

**smallest shippable cut:** a miroshark template — N agents with budgets + goals, an x402-priced service market, run it hour-by-hour, report fee concentration + failure modes. one sim, one chart: "here's what the agent economy looks like under load." good enough to post at the x402 builders.

**kill-criterion:** if the sim just reproduces obvious econ-101 (whoever prices lowest wins, congestion at peak) with no non-trivial finding, it's a toy — kill unless a branch produces something a payments builder didn't already know.

**fit:** miroshark

---

## what i'd build if i could only build one

**skill-attest.** the freshest external signal (a real, citable 22,511-skill audit), the deepest fit (aeon's whole vuln-scanner + "tokenize the defense" thesis), and it serves the north-star directly — the ecosystem is installing community skills *this week* and has no trust layer. audits failed because maintainers can't outspend attackers. so don't audit. tokenize the repo, route the fees, let the agents scan 24/7. ship the receipt.
