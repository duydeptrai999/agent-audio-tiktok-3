# -*- coding: utf-8 -*-
"""
scratch/build_unified_experience_codex.py
Hợp nhất toàn bộ:
1. Đại Kinh Nghiệm Vàng (7 Chương Thực Chiến Đỉnh Cao)
2. Kho Báu Đủ 100 Case Study Audio Triệu View Thực Tế tại Việt Nam (#001 - #100)
3. Cẩm Nang Tối Ưu Hóa 10 Subagent (Master Codex 7.0)
4. Checklist Vàng Kiểm Định 10/10 Trước Khi Xuất Bản
Thành 1 SIÊU FILE DUY NHẤT: docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Đọc các file nguồn
cases_doc = Path("docs/DOCS_100_AUDIO_TIKTOK_TRIEU_VIEW_THUC_CHIEN.md").read_text(encoding="utf-8")
kinh_nghiem_doc = Path("docs/DAI_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md").read_text(encoding="utf-8")
agent_doc = Path("docs/CAM_NANG_TOI_UU_TEAM_AGENT_MASTER_CODEX_7.md").read_text(encoding="utf-8") if Path("docs/CAM_NANG_TOI_UU_TEAM_AGENT_MASTER_CODEX_7.md").exists() else ""

master_content = []
master_content.append("# 📘 TỔNG TẬP ĐẠI KINH NGHIỆM SẢN XUẤT AUDIO DRAMA TIKTOK TRIỆU VIEW (MASTER CODEX 7.0)")
master_content.append("*Siêu tài liệu cẩm nang độc bản: Đúc kết toàn diện từ Đại khảo sát 100 Audio Triệu View Dẫn Đầu TikTok Việt Nam & Hệ thống tối ưu hóa 10 Subagent.*")
master_content.append("\n---\n")

master_content.append("## 🌟 MỤC LỤC TỔNG QUAN")
master_content.append("1. **LỜI CẢNH TỈNH XƯƠNG MÁU**: Nguồn gốc bệnh kịch bản AI không thẩm được và bản án xóa bỏ vĩnh viễn.")
master_content.append("2. **PHẦN 1: CẨM NANG ĐẠI KINH NGHIỆM VÀNG (7 CHƯƠNG THỰC CHIẾN ĐỈNH CAO)**")
master_content.append("   - Chương 1: Bản Đồ Tâm Lý Thính Giả TikTok VN (Thói quen nghe 30 phút, 4 khao khát cảm xúc).")
master_content.append("   - Chương 2: Nghệ Thuật Biên Kịch Đời Thường & Tiêu Diệt Bệnh Cơ Khí Dị Hợm (100% logic đời sống, công cụ pháp lý).")
master_content.append("   - Chương 3: 6 Công Thức Mở Đầu 3 Giây - 15 Giây Thôi Miên (The 3s Hook Mastery).")
master_content.append("   - Chương 4: Nhịp Điệu Micro-Pacing & Kỹ Thuật Giữ Chân Khán Giả (Action-Apex Cliffhanger).")
master_content.append("   - Chương 5: Đạo Diễn Âm Thanh Edge-TTS & BGM Sidechain Ducking -22dB (Giọng Hoài My / Nam Minh).")
master_content.append("   - Chương 6: Giám Tuyển Thị Giác Video Nền ASMR Thôi Miên (B-roll dọc 9:16, Clean Screen).")
master_content.append("   - Chương 7: Nghệ Thuật Tạo 'Nam Châm Bình Luận' (Comment Magnets) & Thúc Đẩy Thuật Toán TikTok.")
master_content.append("3. **PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM (ĐỦ 100 CASES #001 - #100)**")
master_content.append("   - Nhóm 1: Sa Điêu / Tiếng Lòng / Hài Hước Công Sở (Case #001 - #010)")
master_content.append("   - Nhóm 2: Trọng Sinh / Vả Mặt Báo Thù / Ác Nữ Thức Tỉnh (Case #011 - #020)")
master_content.append("   - Nhóm 3: Mẹ Chồng Nàng Dâu / Gia Đấu Đời Thực / Ly Hôn Chia Tài Sản (Case #021 - #030)")
master_content.append("   - Nhóm 4: Thật Giả Thiên Kim / Hoán Đổi Số Phận / Hắt Hủi Con Ruột (Case #031 - #040)")
master_content.append("   - Nhóm 5: Hào Môn Tổng Tài / Cưới Trước Yêu Sau / Cá Mặn Gả Trùm Hắc Bang (Case #041 - #050)")
master_content.append("   - Nhóm 6: Thanh Xuân Vườn Trường / Học Bá Oan Gia / Đại Ca Bảo Kê (Case #051 - #060)")
master_content.append("   - Nhóm 7: Confession Bóc Phốt / Bạn Thân Cướp Bồ / Trả Giá Đời Thực (Case #061 - #070)")
master_content.append("   - Nhóm 8: True Crime / Kỳ Án Pháp Y / Tâm Lý Tội Phạm (Case #071 - #080)")
master_content.append("   - Nhóm 9: Cung Đấu / Trạch Đấu Nữ Quyền / Dưỡng Lão Lãnh Cung (Case #081 - #090)")
master_content.append("   - Nhóm 10: Kinh Dị Đô Thị / Quy Tắc Quái Đàm / Tiếng Khóc Đêm Muộn (Case #091 - #100)")
master_content.append("4. **PHẦN 3: HỆ THỐNG 10 SUBAGENT ĐƯỢC TỐI ƯU HÓA HOÀN TOÀN THEO 100 CASE STUDY**")
master_content.append("5. **PHẦN 4: BẢNG CHECKLIST VÀNG KIỂM ĐỊNH CHẤT LƯỢNG TRƯỚC KHI XUẤT BẢN**")
master_content.append("\n---\n")

# Lấy Phần 1 từ kinh_nghiem_doc (cắt bỏ phần tiêu đề cũ nếu có)
idx_kn_start = kinh_nghiem_doc.find("## LỜI NÓI ĐẦU:")
if idx_kn_start != -1:
    master_content.append(kinh_nghiem_doc[idx_kn_start:].strip())
else:
    master_content.append(kinh_nghiem_doc.strip())

master_content.append("\n\n---\n\n")

# Lấy Phần 2: Toàn bộ 100 Cases từ cases_doc
master_content.append("## PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM (ĐỦ 100 CASES #001 - #100)\n")
master_content.append("> 📊 **DỮ LIỆU ĐẠI KHẢO SÁT THỰC CHIẾN**: Dưới đây là phân tích chi tiết từng trường hợp trong số 100 audio dẫn đầu thị trường TikTok Việt Nam, kèm số liệu lượt xem, lượt tim, nguyên văn câu Hook 3s, cốt truyện, giọng đọc TTS, nhạc nền BGM, video nền B-roll và cơ chế giữ chân thính giả.\n")

idx_c1 = cases_doc.find("### 🎧 Case Study #001:")
idx_end = cases_doc.find("## PHẦN 2: BÓC TÁCH ĐA CHIỀU", idx_c1)
if idx_end == -1:
    idx_end = len(cases_doc)

cases_body = cases_doc[idx_c1:idx_end].strip()
master_content.append(cases_body)
master_content.append("\n\n---\n\n")

# Lấy Phần 3: Tối ưu team agent
master_content.append("## PHẦN 3: HỆ THỐNG 10 SUBAGENT ĐƯỢC TỐI ƯU HÓA HOÀN TOÀN THEO 100 CASE STUDY\n")
if agent_doc:
    idx_agent_body = agent_doc.find("## 1. MỤC TIÊU VÀ BẢN NÂNG CẤP")
    if idx_agent_body != -1:
        master_content.append(agent_doc[idx_agent_body:].strip())
    else:
        master_content.append(agent_doc.strip())
master_content.append("\n\n---\n\n")

# Lấy Phần 4: Checklist
checklist = """## PHẦN 4: CHECKLIST VÀNG KIỂM ĐỊNH KỊCH BẢN & AUDIO (BẮT BUỘC 10/10)

