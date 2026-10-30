import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read source with 100 cases
with open('docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md', 'r', encoding='utf-8') as f:
    source_text = f.read()

# Split out Phần 2 (100 cases) and subsequent parts
marker = "## PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM"
parts = source_text.split(marker)
p1_raw = parts[0]
cases_p2_and_p3 = marker + parts[1]

# Build enhanced Codex 8.0 Frontmatter and Preface
new_header = """# 📘 TỔNG TẬP ĐẠI KINH NGHIỆM SẢN XUẤT AUDIO DRAMA TIKTOK TRIỆU VIEW (MASTER CODEX 8.0)
*Siêu Cẩm Nang Thực Chiến Độc Bản: Đúc Kết Từ Đại Khảo Sát Toàn Diện 100 Audio Triệu View Dẫn Đầu TikTok Việt Nam & Tái Cấu Trúc Toàn Diện Team Agent.*
*Quy chuẩn tối cao: TAI NGHE NGƯỜI THẬT - TỰ NHIÊN ĐỜI THƯỜNG - TRIỆT TIÊU 100% SỰ SƯỢNG TRÂN & HOẠT HÌNH HÓA.*

---

## 🌟 MỤC LỤC TỔNG QUAN
1. **LỜI CẢNH TỈNH XƯƠNG MÁU**: Giải mã gốc rễ bệnh "Kịch bản đến chính mình nghe còn đéo thẩm được" và bản án khai tử vĩnh viễn.
2. **PHẦN 1: CẨM NANG ĐẠI KINH NGHIỆM ĐA CHIỀU (7 CHƯƠNG THỰC CHIẾN ĐỈNH CAO)**
   - Chương 1: Bản Đồ Tâm Lý Thính Giả TikTok VN (Thói quen nghe 30 phút, 4 khao khát cảm xúc).
   - Chương 2: Nghệ Thuật Biên Kịch Đời Thường & Tiêu Diệt Bệnh Hoạt Hình Ba Xu (100% logic đời sống, đối thoại thuần Việt).
   - Chương 3: 4 Công Thức Mở Đầu 3 Giây - 15 Giây Thôi Miên (Hook Codex 8.0).
   - Chương 4: Đạo Diễn Âm Thanh Edge-TTS & BGM Sidechain Ducking -22dB (Giọng Hoài My / Nam Minh, nhịp thở 10-18 từ).
   - Chương 5: Giám Tuyển Thị Giác Video Nền ASMR Thôi Miên (B-roll dọc 9:16, Clean Screen).
   - Chương 6: Tâm Lý Giữ Chân (Retention Engine) & Nam Châm Bình Luận Phân Cực (Comment Magnets).
   - Chương 7: Tổ Chức Team Agent Biên Kịch Chuyên Nghiệp (Ma Trận 6 Subagents Codex 8.0).
3. **PHẦN 2: KHO BÁU ĐỦ 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM (#001 - #100)**
   - Nhóm 1: Sa Điêu / Tiếng Lòng / Hài Hước Công Sở (Case #001 - #010)
   - Nhóm 2: Trọng Sinh / Vả Mặt Báo Thù / Ác Nữ Thức Tỉnh (Case #011 - #020)
   - Nhóm 3: Mẹ Chồng Nàng Dâu / Gia Đấu Đời Thực / Ly Hôn Chia Tài Sản (Case #021 - #030)
   - Nhóm 4: Thật Giả Thiên Kim / Hoán Đổi Số Phận / Hắt Hủi Con Ruột (Case #031 - #040)
   - Nhóm 5: Hào Môn Tổng Tài / Cưới Trước Yêu Sau / Cá Mặn Gả Trùm Hắc Bang (Case #041 - #050)
   - Nhóm 6: Thanh Xuân Vườn Trường / Học Bá Oan Gia / Đại Ca Bảo Kê (Case #051 - #060)
   - Nhóm 7: Confession Bóc Phốt / Bạn Thân Cướp Bồ / Trả Giá Đời Thực (Case #061 - #070)
   - Nhóm 8: True Crime / Kỳ Án Pháp Y / Tâm Lý Tội Phạm (Case #071 - #080)
   - Nhóm 9: Cung Đấu / Trạch Đấu Nữ Quyền / Dưỡng Lão Lãnh Cung (Case #081 - #090)
   - Nhóm 10: Kinh Dị Đô Thị / Quy Tắc Quái Đàm / Tiếng Khóc Đêm Muộn (Case #091 - #100)
4. **PHẦN 3: DEEP DIVE PHÂN TÍCH TỪNG GIÂY CÁC AUDIO VIRAL MẪU MỰC (Túi Mù Audio, Dứa Audio, Tâm Hồn Ăn Uống)**
5. **PHẦN 4: HỆ THỐNG TEAM AGENT ĐƯỢC TỐI ƯU HÓA HOÀN TOÀN THEO 100 CASE STUDY (CODEX 8.0)**
6. **PHẦN 5: BẢNG CHECKLIST VÀNG KIỂM ĐỊNH TAI NGHE NGƯỜI THẬT (BẮT BUỘC 10/10)**

---

## LỜI CẢNH TỈNH XƯƠNG MÁU: VÌ SAO KỊCH BẢN CŨ BỊ NGƯỜI NGHE "ĐÉO THẨM ĐƯỢC"?

Khán giả TikTok ngày nay cực kỳ thông minh, nhạy bén và có đôi tai sành sỏi. Họ sẵn sàng cắm tai nghe 25 đến 35 phút (chia 3 tập) để đắm chìm vào một câu chuyện có chiều sâu cảm xúc. Nhưng nếu câu chuyện giả tạo, họ sẽ lướt qua ngay trong 10 giây đầu!

> 🚨 **CHẨN ĐOÁN 4 CĂN BỆNH CHẾT NGƯỜI CỦA KỊCH BẢN AI VỪA QUA**:
> 1. **Bệnh 'Hoạt Hình Hóa Ba Xu' & Ác Ngô Nghê**:
>    - Nhân vật phản diện bị xây dựng ác một cách ngu xuẩn, kệch cỡm: Mẹ chồng đứng ngoài cửa phòng sinh chê cháu gái là vịt trời, mang cặp lồng 3 cái cổ gà héo úa; em chồng nhảy lên sofa da 80 triệu cắn hạt dưa và vẽ bút sáp màu lên tường; chồng vung tay định tát vợ trước mặt cả họ.
>    - Nhân vật chính thì hô khẩu hiệu gượng gạo: Giơ điện thoại bật quay 4K dọa gửi ban giám đốc, khoe bố là cựu thẩm phán, kéo công an phường và 4 nhân viên mặc đồng phục vệ sĩ chuyên nghiệp vào dẹp tiệc tân gia.
>    - **Hậu quả**: Nghe như phim hoạt hình con nít! Không một người trưởng thành nào hành xử như vậy ngoài đời thực!
> 2. **Bệnh Sáo Ngữ Convert / Văn Dịch Cải Lương**:
>    - Lạm dụng từ ngữ lỗi thời: *"thập tử nhất sinh"*, *"nước mắt ứa ra nơi khóe mi vì cay đắng tột cùng"*, *"ánh mắt sắc bén như hai lưỡi dao cạo"*, *"tiện nhân"*, *"đồ lăng loàn"*, *"quân giết người quân vô phúc"*, *"bàn tay to bè giáng xuống trong gang tấc"*.
> 3. **Bệnh Ép Giọng Đọc Edge-TTS Đọc Văn Bản Vô Hồn**:
>    - Câu văn dài ngoằng, nhiều mệnh đề phụ không có dấu ngắt nghỉ, nhồi nhét dấu ba chấm '...' bừa bãi khiến giọng đọc Hoài My / Nam Minh bị hụt hơi, ngắc ngứ, đều đều như trả bài.
> 4. **Bệnh Mẫu Câu Máy Móc Rập Khuôn**:
>    - Dùng câu mở đầu và câu kêu gọi như rô-bốt: *"Chào mừng các bạn đến với tập 1..."*, *"Theo bạn nhân vật chính nên chọn phương án 1 hay 2..."*.

Cẩm nang Master Codex 8.0 này được viết ra để **KHAI TỬ TRIỆT ĐỂ 4 CĂN BỆNH TRÊN**, biến toàn bộ hệ thống Agent thành cỗ máy sản xuất kịch bản đời thực tự nhiên, cuốn hút, nghe là mê mẩn!

---
"""

# Now write this enhanced master content into both canonical locations
full_master_doc = new_header + p1_raw[p1_raw.find("## CHƯƠNG 1: TÂM LÝ HỌC THÍNH GIẢ"): ] + cases_p2_and_p3

# Update docs/DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md
target_path1 = 'docs/DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md'
with open(target_path1, 'w', encoding='utf-8') as f:
    f.write(full_master_doc)

print(f"Successfully updated {target_path1} (Total chars: {len(full_master_doc):,})")

# Also update docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md to be identical
target_path2 = 'docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md'
with open(target_path2, 'w', encoding='utf-8') as f:
    f.write(full_master_doc)

print(f"Successfully synchronized {target_path2}!")
