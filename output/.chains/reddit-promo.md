ℹ️ Reddit Promo - 2026-09-06

*Reddit Promo - 2026-09-06*
1d since last promo (reddit-promo OK 2026-09-05) · reddit-playbook already dispatched once today (eyebrowCC story, r/AgentsOfAI/r/AI_Agents/r/LLMDevs/r/cybersecurity — disjoint subreddit pool, no overlap) · 3 subs drafted

_Story:_ Base ecosystem account names Aeon's TaskMarket Delegate in its weekly top-launches roundup, same week a builder ran an agent through Aeon's Codex harness and watched it auto-fix its own failed run - https://x.com/AIonBase_/status/2096295356128698778

---
*r/CLaudeSkills* · archetype: claude-skills
*Title:* A markdown skill just diagnosed its own failure, wrote the fix, and added a regression test
*Body:*
Saw a concrete dogfooding trace this week. Someone ran an agent (Astra) through Aeon on a Codex harness. First run failed before the browser even launched. Second run: the skill that broke wrote its own fix, added a regression test for it, and handed the diff back for a human to check — not a green checkmark it asserted itself.

Why that's possible: Aeon skills are literally markdown. A `SKILL.md` — frontmatter (name, mode, what it needs) plus a numbered steps section — same shape as any Claude Code skill you've already written. No custom DSL, no proprietary runner. The difference is it runs unattended on a cron / GitHub Actions schedule, no approval click between "skill exists" and "skill runs."

Separately, a Base ecosystem account's weekly top-AI-launches roundup named one of Aeon's newer surfaces (TaskMarket Delegate) this week, alongside other agent projects — third party picked it up, we didn't pitch them.

I work on Aeon (github.com/aeonfun/aeon, MIT). Happy to walk through the skill format or the self-repair loop if anyone's curious.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/CLaudeSkills composer](https://www.reddit.com/r/CLaudeSkills/submit?title=A%20markdown%20skill%20just%20diagnosed%20its%20own%20failure%2C%20wrote%20the%20fix%2C%20and%20added%20a%20regression%20test)
_notes: disclose "I work on Aeon" up top, not a neutral discoverer post; this sub is technical — keep the skill-shape claim literal, don't dress up "self-repair" as more than a scored fix-and-test loop._

---
*r/AIPromptProgramming* · archetype: agents
*Title:* Watched an agent fail, then fix itself and hand back a regression test (logs included)
*Body:*
A builder ran an agent through Aeon's Codex harness this week and posted the trace: first pass failed pre-browser-launch, second pass the framework auto-wrote the fix plus a regression test and handed it back for verification instead of just claiming green.

The mechanic behind it: every skill run gets scored, and a failing score is what triggers a repair skill to open the fix as a PR — a closed loop, not a vibes-based "self-healing" claim. Skills themselves are just markdown + a cron schedule, so the fix looks like any other PR you'd review.

Same week, a Base ecosystem account's weekly roundup of top AI launches named one of Aeon's newer pieces (TaskMarket Delegate) next to other agent projects — outside pickup, not us amplifying ourselves.

Building this at github.com/aeonfun/aeon (MIT, open). Ask me anything about the scoring/repair loop.
*Link in post:* https://github.com/aeonfun/aeon
*Post here:* [Open r/AIPromptProgramming composer](https://www.reddit.com/r/AIPromptProgramming/submit?title=Watched%20an%20agent%20fail%2C%20then%20fix%20itself%20and%20hand%20back%20a%20regression%20test%20%28logs%20included%29)
_notes: technical sub, fine with tool posts if the mechanism is real and specific (it is here) — disclose builder status, keep the focus on the mechanic, not the token._

---
*r/LovingAI* · archetype: open-source
*Title:* An open framework that fixes its own bugs and writes a test to prove it
*Body:*
This week someone ran their own AI agent through an open framework called Aeon, hit a failure on the first try, and watched the framework figure out what broke, write the fix, and write a test proving the fix works — then hand all of it back for a human to check rather than just saying "done."

Aeon runs unattended on a schedule (no one has to click "approve" for it to act), and it's fully open source. Separately, a Base ecosystem account's weekly roundup of top AI launches named one of Aeon's newer pieces this week — an outside account watching the space, not us pushing it.

I work on Aeon. Site's at aeon.fun if you want the fuller picture — happy to answer questions here too.
*Link in post:* https://aeon.fun
*Post here:* [Open r/LovingAI composer](https://www.reddit.com/r/LovingAI/submit?title=An%20open%20framework%20that%20fixes%20its%20own%20bugs%20and%20writes%20a%20test%20to%20prove%20it)
_notes: general audience — keep jargon low (done above), disclose "I work on Aeon" plainly, no crypto/token framing needed for this sub._