# -*- coding: utf-8 -*-
"""
scripts/assemble_master_codex8_doc.py
Ghép nối hoàn chỉnh Đại Khảo Sát 100 Audio Triệu View TikTok và Tối Ưu Team Agent (Master Codex 8.0).
Bao gồm:
- Toàn bộ Phần 1: Nguyên lý & Kinh nghiệm khảo sát chuyên sâu
- Toàn bộ Phần 2: ĐỦ 100 Case Study (#001 - #100) phân tích độc nhất không trùng lặp
- Toàn bộ Phần 3 & 4: Hệ thống Subagent Master Codex 8.0 & 17 BGM viral tracks đã tải
- Chương 8: Bảng đối chiếu triệt để văn hóa Zhihu vs Cringe Cải lương
"""
import sys
import os

from cases_data_group1_to_5 import CASES_1_TO_50
from cases_data_group6_to_10 import CASES_51_TO_100

def format_case_markdown(case):
    return f"""### 🎧 Case Study #{case['id']:03d}: **{case['title']}**
- **Kênh phát hành**: `{case['channel']}` | **Thời lượng chuẩn**: `{case['duration']}`
- **Số liệu tương tác thực**: 👁️ **{case['views']}** Views | ❤️ **{case['likes']}** Likes | 💬 **{case['comments']}** Bình luận
- **Thể loại**: `{case['genre']}`
- **🪝 Nguyên Văn Câu Hook 3s - 15s**: *"{case['hook']}"*
- **📖 Tóm Tắt Cốt Truyện 3 Hồi & Nút Thắt**: {case['summary']}
- **🎙️ Thông Số Giọng Đọc Edge-TTS**: {case['voice']}
- **🎵 Nhạc Nền Viral (BGM Track & Ducking)**: {case['bgm']}
- **🎬 Video Nền Thôi Miên Thị Giác (Visual B-roll)**: {case['broll']}
- **🧠 Cơ Chế Giữ Chân & Bẫy Bình Luận (Retention & Comment Magnet)**: {case['retention']}
"""

def generate_part_2():
    groups = [
        ("NHÓM 1: SA ĐIÊU / TIẾNG LÒNG / HÀI CÔNG SỞ (#001 - #010)", CASES_1_TO_50[0:10]),
        ("NHÓM 2: TRỌNG SINH / VẢ MẶT BÁO THÙ (#011 - #020)", CASES_1_TO_50[10:20]),
        ("NHÓM 3: MẸ CHỒNG NÀNG DÂU / GIA ĐẤU ĐỜI THỰC (#021 - #030)", CASES_1_TO_50[20:30]),
        ("NHÓM 4: THẬT GIẢ THIÊN KIM / HOÁN ĐỔI VẬN MỆNH (#031 - #040)", CASES_1_TO_50[30:40]),
        ("NHÓM 5: HÀO MÔN TỔNG TÀI / CƯỚI TRƯỚC YÊU SAU (#041 - #050)", CASES_1_TO_50[40:50]),
        ("NHÓM 6: THANH XUÂN VƯỜN TRƯỜNG / HỌC BÁ OAN GIA (#051 - #060)", CASES_51_TO_100[0:10]),
        ("NHÓM 7: CONFESSION BÓC PHỐT / BẠN THÂN ĐỜI THỰC (#061 - #070)", CASES_51_TO_100[10:20]),
        ("NHÓM 8: TRUE CRIME / KỲ ÁN PHÁP Y / TÂM LÝ TỘI PHẠM (#071 - #080)", CASES_51_TO_100[20:30]),
        ("NHÓM 9: CUNG ĐẤU / NỮ QUYỀN TRẠCH ĐẤU CỔ PHONG (#081 - #090)", CASES_51_TO_100[30:40]),
        ("NHÓM 10: KINH DỊ / QUÁI ĐÀM ĐÊM MUỘN / ĐÔ THỊ DỊ VĂN (#091 - #100)", CASES_51_TO_100[40:50]),
    ]
    
    lines = [
        "## PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM (ĐỦ 100 CASES #001 - #100)\n",
        "> 📊 **DỮ LIỆU ĐẠI KHẢO SÁT THỰC CHIẾN**: Dưới đây là phân tích chi tiết từng trường hợp trong số 100 audio dẫn đầu thị trường TikTok Việt Nam, kèm số liệu lượt xem, lượt tim, nguyên văn câu Hook 3s, cốt truyện 3 hồi, giọng đọc TTS, nhạc nền BGM độc nhất, video nền B-roll và cơ chế giữ chân thính giả.\n\n"
    ]
    
    for g_title, g_cases in groups:
        lines.append(f"\n---\n\n### 📚 {g_title}\n\n")
        for c in g_cases:
            lines.append(format_case_markdown(c))
            lines.append("\n---\n\n")
            
    return "".join(lines)

