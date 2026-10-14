# Hướng dẫn riêng cho Chương 1 -- Tổng quan IoT

**Hiện chỉ thực hiện Chương 1**, dựa trên 50 slide `Chapter 1_An overview of IoT.pdf` (TS. Nguyễn Đắc Cử, Khoa Điện--Điện tử, Trường Đại học Phenikaa). Không thay đổi bất kỳ tệp Chương 2 hoặc Chương 3 nào đã hiện diện trong repo; chỉ bàn giao Chương 1.

## Cấu trúc

- `chapter1_main.tex`: tài liệu gốc, định dạng tiếng Việt và khung ghép các chương.
- `chapter1.tex`: **duy nhất nội dung chương 1**, chứa 6 phần kiến thức, bảng, ví dụ, kiến trúc IoT 3--7 tầng, phần đối chiếu slide nguồn.
- `scripts/extract_chapter1_slides.py`: sinh JPEG hình minh họa gốc từ file PDF bài giảng do người học tự cung cấp.
- `assets/chapter1/`: chứa 21 ảnh trích từ các slide có sơ đồ/hình quan trọng và được chèn trong `chapter1.tex`. Script có thể xuất lại toàn bộ 50 ảnh khi có file PDF nguồn.

## Biên dịch PDF bằng LuaLaTeX

1. Cài TeX Live với LuaLaTeX, các gói trong `chapter1_main.tex` và Python `PyMuPDF`.
2. Đặt file `Chapter 1_An overview of IoT.pdf` tại thư mục gốc repo (file này không được tự động upload lên repo).
3. Chạy `python scripts/extract_chapter1_slides.py 'Chapter 1_An overview of IoT.pdf'` để trích xuất toàn bộ hình minh họa từ 50 slide.
4. Chạy `lualatex -interaction=nonstopmode chapter1_main.tex` hai lần để cập nhật mục lục.

Trong repo đã có 21 hình minh họa được chèn trong chương 1, nên chỉ cần LuaLaTeX là có thể biên dịch bản tiếng Việt. Khi có PDF gốc, có thể sinh lại ảnh ở chất lượng cao, hoặc đặt nó tại `chapter1_source.pdf` để chương trình tự nối **50 trang slide gốc** vào cuối PDF như phụ lục đối chiếu. Gói ZIP bàn giao kèm PDF gốc và bản PDF trên 70 trang.

## Cách mở rộng

Khi có chương tiếp theo, tạo `chapter2.tex`, `chapter3.tex`, rồi bỏ ký tự `%` ở hai lệnh `\input{chapter2.tex}` và `\input{chapter3.tex}` trong `chapter1_main.tex`. Không cần chỉnh sửa `chapter1.tex`.

## Nguồn và ghi chú

Tài liệu tiếng Việt là bản tổng hợp diễn giải để học tập dựa trên nội dung nguồn cung cấp, có đánh dấu các trang slide tương ứng. Các số liệu dự báo 2025 từ slide được giữ nguyên bối cảnh là *dự báo*, không được coi là số liệu thực tế ở thời điểm hiện nay. Các hình slide và logo giữ quyền của chủ sở hữu; tránh tái phân phối công khai nếu chưa có quyền phù hợp.

**Lưu ý tích hợp repo:** file `main.tex` sẵn có thuộc Chương 3, do đó tài liệu Chương 1 biên dịch qua `chapter1_main.tex`, hoàn toàn không ghi đè cấu hình hiện tại.