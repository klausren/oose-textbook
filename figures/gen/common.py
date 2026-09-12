#!/usr/bin/env python3
"""Shared helpers for the Chapter 8 figure generators.

Visual language is copied from the existing 63 figures so that the book keeps
one voice; the legibility rules (11.5 font floor, 1.12x leading, 3-unit inner
padding inside every rect) are enforced by the assert helpers below, and then
re-checked independently by figures/qc.py.
"""
import html
import os

from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.dirname(HERE)
OUT = os.path.join(FIGDIR, "svg")

W = 760

INK = "#1F2937"
GRAY = "#6B7280"
LINE = "#C9D4E2"
CANVAS = "#FFFFFF"
BLUE = "#2563EB"; BLUE_F = "#DBEAFE"
TEAL = "#0D9488"; TEAL_F = "#CCFBF1"
AMBER = "#D97706"; AMBER_F = "#FEF3C7"
RED = "#DC2626"; RED_F = "#FEE2E2"
GREEN = "#2E7D46"; GREEN_F = "#DCFCE7"
VIOLET = "#6D3FA8"; VIOLET_F = "#EDE7F6"

MIN_FONT = 11.5
MEASURE = 200
_F = {
    False: ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", MEASURE),
    True: ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", MEASURE),
}


def tw(s, size, bold=False):
    """True Arial advance width, in figure units."""
    return _F[bold].getlength(s) * size / MEASURE


def esc(s):
    return html.escape(s, quote=False)


MARKERS = """<defs>{d}</defs>"""


def _marker_defs():
    colors = {"B": BLUE, "G": GRAY, "V": VIOLET, "R": RED, "T": TEAL,
              "K": INK, "A": AMBER, "Gr": GREEN}
    out = []
    for k, c in colors.items():
        out.append(
            '<marker id="arr%s" viewBox="0 0 10 10" refX="8" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>' % (k, c))
    return MARKERS.format(d="".join(out))


class Fig:
    """One SVG figure: background, elements, and layout assertions."""

    def __init__(self, height):
        self.h = height
        self.el = []
        self.rects = []          # (x, y, w, h) for the overflow check
        self.texts = []          # (x, y, size, bold, lo, hi)

    # -- primitives -------------------------------------------------------
    def bg(self):
        self.el.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>'
                       % (W, self.h, CANVAS))

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=2, rx=10, dash=None):
        s = '<rect x="%g" y="%g" width="%g" height="%g"' % (x, y, w, h)
        if rx:
            s += ' rx="%g"' % rx
        s += ' fill="%s"' % fill
        if stroke:
            s += ' stroke="%s" stroke-width="%g"' % (stroke, sw)
        if dash:
            s += ' stroke-dasharray="%s"' % dash
        self.el.append(s + "/>")
        self.rects.append((x, y, w, h))

    def text(self, x, y, s, size=11.5, color=INK, anchor="start",
             bold=False, italic=False):
        assert size >= MIN_FONT, "font-size %.1f below the floor: %r" % (size, s)
        w = tw(s, size, bold)
        lo, hi = ((x - w / 2, x + w / 2) if anchor == "middle"
                  else (x - w, x) if anchor == "end" else (x, x + w))
        self.texts.append((x, y, size, bold, lo, hi, s))
        st = ' font-style="italic"' if italic else ' font-style="normal"'
        wt = ' font-weight="bold"' if bold else ' font-weight="normal"'
        self.el.append(
            '<text x="%g" y="%g" text-anchor="%s" font-size="%g" fill="%s"%s%s>'
            "%s</text>" % (x, y, anchor, size, color, wt, st, esc(s)))

    def line(self, x1, y1, x2, y2, color=LINE, sw=2.4, m=None, dash=None):
        s = ('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g"'
             % (x1, y1, x2, y2, color, sw))
        if dash:
            s += ' stroke-dasharray="%s"' % dash
        if m:
            s += ' marker-end="url(#arr%s)"' % m
        self.el.append(s + "/>")

    def poly(self, pts, color=LINE, sw=2.4, m=None, dash=None, fill="none"):
        d = " ".join("%g,%g" % p for p in pts)
        s = ('<polyline points="%s" fill="%s" stroke="%s" stroke-width="%g"'
             % (d, fill, color, sw))
        if dash:
            s += ' stroke-dasharray="%s"' % dash
        if m:
            s += ' marker-end="url(#arr%s)"' % m
        self.el.append(s + "/>")

    def circle(self, cx, cy, r, fill, stroke=None, sw=2):
        s = '<circle cx="%g" cy="%g" r="%g" fill="%s"' % (cx, cy, r, fill)
        if stroke:
            s += ' stroke="%s" stroke-width="%g"' % (stroke, sw)
        self.el.append(s + "/>")

    def dot(self, cx, cy, r=4.5, fill=INK):
        self.el.append('<circle cx="%g" cy="%g" r="%g" fill="%s"/>'
                       % (cx, cy, r, fill))

    def diamond(self, cx, cy, r=9, fill=INK):
        self.el.append('<path d="M%g,%g L%g,%g L%g,%g L%g,%g z" fill="%s"/>'
                       % (cx, cy - r, cx + r, cy, cx, cy + r, cx - r, cy, fill))

    def tick(self, cx, cy, r=8.5, fill=GREEN):
        """A drawn check mark, never a font glyph."""
        self.circle(cx, cy, r, fill)
        self.el.append('<path d="M%g,%g L%g,%g L%g,%g" fill="none" stroke="#FFFFFF"'
                       ' stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>'
                       % (cx - r * 0.45, cy + r * 0.02,
                          cx - r * 0.12, cy + r * 0.36,
                          cx + r * 0.46, cy - r * 0.38))

    def cross(self, cx, cy, r=8.5, fill=RED):
        self.circle(cx, cy, r, fill)
        self.el.append('<path d="M%g,%g L%g,%g M%g,%g L%g,%g" fill="none"'
                       ' stroke="#FFFFFF" stroke-width="2.1" stroke-linecap="round"/>'
                       % (cx - r * 0.35, cy - r * 0.35, cx + r * 0.35, cy + r * 0.35,
                          cx + r * 0.35, cy - r * 0.35, cx - r * 0.35, cy + r * 0.35))

    # -- layout assertions -------------------------------------------------
    def check(self, name):
        """Reproduce qc.py's own rules locally so failures name the figure."""
        bad = []
        for (x, y, size, bold, lo, hi, s) in self.texts:
            inside = [r for r in self.rects
                      if r[0] <= x <= r[0] + r[2] and r[1] <= y <= r[1] + r[3]
                      and r[2] > 10]
            if not inside:
                continue
            bx = min(inside, key=lambda r: r[2] * r[3])
            over = max(bx[0] + 3 - lo, hi - (bx[0] + bx[2] - 3))
            if over > -0.5:
                bad.append("overflow %.1f  %r" % (over, s))
        for i, a in enumerate(self.texts):
            for b in self.texts[i + 1:]:
                if abs(a[1] - b[1]) > 0.1:
                    continue
                gap = max(a[4], b[4]) - min(a[5], b[5])
                if 0 <= gap < 6:
                    bad.append("gap %.1f  %r | %r" % (gap, a[6], b[6]))
        order = sorted(self.texts, key=lambda t: t[1])
        for i, a in enumerate(order):
            for b in order[i + 1:]:
                dy = b[1] - a[1]
                if dy > 16:
                    break
                if dy <= 0:
                    continue
                ox = min(a[5], b[5]) - max(a[4], b[4])
                if ox > 2 and dy < max(a[2], b[2]) * 1.12:
                    bad.append("leading %.1f  %r / %r" % (dy, a[6], b[6]))
        if bad:
            raise AssertionError("%s: %d layout problem(s):\n  %s"
                                 % (name, len(bad), "\n  ".join(bad)))

    def write(self, name):
        self.check(name)                      # refuse to ship a broken figure
        head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                'font-family="Arial">' % (W, self.h))
        svg = head + _marker_defs() + "".join(self.el) + "</svg>"
        path = os.path.join(OUT, name + ".svg")
        with open(path, "w") as fh:
            fh.write(svg)
        print("wrote %s.svg  (%d elements)" % (name, len(self.el)))


