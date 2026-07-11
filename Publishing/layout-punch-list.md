---
title: "PDF Layout Punch List"
volume: "Publishing"
status: "review"
last_updated: "2026-07-10"
author: "The Leimbach Method"
---

# PDF Layout Punch List

> **Volume:** Publishing  
> **Status:** Open review items; not final publication guidance

| ID | Page / Section | Problem | Recommended Fix | Priority | Status |
|---|---|---|---|---|---|
| L-001 | PDF artifact / document structure | The committed PDF page tree declares 7 pages, while review notes claim 87 pages. | Rebuild the full manuscript PDF and recommit the correct artifact. Verify the committed blob, not only a local file. | blocker | open |
| L-002 | PDF artifact / xref structure | An earlier automated review reported invalid cross-reference offsets in the PDF. | Generate with a standard PDF library and validate with `qpdf --check`, `pdfinfo`, and a second reader before commit. | blocker | open |
| L-003 | Whole PDF | Full chapter inclusion and source order cannot be confirmed from the committed compact artifact. | Compare the exported chapter list against `MANUSCRIPT.md` and `Publishing/02-table-of-contents.md`; include a build manifest. | blocker | open |
| L-004 | Front matter | Title page, review label, edition metadata, author attribution, and safety disclaimer need a stable reader-facing hierarchy. | Use a dedicated title page followed by a separate disclaimer page and TOC. | high | open |
| L-005 | Table of contents | The full TOC and page numbers have not been verified against the actual committed artifact. | Generate a page-numbered TOC after pagination is final and verify every entry. | high | open |
| L-006 | Chapter openings | Chapter boundaries may blend together in a continuous Markdown-to-PDF export. | Begin every major volume and chapter on a new page with consistent heading treatment. | high | open |
| L-007 | Nutrition and Training tables | Wide tables may become cramped, clipped, or too small on Letter portrait pages. | Use wrapped cells, smaller but readable type, selective landscape pages, or split tables by week/day. | high | open |
| L-008 | Tracking dashboard | Dashboard tables are especially wide and may be difficult to print or complete by hand. | Create a dedicated landscape appendix page or printable dashboard form. | high | open |
| L-009 | Page breaks | Safety notes, tables, and checklists may split across pages in confusing places. | Add keep-together rules for short tables and repeat table headers on continued pages. | high | open |
| L-010 | Repeated review boilerplate | Repeated status lines, source paths, and review disclaimers can dominate the reader experience. | Keep them in the internal review build, but reduce them in the polished publication layout. | medium | open |
| L-011 | Fonts | Monospaced formatting helps preserve tables but can make long chapters tiring to read. | Use a readable proportional body font and reserve monospaced type for code-like tables only. | medium | open |
| L-012 | Headers and footers | Review footer and page numbering need consistent placement without colliding with content. | Standardize running headers by volume and place page numbers outside the main text frame. | medium | open |
| L-013 | Links and paths | Raw repository paths are useful for review but visually noisy in a publication PDF. | Convert internal paths to cleaner chapter references; retain full paths only in a build appendix. | medium | open |
| L-014 | Checkboxes | Markdown checkboxes may render as broken glyphs or inconsistent symbols. | Use tested vector checkbox marks or plain square characters supported by the chosen font. | medium | open |
| L-015 | Metadata | Current PDF metadata has generic or anonymous values. | Set title, author/project, subject, keywords, review status, and generation date explicitly. | medium | open |
| L-016 | Cover design | No final cover system is established. | Create a separate cover/layout issue after the content and proof blockers are resolved. | low | open |
| L-017 | Print testing | Letter-size rendering has not been confirmed on physical print or mobile viewing. | Test at 100% print scale and on a phone/tablet before final export. | low | open |

## Exit Criteria

The layout punch list can move toward closure when the committed PDF is the full manuscript, opens without repair warnings, matches the documented page count, and passes representative visual checks across every volume.