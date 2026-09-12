#!/usr/bin/env python3
"""Chapter 8 figures: the two diagrams and the AI-workflow figure.

  8-6  T3  association class: Care assignment
  8-7  T1  the domain model links back to the use case list
  8-8  T7  AI-assisted concept extraction, with verification
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (Fig, INK, GRAY, LINE, BLUE, BLUE_F, TEAL, TEAL_F, AMBER,
                    AMBER_F, RED, RED_F, GREEN, GREEN_F, VIOLET, VIOLET_F)  # noqa: E402


# ---------------------------------------------------------------- 8-6 -----
def fig8_6():
    f = Fig(490)
    f.bg()
    f.text(380, 38, "An association class: Care assignment", 14, INK, "middle", True)

    # --- the wrong version
    f.rect(20, 58, 720, 92, RED_F, RED, 2, 10, "6 4")
    f.text(34, 80, "WRONG \u00b7 the facts hung on one end", 11.5, RED, "start", True)
    f.rect(56, 90, 168, 48, "#FFFFFF", RED, 1.8)
    f.text(140, 110, "Caregiver", 11.5, INK, "middle", True)
    f.text(140, 130, "weeklyHours = 18", 11.5, RED, "middle")
    f.rect(404, 90, 168, 48, "#FFFFFF", RED, 1.8)
    f.text(488, 118, "Resident", 11.5, INK, "middle", True)
    f.line(224, 114, 400, 114, GRAY, 2.2, "G")
    f.text(314, 106, "assigned to", 11.5, GRAY, "middle")
    for i, s in enumerate(["Deng has three",
                           "arrangements on file.",
                           "The model records one."]):
        f.text(590, 106 + i * 15, s, 11.5, RED)

    f.line(380, 150, 380, 176, INK, 2.4, "K")

    # --- the right version
    f.rect(20, 178, 720, 258, GREEN_F, GREEN, 2)
    f.text(34, 200, "RIGHT \u00b7 the facts get their own box", 11.5, GREEN, "start", True)
    f.rect(50, 230, 160, 40, "#FFFFFF", GREEN, 1.8)
    f.text(130, 254, "Caregiver", 11.5, INK, "middle", True)
    f.rect(550, 230, 160, 40, "#FFFFFF", GREEN, 1.8)
    f.text(630, 254, "Resident", 11.5, INK, "middle", True)
    f.line(210, 250, 546, 250, BLUE, 2.4)
    f.text(222, 242, "1", 11.5, GRAY)
    f.text(538, 242, "0..*", 11.5, GRAY, "end")

    f.rect(290, 290, 180, 90, TEAL_F, TEAL, 2)
    f.text(380, 310, "Care assignment", 12, TEAL, "middle", True)
    f.line(302, 318, 458, 318, TEAL, 1.4)
    for i, s in enumerate(["role \u00b7 primary or backup",
                           "from \u00b7 to",
                           "weeklyHours"]):
        f.text(302, 336 + i * 15, s, 11.5, INK)
    f.line(380, 250, 380, 290, TEAL, 2, None, "4 4")

    f.text(34, 406,
           "Three rows, three arrangements: one pair of concepts, and the "
           "hours belong to neither of them.", 11.5, GRAY)

    f.text(380, 464,
           "If a relationship has an attribute, ask what else has that attribute.",
           12, GRAY, "middle", False, True)
    f.write("ch08-fig8-6-association-class")


# ---------------------------------------------------------------- 8-7 -----
def fig8_7():
    f = Fig(550)
    f.bg()
    f.text(380, 36, "The domain model links back to the use case list",
           14, INK, "middle", True)

    f.line(20, 58, 50, 58, BLUE, 2.4, "B")
    f.text(58, 62, "maintains", 11.5, GRAY)
    f.line(180, 58, 210, 58, GRAY, 2.2, "G", "5 4")
    f.text(218, 62, "mentions only", 11.5, GRAY)
    f.text(150, 84, "use cases", 11.5, GRAY, "middle", True)
    f.text(640, 84, "concepts", 11.5, GRAY, "middle", True)

    left = [("Log a visit", "Caregiver"),
            ("Register a resident", "Care-centre supervisor"),
            ("Maintain contact records", "Family contact"),
            ("Update the caregiver roster", "Care-centre supervisor")]
    for i, (title, sub) in enumerate(left):
        cy = 117 + i * 74
        f.rect(20, cy - 25, 260, 50, "#FFFFFF", BLUE, 2)
        f.text(34, cy - 4, title, 11.5, INK, "start", True)
        f.text(34, cy + 11, sub, 11.5, GRAY)

    right = [("Visit log", BLUE, BLUE_F),
             ("Resident", BLUE, BLUE_F),
             ("Address", RED, RED_F),
             ("Contact record", BLUE, BLUE_F),
             ("Care assignment", RED, RED_F)]
    for i, (title, col, fill) in enumerate(right):
        cy = 110 + i * 64
        f.rect(540, cy - 22, 200, 44, fill, col, 2)
        f.text(640, cy + 4, title, 11.5, INK, "middle",
               col == RED)

    for y1, y2, col, m, dash in [(117, 110, BLUE, "B", None),
                                 (191, 174, BLUE, "B", None),
                                 (191, 238, GRAY, "G", "5 4"),
                                 (265, 302, BLUE, "B", None),
                                 (265, 238, GRAY, "G", "5 4"),
                                 (339, 366, BLUE, "B", None)]:
        f.line(280, y1, 540, y2, col, 2.2, m, dash)

    f.rect(20, 404, 720, 96, "#F5F6F7", LINE, 1.6)
    f.text(34, 426, "The walk in the other direction", 11.5, INK, "start", True)
    f.text(34, 448,
           "\u00b7 Address is mentioned by two use cases and maintained by "
           "none \u2014 the key-box code lived in a spreadsheet.", 11.5, INK)
    f.text(34, 466,
           "\u00b7 Care assignment is implied by Log a visit and stated by no "
           "use case \u2014 new requirement R-057.", 11.5, INK)

    f.text(380, 528,
           "Every concept needs at least one goal that maintains it, or a "
           "reason on the record.", 12, GRAY, "middle", False, True)
    f.write("ch08-fig8-7-usecases-to-concepts")


# ---------------------------------------------------------------- 8-8 -----
def fig8_8():
    f = Fig(360)
    f.bg()
    f.text(380, 38, "AI-assisted concept extraction, with verification",
           14, INK, "middle", True)

    boxes = [
        (23, BLUE, BLUE_F, "1", "Human supplies", "YOU SUPPLY",
         ["Four transcripts,", "eleven thousand words", "of interview."]),
        (206, VIOLET, VIOLET_F, "2", "AI lists", "AI RETURNS",
         ["51 candidate", "concepts, each with", "a definition."]),
        (389, AMBER, AMBER_F, "3", "Human verifies", "YOU CHECK",
         ["Three tests, the", "boundary, and the", "evidence tag."]),
        (572, GREEN, GREEN_F, "4", "Artifact", "YOU PRODUCE",
         ["16 concepts, each", "with a source line", "it can be traced to."]),
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
    f.rect(389, 252, 165, 58, RED_F, RED, 2)
    f.text(401, 274, "reject: no source line", 11.5, RED, "start", True)
    f.text(401, 292, "delete, or log a question", 11.5, INK)
    f.text(480, 246, "any line without a tag", 11.5, RED)

    f.text(380, 344,
           "The extraction is the assistant's. The three tests, the boundary "
           "and the evidence tag are yours.", 12, GRAY, "middle", False, True)
    f.write("ch08-fig8-8-ai-concept-extraction")


if __name__ == "__main__":
    fig8_6()
    fig8_7()
    fig8_8()
