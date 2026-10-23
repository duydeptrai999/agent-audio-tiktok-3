import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# 1. Cycle 15 in core/stories/cycles_11_to_20_masterpieces.py
f1 = ROOT_DIR / "core" / "stories" / "cycles_11_to_20_masterpieces.py"
with open(f1, "r", encoding="utf-8") as f:
    c1 = f.read()
c1 = c1.replace("Ủy ban Chứng khoán Nhà nước", "Ủy ban Giám sát Giao dịch Chứng khoán")
with open(f1, "w", encoding="utf-8") as f:
    f.write(c1)
print("Fixed Cycle 15")

# 2. Cycle 22 in core/stories/cycles_21_to_30_masterpieces.py
f2 = ROOT_DIR / "core" / "stories" / "cycles_21_to_30_masterpieces.py"
with open(f2, "r", encoding="utf-8") as f:
    c2 = f.read()
c2 = c2.replace("trúng gói thầu nghìn tỷ của chính phủ", "trúng gói thầu phát triển hạ tầng cảng biển nghìn tỷ")
with open(f2, "w", encoding="utf-8") as f:
    f.write(c2)
print("Fixed Cycle 22")

# 3. Cycle 31 and 36 in core/stories/cycles_31_to_40_masterpieces.py
f3 = ROOT_DIR / "core" / "stories" / "cycles_31_to_40_masterpieces.py"
with open(f3, "r", encoding="utf-8") as f:
    c3 = f.read()

# Fix Cycle 31
c3 = c3.replace("gạt công tắc kính lúp sang chế độ phân cực", "gạt công tắc kính lúp sang lăng kính phân cực")

# Fix Cycle 36
c3 = c3.replace("căn phòng họp lãnh sự quán", "căn phòng họp hội đồng cứu trợ quốc tế")
c3 = c3.replace("phòng họp lãnh sự quán", "phòng họp hội đồng cứu trợ quốc tế")
c3 = c3.replace("Phó tùy viên Triệu Bân", "Phó ban tài chính Triệu Bân")
c3 = c3.replace("hội đồng ngoại giao", "hội đồng cứu trợ")
c3 = c3.replace("ngân khố quốc gia", "quỹ ký thác bảo trợ")
c3 = c3.replace("phản quốc và tống tiền quốc tế", "cấu kết bắt cóc tống tiền và gian lận tài chính")
c3 = c3.replace("Bộ trưởng Ngoại giao bước vào phòng họp, cài huân chương chiến công lên ngực áo tôi:", "Chủ tịch Hội đồng Cứu trợ bước vào phòng họp, bắt chặt tay tôi xúc động:")
c3 = c3.replace("bảo vệ danh dự quốc gia!", "bảo vệ trọn vẹn quỹ cứu trợ nhân đạo!")
c3 = c3.replace("Lực lượng đặc nhiệm", "Đội an ninh bảo hộ chuyên nghiệp")
c3 = c3.replace("đặc nhiệm cải trang", "nhân viên bảo an cải trang")
c3 = c3.replace("Lực lượng đặc nhiệm chống khủng bố", "Đội an ninh bảo hộ chuyên nghiệp")

with open(f3, "w", encoding="utf-8") as f:
    f.write(c3)
print("Fixed Cycle 31 and Cycle 36")
