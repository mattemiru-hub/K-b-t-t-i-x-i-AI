import sys
from pathlib import Path

import win32com.client as win32
from win32com.client import GetActiveObject


def rgb(r: int, g: int, b: int) -> int:
    return r + g * 256 + b * 65536


NAVY = rgb(18, 36, 61)
NAVY_SOFT = rgb(24, 46, 78)
SLATE = rgb(100, 116, 139)
LINE = rgb(208, 219, 232)
BG = rgb(242, 246, 252)
WHITE = rgb(255, 255, 255)
TEAL = rgb(16, 151, 170)
AMBER = rgb(245, 158, 11)
GREEN = rgb(34, 197, 94)
RED = rgb(220, 38, 38)
METRIC_BLUE = rgb(32, 76, 151)
METRIC_TEAL = rgb(0, 128, 145)

MSO_SEND_TO_BACK = 1
MSO_SHAPE_ROUNDED_RECTANGLE = 5
MSO_SHAPE_RECTANGLE = 1
MSO_TEXT_ORIENTATION_HORIZONTAL = 1
XL_NONE = -4142


def get_workbook_path() -> Path:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: apply_golden_reference_style.py <workbook-path>")
    workbook = Path(sys.argv[1]).expanduser().resolve()
    if not workbook.exists():
        raise SystemExit(f"Workbook not found: {workbook}")
    return workbook


def shape_exists(ws, name: str) -> bool:
    try:
        ws.Shapes(name)
        return True
    except Exception:
        return False


def delete_shape_if_exists(ws, name: str):
    try:
        ws.Shapes(name).Delete()
    except Exception:
        pass


def add_textbox(ws, name, left, top, width, height, text, font_size, color, bold=False):
    tb = ws.Shapes.AddTextbox(MSO_TEXT_ORIENTATION_HORIZONTAL, left, top, width, height)
    tb.Name = name
    tb.Line.Visible = False
    tb.Fill.Visible = False
    tb.TextFrame2.TextRange.Text = text
    tb.TextFrame2.TextRange.Font.Name = "Aptos"
    tb.TextFrame2.TextRange.Font.Size = font_size
    tb.TextFrame2.TextRange.Font.Bold = -1 if bold else 0
    tb.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = color
    return tb


def set_shape_fill(shape, fill_rgb, line_rgb=None, line_weight=1.0, transparency=0):
    shape.Fill.Visible = True
    shape.Fill.ForeColor.RGB = fill_rgb
    shape.Fill.Transparency = transparency
    if line_rgb is None:
        shape.Line.Visible = False
    else:
        shape.Line.Visible = True
        shape.Line.ForeColor.RGB = line_rgb
        shape.Line.Weight = line_weight


def style_panel(shape, *, fill=WHITE, line=LINE):
    set_shape_fill(shape, fill, line, 1.0, 0)
    try:
        shape.Shadow.Visible = True
        shape.Shadow.Style = 6
        shape.Shadow.Blur = 1.5
        shape.Shadow.OffsetX = 0
        shape.Shadow.OffsetY = 1
        shape.Shadow.Transparency = 0.978
    except Exception:
        pass


def style_text_range(rng, *, size=None, bold=None, color=None, name="Aptos"):
    rng.Font.Name = name
    if size is not None:
        rng.Font.Size = size
    if bold is not None:
        rng.Font.Bold = bold
    if color is not None:
        rng.Font.Color = color


