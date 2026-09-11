# Chapter Template — twelve-part structure (EMI + AI edition), ~22 pages

> Every chapter of *Object-Oriented Software Engineering: A Project-Based Path*
> follows this structure. Keep sentences short (median ≤ 20 words).
> File naming: `manuscript/chNN.md`; figures: `figures/chNN-figN-M-topic.svg` (+ `.png` render).
>
> **Three parts exist because this is an EMI book for a global, AI-native audience:**
> *Before You Read* (term pre-teaching), *Language Focus* (academic patterns),
> and *AI Companion* (working with AI on this chapter's task).
> Rules: [`emi-style-guide.md`](emi-style-guide.md), [`ai-integration-guide.md`](ai-integration-guide.md).
> 其中三个小节是本 EMI + AI 版特有，规范见相应文档，不可省略。

**Per-chapter quotas 每章硬指标**

| Item | Quota |
|---|---|
| Figures 插图 | **≥ 8** (Core 3–4 · CareLink 2–3 · AI Companion 1 · Lab 1) |
| Exercises 习题 | **≥ 10**, across 4 tiers |
| AI elements AI 元素 | AI Companion + ≥2 AI-augmented exercises |
| Length 篇幅 | 20–24 pages (≈ 6,000–7,500 words) |

```markdown
# Chapter N — Title

## Learning Objectives
4–6 objectives, each starting with a Bloom verb
(Define, Explain, Compare, Apply, Analyze, Evaluate, Create).
At least one objective must involve AI-assisted work.

## Before You Read  (~0.5 page)
6–10 terms, one line each, ≤15 words, with Chinese gloss.
Rationale: for non-native readers most comprehension breaks happen
at unknown vocabulary — pre-teach it before the prose, not in it.
6–10 条术语，每条一行、不超过 15 词，附中文对照。

## Opening Scenario
1 page. A concrete CareLink situation or dilemma that this
chapter resolves. Start with a scene, not a definition.

## Core Concepts
8–12 pages. The chapter's substance.
- One idea per subsection; one idea per paragraph.
- **Every major concept gets a figure** (see quotas above).
- Numbered examples where a method is demonstrated.
- Where AI changes the practice, say so inline in a short
  `> 🤖 AI note` block — details belong in *AI Companion*.

## CareLink in Action
3–5 pages. Apply this chapter's method to the running case.
Show intermediate artifacts, not just final results.
Include at least one artifact *as produced with AI help* and one
*reviewer checklist* used to validate it.

## AI Companion  (~1.5 pages) ★
Fixed four-part structure — see ai-integration-guide.md:
1. **What AI is good at here** (2–3 bullets)
2. **Prompt pattern** (copy-paste template, ≤8 lines)
3. **Verify before you trust** (3–5 checklist items)
4. **Typical AI failure in this chapter** (1 worked example)
每章固定四段：AI 能做什么 → 提示词模板 → 验证清单 → 本章典型 AI 翻车示例。

## Common Pitfalls
1–2 pages. Frequent student mistakes, stated bluntly, each with
the correction. Include **at least one AI-induced pitfall**
(e.g. plausible-but-wrong model, invented requirement,
terminology drift).

## Guided Lab
2–3 pages. A step-by-step exercise usable in class.
Input given, output expected, time estimate.
Provide **two tracks**: Track A manual / Track B AI-assisted,
with the same acceptance criteria.

## Language Focus  (~1 page)
The 3–5 sentence patterns students need to *write this week's
assignment* — not general English, but this chapter's professional
writing. Three fixed steps: pattern → example → 3 short exercises.
本章作业真正用得上的 3–5 个句型。固定三步：句型 → 例句 → 3 题练习。

## Summary and Key Terms
- 5–8 bullet summary.
- Key-terms box: term (bold) + Chinese gloss. Terms must
  match Appendix B.

## Exercises
**≥ 10 items in four tiers** (answers in the instructor's manual;
starred items have a model answer in Appendix C):
- (a) **Concept checks** (3–4) — recall and discrimination
- (b) **Analysis problems** (3–4) — apply the method to a short scenario
- (c) **AI-augmented tasks** (2) — use AI, then *verify and repair* its
  output; grading rewards the critique, not the prompt
- (d) **Running Project Task** (1–2) — advances the student project,
  synchronised with course milestones

## Figure List (authoring aid, removed before build)
chNN-figN-1 … chNN-figN-8 with one-line captions and alt text.
```
