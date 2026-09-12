#!/usr/bin/env python3
"""Layout QA for the book's figures.

Run after editing any SVG in figures/svg/ and after figures/render.js:

    python3 figures/qc.py

It measures every <text> with real Arial metrics (PIL) and reports the seven
defect classes that have actually shipped in this book at least once:

  1. overflow   text wider than its containing box
  2. gap        two labels on one baseline closer than 6 units
  3. overlap    two labels whose boxes intersect
  4. leading    stacked lines with less than 1.12x their font-size between
                baselines (reads as one smudge at print size)
  5. duplicate  the same string drawn twice at the same spot (invisible
                ghost text; usually a copy-paste leftover)
  6. margin     ink closer than 6 units to the canvas edge (crop clipped it)
  7. tiny       any font-size below MIN_FONT

Thresholds are the ones enforced across all 63 figures, not aspirations.
"""
import glob
import os
import re
import sys

try:
    from PIL import Image, ImageFont
    import numpy as np
except ImportError:  # pragma: no cover
    sys.exit("needs Pillow and numpy:  pip install pillow numpy")

HERE = os.path.dirname(os.path.abspath(__file__))

MIN_FONT = 11.5        # units; 15cm print width => ~6.4pt
MIN_GAP = 6.0          # units between two labels sharing a baseline
MIN_LEADING = 1.12     # x font-size, baseline to baseline
MIN_MARGIN = 6.0       # units of white between ink and canvas edge
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MEASURE_PX = 200       # measure at 200px, then scale

ENTITIES = {
    "&#183;": "\u00b7", "&#8804;": "\u2264", "&#8211;": "\u2013",
    "&#8212;": "\u2014", "&#8594;": "\u2192", "&#8216;": "\u2018",
    "&#8217;": "\u2019", "&#8220;": "\u201c", "&#8221;": "\u201d",
    "&amp;": "&", "&lt;": "<", "&gt;": ">",
}


def _unescape(t):
    for k, v in ENTITIES.items():
        t = t.replace(k, v)
    return t


def _fonts():
    try:
        return (ImageFont.truetype(FONT_REG, MEASURE_PX),
                ImageFont.truetype(FONT_BOLD, MEASURE_PX))
    except OSError:
        sys.exit("Arial not found at %s" % FONT_REG)


REG, BOLD = _fonts()


def text_width(s, fs, bold):
    f = BOLD if bold else REG
    return f.getlength(s) * fs / MEASURE_PX


def parse(path):
    """Return (viewBox, rects, texts) for one SVG."""
    src = open(path).read()
    m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"', src)
    vbox = tuple(float(m.group(i)) for i in (1, 2, 3, 4)) if m else (0, 0, 760, 0)

    rects = []
    for r in re.finditer(r"<rect\s([^>]*?)/?>", src):
        a = r.group(1)

        def g(k, a=a):
            mm = re.search(rf'\b{k}="(-?[\d.]+)"', a)
            return float(mm.group(1)) if mm else None

        if None in (g("x"), g("y"), g("width"), g("height")):
            continue
        rects.append((g("x"), g("y"), g("width"), g("height")))

    texts = []
    for r in re.finditer(r"<text([^>]*)>(.*?)</text>", src, re.S):
        attrs, inner = r.group(1), r.group(2)
        if "transform" in attrs:           # rotated: not measurable this way
            continue
        content = _unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", inner)).strip())
        if not content:
            continue
        fm = re.search(r'font-size="([\d.]+)"', attrs)
        if not fm:
            continue
        fs = float(fm.group(1))
        if fs < 3:                          # deliberate ghost text
            continue
        x = float(re.search(r'\bx="(-?[\d.]+)"', attrs).group(1))
        y = float(re.search(r'\by="(-?[\d.]+)"', attrs).group(1))
        am = re.search(r'text-anchor="(\w+)"', attrs)
        anchor = am.group(1) if am and am.group(1) in ("middle", "end") else "start"
        bold = 'font-weight="bold"' in attrs
        w = text_width(content, fs, bold)
        lo, hi = ((x - w / 2, x + w / 2) if anchor == "middle"
                  else (x - w, x) if anchor == "end" else (x, x + w))
        texts.append(dict(x=x, y=y, fs=fs, t=content, lo=lo, hi=hi, anchor=anchor))
    return vbox, rects, texts


