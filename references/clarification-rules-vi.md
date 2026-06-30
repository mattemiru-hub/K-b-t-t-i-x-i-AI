# Quy Tắc Hỏi Lại Trước Khi Build Dashboard

Mục tiêu của file này là buộc AI hỏi lại đúng các câu cần thiết trước khi động vào cấu trúc workbook, thay vì tự đoán các field quan trọng.

## Khi nào phải hỏi lại

AI phải dừng và hỏi lại nếu gặp một trong các trường hợp sau:

- không rõ sheet nào là raw data chính
- có nhiều sheet raw và không có sheet nào nổi bật rõ ràng
- có nhiều cột ngày và không rõ cột nào là trục thời gian chính
- có nhiều cột doanh thu hoặc sales amount
- user muốn target vs actual nhưng không rõ cột target
- không rõ dimension nào tương ứng với Region, Channel, Category, Area Manager, hoặc Sales Rep
- không rõ nên giữ dashboard hiện tại để polish hay rebuild lại hoàn toàn
- có KPI được yêu cầu nhưng workbook hiện tại chưa có dữ liệu đủ để tính

## Khi nào có thể không cần hỏi

AI có thể tự tiếp tục nếu:

- workbook chỉ có một sheet raw rõ ràng
- field date, revenue, và target có tên hoặc ngữ nghĩa rất rõ
- layout đã được cố định bởi golden reference
- user không yêu cầu thay đổi phong cách visual

## Các field không được phép đoán bừa

Các field sau là business-critical, không được tự đoán khi có hơn một khả năng hợp lý:

- date field chính
- revenue hoặc sales actual
- target hoặc plan
- gross margin nếu có nhiều biến thể
- dimension dùng để điều khiển slicer chính

## Thứ tự hỏi ưu tiên

Khi cần hỏi lại, AI nên hỏi theo thứ tự:

1. raw data sheet
2. date field
3. revenue field
4. target field
5. slicer dimensions
6. giữ dashboard cũ hay rebuild

## Mẫu câu hỏi nên dùng

AI nên dùng câu ngắn, cụ thể, ít mở rộng:

1. Sheet raw data chính là sheet nào?
2. Cột nào là ngày chính để làm trend?
3. Cột nào là doanh thu thực tế?
4. Cột nào là target hoặc kế hoạch?
5. Với workbook này, field nào tương ứng Region, Channel, Category, Area Manager, Sales Rep?
6. Bạn muốn giữ dashboard hiện tại để polish hay rebuild lại từ đầu?

## Nguyên tắc hỏi

- chỉ hỏi những gì thực sự chặn việc làm tiếp
- gom câu hỏi thành một cụm ngắn thay vì hỏi lan man từng câu rời rạc
- nếu chỉ thiếu một mapping, chỉ hỏi đúng một mapping đó
- không hỏi lại những thứ đã được golden reference cố định
- sau khi user trả lời, AI phải bám đúng câu trả lời đó trong toàn bộ phần build

## Quy tắc dừng

Nếu chưa rõ các mapping bắt buộc, AI không được:

- tự dựng query chính
- tự tạo DAX measure business-critical
- tự dựng slicer rail hoàn chỉnh
- tự build KPI cards dựa trên mapping mơ hồ

Phải hỏi lại trước rồi mới làm tiếp.
