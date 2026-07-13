from __future__ import annotations

import html
import os
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
    LongTable,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
BOOK_TITLE = "Mika’s Method to the Madness"
BOOK_SUBTITLE = "Powerbuilding, Nutrition, Recovery, and Performance"
REVIEW_LABEL = "Version 1.0 Review Manuscript"
FINAL_CANDIDATE_LABEL = "Version 1.0 Final Candidate"

OUT = ROOT / "dist" / "Mikas-Method-to-the-Madness-v1.0-review.pdf"
FINAL_CANDIDATE_OUT = ROOT / "dist" / "Mikas-Method-to-the-Madness-v1.0-final-candidate.pdf"
BUILD_NOTES = ROOT / "Publishing" / "review-pdf-notes.md"


@dataclass(frozen=True)
class Chapter:
    section: str
    title: str
    path: Path | None
    source_note: str | None = None


CHAPTERS = [
    Chapter("Front Matter", "Cover", None, "Generated text cover for review. Final cover artwork is not present in the repository."),
    Chapter("Front Matter", "Title Page", ROOT / "Publishing/03-front-matter.md"),
    Chapter("Front Matter", "Copyright Page", ROOT / "Publishing/03-front-matter.md"),
    Chapter("Front Matter", "Dedication", ROOT / "Publishing/03-front-matter.md"),
    Chapter("Front Matter", "Foreword", ROOT / "Publishing/03-front-matter.md"),
    Chapter("Foundation", "The Leimbach Philosophy", ROOT / "README.md"),
    Chapter("Foundation", "How to Use This Manual", ROOT / "Publishing/03-front-matter.md"),
    Chapter("Implementation Guide", "Start Here", ROOT / "Implementation/01-start-here.md"),
    Chapter("Implementation Guide", "First-Week Setup", ROOT / "Implementation/02-first-week-setup.md"),
    Chapter("Implementation Guide", "Week One Entry", ROOT / "Implementation/03-week-one-entry.md"),
    Chapter("Implementation Guide", "Weekly Operating Rhythm", ROOT / "Implementation/04-weekly-operating-rhythm.md"),
    Chapter("Implementation Guide", "Common Scenarios", ROOT / "Implementation/05-common-scenarios.md"),
    Chapter("Implementation Guide", "User Checklists", ROOT / "Implementation/06-user-checklists.md"),
    Chapter("Volume I - Nutrition", "Athlete Profile", ROOT / "Nutrition/01-athlete-profile.md"),
    Chapter("Volume I - Nutrition", "Goals and Nutrition Philosophy", ROOT / "Nutrition/02-goals-and-nutrition-philosophy.md"),
    Chapter("Volume I - Nutrition", "Macro Targets", ROOT / "Nutrition/03-macro-targets.md"),
    Chapter("Volume I - Nutrition", "Day-Shift Meal Timing", ROOT / "Nutrition/04-day-shift-meal-timing.md"),
    Chapter("Volume I - Nutrition", "Night-Shift Meal Timing", ROOT / "Nutrition/05-night-shift-meal-timing.md"),
    Chapter("Volume I - Nutrition", "Training, Cardio, and Rest-Day Nutrition", ROOT / "Nutrition/06-day-type-nutrition.md"),
    Chapter("Volume I - Nutrition", "Fourteen-Day Meal Plan", ROOT / "Nutrition/07-fourteen-day-meal-plan.md"),
    Chapter("Volume I - Nutrition", "Meal-Prep Workflow", ROOT / "Nutrition/08-meal-prep-workflow.md"),
    Chapter("Volume I - Nutrition", "Costco and H-E-B Grocery Guide", ROOT / "Nutrition/09-grocery-guide.md"),
    Chapter("Volume I - Nutrition", "Hydration and Electrolytes", ROOT / "Nutrition/10-hydration-electrolytes.md"),
    Chapter("Volume I - Nutrition", "Supplement Framework", ROOT / "Nutrition/11-supplements.md"),
    Chapter("Volume I - Nutrition", "Progress and Macro Adjustments", ROOT / "Nutrition/12-adjustment-protocol.md"),
    Chapter("Volume II - Training", "Program Overview", ROOT / "Training/01-program-overview.md"),
    Chapter("Volume II - Training", "Readiness and Autoregulation", ROOT / "Training/02-readiness-autoregulation.md"),
    Chapter("Volume II - Training", "Warm-Up and Movement Preparation", ROOT / "Training/03-warm-up-mobility.md"),
    Chapter("Volume II - Training", "Squat Development", ROOT / "Training/04-squat-system.md"),
    Chapter("Volume II - Training", "Bench Press Development", ROOT / "Training/05-bench-system.md"),
    Chapter("Volume II - Training", "Deadlift Development", ROOT / "Training/06-deadlift-system.md"),
    Chapter("Volume II - Training", "Accessory Training", ROOT / "Training/07-accessory-training.md"),
    Chapter("Volume II - Training", "Core Training", ROOT / "Training/08-core-training.md"),
    Chapter("Volume II - Training", "Conditioning", ROOT / "Training/09-conditioning.md"),
    Chapter("Volume II - Training", "Deloads and Fatigue Management", ROOT / "Training/10-deloads.md"),
    Chapter("Volume II - Training", "Six-Week Strength Block", ROOT / "Training/11-four-week-training-block.md"),
    Chapter("Volume II - Training", "Progression Rules", ROOT / "Training/12-progression-rules.md"),
    Chapter("Volume III - Recovery", "Recovery Overview", ROOT / "Recovery/01-recovery-overview.md"),
    Chapter("Volume III - Recovery", "Sleep System", ROOT / "Recovery/02-sleep-system.md"),
    Chapter("Volume III - Recovery", "Shift-Work Recovery", ROOT / "Recovery/03-shift-work-recovery.md"),
    Chapter("Volume III - Recovery", "Heat-Stress Recovery", ROOT / "Recovery/04-heat-stress-recovery.md"),
    Chapter("Volume III - Recovery", "Soreness and Pain Management", ROOT / "Recovery/05-soreness-pain-management.md"),
    Chapter("Volume III - Recovery", "Weekly Recovery Planning", ROOT / "Recovery/06-weekly-recovery-planning.md"),
    Chapter("Volume III - Recovery", "Recovery Checklists", ROOT / "Recovery/07-recovery-checklists.md"),
    Chapter("Volume IV - Tracking", "Tracking Overview", ROOT / "Tracking/01-tracking-overview.md"),
    Chapter("Volume IV - Tracking", "Bodyweight and Waist Tracking", ROOT / "Tracking/02-bodyweight-waist.md"),
    Chapter("Volume IV - Tracking", "Training Log", ROOT / "Tracking/03-training-log.md"),
    Chapter("Volume IV - Tracking", "Recovery Log", ROOT / "Tracking/04-recovery-log.md"),
    Chapter("Volume IV - Tracking", "Weekly Review", ROOT / "Tracking/05-weekly-review.md"),
    Chapter("Volume IV - Tracking", "Dashboard Template", ROOT / "Tracking/06-dashboard-template.md"),
    Chapter("Exercise Library", "Library Overview", ROOT / "Exercise-Library/01-library-overview.md"),
    Chapter("Exercise Library", "Squat Variations", ROOT / "Exercise-Library/02-squat-variations.md"),
    Chapter("Exercise Library", "Bench Variations", ROOT / "Exercise-Library/03-bench-variations.md"),
    Chapter("Exercise Library", "Deadlift Variations", ROOT / "Exercise-Library/04-deadlift-variations.md"),
    Chapter("Exercise Library", "Accessories", ROOT / "Exercise-Library/05-accessories.md"),
    Chapter("Exercise Library", "Core and Conditioning", ROOT / "Exercise-Library/06-core-conditioning.md"),
    Chapter("Exercise Library", "Substitution Rules", ROOT / "Exercise-Library/07-substitution-rules.md"),
    Chapter("Back Matter", "The Promise", ROOT / "Publishing/04-back-matter.md"),
    Chapter("Back Matter", "About the Author", ROOT / "Publishing/04-back-matter.md"),
    Chapter("Back Matter", "References", ROOT / "REFERENCES.md"),
    Chapter("Back Matter", "Version History", ROOT / "Publishing/04-back-matter.md"),
    Chapter("Back Matter", "PDF Export Checklist", ROOT / "Publishing/05-pdf-export-checklist.md"),
    Chapter("Back Matter", "Final Review Checklist", ROOT / "Publishing/06-final-review-checklist.md"),
]


