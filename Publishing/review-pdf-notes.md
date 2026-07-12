---
title: "Review PDF Notes"
volume: "Publishing"
status: "review"
last_updated: "2026-07-12"
author: "The Leimbach Method"
---

# Review PDF Notes

> **Volume:** Publishing  
> **Status:** Draft for review; not final publication guidance

## Review PDF Artifact

Generated Version 1.0 review PDF:

- [../dist/The-Leimbach-Method-v1.0-review.pdf](../dist/The-Leimbach-Method-v1.0-review.pdf)

This artifact is a review draft only. It does not mark the manuscript final and does not change any chapter status to `final`.

## Build Summary

| Item | Result |
|---|---|
| Build date | 2026-07-12 |
| Output file | `dist/The-Leimbach-Method-v1.0-review.pdf` |
| Page count | 141 pages |
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
| Full manuscript content | Present, with approved placeholders preserved where source copy is not yet present |

## Rendered Pages Checked

Representative pages were rendered to PNG and visually inspected:

| Page | Area Checked | Result |
|---|---|---|
| 1 | Cover/title page | Clean review-cover layout; review-draft label and page footer visible |
| 2-4 | Linked table of contents | Page numbers present; major sections and chapter entries visible |
| 5-10 | Front matter and foundation | Source TOC body pages removed; placeholders and safety disclaimer remain visible |
| 24, 27 | Nutrition table pages | Nutrition tables readable; no obvious clipping, overlap, broken glyphs, or black boxes |
| 40, 44, 50, 55 | Meal plan, meal prep, and grocery pages | Dense tables remain readable enough for review proofing |
| 67, 74, 76, 84, 89 | Training table pages | Training tables readable with wrapped cells; chapter starts are cleaner |
| 101, 104 | Recovery/safety pages | Heat-stress chapter starts on a clean page; safety language remains visible |
| 119-120 | Tracking dashboard/checklist pages | Dashboard and weekly metrics tables readable |
| 122, 125 | Exercise Library table pages | Substitution and variation tables readable |
| 137-141 | References, Version History, Final Review Checklist | Back matter and final checklist readable; placeholders remain clearly labeled |

## Verification Notes

- `pdfinfo` reported 141 pages, Letter page size, and readable metadata.
- `pypdf` reported 141 pages, zero blank pages, 144 link annotations, 72 PDF outline entries, and zero unresolved internal TOC link destinations.
- Source validation reported no missing manuscript source files.
- Duplicate source validation reported no duplicate chapter sources, except intentional extraction from `Publishing/03-front-matter.md` for title/safety and how-to-use sections.
- The generated linked TOC remains near the front; the source `Publishing/02-table-of-contents.md` body is no longer rendered as duplicate reader-facing TOC pages.
- Text extraction checks found no raw Markdown link remnants such as `](../` or `Start Here]`.
- Representative pages were rendered with Poppler `pdftoppm`.
- `qpdf` was not installed in this environment, so the PDF was validated with `pdfinfo`, `pypdf`, and rendered PNG inspection instead.
- The generated PDF uses readable repository source paths near chapter starts for review traceability.
- Tables and checklists are preserved with wrapped table cells for review readability, not final publication typography.
- The final PDF has not been created.

## Known Limitations For Later Proofing

- Copyright, dedication, foreword, The Promise, and About the Author remain placeholder sections because approved manuscript copy is not present in the repository.
- Very wide source tables may still need final layout tuning before publication.
- References remain broad in some chapters and should be proofed before final publication.
- Final cover design, edition metadata, release notes, and final PDF export settings remain future publication work.

## Safety Review Reminder

Heat illness symptoms, chest pain, fainting, severe shortness of breath, neurological symptoms, or rapidly worsening symptoms require urgent medical attention. Pain, injury concerns, persistent symptoms, or persistent joint issues should be reviewed with an appropriate coach and clinician.
