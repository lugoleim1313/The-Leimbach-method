---
title: "Review PDF Notes"
volume: "Publishing"
status: "review"
last_updated: "2026-07-12"
author: "Mika Leimbach"
---

# Review PDF Notes

> **Volume:** Publishing  
> **Status:** Draft for review; not final publication guidance

## Review PDF Artifact

Generated Version 1.0 review PDF:

- [../dist/Mikas-Method-to-the-Madness-v1.0-review.pdf](../dist/Mikas-Method-to-the-Madness-v1.0-review.pdf)

This artifact is a review draft only. It does not mark the manuscript final and does not change any chapter status to `final`.

## Build Summary

| Item | Result |
|---|---|
| Build date | 2026-07-12 |
| Output file | `dist/Mikas-Method-to-the-Madness-v1.0-review.pdf` |
| Page count | 142 pages |
| Page size | Letter |
| Source order | `MANUSCRIPT.md`, the generated linked TOC, and Issue 34 front/back matter requirements |
| Review label | Present on cover and footer |
| Page numbers | Present |
| Safety disclaimer near front | Present |
| PDF bookmarks | Present |
| Linked TOC annotations | Present |
| Blank pages | None detected |
| Duplicate source TOC pages | Removed from the reader-facing PDF body |
| Raw Markdown link remnants | None detected in PDF text extraction checks |
| Consolidated references | Present; placeholder reference row replaced with concise grouped references |
| Front/back matter review copy | Present; copyright, dedication, foreword, The Promise, and About the Author drafted for review |
| Table readability pass | Present; dense tables use dynamic column widths, repeated headers, and alternating row backgrounds |
| Full manuscript content | Present, with final publication status withheld |
| Updated manuscript title | Present; cover, metadata, title page, and running footer use `Mika’s Method to the Madness` |
| Author story and purpose | Present; front matter and foundation now explain why the method exists |
| Creed | Present; front matter and foundation include The Creed |
| Week One start | Present; reader-facing implementation and training guidance starts the next full 6-week block at Week 1 |
| Modular nutrition meal-builder options | Present; breakfast, lunch, dinner, snack, and dessert option framework added without changing macro targets or meal rows |

## Rendered Pages Checked

Representative pages were rendered to PNG and visually inspected:

| Page | Area Checked | Result |
|---|---|---|
| 1 | Cover/title page | New title renders cleanly; review-draft label and page footer visible |
| 2-4 | Linked table of contents | Page numbers present; major sections and chapter entries visible |
| 5-12 | Front matter and foundation | Source TOC body pages removed; title, copyright, dedication, foreword review copy and safety disclaimer remain visible |
| 24, 27 | Nutrition table pages | Nutrition tables readable with clearer column weighting, repeated headers, and alternating row backgrounds |
| 40-44, 47, 50, 52, 54, 55, 58 | Meal plan, meal prep, and grocery pages | Dense tables render cleanly without clipping; grocery and meal-plan rows remain readable |
| 40-41 | Modular meal-builder options | Meal Builder Rule plus breakfast, lunch, dinner, snack, and dessert option tables render cleanly |
| 48 | Modular meal-builder prep | Prep components and meal role table render cleanly |
| 54-56 | Meal-builder grocery add-ons | Optional grocery add-ons and adjacent grocery tables render cleanly |
| 67, 74, 76, 84, 86-89 | Training table pages | Training tables, including the six-week block, render cleanly with wrapped cells and clearer row separation |
| 101, 104 | Recovery/safety pages | Heat-stress chapter starts on a clean page; safety language remains visible |
| 108, 110, 116-117 | Tracking dashboard/checklist pages | Bodyweight, training log, dashboard, and worksheet tables render cleanly |
| 119, 121, 124, 131 | Exercise Library table pages | Substitution and variation tables render cleanly |
| 135-140 | Back matter, references, version history, final checklist | The Promise and About the Author review copy render cleanly; consolidated references and final checklist remain readable |
| 1-8, 40, 135-141 | Issue #52 post-merge proof pages | Renamed cover, TOC, safety disclaimer, front matter review copy, meal-builder page, back matter, references, version history, and final checklist render cleanly |
| 8-9, 15, 90, 92 | Issue #54 story/start revision pages | Why This Exists, Week One Entry, Starting the Block at Week 1, and Starting the Next Block render cleanly |
| 8-9 | Issue #54 Creed pages | The Creed renders cleanly in both front matter and foundation |

