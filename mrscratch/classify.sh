#!/usr/bin/env bash
# Classify OWNED files for aeon-update 3-way sync.
BASE=b1d907976ee1d2939b4b545ee4aab46b9fed06a9
HEAD=b7a909aa412d8e654df15417fcff0682dac39682
UP=aeonfun/aeon

blob() { git cat-file -p "$1:$2" 2>/dev/null; }         # $1=ref $2=path
exists_ref() { git cat-file -e "$1:$2" 2>/dev/null; }   # returns 0 if blob exists
h() { sha256sum | cut -d' ' -f1; }

# read "status<TAB>filename" lines on stdin
while IFS=$'\t' read -r status path; do
  [ -z "$path" ] && continue
  case "$path" in
    aeon.yml|STRATEGY.md|.mcp.json|aeon.db|skills.lock|eyebrowlock.json) echo "OPERATOR	$status	$path"; continue;;
    soul/*|memory/*|output/*|catalog/*.json|apps/dashboard/outputs/*) echo "OPERATOR	$status	$path"; continue;;
    .claude/skills/aeon/*) : ;;  # OWNED exception, fall through
    .claude/*) echo "OPERATOR	$status	$path"; continue;;
  esac

  hh=$(blob "$HEAD" "$path" | h)
  hb=$(blob "$BASE" "$path" | h)
  if [ -f "$path" ]; then hl=$(h < "$path"); else hl="ABSENT"; fi

  case "$status" in
    added)
      if [ ! -e "$path" ]; then echo "CLEAN-ADD	$status	$path"; else echo "CONFLICT	$status	$path	collision-local-present"; fi
      ;;
    removed)
      if [ "$hl" = "ABSENT" ]; then echo "SKIP-gone	$status	$path";
      elif [ "$hl" = "$hb" ]; then echo "CLEAN-DELETE	$status	$path";
      else echo "CONFLICT	$status	$path	local-differs-from-baseline"; fi
      ;;
    modified)
      if [ "$hl" = "$hh" ]; then echo "SKIP-synced	$status	$path";
      elif [ "$hl" = "$hb" ]; then echo "CLEAN-UPDATE	$status	$path";
      else echo "THREEWAY	$status	$path"; fi
      ;;
    *) echo "UNKNOWN	$status	$path";;
  esac
done
