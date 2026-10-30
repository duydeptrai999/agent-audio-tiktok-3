import re

path = 'core/stories/script_quality_gate.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

cringe_dict_str = '''    # --- BỘ TỪ KHÓA CHỐNG CRINGE & HOẠT HÌNH HÓA (CODEX 8.0) ---
    "ba cái cổ gà": "vài cọng rau héo úa",
    "bốn nhân viên lực lưỡng": "đại diện pháp lý",
    "công ty vệ sĩ chuyên nghiệp": "văn phòng công chứng",
    "vệ sĩ chuyên nghiệp": "nhân viên an ninh tòa nhà",
    "bố tôi - cựu thẩm phán": "luật sư của tôi",
    "bố tôi cựu thẩm phán": "luật sư của tôi",
    "bàn tay to bè giáng xuống trong gang tấc": "bước tới với vẻ mặt khó coi",
    "bàn tay to bè": "bàn tay",
    "chế độ quay video góc rộng bốn ca": "chế độ ghi âm",
    "quay video góc rộng bốn ca": "ghi âm cuộc gọi",
    "lại là vịt trời, tốn tiền viện phí": "con gái thì có gì đáng mừng đâu",
    "quân giết người, quân vô phúc": "sao cô dám làm thế",
    "quân giết người": "đồ vô ơn",
    "thập tử nhất sinh": "mệt mỏi sau ca sinh",
    "vết khâu tầng sinh môn rát bỏng": "cơn đau nhức sau sinh",
    "bản khế ước nợ năm tỷ": "giấy nợ tài chính",
'''

target = '"từng con số kiểm toán sắc lẹm như những nhát búa": "từng con số kiểm toán đối chiếu",'
if target in content:
    replacement = target + "\n" + cringe_dict_str
    new_content = content.replace(target, replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched script_quality_gate.py!")
else:
    print("Target not found directly, checking regex...")