def main():
    target_path = "docs/DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md"
    artifact_path = r"C:\Users\duydo\.gemini\antigravity\brain\a38926d5-6180-469f-993f-78292957c229\DAI_KHAO_SAT_100_AUDIO_TIKTOK_VA_TOI_UU_TEAM_AGENT.md"
    
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    part2_start_marker = "## PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM"
    part3_start_marker = "## PHẦN 3: HỆ THỐNG 10 SUBAGENT ĐƯỢC TỐI ƯU HÓA HOÀN TOÀN THEO 100 CASE STUDY"
    
    idx1 = content.find(part2_start_marker)
    idx2 = content.find(part3_start_marker)
    
    if idx1 == -1 or idx2 == -1:
        print("Error: Could not find section markers!")
        sys.exit(1)
        
    part1 = content[:idx1]
    part3_original = content[idx2:]
    
    # Nâng cấp Part 3 lên Master Codex 8.0 & cập nhật kho 17 BGM viral
    part3_updated = part3_original.replace("Master Codex 7.0", "Master Codex 8.0")
    
    bgm_inventory_doc = """
### 5. Subagent 5: BGM & Soundscape Specialist (Giám Tuyển Nhạc Nền Triệu View)
- **Nhiệm Vụ Cốt Lõi**:
  - Sở hữu và điều phối kho 17 bài nhạc nền viral triệu view đã được tải về trực tiếp từ TikTok Việt Nam trong thư mục `TikTok_BGM_Audio/` và `assets/bgm/`:
    1. `01 - Senorita (Instrumental)`: Sa điêu, hài hước, vả mặt công sở.
    2. `02 - Attention (Instrumental Lofi)`: Cười thầm, mỏ hỗn, bóc mẽ nhẹ nhàng.
    3. `03 - Cheating on You (Instrumental Lofi)`: Châm biếm tiểu tam, trà xanh.
    4. `04 - Say Em (Instrumental Lofi)`: Đời thực, đối đáp thanh mai trúc mã.
    5. `05 - See Tinh (Acoustic Instrumental)`: Hóm hỉnh, oan gia ngõ hẹp.
    6. `06 - Di Vang Cuoc Tinh (Lofi Instrumental)`: Confession người yêu cũ, hoài niệm.
    7. `07 - Windy Hill (Instrumental)`: Thanh xuân vườn trường, trong sáng.
    8. `08 - Waiting For Love (Acoustic)`: Chữa lành, vượt khó vươn lên.
    9. `09 - Muon Roi Ma Sao Con (Acoustic Lofi)`: Gen Z công sở, độc thoại hài hước.
    10. `10 - Nham Mat Thay Mua He (Instrumental Acoustic)`: Mẹ chồng nàng dâu thấu cảm, gia đình.
    11. `11 - Canh Ba (Instrumental Folk Lofi)`: Cung đấu, trạch đấu cổ phong.
    12. `12 - The Truth That You Leave - Pianoboy`: Trọng sinh, vả mặt hả hê, cao trào cảm xúc.
    13. `13 - Thanh Nam Hoa Da No - Piano`: Tâm lý sâu sắc, tình thân gia đình, chữa lành.
    14. `14 - Snowfall - Oneheart Ambient`: True crime, kỳ án, kinh dị rùng rợn, bí ẩn không gian kín.
    15. `15 - Cau Xem Troi Toi Roi - Piano`: Nghẹt thở, đấu trí hình sự, vạch trần tội ác.
    16. `16 - Thoi Khong Sai Lech - Piano`: Ly hôn dứt khoát, nữ cường quật khởi, trùng sinh.
    17. `17 - Secret - Jay Chou Piano`: Hào môn thế gia, thanh xuân lãng mạn, ngọt ngào sâu lắng.
- **Tiêu Chuẩn Âm Học**: Cố định âm lượng nhạc nền ở ngưỡng **-22dB đến -24dB** (nhỏ hơn giọng đọc tối thiểu 18dB), sử dụng filter highpass/lowpass nhẹ để giọng đọc luôn nổi bật trên nền nhạc.
"""
    
    # Tìm đoạn Subagent 5 trong part3 và cập nhật
    sub5_marker = "### 5. Subagent 5: BGM & Soundscape Specialist"
    sub6_marker = "### 6. Subagent 6: Visual & B-roll Curator"
    
    idx_sub5 = part3_updated.find(sub5_marker)
    idx_sub6 = part3_updated.find(sub6_marker)
    
    if idx_sub5 != -1 and idx_sub6 != -1:
        part3_updated = part3_updated[:idx_sub5] + bgm_inventory_doc.strip() + "\n\n" + part3_updated[idx_sub6:]

    part2_new = generate_part_2()
    
    full_new_content = part1 + part2_new + part3_updated
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_new_content)
    print(f"Successfully assembled {target_path} (length: {len(full_new_content)} chars)")
    
    # Cập nhật cả file artifact nếu tồn tại thư mục
    try:
        os.makedirs(os.path.dirname(artifact_path), exist_ok=True)
        with open(artifact_path, "w", encoding="utf-8") as f:
            f.write(full_new_content)
        print(f"Successfully updated artifact {artifact_path}")
    except Exception as e:
        print(f"Artifact write error: {e}")

if __name__ == "__main__":
    main()
