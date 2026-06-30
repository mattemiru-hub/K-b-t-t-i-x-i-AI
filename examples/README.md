# Examples

This folder explains how to apply `excel-dashboard-ai-skill` on real Excel dashboard tasks.

## Example 1 - Rebuild an existing sales workbook

Use case:

- You already have a workbook with raw sales data and one or more old report sheets
- You want Codex to rebuild it into a refreshable executive dashboard

Suggested prompt:

```text
Use $excel-dashboard-ai-skill on my current workbook.

Goal:
- rebuild the workbook into a Power BI-like Excel executive dashboard
- keep all main visuals based on Power Query + Data Model + DAX + PivotTables + PivotCharts
- create slicers for the key business dimensions that exist in the data
- keep the dashboard refreshable when raw data changes and I press Refresh All
- optimize layout and readability for 75% zoom

Deliver:
- final workbook
- preview image
- summary of query count, model tables, relationships, and measures
```

## Example 2 - Adapt the same style to a different schema

Use case:

- Your workbook does not use the same column names as the reference FMCG file
- You still want the same executive experience

Suggested prompt:

```text
Use $excel-dashboard-ai-skill on my workbook, but do not assume fixed column names.

Map columns by business role:
- date or period
- region or geography
- manager or owner
- rep or seller
- category or product grouping
- channel or route to market
- actual, target, margin, and risk fields if they exist

Then rebuild the full dashboard in the approved style.
```

## Example 3 - Audit and polish an almost-finished dashboard

Use case:

- The workbook already has queries, pivots, charts, and slicers
- You want Codex to fix UX and visual consistency

Suggested prompt:

```text
Use $excel-dashboard-ai-skill to audit and polish my current workbook.

Focus on:
- slicer usability
- chart color stability under slicers
- meaningful monthly trend behavior
- KPI band logic
- number formatting
- title sizing
- card spacing and alignment
- guide card readability
- workbook opening state at 75% zoom

Do not replace the main dashboard with normal charts.
```

## Example 4 - Ask only for a reusable prompt

Use case:

- You do not want Codex to edit the workbook yet
- You only want a prompt template for another AI run

Suggested prompt:

```text
Use $excel-dashboard-ai-skill only to generate a reusable prompt for this workbook.

I want the prompt to:
- adapt to whatever columns exist
- preserve the approved executive dashboard style
- require Power Query, Data Model, DAX measures, PivotTables, PivotCharts, and slicers
- include QA checks and expected deliverables
```

## Expected behavior across all examples

- Keep the dashboard executive and Power BI-like
- Do not let KPI colors and metric colors get mixed
- Keep monthly trend meaningful
- Save the workbook with the dashboard sheet active
- Avoid spreadsheet-looking layout drift