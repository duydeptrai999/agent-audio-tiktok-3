# -*- coding: utf-8 -*-
with open("scripts/daily_24h_master_autopilot.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_chk = """        if part_video.exists() and part_video.stat().st_size > 500000:
            print(f"  ⏭️ Tập {p_num} đã có sẵn video thành phẩm (giữ nguyên khung hình gốc), bỏ qua render.")
            continue"""

new_chk = """        if part_video.exists() and part_video.stat().st_size > 500000:
            v_probe = probe_media_file(part_video)
            if v_probe.get("height", 0) > v_probe.get("width", 0):
                print(f"  ⚠️ Video Tập {p_num} đang bị dính dọc (9:16) lỗi! Tự động xóa để render lại chuẩn 16:9...")
                part_video.unlink(missing_ok=True)
            else:
                print(f"  ⏭️ Tập {p_num} đã có sẵn video thành phẩm (16:9), bỏ qua render.")
                continue"""

assert old_chk in t_norm, "old_chk not found"
t_norm = t_norm.replace(old_chk, new_chk)

final = t_norm.replace("\n", "\r\n")
with open("scripts/daily_24h_master_autopilot.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated scripts/daily_24h_master_autopilot.py cleanly!")
