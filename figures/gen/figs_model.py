#!/usr/bin/env python3
"""Chapter 8 figures: the two domain-model diagrams.

  8-3  T3  CareLink domain model, first pass (13 concepts, no attributes)
  8-4  T3  the refined model around the resident core

Figure 8-3 has 13 boxes and 13 associations. Hand-placing that many nodes
reliably produces lines that cross each other, lines that run through a box,
and boxes that overlap. So the layout is solved: the nodes are assigned to
distinct slots of an aligned grid, and the assignment is improved by swapping
pairs of slots while a cost function watches crossings, line-through-box and
total line length. The grid is what guarantees the boxes never touch.

Figure 8-4 is laid out deliberately (Person above its four roles, the resident
cluster below), and link-versus-box checks run on it as assertions.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (Fig, INK, GRAY, LINE, BLUE, BLUE_F, TEAL, TEAL_F, GREEN,
                    GREEN_F, RED, RED_F, seg_rect_hit, seg_cross,
                    clip_to_rect)  # noqa: E402

BW, BH = 136, 44
COLS = [22, 208, 394, 580]
ROWS = [58, 162, 266, 370, 474]
SLOTS = [(x, y) for y in ROWS for x in COLS]


NODES = ["Resident", "Address", "Device", "ContactRecord", "FamilyContact",
         "Alert", "Notification", "CareAssignment", "Caregiver", "Supervisor",
         "EscalationPolicy", "EscalationStep", "VisitLog"]

EDGES = [("Resident", "Address"), ("Resident", "Device"),
         ("Resident", "ContactRecord"), ("Resident", "Alert"),
         ("Resident", "CareAssignment"), ("ContactRecord", "FamilyContact"),
         ("CareAssignment", "Caregiver"), ("Alert", "EscalationPolicy"),
         ("Alert", "Notification"), ("EscalationPolicy", "EscalationStep"),
         ("VisitLog", "Resident"), ("VisitLog", "Caregiver"),
         ("Supervisor", "EscalationPolicy")]

ACCENTS = {"CareAssignment": (TEAL, TEAL_F)}
DEFAULT_ACCENT = (BLUE, BLUE_F)

# A line grazing a box by two units reads as a mistake, so require clearance.
CLEARANCE = 6.0


def geometry(pos):
    """Count crossings and line-through-box for one placement."""
    c = {n: (x + BW / 2, y + BH / 2) for n, (x, y) in pos.items()}
    rects = {n: (x, y, BW, BH) for n, (x, y) in pos.items()}
    crossings = through = 0
    for i, (a, b) in enumerate(EDGES):
        p, q = c[a], c[b]
        for n, r in rects.items():
            if n in (a, b):
                continue
            if seg_rect_hit(p, q, r, CLEARANCE):
                through += 1
        for (d, e) in EDGES[i + 1:]:
            if len({a, b, d, e}) < 4:
                continue
            if seg_cross(p, q, c[d], c[e]):
                crossings += 1
    length = sum(((c[a][0] - c[b][0]) ** 2 + (c[a][1] - c[b][1]) ** 2) ** 0.5
                 for a, b in EDGES)
    return crossings, through, length


def score(assign):
    pos = {n: SLOTS[i] for n, i in assign.items()}
    crossings, through, length = geometry(pos)
    return 1000 * crossings + 20000 * through + 0.5 * length


def climb(assign):
    cur, best = dict(assign), score(assign)
    improved = True
    while improved:
        improved = False
        for a in NODES:
            for b in NODES:
                if a >= b:
                    continue
                trial = dict(cur)
                trial[a], trial[b] = trial[b], trial[a]
                v = score(trial)
                if v < best - 1e-9:
                    cur, best, improved = trial, v, True
            for j in range(len(SLOTS)):          # move into an empty slot
                if j in cur.values():
                    continue
                trial = dict(cur)
                trial[a] = j
                v = score(trial)
                if v < best - 1e-9:
                    cur, best, improved = trial, v, True
    return cur, best


def solve():
    """Try each central slot for the hub, then hill-climb from many starts."""
    hub = []
    for ri in (1, 2):
        for ci in (1, 2):
            hub.append(ri * len(COLS) + ci)
    rng = random.Random(20260912)
    best, bestv = None, None
    for h in hub:
        for trial in range(120):
            rest = [j for j in range(len(SLOTS)) if j != h]
            if trial == 0:
                pick = rest[:len(NODES) - 1]     # top-left filling, in order
            else:
                pick = rng.sample(rest, len(NODES) - 1)
            assign = {"Resident": h}
            for n, j in zip([x for x in NODES if x != "Resident"], pick):
                assign[n] = j
            cur, v = climb(assign)
            if bestv is None or v < bestv:
                best, bestv = cur, v
    return best


def fig8_3():
    assign = solve()
    pos = {n: SLOTS[i] for n, i in assign.items()}
    cr, th, ln = geometry(pos)
    print("  8-3 solver: crossings=%d through=%d length=%.0f" % (cr, th, ln))
    assert th == 0, "8-3: a line still runs through a box"
    # The solver may leave the last grid rows unused; put the caption under the
    # real ink instead of under the grid.
    bottom = max(y for x, y in pos.values()) + BH
    cap_y = bottom + 30
    f = Fig(cap_y + 16)
    f.bg()
    f.text(380, 34, "CareLink domain model, first pass: thirteen concepts",
           14, INK, "middle", True)

    rects = {n: (x, y, BW, BH) for n, (x, y) in pos.items()}
    for a, b in EDGES:
        ax, ay = pos[a][0] + BW / 2, pos[a][1] + BH / 2
        bx, by = pos[b][0] + BW / 2, pos[b][1] + BH / 2
        p = clip_to_rect(ax, ay, bx, by, *rects[a], pad=3)
        q = clip_to_rect(bx, by, ax, ay, *rects[b], pad=3)
        f.line(p[0], p[1], q[0], q[1], "#94A3B8", 2.2)
    for n in NODES:
        stroke, fill = ACCENTS.get(n, DEFAULT_ACCENT)
        x, y = pos[n]
        f.rect(x, y, BW, BH, fill, stroke, 2)
        f.text(x + BW / 2, y + BH / 2 + 4, n, 12, INK, "middle", True)

    f.text(380, cap_y,
           "Thirteen concepts and thirteen associations. No attributes inside "
           "any box; multiplicities and end names arrive in Figure 8-4.",
           12, GRAY, "middle", False, True)
    f.write("ch08-fig8-3-domain-model-first-pass")


# ---------------------------------------------------------------- 8-4 -----
B4 = {
    "Person": (295, 56, 170, ["name", "dateOfBirth"]),
    "Resident": (16, 180, 170, ["careLevel", "mode"]),
    "Caregiver": (202, 180, 170, ["certification", "maxWeeklyHours"]),
    "FamilyContact": (388, 180, 170, ["(no attributes)"]),
    "Supervisor": (574, 180, 170, ["(no attributes)"]),
    "Alert": (16, 316, 170, ["raisedAt", "level", "status"]),
    "Address": (202, 316, 170, ["line", "entrance", "floor", "keyBoxCode"]),
    "CareAssignment": (388, 316, 170, ["role", "from \u00b7 to", "weeklyHours"]),
    "ContactRecord": (574, 316, 170, ["priority", "verifiedOn"]),
    "SafetyConfirmation": (16, 450, 170, ["method", "note", "confirmedAt"]),
}


def h4(name):
    return 26 + 15 * len(B4[name][3]) + 8


LINKS4 = [
    ("Alert", "Resident", [(101, 316), (101, 244)]),
    ("Address", "Resident", [(287, 316), (101, 244)]),
    ("CareAssignment", "Resident", [(410, 316), (101, 244)]),
    ("CareAssignment", "Caregiver", [(500, 316), (287, 244)]),
    ("ContactRecord", "FamilyContact", [(659, 316), (473, 214)]),
    ("SafetyConfirmation", "Alert", [(101, 450), (101, 395)]),
]

GENERALISATION = [(101, 180), (287, 180), (473, 180), (659, 180)]

MULT = [(94, 262, "1", "end"), (94, 306, "1..*", "end"),
        (108, 262, "0..*", "start"), (108, 306, "1", "start"),
        (281, 262, "0..*", "end"), (281, 306, "1", "end")]

ENDNAMES = [(255, 276, "assigned resident"), (400, 262, "assigned caregiver")]


def fig8_4():
    f = Fig(560)
    f.bg()
    f.text(380, 34, "The refined model: attributes, multiplicities, named ends",
           14, INK, "middle", True)

    rects = {}
    for n, (x, y, w, attrs) in B4.items():
        hh = h4(n)
        rects[n] = (x, y, w, hh)
        f.rect(x, y, w, hh, "#FFFFFF", BLUE, 2)
        f.rect(x, y, w, 26, BLUE_F, BLUE, 2)
        f.text(x + w / 2, y + 18, n, 11.5, INK, "middle", True)
        if len(attrs) == 1 and attrs[0].startswith("("):
            f.text(x + 12, y + 44, attrs[0], 11.5, GRAY, "start", False, True)
        else:
            for i, a in enumerate(attrs):
                f.text(x + 12, y + 44 + i * 15, a, 11.5, INK)

    for gx, gy in GENERALISATION:
        f.line(gx, gy, 380, 132, BLUE, 2)
    f.el.append('<path d="M380,120 L371,133 L389,133 z" fill="#FFFFFF" '
                'stroke="%s" stroke-width="2"/>' % BLUE)

    for a, b, pts in LINKS4:
        f.poly(pts, "#6B7280", 2.2)

    for x, y, s, anchor in MULT:
        f.text(x, y, s, 11.5, GRAY, anchor)
    for x, y, s in ENDNAMES:
        f.text(x, y, s, 11.5, GRAY, "middle")

    for a, b, pts in LINKS4:
        for n, r in rects.items():
            if n in (a, b):
                continue
            for i in range(len(pts) - 1):
                assert not seg_rect_hit(pts[i], pts[i + 1], r, 2.5), \
                    "8-4: link %s-%s passes through %s" % (a, b, n)

    f.text(380, 542,
           "Person and its four roles; the key-box code on Address, not on "
           "Resident; the hours on the assignment, not on the caregiver.",
           12, GRAY, "middle", False, True)
    f.write("ch08-fig8-4-domain-model-refined")


if __name__ == "__main__":
    fig8_3()
    fig8_4()