def get_excel_context():
    workbook = get_workbook_path()
    workbook_path = str(workbook)
    workbook_name = workbook.name.lower()
    try:
        excel = GetActiveObject("Excel.Application")
        for idx in range(1, excel.Workbooks.Count + 1):
            wb = excel.Workbooks(idx)
            if wb.Name.lower() == workbook_name or str(wb.FullName).lower() == workbook_path.lower():
                return excel, wb, False
    except Exception:
        pass

    excel = win32.DispatchEx("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False
    excel.ScreenUpdating = False
    wb = excel.Workbooks.Open(workbook_path)
    return excel, wb, True


def main():
    excel, wb, opened_here = get_excel_context()
    prev_display_alerts = excel.DisplayAlerts
    prev_screen_updating = excel.ScreenUpdating
    excel.DisplayAlerts = False
    excel.ScreenUpdating = False
    ws = wb.Worksheets("00_Executive_Dashboard")

    ws.Range("A1:AG60").Interior.Color = BG
    ws.Range("A1:AG4").Interior.Color = NAVY
    ws.Range("A5:E55").Borders.LineStyle = XL_NONE
    ws.Range("A5:E55").Interior.Color = BG
    ws.Range("A44:E55").ClearContents()
    ws.Range("A5").Value = ""

    for name in [
        "uiFilterRailBg", "uiFilterTitle", "uiGuideCard", "uiGuideTitle",
        "uiGuideSwatchHealthy", "uiGuideSwatchWatch", "uiGuideSwatchRisk",
        "uiGuideTextHealthy", "uiGuideTextWatch", "uiGuideTextRisk",
        "uiGuideBody1", "uiGuideBody2", "uiHeaderSubtitle", "uiHeaderAsOf",
    ]:
        delete_shape_if_exists(ws, name)

    ws.Range("A1").Value = "FMCG Executive Sales Dashboard"
    ws.Range("A3").Value = ""
    ws.Range("F6").Value = "TOTAL REVENUE"
    ws.Range("K6").Value = "TARGET ATTAINMENT"
    ws.Range("P6").Value = "GROSS MARGIN"
    ws.Range("U6").Value = "PRODUCTIVE CALL RATE"
    ws.Range("Z6").Value = "SERVICE RISK / OOS"
    ws.Range("P10").Value = "Profit quality after COGS"
    ws.Range("U10").Value = "Productive calls / total calls"
    ws.Range("K10").Formula = '=IF(K7>=1,"On plan","Below plan by "&TEXT(1-K7,"0.0%"))'
    ws.Range("Z10").Formula = '=IF(Z7<=0.05,"Within threshold","Above threshold")'
    try:
        ws.Range("X1:AD1").ClearContents()
    except Exception:
        pass
    try:
        ws.Range("X3").MergeArea.ClearContents()
        ws.Range("X3:AD3").ClearContents()
        ws.Range("X3").Value = ""
        ws.Range("X3:AD3").HorizontalAlignment = -4152
    except Exception:
        pass

    row_heights = {
        1: 28, 2: 8, 3: 18, 4: 6, 5: 12,
        6: 18, 7: 30, 8: 4, 9: 4, 10: 20,
        44: 10, 45: 10, 46: 10, 47: 10, 48: 10,
        49: 10, 50: 10, 51: 10, 52: 10, 53: 10, 54: 10, 55: 10,
    }
    for row, height in row_heights.items():
        ws.Rows(row).RowHeight = height

    style_text_range(ws.Range("A1:M1"), size=18, bold=True, color=WHITE)
    style_text_range(ws.Range("A3:M3"), size=9.7, bold=False, color=LINE)
    style_text_range(ws.Range("X3:AD3"), size=9.0, bold=False, color=LINE)
    style_text_range(ws.Range("F6:AD6"), size=8.7, bold=True, color=SLATE)
    style_text_range(ws.Range("F7:AD7"), size=17.5, bold=True, color=NAVY)
    style_text_range(ws.Range("F10:AD10"), size=7.4, bold=False, color=SLATE)
    style_text_range(ws.Range("K10:O10"), size=7.4, bold=True, color=RED)
    style_text_range(ws.Range("Z10:AD10"), size=7.4, bold=True, color=GREEN)
    ws.Range("F10:AD10").VerticalAlignment = -4160

    subtitle_anchor = ws.Range("A3:H3")
    subtitle = add_textbox(ws, "uiHeaderSubtitle", 28, subtitle_anchor.Top + 1, 320, 10, "Daily revenue, gross margin and sales execution | FMCG by day", 8.2, LINE, False)
    try:
        subtitle.TextFrame2.TextRange.ParagraphFormat.Alignment = 1
    except Exception:
        pass

    asof_anchor = ws.Range("Y3:AD3")
    asof_width = 106
    asof = add_textbox(ws, "uiHeaderAsOf", asof_anchor.Left + asof_anchor.Width - asof_width - 8, asof_anchor.Top + 1, asof_width, 10, "Data through 31 Dec 2026", 7.1, LINE, False)
    try:
        asof.TextFrame2.TextRange.ParagraphFormat.Alignment = 3
    except Exception:
        pass

    for rng in ("F6:J10", "K6:O10", "P6:T10", "U6:Y10", "Z6:AD10"):
        ws.Range(rng).Interior.Color = WHITE
        for edge in (7, 8, 9, 10):
            ws.Range(rng).Borders(edge).LineStyle = 1
            ws.Range(rng).Borders(edge).Color = LINE
            ws.Range(rng).Borders(edge).Weight = 2

    try:
        ws.Shapes("uiGuideButton").Visible = False
        ws.Shapes("uiExecutiveBadge").Visible = False
    except Exception:
        pass

    chip_specs = [
        ("uiKpiChip1", "REVENUE", "F6:J10", 56, 11, rgb(37, 99, 235)),
        ("uiKpiChip2", "TARGET", "K6:O10", 56, 11, AMBER),
        ("uiKpiChip3", "MARGIN", "P6:T10", 56, 11, TEAL),
        ("uiKpiChip4", "CALLS", "U6:Y10", 52, 11, GREEN),
        ("uiKpiChip5", "RISK", "Z6:AD10", 46, 11, RED),
    ]
    for name, text, card_range, width, height, fill in chip_specs:
        card = ws.Range(card_range)
        left = card.Left + (card.Width - width) / 2
        top = card.Top - height - 6
        shp = ws.Shapes(name)
        shp.Left = left
        shp.Top = top
        shp.Width = width
        shp.Height = height
        set_shape_fill(shp, fill, fill, 1, 0)
        shp.TextFrame2.TextRange.Text = text
        shp.TextFrame2.TextRange.Font.Name = "Aptos"
        shp.TextFrame2.TextRange.Font.Size = 7.2
        shp.TextFrame2.TextRange.Font.Bold = -1
        shp.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = WHITE

    rail = ws.Shapes.AddShape(MSO_SHAPE_ROUNDED_RECTANGLE, 10, 77, 186, 690)
    rail.Name = "uiFilterRailBg"
    set_shape_fill(rail, rgb(250, 252, 255), LINE, 1, 0)
    try:
        rail.Adjustments.Item(1)
        rail.Adjustments[1] = 0.05
    except Exception:
        pass
    try:
        rail.ZOrder(MSO_SEND_TO_BACK)
    except Exception:
        pass

    filter_title = add_textbox(ws, "uiFilterTitle", 20, 86, 158, 20, "INTERACTIVE FILTERS", 11.0, NAVY, True)
    try:
        filter_title.TextFrame2.TextRange.ParagraphFormat.Alignment = 2
    except Exception:
        pass

    slicer_settings = [
        ("Slicer_Year", "Year", "slYearDynamic", 16, 112, 176, 52),
        ("Slicer_Month", "Month (detail)", "slMonthDynamic", 16, 168, 176, 86),
        ("Slicer_Region", "Region", "slRegionDynamic", 16, 258, 176, 58),
        ("Slicer_Channel", "Channel", "slChannelDynamic", 16, 320, 176, 88),
        ("Slicer_Category", "Category", "slCategoryDynamic", 16, 412, 176, 76),
        ("Slicer_AreaManager", "Area Manager", "slManagerDynamic", 16, 492, 176, 68),
        ("Slicer_SalesRep", "Sales Rep", "slRepDynamic", 16, 564, 176, 58),
    ]
    slicer_caches = wb.SlicerCaches
    for cache_name, caption, shape_name, left, top, width, height in slicer_settings:
        sc = slicer_caches.Item(cache_name)
        sl = sc.Slicers.Item(1)
        try:
            sl.Caption = caption
            sl.Style = "SlicerStyleLight1"
            if cache_name == "Slicer_Month":
                sl.NumberOfColumns = 2
            elif cache_name in {"Slicer_Channel", "Slicer_Category"}:
                sl.NumberOfColumns = 1
            else:
                sl.NumberOfColumns = 2
            try:
                sl.RowHeight = 14.2 if cache_name == "Slicer_Category" else 18.3
            except Exception:
                pass
        except Exception:
            pass
        shp = ws.Shapes(shape_name)
        shp.Left = left
        shp.Top = top
        shp.Width = width
        shp.Height = height

    guide = ws.Shapes.AddShape(MSO_SHAPE_ROUNDED_RECTANGLE, 16, 616, 176, 50)
    guide.Name = "uiGuideCard"
    set_shape_fill(guide, WHITE, LINE, 1.0, 0)
    try:
        guide.Shadow.Visible = True
        guide.Shadow.Style = 6
        guide.Shadow.Blur = 2
        guide.Shadow.OffsetX = 0
        guide.Shadow.OffsetY = 1
        guide.Shadow.Transparency = 0.95
    except Exception:
        pass
    try:
        guide.Adjustments.Item(1)
        guide.Adjustments[1] = 0.06
    except Exception:
        pass

    guide_title = add_textbox(ws, "uiGuideTitle", 26, 618, 150, 14, "KPI BAND GUIDE", 8.5, NAVY, True)
    try:
        guide_title.TextFrame2.TextRange.ParagraphFormat.Alignment = 2
    except Exception:
        pass

    swatches = [
        ("uiGuideSwatchHealthy", "uiGuideTextHealthy", GREEN, "Healthy: att. >= 95%", 631),
        ("uiGuideSwatchWatch", "uiGuideTextWatch", AMBER, "Watch: 90% <= att. < 95%", 643),
        ("uiGuideSwatchRisk", "uiGuideTextRisk", RED, "Risk: att. < 90%", 655),
    ]
    for sw_name, tx_name, color, text, top in swatches:
        sw = ws.Shapes.AddShape(MSO_SHAPE_RECTANGLE, 30, top, 14, 10)
        sw.Name = sw_name
        set_shape_fill(sw, color, None, 0, 0)
        add_textbox(ws, tx_name, 50, top - 2, 120, 11, text, 6.6, NAVY, False)

    ws.Shapes("uiSectionTop").Height = 18
    ws.Shapes("uiSectionBottom").Height = 18
    ws.Shapes("uiSectionTop").Left = 208
    ws.Shapes("uiSectionBottom").Left = 208
    ws.Shapes("uiSectionTop").Width = 1328
    ws.Shapes("uiSectionBottom").Width = 1328
    ws.Shapes("uiSectionTop").Top = 123
    ws.Shapes("uiSectionBottom").Top = 359
    ws.Shapes("uiSectionTop").TextFrame2.TextRange.Text = "EXECUTIVE TREND & KPI ATTAINMENT"
    ws.Shapes("uiSectionBottom").TextFrame2.TextRange.Text = "MIX, CHANNEL & SALES EXECUTION"
    for nm in ("uiSectionTop", "uiSectionBottom"):
        shp = ws.Shapes(nm)
        set_shape_fill(shp, NAVY, NAVY, 1, 0)
        shp.TextFrame2.TextRange.Font.Name = "Aptos"
        shp.TextFrame2.TextRange.Font.Size = 9.8
        shp.TextFrame2.TextRange.Font.Bold = -1
        shp.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = WHITE
        try:
            shp.TextFrame2.TextRange.ParagraphFormat.Alignment = 2
        except Exception:
            pass

    panel_names = ["uiTrendPanel", "uiRegionPanel", "uiCategoryPanel", "uiChannelPanel", "uiRepPanel"]
    for nm in panel_names:
        style_panel(ws.Shapes(nm), fill=WHITE, line=LINE)

    chart_titles = [
        "Monthly Revenue Trend | Full selected year(s)",
        "Revenue by Region | Color = KPI band",
        "Revenue by Category | Color = KPI band",
        "Channel Efficiency | Gross Margin vs Trade Spend",
        "Top 10 Sales Reps | Color = KPI band",
    ]
    panel_lookup = {
        1: "uiTrendPanel",
        2: "uiRegionPanel",
        3: "uiCategoryPanel",
        4: "uiChannelPanel",
        5: "uiRepPanel",
    }
    chart_adjust = {
        1: (208, 149, 804, 218),
        2: (1024, 149, 512, 218),
        3: (208, 380, 396, 270),
        4: (616, 380, 490, 270),
        5: (1118, 380, 418, 270),
    }
    for idx, (left, top, width, height) in chart_adjust.items():
        panel = ws.Shapes(panel_lookup[idx])
        panel.Left = left
        panel.Top = top
        panel.Width = width
        panel.Height = height
    chart_objects = ws.ChartObjects()
    for idx, title in enumerate(chart_titles, start=1):
        chart_obj = chart_objects.Item(idx)
        panel = ws.Shapes(panel_lookup[idx])
        chart_obj.Left = panel.Left + 8
        chart_obj.Top = panel.Top + 8
        chart_obj.Width = panel.Width - 16
        chart_obj.Height = panel.Height - 16
        chart = chart_obj.Chart
        chart.HasTitle = True
        chart.ChartTitle.Text = title
        chart.ChartTitle.Font.Name = "Aptos"
        chart.ChartTitle.Font.Size = 12.8 if idx in (3, 4, 5) else 13.2
        chart.ChartTitle.Font.Bold = True
        chart.ChartTitle.Font.Color = NAVY
        try:
            chart.ChartArea.Format.Line.Visible = False
        except Exception:
            pass
        try:
            chart.PlotArea.Format.Line.Visible = False
        except Exception:
            pass
        try:
            chart.ChartArea.Format.Fill.Visible = False
        except Exception:
            pass
        try:
            chart.PlotArea.Format.Fill.Visible = False
        except Exception:
            pass
        try:
            if chart.HasLegend:
                chart.Legend.Font.Name = "Aptos"
                chart.Legend.Font.Size = 7.2
                chart.Legend.Font.Color = SLATE
        except Exception:
            pass
        for axis_type in (1, 2):
            try:
                axis = chart.Axes(axis_type)
                axis.TickLabels.Font.Name = "Aptos"
                axis.TickLabels.Font.Size = 7
                axis.TickLabels.Font.Color = SLATE
                axis.Format.Line.ForeColor.RGB = LINE
            except Exception:
                pass
        if idx == 4:
            try:
                axis = chart.Axes(1)
                axis.TickLabels.Font.Size = 6.3
                axis.TickLabels.Orientation = 36
            except Exception:
                pass
            for sidx, fill_rgb in ((1, METRIC_BLUE), (2, METRIC_TEAL)):
                try:
                    series = chart.SeriesCollection(sidx)
                    series.Format.Fill.ForeColor.RGB = fill_rgb
                    series.Format.Line.ForeColor.RGB = fill_rgb
                except Exception:
                    pass
        for sidx in range(1, chart.SeriesCollection().Count + 1):
            try:
                series = chart.SeriesCollection(sidx)
                if series.ChartType not in {4, 65, 66, 67, 72, 73, 74, 75}:
                    series.HasDataLabels = True
                    labels = series.DataLabels()
                    labels.Font.Name = "Aptos"
                    labels.Font.Size = 7.2
                    labels.Font.Color = SLATE
                    labels.Font.Bold = True
            except Exception:
                pass

    ws.Activate()
    ws.Range("A1").Select()
    try:
        excel.ActiveWindow.Zoom = 75
        excel.ActiveWindow.DisplayGridlines = False
        excel.ActiveWindow.DisplayHeadings = False
        ws.DisplayPageBreaks = False
    except Exception:
        pass

    try:
        ws.Range("AE:XFD").EntireColumn.Hidden = True
        ws.Range("48:1048576").EntireRow.Hidden = True
    except Exception:
        pass

    wb.Save()
    excel.DisplayAlerts = prev_display_alerts
    excel.ScreenUpdating = prev_screen_updating
    if opened_here:
        wb.Close(True)
        excel.Quit()


if __name__ == "__main__":
    main()
