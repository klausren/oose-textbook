# Part II Figure Plan — Requirements Engineering (Ch 4–10)

> Per `templates/figure-system.md` §6: *a chapter without a filled plan is not
> ready to write.* This file is the plan for the seven chapters of Part II.
> Fill order: plan → write prose → draw SVG → render PNG → append to `figures/README.md`.
> Part II 需求工程七章的插图规划，共 **63 幅**（每章 9 幅）。
>
> Naming: `figures/svg/chNN-figN-M-slug.svg` + `figures/chNN-figN-M-slug.png`
> Type codes: T1 concept · T2 process · T3 model · T4 before/after · T5 UI · T6 data · T7 AI workflow

---

## Batch order 批量生产顺序（按类型，不按章）

Per §5, produce by type so the visual language stays stable and speed rises:

| Batch | Type | Figures | Chapters | Note |
|---|---|---|---|---|
| **B1** | **T7 AI workflow** | 7 | Ch4–10 | One per chapter, **identical skeleton**: human → AI → verify → artifact. Violet `#6D3FA8` for the AI step only. Draw once, vary labels. |
| **B2** | **T1 concept maps** | 10 | Ch4–10 | Requirements landscape, elicitation sources, analysis layers, model relationships |
| **B3** | **T2 process/lifecycle** | 9 | Ch4–10 | Elicitation cycle, analysis pipeline, modelling workflow, validation loop |
| **B4** | **T3 model diagrams** | 18 | Ch6–9 | UML: activity, use case, class, sequence, state. Highest effort — draw the CareLink artifacts. |
| **B5** | **T4 before/after** | 7 | Ch4–10 | One per chapter — vague vs testable, incomplete vs complete, etc. |
| **B6** | **T6 data/table figures** | 7 | Ch4–10 | Stakeholder matrix, traceability matrix, priority grid, coverage table |
| **B7** | **T5 UI sketches** | 5 | Ch5, Ch7, Ch10 | CareLink screens used as elicitation props |

> **B1 is the fastest win**: 7 figures, one design, ~1 hour total. Do it first and
> the whole book immediately reads as "AI-augmented".

---

## Ch 4 — Requirements Inception and Elicitation

| # | Type | Caption | Alt text |
|---|---|---|---|
| 4-1 | T1 | The requirements landscape: inception, elicitation, analysis, specification, validation | Five linked boxes showing where elicitation sits in the requirements process |
| 4-2 | T2 | The elicitation cycle: prepare, ask, listen, record, confirm, repeat | A six-step circular diagram; confirm feeds back to prepare |
| 4-3 | T1 | Stakeholder map for CareLink | Concentric rings: users (elder, family, caregiver) inner, operations middle, regulators outer |
| 4-4 | T2 | The interview arc: warm-up, context, problems, wish list, wrap-up | A horizontal five-segment timeline with example questions under each segment |
| 4-5 | T4 | The same request, three ways: vague, leading, and open | Three speech bubbles side by side, the open one marked as best practice |
| 4-6 | T4 | Vague requirement vs testable requirement | Two-column contrast: "the app should be easy to use" against a measurable target |
| 4-7 | T6 | Stakeholder influence/interest grid | 2×2 matrix placing CareLink's five stakeholder groups |
| 4-8 | T7 | AI-assisted interview transcript analysis, with verification | Human records → AI extracts candidate requirements → human verifies against transcript → accepted list |
| 4-9 | T1 | From raw stakeholder statement to a numbered requirement | A four-step funnel: statement, classification, testability check, numbered entry |

**Figure count: 9** (T1 ×3, T2 ×2, T4 ×2, T6 ×1, T7 ×1)

---

## Ch 5 — Requirements Analysis and Specification

| # | Type | Caption | Alt text |
|---|---|---|---|
| 5-1 | T1 | The analysis model and its three views: data, function, behaviour | Triangle with the three views at the corners and the analysis model at the centre |
| 5-2 | T2 | From elicited statement to negotiated specification | Pipeline: raw list, de-duplication, conflict resolution, prioritisation, specification |
| 5-3 | T4 | Over-specified vs correctly specified requirement | Contrast between a requirement dictating implementation and one stating capability |
| 5-4 | T3 | Structured specification outline for CareLink | Nested box outline: functional, non-functional, interface, constraint sections |
| 5-5 | T6 | MoSCoW prioritisation of CareLink's first release | Table figure: must / should / could / won't with example requirements in each row |
| 5-6 | T4 | Ambiguous quantifier vs bounded range | Contrast between "fast" and "≤2 s at p95 on a mid-range phone" |
| 5-7 | T2 | Requirements negotiation: identify, discuss, resolve, record | Four-step loop with the disagreement artifact shown at each step |
| 5-8 | T7 | AI-assisted requirement rewriting, with verification | Human draft → AI rewrites for testability → human checks meaning preserved → final wording |
| 5-9 | T5 | CareLink requirement-capture form (family app) | Wireframe of the screen a family member uses to state a need |

