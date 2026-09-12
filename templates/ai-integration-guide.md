# AI Integration Guide — how this book uses AI

> 本书的 AI 融入规范。**Three layers, not one gimmick.**
> AI 不是加一个章节就完事，而是三层渗透：内容层 / 章节层 / 练习层。
> Author: Ren Zheng · Version 1.0 (2026-09-08)

---

## 1. Why: the positioning claim

By 2027 no software engineering textbook can ignore AI, yet most books still
teach as if every artifact is typed by hand. This book takes a defensible
middle position:

> **AI changes the cost of producing artifacts, not the responsibility for
> their correctness.**
> AI 改变的是"产出制品的成本"，不是"为制品正确性负责"这件事。

Everything below follows from that sentence: we teach students to **use AI,
verify AI, and be accountable** — never to outsource judgement.

This is also the book's **commercial differentiator** alongside EMI:
*the first EMI software engineering textbook with a built-in AI-verification
pedagogy*. 与 EMI 并列的第二个卖点。

---

## 2. Layer 1 — Content: what changes in the engineering itself

Each chapter gets an *AI angle* — the specific way AI alters that chapter's
practice. Authors must address it inline (short `> 🤖 AI note` blocks) and in
depth in *AI Companion*.

| Ch | Topic | AI angle 本章 AI 视角 |
|---|---|---|
| 1 | Software & SE | AI as a force that changed software's economics; why "faster code" did not remove the software crisis |
| 2 | Process models | Where AI assistance fits in waterfall / incremental / spiral; AI-augmented spiral risk analysis |
| 3 | Agile & Scrum | AI in stand-ups, backlog refinement, estimation; velocity inflation risk |
| 4 | Requirements inception & elicitation | AI-assisted stakeholder interview analysis; hallucinated stakeholder needs |
| 5 | Requirements analysis & specification | AI-drafted SRS; ambiguity that reads as precision |
| 6 | Business process modelling | AI extraction of a process from policy documents; the documented process mistaken for the real one |
| 7 | Use case modelling | Generating candidate use cases from transcripts; missing actors and wrong boundaries |
| 8 | Domain modelling | Candidate concept extraction from text; attribute-versus-concept errors |
| 9 | Behavioural modelling | Sequence and state diagram generation; impossible transitions |
| 10 | Requirements validation & management | Using AI as an adversarial reviewer; traceability faking |
| 11 | Design concepts | AI-suggested patterns; over-engineering by suggestion |
| 12 | Architecture | AI-proposed architectures without quality-attribute rationale |
| 13 | Class design | Generated class diagrams; responsibility misassignment |
| 14 | UI design | AI-generated wireframes; accessibility and i18n blind spots |
| 15 | Implementation | Pair programming with AI; code review of AI output; license and provenance |
| 16 | Testing | AI-generated tests that pass but assert nothing; mutation testing |
| 17 | **AI-augmented SE (new chapter)** | Verification discipline, prompt as specification, evidence trails, when not to use AI, licensing and data-protection basics |
| 18 | Project management | AI estimation; planning fallacy with confident AI numbers |
| 19 | Risk & configuration | Model/API dependency as a supply-chain risk; versioning prompts |
| 20 | Evolution & delivery | AI-assisted refactoring and legacy comprehension; telemetry-driven evolution |

**New chapter 17 "AI-Augmented Software Engineering"** (Part IV) is the anchor:
verification discipline, prompt-as-specification, evidence trails, when *not*
to use AI, licensing and data-protection basics.

---

## 3. Layer 2 — Chapter: the *AI Companion* section (four fixed parts)

Every chapter carries an AI Companion (~1.5 pages) with the same four parts:

1. **What AI is good at here** — 2–3 bullets, specific to the chapter's artifact.
2. **Prompt pattern** — a copy-paste template (≤8 lines) with `{{slots}}`.
3. **Verify before you trust** — 3–5 checklist items that catch the *chapter's own*
   failure mode (e.g. Ch 8: "every concept must appear in the inventory; reject
   concepts that are really attributes").
4. **Typical AI failure in this chapter** — one short worked example:
   AI output → what's wrong → the repair. Students learn the shape of the mistake.

**Universal verification checklist (V-AI)** — reuse, then add chapter-specific items:

- [ ] **Traceable** — every statement maps to a source I can inspect (requirement, transcript, code).
- [ ] **Terminological** — uses this book's terms, one term per concept (no synonyms invented).
- [ ] **Testable** — each claim can be checked by an experiment, a test, or a stakeholder.
- [ ] **Complete on the seams** — states its assumptions and what it did *not* cover.
- [ ] **Non-fabricated** — no citations, standards, or statistics I cannot verify.
- [ ] **Licensed** — third-party code/content provenance is known and compatible.

---

## 4. Layer 3 — Practice: labs and exercises

- **Guided Lab: two tracks, one rubric.** Track A manual, Track B AI-assisted,
  identical acceptance criteria. Students submit *which* track plus an evidence
  note (prompt + output + what they changed).
- **AI-augmented exercises (tier c)**: the deliverable is *the critique*, not the
  prompt. Example: "Below is an AI-generated domain model for CareLink. Find four
  defects, fix two, and justify why you left the other two." Answer keys grade
  reasoning, not output quality.
- **Declaration template** (student work): tool used · prompt summary · what was
  accepted · what was rejected and why · who reviewed it.

**Academic integrity policy (recommended wording for adopters)**

| Allowed | Not allowed |
|---|---|
| AI for brainstorming, explanation, drafting, refactoring, review | Submitting unverified AI output as your own analysis |
| Declaring tool use in the evidence note | Hiding AI use when asked |
| AI-generated diagrams that you have checked against the model rules | AI-generated artifacts cited as "verified" without evidence |

---

## 5. Prompt pattern library (reusable across chapters)

> Keep prompts ≤8 lines, always with **role · context · artifact · constraints · output format · verification request**.

**P1 Explain** — *Explain {{concept}} using {{case}}; 150 words; use only these terms: …; end with one self-check question.*

**P2 Generate** — *Draft {{artifact}} for {{scope}}. Constraints: {{rules}}. Output as {{format}}. Do not invent requirements; mark assumptions as [ASSUMPTION].*

**P3 Critique** — *Review this {{artifact}} against {{rules}}. List only defects, each with: location, why it is wrong, minimal fix. If it is correct, say so.*

**P4 Transform** — *Convert {{artifact A}} into {{artifact B}}. Preserve identifiers. Report anything that cannot be mapped.*

**P5 Verify** — *Here is an AI output and the source material. For each claim, mark [SUPPORTED] / [UNSUPPORTED] / [CONTRADICTED] with a line reference.*

---

## 6. Authoring workflow for authors (including the author himself)

1. Write Core Concepts first; mark where AI genuinely changes practice.
2. Draft AI Companion *after* Common Pitfalls — the failure example should be a real
   output you obtained, not an invented one.
3. Produce figures: at least one figure must visualise an AI-related workflow
   (human → AI → verify → artifact).
4. Write tier (c) exercises from real AI outputs; keep the raw output for the
   instructor's manual.
5. Bookkeeping: every AI-assisted section is marked in the chapter's front matter
   as `ai-assisted: yes` for transparency in the print edition.

---

## 7. Figure requirement related to AI

- Every chapter: **≥1 AI figure** (workflow / before-after / verification loop).
- Style: same visual language as other figures (see `figure-system.md`);
  AI elements drawn in a distinguishable accent colour, never as a magic box.
- Never show AI as an authority: every AI figure includes a **human verification step**.