def read_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data, text[end + 5 :]


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"[Image: \1]", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("*", "")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("✓", "[x]")
    return html.escape(text, quote=False)


def styles():
    base = getSampleStyleSheet()
    base.add(ParagraphStyle("CoverTitle", parent=base["Title"], fontName="Times-Bold", fontSize=32, leading=36, alignment=TA_CENTER, spaceAfter=18))
    base.add(ParagraphStyle("CoverSub", parent=base["Normal"], fontName="Times-Roman", fontSize=15, leading=20, alignment=TA_CENTER, spaceAfter=10))
    base.add(ParagraphStyle("PartTitle", parent=base["Title"], fontName="Times-Bold", fontSize=24, leading=30, alignment=TA_CENTER, spaceAfter=16))
    base.add(ParagraphStyle("ChapterTitle", parent=base["Heading1"], fontName="Times-Bold", fontSize=20, leading=24, spaceAfter=12, keepWithNext=True))
    base.add(ParagraphStyle("H2", parent=base["Heading2"], fontName="Times-Bold", fontSize=12.2, leading=14.4, spaceBefore=7, spaceAfter=3, keepWithNext=True))
    base.add(ParagraphStyle("H3", parent=base["Heading3"], fontName="Times-BoldItalic", fontSize=10.5, leading=12.4, spaceBefore=6, spaceAfter=3, keepWithNext=True))
    base.add(ParagraphStyle("Body", parent=base["BodyText"], fontName="Times-Roman", fontSize=8.6, leading=10.4, spaceAfter=3.2))
    base.add(ParagraphStyle("Small", parent=base["BodyText"], fontName="Times-Roman", fontSize=7.2, leading=8.4, spaceAfter=2.6))
    base.add(ParagraphStyle("Tiny", parent=base["BodyText"], fontName="Times-Roman", fontSize=6.7, leading=7.8, spaceAfter=1.8))
    base.add(ParagraphStyle("TableHeader", parent=base["BodyText"], fontName="Times-Bold", fontSize=7, leading=8.1, textColor=colors.HexColor("#111111"), spaceAfter=1.8))
    base.add(ParagraphStyle("Meta", parent=base["BodyText"], fontName="Times-Italic", fontSize=8, leading=10, textColor=colors.HexColor("#555555"), spaceAfter=8))
    base.add(ParagraphStyle("List", parent=base["BodyText"], fontName="Times-Roman", fontSize=8.4, leading=10.2, leftIndent=14, firstLineIndent=-8, spaceAfter=2))
    base.add(ParagraphStyle("TOCHeading", parent=base["Heading1"], fontName="Times-Bold", fontSize=24, leading=28, alignment=TA_CENTER, spaceAfter=16))
    return base


