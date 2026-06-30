# Excel Executive Dashboard Golden Reference

GitHub-ready skill package for building Excel executive dashboards that feel closer to a Power BI cockpit than a spreadsheet report.

This skill is designed around a golden-reference FMCG dashboard with:

- Power Query for data shaping
- Power Pivot / Data Model for relationships
- DAX measures for KPI logic
- PivotTables and PivotCharts for all main visuals
- left-side slicer rail
- top KPI row
- section bars
- guide card
- 75% zoom working view

## What this repo gives you

- a Codex skill entrypoint in `SKILL.md`
- style and UX rules in `references/`
- a reusable Vietnamese prompt template
- automation scripts to:
  - apply the approved visual style
  - export a dashboard preview
  - mirror the skill into the local Codex skills folder

## Folder structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── golden-reference-spec-vi.md
│   ├── prompt-template-vi.md
│   └── qa-checklist-vi.md
├── scripts/
│   ├── apply_golden_reference_style.py
│   ├── export_dashboard_preview.ps1
│   └── install_local_skill.ps1
└── assets/
    └── golden-reference-preview.png
```

## Use cases

Use this skill when you want to:

- rebuild an Excel dashboard from raw data
- convert an existing workbook into a refreshable BI-style dashboard
- force the output to follow an approved executive layout
- audit slicers, colors, workbook visibility, zoom, guide-card logic, or chart UX
- generate a reusable prompt that another AI can follow

## Install for Codex

From this repo:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_local_skill.ps1
```

That mirrors the repo into:

```text
C:\Users\admin\.codex\skills\excel-executive-dashboard-golden-reference
```

## Main scripts

Apply the approved dashboard style:

```powershell
py -3 .\scripts\apply_golden_reference_style.py "C:\path\to\workbook.xlsx"
```

Export a PNG preview and report query / model counts:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\export_dashboard_preview.ps1 -WorkbookPath "C:\path\to\workbook.xlsx"
```

## Design contract

The skill intentionally preserves these rules:

- Power BI-like executive dashboard feel
- Pivot-based visuals for the main dashboard
- KPI band colors only for attainment status
- metric palette for `Channel Efficiency | Gross Margin vs Trade Spend`
- stable chart colors under slicers
- meaningful monthly trend behavior
- clean layout at 75% zoom
- active visible dashboard sheet when saved

Read these files before modifying the behavior:

- `references/golden-reference-spec-vi.md`
- `references/qa-checklist-vi.md`

## Notes

- The local repo includes `assets/golden-reference-preview.png` as the reference image asset.
- The skill is meant for Windows Excel automation because the styling workflow uses Excel COM.
