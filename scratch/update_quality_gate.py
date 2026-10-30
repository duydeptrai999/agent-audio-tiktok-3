# -*- coding: utf-8 -*-
with open('core/stories/script_quality_gate.py', 'r', encoding='utf-8') as f:
    text = f.read()

new_phrases = '''
    "vệ sĩ bọc thép": "nhân viên an ninh",
    "búa tạ mười cân": "sự thật phơi bày",
    "gào khóc như lợn bị chọc tiết": "gào khóc thảm thiết",
    "bò lê lết ôm mũi giày": "quỳ sụp xuống nhận lỗi",
    "đồng tử co rút kịch liệt": "bàng hoàng kinh ngạc",
    "bút máy nạm kim cương": "chiếc bút ký",
    "khuôn mặt méo mó nanh ác": "khuôn mặt đầy toan tính",
    "năm chiếc rolls-royce": "đoàn xe ô tô",
'''

target = '"bản khế ước nợ năm tỷ": "giấy nợ tài chính",'
if target in text:
    text = text.replace(target, target + new_phrases)
    with open('core/stories/script_quality_gate.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added new anti-cringe phrases to script_quality_gate.py successfully!")
else:
    print("Target not found!")