STYLES = styles()


PLACEHOLDER_INSTRUCTIONS = {
    "Cover": [
        "Final cover artwork, subtitle treatment, edition metadata, and final cover design still require author approval.",
        "This review build uses a text cover only.",
    ],
}


@dataclass(frozen=True)
class BuildMode:
    output: Path
    label: str
    metadata_status: str
    footer: str
    show_source_labels: bool
    show_review_cover_note: bool


REVIEW_MODE = BuildMode(
    output=OUT,
    label=REVIEW_LABEL,
    metadata_status="Review",
    footer=f"{BOOK_TITLE} v1.0 Review",
    show_source_labels=True,
    show_review_cover_note=True,
)

FINAL_CANDIDATE_MODE = BuildMode(
    output=FINAL_CANDIDATE_OUT,
    label=FINAL_CANDIDATE_LABEL,
    metadata_status="Final Candidate",
    footer=f"{BOOK_TITLE} v1.0 Final Candidate",
    show_source_labels=False,
    show_review_cover_note=False,
)


class ReviewDoc(BaseDocTemplate):
    def __init__(self, filename: str, mode: BuildMode):
        super().__init__(
            filename,
            pagesize=letter,
            leftMargin=0.58 * inch,
            rightMargin=0.58 * inch,
            topMargin=0.62 * inch,
            bottomMargin=0.58 * inch,
            title=f"{BOOK_TITLE} v1.0 {mode.metadata_status}",
            author="Mika Leimbach",
            subject=f"Version 1.0 {mode.metadata_status.lower()} manuscript",
        )
        self.mode = mode
        body = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates([PageTemplate(id="body", frames=[body], onPage=self.draw_page)])
        self._heading_count = 0
        self._running = mode.footer

    def afterFlowable(self, flowable):
        if hasattr(flowable, "_bookmark_title"):
            title = flowable._bookmark_title
            level = flowable._bookmark_level
            key = flowable._bookmark_key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=level > 0)
            self.notify("TOCEntry", (level, title, self.page, key))
            if level == 0:
                self._running = title

    def draw_page(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#d0d0d0"))
        canvas.setLineWidth(0.3)
        canvas.line(doc.leftMargin, 0.55 * inch, doc.pagesize[0] - doc.rightMargin, 0.55 * inch)
        canvas.setFont("Times-Roman", 8)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawString(doc.leftMargin, 0.38 * inch, self.mode.footer)
        canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 0.38 * inch, str(doc.page))
        canvas.restoreState()


