# Figure System — making this a genuinely illustrated book

> 图文并茂不是"多放几张图"，而是**每章的图构成一个可复用的视觉体系**。
> Version 1.0 (2026-09-08) · Applies to: all 20 chapters

---

## 1. Target and current gap

| Metric | Target | Current (Ch 1–3) | Gap |
|---|---|---|---|
| Figures per chapter | **9** (min 8) | 3 | −6 per chapter |
| Whole book (20 ch) | **180–200** | 9 | ~170 to produce |
| Figure types used per chapter | ≥4 of 7 | 2 | upgrade |
| AI-related figures | ≥1 per chapter | 0 | new |
| Colour / B&W safe | all | unknown | audit needed |

**Reality check 现实判断**: 170 figures is the single largest remaining task.
At ~6 finished figures per week it is ~7 months of calendar time *unless*
production is batched by type (see §5).

---

## 2. The seven figure types (and the per-chapter mix)

| # | Type | Used for | Per chapter |
|---|---|---|---|
| T1 | **Concept map 概念关系图** | how ideas relate | 1–2 |
| T2 | **Process / lifecycle 流程与生命周期** | steps, phases, iterations | 1–2 |
| T3 | **Model diagram 模型图** | UML: use case, class, sequence, state, activity | 2–3 |
| T4 | **Before / after 对照图** | pitfall vs corrected artifact | 1 |
| T5 | **UI sketch 界面草图** | screens, wireframes, storyboards | 0–2 (design chapters) |
| T6 | **Data & table figure 数据图** | estimates, burndown, metric tables | 1 |
| T7 | **AI workflow AI 工作流** | human → AI → verify → artifact | ≥1 |

Rule: **no two consecutive pages without something visual** — a figure, a table,
a code listing, or a checklist box. Prose-only stretches must stay under 1.5 pages.

---

## 3. Visual language (so 180 figures still look like one book)

- **Canvas**: SVG source, 1200 × 675 (16:9) or 1200 × 900 (4:3); exported PNG at 2× for print.
- **Palette** (colour-blind safe, print-safe):
  - ink `#1F3864` (primary), accent blue `#2E74B5`, fill `#DCE8F4`
  - warn orange `#E87A2E`, ok green `#2E7D46`, alert red `#B3261E`
  - neutral greys `#F5F6F7 / #C9D4E2 / #6B7280`
  - **AI elements: violet `#6D3FA8`** — reserved, used nowhere else
- **Type**: one sans family (Calibri / Inter), title 24–28 pt, body 14–16 pt,
  minimum 12 pt at final size.
- **Rules**: 1 px borders, 8 pt grid, rounded corners 6 pt, no drop shadows,
  no 3-D, no clip art, no stock photos of people.
- **Every figure carries**: number, caption (one sentence, informative not
  descriptive), and **alt text** (for accessible PDF/EPUB).

---

## 4. Naming & storage

```
figures/
  svg/ch04-fig4-1-stakeholder-map.svg     ← source of truth
  png/ch04-fig4-1-stakeholder-map.png     ← build output (2×)
  README.md                               ← index: number, caption, type, alt text
```
Numbering: `chNN-figN-M-topic` where N = chapter number, M = sequence in chapter.

---

## 5. Production strategy (how 170 figures get made)

1. **Batch by type, not by chapter.** Produce all T2 lifecycle figures first,
   then all T3 model figures for Part II, etc. Style stays consistent and speed rises.
2. **Author draws, tool renders.** Write the figure as SVG (text → versionable →
   diff-able in Git), render PNG with a headless renderer; never hand-draw bitmaps.
3. **Reuse the case.** CareLink artifacts cascade: the domain model of Ch 9 becomes
   the class diagram of Ch 13 becomes the test fixture of Ch 16 — draw the *variation*,
   not a new picture each time.
4. **Student-sourced (optional).** With permission, adapted student artifacts make
   excellent *Before / After* (T4) figures — and double as adoption evidence.
5. **Colour → B&W audit**: every figure must survive grey-scale. Use position and
   line weight for meaning, colour only for emphasis.

---

## 6. Per-chapter figure plan (fill in before writing the chapter)

```markdown
| # | Type | Caption | Alt text |
|---|---|---|---|
| 4-1 | T1 | Stakeholder map for CareLink | … |
| 4-2 | T2 | Elicitation cycle | … |
| 4-3 | T3 | Use case diagram (draft) | … |
| 4-4 | T3 | Use case description template | … |
| 4-5 | T4 | Vague vs testable requirement | … |
| 4-6 | T6 | Requirements traceability matrix | … |
| 4-7 | T7 | AI-assisted transcript analysis with verification | … |
| 4-8 | T1 | Glossary concept links | … |
| 4-9 | T5 | Interview scheduling screen (CareLink) | … |
```
A chapter without a filled plan is not ready to write.
