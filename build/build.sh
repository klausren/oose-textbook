#!/bin/zsh
# Build the open edition from manuscript/ Markdown sources.
# Usage: ./build.sh [--en-only] [ch01|all]
#
#   --en-only  build from the derived English edition (build/strip-cjk.py)
#              instead of from manuscript/, so the Chinese term glosses are
#              absent. The derivation is verified before anything is built.
#
# Image paths: chapters reference figures as `images/xxx.png`, relative to
# manuscript/. That one path works for BOTH pandoc (here) and Leanpub, whose
# processors look for images inside manuscript/images/. Do NOT reintroduce
# `../figures/...`: pandoc refuses paths that escape the resource root, and
# Leanpub cannot see outside manuscript/. Keep manuscript/images/ in sync with
# figures/ via ./sync-figures.sh
set -e
PANDOC="/Users/renzheng/.workbuddy/binaries/pandoc/conda_extract/bin/pandoc"
PY="${PY:-/Users/renzheng/.workbuddy/binaries/python/envs/default/bin/python}"
BOOK="$(cd "$(dirname "$0")/.." && pwd)"

EN_ONLY=0
TARGET=""
for arg in "$@"; do
  case "$arg" in
    --en-only) EN_ONLY=1 ;;
    -*) print -u2 "unknown option: $arg"; exit 2 ;;
    *) TARGET="$arg" ;;
  esac
done
TARGET="${TARGET:-all}"

if [ "$EN_ONLY" = 1 ]; then
  "$PY" "$BOOK/build/strip-cjk.py" --check --strict
  "$PY" "$BOOK/build/strip-cjk.py"
  SRC="$BOOK/build/en-only"
  SUFFIX="-en"
else
  SRC="$BOOK/manuscript"
  SUFFIX=""
fi

build_chapter() {
  local src="$1"
  local name="$(basename "$src" .md)"
  # The trailing "## Figure List (authoring aid)" table is for us, not for
  # readers. Strip it before pandoc sees it. Images still resolve because
  # --resource-path below points at manuscript/ explicitly.
  local tmp="$BOOK/build/.$name.clean.md"
  awk '/^## Figure List/{exit} {print}' "$src" > "$tmp"
  "$PANDOC" "$tmp" \
    --resource-path="$SRC:$BOOK/manuscript:$BOOK/figures" \
    -o "$BOOK/build/$name$SUFFIX.docx"
  rm -f "$tmp"
  echo "built: build/$name$SUFFIX.docx"
}

mkdir -p "$BOOK/build"
if [ "$TARGET" = "all" ]; then
  # Every manuscript .md, not just ch*.md: the back matter (glossary,
  # appendix, index) is built the same way and would otherwise be skipped.
  for f in "$SRC"/*.md; do build_chapter "$f"; done
else
  build_chapter "$SRC/$TARGET.md"
fi
