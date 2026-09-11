#!/bin/zsh
# Build the open edition from manuscript/ Markdown sources.
# Usage: ./build.sh [ch01|all]
#
# Image paths: chapters reference figures as `images/xxx.png`, relative to
# manuscript/. That one path works for BOTH pandoc (here) and Leanpub, whose
# processors look for images inside manuscript/images/. Do NOT reintroduce
# `../figures/...`: pandoc refuses paths that escape the resource root, and
# Leanpub cannot see outside manuscript/. Keep manuscript/images/ in sync with
# figures/ via ./sync-figures.sh
set -e
PANDOC="/Users/renzheng/.workbuddy/binaries/pandoc/conda_extract/bin/pandoc"
BOOK="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

build_chapter() {
  local src="$1"
  local name="$(basename "$src" .md)"
  # The trailing "## Figure List (authoring aid)" table is for us, not for
  # readers. Strip it before pandoc sees it. Images still resolve because
  # --resource-path below points at manuscript/ explicitly.
  local tmp="$BOOK/build/.$name.clean.md"
  awk '/^## Figure List/{exit} {print}' "$src" > "$tmp"
  "$PANDOC" "$tmp" \
    --resource-path="$BOOK/manuscript:$BOOK/figures" \
    -o "$BOOK/build/$name.docx"
  rm -f "$tmp"
  echo "built: build/$name.docx"
}

mkdir -p "$BOOK/build"
if [ "$TARGET" = "all" ]; then
  for f in "$BOOK"/manuscript/ch*.md; do build_chapter "$f"; done
else
  build_chapter "$BOOK/manuscript/$TARGET.md"
fi
