import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
file_path = ROOT_DIR / "core" / "stories" / "cycles_21_to_30_masterpieces.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_hook = "Phụt! Dây dẫn đường kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen nuốt chửng ánh đèn lặn của tôi trong hốc đá karst."
new_hook = "Phụt! Dây dẫn đường kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen nuốt chửng ánh đèn lặn trong hốc đá karst."

content = content.replace(old_hook, new_hook)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Cycle 29 hook updated to 25 words!")
