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
- Panel titles: 20px bold; box titles: 19px bold; annotations: 14–15px regular.
- Text in figures is **English only** (Chinese key terms stay in body text).
- All labels use `text-anchor` centering; never rely on manual spacing.

## Canvas & rendering 画布与渲染

- SVG `viewBox` width: **760 units** (≈ two-column figure); height per content.
- Rendered to PNG at **2400 px wide** (crisp in docx and PDF at 300 dpi).
- Lines ≥ 3 px; rounded corners (rx 8–12); 2–3 px gaps between stacked shapes.
- Arrowheads: explicit-fill markers, one per color (never `context-stroke`).

## Naming & captions 命名与图题

- Files: `chNN-figN-M-slug.png` (source `.svg` keeps the same stem).
- Captions live **in the manuscript, not inside the image**:

  ```markdown
  ![Alt text](../figures/chNN-figN-M-slug.png){width=15cm}

  *Fig. N-M. One-sentence English caption.*
  ```

- Every figure must be **referenced in body text** before it appears.
- Budget: **2–4 figures per chapter**; reuse lecture-deck vector art by
  re-exporting SVG when geometry fits this palette.

## Canonical figure types 六类标准图

1. **Curve/chart** — axes + labeled curves (e.g., Fig. 1-1 failure curves).
2. **Layered stack** — horizontal layers (e.g., Fig. 1-2 the three essentials).
3. **Context diagram** — actors and system boundary with labeled arrows
   (e.g., Fig. 1-3 CareLink at a glance).
4. **Process/flow** — rounded rects + directed arrows (UML-adjacent).
5. **Comparison panel** — two panels sharing one axis system.
6. **Annotated artifact** — a document/screen mock with callouts.

## Re-render after editing SVG

```zsh
NODE_PATH=/Users/renzheng/.workbuddy/binaries/node/workspace/node_modules \
  /Users/renzheng/.workbuddy/binaries/node/versions/22.22.2/bin/node \
  figures/render.js
```