## Verification Notes

- Issue #48 proof pass rebuilt the PDF from merged `main` after the modular nutrition meal-builder update and rechecked the new nutrition pages.
- Issue #50 title/front-back matter pass updated the review title to `Mika’s Method to the Madness`, renamed the PDF artifact, and replaced explicit publication placeholders with drafted review copy.
- Issue #52 post-merge proof pass rebuilt the renamed PDF from merged `main` and rechecked metadata, TOC, bookmarks, links, page numbers, front matter, meal-builder content, back matter, references, version history, and final checklist pages.
- Issue #54 story/start revision pass added author purpose/life-context copy and removed reader-facing Week 4 entry guidance in favor of starting the next full 6-week block at Week 1.
- Issue #54 follow-up added The Creed to front matter and foundation, then rebuilt and rechecked the PDF.
- `pdfinfo` reported 142 pages, Letter page size, and readable metadata.
- `pypdf` reported 142 pages, zero blank pages, 144 link annotations, 72 PDF outline entries, and zero unresolved internal TOC link destinations.
- Source validation reported no missing manuscript source files.
- Duplicate source validation reported no duplicate chapter sources, except intentional extraction from `Publishing/03-front-matter.md` for title/safety and how-to-use sections.
- The generated linked TOC remains near the front; the source `Publishing/02-table-of-contents.md` body is no longer rendered as duplicate reader-facing TOC pages.
- Text extraction checks found no raw Markdown link remnants such as `](../` or `Start Here]`.
- The consolidated `REFERENCES.md` section renders as grouped reference entries rather than a compressed placeholder table.
- Front/back matter review-copy pages were rendered and visually inspected after the title and placeholder-copy pass.
- Issue #48 rendered and visually inspected cover page 1, TOC page 4, safety disclaimer page 5, meal-builder pages 40-41, modular prep page 48, grocery add-on page 55, and final checklist page 141.
- Issue #52 rendered and visually inspected cover page 1, TOC page 2, safety disclaimer page 5, copyright page 6, dedication page 7, foreword page 8, meal-builder page 40, The Promise page 135, About the Author page 136, references page 137, version history page 139, and final checklist page 141.
- Issue #54 rendered and visually inspected foreword/purpose page 8, foundation purpose page 9, Week One Entry page 15, training block Week 1 start page 90, and progression Week 1 start page 92.
- Issue #54 Creed follow-up rendered and visually inspected Creed pages 8-9.
- Nutrition, meal-builder, meal-plan, grocery, training, tracking dashboard, and exercise-library table pages were rendered and visually inspected after the table readability pass.
- Representative pages were rendered with Poppler `pdftoppm`.
- `qpdf` was not installed in this environment, so the PDF was validated with `pdfinfo`, `pypdf`, and rendered PNG inspection instead.
- The generated PDF uses readable repository source paths near chapter starts for review traceability.
- Tables and checklists are preserved with wrapped table cells for review readability, not final publication typography.
- The final PDF has not been created.

## Known Limitations For Later Proofing

- Copyright, dedication, foreword, The Promise, and About the Author now contain drafted review copy and still require author approval before final publication status.
- Very wide source tables may still need final layout tuning before publication.
- Chapter-level reference notes remain broad in some chapters and should be proofed against the consolidated reference list before final publication.
- Final cover design, edition metadata, release notes, and final PDF export settings remain future publication work.

## Safety Review Reminder

Heat illness symptoms, chest pain, fainting, severe shortness of breath, neurological symptoms, or rapidly worsening symptoms require urgent medical attention. Pain, injury concerns, persistent symptoms, or persistent joint issues should be reviewed with an appropriate coach and clinician.