def check_svg(path):
    vbox, rects, texts = parse(path)
    name = os.path.basename(path)[:-4]
    issues = []

    for t in texts:
        if t["fs"] < MIN_FONT:
            issues.append(("tiny", t["fs"], t["t"][:44]))

    for t in texts:
        boxes = [r for r in rects
                 if r[0] <= t["x"] <= r[0] + r[2] and r[1] <= t["y"] <= r[1] + r[3] and r[2] > 10]
        if not boxes:
            continue
        bx = min(boxes, key=lambda r: r[2] * r[3])
        pad = 3
        over = max(bx[0] + pad - t["lo"], t["hi"] - (bx[0] + bx[2] - pad))
        if over > -0.5:
            issues.append(("overflow", round(over, 1), t["t"][:44]))

    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i], texts[j]
            if a["t"] == b["t"] and abs(a["x"] - b["x"]) < 1 and abs(a["y"] - b["y"]) < 1:
                issues.append(("duplicate", 0, a["t"][:44]))
            if abs(a["y"] - b["y"]) > 0.1:
                continue
            gap = max(a["lo"], b["lo"]) - min(a["hi"], b["hi"])
            if 0 <= gap < MIN_GAP:
                issues.append(("gap", round(gap, 1),
                               "%s | %s" % (a["t"][:26], b["t"][:26])))

    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i], texts[j]
            ox = min(a["hi"], b["hi"]) - max(a["lo"], b["lo"])
            oy = ((min(a["y"], b["y"]) + max(a["fs"], b["fs"]) * 0.22)
                  - (max(a["y"], b["y"]) - max(a["fs"], b["fs"]) * 0.80))
            if ox > 1.5 and oy > 1.5:
                issues.append(("overlap", round(ox * oy),
                               "%s X %s" % (a["t"][:26], b["t"][:26])))

    by_y = sorted(texts, key=lambda t: t["y"])
    for i in range(len(by_y)):
        for j in range(i + 1, len(by_y)):
            a, b = by_y[i], by_y[j]
            dy = b["y"] - a["y"]
            if dy <= 0:
                continue
            if dy > 16:
                break
            ox = min(a["hi"], b["hi"]) - max(a["lo"], b["lo"])
            if ox > 2 and dy < max(a["fs"], b["fs"]) * MIN_LEADING:
                issues.append(("leading", round(dy, 1),
                               "%s / %s" % (a["t"][:26], b["t"][:26])))
    return name, issues


def check_png(svg_path, png_path):
    """Ink must neither reach the canvas edge nor leave a transparent band."""
    issues = []
    im = Image.open(png_path)
    if im.mode != "RGBA":
        return [("alpha", 0, "rendered without an alpha channel")]
    if np.asarray(im)[:, :, 3].min() < 255:
        issues.append(("alpha", 0, "PNG has transparent pixels (background rect)"))
    vx, vy, W, H = parse(svg_path)[0]
    g = np.asarray(im.convert("L"))
    mask = g < 250
    cols = np.where(mask.any(axis=0))[0]
    rows = np.where(mask.any(axis=1))[0]
    if not len(cols):
        return [("blank", 0, "no ink at all")]
    sx, sy = W / im.width, H / im.height
    margins = (cols[0] * sx, W - (cols[-1] + 1) * sx,
               rows[0] * sy, H - (rows[-1] + 1) * sy)
    if min(margins) < MIN_MARGIN:
        issues.append(("margin", round(min(margins), 1),
                       "L/R/T/B = %s" % ", ".join(str(round(m, 1)) for m in margins)))
    return issues


def main():
    svg_dir = os.path.join(HERE, "svg")
    files = sorted(glob.glob(os.path.join(svg_dir, "ch*.svg")))
    if not files:
        sys.exit("no SVGs found in %s" % svg_dir)
    total = 0
    for f in files:
        name, issues = check_svg(f)
        png = os.path.join(HERE, name + ".png")
        if os.path.exists(png):
            issues += check_png(f, png)
        if issues:
            total += len(issues)
            print("%s  (%d)" % (name, len(issues)))
            for kind, val, detail in issues[:8]:
                print("    %-9s %8s  %s" % (kind, val, detail))
    if total:
        print("\n%d issue(s) across %d figures" % (total, len(files)))
        return 1
    print("ALL CLEAN - 0 issues across %d figures" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
