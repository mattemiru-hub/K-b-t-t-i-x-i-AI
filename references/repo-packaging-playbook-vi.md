# Playbook Đóng Gói Repo Skill Hoàn Chỉnh

File này là checklist để lần sau dựng một repo skill hoàn chỉnh ngay từ đầu, tránh kiểu làm xong mới vá dần.

## 1. Xác định repo này là gì

Ngay từ đầu phải chốt:

- đây là skill repo hay chỉ là repo tài liệu
- skill này dùng để build mới, polish, audit, hay cả ba
- output cuối cùng là file gì
- AI có được phép tự đoán hay phải hỏi lại

Nếu chưa chốt 4 ý này, repo sẽ dễ bị nửa tài liệu nửa workflow, dùng không dứt điểm.

## 2. Bộ khung tối thiểu phải có

Một repo skill dùng thật nên có tối thiểu:

- `SKILL.md`
- `README.md`
- `README_vi.md` nếu người dùng chính là tiếng Việt
- `references/`
- `scripts/`
- `examples/`
- `sample-output/`
- `CHANGELOG.md`
- `LICENSE`
- `agents/openai.yaml` nếu muốn package nhìn chuẩn hơn

## 3. `SKILL.md` phải có gì

Không chỉ mô tả chung chung. Phải có:

- quick start
- workflow theo thứ tự thực thi
- clarification gate
- non-negotiables
- script notes
- deliverables

Thiếu clarification gate thì AI dễ đoán. Thiếu non-negotiables thì output dễ trôi style.

## 4. `references/` phải có gì

Ít nhất nên có:

- visual contract hoặc golden-reference spec
- prompt template
- QA checklist
- clarification rules

Đây là nơi giữ những rule dài, để `SKILL.md` gọn nhưng vẫn đủ mạnh.

## 4.1. Nếu muốn tái dùng nhiều lần

Nếu muốn lần sau không dựng lại bằng tay, nên thêm:

- `scripts/init_standard_skill_repo.ps1` để tạo repo mới từ template dựng sẵn

Như vậy lần sau chỉ cần thay tên skill, display name, và domain summary là có ngay một repo đủ bộ để tinh chỉnh tiếp.

## 5. `README.md` phải phục vụ người mới

README tốt phải trả lời được ngay:

- repo này dùng để làm gì
- cài thế nào
- gọi skill ra sao
- có script gì
- đầu ra mong đợi là gì
- khác gì với chỉ viết prompt tay

Nếu người mới mở repo mà vẫn chưa biết bắt đầu từ đâu, README chưa đạt.

## 6. Phải test cài thật

Trước khi coi repo là hoàn chỉnh, phải test:

- cài từ GitHub repo
- cài bằng script local nếu repo có script cài
- mở được `SKILL.md`
- cấu trúc file sau khi cài không bị thiếu

Không test cài thật thì repo rất dễ “nhìn đúng nhưng dùng không được”.

## 7. Phải test hành vi thật

Không chỉ test cài. Còn phải test:

- AI có nhận đúng skill không
- AI có hỏi lại khi mapping mơ hồ không
- AI có giữ đúng non-negotiables không
- AI có đọc reference đúng thứ tự không

## 8. Phải có sample output

Repo càng giống sản phẩm thật càng tốt. Nên có:

- preview image
- sample-output README
- mô tả gói bàn giao cuối cùng

Như vậy người dùng biết “output đẹp” trông như thế nào.

## 9. Phải có release đầu tiên

Khi repo đã dùng được, nên chốt:

- description
- topics
- release tag đầu tiên
- release note

Làm vậy để repo có trạng thái public-ready rõ ràng.

## 10. Checklist hoàn chỉnh 1 lần

Lần sau nếu muốn làm một mạch cho trọn, nên đi theo thứ tự này:

1. chốt mục tiêu repo
2. dựng `SKILL.md`
3. dựng `references/`
4. dựng `README.md` và `README_vi.md`
5. thêm `scripts/`
6. thêm `examples/` và `sample-output/`
7. test cài thật
8. test hành vi thật
9. sửa lỗi wording, cấu trúc, và install path
10. publish release đầu tiên

## Kết luận

Một repo skill hoàn chỉnh không chỉ là có `SKILL.md`.

Nó phải đủ 4 lớp:

- hướng dẫn dùng
- luật vận hành
- tài liệu tham chiếu
- kiểm thử cài và hành vi

Đủ 4 lớp này thì lần sau AI và người dùng mới không phải mò lại từ đầu.
