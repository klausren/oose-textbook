# Figure Style Guide 插图规范

All figures in this book follow one visual system so that 20 chapters read as
one coherent artifact. Source of truth: the SVG files in `figures/svg/`,
rendered to PNG by `figures/render.js`.

## Palette 配色

| Role | Hex | Used for |
|---|---|---|
| Ink (text/axes) | `#1F2937` | All primary text, axes, borders |
| Gray (secondary) | `#6B7280` | Axis labels, annotations, muted text |
| Blue (primary) | `#2563EB` | The "main" curve/box of a figure |
| Blue fill | `#DBEAFE` | Primary box backgrounds |
| Teal (secondary actor) | `#0D9488` / fill `#CCFBF1` | Second key element (e.g., family app) |
| Amber (caution/human) | `#D97706` / fill `#FEF3C7` | Human actors, warnings, care center |
| Red (danger) | `#DC2626` / fill `#FEE2E2` | Failure, escalation, defects |
| Canvas | `#FFFFFF` | Background — never dark backgrounds |

## Typography 排版

- Font: **Arial** (rendered via system font file; safe in Word/print).
- **Hard floor: no `<text>` smaller than 11.5 units.** Measured across all 63
  figures — the current distribution is 11.5 (47), 12 (7), 13 (6), 13.5–15 (3).
- Panel titles 18–20; box/card titles 13.5–15 bold; body and annotations 11.5–12.
- Text in figures is **English only** (Chinese key terms stay in body text).
- All labels use `text-anchor` centering; never rely on manual spacing.

### Why 11.5 is the floor 字号下限的来历

Figures are placed at `{width=15cm}` in the manuscript, so printed type size is

    printed_pt  =  15 cm x font_size / viewBox_width  x  28.35 pt/cm

At a 760-unit canvas, 11.5 units prints at **6.4 pt** — the low end of what is
acceptable in a textbook. Two consequences follow, and both are enforced:

1. **Do not add text to a figure until you have checked what it costs.** Adding a
   fourth bullet to a card either shrinks the type or overflows the box.
2. **Cropping the canvas is a free type-size increase.** A narrower `viewBox`
   at the same font-size prints bigger. Two figures are wired the same way only
   if they are cropped the same way — see below.

## Legibility standard 可读性标准

Seven defect classes have shipped in this book at least once. `figures/qc.py`
checks all of them, on every figure, in one command:

```sh
python3 figures/qc.py          # exit 0 = clean, exit 1 = findings
```

| # | Check | Rule | Why it shipped before |
|---|---|---|---|
| 1 | `overflow` | text must fit its containing box (±3 units padding) | a widened label silently ran past the card edge |
| 2 | `gap` | two labels on one baseline need ≥ 6 units between them | `Customer`/`Developer` column heads touched |
| 3 | `overlap` | no two label boxes may intersect | same bug, worse |
| 4 | `leading` | stacked baselines ≥ 1.12 x font-size apart | 11.5 px type on 12-unit leading read as one smudge |
| 5 | `duplicate` | no string drawn twice at the same spot | ghost text (`font-size="0.1"` white, and a doubled row) |
| 6 | `margin` | ink ≥ 6 units from the canvas edge | a crop clipped the "Chapter 4" tab |
| 7 | `tiny` | no font-size below 11.5 | 48 of 63 figures were under 12 before this was enforced |

The checker measures real Arial advance widths through PIL rather than estimating
characters x 0.55, so its numbers match what the renderer actually draws.
**Run it after every SVG edit, before `render.js` is considered done.**

## Canvas fitting 画布贴合

`svg/` viewBoxes are fitted to the real ink bounding box (measured from the
rendered PNG, not from the source coordinates) plus **16 units of padding**,
with a **620-unit floor on width**. The floor keeps a narrow diagram from being
blown up 2.9x and printing at a size no other figure uses.

Re-fit after any content change — it is what keeps an 8-word figure from
occupying a full page:

```sh
# dry run first, then --apply; back up svg/ before applying
python3 figures/fitvbox.py --apply
python3 figures/qc.py && node figures/render.js && bash build/sync-figures.sh
```

If a figure genuinely cannot fit its text, **cut text, do not shrink type**.

## Canvas & rendering 画布与渲染

- SVG `viewBox` width: **760 units** (≈ two-column figure); height per content.
- Rendered to PNG at **2400 px wide** (crisp in docx and PDF at 300 dpi).
- Lines ≥ 3 px; rounded corners (rx 8–12); 2–3 px gaps between stacked shapes.
- Arrowheads: explicit-fill markers, one per color (never `context-stroke`).

## Naming & captions 命名与图题

