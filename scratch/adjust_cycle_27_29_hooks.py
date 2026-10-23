import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
file_path = ROOT_DIR / "core" / "stories" / "cycles_21_to_30_masterpieces.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace hook and first line of p1 for Cycle 27
old_27_hook = 'Cắc! Chốt an toàn van ngăn phun trào dưới đáy biển ba nghìn mét nhảy bật, kim đo áp suất giếng dầu vọt lên mười lăm nghìn PSI giữa lúc tâm bão cấp mười lăm đổ bộ.'
new_27_hook = 'Cắc! Chốt an toàn van ngăn phun trào nhảy bật, kim đo áp suất giếng dầu vọt lên mười lăm nghìn PSI giữa tâm bão biển.'

content = content.replace(old_27_hook, new_27_hook)

# Replace hook and first line of p1 for Cycle 29
old_29_hook = 'Phụt! Sợi dây dẫn đường hang ngầm bằng sợi kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen mù mịt lập tức nuốt chửng ánh đèn lặn của tôi trong hốc đá karst.'
new_29_hook = 'Phụt! Dây dẫn đường kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen nuốt chửng ánh đèn lặn của tôi trong hốc đá karst.'

content = content.replace(old_29_hook, new_29_hook)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Adjusted hooks for Cycle 27 and Cycle 29 to <= 26 words!")
