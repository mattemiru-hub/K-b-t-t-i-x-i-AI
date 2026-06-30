---
name: excel-dashboard-ai-skill
description: Build premium Excel executive dashboards inside Excel using Power Query, Power Pivot, DAX, PivotTables, PivotCharts, slicers, KPI cards, and a Power BI-like layout. Use when Codex needs to turn an existing workbook or raw dataset into a refreshable executive dashboard, rebuild a dashboard to match an approved local reference, polish workbook UX at 75 percent zoom, export dashboard previews, or audit slicer, chart, guide-card, and workbook-visibility issues.
---

# Excel Dashboard AI Skill

## Quick Start

- Treat the approved local dashboard as the visual contract.
- Read `references/golden-reference-spec-vi.md` before rebuilding or polishing any workbook.
- Read `references/qa-checklist-vi.md` before saving the final workbook.
- Read `references/prompt-template-vi.md` only when the user asks for a reusable prompt.

## Workflow

1. Inspect the workbook, active sheets, schema, existing queries, model tables, relationships, measures, PivotTables, PivotCharts, slicers, and visible workbook state.
2. Map source columns to business roles instead of assuming fixed headers. Preserve the approved design language even when the input schema changes.
3. Build or repair the data stack in this order: Power Query -> Data Model / Power Pivot -> DAX measures -> PivotTables -> PivotCharts -> slicers -> dashboard layer.
4. Keep all main visuals sourced from Power Query outputs, Data Model measures, and PivotTable / PivotChart objects. Do not replace the main dashboard with normal charts.
5. Apply the approved executive layout and styling rules from `references/golden-reference-spec-vi.md`.
6. Run the reusable scripts when they help:
   - `scripts/apply_golden_reference_style.py <workbook-path>`
   - `scripts/export_dashboard_preview.ps1 -WorkbookPath <workbook-path>`
   - `scripts/install_local_skill.ps1` to mirror this repo into the local Codex skills folder
7. Finish with the QA checks in `references/qa-checklist-vi.md`, then save a stable local copy if the workbook lives in OneDrive or another cloud-synced path.

## Non-Negotiables

- Preserve a Power BI-like executive experience, not a spreadsheet-looking report.
- Keep the left slicer rail, top KPI row, section bars, and five-chart layout unless the user explicitly asks for a different composition.
- Use KPI band colors only for attainment-status visuals and guide-card meaning:
  - Healthy = green
  - Watch = amber
  - Risk = red
- Keep the `Channel Efficiency | Gross Margin vs Trade Spend` visual on a metric palette, not KPI-band colors.
- Keep chart colors stable across slicer changes. Do not let colors jump meaninglessly.
- Make the monthly trend remain meaningful even when Month slicers are used; limit slicer interaction if necessary.
- Format numbers for reading speed using compact units, clean percent precision, and data labels where column or bar charts need them.
- Save the workbook with the dashboard sheet active, workbook window visible, gridlines hidden, and default zoom at 75 percent.

## Script Notes

- `scripts/apply_golden_reference_style.py` is Windows Excel COM automation. Pass the workbook path explicitly.
- `scripts/export_dashboard_preview.ps1` exports a PNG preview and reports query / model counts from the workbook.
- If a script touches workbook styling, inspect the workbook again after it runs because Excel COM can keep stale windows open.

## Deliverables

- Final `.xlsx` workbook
- Local non-cloud copy when needed for reliable opening
- Dashboard preview image
- Summary of query count, model table count, relationship count, measure count, and any schema compromises
