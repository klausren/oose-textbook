#!/usr/bin/env python3
"""Chapter 10 figures: requirements validation and management.

  10-1  T2  the validation loop
  10-2  T6  a requirements review checklist, scored
  10-3  T4  four requirement defect classes
  10-4  T2  change control: request to re-baseline
  10-5  T6  the CareLink traceability matrix
  10-6  T1  why baselines exist: two timelines
  10-7  T4  traceability after a scope change
  10-8  T7  AI-assisted requirement review, with verification
  10-9  T5  the CareLink change-request form
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (Fig, INK, GRAY, LINE, BLUE, BLUE_F, TEAL, TEAL_F, AMBER,
                    AMBER_F, RED, RED_F, GREEN, GREEN_F, VIOLET, VIOLET_F,
                    block, lblock, wrap)  # noqa: E402

W = 760


def head(f, title, sub=None):
    f.text(10, 40, title, 17, INK, "start", True)
    if sub:
        f.text(10, 62, sub, 12.5, GRAY, "start")


# ---------------------------------------------------------------- 10-1 ----
def fig10_1():
    f = Fig(400)
    f.bg()
    head(f, "The validation loop",
         "Four checks, run until every requirement is traced, testable and agreed")

    cards = [
        ("1  Inspect", BLUE, BLUE_F,
         "The specification is read against the models: does every "
         "sentence in the document have a diagram behind it?"),
        ("2  Review", TEAL, TEAL_F,
         "Stakeholders walk the scenarios out loud. Mei and Deng read the "
         "same sentence and disagree in public."),
        ("3  Test", AMBER, AMBER_F,
         "Each acceptance criterion is handed to the person who will write "
         "the test. If they cannot write one, the criterion is not written yet."),
        ("4  Agree", GREEN, GREEN_F,
         "The requirement set is signed and frozen. Signing is a decision, "
         "not a formality: it commits the project to a scope."),
    ]
    cw, gap, ch = 171, 19, 176
    y = 84
    for i, (name, col, fill, body) in enumerate(cards):
        x = 10 + i * (cw + gap)
        f.rect(x, y, cw, ch, fill, col, 2, 10)
        f.text(x + 12, y + 26, name, 13.5, col, "start", True)
        block(f, x + cw / 2, y + 50, body, 25, 11.5, INK, 15)
        if i < 3:
            f.line(x + cw + 3, y + ch / 2, x + cw + gap - 3, y + ch / 2,
                   col, 2.4, "B")

    ly = y + ch + 34
    f.line(94, y + ch + 4, 94, ly, GRAY, 2.4)
    f.line(94, ly, 666, ly, GRAY, 2.4)
    f.line(666, ly, 666, y + ch + 4, GRAY, 2.4, "G")
    f.text(380, ly + 20, "each finding returns to the source it came from",
           11.5, GRAY, "middle", False, True)
    f.text(380, ly + 48,
           "Exit condition: every requirement is traced to a source, testable, and agreed by "
           "the customer.", 12, INK, "middle", True)
    f.text(380, ly + 68,
           "Without a stated exit condition, validation continues until the schedule ends it.",
           11.5, GRAY, "middle", False, True)
    f.write("ch10-fig10-1-validation-loop")


# ---------------------------------------------------------------- 10-2 ----
def fig10_2():
    f = Fig(440)
    f.bg()
    head(f, "A requirements review checklist",
         "Six criteria, each answered yes or no by a different reader")

    cols = [96, 236, 316, 92]
    x0 = 10
    rows = [
        ("1  Complete", "Is every path through the scenario covered, "
                        "including the ones nobody mentioned?", "Every extension named"),
        ("2  Unambiguous", "Can two readers take two different meanings "
                           "from this sentence?", "One reading only"),
        ("3  Testable", "Can a tester write a pass/fail check from this "
                        "sentence alone?", "Criterion exists"),
        ("4  Traceable", "Does it name the interview record it came from?",
         "Source identified"),
        ("5  Consistent", "Does it contradict anything else in the set?",
         "No contradiction"),
        ("6  Bounded", "Does it say what is out of scope as well as in?",
         "Won't list present"),
    ]
    hdrs = ["Criterion", "The question the reader answers", "Pass condition",
            "Verdict"]

    hy, rh = 80, 46
    f.rect(x0, hy, sum(cols), 34, INK, None, 2, 6)
    cx = x0
    for j, htxt in enumerate(hdrs):
        f.text(cx + 10, hy + 22, htxt, 12, "#FFFFFF", "start", True)
        cx += cols[j]
    for i, (name, q, cond) in enumerate(rows):
        y = hy + 34 + i * rh
        fill = "#F5F6F7" if i % 2 == 0 else "#FFFFFF"
        f.rect(x0, y, sum(cols), rh, fill, LINE, 1.6, 4)
        cx = x0
        f.text(cx + 10, y + 28, name, 12.5, INK, "start", True)
        cx += cols[0]
        lblock(f, cx + 10, y + 20, q, 44, 11.5, GRAY, 15)
        cx += cols[1]
        f.text(cx + 10, y + 28, cond, 11.5, INK)
        cx += cols[2]
        f.circle(cx + 46, y + rh / 2, 12, "#FFFFFF", LINE, 1.8)
        for j in range(4):
            f.line(x0 + 6, y + j * rh / 4, x0 + sum(cols) - 6, y + j * rh / 4,
                   "#EDEFF2", 1)
    f.text(10, hy + 34 + len(rows) * rh + 26,
           "Two readers fill this in independently. Where they disagree, the requirement — "
           "not the reader — is wrong.",
           12, INK, "start", True)
    f.write("ch10-fig10-2-review-checklist")


# ---------------------------------------------------------------- 10-3 ----
def fig10_3():
    f = Fig(456)
    f.bg()
    head(f, "Four ways a requirement goes wrong",
         "One CareLink example per class, all four found in the same review")

    panels = [
        ("Omission", BLUE, BLUE_F,
         "Something that must happen is not written down anywhere.",
         "R-055 covers the acknowledgement that stops an escalation. "
         "No requirement covers what happens when the escalation is never "
         "acknowledged at all."),
        ("Conflict", TEAL, TEAL_F,
         "Two requirements cannot both hold at the same time.",
         "R-055 escalates to the second contact at eight minutes. R-061 "
         "notifies the neighbour at ten, and nothing says whether the "
         "escalation pauses."),
        ("Ambiguity", AMBER, AMBER_F,
         "Two readers, two defensible readings, one sentence.",
         "R-056: \u201can alert cannot be closed without a recorded safety "
         "confirmation.\u201d Recorded by whom, and does a photograph count?"),
        ("Gold-plating", RED, RED_F,
         "A capability nobody asked for, carried at full cost.",
         "The v1 specification includes a monthly PDF report that no "
         "stakeholder in chapters 4 to 7 ever requested or would open."),
    ]
    pw, ph, gap = 360, 152, 20
    for i, (name, col, fill, rule, ex) in enumerate(panels):
        x = 10 + (i % 2) * (pw + gap)
        y = 84 + (i // 2) * (ph + gap)
        f.rect(x, y, pw, ph, fill, col, 2, 10)
        f.text(x + 14, y + 26, name, 13.5, col, "start", True)
        block(f, x + pw / 2, y + 50, rule, 58, 11.5, INK, 15)
        f.line(x + 14, y + 76, x + pw - 14, y + 76, col, 1.4)
        lblock(f, x + 14, y + 96, ex, 60, 11.5, GRAY, 15)
    f.text(380, 84 + 2 * ph + gap + 30,
           "The first three are defects in the specification. The fourth is a defect in "
           "the process that let it in.",
           12, INK, "middle", True)
    f.write("ch10-fig10-3-defect-classes")


# ---------------------------------------------------------------- 10-4 ----
def fig10_4():
    f = Fig(470)
    f.bg()
    head(f, "Change control: from request to re-baseline",
         "Five steps, and the artefact each one leaves behind")

    steps = [
        ("1  Request", BLUE, "Anybody may raise one, in writing, on the form of "
                             "figure 10-9.", "a numbered change request"),
        ("2  Assess", TEAL, "Which requirements, use cases, model elements and "
                            "tests are touched — and what that costs.",
         "an impact list"),
        ("3  Decide", AMBER, "The customer accepts, defers or rejects. Acceptance "
                             "is a decision with a date and a name.",
         "a recorded decision"),
        ("4  Implement", RED, "The specification, the models and the traceability "
                              "matrix are updated together.",
         "a revised specification"),
        ("5  Re-baseline", GREEN, "A new version number is issued, and the old one "
                                  "stays readable forever.",
         "a new baseline"),
    ]
    y0, rh, gap = 90, 52, 12
    for i, (name, col, body, artefact) in enumerate(steps):
        y = y0 + i * (rh + gap)
        f.rect(10, y, 214, rh, BLUE_F if i % 2 == 0 else "#FFFFFF", col, 2, 8)
        f.text(24, y + 22, name, 13, col, "start", True)
        lblock(f, 24, y + 39, body, 34, 11.5, INK, 14)
        f.line(232, y + rh / 2, 268, y + rh / 2, GRAY, 2.4, "G")
        f.rect(280, y, 470, rh, "#F5F6F7", LINE, 1.6, 8)
        f.text(298, y + rh / 2 + 4, artefact, 12, INK)
    f.text(10, y0 + 5 * (rh + gap) + 28,
           "Steps 1 to 3 cost nothing but a meeting. Steps 4 and 5 are where the schedule moves.",
           12, INK, "start", True)
    f.write("ch10-fig10-4-change-control")


# ---------------------------------------------------------------- 10-5 ----
def fig10_5():
    f = Fig(452)
    f.bg()
    head(f, "The CareLink traceability matrix",
         "One row per requirement, read left to right as a chain of custody")

    cols = [78, 116, 148, 176, 118, 104]
    hdrs = ["Requirement", "Source record", "Use case", "Model element",
            "Design element", "Test case"]
    rows = [
        ("R-053", "R-03-01", "Monitor a resident", "Alert.dispatch",
         "AlertService", "T-053"),
        ("R-054", "R-03-04", "Acknowledge an alert", "Alert.state",
         "AlertService", "T-054"),
        ("R-055", "R-03-04", "Acknowledge an alert", "Escalation.timer",
         "EscalationJob", "T-055"),
        ("R-056", "R-03-06", "Close an alert", "Alert.close()",
         "AlertService", "T-056"),
        ("R-057", "R-04-02", "Schedule a visit", "Visit : CarePlan",
         "VisitRepository", "T-057"),
        ("R-058", "R-05-01", "Hand over a shift", "Caregiver.roster",
         "RosterService", "T-058"),
        ("R-059", "R-05-01", "Hand over a shift", "Handover.record",
         "(not yet designed)", "T-059"),
        ("R-060", "R-05-03", "Record an observation", "Observation : Visit",
         "(not yet designed)", "(not yet written)"),
    ]
    x0, hy, rh = 10, 84, 34
    f.rect(x0, hy, sum(cols), 32, INK, None, 2, 6)
    cx = x0
    for j, h in enumerate(hdrs):
        f.text(cx + 10, hy + 21, h, 11.5, "#FFFFFF", "start", True)
        cx += cols[j]
    for i, row in enumerate(rows):
        y = hy + 32 + i * rh
        f.rect(x0, y, sum(cols), rh, "#F5F6F7" if i % 2 == 0 else "#FFFFFF",
               LINE, 1.6, 4)
        cx = x0
        for j, v in enumerate(row):
            col = INK if v else GRAY
            ital = v.startswith("(")
            f.text(cx + 10, y + 22, v, 11.5, GRAY if ital else col, "start",
                   j == 0, ital)
            cx += cols[j]
        f.line(x0 + 6, y + rh, x0 + sum(cols) - 6, y + rh, "#EDEFF2", 1)
    f.text(10, hy + 32 + len(rows) * rh + 26,
           "Two rows end in a bracket. Those two brackets are the whole point of keeping a matrix: "
           "they are the work not yet done.",
           12, INK, "start", True)
    f.text(10, hy + 32 + len(rows) * rh + 46,
           "A requirement with a blank cell is not a failure. A requirement with a blank cell that "
           "nobody noticed is.", 11.5, GRAY, "start", False, True)
    f.write("ch10-fig10-5-traceability-matrix")


# ---------------------------------------------------------------- 10-6 ----
def fig10_6():
    f = Fig(400)
    f.bg()
    head(f, "Why baselines exist",
         "The same change request, with one difference: a version number")

    def timeline(y, label, colour, fill, marks, tail, tail_col):
        f.rect(10, y, 740, 132, fill, colour, 2, 10)
        f.text(26, y + 26, label, 13.5, colour, "start", True)
        f.line(60, y + 72, 700, y + 72, colour, 2.4)
        for i, (t, kind) in enumerate(marks):
            x = 60 + i * 152
            f.circle(x, y + 72, 7, colour)
            f.text(x, y + 56, t, 11.5, INK, "middle", True)
        f.text(380, y + 96, tail, 11.5, tail_col, "middle")
        f.text(700, y + 56, "time", 11.5, GRAY, "end")

    timeline(84, "With a baseline: v1.2", BLUE, BLUE_F,
             [("v1.0", 0), ("v1.1", 1), ("v1.2", 2), ("change", 3)],
             "Every requirement can be answered from the version that was current when it was written.",
             INK)
    timeline(232, "Without a baseline: main", RED, RED_F,
             [("as written", 0), ("informally edited", 1), ("edited again", 2),
              ("change", 3)],
             "Nobody can say which sentence the design was built from, so nobody can cost the change.",
             RED)
    f.text(380, 232 + 150,
           "A baseline is not bureaucracy. It is the answer to \u201cwhich version did you agree to?\u201d",
           12, INK, "middle", True)
    f.write("ch10-fig10-6-baselines")


# ---------------------------------------------------------------- 10-7 ----
def fig10_7():
    f = Fig(430)
    f.bg()
    head(f, "Traceability after a scope change",
         "The same matrix before and after re-baselining, with the links that moved")

    def matrix(x, y, title, colour, fill, rows, note):
        f.rect(x, y, 350, 268, fill, colour, 2, 10)
        f.text(x + 16, y + 26, title, 13.5, colour, "start", True)
        f.line(x + 16, y + 40, x + 334, y + 40, colour, 1.4)
        for i, (req, txt, state) in enumerate(rows):
            yy = y + 62 + i * 26
            f.text(x + 16, yy, req, 11.5, INK, "start", True)
            mark = {"ok": GREEN, "moved": AMBER, "lost": RED}[state]
            fm = {"ok": GREEN_F, "moved": AMBER_F, "lost": RED_F}[state]
            f.rect(x + 66, yy - 13, 176, 20, fm, mark, 1.4, 4)
            f.text(x + 76, yy + 1, txt, 11.5, INK)
            if state == "ok":
                f.tick(x + 266, yy - 3, 8)
            elif state == "moved":
                f.text(x + 266, yy + 1, "re-linked", 11.5, AMBER, "middle")
            else:
                f.cross(x + 266, yy - 3, 8)
                f.text(x + 306, yy + 1, "gap", 11.5, RED, "middle")
        f.text(x + 175, y + 250, note, 11.5, GRAY, "middle")

    before = [("R-053", "Monitor \u2192 AlertService", "ok"),
              ("R-054", "Acknowledge \u2192 AlertService", "ok"),
              ("R-055", "Escalation \u2192 EscalationJob", "ok"),
              ("R-056", "Close \u2192 AlertService", "ok"),
              ("R-057", "Visit \u2192 VisitRepository", "ok"),
              ("R-058", "Roster \u2192 RosterService", "ok")]
    after = [("R-053", "Monitor \u2192 AlertService", "ok"),
             ("R-054", "Acknowledge \u2192 AlertService", "ok"),
             ("R-055", "Escalation \u2192 AlertService", "moved"),
             ("R-056", "Close \u2192 AlertService", "ok"),
             ("R-057", "Visit \u2192 VisitRepository", "ok"),
             ("R-061", "(new) needs a design element", "lost")]
    matrix(10, 84, "Baseline v1.2, before the change", BLUE, "#FFFFFF", before,
           "six rows, six live links")
    matrix(400, 84, "Baseline v1.3, after re-baselining", GREEN, "#FFFFFF", after,
           "one moved, one still open, one added")
    f.text(380, 84 + 288,
           "Re-baselining is the moment the matrix earns its keep: it shows which links survived "
           "and which did not.",
           12, INK, "middle", True)
    f.write("ch10-fig10-7-rebaseline")


# ---------------------------------------------------------------- 10-8 ----
def fig10_8():
    f = Fig(390)
    f.bg()
    head(f, "AI-assisted requirement review, with verification",
         "The model drafts; the human is accountable for every confirmed defect")

    steps = [
        ("Human", BLUE, BLUE_F,
         "Supplies the specification and the interview records it claims "
         "to come from. No summary, no paraphrase."),
        ("AI", VIOLET, VIOLET_F,
         "Lists suspected defects: sentences with no source, pairs that "
         "conflict, terms used two ways, capabilities nobody asked for."),
        ("Human", BLUE, BLUE_F,
         "Checks each suggestion against the source. Keeps the real ones, "
         "discards the plausible ones, records why."),
        ("Confirmed list", GREEN, GREEN_F,
         "What reaches the customer is only what a person has verified. "
         "The rejected suggestions are kept as evidence of the check."),
    ]
    cw, gap, ch = 171, 19, 168
    y = 84
    for i, (who, col, fill, body) in enumerate(steps):
        x = 10 + i * (cw + gap)
        f.rect(x, y, cw, ch, fill, col, 2, 10)
        f.text(x + 12, y + 24, who, 13, col, "start", True)
        block(f, x + cw / 2, y + 46, body, 25, 11.5, INK, 15)
        if i < 3:
            f.line(x + cw + 3, y + ch / 2, x + cw + gap - 3, y + ch / 2,
                   col, 2.4, "V")
    f.rect(10, y + ch + 26, 740, 74, VIOLET_F, VIOLET, 2, 10)
    f.text(26, y + ch + 50,
           "Verify before you trust: a defect list is a set of claims, and every claim needs a "
           "source before it reaches a customer.",
           12, VIOLET, "start", True)
    f.text(26, y + ch + 72,
           "An AI suggestion with no interview record behind it is a hypothesis, not a finding.",
           11.5, INK, "start")
    f.write("ch10-fig10-8-ai-review")


# ---------------------------------------------------------------- 10-9 ----
def fig10_9():
    f = Fig(520)
    f.bg()
    head(f, "The CareLink change-request form",
         "Paper or tracker, the fields are the same — and the first two are the ones people skip")

    f.rect(10, 84, 740, 412, "#FFFFFF", LINE, 2, 10)
    f.rect(10, 84, 740, 44, INK, None, 2, 10)
    f.text(26, 112, "Change request  \u00b7  CareLink", 14.5, "#FFFFFF", "start", True)
    f.text(734, 112, "CR-004", 13, "#FFFFFF", "end", True)

    fields = [
        ("Raised by", "Deng Wei, care co-ordinator", "who", False),
        ("Date raised", "2026-03-02", "who", False),
        ("What should change", "The alert must also notify the resident's "
                               "named neighbour when nobody acknowledges it "
                               "within ten minutes.", "what", True),
        ("Why now", "Two no-acknowledgement incidents in February, both "
                    "resolved by the neighbour after a phone call.", "why", True),
        ("Requirements touched", "R-053, R-055, and the extension in R-056",
         "impact", False),
        ("Models touched", "Alert state machine: one new state, two new "
                           "transitions", "impact", False),
        ("Requested by when", "before the April release", "when", False),
        ("Decision", "accepted \u2611   deferred \u2610   rejected \u2610",
         "decision", False),
        ("Decision by / on", "\u2014", "decision", False),
    ]
    y = 146
    for label, value, kind, big in fields:
        h = 44 if big else 34
        f.text(26, y + h / 2 + 4, label, 12, INK, "start", True)
        f.rect(196, y, 540, h, "#F5F6F7", LINE, 1.6, 6)
        lblock(f, 210, y + (22 if big else 21), value, 68, 11.5, INK, 15)
        y += h + 4
    f.text(26, 506,
           "Fields 3 and 4 are the ones that get left blank. A change request without a reason "
           "cannot be assessed, only obeyed.",
           11.5, GRAY, "start", False, True)
    f.write("ch10-fig10-9-change-request-form")


if __name__ == "__main__":
    fig10_1()
    fig10_2()
    fig10_3()
    fig10_4()
    fig10_5()
    fig10_6()
    fig10_7()
    fig10_8()
    fig10_9()
    print("all chapter 10 figures written")
