#!/usr/bin/env python3
"""Generate the complete Markdown framework for The Leimbach Method.

Run from the repository root:
    python3 bootstrap_repository.py
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(text).strip() + "\n", encoding="utf-8")


def slug(text: str) -> str:
    return (text.lower().replace("&", "and").replace("—", "")
            .replace(":", "").replace("/", "").replace(" ", "-"))


def chapter(title: str, volume: str, number: int, purpose: str, sections: list[str], refs: bool = True) -> str:
    toc = "\n".join(f"- [{section}](#{slug(section)})" for section in sections)
    body = []
    for section in sections:
        body.append(f"""
## {section}

> **Draft note:** Replace this callout with finalized coaching guidance, data, or narrative.

### Key Points

- 
- 
- 

### Working Table

| Item | Target / Standard | Notes |
|---|---:|---|
|  |  |  |
|  |  |  |

### Figure or Image Placeholder

![{section} illustration](../Assets/Images/placeholder-{number:02d}.jpg)

*Figure {number}.1 — Add a concise caption and source credit.*
""")
    reference_block = """
## References

1. Author or Organization. *Title of source*. Publisher or Journal, Year.
2. Add a stable URL, DOI, edition, or access date where applicable.
3. Use numbered citations in the text, such as **[1]**.

> **Reference status:** Draft placeholders only. Verify every citation before publication.
""" if refs else ""
    return f"""---
title: "{title}"
volume: "{volume}"
chapter: {number}
status: "template"
last_updated: "2026-07-08"
author: "The Leimbach Method"
---

# {title}

> **Volume:** {volume}  
> **Chapter:** {number}  
> **Status:** Template / not final coaching guidance

## Purpose

{purpose}

## Chapter Contents

{toc}

---

{''.join(body)}

## Action Checklist

- [ ] Finalize chapter text.
- [ ] Verify quantities, calculations, and claims.
- [ ] Add tables or figures where they improve understanding.
- [ ] Add image captions and source credits.
- [ ] Complete references.
- [ ] Review formatting and internal links.
- [ ] Mark status as `review` or `final` in the front matter.

## Coach Review Notes

- 
- 
- 

