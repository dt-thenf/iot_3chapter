# Cơ sở và thiết kế hệ thống IoT — Chương 3

Bản tổng hợp kiến thức **tiếng Việt** cho riêng Chương 3: *Networking technologies in IoT*, từ 81 trang slide do TS. Nguyễn Đắc Cử (Khoa Điện – Điện tử, Trường Đại học Phenikaa) giảng dạy. Bản biên soạn có diễn giải, các bảng đối chiếu thông số, sơ đồ TikZ, mục lục và ghi nguồn trang slide.

## Cấu trúc

- `chapter3.tex`: **toàn bộ nội dung kiến thức Chương 3**. Đây là một chapter độc lập có thể ghép vào bộ giáo trình ba chương.
- `main.tex`: preamble LuaLaTeX, bìa, mục lục. Hiện file **chỉ nhập `chapter3.tex`**, chưa tạo nội dung hai chương chưa được cung cấp. Sử dụng `\setcounter{chapter}{2}` để hiện đúng nhãn **Chương 3**.
- `source/base64/chapter3.part01.b64` … `chapter3.part09.b64`: 9 phần của bản PDF slide gốc; lưu theo dạng văn bản base64 để có thể quản lý qua GitHub Content API mà vẫn bảo toàn hình, bảng và hình vẽ trong slide. Các phần được kiểm tra lại bằng mã băm SHA-256.
- `scripts/rebuild_slide_pdf.py`: dựng lại `source/chapter3-slides.pdf` (81 trang) và kiểm tra SHA-256.
- `.github/workflows/build-chapter3.yml`: tự chạy LuaLaTeX, xuất `chapter3.pdf` 105 trang (nội dung tổng hợp + 81 slide gốc), đưa lên artifact và cập nhật PDF trong repo.

## Biên dịch trên máy tính

Yêu cầu TeX Live hoặc MiKTeX có **LuaLaTeX**, các gói `fontspec`, `babel-vietnamese`, `tikz`, `tcolorbox`, `booktabs`, `longtable`, `pdfpages`, phông **DejaVu Serif** và Python 3.

```bash
python3 scripts/rebuild_slide_pdf.py
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

`main.pdf` là bản hoàn chỉnh; bản xuất CI sẽ mang tên `chapter3.pdf`. Trong môi trường không ghép được slide PDF, nội dung tiếng Việt và các sơ đồ TikZ vẫn được biên dịch, nhưng sẽ không có phụ lục slide gốc.

## Nguyên tắc biên soạn

1. Biên soạn thành tài liệu kiến thức chứ không chuyển 81 slide thành 81 trang thuyết trình. Các thông tin đã được nhóm lại theo định danh/địa chỉ, giao thức truyền dẫn, bảo mật, định tuyến, các loại mạng và giao thức dữ liệu.
2. Những giá trị được ghi **theo slide** được giữ nguyên hoặc ghi chú khi có điểm chưa nhất quán. Không tự coi tốc độ/vùng phủ của bảng là cam kết kỹ thuật cho thiết bị hiện tại.
3. Phụ lục chứa 81 trang slide nguồn để rà soát toàn bộ hình minh họa và biểu đồ không thể chuyển sang văn bản.
4. Chưa thêm Chương 1 hay Chương 2. Khi có tài liệu, tạo `chapter1.tex`, `chapter2.tex` riêng và ghép vào `main.tex`, không trộn nội dung của các chương.

**Lưu ý sử dụng:** PDF gốc của bài giảng thuộc học liệu của tác giả/đơn vị tương ứng; người sử dụng chịu trách nhiệm bảo đảm quyền chia sẻ khi đưa repository vào chế độ công khai.