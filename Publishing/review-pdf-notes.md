---
title: "Review PDF Notes"
volume: "Publishing"
status: "review"
last_updated: "2026-07-10"
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
| Build date | 2026-07-10 |
| Output file | `dist/The-Leimbach-Method-v1.0-review.pdf` |
| Page count | 117 pages |
| Page size | Letter |
| Source order | `MANUSCRIPT.md`, `Publishing/02-table-of-contents.md`, and Issue 34 front/back matter requirements |
| Review label | Present on cover and footer |
| Page numbers | Present |
| Safety disclaimer near front | Present |
| PDF bookmarks | Present |
| Linked TOC annotations | Present |
| Blank pages | None detected |
| Full manuscript content | Present, with approved placeholders preserved where source copy is not yet present |

## Rendered Pages Checked

Representative pages were rendered to PNG and visually inspected:

| Page | Area Checked | Result |
|---|---|---|
| 1 | Cover/title page | Clean review-cover layout; review-draft label and page footer visible |
| 2 | Linked table of contents | Page numbers present; major sections and chapter entries visible |
| 23 | Nutrition table page | Nutrition table readable; list formatting clean; no obvious clipping, overlap, broken glyphs, or black boxes |
| 77 | Training table page, Six-Week Strength Block | Dense training tables readable with wrapped cells; no obvious clipping or overlap |
| 87 | Recovery/safety page, Heat-Stress Recovery | Safety language visible; heat-stress content readable |
| 102 | Tracking dashboard/checklist page | Dashboard and weekly metrics tables readable |
| 117 | Final Review Checklist | Final checklist text readable; no obvious clipping or overlap |

## Verification Notes

- `pdfinfo` reported 117 pages, Letter page size, and readable metadata.
- `pypdf` reported 117 pages, zero blank pages, 146 link annotations, and PDF outline entries.
- Source validation reported no missing manuscript source files.
- Duplicate source validation reported no duplicate chapter sources, except intentional extraction from `Publishing/03-front-matter.md` for title/safety and how-to-use sections.
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
