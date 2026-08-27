#!/usr/bin/env bash
set -uo pipefail
REPOS="aeonfun/aeon aaronjmars/aeon-agent aaronjmars/miroshark-aeon MiroShark/MiroShark"
for repo in $REPOS; do
  slug=$(echo "$repo" | tr '/' '-')
  gh api "repos/$repo/forks?sort=newest&per_page=40" > "/tmp/bd-forks-$slug.json" 2>/dev/null
  if [ ! -s "/tmp/bd-forks-$slug.json" ]; then echo '[]' > "/tmp/bd-forks-$slug.json"; fi
  gh api "repos/$repo/issues?state=open&per_page=40" > "/tmp/bd-issues-$slug.json" 2>/dev/null
  if [ ! -s "/tmp/bd-issues-$slug.json" ]; then echo '[]' > "/tmp/bd-issues-$slug.json"; fi
  echo "done: $repo"
done
