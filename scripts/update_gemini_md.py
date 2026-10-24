# -*- coding: utf-8 -*-
"""
scripts/update_gemini_md.py
Nâng cấp GEMINI.md lên MASTER SCRIPTWRITING CODEX 6.0
"""
from pathlib import Path

gemini_path = Path("GEMINI.md")
content = gemini_path.read_text(encoding="utf-8")

old_mark = "## 1. NGUYÊN TẮC VÀNG VỀ SÁNG TÁC KỊCH BẢN (MASTER SCRIPTWRITING CODEX 5.0 - 50 VÒNG THỰC CHIẾN)"

new_section = """## 0. QUY TẮC THỜI LƯỢNG SỐNG CÒN: CHUẨN 30 PHÚT ĐIỆN ẢNH (ZERO 49S TOLERANCE)

> 🚨 **CẢNH BÁO TỐI CAO TỪ NGHIÊN CỨU 100 AUDIO TRIỆU VIEW THỰC TẾ**:
> 100% video truyện viral triệu view tại Việt Nam (Dứa Audio, Túi Mù Audio, Tâm Hồn Ăn Uống, Truyện Audio TTH...) đều có thời lượng từ **25 đến 55 phút** (khi chia 3 tập tương đương **8 - 12 phút / tập**).
> Khán giả nghe audio TikTok trong lúc làm việc nhà, nấu ăn, đi xe hoặc đi ngủ; họ cần một hành trình cảm xúc trọn vẹn, sâu sắc và nghẹt thở. Các video 40 - 50 giây bị người nghe tẩy chay vì hời hợt, làm hỏng tỷ lệ giữ chân và vi phạm chính sách video dài (TikTok Long-Form Program)!

1. **Độ Dài Kịch Bản Bắt Buộc**:
   - **Mỗi tập (Part 1, Part 2, Part 3)**: TỐI THIỂU **1.400 từ đến 2.500 từ** (thời lượng đọc thực tế **8 đến 12 phút / tập**).
   - **Tổng cả 3 tập**: TỐI THIỂU **4.500 từ đến 7.500 từ** (tổng thời lượng **25 đến 35 phút** cho trọn bộ).
   - **LỆNH CẤM TUYỆT ĐỐI**: Bất kỳ kịch bản nào dưới 1.200 từ/tập hoặc tổng dưới 3.600 từ ĐỀU BỊ COI LÀ LỖI KỸ THUẬT NGHIÊM TRỌNG và bị `script_quality_gate.py` tự động từ chối xuất bản ngay lập tức!
2. **Tốc Độ Đọc Edge-TTS Chuẩn**:
   - Tốc độ đọc: **rate="+5%" đến "+10%"** (tương đương 160 - 180 từ / phút).
   - TUYỆT ĐỐI CẤM tăng tốc độ lên 1.5x (rate="+50%"). Giọng đọc phải có độ ấm, nhịp thở, độ lắng và tự nhiên như người thật.
3. **Âm Lượng Nhạc Nền (BGM Ducking)**:
   - Cố định ở ngưỡng **-22dB đến -24dB** (nhỏ hơn giọng đọc ít nhất 18dB), không át tiếng, không có hiệu ứng giật mình.
4. **Hình Ảnh Nền (B-roll Thôi Miên Thị Giác)**:
   - 100% video nền định dạng dọc 1080x1920 (9:16), ưu tiên 4 thể loại triệu view: ASMR làm bánh & nấu ăn, điêu khắc mỹ nghệ thủ công, mưa rơi quán cà phê lofi, hoạt hình 2D vòng lặp.

---

## 1. NGUYÊN TẮC VÀNG VỀ SÁNG TÁC KỊCH BẢN (MASTER SCRIPTWRITING CODEX 6.0)"""

if old_mark in content:
    content = content.replace(old_mark, new_section)
    gemini_path.write_text(content, encoding="utf-8")
    print("✅ ĐÃ NÂNG CẤP GEMINI.MD LÊN MASTER CODEX 6.0 THÀNH CÔNG!")
else:
    print("⚠️ Không tìm thấy vị trí đánh dấu cũ, kiểm tra lại nội dung.")
