#!/usr/bin/env bash
# Pre-fetch GitHub data via a READ-ONLY PAT (GH_READ_PAT), OUTSIDE the sandbox.
# The default GITHUB_TOKEN is integration-scoped to aeon-nur, so cross-repo reads
# (private product repos; forks/issues of aeon + MiroShark) 403/404 from inside
# the skill. This caches them to .xai-cache/*.json (gitignored) so the in-sandbox
# skill reads cached JSON instead of curling with a secret.
#
#   product-pulse -> .xai-cache/private-repos.json    (private product-repo health)
#   bd-radar      -> .xai-cache/bd-radar-github.json  (forks + open issues of aeon + MiroShark)
#
# GH_READ_PAT must be READ-only — used ONLY for reads here, never the
# checkout/commit token (that stays the default GITHUB_TOKEN).
set -euo pipefail

SKILL="${1:-}"
case "$SKILL" in
  product-pulse|bd-radar) ;;
  *) exit 0 ;;
esac

if [ -z "${GH_READ_PAT:-}" ]; then
  echo "prefetch-private-repos: GH_READ_PAT not set, skipping"
  exit 0
fi

mkdir -p .xai-cache

if [ "$SKILL" = "product-pulse" ]; then
  # Private product-repo health. Out-of-scope repos (404) are skipped silently,
  # so this self-heals if the PAT's repo scope changes later.
  CANDIDATES="aaronjmars/aeon-website aaronjmars/aeon-wc aaronjmars/miroshark-website aaronjmars/MiroShark-x402"
  OUT="[]"; N=0
  for r in $CANDIDATES; do
    repo=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r" \
      --jq '{repo:.full_name, private:.private, issues:.open_issues_count, pushed:.pushed_at, default_branch:.default_branch}' 2>/dev/null) || {
      echo "prefetch-private-repos: $r not accessible (out of PAT scope) — skipping"; continue; }
    prs=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/pulls?state=open" --jq 'length' 2>/dev/null || echo "0")
    rel=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/releases/latest" --jq '.tag_name' 2>/dev/null || echo "none")
    row=$(echo "$repo" | jq --argjson prs "${prs:-0}" --arg rel "$rel" '. + {open_prs:$prs, latest_release:$rel}')
    OUT=$(echo "$OUT" | jq --argjson row "$row" '. + [$row]'); N=$((N+1))
  done
  echo "$OUT" > .xai-cache/private-repos.json
  echo "prefetch-private-repos: cached $N private repo(s) -> .xai-cache/private-repos.json"
fi

if [ "$SKILL" = "bd-radar" ]; then
  # Forks + open issues of the two flagship repos — the forking/integrating BD
  # signals that 403 under the default token. GH_READ_PAT reads them (public, in scope).
  REPOS="aaronjmars/aeon aaronjmars/MiroShark"
  OUT='{"forks":{},"issues":{}}'
  for r in $REPOS; do
    key="${r##*/}"
    forks=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/forks?sort=newest&per_page=40" \
      --jq '[.[]|{repo:.full_name, owner:.owner.login, created:.created_at, pushed:.pushed_at, size:.size}]' 2>/dev/null || echo "[]")
    # the issues endpoint also returns PRs — drop those, keep real issues (integration asks)
    issues=$(GH_TOKEN="$GH_READ_PAT" gh api "repos/$r/issues?state=open&per_page=40" \
      --jq '[.[]|select(.pull_request==null)|{n:.number, title:.title, user:.user.login, created:.created_at}]' 2>/dev/null || echo "[]")
    OUT=$(echo "$OUT" | jq --arg k "$key" --argjson f "${forks:-[]}" --argjson i "${issues:-[]}" '.forks[$k]=$f | .issues[$k]=$i')
    echo "prefetch-private-repos: $r forks=$(echo "$forks" | jq 'length') issues=$(echo "$issues" | jq 'length')"
  done
  echo "$OUT" > .xai-cache/bd-radar-github.json
  echo "prefetch-private-repos: cached forks+issues -> .xai-cache/bd-radar-github.json"
fi
