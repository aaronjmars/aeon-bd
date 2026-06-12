*Agent Buzz — 2026-06-12*
all sources failed — no buzz today.

xAI x_search unreachable (curl auth-POST blocked in sandbox, WebFetch 405), and plain web search only surfaces blog roundups, not live tweets w/ engagement. signal scoring needs the metrics, so nothing to score. not fabricating it.

fix: wire agent-buzz into `scripts/prefetch-xai.sh` so the X data lands in `.xai-cache/` before the run, same as product-pulse.
