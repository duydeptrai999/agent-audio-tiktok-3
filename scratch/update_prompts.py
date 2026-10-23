# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/prompts.py")
text = fpath.read_text(encoding="utf-8")

mandatory_gate = """# =============================================================================
# BẮT BUỘC ĐỌC KINH NGHIỆM TRƯỚC KHI BIÊN KỊCH / LÀM AUDIO MỚI (PRE-FLIGHT GATE):
# 1. Agent BẮT BUỘC đối chiếu 100% với GEMINI.md và docs/10_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md
# 2. ÁP DỤNG TRIỆT ĐỂ 5 CÔNG THỨC VÀNG MỞ ĐẦU AUDIO 3 GIÂY (THE 3-SECOND HOOK CODEX):
#    - Dị Thường Thị Giác / Nghịch Lý Hành Động neo vào vật thể có thật trong 15 từ đầu tiên.
#    - CẤM TIỆT 4 Tử Huyệt: Tả thời tiết mưa gió, Thoại gào thét rỗng tuếch, Tóm tắt tiểu sử (7 năm trước), Dẫn chuyện YouTube ('Nếu bạn vô tình...').
# 3. ĐỐI THOẠI NHÁT GỪNG CÓ DAO GĂM: Thoại ngắn dưới 12 từ, có bẫy tâm lý, CẤM thoại dài (> 20 từ) mang tính thuyết giảng.
# 4. MICRO-PACING 25S & MICRO-MOVEMENT: Cứ mỗi 60-75 từ thả 1 biến số mới; sau 2 câu thoại có 1 chuyển động cơ thể.
# 5. ÂM HỌC EDGE-TTS: Câu ngắn 8-16 từ, có dấu ngắt nghỉ lấy hơi, chốt bằng thanh trắc dứt khoát.
# =============================================================================
"""

if "# BẮT BUỘC ĐỌC KINH NGHIỆM TRƯỚC KHI BIEN KICH" not in text and "BẮT BUỘC ĐỌC KINH NGHIỆM TRƯỚC KHI BIÊN KỊCH" not in text:
    text = mandatory_gate + "\n" + text

# Update BOSS_PROMPT
boss_instruction = """
QUY CHUẨN BẮT BUỘC TRƯỚC KHI BIÊN KỊCH (PRE-FLIGHT EXPERIENCE GATE):
- Trước khi duyệt hoặc sản xuất bất kỳ kịch bản nào, BẮT BUỘC phải kiểm tra việc áp dụng đầy đủ 10 NGUYÊN TẮC VÀNG và 5 CÔNG THỨC MỞ ĐẦU 3S trong docs/10_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md.
- Mở đầu 15 từ đầu tiên phải có Dị Thường Thị Giác / Nghịch Lý Hành Động neo vào vật thể cụ thể (bát yến, bật lửa Zippo, mũi kéo inox, thẻ nhớ).
- Thoại nhát gừng dưới 12 từ, cấm thoại dài thuyết giảng bệnh án (> 20 từ).
"""

if "QUY CHUẨN BẮT BUỘC TRƯỚC KHI BIÊN KỊCH" not in text:
    text = text.replace('BOSS_PROMPT = """Bạn là Tổng Giám Đốc Điều Hành', 'BOSS_PROMPT = """' + boss_instruction + '\nBạn là Tổng Giám Đốc Điều Hành')

fpath.write_text(text, encoding="utf-8")
print("Updated core/prompts.py successfully!")
