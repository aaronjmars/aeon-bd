ℹ️ Reddit Promo — 09-15

*Reddit Promo — 2026-09-15*
3d since last promo (prior OK: 09-12, Submit Hook skill; 09-13/09-14 both skipped as thin) · 4 subs drafted

_Story:_ 0x Protocol scanned 84k Uniswap v4 hooks and found only 19% safe; Uniswap founder Hayden Adams then dismissed hook-safety complaints as a "skill issue" in a viral tweet, sparking a live 65-reply debate that grassroots builders are already pointing at Aeon's pre-audited hooks marketplace to answer — https://x.com/haydenzadams/status/2099711270115013085

---
*r/Agent_AI* · archetype: agents
*Title:* A Uniswap founder called malicious hook complaints a "skill issue." The data says otherwise.
*Body:*
0x Protocol scanned 84,000 Uniswap v4 hooks this week. Only 19% came back safe (https://x.com/0xProject/status/2099578032960995502 — 608 likes, 82 rt, 71 replies).

A few days later Hayden Adams, Uniswap's founder, posted that hook-safety complaints are basically a "skill issue" (https://x.com/haydenzadams/status/2099711270115013085 — 288 likes, 65 replies, 33k views). That thread is still climbing, and it's turned into a real argument about whether hook risk is a user problem or an ecosystem problem.

I work on Aeon. We built a marketplace for pre-audited v4 hooks (12 hooks live across 7 chains right now) specifically because "just read the code" doesn't scale when 4 out of 5 hooks fail a basic safety check. A couple of builders (not us) are already dropping that stat and our repo into the replies under Hayden's tweet — which is honestly the best kind of validation, unprompted.

Repo: https://github.com/aeonfun/aeon

Happy to answer questions on how the audit pipeline works or why we think "skill issue" undersells the actual attack surface.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/Agent_AI composer](https://www.reddit.com/r/Agent_AI/submit?title=A%20Uniswap%20founder%20called%20malicious%20hook%20complaints%20a%20%22skill%20issue.%22%20The%20data%20says%20otherwise.)
_notes: disclose as builder up top (done above) — r/Agent_AI runs a normal self-promo ratio, this reads as commentary-with-receipts rather than an ad, so it should clear fine._

---
*r/aiecosystem* · archetype: agents
*Title:* Independent research just validated a thesis we've been building on for months
*Body:*
Not our data, not our tweet, but it's the clearest number I've seen on this: 0x Protocol independently audited 84,000 live Uniswap v4 hooks and found 81% fail a basic safety check (https://x.com/0xProject/status/2099578032960995502). That's not a hypothetical attack surface, that's the current state of a major DeFi primitive.

It landed right as Hayden Adams (Uniswap's founder) told hook-safety critics it's a "skill issue" — and that tweet is now a 65-reply debate about who's actually responsible for vetting this stuff (https://x.com/haydenzadams/status/2099711270115013085).

I'm one of the people building Aeon, an agent framework that runs security/audit work unattended on a schedule. We shipped a marketplace for pre-audited v4 hooks off the back of exactly this problem — and a few builders outside our team are already using 0x's numbers to make the case for it in the wild, which is the part I actually care about, not the marketplace itself.

Site: https://aeon.fun

Curious what this sub thinks the actual fix is — better tooling, mandatory audits, or something else. Not claiming we've solved it, just that "skill issue" undersells it.

*Link in post:* https://aeon.fun
*Post here:* [Open r/aiecosystem composer](https://www.reddit.com/r/aiecosystem/submit?title=Independent%20research%20just%20validated%20a%20thesis%20we%27ve%20been%20building%20on%20for%20months)
_notes: r/aiecosystem is discussion-first — lead with the 0x data, keep the product mention secondary, disclose builder status (done)._

---
*r/OpenSourceAI* · archetype: open-source
*Title:* Open sourcing the audit layer that answers "is this Uniswap hook safe" (after seeing 81% of them aren't)
*Body:*
0x Protocol scanned 84k Uniswap v4 hooks this week and only 19% came back safe (https://x.com/0xProject/status/2099578032960995502). A day or two later Uniswap's own founder called hook-safety complaints a "skill issue" (https://x.com/haydenzadams/status/2099711270115013085) — that tweet's sitting at 65 replies and climbing, mostly people disagreeing with him.

I build Aeon, an open-source (AGPL) agent framework. The whole thing is just markdown "skills" that run unattended on GitHub Actions — no approval loop, no server to babysit. One of those skills is a vuln scanner that audits contracts and hooks and opens real PRs when it finds something. We used that same mechanic to build a marketplace of pre-audited v4 hooks so builders don't have to trust a raw contract on faith.

None of this is "trust us" — the repo's public, the runs are public, and now there's independent third-party data (not ours) saying the underlying problem is real and bigger than people assumed.

Repo: https://github.com/aeonfun/aeon

Open to questions on the skill structure or the audit pipeline specifically.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/OpenSourceAI composer](https://www.reddit.com/r/OpenSourceAI/submit?title=Open%20sourcing%20the%20audit%20layer%20that%20answers%20%22is%20this%20Uniswap%20hook%20safe%22%20%28after%20seeing%2081%25%20of%20them%20aren%27t%29)
_notes: OSS crowd wants mechanics not marketing — keep the "how it runs on GH Actions" detail front and center, disclosed as builder._

---
*r/CoolGithubProjects* · archetype: github
*Title:* Aeon - autonomous agent framework running the audit skill behind a pre-audited Uniswap v4 hooks marketplace
*Body:*
What it is: an open-source (AGPL) agent framework — skills are plain markdown, agents run unattended on GitHub Actions on a cron, no approval loop, self-repairing.

Why now: 0x Protocol just published data showing 81% of 84,000 live Uniswap v4 hooks fail a basic safety check (https://x.com/0xProject/status/2099578032960995502), right as Uniswap's founder dismissed the concern as a "skill issue" in a tweet that's now a 65-reply debate (https://x.com/haydenzadams/status/2099711270115013085). One of Aeon's standing skills is a vuln scanner that finds and fixes exploits and opens real PRs on real repos — we used the same pipeline to stand up a marketplace of pre-audited hooks (12 live, 7 chains).

Stack: Claude Code / OpenClaw / Codex-compatible skill harness, GitHub Actions cron + chains, git-backed memory, public run traces.

Repo: https://github.com/aeonfun/aeon

I work on this, happy to answer anything about the skill format or the audit pipeline.

*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CoolGithubProjects composer](https://www.reddit.com/r/CoolGithubProjects/submit?title=Aeon%20-%20autonomous%20agent%20framework%20running%20the%20audit%20skill%20behind%20a%20pre-audited%20Uniswap%20v4%20hooks%20marketplace)
_notes: r/CoolGithubProjects enforces the "Aeon - <one-line desc>" title format strictly (followed above) and wants the repo link to be the actual payload, not an afterthought — disclosed as builder._