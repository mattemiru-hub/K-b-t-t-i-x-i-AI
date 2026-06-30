---
name: excel-dashboard-ai-skill
description: Build premium Excel executive dashboards inside Excel using Power Query, Power Pivot, DAX, PivotTables, PivotCharts, slicers, KPI cards, and a Power BI-like layout. Use when Codex needs to turn an existing workbook or raw dataset into a refreshable executive dashboard, rebuild a dashboard to match an approved local reference, polish workbook UX at 75 percent zoom, export dashboard previews, or audit slicer, chart, guide-card, and workbook-visibility issues.
---

# Excel Dashboard AI Skill

## Quick Start

- Treat the approved local dashboard as the visual contract.
- Read `references/clarification-rules-vi.md` before mapping fields or rebuilding structure.
- Read `references/golden-reference-spec-vi.md` before rebuilding or polishing any workbook.
- Read `references/qa-checklist-vi.md` before saving the final workbook.
- Read `references/prompt-template-vi.md` only when the user asks for a reusable prompt.

## Workflow

1. Inspect the workbook, active sheets, schema, existing queries, model tables, relationships, measures, PivotTables, PivotCharts, slicers, and visible workbook state.
2. Run the clarification gate from `references/clarification-rules-vi.md` before mapping fields or making structural workbook changes.
3. Map source columns to business roles instead of assuming fixed headers. Preserve the approved design language even when the input schema changes.
4. Build or repair the data stack in this order: Power Query -> Data Model / Power Pivot -> DAX measures -> PivotTables -> PivotCharts -> slicers -> dashboard layer.
5. Keep all main visuals sourced from Power Query outputs, Data Model measures, and PivotTable / PivotChart objects. Do not replace the main dashboard with normal charts.
6. Apply the approved executive layout and styling rules from `references/golden-reference-spec-vi.md`.
7. Run the reusable scripts when they help:
   - `scripts/apply_golden_reference_style.py <workbook-path>`
   - `scripts/export_dashboard_preview.ps1 -WorkbookPath <workbook-path>`
   - `scripts/install_local_skill.ps1` to mirror this repo into the local Codex skills folder
8. Finish with the QA checks in `references/qa-checklist-vi.md`, then save a stable local copy if the workbook lives in OneDrive or another cloud-synced path.

## Clarification Gate

Before rebuilding any dashboard, decide whether the workbook can be interpreted with high confidence.

Ask the user before proceeding if any of these are missing, ambiguous, or have more than one plausible match:

- which sheet is the main raw-data source
- which field is the primary date field for trend logic
- which field is the actual revenue or sales value
- which field is the target or plan value when target-attainment visuals are required
- which fields should drive Region, Channel, Category, Area Manager, and Sales Rep slicers
- whether to preserve the current dashboard sheet or rebuild from scratch
- whether a requested KPI exists in the data or must be derived

Do not make structural workbook changes until the required clarifications are resolved.
Do not guess low-confidence mappings for business-critical fields.
If confidence is below high confidence, stop and ask.

## Required Question Style

When clarification is needed, ask the minimum set of short concrete questions required to continue.

Preferred examples:

1. Sheet raw data chính là sheet nào?
2. Cột nào là doanh thu thực tế?
3. Cột nào là target hoặc kế hoạch?
4. Nếu có nhiều cột ngày, cột nào dùng làm trục thời gian chính?
5. Giữ dashboard hiện tại để polish hay rebuild lại từ đầu?

Do not ask broad open-ended questions when a short targeted question will unblock the work.
Do not ask about visual preferences that are already fixed by the golden-reference rules unless the user explicitly wants a different style.

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
- Short clarification summary when important field mappings were confirmed by the user
- Summary of query count, model table count, relationship count, measure count, and any schema compromises
