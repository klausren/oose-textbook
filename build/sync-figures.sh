#!/bin/zsh
# Sync rendered figures from figures/ into manuscript/images/.
#
# Why this exists: figures/ is the OPEN, CC BY 4.0 asset (teachers may reuse
# these files, and they are the marketing asset). manuscript/images/ is what
# Leanpub is allowed to read. Both must hold the same PNGs, and the chapter
# sources reference them as `images/xxx.png`.
#
# Run this after any change in figures/ (i.e. after figures/render.js).
set -e
BOOK="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$BOOK/manuscript/images"
cp "$BOOK"/figures/*.png "$BOOK/manuscript/images/"

count=$(ls -1 "$BOOK"/manuscript/images/*.png 2>/dev/null | wc -l | tr -d ' ')
echo "synced $count PNG(s) -> manuscript/images/"