{reference_block}
"""


def build_volume(folder: str, volume: str, records: list[tuple[str, str, str, list[str]]], refs: bool = True) -> None:
    for number, (filename, title, purpose, sections) in enumerate(records, 1):
        write(f"{folder}/{filename}", chapter(title, volume, number, purpose, sections, refs))


nutrition = [
("01-athlete-profile.md", "Athlete Profile", "Document the athlete's current profile, work demands, training history, preferences, constraints, and measurable objectives.", ["Profile Snapshot", "Work and Schedule Demands", "Training Background", "Nutrition Preferences", "Health and Recovery Context", "Primary Outcomes"]),
("02-goals-and-nutrition-philosophy.md", "Goals and Nutrition Philosophy", "Define the principles that guide the nutrition system and translate the 260-to-275-lb objective into realistic performance outcomes.", ["Mission", "Desired Rate of Gain", "Performance Priorities", "Food Quality and Flexibility", "Consistency Standards", "Success Criteria"]),
("03-macro-targets.md", "Macro Targets", "Establish starting calorie and macronutrient targets with clear assumptions and adjustment ranges.", ["Starting Assumptions", "Training-Day Targets", "Cardio-Day Targets", "Rest-Day Targets", "Meal Distribution", "Monitoring and Recalculation"]),
("04-day-shift-meal-timing.md", "Day-Shift Meal Timing", "Create a practical meal and hydration schedule for a 3:00 a.m. to 7:00 p.m. workday.", ["Shift Timeline", "Wake-Up Meal", "Work Meals", "Training Window", "Post-Training Meal", "Bedtime Nutrition"]),
("05-night-shift-meal-timing.md", "Night-Shift Meal Timing", "Create a practical meal and hydration schedule for a 3:00 p.m. to 7:00 a.m. work night.", ["Shift Timeline", "Pre-Shift Meal", "Overnight Meals", "Training Window", "Post-Shift Meal", "Sleep Preparation"]),
("06-day-type-nutrition.md", "Training, Cardio, and Rest-Day Nutrition", "Explain how food quantity and meal timing change by activity type.", ["Training Days", "Cardio Days", "Rest Days", "Pre-Workout Nutrition", "Post-Workout Nutrition", "Substitution Rules"]),
("07-fourteen-day-meal-plan.md", "Fourteen-Day Meal Plan", "Provide a two-week rotating meal schedule with portions, daily totals, timing, and prep notes.", ["Week One Overview", "Week One Schedule", "Week Two Overview", "Week Two Schedule", "Daily Macro Totals", "Meal Swaps"]),
("08-meal-prep-workflow.md", "Meal-Prep Workflow", "Build an efficient, food-safe workflow for preparing, packaging, transporting, storing, freezing, and reheating meals.", ["Planning", "Batch Cooking Order", "Portioning", "Cooling and Storage", "Freezing", "Work-Cooler Packing"]),
("09-grocery-guide.md", "Costco and H-E-B Grocery Guide", "Organize exact quantities by store, aisle, cost priority, shelf life, and meal-plan use.", ["Shopping Strategy", "Costco List", "H-E-B List", "Quantities", "Budget Notes", "Substitutions"]),
("10-hydration-electrolytes.md", "Hydration and Electrolytes", "Create a shift-aware hydration system for heavy training, cardio, and West Texas heat exposure.", ["Baseline Fluids", "Heat and Sweat Loss", "Sodium", "Potassium and Magnesium", "Work-Shift Schedule", "Warning Signs"]),
("11-supplements.md", "Supplement Framework", "Separate useful supplements from optional or unsupported products and document timing, dose, evidence, and precautions.", ["Decision Framework", "Performance Supplements", "Convenience Supplements", "Micronutrients", "Timing", "Safety and Medical Review"]),
("12-adjustment-protocol.md", "Progress and Macro Adjustments", "Define the weekly decision process for bodyweight, waist, performance, hunger, digestion, and recovery.", ["Data Collection", "Weekly Average", "Rate-of-Gain Rules", "Calorie Adjustments", "Plateau Troubleshooting", "Decision Log"]),
]

training = [
("01-program-overview.md", "Program Overview", "Define the training system, annual structure, priorities, constraints, and progression model.", ["Training Mission", "Weekly Structure", "Annual Phases", "Main-Lift Priorities", "Volume and Intensity", "Success Metrics"]),
("02-readiness-autoregulation.md", "Readiness and Autoregulation", "Adapt training to long shifts, sleep, heat, pain, and performance.", ["Readiness Inputs", "Daily Score", "RPE and RIR", "Green Yellow Red Decisions", "Volume Adjustments", "Examples"]),
("03-warm-up-mobility.md", "Warm-Up and Movement Preparation", "Standardize general warm-up, dynamic mobility, activation, and lift-specific ramp-up sets.", ["General Warm-Up", "Dynamic Mobility", "Lift-Specific Preparation", "Ramp-Up Sets", "Time-Saving Version", "Common Errors"]),
("04-squat-system.md", "Squat Development", "Build the squat through technique, programming, variation selection, accessory work, and fatigue control.", ["Technical Model", "Primary Programming", "Variations", "Accessory Selection", "Common Weak Points", "Progression"]),
("05-bench-system.md", "Bench Press Development", "Build the bench press through technical practice, upper-body hypertrophy, and triceps strength.", ["Technical Model", "Primary Programming", "Variations", "Accessory Selection", "Common Weak Points", "Progression"]),
("06-deadlift-system.md", "Deadlift Development", "Maintain and improve the deadlift while managing posterior-chain and lower-back fatigue.", ["Technical Model", "Primary Programming", "Variations", "Accessory Selection", "Common Weak Points", "Progression"]),
("07-accessory-training.md", "Accessory Training", "Select hypertrophy and corrective accessories that directly support strength and physique goals.", ["Selection Rules", "Lower Body", "Upper Push", "Upper Pull", "Arms and Delts", "Progression"]),
("08-core-training.md", "Core Training", "Develop bracing, anti-extension, anti-rotation, lateral stability, and loaded-carry capacity.", ["Core Function", "Anti-Extension", "Anti-Rotation", "Lateral Stability", "Loaded Carries", "Progression"]),
("09-conditioning.md", "Conditioning", "Program two weekly interval sessions without compromising strength, muscle gain, or recovery.", ["Goals", "Modality Selection", "Interval Prescriptions", "Progression", "Placement in the Week", "Recovery Rules"]),
("10-deloads.md", "Deloads and Fatigue Management", "Define planned and reactive deloads, fatigue markers, and return-to-loading decisions.", ["Fatigue Markers", "Planned Deloads", "Reactive Deloads", "Volume Reduction", "Intensity Reduction", "Return Criteria"]),
("11-fifty-two-week-plan.md", "Fifty-Two-Week Plan", "Map the annual powerbuilding progression into blocks with test weeks, deloads, and optional meet preparation.", ["Annual Calendar", "Foundation Block", "Hypertrophy Blocks", "Strength Blocks", "Power and Peaking", "Transition Weeks"]),
("12-exercise-library.md", "Exercise Library", "Create standardized exercise entries with purpose, execution, cues, errors, substitutions, and progression.", ["Entry Format", "Squat Accessories", "Bench Accessories", "Deadlift Accessories", "Core Exercises", "Conditioning and Mobility"]),
]

recovery = [
("01-sleep.md", "Sleep", "Develop realistic sleep targets and routines around day shift, night shift, training, and family obligations.", ["Sleep Targets", "Day-Shift Routine", "Night-Shift Routine", "Environment", "Naps", "Troubleshooting"]),
("02-shift-work-recovery.md", "Shift-Work Recovery", "Manage circadian disruption, training placement, appetite, fatigue, and schedule transitions.", ["Shift Challenges", "Schedule Transition", "Light Exposure", "Meal Timing", "Training Decisions", "Recovery Checklist"]),
("03-heat-management.md", "Heat Management", "Reduce heat-stress risk and protect performance during long outdoor work shifts.", ["Heat Risk", "Acclimatization", "Hydration", "Cooling", "Training Modifications", "Warning Signs"]),
("04-mobility-stretching.md", "Mobility and Stretching", "Define what to perform before training, after training, on recovery days, and during work breaks.", ["Mobility Goals", "Before Training", "After Training", "Daily Micro-Sessions", "Problem Areas", "Progression"]),
("05-fatigue-pain.md", "Fatigue, Pain, and Training Decisions", "Separate normal discomfort, modification-worthy symptoms, and medical red flags.", ["Normal Soreness", "Fatigue", "Pain Scale", "Modification Options", "Stop Criteria", "Professional Evaluation"]),
("06-medical-monitoring.md", "Medical Monitoring", "Organize physician-led monitoring topics relevant to a large strength athlete working in heat and using prescribed therapies.", ["Scope and Limitations", "Vital Signs", "Laboratory Discussion List", "Medication and Supplement Review", "Blood Donation Considerations", "Follow-Up"]),
("07-travel.md", "Travel and Schedule Disruptions", "Maintain minimum-effective nutrition, training, hydration, and recovery during travel or unexpected overtime.", ["Minimum Standards", "Travel Nutrition", "Hotel Training", "Missed Sessions", "Schedule Reset", "Return Plan"]),
]

tracking = [
("01-weekly-check-in.md", "Weekly Check-In", "Capture the minimum data needed to make evidence-based weekly coaching decisions.", ["Week Summary", "Bodyweight Trend", "Training Performance", "Nutrition Adherence", "Recovery", "Next-Week Decisions"]),
("02-bodyweight-measurements.md", "Bodyweight and Measurements", "Standardize weighing, waist measurements, progress photos, and trend interpretation.", ["Measurement Protocol", "Daily Weight", "Weekly Average", "Waist", "Progress Photos", "Interpretation"]),
("03-training-log.md", "Training Log", "Record exercises, sets, reps, load, RPE, pain, and session notes.", ["Session Header", "Main Lifts", "Accessories", "Conditioning", "Readiness", "Coach Notes"]),
("04-nutrition-log.md", "Nutrition Log", "Track calories, macros, meal timing, hydration, digestion, and deviations.", ["Daily Targets", "Meal Record", "Hydration", "Digestion", "Adherence", "Notes"]),
("05-recovery-score.md", "Recovery Score", "Combine sleep, soreness, stress, energy, and pain into a simple readiness trend.", ["Scoring System", "Sleep", "Soreness", "Stress and Energy", "Pain", "Training Recommendation"]),
("06-monthly-review.md", "Monthly Review", "Evaluate four weeks and make one clear set of changes for the next block.", ["Outcome Review", "Body Composition", "Strength", "Conditioning", "Recovery", "Next Block"]),
]

build_volume("Nutrition", "Volume I — Nutrition", nutrition)
build_volume("Training", "Volume II — Training", training)
build_volume("Recovery", "Volume III — Recovery", recovery)
build_volume("Tracking", "Volume IV — Tracking", tracking, refs=False)

write("STYLE_GUIDE.md", """
# Publication Style Guide

