#!/usr/bin/env python3
"""Back-matter generator and checker for the open edition.

Two jobs, one source of truth:

  1. `--check`  Compare every chapter's `**Key terms:**` line against the
     entries in manuscript/glossary.md, in BOTH directions. A term a chapter
     introduces but the glossary does not define is a defect; a term the
     glossary defines but no chapter introduces is either a leftover or a
     term waiting for the chapter that will need it.

  2. (default)  Regenerate manuscript/index.md from the chapter sources, so
     the index cannot drift from the chapters. Every reference is a SECTION
     number (5.4), not a page number: the manuscript has no pagination of
     its own -- Leanpub, PDF and DOCX all repaginate -- but section numbers
     are stable across every output format.

Usage:
    python3 build/make-backmatter.py            # regenerate manuscript/index.md
    python3 build/make-backmatter.py --check    # report glossary coverage only
    python3 build/make-backmatter.py --check --strict   # non-zero exit on a gap

Run `--check` before every release, and regenerate the index whenever a
chapter is added or a section is renumbered.
"""

from __future__ import annotations

import argparse
import glob
import pathlib
import re
import sys
import unicodedata

BOOK = pathlib.Path(__file__).resolve().parent.parent
MANUSCRIPT = BOOK / "manuscript"
GLOSSARY = MANUSCRIPT / "glossary.md"
INDEX = MANUSCRIPT / "index.md"

NUMBERED = re.compile(r"^###\s+(\d+\.\d+)\s+(.*)$")
UNNUMBERED_H3 = re.compile(r"^###\s+(?![0-9])")
H2 = re.compile(r"^##\s")

CJK = re.compile(r"[\u3400-\u9fff\u3000-\u303f\uff00-\uffef]+")

# Terms a chapter lists that the glossary files under a slightly different
# headword. One entry per deliberate decision -- if this table grows, the
# chapters and the glossary have started to drift apart and the drift should
# be fixed rather than mapped.
ALIASES = {
    "umbrella activities": "umbrella activity",
}

# Irregular plurals the chapters actually use. Kept explicit rather than
# guessed at, because a stemmer that turned every "-is" into "-es" would
# match words nobody wrote and the index would start inventing references.
IRREGULAR = {
    "acceptance criterion": ("acceptance criteria",),
    "criterion": ("criteria",),
    "class": ("classes",),
    "process": ("processes",),
    "analysis": ("analyses",),
    "hypothesis": ("hypotheses",),
    "owner": ("ownership",),
}

# Alternative word forms a chapter uses in place of the glossary headword.
# These exist so the CITATION AUDIT can find the section that teaches a
# concept whose headword is a noun but whose chapter text uses the verb, or
# a slash-list headword that the chapter writes out with commas. They are
# deliberately NOT used when building the index: an index that equated
# `eliminate` with the entry `eliminate / simplify / parallelise / automate`
# would point the reader at every unrelated use of the word.
FORMS = {
    "classification": ("classify", "classifying", "classified"),
    "corrective / adaptive / perfective / preventive maintenance": (
        "corrective maintenance", "adaptive maintenance",
        "perfective maintenance", "preventive maintenance",
    ),
    "data / function / behaviour view": (
        "behaviour view", "data view", "function view", "three views",
    ),
    "decision node": ("decision diamond", "decision"),
    "eliminate / simplify / parallelise / automate": (
        "eliminate", "simplify", "parallelise", "automate",
    ),
    "empirical process control": ("empirical",),
    "entry / exit criteria": ("entry criteria", "exit criteria"),
    "factual / goal / resource conflict": (
        "factual conflict", "goal conflict", "resource conflict",
    ),
    "generalisation": ("generalise", "generalised", "generalising"),
    "merge node": ("merge",),
    "open / leading / closed question": (
        "open question", "leading question", "closed question",
    ),
    "ordering guarantee": ("ordering",),
    "transparency / inspection / adaptation": (
        "transparency", "inspection", "adaptation",
    ),
}


def strip_cjk(text: str) -> str:
    """Keep the English headword, drop the Chinese gloss.

    Cutting at the first CJK character is deliberate: the glosses are
    themselves slash- and hyphen-separated ("修正性/适应性/…", "状态-事件表"),
    so deleting CJK runs in place would leave their separators behind and
    produce a phantom headword like `moscow///`.
    """
    hit = CJK.search(text)
    return text[:hit.start()] if hit else text