def wrap(s, n):
    """Greedy wrap at n characters. SVG does not wrap, so we do it by hand."""
    out, cur = [], ""
    for word in s.split():
        if cur and len(cur) + 1 + len(word) > n:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


def block(f, x, y, s, n, size, color, lh, bold=False, anchor="middle", italic=False):
    for i, ln in enumerate(wrap(s, n)):
        f.text(x, y + i * lh, ln, size, color, anchor, bold, italic)
    return y + (len(wrap(s, n)) - 1) * lh


def lblock(f, x, y, s, n, size, color, lh, bold=False, italic=False):
    return block(f, x, y, s, n, size, color, lh, bold, "start", italic)


# -- geometry helpers used by the model diagrams ---------------------------

def seg_rect_hit(p, q, r, pad=0.0):
    """Does segment p-q touch rect (x,y,w,h) inflated by pad? Liang-Barsky."""
    x0, y0, x1, y1 = r[0] - pad, r[1] - pad, r[0] + r[2] + pad, r[1] + r[3] + pad
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]),
                   (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0:
                return False
            continue
        t = qq / pp
        if pp < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return False
    return True


def _ccw(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])


def seg_cross(p1, p2, p3, p4):
    d1 = _ccw(p3, p4, p1)
    d2 = _ccw(p3, p4, p2)
    d3 = _ccw(p1, p2, p3)
    d4 = _ccw(p1, p2, p4)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))


def clip_to_rect(cx, cy, tx, ty, x, y, w, h, pad=1.5):
    """Point where the ray from (cx,cy) towards (tx,ty) leaves the rect."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    cand = []
    for bx, sgn in ((x + w + pad, 1), (x - pad, -1)):
        if dx:
            t = (bx - cx) / dx
            yy = cy + t * dy
            if t > 0 and y - pad <= yy <= y + h + pad:
                cand.append((t, bx, yy))
    for by, sgn in ((y + h + pad, 1), (y - pad, -1)):
        if dy:
            t = (by - cy) / dy
            xx = cx + t * dx
            if t > 0 and x - pad <= xx <= x + w + pad:
                cand.append((t, xx, by))
    if not cand:
        return cx, cy
    t, px, py = min(cand)
    return px, py