Use a direct, practical coaching voice. Use one `#` heading for each chapter title, `##` for major sections, and `###` for subsections. Keep paragraphs short. List food weights in grams and add cups when useful. Use pounds and kilograms for bodyweight and barbell loads where practical.

## Images

```markdown
![Descriptive alt text](../Assets/Images/file-name.jpg)

*Figure X.Y — Concise caption and source credit.*
```

## Citations

Use numbered citations such as **[1]** and list complete references at the end of each chapter.
""")

write("REFERENCES.md", """
# Master References

| ID | Author / Organization | Title | Publication | Year | DOI / URL | Used In | Verification |
|---:|---|---|---|---:|---|---|---|
| 1 |  |  |  |  |  |  | Pending |

Prefer systematic reviews, consensus statements, professional guidelines, textbooks, and primary research. Verify that every source supports the claim attached to it.
""")

write("CHANGELOG.md", """
# Change Log

## [0.1.0] — 2026-07-08

### Added

- Complete directory structure.
- Linked table of contents.
- Nutrition, training, recovery, and tracking templates.
- Recipe and progress-log templates.
- Style and reference guides.
""")

write("Recipes/README.md", """
# Recipe Library

Categories: Mexican, Italian, Asian, BBQ, Breakfast, Soups, Protein Desserts, and Shakes-Smoothies. Every recipe must include exact portions, batch yield, calories, macros, fiber, storage, reheating, substitutions, and training/cardio/rest-day fit.
""")

write("Recipes/recipe-template.md", """
---
title: "Recipe Name"
category: "Cuisine or Meal Type"
status: "template"
yield: 0
serving_size: ""
meal_fit: ["training-day"]
---