def bookmark_para(text: str, style_name: str, level: int) -> Paragraph:
    key = "h_%04d" % bookmark_para.counter
    bookmark_para.counter += 1
    p = Paragraph(clean_inline(text), STYLES[style_name])
    p._bookmark_title = text
    p._bookmark_level = level
    p._bookmark_key = key
    return p


bookmark_para.counter = 1


def parse_table(rows: list[str]) -> Table:
    parsed: list[list[str]] = []
    for row in rows:
        cells = [clean_inline(c.strip()) for c in row.strip().strip("|").split("|")]
        if cells and all(set(c.replace(":", "").strip()) <= {"-"} for c in cells):
            continue
        parsed.append(cells)
    if not parsed:
        parsed = [[""]]
    width = 7.34 * inch
    columns = max(len(r) for r in parsed)
    normalized = [r + [""] * (columns - len(r)) for r in parsed]
    dense = columns >= 6 or len(normalized) >= 12
    body_style = STYLES["Tiny"] if dense else STYLES["Small"]
    weights: list[float] = []
    for col in range(columns):
        values = [re.sub(r"<[^>]+>", "", row[col]) for row in normalized]
        longest = max((len(v) for v in values), default=1)
        average = sum(len(v) for v in values) / max(len(values), 1)
        weights.append(max(4.0, min(24.0, longest * 0.7 + average * 0.3)))
    total = sum(weights) or 1
    col_widths = [width * weight / total for weight in weights]
    min_width = (0.42 if dense else 0.58) * inch
    max_width = (1.9 if dense else 2.7) * inch
    col_widths = [max(min_width, min(max_width, w)) for w in col_widths]
    scale = width / sum(col_widths)
    col_widths = [w * scale for w in col_widths]
    data = []
    for row_index, row in enumerate(normalized):
        style = STYLES["TableHeader"] if row_index == 0 else body_style
        data.append([Paragraph(c, style) for c in row])
    table_class = LongTable if len(normalized) >= 10 else Table
    table = table_class(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e4e7eb")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111111")),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#c8c8c8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.4 if dense else 3.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.4 if dense else 3.2),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f7f7")]),
    ]
    table.setStyle(TableStyle(commands))
    return table


