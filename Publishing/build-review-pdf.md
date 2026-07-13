---
title: "Build Review PDF"
volume: "Publishing"
status: "review"
last_updated: "2026-07-12"
author: "Mika Leimbach"
---

# Build Review PDF

> **Volume:** Publishing  
> **Status:** Draft for review; not final publication guidance

## Purpose

This file documents the Version 1.0 review-manuscript PDF build for *Mika’s Method to the Madness*. The output is a proofing artifact, not a final publication PDF. All source chapters remain in `review` status.

## Output

Version 1.0 review PDF output:

- [../dist/Mikas-Method-to-the-Madness-v1.0-review.pdf](../dist/Mikas-Method-to-the-Madness-v1.0-review.pdf)

Version 1.0 final-candidate PDF output:

- [../dist/Mikas-Method-to-the-Madness-v1.0-final-candidate.pdf](../dist/Mikas-Method-to-the-Madness-v1.0-final-candidate.pdf)

The previous compact proof file remains a formatting proof only:

- [../dist/The-Leimbach-method-review-draft.pdf](../dist/The-Leimbach-method-review-draft.pdf)

Do not rename either file as a final PDF until a later publication approval step explicitly authorizes final release.

## Build Script

Run the repeatable build script from the repository root:

```bash
python3 Publishing/build_v1_review_pdf.py
```

To build the clean final-candidate PDF without review/source traceability labels:

```bash
python3 Publishing/build_v1_review_pdf.py --final-candidate
```

The script validates linked source files, assembles the manuscript, creates the PDF, adds page numbers and bookmarks, and generates a linked table of contents. The generated TOC is the reader-facing TOC; the source `Publishing/02-table-of-contents.md` file is not rendered again as body content.

## Source Order

The Version 1.0 review PDF follows [../MANUSCRIPT.md](../MANUSCRIPT.md) and [02-table-of-contents.md](02-table-of-contents.md) for manuscript order, with front/back matter represented by drafted review copy where final publication approval is still pending.

The generated review PDF includes:

1. Cover
2. Title page
3. Copyright page review copy
4. Dedication review copy
5. Foreword review copy
6. Linked table of contents
7. Mika’s Method to the Madness
8. How to Use This Manual
9. Implementation Guide
10. Volume I - Nutrition
11. Volume II - Training
12. Volume III - Recovery
13. Volume IV - Tracking
14. Exercise Library
15. The Promise review copy
16. About the Author review copy
17. References
18. Version History
19. PDF export checklist
20. Final review checklist

## Build Format

The full review PDF is generated from Markdown source files with ReportLab. The build uses proportional typography for body copy, structured tables for Markdown tables, dynamic table column widths, repeated table headers, consistent margins, page numbers, running footer text, PDF bookmarks, code-native visual accents, section divider bands, and a generated table of contents.

The PDF includes:

- Review-draft cover
- Generated date
- Conservative safety disclaimer near the front
- Drafted review copy for front/back matter sections, with final status still withheld
- Page numbers
- Review-draft footer
- Source paths for included chapters
- Review status labels
- Wrapped table and checklist formatting for proof review
- Alternating table row backgrounds for dense worksheet readability
- Code-native cover marks, section bands, chapter accent rules, and footer accents
- PDF bookmarks and linked table of contents entries
- Chapter-level page breaks for cleaner proof review

The final-candidate export writes to a separate file, hides generated `Source:` and `Status:` labels, uses final-candidate cover/footer wording, and adapts front-matter review-manuscript wording for clean proofing. It does not change source chapter front matter, and it does not mark the manuscript final.

## Safety Disclaimer Placement

The title/front-matter section includes the review-draft status and urgent-symptom safety notice. Front matter and relevant chapters also preserve conservative safety language from the Markdown source.

Heat illness symptoms, chest pain, fainting, severe shortness of breath, neurological symptoms, or rapidly worsening symptoms require urgent medical attention.

## Build Checks Before Review

- [x] Confirmed output path is `dist/Mikas-Method-to-the-Madness-v1.0-review.pdf`.
- [x] Confirmed the file is a review PDF, not a final PDF.
- [x] Confirmed source chapters remain in `review` status.
- [x] Confirmed no linked manuscript source files are missing.
- [x] Confirmed no duplicate chapter source files, except intentional front-matter extraction.
- [x] Confirmed safety disclaimer appears near the front.
- [x] Confirmed representative pages were rendered for visual inspection.
- [x] Confirmed page numbers are present.
- [x] Confirmed tables and checklists are readable enough for review proofing.
- [x] Confirmed dense Nutrition, meal-plan, grocery, Training, Tracking, and Exercise Library tables render cleanly.
- [x] Confirmed PDF bookmarks and internal TOC link annotations are present.
- [x] Confirmed no blank pages were detected.
- [x] Confirmed the duplicate source TOC pages are not rendered in the reader-facing PDF body.
- [x] Confirmed raw Markdown link remnants are not visible in extracted PDF text.
- [x] Confirmed front/back matter review copy renders cleanly and remains labeled as review draft material.
- [x] Confirmed clean final-candidate output is available at `dist/Mikas-Method-to-the-Madness-v1.0-final-candidate.pdf`.
- [x] Confirmed final-candidate output hides generated review/source labels while source chapter statuses remain `review`.

## Not Final

This Version 1.0 review PDF is for proofing layout, readability, links, tables, safety disclaimer placement, and page breaks. It should not be distributed as final publication copy.
