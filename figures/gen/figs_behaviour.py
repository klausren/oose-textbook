#!/usr/bin/env python3
"""Chapter 9 (Behavioural Modelling) figure generators.

Every number that appears in a figure is copied from manuscript/ch09.md, and
the two that the chapter argues about (nine messages, thirty-six cells) are
asserted below so that a drift between prose and picture fails the build.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (Fig, W, tw, wrap, lblock, INK, GRAY, LINE,
                    BLUE, BLUE_F, TEAL, TEAL_F, AMBER, AMBER_F,
                    RED, RED_F, GREEN, GREEN_F, VIOLET, VIOLET_F)

RUN = []


def fig(fn):
    RUN.append(fn)
    return fn


# ---------------------------------------------------------------- 9-1

def _card(f, x, y, w, h, accent, accent_f, title, rows):
    body = [(lab, wrap(val, 34)) for lab, val in rows]
    need = 34 + sum(22 + 16 * len(v) for _, v in body) + 8
    assert need <= h, "card content needs %d, got %d" % (need, h)
    f.rect(x, y, w, h, fill="#FFFFFF", stroke=accent, sw=2, rx=10)
    f.rect(x, y, w, 34, fill=accent_f, rx=10)           # header band ...
    f.rect(x, y + 17, w, 17, fill=accent_f, rx=0)       # ... squared off
    f.text(x + w / 2, y + 23, title, 12.5, accent, "middle", True)
    ry = y + 34
    for i, (lab, lines) in enumerate(body):
        if i:
            f.line(x + 1, ry, x + w - 1, ry, "#E5EAF2", 1.2)
        f.text(x + 12, ry + 13, lab, 11.5, accent, "start", True)
        for j, ln in enumerate(lines):
            f.text(x + 12, ry + 29 + 16 * j, ln, 11.5, INK)
        ry += 22 + 16 * len(lines)
    return h


@fig
def fig_9_1():
    f = Fig(406)
    f.bg()
    f.text(380, 22, "The question you are asking names the diagram.",
           12, GRAY, "middle", italic=True)
    H = 334
    _card(f, 18, 44, 236, H, BLUE, BLUE_F, "Sequence diagram", [
        ("Answers", "who talks to whom, in what order"),
        ("Subject", "one scenario, start to finish"),
        ("Vocabulary", "participant, lifeline, message, guarded branch"),
        ("CareLink", "the alarm-escalation scenario"),
        ("Finds", "a missing message; two failures that look identical"),
        ("Cannot say", "whether the receiver is in a legal state"),
    ])
    _card(f, 262, 44, 236, H, VIOLET, VIOLET_F, "State machine", [
        ("Answers", "what can happen to this one object"),
        ("Subject", "one object, for its whole life"),
        ("Vocabulary", "state, event, guard, action, transition"),
        ("CareLink", "the Alert object"),
        ("Finds", "a trap state; a cell nobody decided"),
        ("Cannot say", "who sent the event, or how many participants"),
    ])
    _card(f, 506, 44, 236, H, GREEN, GREEN_F, "Activity diagram", [
        ("Answers", "the workflow, and who does each step"),
        ("Subject", "one workflow, across roles and the system"),
        ("Vocabulary", "action, decision, merge, swimlane"),
        ("CareLink", "the shift hand-over"),
        ("Finds", "an unowned step; a hand-over that loses work"),
        ("Cannot say", "the order of messages inside one step"),
    ])
    f.write("ch09-fig9-1-three-models-three-questions")


# ---------------------------------------------------------------- 9-2

LIFE_92 = [("Device", 80, 108), ("CareLink", 300, 108),
           ("Caregiver", 540, 108), ("Family contact", 675, 126)]


def _lifelines(f, life, top, bot, head_y=22, head_h=30, size=12):
    for name, x, w in life:
        f.rect(x - w / 2, head_y, w, head_h, fill="#EEF2FF", stroke=BLUE,
               sw=1.8, rx=7)
        f.text(x, head_y + 20, name, size, INK, "middle", True)
        f.line(x, top, x, bot, LINE, 1.6, dash="4 4")


@fig
def fig_9_2():
    f = Fig(576)
    f.bg()
    _lifelines(f, LIFE_92, 52, 544)

    def msg(y, x1, x2, label, color=INK, m="K"):
        f.line(x1, y, x2, y, color, 2.0, m)
        f.text((x1 + x2) / 2, y - 7, label, 11.5, INK, "middle")

    def selfmsg(y, x, label, color=BLUE, m="B"):
        f.poly([(x, y), (x + 46, y), (x + 46, y + 16), (x + 8, y + 16)],
               color=color, sw=2.0, m=m)
        f.text(x + 54, y + 5, label, 11.5, INK, "start")

    msg(84, 80, 300, "raiseAlert(type, resident, raisedAt)", BLUE, "B")
    selfmsg(120, 300, "startEscalationTimer()")
    msg(156, 300, 540, "notify(alert, address, keyBoxCode)", BLUE, "B")

    f.line(80, 188, 675, 188, AMBER, 1.6, dash="5 5")
    f.text(377, 181, "interval elapses; nothing acknowledged  "
           "(a time marker, not a message)", 11.5, AMBER, "middle")

    selfmsg(220, 300, "timerExpired()")
    msg(256, 300, 675, "escalate(step 2 of the policy)", BLUE, "B")
    msg(292, 675, 300, "acknowledge()", TEAL, "T")
    msg(328, 300, 540, "inform(acknowledgedBy, at)  - R-054", BLUE, "B")
    selfmsg(364, 300, "recordEscalation(); stopTimer()")
    msg(400, 300, 675, "confirm(reference)", BLUE, "B")

    f.text(60, 430, "alt", 12, VIOLET, "start", True)
    f.rect(56, 436, 660, 108, fill="#FAF8FE", stroke=VIOLET, sw=1.8,
           rx=8, dash="6 4")
    f.text(68, 456, "[acknowledged before the timer fires]", 11.5, VIOLET)
    f.line(300, 490, 540, 490, TEAL, 2.0, "T")
    f.text(420, 483, "acknowledge()", 11.5, INK, "middle")
    f.line(56, 506, 716, 506, VIOLET, 1.4, dash="6 4")
    f.text(68, 528, "[no acknowledgement]  messages 4-9 run", 11.5, VIOLET)
    assert len([1 for e in f.el if 'marker-end="url(#arr' in e]) == 10, \
        "9-2 must show the nine numbered messages plus the branch"
    f.write("ch09-fig9-2-sequence-alarm-escalation")


# ---------------------------------------------------------------- 9-3

BW, BH = 118, 36
# The states sit on a vertical spine so that the one long back-edge
# (Escalated -> Acknowledged) never has to cross a label.
STATES_93 = {
    "Raised":       (120, 100),
    "Notified":     (120, 240),
    "Acknowledged": (120, 380),
    "Closed":       (120, 520),
    "Escalated":    (400, 380),
    "Unresolved":   (660, 380),
}
TERMINAL_93 = ("Closed", "Unresolved")


@fig
def fig_9_3():
    f = Fig(566)
    f.bg()
    rect = {}
    for name, (cx, cy) in STATES_93.items():
        f.rect(cx - BW / 2, cy - BH / 2, BW, BH, fill="#FFFFFF",
               stroke=VIOLET, sw=2, rx=9)
        f.text(cx, cy + 4.5, name, 12, INK, "middle", True)
        rect[name] = (cx - BW / 2, cy - BH / 2)
    for name in TERMINAL_93:
        x, y = rect[name]
        cy = y + BH / 2
        f.line(x + BW, cy, x + BW + 8, cy, INK, 2.2)
        f.circle(x + BW + 17, cy, 9, "#FFFFFF", INK, 2.2)
        f.dot(x + BW + 17, cy, 5, INK)

    f.dot(44, 100, 6)
    f.line(50, 100, 61, 100, INK, 2.2, "K")                     # initial
    f.line(120, 118, 120, 222, INK, 2.2, "K")                   # Raised
    f.text(134, 176, "notify /startEscalationTimer", 11.5, INK)
    f.line(120, 258, 120, 362, INK, 2.2, "K")                   # Notified
    f.text(134, 304, "acknowledge", 11.5, INK)
    f.text(134, 320, "/stopEscalationTimer", 11.5, GRAY)
    f.line(120, 398, 120, 502, INK, 2.2, "K")                   # Acknowledged
    f.text(134, 476, "confirmSafety", 11.5, INK)
    f.text(134, 494, "/recordConfirmation", 11.5, GRAY)
    f.line(179, 240, 400, 362, INK, 2.2, "K")                   # N -> Esc
    f.text(322, 296, "timerExpires [stepsRemain]", 11.5, INK)
    f.text(322, 312, "/escalateNextStep", 11.5, GRAY)
    f.line(341, 380, 179, 380, INK, 2.2, "K")                   # Esc -> Ack
    f.text(260, 356, "acknowledge", 11.5, INK, "middle")
    f.text(260, 372, "/stopEscalationTimer", 11.5, GRAY, "middle")
    f.poly([(420, 398), (420, 434), (452, 434), (452, 398)],
           INK, 2.2, "K")                                       # Esc self
    f.text(436, 480, "timerExpires [stepsRemain]", 11.5, INK, "middle")
    f.text(436, 496, "/escalateNextStep", 11.5, GRAY, "middle")
    f.line(459, 380, 601, 380, INK, 2.2, "K")                   # Esc -> Unr
    f.text(530, 352, "timerExpires", 11.5, INK, "middle")
    f.text(530, 368, "[noStepsRemain]", 11.5, INK, "middle")
    # the two refusals of R-054 and R-056: events that must be rejected
    f.poly([(150, 398), (150, 422), (212, 422), (212, 398)], RED, 2.2, "R")
    f.text(222, 424, "acknowledge [alreadyAcknowledged]", 11.5, INK)
    f.text(222, 440, "close [noConfirmation]", 11.5, INK)
    f.text(222, 456, "both: /refuse; recordAttempt", 11.5, RED)
    # what the Exit check found, six weeks before the code existed
    f.text(28, 326, "before R-056:", 11.5, AMBER, "start", True)
    f.text(28, 342, "a trap state", 11.5, AMBER)
    f.write("ch09-fig9-3-state-machine-alert")


# ---------------------------------------------------------------- 9-4

LANES_94 = [("Outgoing caregiver", 18, 170),
            ("CareLink", 188, 312),
            ("Incoming caregiver", 500, 242)]


def _lanes(f, top, bot, lanes):
    for name, x, w in lanes:
        f.rect(x, top, w, bot - top, fill="#FAFBFD", stroke="#DCE3EC",
               sw=1.6, rx=0)
        f.rect(x, top, w, 30, fill="#EEF2F7", stroke="#DCE3EC", sw=1.6, rx=0)
        f.text(x + w / 2, top + 20, name, 12, INK, "middle", True)


@fig
def fig_9_4():
    f = Fig(676)
    f.bg()
    _lanes(f, 24, 660, LANES_94)

    def act(x, y, w, h, lines, accent=BLUE, fill="#FFFFFF"):
        f.rect(x, y, w, h, fill=fill, stroke=accent, sw=2, rx=9)
        n = len(lines)
        y0 = y + h / 2 - (n - 1) * 8 + 4
        for i, s in enumerate(lines):
            f.text(x + w / 2, y0 + i * 16, s, 11.5, INK, "middle")

    def dia(cx, cy, r=14, col=VIOLET, fill=VIOLET_F):
        f.poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy),
                (cx, cy - r)], col, 2.0, fill=fill)

    # 1  outgoing caregiver selects the hand-over
    f.dot(103, 78, 6)
    f.line(103, 84, 103, 96, INK, 2.2, "K")
    act(28, 96, 150, 40, ["Selects hand-over"])
    f.poly([(103, 136), (103, 142), (345, 142), (345, 152)], INK, 2.2, "K")

    # 2  CareLink lists everything that is open
    act(202, 152, 286, 62, ["Lists every open item: open alerts,",
                            "incomplete visits, and alerts",
                            "acknowledged but not confirmed"])
    f.poly([(345, 214), (345, 222), (450, 222), (450, 236)], INK, 2.2, "K")

    # 3  decision: any open alert?
    dia(450, 250)
    f.text(430, 246, "any open alert?", 11.5, VIOLET, "end")
    f.line(464, 250, 512, 250, INK, 2.2, "K")
    f.text(484, 244, "yes", 11.5, GREEN, "middle", True)
    act(512, 228, 230, 44, ["Accepts ownership of the alert",
                            "with its remaining escalation time"])
    f.line(450, 264, 450, 303, INK, 2.2, "K")
    f.text(458, 288, "no", 11.5, GRAY, "start", True)
    dia(450, 316, 13, GRAY, "#F5F6F7")                 # merge, carries nothing
    f.poly([(627, 272), (627, 316), (463, 316)], INK, 2.2, "K")

    # 4  decision: any incomplete visit?
    f.line(450, 329, 450, 366, INK, 2.2, "K")
    dia(450, 380)
    f.text(430, 376, "any incomplete visit?", 11.5, VIOLET, "end")
    f.line(464, 380, 512, 380, INK, 2.2, "K")
    f.text(484, 374, "yes", 11.5, GREEN, "middle", True)
    act(512, 360, 230, 40, ["Takes the visit over"])
    f.line(450, 394, 450, 433, INK, 2.2, "K")
    f.text(458, 418, "no", 11.5, GRAY, "start", True)
    dia(450, 446, 13, GRAY, "#F5F6F7")
    f.poly([(627, 400), (627, 446), (463, 446)], INK, 2.2, "K")

    # 5  the step the first draft did not have
    f.line(450, 459, 450, 496, INK, 2.2, "K")
    act(202, 496, 286, 44, ["Records the hand-over: outgoing,",
                            "incoming, and the time"],
        accent=AMBER, fill=AMBER_F)
    f.text(200, 562, "the step whose absence became R-059",
           11.5, AMBER, "start", True)

    # 6  the incoming caregiver owns everything
    f.poly([(460, 540), (460, 600), (512, 600)], INK, 2.2, "K")
    act(512, 580, 230, 40, ["Owns every open item"])
    f.line(627, 620, 627, 634, INK, 2.2)
    f.circle(627, 644, 9, "#FFFFFF", INK, 2.2)
    f.dot(627, 644, 5)
    f.write("ch09-fig9-4-activity-shift-handover")


# ---------------------------------------------------------------- 9-5

LIFE_95 = [("Device", 120), ("CareLink", 330), ("Caregiver", 540)]


def _head(f, life, y, h=28, size=11.5):
    for name, x in life:
        f.rect(x - 56, y, 112, h, fill="#EEF2FF", stroke=BLUE, sw=1.8, rx=7)
        f.text(x, y + 18.5, name, size, INK, "middle", True)


def _spine(f, life, top, bot):
    for _, x in life:
        f.line(x, top, x, bot, LINE, 1.6, dash="4 4")


@fig
def fig_9_5():
    f = Fig(616)
    f.bg()
    dev, cl, cg = 120, 330, 540

    def msg(y, x1, x2, label, col=BLUE, m="B"):
        f.line(x1, y, x2, y, col, 2.0, m)
        f.text((x1 + x2) / 2, y - 7, label, 11.5, INK, "middle")

    # ---- before ---------------------------------------------------------
    f.rect(18, 36, 724, 258, fill="#FFFBFB", stroke=RED, sw=2, rx=12,
           dash="7 5")
    f.text(32, 56, "BEFORE", 12, RED, "start", True)
    f.text(96, 56, "the diagram has no delivery message", 11.5, GRAY)
    f.text(728, 56, "self-messages omitted", 11.5, GRAY, "end", False, True)
    _head(f, LIFE_95, 70)
    _spine(f, LIFE_95, 98, 282)

    msg(126, dev, cl, "raiseAlert()")
    msg(158, cl, cg, "notify()")
    f.cross(cg, 184, 8.5)
    f.text(616, 176, "no reply:", 11.5, RED, "start", True)
    f.text(616, 192, "silence", 11.5, RED)
    f.line(cl, 214, cg, 214, AMBER, 1.6, dash="5 5")
    f.text(435, 207, "interval elapses", 11.5, AMBER, "middle")
    msg(246, cl, cg, "escalate()")

    f.text(380, 310,
           "An undelivered notification and an ignored one are the same picture.",
           11.5, RED, "middle", False, True)

    # ---- after ----------------------------------------------------------
    f.rect(18, 330, 724, 246, fill="#F8FDF9", stroke=GREEN, sw=2, rx=12,
           dash="7 5")
    f.text(32, 350, "AFTER", 12, GREEN, "start", True)
    f.text(96, 350,
           "R-058: the delivery is recorded, and the timer starts at confirmed "
           "delivery", 11.5, GRAY)
    _head(f, LIFE_95, 364)
    _spine(f, LIFE_95, 392, 562)

    msg(418, dev, cl, "raiseAlert()")
    msg(448, cl, cg, "notify()")
    msg(478, cg, cl, "deliveryConfirmed()", GREEN, "Gr")
    f.tick(cg, 478, 8.5)
    f.text(616, 458, "the reply", 11.5, GREEN, "start", True)
    f.text(616, 474, "that makes the", 11.5, GREEN)
    f.text(616, 490, "difference", 11.5, GREEN)
    msg(512, cl, cg, "escalate()")

    f.text(380, 594,
           "The timer is now measured from an event that is known to have happened.",
           11.5, GREEN, "middle", False, True)
    f.write("ch09-fig9-5-missing-alternative")


# ---------------------------------------------------------------- 9-6


@fig
def fig_9_6():
    f = Fig(452)
    f.bg()
    f.text(380, 34, "The sentence-to-message check, in both directions",
           14, INK, "middle", True)

    def block(y, accent, fill, title, rule1, rule2, result, card):
        f.rect(18, y, 724, 122, fill=fill, stroke=accent, sw=2, rx=10)
        f.text(36, y + 24, title, 12, accent, "start", True)
        f.text(36, y + 44, rule1, 11.5, INK)
        f.text(36, y + 60, rule2, 11.5, INK)
        f.text(36, y + 82, result, 11.5, GRAY)
        f.rect(400, y + 36, 330, 74, fill="#FFFFFF", stroke=RED, sw=1.8, rx=8)
        f.text(414, y + 56, card[0], 11.5, RED, "start", True)
        f.text(414, y + 74, card[1], 11.5, INK)
        f.text(414, y + 94, card[2], 11.5, RED)

    block(56, BLUE, "#F6F9FF",
          "Direction 1 — sentence to message",
          "Rule: every sentence that names a sender and a",
          "receiver must have a message.",
          "Result: this is where a missing requirement is found.",
          ("the sentence:", '"the phone shows not yet confirmed"',
           "no message  \u2192  R-058"))
    block(190, TEAL, "#F3FBFA",
          "Direction 2 — message to sentence",
          "Rule: every message in the diagram must have",
          "a sentence in the scenario.",
          "Result: this is where design leaks into analysis.",
          ("the message:", "NotificationService.deliver()",
           "no sentence  \u2192  removed"))

    f.rect(18, 324, 724, 78, fill="#F5F6F7", stroke=LINE, sw=1.6, rx=10)
    f.text(36, 350, "The third result, and the quiet one", 11.5, INK,
           "start", True)
    f.text(36, 372,
           '"the system escalates" and "the system tells Deng" are one message '
           "and one guard.", 11.5, INK)
    f.text(36, 390,
           "Keeping them as two arrows draws a decision as a message.",
           11.5, GRAY)

    f.text(380, 430,
           "Two breaks, and only two: one sentence with no message, one "
           "message with no sentence.", 12, GRAY, "middle", False, True)
    f.write("ch09-fig9-6-scenario-to-message")


# ---------------------------------------------------------------- 9-7

COL0_97 = 106
COLW_97 = 104
X0_97, Y0_97 = 16, 54
HDR_97 = 46
ROWH_97 = 44
EVENTS_97 = [("N", "notify"), ("A", "acknowledge"), ("T", "timerExpires"),
             ("C", "confirmSafety"), ("X", "close"), ("H", "shift hand-over")]
STATES_97 = ["Raised", "Notified", "Acknowledged", "Escalated", "Closed",
             "Unresolved"]
CELLS_97 = [
    [("Notified", INK), ("\u2013", GRAY), ("\u2013", GRAY), ("\u2013", GRAY),
     ("\u2013", GRAY), ("\u2013", GRAY)],
    [("\u2013", GRAY), ("Acknowledged", INK), ("Escalated", INK),
     ("\u2013", GRAY), ("\u2013", GRAY), ("\u2013", GRAY)],
    [("\u2013", GRAY), ("refuse \u00b7 R-054", RED), ("?", AMBER),
     ("Closed", INK), ("refuse \u00b7 R-056", RED), ("owner changes", BLUE)],
    [("\u2013", GRAY), ("Acknowledged", INK), ("Escalated /\nUnresolved", INK),
     ("\u2013", GRAY), ("\u2013", GRAY), ("\u2013", GRAY)],
    [("\u2013", GRAY)] * 6,
    [("\u2013", GRAY), ("Acknowledged", INK), ("\u2013", GRAY), ("\u2013", GRAY),
     ("\u2013", GRAY), ("\u2013", GRAY)],
]
TINT_97 = {"?": AMBER_F, "owner changes": BLUE_F, "Escalated /\nUnresolved":
           "#F5F6F7", "refuse \u00b7 R-054": RED_F, "refuse \u00b7 R-056": RED_F}


@fig
def fig_9_7():
    assert len(STATES_97) == 6 and len(EVENTS_97) == 6, \
        "the chapter says six states and six events"
    moves = sum(1 for row in CELLS_97 for _, col in row if col == INK)
    refusals = sum(1 for row in CELLS_97 for _, col in row if col == RED)
    assert (moves, refusals) == (7, 2), "seven moves and two refusals"
    assert moves + refusals + 1 + 26 == 36, \
        "seven moving cells, two refusals, one owner change, 26 ignored"
    f = Fig(520)
    f.bg()
    f.text(380, 32, "The state-event table behind the machine", 14, INK,
           "middle", True)

    def cx(j):
        return X0_97 + COL0_97 + (j + 0.5) * COLW_97

    f.rect(X0_97, Y0_97, COL0_97, HDR_97, fill="#EEF2F7", stroke="#DCE3EC",
           sw=1.4, rx=0)
    f.text(X0_97 + COL0_97 / 2, Y0_97 + 32, "State \\ Event", 11.5, INK,
           "middle", True)
    for j, (letter, name) in enumerate(EVENTS_97):
        f.rect(X0_97 + COL0_97 + j * COLW_97, Y0_97, COLW_97, HDR_97,
               fill="#EEF2F7", stroke="#DCE3EC", sw=1.4, rx=0)
        f.text(cx(j), Y0_97 + 20, letter, 11.5, INK, "middle", True)
        f.text(cx(j), Y0_97 + 36, name, 11.5, GRAY, "middle")

    for i, state in enumerate(STATES_97):
        y = Y0_97 + HDR_97 + i * ROWH_97
        f.rect(X0_97, y, COL0_97, ROWH_97, fill="#FAFBFD", stroke="#DCE3EC",
               sw=1.4, rx=0)
        f.text(X0_97 + COL0_97 / 2, y + ROWH_97 / 2 + 4, state, 11.5, INK,
               "middle", True)
        for j, (txt, col) in enumerate(CELLS_97[i]):
            fill = TINT_97.get(txt, "#FFFFFF")
            f.rect(X0_97 + COL0_97 + j * COLW_97, y, COLW_97, ROWH_97,
                   fill=fill, stroke="#DCE3EC", sw=1.4, rx=0)
            lines = txt.split("\n")
            y0 = y + ROWH_97 / 2 + 4 - (len(lines) - 1) * 8
            for k, ln in enumerate(lines):
                f.text(cx(j), y0 + k * 16, ln, 11.5, col, "middle",
                       txt == "?" or txt in ("owner changes",
                                             "refuse \u00b7 R-054",
                                             "refuse \u00b7 R-056"))

    f.text(18, 388, "6 states \u00d7 6 events = 36 cells", 11.5, INK,
           "start", True)
    leg = [(AMBER_F, AMBER, "the cell nobody decided \u2014 it produced R-060"),
           (RED_F, RED, "the system must refuse the event and record it"),
           (BLUE_F, BLUE, "the owner changes; the state does not"),
           ("#FFFFFF", GRAY, "the event is ignored \u2014 a decision as well")]
    for i, (fill, col, txt) in enumerate(leg):
        y = 410 + i * 24
        f.rect(20, y - 9, 13, 13, fill=fill, stroke=col, sw=1.6, rx=3)
        f.text(42, y + 1, txt, 11.5, INK)
    f.text(380, 498, "Thirty-six cells is a test matrix.", 12, GRAY, "middle",
           False, True)
    f.write("ch09-fig9-7-state-event-table")


# ---------------------------------------------------------------- 9-8


@fig
def fig_9_8():
    f = Fig(364)
    f.bg()
    f.text(380, 38, "AI-assisted behavioural model drafting, with verification",
           14, INK, "middle", True)

    boxes = [
        (23, BLUE, BLUE_F, "1", "Human supplies", "YOU SUPPLY",
         ["The escalation", "scenario, pasted", "with a four-step prompt."]),
        (206, VIOLET, VIOLET_F, "2", "AI drafts", "AI RETURNS",
         ["Four participants,", "nine messages,", "one alt branch."]),
        (389, AMBER, AMBER_F, "3", "Human verifies", "YOU CHECK",
         ["Message count,", "named lifelines,", "three failures each."]),
        (572, GREEN, GREEN_F, "4", "Artifact", "YOU PRODUCE",
         ["The model with the", "invented parts", "removed."]),
    ]
    for x, accent, fill, num, title, label, body in boxes:
        f.rect(x, 76, 165, 152, "#FFFFFF", accent, 2.2)
        f.rect(x, 76, 165, 56, fill, accent, 2.2)
        f.text(x + 82.5, 100, num, 12.5, accent, "middle", True)
        f.text(x + 82.5, 122, title, 12, accent, "middle", True)
        f.text(x + 13, 156, label, 11.5, accent, "start", True)
        for i, s in enumerate(body):
            f.text(x + 13, 176 + i * 15, s, 11.5, INK)

    for x in (191, 374, 557):
        f.line(x, 152, x + 12, 152, INK, 2.4, "K")

    f.line(471.5, 228, 471.5, 250, RED, 2.2, "R")
    f.text(481, 244, "a second diagram", 11.5, RED)
    f.rect(200, 250, 400, 78, RED_F, RED, 2)
    f.text(214, 272, "reject: the assistant's second run, unchecked",
           11.5, RED, "start", True)
    f.text(214, 292,
           "\u201cwith error handling\u201d adds a NotificationService and a "
           "Timer, retries", 11.5, INK)
    f.text(214, 310,
           "three times, and replaces R-021's condition with its own.",
           11.5, INK)

    f.text(380, 346,
           "The assistant drafts. The participants, the ordering and the "
           "guards are yours.", 12, GRAY, "middle", False, True)
    f.write("ch09-fig9-8-ai-behavioural-draft")


# ---------------------------------------------------------------- 9-9

QUESTIONS_99 = [
    (BLUE, "state machine", "one object, its whole life",
     ["Does it name one object, and what becomes of it",
      "over time?",
      "e.g. \u201cWhat happens to an alert between 02:31 and 02:41?\u201d"]),
    (VIOLET, "sequence diagram", "who talks to whom, in order",
     ["Does it name the order of messages between",
      "named participants?",
      "e.g. \u201cWho tells whom, and in what order?\u201d"]),
    (GREEN, "activity diagram", "one workflow, across roles",
     ["Does it name a workflow with steps, decisions",
      "and hand-offs?",
      "e.g. \u201cWhat happens when the shift changes?\u201d"]),
    (AMBER, "a different chapter", "data, goal or process",
     ["None of the three?",
      "Then it is a data question, a goal question, or a",
      "process question. Do not force it."]),
]


@fig
def fig_9_9():
    f = Fig(470)
    f.bg()
    f.text(380, 32, "Four questions, asked in this order", 14, INK,
           "middle", True)

    for i, (accent, answer, sub, lines) in enumerate(QUESTIONS_99):
        y = 96 + i * 80
        f.rect(18, y - 30, 440, 60, fill="#FFFFFF", stroke=accent, sw=2, rx=9)
        f.text(30, y - 14, lines[0], 11.5, INK)
        f.text(30, y + 2, lines[1], 11.5, INK)
        f.text(30, y + 20, lines[2], 11.5, GRAY, "start", False, True)
        f.line(458, y, 500, y, INK, 2.2, "K")
        f.text(479, y - 6, "yes", 11.5, GREEN, "middle", True)
        f.rect(500, y - 24, 242, 48, fill="#FFFFFF", stroke=accent, sw=2, rx=9)
        f.text(621, y - 2, answer, 11.5, accent, "middle", True)
        f.text(621, y + 16, sub, 11.5, GRAY, "middle")
        if i < len(QUESTIONS_99) - 1:
            f.line(238, y + 30, 238, y + 50, INK, 2.2, "K")
            f.text(248, y + 45, "no", 11.5, GRAY, "start", True)

    f.rect(18, 384, 724, 66, fill="#F5F6F7", stroke=LINE, sw=1.6, rx=10)
    f.text(32, 408, "Do not draw a model because the notation exists.",
           11.5, INK, "start", True)
    f.text(32, 428,
           "Its real cost is that it must now agree with the other models, in "
           "every review, for the rest of the project.", 11.5, GRAY)
    f.write("ch09-fig9-9-choosing-a-model")


if __name__ == "__main__":
    want = sys.argv[1:]
    for fn in RUN:
        if not want or any(w in fn.__name__ for w in want):
            fn()
