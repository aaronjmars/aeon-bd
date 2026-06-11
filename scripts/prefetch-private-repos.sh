#!/usr/bin/env bash
# Pre-fetch health for PRIVATE product repos OUTSIDE the sandbox, using a
# read-only GitHub PAT (GH_READ_PAT). The default GITHUB_TOKEN only covers
# this repo, so private MiroShark/Aeon repos 404 from inside the skill.
# This caches their health to .xai-cache/private-repos.json (gitignored) so the
# in-sandbox skill reads cached JSON instead of curling with a secret.
#
# GH_READ_PAT must be READ-only — it is used ONLY for reads here and is never
# the checkout/commit token (that stays the default GITHUB_TOKEN).
set -euo pipefail

SKILL="${1:-}"

# Only product-pulse consumes this cache today.
case "$SKILL" in
  product-pulse) ;;
  *) exit 0 ;;
esac

if [ -z "${GH_READ_PAT:-}" ]; then
  echo "prefetch-private-repos: GH_READ_PAT not set, skipping"
  exit 0
fi

mkdir -p .xai-cache

# Candidate private product repos. Any the PAT can't see (404) are skipped
# silently, so this self-heals if the PAT's repo scope changes later.
CANDIDATES="aaronjmars/aeon-website aaronjmars/aeon-wc aaronjmars/miroshark-website aaronjmars/MiroShark-x402"

OUT="[]"
ACCESSIBLE=0
for r in $CANDIDATES; do
  repo=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r" \
    --jq '{repo:.full_name, private:.private, issues:.open_issues_count, pushed:.pushed_at, default_branch:.default_branch}' 2>/dev/null) || {
    echo "prefetch-private-repos: $r not accessible (out of PAT scope) — skipping"
    continue
  }
  prs=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/pulls?state=open" --jq 'length' 2>/dev/null || echo "0")
  rel=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/releases/latest" --jq '.tag_name' 2>/dev/null || echo "none")
  row=$(echo "$repo" | jq --argjson prs "${prs:-0}" --arg rel "$rel" '. + {open_prs:$prs, latest_release:$rel}')
  OUT=$(echo "$OUT" | jq --argjson row "$row" '. + [$row]')
  ACCESSIBLE=$((ACCESSIBLE + 1))
done

echo "$OUT" > .xai-cache/private-repos.json
echo "prefetch-private-repos: cached $ACCESSIBLE private repo(s) -> .xai-cache/private-repos.json"
