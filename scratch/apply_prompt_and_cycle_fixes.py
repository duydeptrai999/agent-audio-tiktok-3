# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# 1. Update core/prompts.py
prompts_file = ROOT_DIR / "core" / "prompts.py"
content = prompts_file.read_text(encoding="utf-8")

# Ensure BOSS_PROMPT has "80% Nữ giới" and "ASMR Trung Quốc" and "Clean Screen"
content = content.replace(
    "giữ chân thính giả trên 120s-180s:",
    "đánh trúng thị hiếu 80% Nữ giới trẻ, giữ chân thính giả trên 120s-180s:"
)
content = content.replace(
    "Visual B-Roll ASMR thư giãn mãn nhãn,",
    "Visual B-Roll ASMR Trung Quốc thư giãn mãn nhãn,"
)

# Ensure TREND_HUNTER_PROMPT has Liễu Như Yên, Bạch Ngưng Băng, Cố Bắc Thần, Thẩm Tri Ý
trend_target = """   - Luân chuyển 10 Vũ trụ nhân vật (Kiểm toán, Vi phẫu thần kinh, Boong ke băng hà, Olympic học đường, Cổ vật...)."""
trend_replacement = """   - Luân chuyển 10 Vũ trụ nhân vật (Kiểm toán, Vi phẫu thần kinh, Boong ke băng hà, Olympic học đường, Cổ vật...).
   - Tận dụng mỏ neo meme viral có kiểm soát: Liễu Như Yên (trà xanh), Bạch Ngưng Băng (bạch nguyệt quang), Cố Bắc Thần (tổng tài bá đạo), Thẩm Tri Ý (nữ cường tài chính)."""
content = content.replace(trend_target, trend_replacement)
prompts_file.write_text(content, encoding="utf-8")
print("1. Updated core/prompts.py")

# 2. Fix core/stories/cycles_21_to_30_masterpieces.py line 103
c21_file = ROOT_DIR / "core" / "stories" / "cycles_21_to_30_masterpieces.py"
c21_content = c21_file.read_text(encoding="utf-8")
old_clause = "Bản án tuyên hủy toàn bộ giao dịch dân sự mua căn hộ áp mái năm mươi tỷ do có hành vi tẩu tán tài sản hôn nhân bất hợp pháp."
new_clause = "Bản án tuyên hủy toàn bộ giao dịch dân sự, phong tỏa căn hộ áp mái năm mươi tỷ, do có hành vi tẩu tán tài sản hôn nhân bất hợp pháp."
if old_clause in c21_content:
    c21_content = c21_content.replace(old_clause, new_clause)
    c21_file.write_text(c21_content, encoding="utf-8")
    print("2. Fixed Cycle 21 Part 3 clause in core/stories/cycles_21_to_30_masterpieces.py")
else:
    print("Warning: old_clause not found in c21")

# 3. Fix core/stories/cycles_31_to_40_masterpieces.py Cycle 35 Part 1
c35_file = ROOT_DIR / "core" / "stories" / "cycles_31_to_40_masterpieces.py"
c35_content = c35_file.read_text(encoding="utf-8")
old_p1 = """    p1 = \"\"\"Tiếng lòng của tôi vừa vang lên chê chiếc giọng hát nốt cao giả tạo, ca sĩ thần tượng bỗng đánh rơi micro xuống sàn.

Màn hình máy phân tích dải tần sóng âm Spectrum Analyzer trước mặt tôi hiển thị một đường thẳng băng không gợn sóng.
File âm thanh thu sẵn ba mươi hai bit đang chạy ngầm trên máy tính phát nhạc nền với âm lượng tối đa.

Ca sĩ thần tượng Lục Phi vội vàng nhặt micro bọc vàng lên, mặt đỏ bừng gượng cười trước năm nghìn khán giả:
Tôi thầm nghĩ trong đầu: 'Hát nốt Đô năm mà thanh quản không rung, chiếc răng khểnh bọc sứ sắp rớt ra kìa!'.

Lục Phi giật mình lấy tay che miệng, ánh mắt hoảng hốt nhìn quanh buồng điều khiển âm thanh tầng hai.
Nhà sản xuất Lâm Chấn bước vào, tay cầm bản hợp đồng tài trợ hai mươi tỷ dí sát vào mặt tôi:
'Diệp Khả Vi... Cứ để đĩa than chạy tiếp, đừng phá đám kiếm tiền!'.

Tôi ngước nhìn Lâm Chấn, ngón tay trỏ đặt hờ trên cần gạt âm lượng tổng của bàn mixer ba mươi hai kênh!\"\"\""""

new_p1 = """    p1 = \"\"\"Tiếng lòng của tôi vừa vang lên chê chiếc giọng hát nốt cao giả tạo. Ca sĩ thần tượng bỗng đánh rơi micro xuống sàn.

Màn hình máy phân tích dải tần sóng âm Spectrum Analyzer trước mặt tôi hiển thị một đường thẳng băng không gợn sóng.
File âm thanh thu sẵn ba mươi hai bit đang chạy ngầm trên máy tính phát nhạc nền với âm lượng tối đa.

Ca sĩ thần tượng Lục Phi vội vàng nhặt micro bọc vàng lên. Mặt hắn đỏ bừng gượng cười trước năm nghìn khán giả.
Tôi thầm nghĩ trong đầu: 'Hát nốt Đô năm mà thanh quản không rung, chiếc răng khểnh bọc sứ sắp rớt ra kìa!'.

Lục Phi giật mình lấy tay che miệng. Ánh mắt hắn hoảng hốt nhìn quanh buồng điều khiển âm thanh tầng hai.
Nhà sản xuất Lâm Chấn bước vào phòng máy. Hắn cầm bản hợp đồng tài trợ hai mươi tỷ dí sát vào mặt tôi:
'Diệp Khả Vi... Cứ để đĩa than chạy tiếp, đừng phá đám kiếm tiền!'.

Tôi ngước nhìn Lâm Chấn. Ngón tay trỏ của tôi đặt hờ trên cần gạt âm lượng tổng của bàn mixer ba mươi hai kênh!\"\"\""""

if old_p1 in c35_content:
    c35_content = c35_content.replace(old_p1, new_p1)
    c35_file.write_text(c35_content, encoding="utf-8")
    print("3. Fixed Cycle 35 Part 1 in core/stories/cycles_31_to_40_masterpieces.py")
else:
    print("Warning: old_p1 not found in c35")
