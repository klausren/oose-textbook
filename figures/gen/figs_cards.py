#!/usr/bin/env python3
"""Chapter 8 figures: the four comparison / table figures.

  8-1  T1  domain model vs design class diagram vs database schema
  8-2  T2  noun phrases -> discard -> name
  8-5  T4  attribute mistaken for a concept (the key-box code)
  8-9  T6  concept inventory and the ledger
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (Fig, INK, GRAY, LINE, BLUE, BLUE_F, TEAL, TEAL_F, AMBER,
                    AMBER_F, RED, RED_F, GREEN, GREEN_F)  # noqa: E402


# ---------------------------------------------------------------- 8-1 -----
def fig8_1():
    f = Fig(470)
    f.bg()
    f.text(380, 38, "Three artefacts, three questions", 14, INK, "middle", True)

    cards = [
        (20, BLUE, BLUE_F, "Domain model", "a model of the problem", [
            ("MODELS", ["the problem"]),
            ("CONTAINS", ["concepts, attributes,", "associations, multiplicities"]),
            ("ANSWERS", ["what this organisation knows", "about the care it delivers"]),
            ("READER", ["Deng, Wei and Mei \u2014 the", "people whose world it describes"]),
            ("CHANGES WHEN", ["our understanding changes"]),
        ]),
        (266, TEAL, TEAL_F, "Design class diagram", "a model of the solution", [
            ("MODELS", ["the solution"]),
            ("CONTAINS", ["classes, operations, types,", "visibility, design patterns"]),
            ("ANSWERS", ["which object does what, and", "what it depends on"]),
            ("READER", ["the developers who build it"]),
            ("CHANGES WHEN", ["the design changes"]),
        ]),
        (512, GREEN, GREEN_F, "Database schema", "a model of the store", [
            ("MODELS", ["the store"]),
            ("CONTAINS", ["tables, columns, keys,", "indexes, constraints"]),
            ("ANSWERS", ["how the model is persisted", "and queried"]),
            ("READER", ["whoever operates the store"]),
            ("CHANGES WHEN", ["volume, latency or access", "pattern changes"]),
        ]),
    ]

    row_y = [138, 182, 241, 300, 359]
    for x0, accent, fill, title, purpose, rows in cards:
        f.rect(x0, 64, 226, 360, "#FFFFFF", accent, 2.2)
        f.rect(x0, 64, 226, 52, fill, accent, 2.2)
        f.text(x0 + 113, 88, title, 12.5, accent, "middle", True)
        f.text(x0 + 113, 105, purpose, 11.5, GRAY, "middle")
        for (label, vals), yl in zip(rows, row_y):
            f.text(x0 + 14, yl, label, 11.5, accent, "start", True)
            for i, v in enumerate(vals):
                f.text(x0 + 14, yl + 20 + i * 15, v, 11.5, INK)

    f.text(380, 452,
           "The reader row decides whether the people whose world the model "
           "describes can still read it.", 12, GRAY, "middle", False, True)
    f.write("ch08-fig8-1-three-artefacts")


# ---------------------------------------------------------------- 8-2 -----
def fig8_2():
    f = Fig(470)
    f.bg()
    f.text(380, 38, "Finding concepts: nouns, then discard, then name",
           14, INK, "middle", True)

    # ---- card 1: collect
    f.rect(20, 64, 160, 320, "#FFFFFF", BLUE, 2.2)
    f.rect(20, 64, 160, 52, BLUE_F, BLUE, 2.2)
    f.text(100, 90, "1 \u00b7 Collect", 12.5, BLUE, "middle", True)
    f.text(100, 107, "from the sources", 11.5, GRAY, "middle")
    f.text(32, 140, "54 candidate", 12.5, BLUE, "start", True)
    f.text(32, 160, "noun phrases", 11.5, INK)
    f.text(32, 176, "from nine sources", 11.5, INK)
    f.text(32, 210, "One pass.", 11.5, BLUE, "start", True)
    f.text(32, 226, "No editing.", 11.5, INK)
    f.text(32, 260, "A source tag on", 11.5, INK)
    f.text(32, 276, "every card, before", 11.5, INK)
    f.text(32, 292, "it is sorted.", 11.5, INK)
    f.text(32, 326, "Five minutes of", 11.5, GRAY)
    f.text(32, 342, "tags beats an", 11.5, GRAY)
    f.text(32, 358, "hour of argument.", 11.5, GRAY)

    # ---- card 2: discard
    f.rect(206, 64, 300, 320, "#FFFFFF", INK, 2.2)
    f.rect(206, 64, 300, 52, "#F5F6F7", INK, 2.2)
    f.text(356, 90, "2 \u00b7 Discard", 12.5, INK, "middle", True)
    f.text(356, 107, "the ledger, by family", 11.5, GRAY, "middle")
    rows = [
        (GRAY, "synonyms \u00b7 merged into one word", "12", GRAY),
        (AMBER, "attributes \u00b7 demoted to a field", "9", AMBER),
        (BLUE, "outside the boundary \u00b7 recorded", "5", BLUE),
        (RED, "no evidence \u00b7 deleted", "8", RED),
        (RED, "the solution \u00b7 removed", "4", RED),
    ]
    for i, (chip, label, count, col) in enumerate(rows):
        y = 150 + i * 46
        f.rect(222, y - 9, 12, 12, chip, None, rx=2)
        f.text(244, y, label, 11.5, INK)
        f.text(496, y, count, 12.5, col, "end", True)
    f.text(356, 364, "The ledger is a deliverable.", 11.5, GRAY, "middle", False, True)

    # ---- card 3: name
    f.rect(532, 64, 208, 320, "#FFFFFF", GREEN, 2.2)
    f.rect(532, 64, 208, 52, GREEN_F, GREEN, 2.2)
    f.text(636, 90, "3 \u00b7 Name", 12.5, GREEN, "middle", True)
    f.text(636, 107, "what survives", 11.5, GRAY, "middle")
    f.text(544, 140, "16 concepts", 12.5, GREEN, "start", True)
    f.text(544, 160, "kept", 11.5, INK)
    f.text(544, 194, "A singular noun", 11.5, INK)
    f.text(544, 210, "in the users' words", 11.5, INK)
    f.text(544, 244, "One word per", 11.5, INK)
    f.text(544, 260, "concept, everywhere", 11.5, INK)
    f.text(544, 294, "No Manager, Info,", 11.5, INK)
    f.text(544, 310, "Data or Service", 11.5, INK)
    f.text(544, 344, "Question the noun,", 11.5, GRAY)
    f.text(544, 360, "not the source.", 11.5, GRAY)

    f.line(182, 224, 200, 224, INK, 2.4, "K")
    f.line(508, 224, 526, 224, INK, 2.4, "K")

    f.text(380, 436,
           "Extraction is mechanical. Reduction is the analysis, and the "
           "ledger is what a reviewer can check.", 12, GRAY, "middle", False, True)
    f.write("ch08-fig8-2-noun-to-concept")


# ---------------------------------------------------------------- 8-5 -----
def fig8_5():
    f = Fig(420)
    f.bg()
    f.text(380, 38, "Attribute mistaken for a concept: the key-box code",
           14, INK, "middle", True)

    f.rect(20, 64, 350, 300, "#FFFFFF", RED, 2.2)
    f.rect(20, 64, 350, 52, RED_F, RED, 2.2)
    f.text(195, 90, "A field on Resident", 12.5, RED, "middle", True)
    f.text(195, 107, "the version the team drew first", 11.5, GRAY, "middle")
    for y, s, bold, col in [
        (142, "IDENTITY", True, RED),
        (162, "No. Four digits \u2014 and the", False, INK),
        (177, "second resident's card holds", False, INK),
        (192, "the same four.", False, INK),
        (222, "INDEPENDENT LIFE", True, RED),
        (242, "Yes \u2014 but not of the resident.", False, INK),
        (257, "It changes when the lock does.", False, INK),
        (287, "SHARING", True, RED),
        (307, "Yes. Two residents in one", False, INK),
        (322, "building share one box.", False, INK),
    ]:
        f.text(34, y, s, 11.5, col, "start", bold)
    f.rect(34, 336, 322, 26, RED_F, RED, 1.4, rx=6)
    f.text(46, 353, "Verdict: an attribute of the wrong concept", 11.5, RED, "start", True)

    f.rect(390, 64, 350, 300, "#FFFFFF", GREEN, 2.2)
    f.rect(390, 64, 350, 52, GREEN_F, GREEN, 2.2)
    f.text(565, 90, "An attribute of Address", 12.5, GREEN, "middle", True)
    f.text(565, 107, "after the three tests", 11.5, GRAY, "middle")
    for y, s, bold, col in [
        (142, "IDENTITY", True, GREEN),
        (162, "Yes. This box, at this door.", False, INK),
        (192, "INDEPENDENT LIFE", True, GREEN),
        (212, "Yes. Re-coded once, for every", False, INK),
        (227, "resident behind it.", False, INK),
        (257, "SHARING", True, GREEN),
        (277, "Yes \u2014 and this is the point.", False, INK),
        (292, "Two residents, one door, one box.", False, INK),
    ]:
        f.text(404, y, s, 11.5, col, "start", bold)
    f.rect(404, 336, 322, 26, GREEN_F, GREEN, 1.4, rx=6)
    f.text(416, 353, "Verdict: a fact owned by a door", 11.5, GREEN, "start", True)

    f.text(380, 400,
           "The three tests do not stop at concept or attribute. They name "
           "which concept owns the fact.", 12, GRAY, "middle", False, True)
    f.write("ch08-fig8-5-attribute-vs-concept")


# ---------------------------------------------------------------- 8-9 -----
def fig8_9():
    f = Fig(560)
    f.bg()
    f.text(380, 36, "Concept inventory: name, evidence, verdict",
           14, INK, "middle", True)

    # left: the ledger
    f.rect(20, 58, 340, 262, "#FFFFFF", INK, 2.2)
    f.text(190, 86, "The ledger", 12.5, INK, "middle", True)
    f.text(190, 104, "what happened to 54 candidates", 11.5, GRAY, "middle")
    ledger = [
        ("candidates collected", "54", INK),
        ("kept as concepts", "16", GREEN),
        ("synonyms, merged", "12", GRAY),
        ("attributes, demoted", "9", AMBER),
        ("outside the boundary", "5", BLUE),
        ("no evidence, deleted", "8", RED),
        ("solution words, removed", "4", RED),
    ]
    for i, (label, count, col) in enumerate(ledger):
        y = 134 + i * 28
        f.text(34, y, label, 11.5, INK, "start", label == "kept as concepts")
        f.text(346, y, count, 12, col, "end", True)

    # right: evidence tags
    f.rect(380, 58, 360, 262, "#FFFFFF", INK, 2.2)
    f.text(560, 86, "Where the evidence comes from", 12.5, INK, "middle", True)
    tags = [
        ("INT-3", BLUE, "an interview with Deng"),
        ("OBS-1", AMBER, "a shift observation at 02:40"),
        ("POL-2", TEAL, "the key-holder procedure, 4.3"),
        ("UC-4", GREEN, "a use case from Chapter 7"),
    ]
    for i, (tag, col, desc) in enumerate(tags):
        y = 140 + i * 32
        f.text(394, y, tag, 11.5, col, "start", True)
        f.text(458, y, desc, 11.5, INK)
    f.text(394, 290, "A concept with no tag is a finding, not a detail.",
           11.5, GRAY, "start", False, True)

    # table
    f.rect(20, 344, 720, 26, "#F5F6F7", LINE, 1.4, rx=6)
    f.text(34, 362, "Concept", 11.5, INK, "start", True)
    f.text(240, 362, "Evidence", 11.5, INK, "start", True)
    f.text(470, 362, "Verdict", 11.5, INK, "start", True)
    f.line(26, 378, 734, 378, LINE, 1.4)
    table = [
        ("Resident", "INT-3 \u00b7 POL-2", "supported", INK),
        ("Address", "OBS-1 \u00b7 POL-2", "supported", INK),
        ("Care assignment", "UC-4, implied", "inferred \u2014 ask the supervisor", AMBER),
        ("Building", "none found", "unsupported \u00b7 an attribute of Address", RED),
    ]
    for i, (c, e, v, col) in enumerate(table):
        y = 400 + i * 30
        f.text(34, y, c, 11.5, INK, "start", True)
        f.text(240, y, e, 11.5, GRAY)
        f.text(470, y, v, 11.5, col)
        if i < 3:
            f.line(26, y + 9, 734, y + 9, "#F5F6F7", 1.3)

    f.text(380, 536,
           "Fifty-four candidates, sixteen concepts, and a source tag on every line.",
           12, GRAY, "middle", False, True)
    f.write("ch08-fig8-9-concept-inventory")


if __name__ == "__main__":
    fig8_1()
    fig8_2()
    fig8_5()
    fig8_9()
