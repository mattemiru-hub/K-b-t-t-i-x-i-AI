# Sample Output

This folder describes what a polished deliverable from `excel-dashboard-ai-skill` should include.

## Expected handoff package

When the skill finishes well, the output package should normally contain:

- final Excel workbook (`.xlsx` or `.xlsm`)
- dashboard sheet opened by default
- clean 75% zoom working view
- refreshable queries and model logic
- preview image for quick review
- short usage guide
- count of queries, model tables, relationships, and DAX measures

## Visual reference

The file `executive-dashboard-preview.png` is the public preview reference for the current approved style.

Use it to validate:

- executive layout hierarchy
- left slicer rail
- KPI card row
- chart card spacing
- section bar treatment
- premium, Power BI-like reading experience

## What should not happen

- spreadsheet-like raw grids as the main dashboard surface
- normal charts replacing the main PivotChart layer
- KPI colors changing meaning under slicers
- metric colors reusing KPI-band colors where they should not
- broken labels, cropped text, or unstable chart framing at 75% zoom

## Suggested review flow

1. Open the workbook
2. Press `Refresh All`
3. Test major slicers
4. Confirm trend logic still makes sense
5. Compare the final dashboard against `executive-dashboard-preview.png`
6. Export a final preview image before handoff