# -*- coding: utf-8 -*-
with open("core/background_manager.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_check = """        if slice_path.exists() and slice_path.stat().st_size > 500000:
            print(f"🎬 [BackgroundManager] Sử dụng phân đoạn có sẵn: {slice_name}")
            return slice_path"""

new_check = """        if slice_path.exists() and slice_path.stat().st_size > 500000:
            probe_sl = probe_media_file(slice_path)
            if probe_sl.get("height", 0) > probe_sl.get("width", 0):
                print(f"⚠️ [BackgroundManager] Slice {slice_name} bị dính dọc (9:16), tự động xóa để cắt lại 16:9 chuẩn...")
                slice_path.unlink(missing_ok=True)
            else:
                print(f"🎬 [BackgroundManager] Sử dụng phân đoạn có sẵn (16:9): {slice_name}")
                return slice_path"""

assert old_check in t_norm, "old_check not found"
t_norm = t_norm.replace(old_check, new_check)

final = t_norm.replace("\n", "\r\n")
with open("core/background_manager.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated core/background_manager.py cleanly!")
