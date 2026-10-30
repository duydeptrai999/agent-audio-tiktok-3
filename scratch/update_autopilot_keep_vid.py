# -*- coding: utf-8 -*-
with open("scripts/daily_24h_master_autopilot.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_reuse_check = '''        if part_video.exists() and part_video.stat().st_size > 500000:
            v_probe = probe_media_file(part_video)
            # Chỉ tái sử dụng nếu video đã đúng chuẩn dọc 9:16 (1080x1920)
            if v_probe.get("height", 0) >= v_probe.get("width", 1):
                print(f"  ⏭️ Tập {p_num} đã có sẵn video dọc 9:16 thành phẩm, bỏ qua render.")
                continue'''

new_reuse_check = '''        if part_video.exists() and part_video.stat().st_size > 500000:
            print(f"  ⏭️ Tập {p_num} đã có sẵn video thành phẩm (giữ nguyên khung hình gốc), bỏ qua render.")
            continue'''

old_render_msg = 'print(f"  🎥 Đang render video dọc 9:16 (1080x1920) cho Tập {p_num}...")'
new_render_msg = 'print(f"  🎥 Đang render video giữ nguyên khung hình gốc cho Tập {p_num}...")'

assert old_reuse_check in t_norm, "old_reuse_check not found"
assert old_render_msg in t_norm, "old_render_msg not found"

t_norm = t_norm.replace(old_reuse_check, new_reuse_check)
t_norm = t_norm.replace(old_render_msg, new_render_msg)

final = t_norm.replace("\n", "\r\n")

with open("scripts/daily_24h_master_autopilot.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated daily_24h_master_autopilot.py successfully!")
