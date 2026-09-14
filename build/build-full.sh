#!/bin/zsh
# Build the WHOLE book as one file, in Book.txt order.
#
# build.sh produces one docx per manuscript file, which is what a chapter
# review wants. This script exists for the other use: reading the book
# straight through. It concatenates every enabled line of Book.txt into a
# single Markdown file, then hands it to pandoc once.
#
# Usage: ./build-full.sh [--en-only] [--pdf]
#
#   --en-only  derive the English edition first (build/strip-cjk.py) and build
#              from that instead of from manuscript/. The manuscript keeps its
#              Chinese term glosses as the source of record; this flag produces
#              the gloss-free book that ships. It runs `--check --strict` first
#              and refuses to build if the derivation is not clean.
#   --pdf      also emit a PDF, via headless LibreOffice.
#
# The order comes from Book.txt, never from a glob -- a glob would put the
# appendix before the chapters it collects, and would quietly disagree with
# what Leanpub actually ships.
#
# Image paths stay `images/xxx.png` (relative to manuscript/), same as
# build.sh -- --resource-path resolves them. Do not rewrite them to
# ../figures/: pandoc refuses paths that escape the resource root. In
# --en-only mode the resource path carries both directories, because the
# derived edition holds text only and no images/ of its own.
set -e
PANDOC="/Users/renzheng/.workbuddy/binaries/pandoc/conda_extract/bin/pandoc"
SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
PY="${PY:-/Users/renzheng/.workbuddy/binaries/python/envs/default/bin/python}"
BOOK="$(cd "$(dirname "$0")/.." && pwd)"

EN_ONLY=0
PDF=0
for arg in "$@"; do
  case "$arg" in
    --en-only) EN_ONLY=1 ;;
    --pdf)     PDF=1 ;;
    *) print -u2 "unknown argument: $arg (expected --en-only and/or --pdf)"; exit 2 ;;
  esac
done

if [ "$EN_ONLY" = 1 ]; then
  # A derived edition is verified before it is built, not after.
  "$PY" "$BOOK/build/strip-cjk.py" --check --strict
  "$PY" "$BOOK/build/strip-cjk.py"
  SRC="$BOOK/build/en-only"
  SUFFIX="-en"
else
  SRC="$BOOK/manuscript"
  SUFFIX=""
fi

OUT="$BOOK/build/oose-textbook-full$SUFFIX"
TMP="$BOOK/build/.full$SUFFIX.clean.md"

# 1) An explicit title page. pandoc's --metadata title only fills a header,
#    and this file is opened on its own, so the title has to be in the body.
{
  print '# Object-Oriented Software Engineering'
  print ''
  print '*A Project-Driven Introduction with Embedded AI Practice*'
  print ''
  print 'Ren Zheng'
  print ''
} > "$TMP"

# 2) Contents, assembled from the first heading of each file. Do NOT use
#    pandoc's --toc here: for docx it emits an unpopulated Word TOC field,
#    which LibreOffice renders as the words "Table of Contents" followed by
#    nothing -- worse than no contents page at all. Take the titles from the
#    sources instead, so this page cannot drift from the book.
{
  print '---'
  print ''
  print '## Contents'
  print ''
} >> "$TMP"
while IFS= read -r line; do
  line="${line%%#*}"
  line="$(print -r -- "$line" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
  [ -z "$line" ] && continue
  title="$(head -1 "$SRC/$line" | sed 's/^# //')"
  print -- "- $title" >> "$TMP"
done < "$SRC/Book.txt"
print '' >> "$TMP"

# 3) Every enabled line of Book.txt, in order. `#` is a comment; blank lines
#    are separators. A page break goes between files so chapters do not run
#    into one another.
first=1
while IFS= read -r line; do
  line="${line%%#*}"
  line="$(print -r -- "$line" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
  [ -z "$line" ] && continue
  src="$SRC/$line"
  if [ ! -f "$src" ]; then
    print -u2 "missing (is it still commented out?): $line"
    exit 1
  fi
  if [ "$first" = 0 ]; then
    # Raw OpenXML page break; pandoc passes it through verbatim for docx.
    {
      print '```{=openxml}'
      print '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
      print '```'
      print ''
    } >> "$TMP"
  fi
  first=0
  # Drop the authoring-aid figure table at the end of a chapter: it is a
  # build-time checklist, not something a reader should see.
  awk '/^## Figure List/{exit} {print}' "$src" >> "$TMP"
  print '' >> "$TMP"
  print "  + $line"
done < "$SRC/Book.txt"

# 4) One pandoc run.
"$PANDOC" "$TMP" \
  --resource-path="$SRC:$BOOK/manuscript:$BOOK/figures" \
  -o "$OUT.docx"
echo "built: build/$(basename "$OUT").docx ($(du -h "$OUT.docx" | cut -f1))"

# 5) Optional PDF for handing to someone who does not want a docx. LibreOffice
#    is used rather than pandoc's LaTeX writer because the bilingual edition's
#    glossary has a Chinese column that needs a CJK font at the rasterisation
#    stage; keeping one converter for both editions means the two PDFs lay out
#    the same way.
if [ "$PDF" = 1 ]; then
  "$SOFFICE" -env:UserInstallation=file:///tmp/lo_fullbook \
    --headless --norestore --convert-to pdf --outdir "$BOOK/build" "$OUT.docx" \
    >/dev/null 2>&1
  echo "built: build/$(basename "$OUT").pdf ($(du -h "$OUT.pdf" | cut -f1))"
fi

rm -f "$TMP"
