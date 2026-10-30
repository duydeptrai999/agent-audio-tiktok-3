# -*- coding: utf-8 -*-
from pathlib import Path

gate_file = Path("core/stories/script_quality_gate.py")
text = gate_file.read_text(encoding="utf-8")

old_hook_fn = """def detect_4_hook_archetype(hook_text: str) -> str:
    \"\"\"
    PhAn loi cAu mY ` u theo Ma Tr-n 4 Tr?ng PhAi MY ? u Audio Part 1 Triu View (Master Codex 5.0):
    1. MICRO_SENSORY: ThoAng qua gi-t mAng nhc bng d< th?ng Am thanh, hAnh nh, khcu giAc hoc v-t chcng rn gAy.
    2. HIGH_STAKES_SCENE: C-n cnh hin tr?ng ngAn cAn treo si tA3c, xung `Tt sinh t- (cAng s` tAm, dA1i cui, ch`t s_t, cTt sA3ng `?).
    3. PARADOXICAL_REALITY: By tA mA ngh<ch lA `?i thc (`inh `c phAt wifi h"ng ngoi, mAcp giy bo him d>i bAt yn).
    4. DETAILED_PARADOXICAL: ?o c d< th?ng bt kh thi (l"ng mA"o b?c chA cn X-quang, bAt kim cng 500 t).
    \"\"\"
    t = hook_text.strip().lower()
    
    if any(k in t for k in [\"b?c chA\", \"l\"ng mA\"o\", \"nng bt th?ng\", \"m?i hai cAn\", \"bAt mAy nm\", \"nm trm t\"]):
        return \"DETAILED_PARADOXICAL\"
    if any(k in t for k in [\"`inh `c\", \"h\"ng ngoi\", \"wifi\", \"bo him\", \"bAt yn\", \"camera `in thoi\"]):
        return \"PARADOXICAL_REALITY\"
    if any(k in t for k in [\"cAng s` tAm\", \"dA1i cui\", \"tia l-a\", \"ch`t thAcp\", \"ch`t `in t-\", \"sAng sn\", \"cTt sA3ng `?\"]):
        return \"HIGH_STAKES_SCENE\"
    return \"MICRO_SENSORY\""""

new_hook_fn = """def detect_4_hook_archetype(hook_text: str) -> str:
    \"\"\"
    Phân loại câu mở đầu theo 4 Công Thức Mở Đầu Hook Triệu View Đời Thật (Master Codex 8.0):
    1. ACTION_SHOCK: Hành động dứt khoát gây sốc (Vừa ký đơn ly hôn chuyển khoản 1.2 tỷ; Vừa sinh xong bế con ra khỏi cổng viện...).
    2. SCANDALOUS_QUOTE: Lời nói trơ trẽn / cay đắng của đối phương (Mẹ bạn trai bưng mâm bát đĩa bảo nhà này thử dâu; Em họ bảo nhường chồng...).
    3. RED_HANDED: Bắt quả tang tại trận (Vừa bước vào phòng làm việc lúc 9h tối thấy bạn trai cài trâm; Mở camera thấy mẹ chồng...).
    4. REALISTIC_PARADOX: Nghịch lý đời thường hóm hỉnh (Sếp kêu công ty phá sản giảm nửa lương cho đến khi thấy bảo vệ lái Maybach; Cả công ty giả nghèo...).
    \"\"\"
    t = hook_text.strip().lower()
    if any(k in t for k in [\"ly hôn\", \"chuyển khoản\", \"ký đơn\", \"ra khỏi cổng viện\", \"bế con\", \"vừa xuất viện\", \"đuổi ra khỏi nhà\"]):
        return \"ACTION_SHOCK\"
    if any(k in t for k in [\"thử lòng con dâu\", \"rửa bát\", \"nhường chồng\", \"đẻ con gái\", \"quản tiền\", \"mượn xe\", \"sổ đỏ\", \"ăn bám\"]):
        return \"SCANDALOUS_QUOTE\"
    if any(k in t for k in [\"bắt quả tang\", \"bước vào phòng\", \"cài trâm\", \"trích xuất camera\", \"tin nhắn ẩn\", \"son môi\", \"trong túi áo\"]):
        return \"RED_HANDED\"
    if any(k in t for k in [\"phá sản\", \"giảm lương\", \"giả nghèo\", \"maybach\", \"bảo vệ\", \"rolls-royce\", \"gánh kpi\", \"tiếng lòng\"]):
        return \"REALISTIC_PARADOX\"
    return \"ACTION_SHOCK\""""

# Add new forbidden phrases
new_forbidden_entries = """    "tệp tin lưu trữ bản scan màu công chứng": "giấy tờ pháp lý rõ ràng",
    "bản hợp đồng hôn nhân độc lập tài chính": "thỏa thuận tài sản rõ ràng",
    "nụ cười trên môi lập tức tắt ngấm": "sững người bối rối",
    "sắc mặt sững sờ chuyển từ trắng bệch sang đỏ gay": "mặt biến sắc vì xấu hổ",
    "ăn sóng nói gió quen mồm": "tính bộc trực",
    "lồng mèo bọc chì": "lồng sắt an toàn",
    "đinh ốc phát wifi": "thiết bị định vị bí mật",
"""

text_norm = text.replace("\r\n", "\n")

# Replace hook function
hook_pattern_start = "def detect_4_hook_archetype(hook_text: str) -> str:"
hook_pattern_end = '    return "MICRO_SENSORY"'
idx_start = text_norm.find(hook_pattern_start)
idx_end = text_norm.find(hook_pattern_end)

if idx_start != -1 and idx_end != -1:
    full_end = idx_end + len(hook_pattern_end)
    text_norm = text_norm[:idx_start] + new_hook_fn + text_norm[full_end:]
    print("Replaced detect_4_hook_archetype successfully!")
else:
    print("Could not locate detect_4_hook_archetype function boundary")

# Add forbidden phrases into FORBIDDEN_PHRASES dict
forb_marker = "FORBIDDEN_PHRASES = {"
idx_forb = text_norm.find(forb_marker)
if idx_forb != -1:
    insert_pos = idx_forb + len(forb_marker)
    text_norm = text_norm[:insert_pos] + "\n" + new_forbidden_entries + text_norm[insert_pos:]
    print("Added new forbidden phrases successfully!")

gate_file.write_text(text_norm, encoding="utf-8")
print("Saved updated script_quality_gate.py!")
