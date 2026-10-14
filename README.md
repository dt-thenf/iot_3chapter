# IoT System Design — Chương 3: Công nghệ mạng trong IoT

Biên soạn tiếng Việt theo toàn bộ **81 trang** của tài liệu *Chapter 3: Networking technologies in IoT* (TS. Nguyễn Đắc Cử, Phenikaa). Tách biệt `chapter3.tex` để sau có thể bổ sung các chương khác bằng `\input{chapter1.tex}` và `\input{chapter2.tex}` tại `main.tex`.

## Thành phần
- `main.tex`: tài liệu chủ LuaLaTeX, hiện biên dịch **chỉ Chương 3**.
- `chapter3.tex`: nội dung kiến thức tiếng Việt theo các chủ đề, bảng số liệu, sơ đồ vẽ bằng TikZ, nguồn đối chiếu slide.
- `source/chapter3-slides.pdf`: bản 81 trang để đối chiếu đồ họa nguồn. Lưu ý bản gốc có thể không được đưa vào repo công khai nếu không được phép tái phân phối.

## Biên dịch
Cần TeX Live hoặc MiKTeX với LuaLaTeX, `fontspec`, `babel-vietnamese`, `tikz`, `tcolorbox`, `booktabs`, `longtable` và phông DejaVu Serif.

```bash
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

PDF xuất ra: `main.pdf`. Các bảng và hình có chú thích số trang PDF gốc. Một số giá trị lịch sử chỉ có ý nghĩa trong bối cảnh slide, không phải thông số hiện hành của mọi sản phẩm.