**Figure count: 9** (T1 ×1, T2 ×2, T3 ×1, T4 ×2, T5 ×1, T6 ×1, T7 ×1)

---

## Ch 6 — Business Process Modelling

| # | Type | Caption | Alt text |
|---|---|---|---|
| 6-1 | T1 | Why model the business before the software | Two branches: process-first vs screen-first, with the failure each leads to |
| 6-2 | T2 | As-is, to-be, and the gap | Three-panel flow: current process, desired process, the difference the system must close |
| 6-3 | T3 | CareLink as-is: how an alarm call is handled today | Activity diagram with the manual phone chain and its delays |
| 6-4 | T3 | CareLink to-be: the same call with the system | Activity diagram with system steps highlighted |
| 6-5 | T3 | Swimlane view across elder, caregiver, and care centre | Three-lane activity diagram showing hand-offs |
| 6-6 | T4 | Process model with unsupported claims flagged | A model annotated with the evidence gap at each unverified step |
| 6-7 | T6 | Cycle-time table: as-is versus to-be | Table with elapsed time per step and the total improvement |
| 6-8 | T7 | AI-assisted process extraction from policy documents | Human supplies documents → AI drafts activity flow → human checks against real practice → validated model |
| 6-9 | T1 | Process model and requirements: what each answers | Side-by-side: process answers "how work happens", requirements answer "what the system must do" |

**Figure count: 9** (T1 ×2, T2 ×1, T3 ×3, T4 ×1, T6 ×1, T7 ×1)

---

## Ch 7 — Use Case Modelling

| # | Type | Caption | Alt text |
|---|---|---|---|
| 7-1 | T3 | CareLink use case diagram, first release | Actors (elder, family, caregiver) with their use cases inside the system boundary |
| 7-2 | T4 | Use case vs function: the same feature described both ways | Contrast between a user-goal use case and a function list |
| 7-3 | T3 | The anatomy of a use case diagram | Labelled example showing actor, system boundary, association, include, extend, generalisation |
| 7-4 | T3 | The use case description template, filled for one CareLink case | Two-column template: field name beside CareLink's alarm-escalation content |
| 7-5 | T2 | Writing a use case: identify actors, name goals, write main flow, add alternatives | Four-step sequence with the artifact produced at each step |
| 7-6 | T3 | Include and extend in CareLink's alarm escalation | Fragment diagram showing the base case, the always-run include, and the conditional extend |
| 7-7 | T4 | Use case list organised by feature vs by actor goal | Two groupings of the same eight cases, showing which one reveals missing goals |
| 7-8 | T7 | AI-assisted use case drafting, with verification | Human supplies goal → AI drafts flow → human tests against the actor's real goal → corrected flow |
| 7-9 | T5 | CareLink alarm screen, as a use case prop for review | Wireframe used in the walkthrough of the escalation use case |

**Figure count: 9** (T2 ×1, T3 ×4, T4 ×2, T5 ×1, T7 ×1)

---

## Ch 8 — Domain Modelling

| # | Type | Caption | Alt text |
|---|---|---|---|
| 8-1 | T1 | Domain model, class diagram, and database schema: three different artifacts | Three linked boxes with a one-line purpose under each |
| 8-2 | T2 | Finding concepts: nouns, then discard, then name | Pipeline from candidate noun list to a curated concept list |
| 8-3 | T3 | CareLink domain model: first pass | Concepts and associations without attributes |
| 8-4 | T3 | CareLink domain model: with attributes and multiplicities | The refined model with attributes and association ends labelled |
| 8-5 | T4 | Attribute mistaken for a concept | Contrast between a flat list ("address" as a field) and "Address" as a concept with its own life |
| 8-6 | T3 | Association classes and why CareLink needs one | Diagram showing a care-assignment association that carries its own attributes |
| 8-7 | T1 | The domain model links back to the use case list | Mapping arrows from use cases to the concepts they touch |
| 8-8 | T7 | AI-assisted concept extraction from a description, with verification | Human supplies text → AI lists candidate concepts → human removes attributes and duplicates → corrected model |
| 8-9 | T6 | Concept inventory: name, definition, evidence in the transcript | Table figure with two columns of the CareLink concept list |