def parse_markdown(text: str, include_ranges: tuple[str, str] | None = None) -> list:
    _, body = read_front_matter(text)
    if include_ranges:
        start, end = include_ranges
        start_idx = body.find(start)
        if start_idx >= 0:
            end_idx = body.find(end, start_idx + len(start)) if end else -1
            body = body[start_idx:end_idx if end_idx >= 0 else None]
    flow: list = []
    paragraph: list[str] = []
    table_rows: list[str] = []
    bullets: list[str] = []

    def flush_paragraph():
        if paragraph:
            flow.append(Paragraph(clean_inline(" ".join(paragraph)), STYLES["Body"]))
            paragraph.clear()

    def flush_table():
        if table_rows:
            flow.append(parse_table(table_rows))
            flow.append(Spacer(1, 6))
            table_rows.clear()

    def flush_bullets():
        if bullets:
            for item in bullets:
                flow.append(Paragraph("- " + clean_inline(item), STYLES["List"]))
            bullets.clear()

    for raw in body.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("> **Volume:**") or stripped.startswith("> **Chapter:**") or stripped.startswith("> **Status:**"):
            continue
        if not stripped:
            flush_paragraph()
            flush_table()
            flush_bullets()
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            flush_bullets()
            table_rows.append(stripped)
            continue
        flush_table()
        if stripped.startswith("# "):
            flush_paragraph()
            flush_bullets()
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            flush_bullets()
            flow.append(Paragraph(clean_inline(stripped[3:]), STYLES["H2"]))
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            flush_bullets()
            flow.append(Paragraph(clean_inline(stripped[4:]), STYLES["H3"]))
            continue
        bullet_match = re.match(r"^([-*]|\d+\.)\s+(.*)$", stripped)
        if bullet_match:
            flush_paragraph()
            item = re.sub(r"^\[[ xX]\]\s+", "", bullet_match.group(2))
            bullets.append(item)
            continue
        paragraph.append(stripped)
    flush_paragraph()
    flush_table()
    flush_bullets()
    return flow


def source_meta(path: Path | None) -> dict[str, str]:
    if path is None:
        return {"status": "review"}
    fm, _ = read_front_matter(path.read_text())
    return fm


def render_text_for_mode(text: str, mode: BuildMode) -> str:
    if mode.show_source_labels:
        return text
    text = text.replace("Version 1.0 Review Manuscript", "Version 1.0 Final Candidate")
    text = text.replace(
        "This review manuscript is built for author, coaching, safety, copy, layout, and PDF proof review before any final publication decision. It is not final publication copy.",
        "This final-candidate manuscript is built for author, coaching, safety, copy, layout, and PDF proofing before any publication decision. It is not final publication copy.",
    )
    text = text.replace(
        "This is a Version 1.0 review manuscript of *Mika’s Method to the Madness*. It is provided for review, proofing, and author approval. No part of this review manuscript should be reproduced, distributed, sold, or represented as final publication copy without written permission from the author.",
        "This is a Version 1.0 final-candidate manuscript of *Mika’s Method to the Madness*. It is provided for proofing and author approval. No part of this manuscript should be reproduced, distributed, sold, or represented as final publication copy without written permission from the author.",
    )
    text = text.replace("included for manuscript review", "included for final-candidate proofing")
    text = text.replace(
        "This review draft should still be challenged. The programming should be reviewed. The safety language should be reviewed. The nutrition should be checked for practicality. The PDF should be proofed before publication. Nothing here becomes final because it looks finished; it becomes final only after it holds up under review.",
        "This final candidate should still be challenged. The programming should be checked. The safety language should be checked. The nutrition should be checked for practicality. The PDF should be proofed before publication. Nothing here becomes final because it looks finished; it becomes final only after it holds up under approval.",
    )
    text = re.sub(r"\n## Review Draft Notice\n.*?(?=\n## Safety Disclaimer\n)", "\n", text, flags=re.S)
    return text


