# Object-Oriented Software Engineering: A Project-Based Path

[![License](https://img.shields.io/badge/license-layered--see%20LICENSE.md-blueviolet)](./LICENSE.md)
[![Figures](https://img.shields.io/badge/figures-CC%20BY%204.0-2EA043)](./LICENSE.md)
[![Language](https://img.shields.io/badge/language-English-blue)]()
[![Chapters](https://img.shields.io/badge/chapters%20drafted-8%2F20-orange)]()
[![AI](https://img.shields.io/badge/AI--augmented-every%20chapter-6D3FA8)]()
[![Status](https://img.shields.io/badge/status-writing%20in%20progress-yellow)]()

An open, project-driven English textbook on object-oriented software engineering, spanning a complete software lifecycle — from requirements elicitation to delivery and evolution — through **one original running case: CareLink**, a community elder-care platform.

**Designed for a 64-hour, two-semester course** (Software Engineering I + II).

> 🎓 **Companion course 配套课程**：This book is written alongside a bilingual open course; weekly lecture slides (W01–W16, CampusGuard running case) are released in parallel at **[klausren/software-engineering-course](https://github.com/klausren/software-engineering-course)**.
> 本教材与双语开源课程同步编写，每周课件（W01–W16，CampusGuard 案例）在课程仓库同步发布。
>
> *By design 教学设计*：this book teaches with the original **CareLink** case, while the course's student teams build **CampusGuard** — readers learn each technique from one case and apply it to another, which prevents copy-paste and trains real modeling transfer. 教材用原创案例 CareLink 讲解，课程学生团队做 CampusGuard 项目——学一个案例、练另一个案例，防止照抄，训练真正的迁移能力。

## Why This Book

- **One case, full lifecycle.** CareLink is introduced in Chapter 1 and grows with every chapter — the same requirements, models, designs, tests, and plans you read about are the ones you build.
- **Right-sized for teaching.** ~380 pages, 20 chapters, one chapter per teaching week — not an 800-page reference.
- **Written for EMI classrooms.** This is the book's real differentiator. Pressman and Sommerville are written by and for native speakers; at an English-medium university, students' bottleneck is usually **the English, not the engineering**. Every chapter controls sentence length, pre-teaches its terms, enforces one term per concept across all 20 chapters, and closes with a *Language Focus* on the academic English patterns the chapter needs. See [`templates/emi-style-guide.md`](templates/emi-style-guide.md).
  面向 EMI（英语作为教学语言）课堂而写——这是本书真正的差异点。主流教材由母语者写、为母语者写；在英语授课的大学里，学生的瓶颈往往是**英语而非工程**。本书控制句长、每章预教术语、全书一词一义，章末附 Language Focus 讲本章所需的学术英语句型。
- **AI-augmented, with verification discipline.** Every chapter carries an **AI Companion**: what AI is good at in *this* chapter's task, a copy-paste prompt pattern, a *Verify Before You Trust* checklist, and one real example of how AI gets this chapter wrong. Labs run two tracks (manual / AI-assisted) with **one rubric**; exercises include AI-augmented tasks graded on the **critique, not the prompt**. Position statement: *AI changes the cost of producing artefacts, not the responsibility for their correctness.* See [`templates/ai-integration-guide.md`](templates/ai-integration-guide.md).
  每章含 AI Companion：本章 AI 能做什么、提示词模板、验证清单、一个真实的 AI 翻车示例。实验分手工/AI 双轨同一评分标准；习题含 AI 任务，**评分看批判不看提示词**。
- **Genuinely illustrated.** Target: **≥9 figures per chapter, 180+ in the book** (concept maps, process diagrams, UML models, before/after contrasts, UI sketches, data figures, and one AI-workflow figure per chapter), all drawn as versionable SVG in one visual language. See [`templates/figure-system.md`](templates/figure-system.md).
  图文并茂：每章 ≥9 幅、全书 180+ 幅，统一视觉语言的 SVG 图。
- **Classroom-proven.** Every chapter is written while the material is being taught, tested on real students, and revised from their feedback.

> 🎯 **Who it is for 目标读者**：undergraduates at English-medium programmes in China, Southeast Asia, Central &amp; Eastern Europe, the Gulf and Latin America — plus the instructors who teach them. 面向中国、东南亚、中东欧、海湾地区与拉美的英语授课项目本科生，以及讲授这些课程的教师。

## Table of Contents

### Part I — Foundations

| Ch | Title | Status |
|---|---|---|
| 1 | Software and Software Engineering | ✅ draft · 9 figures |
| 2 | Software Process Models | ✅ draft · 9 figures |
| 3 | Agile Development and Scrum | ✅ draft · 9 figures |

### Part II — Requirements Engineering

| Ch | Title | Status |
|---|---|---|
| 4 | Requirements Inception and Elicitation | ✅ draft · 9 figures |
| 5 | Requirements Analysis and Specification | ✅ draft · 9 figures |
| 6 | Business Process Modelling | ✅ draft · 9 figures |
| 7 | Use Case Modelling | ✅ draft · 9 figures |
| 8 | Domain Modelling | ✅ draft · 9 figures |
| 9 | Behavioural Modelling | ⏳ planned |
| 10 | Requirements Validation and Management | ⏳ planned |

Full figure plan for Part II (63 figures): [`figures/PLAN-part2-requirements.md`](figures/PLAN-part2-requirements.md)

### Part III — Design (Ch 11–14) · Part IV — Implementation and Quality (Ch 15–17) · Part V — Management and Evolution (Ch 18–20)

Full chapter map: see `manuscript/` as chapters are released weekly.

## Repository Layout

```
manuscript/    Chapter sources (Markdown), one file per chapter
               Book.txt / Sample.txt / title.txt / subtitle.txt / author.txt
               (Leanpub manifest — see publishing/leanpub-launch-checklist.md)
manuscript/    images/ — the PNGs Leanpub reads (synced from figures/)
figures/       Original figures (SVG + PNG), numbered chNN-figN-M-topic
               CC BY 4.0 — the open, reusable asset
case-study/    The CareLink running case: full specification and all models
templates/     Chapter template (12 parts), EMI style guide,
               AI integration guide, figure system
publishing/    Commercial plan, Leanpub book-page copy, 5-step launch checklist
build/         build.sh (Markdown -> DOCX) and sync-figures.sh
instructor/    Instructor's manual (not part of the open release)
```

> **Two figure folders, on purpose.** `figures/` is the public CC BY 4.0 asset
> (reuse it, teach with it). `manuscript/images/` is what the publishing
> pipeline reads. Chapters reference figures as `images/xxx.png` — one path
> that works for both pandoc and Leanpub. Run `build/sync-figures.sh` after
> changing anything in `figures/`.

## Reading the Book

Each chapter follows the same **twelve-part structure**:

**Learning Objectives → Before You Read → Opening Scenario → Core Concepts → CareLink in Action → 🤖 AI Companion → Common Pitfalls → Guided Lab (2 tracks) → Language Focus → Summary & Key Terms → Exercises (4 tiers) → Running Project Task**

Per-chapter quotas: **≥9 figures · ≥10 exercises in four tiers · ≥2 AI-augmented tasks · 20–24 pages**.

Three parts are EMI/AI-specific — **Before You Read** (term pre-teaching),
**Language Focus** (this chapter's academic English patterns), and
**AI Companion** (working with and verifying AI) — and they are what
distinguish this book from a shorter Pressman.
其中 **Before You Read**（术语预热）、**Language Focus**（本章学术英语句型）与 **AI Companion**（AI 协同与验证）是本书特有部分。

## Commercial Edition 商业版（面向全球学生）

Chapters 1–3 stay free here. The complete 20-chapter edition — with exercise
answers, the prompt library, and instructor resources — will be **sold
worldwide**: Leanpub (ebook, lifetime updates), Amazon KDP (paperback),
IngramSpark (libraries), and institutional licences.

<!-- EARLY ACCESS LINK: replace the placeholder below with the live Leanpub URL
     once the book is published (format: https://leanpub.com/oose-textbook) -->

> 🛒 **Early Access — 2026 Q4** · `https://leanpub.com/oose-textbook` *(coming soon)*
> Buy once, get every future revision. Chapters 1–3 are free here; the paid edition adds
> Chapters 4–20 as they are released, plus exercise answers, the AI prompt library and the
> complete CareLink model appendix.
> 一次购买、终身更新。前 3 章在本仓库免费；付费版随写随发补齐第 4–20 章，另含习题答案、
> AI 提示词库与 CareLink 完整模型附录。

**Launch materials 上架材料**：
[`publishing/commercial-plan.md`](publishing/commercial-plan.md)（渠道 / 定价 / 时间表）·
[`publishing/leanpub-book-description.md`](publishing/leanpub-book-description.md)（书目页文案）·
[`publishing/leanpub-launch-checklist.md`](publishing/leanpub-launch-checklist.md)（5 步上线清单）
前 3 章永久免费；完整 20 章（含习题答案、提示词库、教师资源）全球发售。

## Adopting This Book

Chapters are released while being taught. You are welcome to pilot them in your own
course **non-commercially, with attribution** — see [`LICENSE.md`](./LICENSE.md) for the
exact terms. If you do, **please register your adoption**: a public record of real
classroom use is the strongest evidence a textbook can have, and it directly supports the
planned print edition.

👉 [Register / 登记](https://github.com/klausren/oose-textbook/issues/new?template=textbook-adoption.md) — a one-minute issue with a ready-made template.

> 💡 **What an adoption record does for you** 登记能带来什么：registered adopters are the
> first to hear about the instructor's manual, slide decks and the print edition — and are
> credited (unless you prefer otherwise) in the book's front matter.
> 登记采用者将优先获得教师手册、课件与出版信息，并（除非你另有说明）列入书前致谢。

**Known adoptions**

| Institution | Course | Term | Chapters Used |
|---|---|---|---|
| Dalian Neusoft University of Information | Software Engineering I (bilingual, international class) | 2026–2027–1 | Ch. 1–3 (piloted alongside the course) |
| *Yours?* | | | |

## License & Citation

**Layered licensing** — see [`LICENSE.md`](./LICENSE.md):

| Part | License |
|---|---|
| `manuscript/`, `case-study/`, `instructor/` | © Ren Zheng, all rights reserved (free for non-commercial course use with attribution) |
| `figures/` | **CC BY 4.0** — reuse freely, including commercially, with attribution |
| Chapters 1–3 (released before 2026-09-05) | Also available under **CC BY-NC-SA 4.0**; use whichever licence suits you |

The layering exists because a print edition is planned and publishers require exclusive
commercial rights. Figures stay open because diagram reuse is what helps teachers most.
分层授权是因为计划出版，出版社要求独家商业授权；插图保持开放是因为复用图表对教师帮助最大。

```
Ren Zheng. Object-Oriented Software Engineering: A Project-Based Path.
Open edition, 2026–. https://github.com/klausren/oose-textbook
```

## Author

**Ren Zheng** — School of Software, with nine years of teaching software engineering to international and bilingual classes. Feedback welcome via GitHub Issues.
