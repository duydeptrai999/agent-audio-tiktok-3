# -*- coding: utf-8 -*-
import re

with open("core/background_manager.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

# 1. Update _collect_all_candidate_pool_files
old_collect = """        # Bổ sung thêm các video dọc 9:16 dài (>= 10 phút) có sẵn trong baking/ và cooking/
        for subdir in ["baking", "cooking"]:
            sub_path = ROOT_DIR / "assets" / "footage" / subdir
            if sub_path.exists():
                for vf in sub_path.glob("*vertical*.mp4"):
                    if vf.is_file() and vf.stat().st_size > 15000000:
                        pool_files.append(vf)"""

new_collect = """        # Bổ sung các video gốc ngang 16:9 có sẵn trong raw_downloaded (baking/cooking/nature 16:9)
        raw_dir = ROOT_DIR / "assets" / "footage" / "raw_downloaded"
        if raw_dir.exists():
            for rf in raw_dir.glob("*.mp4"):
                if rf.is_file() and rf.stat().st_size > 15000000:
                    pool_files.append(rf)"""

assert old_collect in t_norm, "old_collect not found"
t_norm = t_norm.replace(old_collect, new_collect)

# 2. Update fallback source_path in get_distinct_slice_for_part
old_cand = """        if not source_path or not source_path.exists():
            cand = list((ROOT_DIR / "assets" / "footage").glob("*vertical*.mp4")) or list((ROOT_DIR / "assets" / "footage").glob("*clean*.mp4"))
            source_path = cand[0] if cand else (ROOT_DIR / "assets" / "footage" / "baking_vertical.mp4")"""

new_cand = """        if not source_path or not source_path.exists():
            cand = (
                list((ROOT_DIR / "assets" / "footage" / "youtube_pool").glob("*.mp4")) or
                list((ROOT_DIR / "assets" / "footage" / "raw_downloaded").glob("*.mp4")) or
                list((ROOT_DIR / "assets" / "footage").glob("*horizontal*.mp4"))
            )
            source_path = cand[0] if cand else (ROOT_DIR / "assets" / "footage" / "youtube_pool" / "traditional_pottery_teapot_asmr_AGVNlB400qI.mp4")"""

assert old_cand in t_norm, "old_cand not found"
t_norm = t_norm.replace(old_cand, new_cand)

# 3. Update slice check in get_distinct_slice_for_part to reject vertical slices
old_slice_check = """        if slice_path.exists() and slice_path.stat().st_size > 500000:
            print(f"🎬 [BackgroundManager] Sử dụng phân đoạn video có sẵn: {slice_name}")
            return slice_path"""

new_slice_check = """        if slice_path.exists() and slice_path.stat().st_size > 500000:
            probe_sl = probe_media_file(slice_path)
            # Nếu slice cũ vô tình bị dính tỷ lệ dọc (9:16) -> tự động xóa để cắt lại 16:9 nguyên bản
            if probe_sl.get("height", 0) > probe_sl.get("width", 0):
                print(f"⚠️ [BackgroundManager] Slice cũ {slice_name} bị dọc (9:16), tự động xóa để cắt lại chuẩn 16:9...")
                slice_path.unlink(missing_ok=True)
            else:
                print(f"🎬 [BackgroundManager] Sử dụng phân đoạn video có sẵn (16:9): {slice_name}")
                return slice_path"""

assert old_slice_check in t_norm, "old_slice_check not found"
t_norm = t_norm.replace(old_slice_check, new_slice_check)

# 4. Update log text
t_norm = t_norm.replace("Đang cắt phân đoạn B-Roll 9:16 (1080x1920)", "Đang cắt phân đoạn B-Roll 16:9 (1920x1080)")

final_text = t_norm.replace("\n", "\r\n")
with open("core/background_manager.py", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Updated core/background_manager.py successfully!")
