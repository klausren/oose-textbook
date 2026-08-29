# Object-Oriented Software Engineering: A Project-Based Path

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Language](https://img.shields.io/badge/language-English-blue)]()
[![Chapters](https://img.shields.io/badge/chapters%20drafted-1%2F20-orange)]()
[![Status](https://img.shields.io/badge/status-writing%20in%20progress-yellow)]()

An open, project-driven English textbook on object-oriented software engineering, spanning a complete software lifecycle — from requirements elicitation to delivery and evolution — through **one original running case: CareLink**, a community elder-care platform.

**Designed for a 64-hour, two-semester course** (Software Engineering I + II), with companion slide decks released weekly at [software-engineering-course](https://github.com/klausren/software-engineering-course).

## Why This Book

- **One case, full lifecycle.** CareLink is introduced in Chapter 1 and grows with every chapter — the same requirements, models, designs, tests, and plans you read about are the ones you build.
- **Right-sized for teaching.** ~420 pages, 20 chapters, one chapter per teaching week — not an 800-page reference.
- **Written for non-native readers.** Short sentences, consistent terminology, and a bilingual glossary of 150+ core terms.
- **Classroom-proven.** Every chapter is written while the material is being taught, tested on real students, and revised from their feedback.

## Table of Contents

### Part I — Foundations

| Ch | Title | Status |
|---|---|---|
| 1 | Software and Software Engineering | ✅ draft |
| 2 | Software Process and Process Models | 🚧 planned |
| 3 | Agile Development and Scrum | 🚧 planned |

### Part II — Requirements Engineering (Ch 4–10) · Part III — Design (Ch 11–14) · Part IV — Implementation and Quality (Ch 15–17) · Part V — Management and Evolution (Ch 18–20)

Full chapter map: see `manuscript/` as chapters are released weekly.

## Repository Layout

```
manuscript/    Chapter sources (Markdown), one file per chapter
figures/       Original figures (SVG), numbered fig-NN-MM
case-study/    The CareLink running case: full specification and all models
templates/     The eight-part chapter template
build/         Pandoc build scripts (Markdown -> DOCX / PDF)
instructor/    Instructor's manual (not part of the open release)
```

## Reading the Book

Each chapter follows the same structure: **Learning Objectives → Opening Scenario → Core Concepts → CareLink in Action → Common Pitfalls → Guided Lab → Summary & Key Terms → Exercises + Running Project Task**.

## License & Citation

Open edition released under **CC BY-NC-SA 4.0** — free to read, use in courses, and remix non-commercially with attribution and share-alike.

```
Ren Zheng. Object-Oriented Software Engineering: A Project-Based Path.
Open edition, 2026–. https://github.com/klausren/oose-textbook
```

## Author

**Ren Zheng** — School of Software, with nine years of teaching software engineering to international and bilingual classes. Feedback welcome via GitHub Issues.
