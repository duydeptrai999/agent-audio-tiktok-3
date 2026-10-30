# -*- coding: utf-8 -*-
with open("GEMINI.md", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_part = """### 🎨 2. QUY CHUẨN ĐỒ HỌA & BAO BÌ THỊ GIÁC (PACKAGING DESIGN SYSTEM CODEX 8.5)

> 🚨 **TRIỆT TIÊU VĨNH VIỄN BỆNH "CHỮ TRÊN NỀN BÓNG ĐEN XẤU NHƯ CỨT"**:
> Khán giả lướt TikTok nhìn Thumbnail và Header Video trong 0.5 giây đầu tiên.
> Bao bì phải đạt đẳng cấp điện ảnh sang trọng, hiện đại, không dùng các khối hộp đen/đỏ che khuất video!

1. **Bộ Font Chuẩn Độc Tôn: Be Vietnam Pro**:
   - Tên Phim (Main Title): Font `BeVietnamPro-Black` hoặc `ExtraBold` (60pt - 72pt), nét dày dặn, sang trọng, bo viền đổ bóng nổi khối.
   - Huy Hiệu Tập (Episode Pill Badge) & Mô Tả (Subtitle): Font `BeVietnamPro-SemiBold` (34pt - 42pt), sắc nét, dễ đọc trên màn hình điện thoại.
   - BẮT BUỘC dùng font chuẩn tiếng Việt hoàn hảo, chống hoàn toàn hiện tượng vỡ dấu, nhảy font hệ thống hoặc lệch dòng.
2. **Loại Bỏ Hoàn Toàn Hộp Đen Thô Cứng (Zero Hard Black Box)**:
   - TUYỆT ĐỐI CẤM: `drawbox=color=black@0.76` hoặc các thanh hộp chữ nhật đỏ đập vào mắt người xem.
   - THAY THẾ BẰNG: Dải chuyển sắc dọc mềm mại (Soft Vertical Gradient `rgba(0,0,0,0.85)` ở đỉnh -> mờ dần trong suốt tại 380px), kết hợp đổ bóng chữ Gaussian đa tầng (`radius=14-18`, offset `+3..+5`).
3. **Bảng Màu Nhận Diện Theo Thể Loại (Genre Palettes)**:
   - `SA_DIEU` / `HAO_MON`: Vàng Ánh Kim Hoàng Gia (`#FFE066`, `#F59E0B`).
   - `THANH_XUAN` / `CHUA_LANH`: Xanh Cyan Ngọc Bích Tươi Sáng (`#38BDF8`, `#0284C7`).
   - `GIA_DAU` / `TRONG_SINH`: Hồng Đào / Đỏ Hồng Quyền Lực (`#FB7185`, `#E11D48`).
   - `TRINH_THAM` / `TRUE_CRIME`: Hổ Phách Cảnh Báo (`#FBBF24`, `#D97706`).
   - `KINH_DI` / `QUAI_DAM`: Đỏ Thẫm Máu Rùng Rợn (`#F43F5E`, `#BE123C`).
4. **Huy Hiệu Bo Góc (Rounded Pill Badge) & Phân Tầng Thị Giác**:
   - Huy hiệu `[TẬP 1]`, `[TẬP 2]`, `[TẬP 3 - KẾT]` dạng viên thuốc bo tròn (Rounded Pill, `radius=16`), nền mờ bán trong suốt `rgba(0,0,0,0.55)` viền neon tinh tế.
   - Bố cục Thumbnail nằm trọn trong Vùng An Toàn Lưới Hồ Sơ TikTok 3:4 (Y: 520px - 1400px), không bị ảnh đại diện hay nút giao diện che khuất."""

new_part = """### 🎨 2. QUY CHUẨN ĐỒ HỌA & BAO BÌ THỊ GIÁC (PACKAGING DESIGN SYSTEM CODEX 8.5)

> 🚨 **TRIỆT TIÊU VĨNH VIỄN BỆNH "CHỮ TRÊN NỀN BÓNG ĐEN XẤU NHƯ CỨT" & "THUMBNAIL BỊ KÉO DÃN MÉO HÌNH"**:
> - Khán giả lướt TikTok nhìn video trong 0.5 giây đầu tiên. Video phải trong trẻo, sang trọng, sáng rõ từng chi tiết B-roll.
> - TUYỆT ĐỐI KHÔNG làm thumbnail ảnh tĩnh rời tải lên vì TikTok Studio sẽ kéo dãn méo hình! TikTok lấy trực tiếp frame gốc chuẩn dọc 1080x1920 (setsar=1) từ video MP4 đã khắc sẵn Header Text Title và Mô Tả sắc nét.

1. **Bộ Font Chuẩn Độc Tôn: Be Vietnam Pro**:
   - Tên Phim (Main Title): Font `BeVietnamPro-ExtraBold` hoặc `Black` (46pt - 50pt), trắng tinh khiết `(255, 255, 255)`, viền vi mảnh sắc nét (sharp micro-stroke 2px `rgb(12, 16, 24)`), căn giữa, tối đa 2 dòng.
   - Mô Tả Phim / Tập (Subtitle): Font `BeVietnamPro-SemiBold` (30pt - 34pt), màu pastel dịu mắt theo thể loại, viền 2px chống lóa, căn giữa.
   - Huy Hiệu Tập (Episode Pill Badge): Bo tròn capsule hiện đại (`radius=ph//2`), viền trắng mờ tinh tế 1px, màu nền theo thể loại, chữ sắc nét, KHÔNG bóng đen nhòe.
2. **Loại Bỏ Hoàn Toàn Hộp Đen Thô Cứng & Bóng Đen Nhòe (Zero Hard Box & Zero Muddy Shadow)**:
   - TUYỆT ĐỐI CẤM: `drawbox=color=black@0.76` hoặc các dải gradient đen sẫm che tối mịt video B-roll.
   - THAY THẾ BẰNG: Dải scrim siêu nhẹ ở đỉnh (alpha max chỉ 55, mờ dần về trong suốt tại y=360), kết hợp micro-stroke 2px. Video nền ASMR giữ nguyên 100% độ sáng, độ trong và màu sắc tự nhiên.
3. **Bảng Màu Nhận Diện Theo Thể Loại (Genre Palettes)**:
   - `SA_DIEU` / `HAO_MON`: Vàng Ánh Kim Hoàng Gia (`#FFE066`, `#F59E0B`).
   - `THANH_XUAN` / `CHUA_LANH`: Xanh Cyan Ngọc Bích Tươi Sáng (`#38BDF8`, `#0284C7`).
   - `GIA_DAU` / `TRONG_SINH`: Hồng Đào / Đỏ Hồng Quyền Lực (`#FB7185`, `#E11D48`).
   - `TRINH_THAM` / `TRUE_CRIME`: Hổ Phách Cảnh Báo (`#FBBF24`, `#D97706`).
   - `KINH_DI` / `QUAI_DAM`: Đỏ Thẫm Máu Rùng Rợn (`#F43F5E`, `#BE123C`).
4. **Vùng An Toàn Top Safe Zone (y = 135 .. 380)**:
   - Toàn bộ khối tiêu đề nằm chuẩn bên dưới thanh tab "Following | For You" của TikTok, không bị giao diện che khuất, giải phóng 80% màn hình phía dưới cho B-roll thôi miên và phụ đề động."""

old_caption_doc = """### 📝 4. QUY CHUẨN MÔ TẢ & BÌNH LUẬN ĐỘNG THEO TẬP (DYNAMIC CAPTIONS & MAGNETS)
1. **Mỗi Tập Có Trích Đoạn Riêng Biệt (Per-Part Snippet Extraction)**:
   - Tập 1: Trích 18-22 từ mở màn gây tò mò -> Đặt câu hỏi mâu thuẫn gia đình / tình cảm.
   - Tập 2: Trích 18-22 từ biến cố cao trào -> Đặt câu hỏi đấu trí / vạch mặt.
   - Tập 3: Trích 18-22 từ đại kết cục -> Đặt câu hỏi đánh giá sự trừng phạt / bài học nhân sinh.
2. **CẤM Tuyệt Đối Câu Hỏi Robot "Bình Luận 1 Hoặc 2"**:
   - Kêu gọi tranh luận đời thường tự nhiên theo đúng tâm lý người nghe, kích thích tương tác giữ chân người xem."""

new_caption_doc = """### 📝 4. QUY CHUẨN MÔ TẢ & BÌNH LUẬN ĐỘNG THEO TẬP (DYNAMIC CAPTIONS & MAGNETS)
1. **Cấu Trúc Mô Tả Bài Đăng TikTok Đa Tầng Sang Trọng**:
   - Dòng 1: `[TẬP X] Tên Phim`
   - Dòng 2: `📖 Mô tả phim / Tập`
   - Dòng 3: `💬 Câu hỏi thảo luận / Bẫy tâm lý kích thích tương tác theo tập`
   - Dòng 4: `👉 Cắm tai nghe thưởng thức trọn bộ tại kênh!`
   - Dòng 5: `#audiotruyen #kechuyen #xuhuong #fyp #tagtheloai`
2. **CẤM Tuyệt Đối Câu Hỏi Robot "Bình Luận 1 Hoặc 2"**:
   - Kêu gọi tranh luận đời thường tự nhiên theo đúng tâm lý người nghe, kích thích tương tác giữ chân người xem."""

assert old_part in t_norm, "old_part not found"
assert old_caption_doc in t_norm, "old_caption_doc not found"

t_norm = t_norm.replace(old_part, new_part)
t_norm = t_norm.replace(old_caption_doc, new_caption_doc)

final = t_norm.replace("\n", "\r\n")

with open("GEMINI.md", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated GEMINI.md successfully!")
