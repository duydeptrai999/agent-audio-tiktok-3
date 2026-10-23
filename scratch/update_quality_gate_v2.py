# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/stories/script_quality_gate.py")
content = fpath.read_text(encoding="utf-8")

# Thêm các từ cấm mới vào FORBIDDEN_PHRASES
new_entries = """    "chết lặng như bị bàng hoàng": "chết lặng",
    "mình... mình chưa chết": "tôi bàng hoàng mở mắt",
    "mình đã thực sự trọng sinh": "tôi nhìn đồng hồ đếm ngược",
    "lũ súc sinh vô ơn": "những kẻ phản trắc",
    "nhâm nhi ly trà sữa": "nhìn qua camera",
    "nụ cười sắc lạnh thấu xương": "nụ cười toan tính",
    "thẩm băng tuyết thong thả nhấp ngụm rượu vang": "ngón tay lật giở trang hồ sơ",
    "trong ván cờ sinh tử của giới tài phiệt": "trên bàn đàm phán",
    "giá trị đích thực của một con người": "kết quả kinh doanh",
    "mười năm sống trong bùn lầy kiếp trước": "những năm tháng gian khó",
    "từng con số kiểm toán sắc lẹm như những nhát búa": "từng con số kiểm toán đối chiếu","""

if '"chết lặng như bị bàng hoàng": "chết lặng",' in content:
    content = content.replace('"chết lặng như bị bàng hoàng": "chết lặng",', new_entries)

# Thêm các pattern mở đầu cấm kỵ mới
new_cliches = """    r"^['\\\"“][^'\\\"”]+['\\\"”]\s*-\s*Tiếng\s+(hét|thét|xé|gầm|đập|rên)",
    r"^Bảy\s+năm\s+(sau|trước)",
    r"^Mười\s+năm\s+(sau|trước)",
    r"^Mình\.\.\.\s*mình\s+(chưa\s+chết|trọng\s+sinh)",
    r"^Tại\s+đám\s+tang\s+của\s+người\s+chồng",
    r"^Trước\s+khi\s+phiên\s+họp","""

target_line = '    r"^[\'\\"“][^\'\\"”]+[\'\\"”]\s*-\s*Tiếng\s+xé",'
if target_line in content:
    content = content.replace(target_line, target_line + "\n" + new_cliches)

fpath.write_text(content, encoding="utf-8")
print("Update script_quality_gate completed successfully!")