- Files: `chNN-figN-M-slug.png` (source `.svg` keeps the same stem).
- Captions live **in the manuscript, not inside the image**:

  ```markdown
  ![Alt text](images/chNN-figN-M-slug.png){width=15cm}

  *Fig. N-M. One-sentence English caption.*
  ```

- Every figure must be **referenced in body text** before it appears.
- Budget: **9 figures per chapter** (minimum 8) — see the per-chapter figure
  plan in `figures/PLAN-part2-requirements.md` and `templates/figure-system.md`.
- Path rule: chapter sources reference `images/...`, because that single path
  works for both pandoc and Leanpub. Run `build/sync-figures.sh` after
  rendering so `manuscript/images/` stays in sync with this folder.

## Canonical figure types 七类标准图

Type codes follow `templates/figure-system.md` §2:

| # | Type | Used for |
|---|---|---|
| T1 | Concept map | how ideas relate |
| T2 | Process / lifecycle | steps, phases, iterations |
| T3 | Model diagram | UML: use case, class, sequence, state, activity |
| T4 | Before / after | pitfall versus corrected artifact |
| T5 | UI sketch | screens, wireframes, storyboards |
| T6 | Data & table | estimates, matrices, metric tables |
| T7 | **AI workflow** | human → AI → verify → artifact (violet `#6D3FA8`) |

Every chapter carries **exactly one T7** and **at least one T4**.

## Re-render after editing SVG

```zsh
NODE="/Users/renzheng/.workbuddy/binaries/node/versions/$(cat /Users/renzheng/.workbuddy/binaries/node/versions/current)/bin/node"
NODE_PATH=/Users/renzheng/.workbuddy/binaries/node/workspace/node_modules \
  "$NODE" figures/render.js
```

`versions/current` is a plain text file holding the version string, not a symlink —
hence the `$(cat ...)`. Do not pin a version number: the managed runtime is replaced
on upgrade and a pinned path silently disappears.

## Figure index 图索引

### Chapter 1 — Software and Software Engineering
| # | Type | File | Caption |
|---|---|---|---|
| 1-1 | T6 | `ch01-fig1-1-failure-curves` | Hardware bathtub curve versus software deterioration curve |
| 1-2 | T1 | `ch01-fig1-2-layered-technology` | The three essentials of software engineering |
| 1-3 | T3 | `ch01-fig1-3-carelink-context` | CareLink system context diagram |
| 1-4 | T1 | `ch01-fig1-4-product-anatomy` | Programs, data and documents; generic versus customized products |
| 1-5 | T2 | `ch01-fig1-5-crisis-timeline` | From the 1968 software crisis to AI-assisted engineering |
| 1-6 | T4 | `ch01-fig1-6-program-vs-product` | A program that works versus a product that ships |
| 1-7 | T6 | `ch01-fig1-7-four-changes` | The four kinds of change and where maintenance effort goes |
| 1-8 | T2 | `ch01-fig1-8-framework-activities` | The five framework activities under the umbrella activities |
| 1-9 | T7 | `ch01-fig1-9-ai-classification` | AI-assisted classification, with a verification step |

### Chapter 2 — Software Process Models
| # | Type | File | Caption |
|---|---|---|---|
| 2-1 | T2 | `ch02-fig2-1-waterfall` | The waterfall model: five sequential phases |
| 2-2 | T2 | `ch02-fig2-2-incremental` | The incremental model: three full-process passes |
| 2-3 | T2 | `ch02-fig2-3-spiral` | The spiral model: four quadrants per loop |
| 2-4 | T1 | `ch02-fig2-4-process-vocabulary` | Process model, framework activity and process frame |
| 2-5 | T2 | `ch02-fig2-5-v-model` | The V model and its artefact-to-test pairings |
| 2-6 | T2 | `ch02-fig2-6-prototyping` | The prototyping loop and the two roads out of it |
| 2-7 | T6 | `ch02-fig2-7-model-selection` | Choosing a model: fit, cost and verdict |
| 2-8 | T4 | `ch02-fig2-8-one-project-two-models` | One project under waterfall and under incremental |
| 2-9 | T7 | `ch02-fig2-9-ai-model-selection` | AI-assisted process selection, with ceremony costing |

