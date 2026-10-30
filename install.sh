#!/usr/bin/env sh
# Copies every skill in ./skills into the user's Claude Code skills folder.
set -e
target="${1:-$HOME/.claude/skills}"
src="$(cd "$(dirname "$0")" && pwd)/skills"
mkdir -p "$target"
for d in "$src"/*/; do
  name="$(basename "$d")"
  rm -rf "$target/$name"
  cp -R "$d" "$target/$name"
  echo "installed $name"
done