def chapter_story(chapter: Chapter, previous_section: str | None, mode: BuildMode) -> list:
    flow: list = [PageBreak()]
    if chapter.section != previous_section:
        flow.append(bookmark_para(chapter.section, "PartTitle", 0))
        flow.append(Spacer(1, 16))
    flow.append(bookmark_para(chapter.title, "ChapterTitle", 1))
    meta = source_meta(chapter.path)
    status = meta.get("status", "review")
    source = chapter.path.relative_to(ROOT).as_posix() if chapter.path else "Generated review placeholder"
    if mode.show_source_labels:
        flow.append(Paragraph(f"Source: {source} | Status: {clean_inline(status)}", STYLES["Meta"]))
    if chapter.source_note and mode.show_source_labels:
        flow.append(Paragraph(clean_inline(chapter.source_note), STYLES["Meta"]))
    if chapter.path is None:
        flow.append(Paragraph("Review placeholder - final copy needed.", STYLES["H2"]))
        for note in PLACEHOLDER_INSTRUCTIONS.get(chapter.title, []):
            flow.append(Paragraph(clean_inline(note), STYLES["Body"]))
        flow.append(Spacer(1, 6))
        flow.append(Paragraph("This placeholder is intentionally preserved for review and does not mark the manuscript final.", STYLES["Meta"]))
        return flow
    text = render_text_for_mode(chapter.path.read_text(), mode)
    if chapter.title == "Title Page":
        flow.extend(parse_markdown(text, ("## Title Page", "## Copyright Page")))
        flow.extend(parse_markdown(text, ("## Safety Disclaimer", "## How To Use This Manual")))
    elif chapter.title == "Copyright Page":
        flow.extend(parse_markdown(text, ("## Copyright Page", "## Dedication")))
    elif chapter.title == "Dedication":
        flow.extend(parse_markdown(text, ("## Dedication", "## Foreword")))
    elif chapter.title == "Foreword":
        flow.extend(parse_markdown(text, ("## Foreword", "## Author And Project Attribution")))
    elif chapter.title == "How to Use This Manual":
        flow.extend(parse_markdown(text, ("## How To Use This Manual", "## Who This Manual Is For")))
    elif chapter.title == "The Leimbach Philosophy":
        flow.extend(parse_markdown(text, ("## Who This Method Is For", "## Main Sections")))
    elif chapter.title == "Version History":
        flow.extend(parse_markdown(text, ("## Version History Review Placeholder", "## Appendix List Review Placeholder")))
    elif chapter.title == "The Promise":
        flow.extend(parse_markdown(text, ("## The Promise", "## About the Author")))
    elif chapter.title == "About the Author":
        flow.extend(parse_markdown(text, ("## About the Author", "## Reference Note")))
    else:
        flow.extend(parse_markdown(text))
    return flow


def cover_story(mode: BuildMode) -> list:
    story = [
        Spacer(1, 1.35 * inch),
        Paragraph(mode.label.upper(), STYLES["CoverSub"]),
        Spacer(1, 0.35 * inch),
        Paragraph(BOOK_TITLE.upper(), STYLES["CoverTitle"]),
        Paragraph(BOOK_SUBTITLE, STYLES["CoverSub"]),
        Spacer(1, 0.6 * inch),
        Paragraph(mode.label, STYLES["CoverSub"]),
        Paragraph(f"Generated {date.today().isoformat()}", STYLES["CoverSub"]),
        Spacer(1, 0.8 * inch),
    ]
    if mode.show_review_cover_note:
        story.append(Paragraph("Review draft - not final publication copy", STYLES["CoverSub"]))
    story.append(Paragraph("Final cover artwork pending author approval", STYLES["CoverSub"]))
    story.append(PageBreak())
    return story


def validate_sources() -> tuple[list[str], list[str]]:
    paths = [c.path.relative_to(ROOT).as_posix() for c in CHAPTERS if c.path is not None]
    missing = [p for p in paths if not (ROOT / p).exists()]
    duplicates = sorted({p for p in paths if paths.count(p) > 1})
    return missing, duplicates


def build(mode: BuildMode = REVIEW_MODE) -> None:
    missing, duplicates = validate_sources()
    if missing:
        raise SystemExit("Missing manuscript files:\n" + "\n".join(missing))
    mode.output.parent.mkdir(exist_ok=True)
    story = cover_story(mode)
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOCLevel0", fontName="Times-Bold", fontSize=11, leading=14, leftIndent=0, firstLineIndent=0, spaceBefore=5),
        ParagraphStyle("TOCLevel1", fontName="Times-Roman", fontSize=9.4, leading=12, leftIndent=18, firstLineIndent=-12),
    ]
    story.append(bookmark_para("Table of Contents", "TOCHeading", 0))
    story.append(toc)
    previous: str | None = None
    for chapter in CHAPTERS[1:]:
        story.extend(chapter_story(chapter, previous, mode))
        previous = chapter.section
    doc = ReviewDoc(str(mode.output), mode)
    doc.multiBuild(story)


if __name__ == "__main__":
    selected_mode = FINAL_CANDIDATE_MODE if "--final-candidate" in sys.argv else REVIEW_MODE
    build(selected_mode)
    print(selected_mode.output)
