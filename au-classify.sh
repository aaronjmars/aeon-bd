#!/usr/bin/env bash
# Classify each changed file: OPERATOR / CLEAN-ADD / SKIP / CLEAN-UPDATE / CLEAN-MERGE / CONFLICT / CLEAN-DELETE
BASE=3b4c5a3ff1d9846530e02ed5e6796a4a409d2674
HEAD=bf33365164c5a8b50d49a0ed64a45521dbe96771

is_operator() {
  case "$1" in
    aeon.yml|STRATEGY.md|.mcp.json|aeon.db|skills.lock|eyebrowlock.json) return 0;;
    soul/*|memory/*|output/*|.env*|catalog/*.json|apps/dashboard/outputs/*) return 0;;
    .claude/skills/aeon/*) return 1;;   # exception -> OWNED
    .claude/*) return 0;;
  esac
  return 1
}

gblob() { git rev-parse "$1:$2" 2>/dev/null; }   # $1=ref $2=path -> blob sha or empty
lblob() { [ -f "$2" ] && git hash-object "$2" 2>/dev/null; }  # local blob sha

while IFS=$'\t' read -r st f; do
  [ -z "$f" ] && continue
  if is_operator "$f"; then
    printf 'OPERATOR\t%s\t%s\n' "$st" "$f"
    continue
  fi
  bsha=$(gblob "$BASE" "$f")
  hsha=$(gblob "$HEAD" "$f")
  lsha=$(lblob x "$f")
  case "$st" in
    A)
      if [ -z "$lsha" ]; then printf 'CLEAN-ADD\t%s\t%s\n' "$st" "$f"
      else printf 'CONFLICT-addcollision\t%s\t%s\n' "$st" "$f"; fi
      ;;
    M)
      if [ -z "$lsha" ]; then printf 'ABSENT-LOCAL\t%s\t%s\n' "$st" "$f"
      elif [ "$lsha" = "$hsha" ]; then printf 'SKIP-synced\t%s\t%s\n' "$st" "$f"
      elif [ "$lsha" = "$bsha" ]; then printf 'CLEAN-UPDATE\t%s\t%s\n' "$st" "$f"
      else printf 'THREEWAY\t%s\t%s\n' "$st" "$f"; fi
      ;;
    D)
      if [ -z "$lsha" ]; then printf 'SKIP-alreadygone\t%s\t%s\n' "$st" "$f"
      elif [ "$lsha" = "$bsha" ]; then printf 'CLEAN-DELETE\t%s\t%s\n' "$st" "$f"
      else printf 'CONFLICT-delete\t%s\t%s\n' "$st" "$f"; fi
      ;;
    R*)
      printf 'RENAME\t%s\t%s\n' "$st" "$f"
      ;;
    *)
      printf 'UNKNOWN\t%s\t%s\n' "$st" "$f"
      ;;
  esac
done < <(git diff --name-status "$BASE" "$HEAD")