### Chapter 3 — Agile Development and Scrum
| # | Type | File | Caption |
|---|---|---|---|
| 3-1 | T1 | `ch03-fig3-1-manifesto` | The four values of the Agile Manifesto |
| 3-2 | T2 | `ch03-fig3-2-sprint-cycle` | The Scrum sprint cycle |
| 3-3 | T6 | `ch03-fig3-3-burndown` | A sprint burndown chart: ideal versus actual |
| 3-4 | T1 | `ch03-fig3-4-values-principles-practices` | Values, principles and practices as three levels |
| 3-5 | T2 | `ch03-fig3-5-three-artifacts` | The three Scrum artefacts inside one sprint |
| 3-6 | T5 | `ch03-fig3-6-sprint-board` | The sprint board on day 6 |
| 3-7 | T6 | `ch03-fig3-7-velocity` | Velocity across six sprints against the average |
| 3-8 | T4 | `ch03-fig3-8-theatre-vs-agility` | Agile theatre versus real agility |
| 3-9 | T7 | `ch03-fig3-9-ai-backlog-refinement` | AI-assisted backlog refinement, with grounding |

### Chapter 4 — Requirements Inception and Elicitation
| # | Type | File | Caption |
|---|---|---|---|
| 4-1 | T1 | `ch04-fig4-1-requirements-landscape` | The requirements landscape: six activities, with management beneath |
| 4-2 | T2 | `ch04-fig4-2-elicitation-cycle` | The elicitation cycle: prepare, ask, listen, record, confirm, repeat |
| 4-3 | T1 | `ch04-fig4-3-stakeholder-map` | Stakeholder map for CareLink: served, operated, constrained |
| 4-4 | T2 | `ch04-fig4-4-interview-arc` | The interview arc: warm-up, context, problems, wish list, wrap-up |
| 4-5 | T4 | `ch04-fig4-5-three-questions` | The same request asked three ways: closed, leading, open |
| 4-6 | T4 | `ch04-fig4-6-vague-vs-testable` | Vague requirement versus testable requirement |
| 4-7 | T6 | `ch04-fig4-7-stakeholder-grid` | Stakeholder influence and interest grid for CareLink |
| 4-8 | T7 | `ch04-fig4-8-ai-transcript-analysis` | AI-assisted interview transcript analysis, with verification |
| 4-9 | T1 | `ch04-fig4-9-statement-to-requirement` | From raw stakeholder statement to a numbered requirement |

### Chapter 5 — Requirements Analysis and Specification
| # | Type | File | Caption |
|---|---|---|---|
| 5-1 | T1 | `ch05-fig5-1-analysis-views` | The analysis model and its three views |
| 5-2 | T2 | `ch05-fig5-2-analysis-pipeline` | From raw candidates to a checked requirement set |
| 5-3 | T4 | `ch05-fig5-3-overspecified-vs-correct` | Over-specified versus correctly specified requirement |
| 5-4 | T3 | `ch05-fig5-4-srs-outline` | Structured specification outline, with its three readers |
| 5-5 | T6 | `ch05-fig5-5-moscow` | MoSCoW for CareLink's first release |
| 5-6 | T4 | `ch05-fig5-6-vague-vs-bounded` | Unmeasurable words versus a bounded requirement |
| 5-7 | T2 | `ch05-fig5-7-negotiation-loop` | The requirements negotiation loop |
| 5-8 | T7 | `ch05-fig5-8-ai-requirement-rewrite` | AI-assisted requirement rewriting, with a meaning check |
| 5-9 | T5 | `ch05-fig5-9-need-intake-form` | CareLink need-intake form |


### Chapter 6 — Business Process Modelling
| # | Type | File | Caption |
|---|---|---|---|
| 6-1 | T1 | `ch06-fig6-1-why-model-process` | Why model the business before the software |
| 6-2 | T2 | `ch06-fig6-2-as-is-to-be-gap` | As-is, to-be, and the gap between them |
| 6-3 | T3 | `ch06-fig6-3-as-is-alarm-call` | CareLink as-is: how an alarm call is handled today |
| 6-4 | T3 | `ch06-fig6-4-to-be-alarm-call` | CareLink to-be: the same call with the system |
| 6-5 | T3 | `ch06-fig6-5-swimlane-alarm-call` | Swimlane view across elder, care centre and caregiver |
| 6-6 | T4 | `ch06-fig6-6-evidence-labels` | Documented process versus observed process, with evidence labels |
| 6-7 | T6 | `ch06-fig6-7-cycle-time-table` | Cycle-time table: as-is versus to-be |
| 6-8 | T7 | `ch06-fig6-8-ai-process-extraction` | AI-assisted process extraction from policy documents |
| 6-9 | T1 | `ch06-fig6-9-process-vs-requirements` | Process model and specification: what each answers |


