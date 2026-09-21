**aeon-update — 19 commits synced → [PR #106](https://github.com/aaronjmars/aeon-bd/pull/106)**

Upstream `aeonfun/aeon` `95142d1..ba01e9f`. **31 files applied clean, CI fully green** (incl. the eyebrow integrity gate). Baseline advanced.

What landed: the **dev-loop** stack (proof-gated feature→review→repair), a reflected-XSS fix on the dashboard MCP OAuth callback, Riva shadow-mode isolation on the MCP server, an always-on CI Gate. The synced aeon-update skill also self-patches the recurring red-PR bug (prose edits relocating pinned findings) — applied to this run.

**8 need a manual look**, one worth your call:
- **`sc-audit`** — new upstream skill: deep smart-contract audit (Slither + agentic invariant/access-control/oracle pass, Opus-pinned). Deferred (needs an eyebrow scan + glyph to land). **Product-relevant** — this is the same Uniswap-hook-security thread @svector_eth pitched to jessepollak. Worth adopting.
- Rest are fork-narrowed conflicts (README, ci-tests, changelog, vuln-scanner, idea-pipeline) + `create-prove` dev-loop sub-skill. All in the PR body.

One decision: **review + merge #106.** Nothing auto-touched your config.
