---
title: "Build Review PDF"
volume: "Publishing"
status: "review"
last_updated: "2026-07-09"
author: "The Leimbach Method"
---

# Build Review PDF

> **Volume:** Publishing  
> **Status:** Draft for review; not final publication guidance

## Purpose

This file documents the first compact review PDF build for The Leimbach Method. The output is a proofing artifact, not a final publication PDF. All source chapters remain in `review` status.

## Output

Review PDF output:

- [../dist/The-Leimbach-method-review-draft.pdf](../dist/The-Leimbach-method-review-draft.pdf)

Do not rename this file as a final PDF until a later publication approval step explicitly authorizes final release.

## Source Order

The review PDF uses [../MANUSCRIPT.md](../MANUSCRIPT.md) and [02-table-of-contents.md](02-table-of-contents.md) as the source order.

The generated review PDF includes:

1. Front matter and title page placeholder
2. Safety disclaimer near the front
3. Table of contents
4. Implementation Guide
5. Volume I - Nutrition
6. Volume II - Training
7. Volume III - Recovery
8. Volume IV - Tracking
9. Exercise Library
10. Back matter
11. PDF export checklist
12. Final review checklist

## Build Format

The first review PDF was generated from the manuscript assembly and table of contents using a local ReportLab build process. The artifact is a compact proof draft: it includes the front safety notice, source order, section/volume order, and representative table/checklist pages for layout review before a later full-manuscript PDF pass.

The PDF includes:

- Review-draft title page
- Generated date
- Conservative safety disclaimer near the front
- Page numbers
- Review-draft footer
- Source-order table with repository paths
- Review status labels
- Representative table formatting for proof review

## Safety Disclaimer Placement

The title/front page includes the review-draft status and urgent-symptom safety notice. Front matter and relevant chapters also preserve conservative safety language from the Markdown source.

Heat illness symptoms, chest pain, fainting, severe shortness of breath, neurological symptoms, or rapidly worsening symptoms require urgent medical attention.

## Build Checks Before Review

- [x] Confirmed output path is `dist/The-Leimbach-method-review-draft.pdf`.
- [x] Confirmed the file is a review PDF, not a final PDF.
- [x] Confirmed source chapters remain in `review` status.
- [x] Confirmed safety disclaimer appears near the front.
- [x] Confirmed representative pages were rendered for visual inspection.
- [x] Confirmed page numbers are present.
- [x] Confirmed tables and checklists are readable enough for review proofing.

## Not Final

This review PDF is for proofing layout, readability, links, tables, safety disclaimer placement, and page breaks. It should not be distributed as final publication copy.