### Chapter 7 — Use Case Modelling
| # | Type | File | Caption |
|---|---|---|---|
| 7-1 | T3 | `ch07-fig7-1-usecase-diagram-carelink` | CareLink use case diagram: eleven goals, four actors |
| 7-2 | T4 | `ch07-fig7-2-goal-vs-feature` | Use case versus function: the same feature described both ways |
| 7-3 | T3 | `ch07-fig7-3-usecase-anatomy` | The anatomy of a use case diagram |
| 7-4 | T3 | `ch07-fig7-4-usecase-description` | The description template, filled for Acknowledge an alert |
| 7-5 | T2 | `ch07-fig7-5-usecase-workflow` | Writing a use case: four steps and what each prevents |
| 7-6 | T3 | `ch07-fig7-6-include-and-extend` | Include and extend on one base case |
| 7-7 | T4 | `ch07-fig7-7-feature-vs-goal-sorting` | The same work sorted by feature and by actor goal |
| 7-8 | T7 | `ch07-fig7-8-ai-usecase-drafting` | AI-assisted use case drafting, with verification |
| 7-9 | T5 | `ch07-fig7-9-alarm-screen-wireframe` | CareLink alarm screen, used as a use case prop |

### Chapter 8 — Domain Modelling
| # | Type | File | Caption |
|---|---|---|---|
| 8-1 | T1 | `ch08-fig8-1-three-artefacts` | Domain model, design class diagram and database schema: three different artefacts |
| 8-2 | T2 | `ch08-fig8-2-noun-to-concept` | Finding concepts: collect noun phrases, discard five families, then name |
| 8-3 | T3 | `ch08-fig8-3-domain-model-first-pass` | CareLink domain model, first pass: thirteen concepts, no attributes |
| 8-4 | T3 | `ch08-fig8-4-domain-model-refined` | CareLink domain model with attributes, multiplicities and named ends |
| 8-5 | T4 | `ch08-fig8-5-attribute-vs-concept` | Attribute mistaken for a concept: the key-box code |
| 8-6 | T3 | `ch08-fig8-6-association-class` | Association classes and why CareLink needs one |
| 8-7 | T1 | `ch08-fig8-7-usecases-to-concepts` | The domain model links back to the use case list |
| 8-8 | T7 | `ch08-fig8-8-ai-concept-extraction` | AI-assisted concept extraction, with verification |
| 8-9 | T6 | `ch08-fig8-9-concept-inventory` | Concept inventory: name, evidence, verdict |

### Chapter 9 — Behavioural Modelling
| # | Type | File | Caption |
|---|---|---|---|
| 9-1 | T1 | `ch09-fig9-1-three-models-three-questions` | Which behavioural model answers which question |
| 9-2 | T3 | `ch09-fig9-2-sequence-alarm-escalation` | CareLink sequence diagram for the alarm-escalation scenario |
| 9-3 | T3 | `ch09-fig9-3-state-machine-alert` | CareLink state machine for the alert object |
| 9-4 | T3 | `ch09-fig9-4-activity-shift-handover` | CareLink activity diagram for the caregiver shift hand-over |
| 9-5 | T4 | `ch09-fig9-5-missing-alternative` | Before and after: the same sequence diagram with a missing alternative path |
| 9-6 | T3 | `ch09-fig9-6-scenario-to-message` | Traceability from the scenario narration to the messages |
| 9-7 | T6 | `ch09-fig9-7-state-event-table` | State-event table for the alert object |
| 9-8 | T7 | `ch09-fig9-8-ai-behavioural-draft` | AI-assisted behavioural model drafting, with verification |
| 9-9 | T2 | `ch09-fig9-9-choosing-a-model` | Choosing a behavioural model: four questions, in order |

**Running total: 81 figures.** Chapters 1–9 are all at quota (9 each).
Type coverage per chapter: ≥4 of 7, with exactly one T7 and at least one T4.
Next batch: Chapter 9, Behavioural Modelling (see `PLAN-part2-requirements.md`).

### Regenerating a chapter's figures
Chapter 8's nine figures are produced by three scripts under `figures/gen/`
(`common.py` holds the palette and the layout assertions, `figs_cards.py` the
four comparison/table figures, `figs_flow.py` the two diagrams and the AI
workflow, `figs_model.py` the two domain-model diagrams with its layout
solver). Figure 8-3's node placement is **solved**, not hand-placed: nodes are
assigned to distinct slots of an aligned grid and the assignment is improved by
swapping slots while a cost function watches line crossings,
line-through-box and total line length. Re-run the flow
(generate → `fitvbox.py --apply` → `qc.py` → `render.js`) after any edit.

Chapter 9's nine figures all come from one script, `figures/gen/figs_behaviour.py`
(`python3 figures/gen/figs_behaviour.py` regenerates all nine;
`python3 figures/gen/figs_behaviour.py 9_4` regenerates one). The two diagrams
whose numbers the chapter argues about — nine messages and thirty-six cells —
are asserted inside the script, so a drift between the prose and the picture
fails the build rather than reaching the page.
