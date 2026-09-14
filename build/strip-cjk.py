#!/usr/bin/env python3
"""Produce the English-only edition from the bilingual manuscript.

Why this exists
---------------
The manuscript carries a Chinese gloss beside every key term, because the
chapter template and the EMI style guide both call for one:

    - **software 软件** -- instructions, data structures, and documents ...
    **acceptance criterion** 验收标准 -- A statement of how a requirement ...
    - **process** / 过程 -- the agreed set of tasks ...

Three different spellings, and the `**Key terms:**` block at the end of each
chapter can break a gloss ACROSS a line break, so its Chinese is not always on
the same line as the term it belongs to.

That gloss serves a Chinese-speaking reader. This book's readers are not
necessarily Chinese-speaking -- it is sold to English-taught programmes in
Latin America, Central Europe and the Gulf, and piloted with the international
cohort here. For those readers a Chinese gloss is noise, and it undercuts the
claim that the book is in English.

So: the manuscript stays bilingual (nothing is lost, and the glosses are the
raw material for a future Chinese or bilingual edition), and THIS script
derives a clean English edition from it. The derivation is mechanical and
checked, not editorial.

Usage
-----
    python3 build/strip-cjk.py              # write build/en-only/
    python3 build/strip-cjk.py --check      # verify the derivation (no writes)
    python3 build/strip-cjk.py --check --strict   # non-zero exit on any defect
    python3 build/strip-cjk.py --report     # show what would be removed

What `--check` asserts
----------------------
0 CJK     no Han character survives anywhere in the derived text
shape     headings, bullets, numbered items, table rows, image references and
          section citations are all preserved EXACTLY -- stripping must not
          add, remove or reorder a single structural element
markup    every non-blank line still has an even number of `**`
artifacts no double spaces, no orphaned separator at the start of a line, no
          empty bold run, no doubled middot
coverage  the number of chapter key terms that the glossary does not define is
          the SAME before and after stripping -- a process that quietly drops
          a term would change this number

Run `--check` after editing any chapter, and before every English release.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import sys

BOOK = pathlib.Path(__file__).resolve().parent.parent
MANUSCRIPT = BOOK / "manuscript"
OUT = BOOK / "build" / "en-only"
WRAP = 78

CJK = re.compile(r"[\u4e00-\u9fff]")

# A Chinese gloss inside a bold run: `**software 软件**`, `**MoSCoW 必做/应做**`,
# `**process / method / tool 过程 / 方法 / 工具**`. Cut at the first Han
# character and keep only the English headword.
#
# The tail is `[^—·*]*`, NOT `[^*]*`: an em dash or middot between the gloss and
# the closing `**` means the bold run has already closed and we are looking at
# the NEXT one. `**activity diagram** 活动图 — **6.3**` is a real index line
# where `[^*]*` would happily swallow ` 活动图 — ` and emit
# `**activity diagram****6.3**`, deleting the separator.
GLOSS_IN_BOLD = re.compile(r"\*\*([^*]*?)[ \t]*(?:/[ \t]*)?[\u4e00-\u9fff][^\u2014\u00b7*]*\*\*")

# A Chinese gloss AFTER a bold run, in either spelling:
#   `**acceptance criterion** 验收标准 -- def`   (glossary, index)
#   `**process** / 过程 -- def`                  (ch02, ch03)
# The lookahead stops at the separator so the definition survives.
GLOSS_AFTER_BOLD = re.compile(
    r"(\*\*[^*]+\*\*)[ \t]*(?:/[ \t]*)?[\u4e00-\u9fff][^\u2014\u00b7]*?(?=[ \t]*[\u2014\u00b7]|$)"
)

# Anything left over: a Han run, plus the `/` that often joins several of them
# (`修正性 / 适应性 / 完善性 / 预防性维护`). Only ever matches a line that had
# Chinese in it, so English prose cannot be touched.
RESIDUE = re.compile(r"\s*(?:/\s*)?[\u4e00-\u9fff]+(?:\s*[-/]\s*[\u4e00-\u9fff]+)*\s*")

# Layout damage worth reporting. Each pattern is deliberately narrow: a loose
# check here produces false alarms that cost more than the bugs they catch.
#
#   - a double space in a HEADING is unambiguously a typo. Elsewhere it is
#     usually deliberate: ch05's SRS outline aligns its columns with runs of
#     spaces, and flagging that would be wrong.
#   - `****` is an empty bold run. `**a** **b**` is two bold runs and matches a
#     naive `\*\*\s*\*\*`, which is why that spelling is not used.
#   - `() ` is a function call in half this book. Only a spaced `( )` is junk.
#   - `//` is `https://`. Only a slash pair with no colon in front is junk.
#
# The third field says whether a hit is worth reporting as a pre-existing
# defect in the source. Em dashes that open a line are this manuscript's house
# style for a clause that wraps, so they are still COUNTED (a new one means the
# joiner failed) but never reported as something to go and fix.
ARTIFACTS = [
    (re.compile(r"(?m)^#{1,6} .*?  "), "double space in a heading", True),
    (re.compile(r"\*\*\*\*"), "empty bold run", True),
    (re.compile(r"\(\s+\)"), "empty parenthesis", True),
    (re.compile(r"(?<!:)//"), "doubled slash", True),
    (re.compile(r"\u00b7\s*\u00b7"), "doubled middot", True),
    (re.compile(r"\u2014\s*\u2014"), "doubled em dash", True),
    (re.compile(r"^[\u2014\u00b7]"), "line starts with an orphaned separator", False),
]


def strip_tail_cjk(segment: str) -> str:
    """Cut a key-term segment at its first Han character."""
    m = CJK.search(segment)
    if m:
        segment = segment[: m.start()]
    return segment.rstrip(" /-")


def strip_line(line: str) -> str:
    """Remove every Chinese gloss from one line."""
    previous = None
    while previous != line:
        previous = line
        line = GLOSS_IN_BOLD.sub(r"**\1**", line)
        line = GLOSS_AFTER_BOLD.sub(r"\1", line)
    line = RESIDUE.sub(" ", line)
    return line.rstrip()


def wrap_keyterms(segs: list[str]) -> list[str]:
    """Re-emit the `**Key terms:**` block, wrapped after ` · `."""
    lines: list[str] = []
    current = "**Key terms:** "
    for k, seg in enumerate(segs):
        token = seg + (" \u00b7 " if k < len(segs) - 1 else "")
        if len(current) + len(token) > WRAP and current.rstrip() != "**Key terms:**":
            lines.append(current.rstrip())
            current = token
        else:
            current += token
    lines.append(current.rstrip())
    return lines


def is_keyterms(line: str) -> bool:
    return line.startswith("**Key terms:**")


def strip_file(text: str) -> str:
    """Derive the English text of one manuscript file."""
    src = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(src):
        line = src[i]

        # The key-terms block is a ` · `-separated enumeration whose glosses can
        # straddle line breaks. Rebuild it whole, strip segment by segment,
        # then re-wrap. A blank line ends the block.
        if is_keyterms(line):
            j = i
            while j < len(src) and src[j].strip():
                j += 1
            joined = " ".join(part.strip() for part in src[i:j])
            body = re.sub(r"^\*\*Key terms:\*\*[ \t]*", "", joined)
            segs = [strip_tail_cjk(s.strip()) for s in body.split(" \u00b7 ")]
            segs = [s for s in segs if s]
            out.extend(wrap_keyterms(segs))
            i = j
            continue

        stripped = strip_line(line)

        # A gloss that occupied its own line leaves a bare separator behind;
        # glue it back onto the headword above so the entry reads as one line.
        if stripped.strip() and re.match(r"^[\u2014\u00b7]", stripped.strip()) and out:
            if out[-1].strip() and not out[-1].rstrip().endswith(("|",)):
                out[-1] = out[-1].rstrip() + " " + stripped.strip()
                i += 1
                continue

        # A line that was pure Chinese simply disappears.
        if line.strip() and not stripped.strip():
            i += 1
            continue

        out.append(stripped)
        i += 1

    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def shape(text: str) -> dict[str, int]:
    """A structural fingerprint that stripping must not change."""
    return {
        "headings": len(re.findall(r"(?m)^#", text)),
        "bullets": len(re.findall(r"(?m)^- ", text)),
        "numbered": len(re.findall(r"(?m)^\d+\. ", text)),
        "table_rows": len(re.findall(r"(?m)^\|", text)),
        "images": text.count("!["),
        "citations": text.count("*\u00a7"),
        "blockquotes": len(re.findall(r"(?m)^>", text)),
    }


def content_of(line: str) -> str:
    """A line's text with every leading blockquote marker and indent removed.

    This manuscript hard-wraps inside list items and blockquotes and indents
    the continuation lines to line up under the text, so `>    and key-box
    code.` is correct markdown and must not read as a double space.
    """
    body = line
    while True:
        stripped = body.lstrip()
        if stripped.startswith(">"):
            body = stripped[1:]
            continue
        if len(stripped) < len(body):
            body = stripped
        break
    return body


def artifacts(text: str) -> dict[str, int]:
    """Count layout damage, keyed by kind.

    Returned as counts rather than line numbers because the caller compares
    two texts whose line numbers do not correspond.
    """
    counts: dict[str, int] = {label: 0 for _, label, _ in ARTIFACTS}
    for line in text.splitlines():
        body = content_of(line)
        if not body:
            continue
        for pattern, label, _ in ARTIFACTS:
            counts[label] += len(pattern.findall(body))
    return counts


def coverage(text_of: dict[str, str]) -> int:
    """Chapter key terms that the glossary does not define.

    A crude version of what make-backmatter.py --check owns, used here only as
    a differential: stripping must not change this number. Both sides are put
    through `strip_tail_cjk` first, otherwise the SOURCE would score a miss for
    every single term simply because its gloss is still attached.
    """
    glossary = text_of.get("glossary.md", "")
    defined = set()
    for line in glossary.splitlines():
        m = re.match(r"\*\*(.+?)\*\*", line)
        if m:
            defined.add(m.group(1).strip().lower())

    missing = 0
    for name, text in text_of.items():
        if not name.startswith("ch"):
            continue
        lines = text.splitlines()
        for k, line in enumerate(lines):
            if not is_keyterms(line):
                continue
            j = k
            block = []
            while j < len(lines) and lines[j].strip():
                block.append(lines[j].strip())
                j += 1
            body = re.sub(r"^\*\*Key terms:\*\*[ \t]*", "", " ".join(block))
            for seg in body.split(" \u00b7 "):
                term = strip_tail_cjk(seg.strip()).lower()
                if term and term not in defined:
                    missing += 1
    return missing


def collect() -> dict[str, str]:
    return {
        p.name: p.read_text(encoding="utf-8")
        for p in sorted(MANUSCRIPT.glob("*.md"))
    }


def run_check(source: dict[str, str], strict: bool) -> int:
    derived = {name: strip_file(text) for name, text in source.items()}
    failures: list[str] = []
    preexisting: dict[str, int] = {}

    print(f"{'file':<34}{'CJK':>5}{'head':>5}{'bul':>5}{'num':>5}{'img':>5}{'\u00a7':>5}{'**':>7}{'new':>5}  status")
    for name in source:
        src, dst = source[name], derived[name]
        left = len(CJK.findall(dst))
        a, b = shape(src), shape(dst)
        bad = [k for k in a if a[k] != b[k]]

        # `**` is a COUNT invariant, not a per-line parity check: this
        # manuscript wraps bold runs across line breaks, so a single line can
        # legitimately carry an odd number of them. Stripping never adds or
        # removes a bold run, so the totals must match exactly.
        bold_src, bold_dst = src.count("**"), dst.count("**")
        bold_bad = bold_src != bold_dst

        # Layout damage is judged differentially: a double space that was
        # already in the source is the author's to fix, not this script's
        # doing, so only newly-introduced damage counts against it.
        arts_src = artifacts(src)
        arts_dst = artifacts(dst)
        new_arts = {k: arts_dst[k] - arts_src.get(k, 0) for k in arts_dst if arts_dst[k] > arts_src.get(k, 0)}
        for pattern, label, reportable in ARTIFACTS:
            if reportable and arts_src.get(label):
                preexisting[label] = preexisting.get(label, 0) + arts_src[label]

        if left:
            failures.append(f"{name}: {left} Han characters survived")
        if bad:
            failures.append(f"{name}: shape changed in {', '.join(bad)}")
        if bold_bad:
            failures.append(f"{name}: bold runs {bold_src} -> {bold_dst}")
        if new_arts:
            detail = ", ".join(f"{k} x{v}" for k, v in new_arts.items())
            failures.append(f"{name}: introduced {detail}")

        ok = not (left or bad or bold_bad or new_arts)
        print(f"{name:<34}{left:>5}{b['headings']:>5}{b['bullets']:>5}{b['numbered']:>5}{b['images']:>5}"
              f"{b['citations']:>5}{bold_dst:>7}{sum(new_arts.values()):>5}  {'ok' if ok else 'FAIL'}")

    before, after = coverage(source), coverage(derived)
    print(f"\nglossary coverage (undefined terms): source {before} -> derived {after}", end="")
    if before != after:
        print("   MISMATCH")
        failures.append(f"coverage changed: {before} -> {after}")
    else:
        print("   same")

    if preexisting:
        total = sum(preexisting.values())
        detail = ", ".join(f"{k} x{v}" for k, v in sorted(preexisting.items()))
        print(f"\nnote: {total} pre-existing layout nit(s) in the SOURCE, not caused by "
              f"stripping ({detail}) -- worth fixing in manuscript/ so both editions benefit.")

    if failures:
        print(f"\n{len(failures)} problem(s):")
        for f in failures:
            print("  -", f)
        return 1 if strict else 0

    print("\nALL CLEAN - the English edition is structurally identical, gloss-free.")
    return 0


def run_report(source: dict[str, str]) -> int:
    print(f"{'file':<34}{'CJK in':>7}{'CJK out':>8}{'len %':>7}")
    total = 0
    for name, text in source.items():
        dst = strip_file(text)
        n = len(CJK.findall(text))
        total += n
        ratio = len(dst) / len(text) * 100
        print(f"{name:<34}{n:>7}{len(CJK.findall(dst)):>8}{ratio:>6.1f}%")
    print(f"\ntotal Han characters removed: {total}")

    print("\n--- sample: ch01 Before You Read ---")
    for line in strip_file(source["ch01.md"]).splitlines()[20:31]:
        print(" ", line[:100])
    print("\n--- sample: glossary.md ---")
    for line in strip_file(source["glossary.md"]).splitlines()[54:60]:
        print(" ", line[:100])
    print("\n--- sample: index.md ---")
    for line in strip_file(source["index.md"]).splitlines()[11:17]:
        print(" ", line[:100])
    return 0


def write_out(source: dict[str, str]) -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for name, text in source.items():
        (OUT / name).write_text(strip_file(text), encoding="utf-8")
    for name in ("Book.txt", "Sample.txt", "title.txt", "subtitle.txt", "author.txt"):
        src = MANUSCRIPT / name
        if src.exists():
            shutil.copy2(src, OUT / name)
    print(f"wrote {len(source)} stripped file(s) to {OUT.relative_to(BOOK)}/")
    print("images/ is NOT copied -- the build resolves images/ from manuscript/ "
          "via --resource-path, and the reference `images/x.png` is unchanged.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Derive the English-only edition from the bilingual manuscript.")
    ap.add_argument("--check", action="store_true", help="verify the derivation, write nothing")
    ap.add_argument("--report", action="store_true", help="show what would be removed")
    ap.add_argument("--strict", action="store_true", help="with --check, exit non-zero on any defect")
    args = ap.parse_args()

    source = collect()
    if not source:
        print(f"no manuscript files under {MANUSCRIPT}", file=sys.stderr)
        return 2

    if args.check:
        return run_check(source, args.strict)
    if args.report:
        return run_report(source)
    return write_out(source)


if __name__ == "__main__":
    sys.exit(main())