def normalise(text: str) -> str:
    """Lowercase, drop punctuation noise, squeeze whitespace."""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("’", "'")
    text = re.sub(r"\s*/\s*", "/", text)
    text = re.sub(r"[^0-9a-z/'\- ]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


# Lookup is by NORMALISED key, and normalise() is what strips the spaces
# around the slashes -- so `transparency / inspection / adaptation` has to be
# filed under `transparency/inspection/adaptation` or the table never fires.
# Rebound here, after normalise() exists, rather than at the literal above.
ALIASES = {normalise(k): normalise(v) for k, v in ALIASES.items()}
FORMS = {normalise(k): v for k, v in FORMS.items()}


def read_chapters() -> dict[int, dict]:
    """Chapter number -> {text, sections: {id: text}, key_terms: [str]}."""
    out: dict[int, dict] = {}
    for path in sorted(glob.glob(str(MANUSCRIPT / "ch*.md"))):
        m = re.search(r"ch(\d+)\.md$", path)
        if not m:
            continue
        number = int(m.group(1))
        raw = pathlib.Path(path).read_text(encoding="utf-8")

        # Body without the authoring-aid figure list at the end.
        body = re.split(r"^##\s+Figure List", raw, flags=re.M)[0]

        sections: dict[str, list[str]] = {}
        titles: dict[str, str] = {}
        current = None
        for line in body.splitlines():
            hit = NUMBERED.match(line)
            if hit:
                current = hit.group(1)
                titles[current] = hit.group(2)
                sections.setdefault(current, [])
                continue
            if UNNUMBERED_H3.match(line) or H2.match(line):
                current = None  # Summary, References, AI Companion: not indexed
                continue
            if current:
                sections[current].append(line)

        terms: list[str] = []
        tm = re.search(r"\*\*Key terms:\*\*(.*?)(?=\n##\s|\n---|\Z)",
                       raw, flags=re.S)
        if tm:
            for item in tm.group(1).split("·"):
                item = item.strip()
                if item:
                    terms.append(normalise(strip_cjk(item)))

        out[number] = {
            "text": clean_markdown("\n".join(body.splitlines())),
            "sections": {
                k: clean_markdown("\n".join(v)) for k, v in sections.items()
            },
            "titles": titles,
            "key_terms": terms,
        }
    return out


def read_glossary() -> list[tuple[str, str, str]]:
    """[(headword_display, chinese_gloss, entry_body)] in file order.

    Entries are cut on a line that *starts* with `**Word`. Cutting at the
    line start rather than matching a whole entry in one regex is what makes
    this correct for wrapped entries: a long headword puts its Chinese gloss
    on the following line, and a single-line pattern would silently skip
    exactly the longest terms.
    """
    text = GLOSSARY.read_text(encoding="utf-8")
    # The body runs from the first letter section to the proper-name table;
    # that table is a name/role list, not a list of definitions.
    body = text.split("\n## Proper names", 1)[0]
    parts = body.split("\n## A\n", 1)
    body = parts[1] if len(parts) > 1 else ""

    entries: list[tuple[str, str, str]] = []
    for chunk in re.split(r"(?m)^(?=\*\*[A-Za-z])", body):
        if not chunk.startswith("**"):
            continue
        m = re.match(r"^\*\*([^*]+?)\*\*(.*)", chunk, flags=re.S)
        if not m:
            continue
        head = re.sub(r"\s+", " ", m.group(1)).strip()
        rest = m.group(2)
        dash = rest.find("\u2014")
        if dash == -1:
            continue
        # Everything between the headword and the dash IS the gloss, so keep
        # it whole: a findall over CJK runs would split `状态-事件表` into two
        # pieces, because the hyphen between them is not itself a CJK
        # character.
        chinese = re.sub(r"\s+", " ", rest[:dash]).strip()
        entries.append((head, chinese, rest[dash:]))
    return entries


def clean_markdown(text: str) -> str:
    """Drop inline emphasis markers before searching.

    Section 9.3 writes the frame as `` `alt` fragment ``, with the backticks
    inside the phrase. Searching the raw source would report that the book
    never discusses the alt fragment at all, when it discusses nothing else
    in that section. Hyphens are kept: `as-is` and `state-event` are words.
    """
    return re.sub(r"[`*_]", "", text)


def plural_of(phrase: str) -> str:
    """Pluralise the last word of a phrase, by English rules not by `+s`.

    Appending `s` blindly turns `umbrella activity` into `umbrella activitys`,
    which matches nothing — and the term is taught in a section whose heading
    is `Umbrella Activities`. A reference checker that cannot see the plural
    of the word it is checking reports false defects by the dozen.
    """
    head, _, last = phrase.rpartition(" ")
    if re.search(r"[^aeiou]y$", last):
        last = last[:-1] + "ies"
    elif re.search(r"(s|x|z|ch|sh)$", last):
        last = last + "es"
    else:
        last = last + "s"
    return f"{head} {last}".strip()


def pattern_for(needle: str, *, variants: bool = False) -> re.Pattern:
    """A whole-word pattern for `needle`, tolerant of plural forms.

    Plural tolerance is not cosmetic. Section 5.6 teaches the *acceptance
    criterion* and the body reads *acceptance criteria*; an exact match would
    report the term as never discussed and send the reader to the chapter
    heading instead of to the section that defines it.

    `variants=True` additionally accepts the FORMS table, which is what the
    citation audit needs and what the index must not use.
    """
    forms = {needle, plural_of(needle)}
    forms.update(IRREGULAR.get(needle, ()))
    if variants:
        forms.update(FORMS.get(needle, ()))
    body = "|".join(
        re.escape(f) for f in sorted(forms, key=len, reverse=True)
    )
    return re.compile(
        r"(?<![0-9A-Za-z])(?:" + body + r")(?![0-9A-Za-z])",
        re.IGNORECASE,
    )


def count_in(text: str, needle: str, *, variants: bool = False) -> int:
    return len(pattern_for(needle, variants=variants).findall(text))


# Index-only entries. The glossary answers "what does this word mean"; the
# index answers "where is it discussed". Proper names, identifier families
# and the chapter-level recurring features belong in the second and not the
# first. mode "chapters" scans the whole chapter; "sections" scans numbered
# sections only.
EXTRAS: list[tuple[str, str, str, str]] = [
    # (lookup key, display, chinese, mode)
    ("CareLink", "CareLink", "运行案例", "sections"),
    ("Grandma Lin", "Grandma Lin", "林奶奶", "sections"),
    ("Wei", "Wei", "魏（家属）", "sections"),
    ("Operator Yan", "Operator Yan", "严（护理中心操作员）", "sections"),
    ("Deng", "Deng", "邓（护理中心主管）", "sections"),
    ("Piotr", "Piotr", "彼得（开发人员）", "sections"),
    ("AI Companion", "AI Companion", "AI 协作环节", "chapters"),
    ("Running Project Task", "Running Project Task", "课程项目任务", "chapters"),
    ("alarm call", "alarm call", "告警呼叫", "sections"),
    ("escalation", "escalation", "逐级升级", "sections"),
    ("planning poker", "Planning Poker", "", "sections"),
]

ID_PATTERNS = [
    # The lookbehind matters: without it `R-001` also matches inside
    # `CR-001`, and the index would claim Chapter 4 introduced a requirement
    # identifier it never used.
    ("requirement", r"(?<![A-Za-z])R-0\d\d", "需求"),
    ("candidate requirement", r"(?<![A-Za-z])CR-0\d\d", "候选需求"),
    ("test case", r"(?<![A-Za-z])T-0\d\d", "测试用例"),
]


def build_index(chapters: dict[int, dict], glossary: list[tuple[str, str]]) -> str:
    def refs_sections(key: str) -> tuple[list[str], dict[str, int]]:
        counts: dict[str, int] = {}
        for number, data in chapters.items():
            for section, body in data["sections"].items():
                n = count_in(body, key)
                if n:
                    counts[section] = counts.get(section, 0) + n
        return sorted(counts, key=lambda s: [int(p) for p in s.split(".")]), counts

    def refs_chapters(key: str) -> list[int]:
        return sorted(
            n for n, d in chapters.items() if count_in(d["text"], key)
        )

    def titled(key: str, sections: list[str]) -> str | None:
        """The section whose HEADING names the term, if there is one.

        This is the only claim the index makes with emphasis, and it is a
        claim a reader can verify at a glance: the heading either contains
        the word or it does not. Choosing "the section that mentions it most"
        instead would confidently bold whichever chapter happened to repeat
        the word most often, which is not the same thing as teaching it.
        """
        hits = []
        for number, data in chapters.items():
            for section, title in data["titles"].items():
                if section in sections and pattern_for(key).search(title):
                    hits.append(section)
        if not hits:
            return None
        return sorted(hits, key=lambda s: [int(p) for p in s.split(".")])[0]

    def fmt(chapter_hint: int | None, sections: list[str],
            counts: dict[str, int], key: str = "") -> str:
        if sections:
            mark = titled(key, sections) if key else None
            shown = [
                f"**{s}**" if s == mark else s
                for s in sections[:6]
            ]
            if len(sections) > 6:
                shown.append(f"*+{len(sections) - 6} more*")
            return ", ".join(shown)
        if chapter_hint is not None:
            return f"Ch {chapter_hint}"
        return ""

    def runs_of(chs: list[int]) -> str:
        runs: list[str] = []
        start = prev = chs[0]
        for c in chs[1:]:
            if c == prev + 1:
                prev = c
                continue
            runs.append(f"{start}" if start == prev else f"{start}–{prev}")
            start = prev = c
        runs.append(f"{start}" if start == prev else f"{start}–{prev}")
        return ", ".join(runs)

    groups: dict[str, list[tuple[str, str, str]]] = {}

    for head, chinese, _ in glossary:
        key = ALIASES.get(normalise(head), normalise(head))
        sections, counts = refs_sections(key)
        hint = None
        if not sections:
            for n, d in chapters.items():
                if key in d["key_terms"]:
                    hint = n
                    break
        cell = fmt(hint, sections, counts, key)
        if not cell:
            continue
        letter = head[0].upper()
        letter = letter if letter.isalpha() else "#"
        groups.setdefault(letter, []).append((head, chinese, cell))

    for key, display, chinese, mode in EXTRAS:
        if mode == "chapters":
            chs = refs_chapters(key)
            if not chs:
                continue
            cell = "Ch " + runs_of(chs)
        else:
            sections, counts = refs_sections(key)
            cell = fmt(None, sections, counts, key)
        if not cell:
            continue
        letter = display[0].upper()
        groups.setdefault(letter, []).append((display, chinese, cell))

    for _, pattern, chinese in ID_PATTERNS:
        found: dict[str, list[int]] = {}
        for number, data in chapters.items():
            for ident in sorted(set(re.findall(pattern, data["text"]))):
                found.setdefault(ident, []).append(number)
        for ident in sorted(found):
            groups.setdefault("#", []).append(
                (ident, chinese, "Ch " + runs_of(found[ident]))
            )

    lines: list[str] = []
    lines.append("# Index")
    lines.append("")
    lines.append(
        "References are to **section numbers**, not page numbers. The "
        "manuscript has no pagination of its own -- Leanpub, PDF and DOCX "
        "each repaginate -- but `5.4` names the same section in all three, "
        "so a reference survives a change of format, of font or of edition."
    )
    lines.append("")
    lines.append(
        "A reference in **bold** is a section whose *heading* uses the term "
        "— the section that teaches it. Where no heading does, the "
        "references are given plain and unranked rather than guessed at. "
        "Identifiers beginning `R-` and `CR-` are requirements and `T-` are "
        "test cases; for those the reference is the chapter, because an "
        "identifier is introduced once and cited across chapters."
    )
    lines.append("")
    lines.append(
        "This index is generated from the chapter sources by "
        "`build/make-backmatter.py` and is never edited by hand. Regenerate "
        "it whenever a chapter is added or a section is renumbered."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    for letter in sorted(groups, key=lambda c: (c == "#", c)):
        lines.append(f"## {letter}")
        lines.append("")
        for display, chinese, cell in sorted(
            groups[letter], key=lambda t: t[0].lower()
        ):
            if chinese:
                lines.append(f"**{display}** {chinese} — {cell}")
            else:
                lines.append(f"**{display}** — {cell}")
            lines.append("")
        if lines[-1] == "":
            lines.pop()
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def check(chapters: dict[int, dict], glossary: list[tuple[str, str, str]]) -> int:
    have = {normalise(h) for h, _, _ in glossary}
    alias_targets = {normalise(v) for v in ALIASES.values()}

    introduced: dict[str, list[int]] = {}
    for number, data in chapters.items():
        for term in data["key_terms"]:
            introduced.setdefault(term, []).append(number)

    missing = {
        t: c for t, c in introduced.items()
        if ALIASES.get(t, t) not in have
    }
    unused = sorted(
        h for h, _, _ in glossary
        if normalise(h) not in introduced
        and normalise(h) not in alias_targets
    )

    print(f"chapters scanned : {len(chapters)}")
    print(f"glossary entries : {len(glossary)}")
    print(f"distinct key terms introduced by the chapters : {len(introduced)}")
    print()

    if missing:
        print(f"UNDEFINED — {len(missing)} term(s) a chapter introduces "
              f"but the glossary does not define:")
        for term in sorted(missing):
            print(f"  - {term}   (ch {', '.join(map(str, missing[term]))})")
    else:
        print("UNDEFINED — none. Every key term in every chapter is defined.")

    print()
    if unused:
        print(f"UNUSED — {len(unused)} glossary entry/entries no chapter "
              f"lists as a key term:")
        for term in unused:
            print(f"  - {term}")
        print("  (A term may legitimately sit here: it can be needed by a "
              "chapter not yet written, or be a cross-cutting word the "
              "glossary settles without a chapter claiming it.)")
    else:
        print("UNUSED — none.")

    return len(missing)


def audit_citations(chapters: dict[int, dict],
                    glossary: list[tuple[str, str, str]]) -> int:
    """Check that every reference a glossary entry makes is a true one.

    The glossary is a reference section, and a reference that points at the
    wrong section is worse than no reference: the reader goes there, does not
    find the word, and stops trusting the apparatus. The check is mechanical
    and the fix is mechanical, so there is no reason to leave it to memory.

    Two citation forms are legal. `§5.4` promises that Section 5.4 uses the
    term. `Ch 5` promises only that Chapter 5 introduces it — the honest form
    for a term a chapter primes in *Before You Read* and then names in its
    summary without ever using it in a numbered section.
    """
    # A heading counts as using the term: a section called "Umbrella
    # Activities" is where umbrella activities are taught, whether or not the
    # body repeats the phrase.
    searchable = {
        s: chapters[n]["titles"].get(s, "") + "\n" + body
        for n, d in chapters.items()
        for s, body in d["sections"].items()
    }

    def best_ref(key: str) -> str:
        ranked = sorted(
            searchable,
            key=lambda s: (-count_in(searchable[s], key, variants=True),
                           [int(p) for p in s.split(".")]),
        )[:3]
        return "  ".join(
            f"§{s}({count_in(searchable[s], key, variants=True)})"
            for s in ranked
        )

    bad = 0
    for head, _, body in glossary:
        key = ALIASES.get(normalise(head), normalise(head))
        sections = re.findall(r"§(\d+\.\d+)", body)
        chapters_cited = [int(c) for c in re.findall(r"\bCh\s+(\d+)", body)]

        for ref in sections:
            text = searchable.get(ref)
            if text is None or not pattern_for(key, variants=True).search(text):
                where = "does not exist" if text is None else "does not use the term"
                print(f"  {head}\n      §{ref} {where}   -> {best_ref(key)}")
                bad += 1

        for c in chapters_cited:
            data = chapters.get(c)
            if data is None or not count_in(data["text"], key, variants=True):
                print(f"  {head}\n      Ch {c} does not mention the term")
                bad += 1

        if not sections and not chapters_cited:
            print(f"  {head}\n      NO CITATION   -> {best_ref(key)}")
            bad += 1

    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true",
                       help="report glossary coverage instead of writing the index")
    group.add_argument("--audit", action="store_true",
                       help="verify every §-reference in the glossary")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero when a gap is found")
    args = ap.parse_args()

    chapters = read_chapters()
    glossary = read_glossary()
    if not chapters or not glossary:
        print("nothing to do: no chapters or no glossary found", file=sys.stderr)
        return 2

    if args.check:
        n = check(chapters, glossary)
        return 1 if (n and args.strict) else 0

    if args.audit:
        print(f"auditing {len(glossary)} glossary citations")
        bad = audit_citations(chapters, glossary)
        if bad == 0:
            print("ALL CLEAN — every cited section uses the term it is cited for.")
        else:
            print(f"\n{bad} citation(s) to fix.")
        return 1 if (bad and args.strict) else 0

    INDEX.write_text(build_index(chapters, glossary), encoding="utf-8")
    n_entries = sum(
        1 for ln in INDEX.read_text(encoding="utf-8").splitlines()
        if ln.startswith("**")
    )
    print(f"wrote {INDEX.relative_to(BOOK)} — {n_entries} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
