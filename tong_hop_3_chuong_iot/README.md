# IoT — Tài liệu tổng hợp ba chương + ôn tập 6 câu

Thư mục độc lập; các file `chapter1.tex`, `chapter2.tex`, `chapter3.tex` và `on_tap_tu_luan_6_cau.tex` được **sao chép chính xác từ Git blob gốc**. Các file gốc trong repository không bị thay đổi.

- `iot_3_chuong.pdf`: tài liệu tổng hợp một bản gồm chương 1–3, mục lục, bảng biểu, công thức và hình minh họa.
- `on_tap_tu_luan_6_cau.pdf`: PDF riêng của file tự luận 6 câu.
- `main.tex`: cấu hình LuaLaTeX chung; `build.sh`: khôi phục slide Chương 2 và biên dịch 2 PDF.
- `assets/chapter1/`: ảnh đã sao chép; `source/base64/chapter2.part*.b64` và `scripts/build_chapter2.py`: phục hồi PDF hình minh họa Chương 2 không cần Internet.

### Biên dịch
```sh
cd tong_hop_3_chuong_iot
bash build.sh
```

Cần LuaLaTeX, TeX Live (latex-extra, lang-other, fonts-recommended), font DejaVu và Python 3.

**Lưu ý:** Không gộp các phụ lục slide nguyên bản 50/79/81 trang để tránh lặp nội dung. Hình tham chiếu trong phần diễn giải Chương 1–2 vẫn được đưa vào. Phụ lục gốc Chương 2 chỉ kích hoạt trong chế độ biên dịch từng chương riêng lẻ. Tôn trọng quyền tác giả đối với bài giảng và hình.
