#!/usr/bin/env python3
"""Fit each figure's viewBox to its real ink bounding box.

    python3 figures/fitvbox.py            # dry run, prints the plan
    python3 figures/fitvbox.py --apply    # rewrites svg/*.svg (backs up first)

Why: the manuscript places every figure at {width=15cm}, so printed type size is
15cm x font_size / viewBox_width. Dead margin on the canvas therefore costs real
legibility. Measuring the ink from the rendered PNG (not from the source
coordinates, which miss <path> curves and marker tips) and trimming to
ink + PAD gives a free 1.0-1.23x increase in apparent type size.

MIN_W is a floor, not a target: without it a narrow diagram such as the
waterfall would be blown up ~2.9x and print at a size no other figure uses.

Run order after editing any SVG:

    python3 figures/fitvbox.py --apply
    python3 figures/qc.py
    node figures/render.js
    bash build/sync-figures.sh
"""
import glob
import os
import re
import shutil
import statistics
import sys

try:
    from PIL import Image
    import numpy as np
except ImportError:  # pragma: no cover
    sys.exit("needs Pillow and numpy:  pip install pillow numpy")

HERE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(HERE, "svg")
BACKUP = os.path.join(HERE, ".svg-prefit-backup")

PAD = 16        # units of white kept on every side
MIN_W = 620     # never crop below this width (caps the type-size blow-up)
MIN_H = 240
INK = 250       # grayscale threshold: anything darker counts as ink


def main():
    apply = "--apply" in sys.argv
    if apply:
        if os.path.isdir(BACKUP):
            shutil.rmtree(BACKUP)
        shutil.copytree(SVG_DIR, BACKUP)
        print("backup -> %s" % BACKUP)

    plan = []
    for png in sorted(glob.glob(os.path.join(HERE, "ch*.png"))):
        stem = os.path.basename(png)[:-4]
        svg_path = os.path.join(SVG_DIR, stem + ".svg")
        if not os.path.exists(svg_path):
            print("SKIP (no svg): %s" % stem)
            continue
        src = open(svg_path).read()
        m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"', src)
        if not m:
            print("SKIP (no viewBox): %s" % stem)
            continue
        vx, vy, W, H = (float(m.group(i)) for i in (1, 2, 3, 4))

        g = np.asarray(Image.open(png).convert("L"))
        mask = g < INK
        cols = np.where(mask.any(axis=0))[0]
        rows = np.where(mask.any(axis=1))[0]
        if not len(cols):
            print("SKIP (blank): %s" % stem)
            continue
        sx, sy = W / g.shape[1], H / g.shape[0]
        # Ink extents in FIGURE coordinates. The PNG is a rendering of the
        # current viewBox, so the origin has to be added back. Omitting it made
        # the tool non-idempotent: on a figure whose viewBox origin is not
        # (0,0) a second run slid the crop up-left, clipped the right and
        # bottom edges, and qc.py reported margin 0.0 on 63 figures.
        x0, x1 = vx + cols[0] * sx, vx + (cols[-1] + 1) * sx
        y0, y1 = vy + rows[0] * sy, vy + (rows[-1] + 1) * sy

        nW = min(W, max(MIN_W, (x1 - x0) + 2 * PAD))
        nH = min(H, max(MIN_H, (y1 - y0) + 2 * PAD))
        ncx = max(vx, min(vx + W - nW, (x0 + x1) / 2 - nW / 2))
        ncy = max(vy, min(vy + H - nH, (y0 + y1) / 2 - nH / 2))
        ncx, ncy, nW, nH = round(ncx), round(ncy), round(nW), round(nH)
        plan.append((stem, W, H, nW, nH, W / nW))

        if not apply:
            continue
        out = re.sub(r'viewBox="[^"]+"', 'viewBox="%g %g %g %g"' % (ncx, ncy, nW, nH),
                     src, count=1)
        # The white background rect must follow the viewBox, or the PNG gets a
        # transparent band and prints unpredictably. Accept both spellings.
        pats = [r'<rect width="100%" height="100%" fill="#FFFFFF"\s*/>',
                r'<rect x="-?[\d.]+" y="-?[\d.]+" width="%g" height="%g" fill="#FFFFFF"/>' % (W, H)]
        for pat in pats:
            if re.search(pat, out):
                out = re.sub(pat,
                             '<rect x="%g" y="%g" width="%g" height="%g" fill="#FFFFFF"/>'
                             % (ncx, ncy, nW, nH), out, count=1)
                break
        else:
            print("  !! background rect not matched: %s" % stem)
        open(svg_path, "w").write(out)

    if not plan:
        print("nothing to do (no rendered PNGs found in %s)" % HERE)
        return 0

    print("%-46s %10s %10s %6s" % ("figure", "old", "new", "gain"))
    for stem, W, H, nW, nH, gain in plan:
        print("%-46s %10s %10s %6.3f" % (stem, "%gx%g" % (W, H), "%gx%g" % (nW, nH), gain))
    gains = [p[5] for p in plan]
    print("\nfigures: %d   median gain %.3f   max %.3f"
          % (len(plan), statistics.median(gains), max(gains)))
    print("APPLIED" if apply else "DRY RUN (re-run with --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