**Figure count: 9** (T1 ×2, T2 ×1, T3 ×3, T4 ×1, T6 ×1, T7 ×1)

---

## Ch 9 — Behavioural Modelling

| # | Type | Caption | Alt text |
|---|---|---|---|
| 9-1 | T1 | Which behavioural model answers which question | Three-question grid mapping interaction, state, and activity models |
| 9-2 | T3 | CareLink sequence diagram: the alarm-escalation scenario | Participants across the top; the ordered message chain down the page |
| 9-3 | T3 | CareLink state machine: the alarm object's life | States from raised to resolved with the events and guards between them |
| 9-4 | T3 | CareLink activity diagram: caregiver shift hand-over | Activity flow with decision and merge nodes |
| 9-5 | T4 | Sequence diagram with a missing alternative path | A happy-path-only diagram beside the corrected version with the failure branch |
| 9-6 | T3 | Traceability from scenario to message | The same scenario narration with each sentence connected to its message in the diagram |
| 9-7 | T6 | State-event table for the alarm object | Matrix of states against events, cells showing the resulting state |
| 9-8 | T7 | AI-assisted behavioural model drafting, with verification | Human narrates scenario → AI drafts sequence → human checks ordering and branches → corrected diagram |
| 9-9 | T2 | Choosing a behavioural model: scenarios, states, or workflows | Decision flow based on the question being asked |

**Figure count: 9** (T1 ×1, T2 ×1, T3 ×4, T4 ×1, T6 ×1, T7 ×1)

---

## Ch 10 — Requirements Validation and Management

| # | Type | Caption | Alt text |
|---|---|---|---|
| 10-1 | T2 | The validation loop: inspect, review, test, agree | Four-step loop with the exit condition stated |
| 10-2 | T6 | A requirements review checklist, scored | Table figure with review criteria and a pass/fail column |
| 10-3 | T4 | Requirement defect classes: omission, conflict, ambiguity, gold-plating | Four-panel contrast with one CareLink example per class |
| 10-4 | T2 | Change control: request, assess, decide, implement, re-baseline | Five-step flow with the traceability artifact at each stage |
| 10-5 | T6 | Requirements traceability matrix for CareLink | Matrix linking requirement ID to use case, model element, design element and test |
| 10-6 | T1 | Why baselines exist: a change without one | Two timelines, one with a baseline and one without, showing the cost difference |
| 10-7 | T4 | Traceability after a scope change: before and after re-baseline | Two versions of the matrix showing which links survived the change |
| 10-8 | T7 | AI-assisted requirement review, with verification | Human supplies spec → AI lists suspected defects → human confirms each against the source → confirmed defect list |
| 10-9 | T5 | CareLink change-request form | Wireframe of the form that starts the change-control flow |

**Figure count: 9** (T1 ×1, T2 ×2, T4 ×2, T5 ×1, T6 ×2, T7 ×1)

---

## Totals 合计

| Chapter | Figures | Types used |
|---|---|---|
| Ch 4 | 9 | T1, T2, T4, T6, T7 |
| Ch 5 | 9 | T1, T2, T3, T4, T5, T6, T7 |
| Ch 6 | 9 | T1, T2, T3, T4, T6, T7 |
| Ch 7 | 9 | T2, T3, T4, T5, T7 |
| Ch 8 | 9 | T1, T2, T3, T4, T6, T7 |
| Ch 9 | 9 | T1, T2, T3, T4, T6, T7 |
| Ch 10 | 9 | T1, T2, T4, T5, T6, T7 |
| **Part II** | **63** | all seven types used |

Every chapter has **exactly one T7 AI-workflow figure** and **at least one T4
before/after figure** — the two types that carry the book's argument.

## Remaining Parts 剩余篇的规划

| Part | Chapters | Figures (at 9/ch) | Plan file |
|---|---|---|---|
| I Foundations | 1–3 | 27 (9 done, 18 to add) | ⏳ needs backfill |
| II Requirements | 4–10 | 63 | ✅ this file |
| III Design | 11–14 | 36 | ⏳ to write |
| IV Implementation & Quality | 15–17 | 27 | ⏳ to write |
| V Management & Evolution | 18–20 | 27 | ⏳ to write |
| **Total** | **20** | **180** | |

> ⚠️ **Part I backfill**: Ch 1–3 currently have 3 figures each. Each needs 6 more
> (including its T7 AI-workflow figure) before the free sample reads as
> "genuinely illustrated" — this matters because **Ch 1–3 are the marketing sample**.
