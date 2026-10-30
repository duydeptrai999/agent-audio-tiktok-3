# -*- coding: utf-8 -*-
with open("GEMINI.md", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_line = "- 100% video nền định dạng dọc 1080x1920 (9:16), ưu tiên 4 thể loại triệu view:"
new_line = "- GIỮ NGUYÊN BẢN 100% KHUNG HÌNH GỐC 16:9 (1920x1080) CỦA VIDEO, TUYỆT ĐỐI CẤM KÉO RA 9:16: Ưu tiên 4 thể loại triệu view:"

assert old_line in t_norm, "old_line not found in GEMINI.md"
t_norm = t_norm.replace(old_line, new_line)

final = t_norm.replace("\n", "\r\n")
with open("GEMINI.md", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated GEMINI.md successfully!")

with open(".agents/rules/scriptwriting_standards.md", "r", encoding="utf-8") as f:
    text2 = f.read()

t_norm2 = text2.replace("\r\n", "\n")
if old_line in t_norm2:
    t_norm2 = t_norm2.replace(old_line, new_line)
    final2 = t_norm2.replace("\n", "\r\n")
    with open(".agents/rules/scriptwriting_standards.md", "w", encoding="utf-8") as f:
        f.write(final2)
    print("Updated scriptwriting_standards.md successfully!")
