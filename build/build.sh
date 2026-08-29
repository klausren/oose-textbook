#!/bin/zsh
# Build the open edition from manuscript/ Markdown sources.
# Usage: ./build.sh [ch01|all]
set -e
PANDOC="/Users/renzheng/.workbuddy/binaries/pandoc/conda_extract/bin/pandoc"
BOOK="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

build_chapter() {
  local src="$1"
  local name="$(basename "$src" .md)"
  "$PANDOC" "$src" \
    --resource-path="$BOOK:$BOOK/figures" \
    -o "$BOOK/build/$name.docx"
  echo "built: build/$name.docx"
}

mkdir -p "$BOOK/build"
if [ "$TARGET" = "all" ]; then
  for f in "$BOOK"/manuscript/ch*.md; do build_chapter "$f"; done
else
  build_chapter "$BOOK/manuscript/$TARGET.md"
fi
