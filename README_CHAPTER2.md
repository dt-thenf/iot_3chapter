# Chương 2 – Phần cứng IoT (IoT Hardware)

Tài liệu tiếng Việt biên soạn riêng từ **79 trang slide của TS. Nguyễn Đắc Cử**, Khoa Điện – Điện tử, Trường Đại học Phenikaa. Không chứa nội dung các chương khác. Module chapter2.tex có thể ghép về sau bằng lệnh LaTeX input.

## Cấu trúc

- **chapter2.tex** – toàn bộ phần tổng hợp: cảm biến, cơ cấu chấp hành, nút cảm biến, ATmega328P, Arduino và lập trình, ESP8266, ESP32, Intel Edison, điện toán biên và Raspberry Pi.
- **chapter2_main.tex** – tài liệu chủ riêng của Chương 2, sử dụng LuaLaTeX và bật phụ lục 79 trang.
- **source/base64/chapter2.part01.b64 đến chapter2.part12.b64** – 12 phần dữ liệu mã hóa của PDF slide gốc 79 trang, đã lưu trong GitHub nhằm giữ đầy đủ hình ảnh và bảng minh họa.
- **scripts/build_chapter2.py** – ghép và giải mã 12 phần thành assets/chapter2_original_slides.pdf, xác minh SHA-256, tùy chọn biên dịch.

## Biên dịch bản có đầy đủ hình minh họa

Cài đặt Python 3 và TeX Live/MiKTeX có LuaLaTeX, fontspec, babel-vietnamese, tikz, tcolorbox, pdfpages, listings, longtable, cùng phông DejaVu.

Tại thư mục gốc repository chạy:

    python scripts/build_chapter2.py --compile

Chương trình tạo lại PDF nguồn, so sánh SHA-256, rồi gọi LuaLaTeX hai lần. Kết quả: chapter2_main.pdf. Bản biên dịch đầy đủ đã kiểm tra ở môi trường tác giả gồm 118 trang, bao gồm phụ lục nguyên bản 79 slide.

Có thể chạy thủ công:

    python scripts/build_chapter2.py
    lualatex -interaction=nonstopmode -halt-on-error chapter2_main.tex
    lualatex -interaction=nonstopmode -halt-on-error chapter2_main.tex

## Ghép nhiều chương sau này

Đưa lệnh LaTeX \input{chapter2.tex} vào tài liệu chủ đã khai báo các gói và macro của Chương 2. Khi không khai báo \iotstandalone, phụ lục 79 trang sẽ không được tự động chèn sau Chương 2; tài liệu chủ vẫn có thể nhập Chương 1 và Chương 3 theo đúng thứ tự. Tệp chapter2_main.tex chủ động bật \iotstandalone để biên dịch riêng đủ chương và slide gốc.

## Đối chiếu slide

Toàn bộ 79 trang slide, bao gồm hình minh họa, pinout và ảnh màn hình IDE, đều được khôi phục nguyên dạng từ Base64. Phần nội dung tiếng Việt ghi số trang tham chiếu. Các số liệu lịch sử trong slide không tự động được xem là thông số hiện hành của mọi dòng sản phẩm.

**Bản quyền:** Bài giảng gốc thuộc quyền của các chủ sở hữu tương ứng. Việc phát hành lại ngoài phạm vi được cho phép cần tuân thủ quyền tác giả.
