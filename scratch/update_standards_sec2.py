# -*- coding: utf-8 -*-
with open(".agents/rules/scriptwriting_standards.md", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_sec2 = """## 2. QUY CHUẨN ĐỒ HỌA & BAO BÌ THỊ GIÁC (PACKAGING DESIGN SYSTEM CODEX 8.5)

1. **Bộ Font Chuẩn Độc Tôn: Be Vietnam Pro**:
   - Font `BeVietnamPro-Black` cho Tên Phim (Main Title) to bản nổi bật (60pt - 72pt).
   - Font `BeVietnamPro-SemiBold` cho Huy Hiệu Tập (Episode Badge) và Mô Tả (Subtitle) (34pt - 42pt).
   - 100% chuẩn dấu tiếng Việt, không bị vỡ font, không bị lỗi dấu thanh.
2. **Loại Bỏ Hộp Đen Thô Cứng (Zero Hard Black Box)**:
   - TUYỆT ĐỐI CẤM: `drawbox=color=black@0.76` hoặc các khối chữ nhật màu đỏ chói mắt.
   - Dùng Dải chuyển sắc mềm (Soft Vertical Gradient `rgba(0,0,0,0.85)` mờ dần đến trong suốt) kết hợp đổ bóng chữ Gaussian đa tầng (`radius=14-18`, offset `+3..+5`).
3. **Hệ Thống Bảng Màu Thể Loại (`GENRE_PALETTES`)**:
   - Sa điêu/Hào môn: Vàng ánh kim (`#FFE066`, `#F59E0B`).
   - Thanh xuân/Chữa lành: Xanh Cyan ngọc bích (`#38BDF8`, `#0284C7`).
   - Gia đấu/Mẹ chồng: Hồng đào quyền lực (`#FB7185`, `#E11D48`).
   - Trinh thám/Kỳ án: Hổ phách bí ẩn (`#FBBF24`, `#D97706`).
   - Kinh dị/Quái đàm: Đỏ thẫm máu rùng rợn (`#F43F5E`, `#BE123C`).
4. **Huy Hiệu Bo Góc (Rounded Pill Badge)**:
   - Huy hiệu `[TẬP 1]`, `[TẬP 2]`, `[TẬP 3 - KẾT]` dạng viên thuốc bo tròn mềm mại (`radius=16`).
   - Bố cục Thumbnail nằm trọn trong Vùng An Toàn Lưới Hồ Sơ TikTok 3:4."""

new_sec2 = """## 2. QUY CHUẨN ĐỒ HỌA & BAO BÌ THỊ GIÁC (PACKAGING DESIGN SYSTEM CODEX 8.5)

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
3. **Hệ Thống Bảng Màu Thể Loại (`GENRE_PALETTES`)**:
   - Sa điêu/Hào môn: Vàng ánh kim (`#FFE066`, `#F59E0B`).
   - Thanh xuân/Chữa lành: Xanh Cyan ngọc bích (`#38BDF8`, `#0284C7`).
   - Gia đấu/Mẹ chồng: Hồng đào quyền lực (`#FB7185`, `#E11D48`).
   - Trinh thám/Kỳ án: Hổ phách bí ẩn (`#FBBF24`, `#D97706`).
   - Kinh dị/Quái đàm: Đỏ thẫm máu rùng rợn (`#F43F5E`, `#BE123C`).
4. **Vùng An Toàn Top Safe Zone (y = 135 .. 380)**:
   - Toàn bộ khối tiêu đề nằm chuẩn bên dưới thanh tab "Following | For You" của TikTok, không bị giao diện che khuất, giải phóng 80% màn hình phía dưới cho B-roll thôi miên và phụ đề động."""

assert old_sec2 in t_norm, "old_sec2 not found"
t_norm = t_norm.replace(old_sec2, new_sec2)
final = t_norm.replace("\n", "\r\n")

with open(".agents/rules/scriptwriting_standards.md", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated scriptwriting_standards.md successfully!")