Trước khi bất kỳ kịch bản nào được chuyển sang khâu Text-To-Speech (Edge-TTS) và Render Video để đăng tải lên kênh TikTok, toàn bộ 10 câu hỏi sau đây phải được trả lời **ĐẠT (YES)** 100%:

| STT | Tiêu chí kiểm định sống còn | Yêu cầu bắt buộc | Kết quả |
| :---: | :--- | :--- | :---: |
| 1 | **Thời lượng chuẩn 30 phút điện ảnh** | Mỗi tập tối thiểu 1.400 - 2.200 từ; Cả bộ 3 tập tối thiểu 4.500 - 6.500 từ (nghe thực tế 25 - 35 phút). | [ ] ĐẠT |
| 2 | **Loại bỏ 100% cơ khí dị hợm & báo cáo kỹ thuật** | Tuyệt đối không có sóng hạ âm 18Hz, FFT, lồng mèo bọc chì, áp lực âm, blockchain trong drama gia đình/tình cảm. | [ ] ĐẠT |
| 3 | **Hook 3 giây - 15 giây giật màng nhĩ** | 15 từ đầu tiên phải ném người nghe vào mâu thuẫn sống còn hoặc nghịch lý đời thực. | [ ] ĐẠT |
| 4 | **Logic đời thực & đạo cụ pháp lý** | Mọi giải pháp tài chính/pháp lý phải có căn cứ: Sổ đỏ, sao kê, camera, biên bản công an, xét nghiệm ADN. | [ ] ĐẠT |
| 5 | **Không nhồi dấu câu phá nhịp đọc** | Không spam '...' hay '!' sau mỗi 5 từ. Câu văn mượt mà (15 - 25 từ/câu) để Edge-TTS ngắt nghỉ tự nhiên. | [ ] ĐẠT |
| 6 | **Giọng đọc Edge-TTS phân bổ chuẩn** | Hoài My (rate +5% đến +8%) cho drama/sa điêu/gia đấu; Nam Minh cho trinh thám/kỳ án/kinh dị. | [ ] ĐẠT |
| 7 | **BGM Sidechain Ducking -22dB** | Nhạc nền lùi sâu dưới giọng đọc ít nhất 18dB, không át tiếng, không có hiệu ứng chói tai. | [ ] ĐẠT |
| 8 | **Video nền ASMR 9:16 thôi miên thị giác** | 100% video dọc 1080x1920: Làm bánh/nấu ăn, mỹ nghệ thủ công, mưa rơi lofi hoặc dọn dẹp tối giản. | [ ] ĐẠT |
| 9 | **Clean Screen & Không che chắn an toàn** | Không dùng chữ phụ đề to đè video; chừa không gian an toàn (Safe Zone) cho TikTok Auto CC và nút thả tim. | [ ] ĐẠT |
| 10 | **Cổng Thẩm Mỹ Tai Nghe Người Thật (Human Ear Gate)** | Đọc to kịch bản bằng miệng hoặc nghe file audio mẫu: Không sượng trân, không ngượng mồm, nghe đã cái nết. | [ ] ĐẠT |
"""
master_content.append(checklist)

final_text = "\n".join(master_content)

# Ghi ra file docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md
target_path = Path("docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md")
target_path.write_text(final_text, encoding="utf-8")

# Cập nhật đồng bộ vào docs/DAI_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md
Path("docs/DAI_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md").write_text(final_text, encoding="utf-8")

print(f"XONG! Đã tạo thành công file: {target_path}")
print(f"Kích thước: {len(final_text)} ký tự | {len(final_text.splitlines())} dòng | {len(final_text.split())} từ")
