#!/usr/bin/env bash
# Classify OWNED files. Reads .aeon-work/owned.tsv (status<TAB>path).
# Emits .aeon-work/result.tsv: disposition<TAB>status<TAB>path
set -u
UP="aeonfun/aeon"
BASE="95142d19705ca379815e7fc9493a497ee0504e8d"
HEAD="ba01e9f3e4495c8f761ab483000639cc8d5f5221"
WORK=".aeon-work"
: > "$WORK/result.tsv"

fetch() { # path ref outfile
  gh api "repos/$UP/contents/$1?ref=$2" --jq '.content' 2>/dev/null | base64 -d > "$3" 2>/dev/null
}
sh256() { sha256sum "$1" 2>/dev/null | cut -d' ' -f1; }

n=0
while IFS=$'\t' read -r st path; do
  [ -z "$path" ] && continue
  n=$((n+1))
  safe=$(echo "$path" | tr '/' '_')
  bfile="$WORK/base/$safe"
  hfile="$WORK/head/$safe"
  case "$st" in
    added)
      fetch "$path" "$HEAD" "$hfile"
      if [ -e "$path" ]; then
        echo -e "CONFLICT-ADDCOLLIDE\t$st\t$path" >> "$WORK/result.tsv"
      else
        echo -e "CLEAN-ADD\t$st\t$path" >> "$WORK/result.tsv"
      fi
      ;;
    modified|renamed)
      fetch "$path" "$BASE" "$bfile"
      fetch "$path" "$HEAD" "$hfile"
      if [ ! -e "$path" ]; then
        # upstream modified a file we don't have locally (deferred/absent skill)
        echo -e "ABSENT-LOCAL\t$st\t$path" >> "$WORK/result.tsv"
        continue
      fi
      lsha=$(sh256 "$path"); hsha=$(sh256 "$hfile"); bsha=$(sh256 "$bfile")
      if [ "$lsha" = "$hsha" ]; then
        echo -e "SKIP-SYNCED\t$st\t$path" >> "$WORK/result.tsv"
      elif [ "$lsha" = "$bsha" ]; then
        echo -e "CLEAN-UPDATE\t$st\t$path" >> "$WORK/result.tsv"
      else
        # 3-way merge
        cp "$path" "$WORK/local.tmp"
        if git merge-file -p --diff3 "$WORK/local.tmp" "$bfile" "$hfile" > "$WORK/merged/$safe" 2>/dev/null; then
          echo -e "CLEAN-MERGE\t$st\t$path" >> "$WORK/result.tsv"
        else
          echo -e "CONFLICT-3WAY\t$st\t$path" >> "$WORK/result.tsv"
        fi
      fi
      ;;
    removed)
      fetch "$path" "$BASE" "$bfile"
      if [ ! -e "$path" ]; then
        echo -e "SKIP-ALREADYGONE\t$st\t$path" >> "$WORK/result.tsv"
      else
        lsha=$(sh256 "$path"); bsha=$(sh256 "$bfile")
        if [ "$lsha" = "$bsha" ]; then
          echo -e "CLEAN-DELETE\t$st\t$path" >> "$WORK/result.tsv"
        else
          echo -e "CONFLICT-DELETE\t$st\t$path" >> "$WORK/result.tsv"
        fi
      fi
      ;;
  esac
done < "$WORK/owned.tsv"
echo "classified $n files"
