# Golden Reference Spec

## Mục tiêu

Tái tạo một executive dashboard trong Excel có trải nghiệm gần Power BI, nhưng vẫn refresh được bằng Power Query, Power Pivot, DAX, PivotTable, PivotChart và slicer.

## Hợp đồng về bố cục

- Header nền navy, tiêu đề dashboard rõ, subtitle nhỏ, thông tin as-of nằm bên phải.
- Bên trái là slicer rail riêng, không để worksheet grid lộ ra.
- Hàng KPI nằm ngang phía trên với các chip nhỏ màu ở phía đầu mỗi KPI card.
- Có 2 thanh section navy:
  - `EXECUTIVE TREND & KPI ATTAINMENT`
  - `MIX, CHANNEL & SALES EXECUTION`
- Cụm chart:
  - Trend chart ben trai, region chart ben phai
  - Hang duoi: category, channel efficiency, top sales reps
- Guide card nhỏ, gọn, nằm dưới slicer Sales Rep.

## Hợp đồng về dữ liệu

- Visual chính phải đi từ:
  - Power Query
  - Data Model / Power Pivot
  - DAX measures
  - PivotTable / PivotChart
- Không dùng chart thường để thay cho dashboard chính.
- Không cố định tên cột. Luôn map tên cột gốc sang vai trò nghiệp vụ.

## Hợp đồng về màu sắc

### KPI band

- Healthy = xanh lá
- Watch = amber
- Risk = đỏ

Chỉ dùng hệ màu này cho các visual thể hiện tình trạng KPI / attainment.

### Metric palette

Chart `Channel Efficiency | Gross Margin vs Trade Spend` phai dung:

- Gross Margin % = dark navy / metric blue
- Trade Spend % = teal / cyan

Không dùng màu KPI band cho chart này.

## Hợp đồng về UX

- Trend theo tháng không được mất ý nghĩa khi user chọn slicer Month.
- Nếu cần, giảm kết nối slicer đến chart trend thay vì để chart chỉ còn 1 điểm vô nghĩa.
- Màu chart phải ổn định theo ý nghĩa, không nhảy linh tinh theo slicer.
- Số liệu hiển thị cần dễ đọc nhanh:
  - B / M / K neu phu hop
  - phần trăm có độ chính xác vừa đủ
  - data label cho column / bar chart khi cần đọc giá trị
- Không để subtitle, slicer caption, guide text, legend, title bị cắt.

## Hợp đồng về workbook

- Sheet dashboard phải là sheet active lúc lưu.
- Workbook window phải visible, không được mở lên trắng trang chỉ vì hidden window.
- Zoom mặc định = 75%.
- Gridlines và headings nên được tắt ở dashboard.
- Nếu file gốc ở OneDrive / cloud path, nên xuất thêm 1 bản local để mở ổn định.

## Các visual ưu tiên

- Monthly Revenue Trend
- Revenue by Region
- Revenue by Category
- Channel Efficiency
- Top Sales Reps

## Guide card đúng

- `Healthy: att. >= 95%`
- `Watch: 90% <= att. < 95%`
- `Risk: att. < 90%`
