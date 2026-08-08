*Reddit Promo — 2026-08-08*

_Story:_ An engineer with no connection to the project (tom_doerr) unprompted-described Aeon as "an autonomous framework that ships features, finds vulns, and deploys apps without approval loops" and linked straight to the repo — 45 likes, today. — https://x.com/tom_doerr/status/2085569978862813264

---
*r/LovingAI* · archetype: open-source
*Title:* We built an AI agent that runs itself — today a stranger explained it better than our docs do
*Body:*
We've been building Aeon, an open-source AI agent that runs on a schedule and just... does its job. No dashboard to babysit, no "approve this action" popup. It reads its own memory, does the task, and reports back.

Today an engineer we've never talked to (tom_doerr on X) described it, unprompted, as a framework that "ships features, finds vulns, and deploys apps without approval loops" — and linked straight to the GitHub repo himself. Nobody asked him to. That's the best writeup we've gotten this month.

Same week, our sister project Miroshark (a swarm-simulation engine) got listed on the x402 agentic marketplace right next to Claude, Tripadvisor, and CoinMarketCap as a paid API endpoint — so this isn't a one-off, it's a pattern of people outside our circle noticing on their own.

If "an AI that runs unattended and doesn't wait for you to click approve" sounds interesting, it's open source (AGPL) and free to run: https://aeon.fun

Happy to answer anything about how it actually works under the hood.
*Link in post:* https://aeon.fun
*Post here:* [Open r/LovingAI composer](https://www.reddit.com/r/LovingAI/submit?title=We%20built%20an%20AI%20agent%20that%20runs%20itself%20%E2%80%94%20today%20a%20stranger%20explained%20it%20better%20than%20our%20docs%20do)
_notes: keep jargon low per sub norms; disclose "I work on Aeon" in the post, not a neutral-discoverer framing — check if the sub requires a self-promo flair before posting._

---
*r/Ollama* · archetype: open-source
*Title:* Self-hosted AI agent that ships its own code — no approval loop, runs on your own GitHub Actions
*Body:*
If you're the type who self-hosts because you want to own the loop end to end, this might be relevant: Aeon is an open-source agent framework where "skills" are just markdown files that run on a cron schedule via GitHub Actions — no vendor dashboard, no hosted approval queue sitting between the agent and the action it wants to take.

What made me post it here: an engineer unconnected to the project (tom_doerr) described it, unprompted, as a framework that "ships features, finds vulns, and deploys apps without approval loops" and linked the repo himself. That's the exact autonomy pitch, coming from someone with nothing to gain by saying it.

It's AGPL, self-repairing (a health loop scores its own runs and files fixes as PRs), and everything it does leaves a public trace in the repo — no black box.

Repo: https://github.com/aeonfun/aeon — happy to dig into the mechanics if anyone's curious.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Ollama composer](https://www.reddit.com/r/Ollama/submit?title=Self-hosted%20AI%20agent%20that%20ships%20its%20own%20code%20%E2%80%94%20no%20approval%20loop%2C%20runs%20on%20your%20own%20GitHub%20Actions)
_notes: self-hosting crowd is skeptical of anything that smells hosted-SaaS — lead with "you run this on your own infra," disclose as builder, watch the sub's self-promo ratio._

---
*r/AskVibecoders* · archetype: vibecoders
*Title:* I vibe-coded an agent that ships its own PRs while I sleep — today a random dev noticed and described it better than I could
*Body:*
Been running Aeon, an agent framework where each "skill" is a markdown file that fires on a schedule and just does the thing — no approval popup, no me clicking "yes proceed." It reads memory, picks a task, ships it, logs what it did.

Funniest part: I didn't post about this today, someone else did. An engineer I've never talked to (tom_doerr) described it on X as shipping features, finding vulns, and deploying apps "without approval loops" and linked the repo himself. Free marketing from a stranger who just liked the mechanic.

If you're into ship-fast setups, it's open source, AGPL, runs on GitHub Actions — clone it, point it at your own repo, watch it go: https://github.com/aeonfun/aeon

Ask me anything, will actually answer.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AskVibecoders composer](https://www.reddit.com/r/AskVibecoders/submit?title=I%20vibe-coded%20an%20agent%20that%20ships%20its%20own%20PRs%20while%20I%20sleep%20%E2%80%94%20today%20a%20random%20dev%20noticed%20and%20described%20it%20better%20than%20I%20could)
_notes: casual first-person tone fits this sub — disclose as the builder up front, keep it light, don't oversell._