# Recipe Name

## Nutrition Per Serving

| Calories | Protein | Carbohydrate | Fat | Fiber |
|---:|---:|---:|---:|---:|
|  |  |  |  |  |

## Ingredients

| Ingredient | Batch Quantity | Per-Serving Quantity | Measurement State |
|---|---:|---:|---|
|  |  |  | Raw / cooked |

## Instructions

1. 
2. 
3. 

## Portioning, Storage, and Reheating

- Refrigerator:
- Freezer:
- Reheating:

## References

1. Add sources for nutrition or food-safety claims.
""")

categories = {
    "Mexican": "Burrito bowls, fajitas, tacos, enchilada bakes, chili, beans, rice, salsa, and avocado-based meals.",
    "Italian": "High-protein pasta, meatballs, chicken parmesan, lighter sauces, soups, and baked dishes.",
    "Asian": "Teriyaki, stir-fries, rice bowls, curries, salmon, shrimp, and noodle dishes.",
    "BBQ": "Smoked or grilled meats, potatoes, beans, vegetables, and high-protein sides.",
    "Breakfast": "Overnight oats, eggs, breakfast burritos, yogurt bowls, and pancakes.",
    "Soups": "Chicken tortilla soup, chili, beef vegetable soup, and freezer-friendly meals.",
    "Protein-Desserts": "Greek-yogurt bowls, cheesecake-style desserts, puddings, and frozen desserts.",
    "Shakes-Smoothies": "Breakfast shakes, recovery shakes, and meal-replacement options.",
}
for category, description in categories.items():
    write(f"Recipes/{category}/README.md", f"# {category.replace('-', ' ')}\n\n{description}\n\n## Recipe Index\n\n| Recipe | Calories | Protein | Meal Fit | Status |\n|---|---:|---:|---|---|\n|  |  |  |  | Planned |")

write("Progress Logs/README.md", """
# Progress Logs

Copy completed weekly and monthly templates into the appropriate year folder. Use `YYYY-W##-weekly-check-in.md` and `YYYY-MM-monthly-review.md` naming.
""")
write("Progress Logs/2026/Weekly/weekly-log-template.md", """
# Weekly Check-In — YYYY-W##

| Metric | Result |
|---|---:|
| Morning bodyweight |  |
| Calories |  |
| Protein |  |
| Sleep |  |

## Weekly Decisions

- Nutrition:
- Training:
- Recovery:
""")
write("Progress Logs/2026/Monthly/monthly-review-template.md", """
# Monthly Review — YYYY-MM

| Metric | Start | End | Change |
|---|---:|---:|---:|
| Bodyweight |  |  |  |
| Waist |  |  |  |
| Squat estimate |  |  |  |
| Bench estimate |  |  |  |
| Deadlift estimate |  |  |  |

## Adjustments for Next Month

- Nutrition:
- Training:
- Recovery:
""")

for path in ["Assets/Images/.gitkeep", "Assets/Logos/.gitkeep", "Assets/Tables/.gitkeep", "Assets/Figures/.gitkeep", "Assets/References/.gitkeep"]:
    write(path, "")

manifest = sorted(str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file())
write("PROJECT_MANIFEST.md", "# Project Manifest\n\n" + "\n".join(f"- `{item}`" for item in manifest))
print(f"Generated {len(manifest)} repository files.")
