# -*- coding: utf-8 -*-
with open("core/ffmpeg_utils.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_footage_fn = '''    vf_916 = "crop='min(iw,ih*9/16)':'min(ih,iw*16/9)':'(iw-min(iw,ih*9/16))/2':'(ih-min(ih,iw*16/9))/2',scale=1080:1920,setsar=1"

    # 1. Nếu có file source_video chỉ định hợp lệ (> 100KB)
    if source_video and Path(source_video).exists() and Path(source_video).stat().st_size > 100000:
        cmd = [
            ffmpeg, "-y",
            "-i", str(source_video),
            "-vf", vf_916,
            "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
            "-an",
            str(output_file)
        ]'''

new_footage_fn = '''    # 1. Nếu có file source_video chỉ định hợp lệ (> 100KB) - GIỮ NGUYÊN KHUNG HÌNH GỐC
    if source_video and Path(source_video).exists() and Path(source_video).stat().st_size > 100000:
        cmd = [
            ffmpeg, "-y",
            "-i", str(source_video),
            "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
            "-an",
            str(output_file)
        ]'''

old_render_base = '''    # 1. Cưỡng bức khung hình chuẩn dọc 9:16 (1080x1920) Full-Screen cho mọi nguồn video đầu vào
    base_vf = (
        "crop='min(iw,ih*9/16)':'min(ih,iw*16/9)':'(iw-min(iw,ih*9/16))/2':'(ih-min(ih,iw*16/9))/2',"
        "scale=1080:1920,setsar=1"
    )

    # 2. Tạo Header Overlay PNG trong suốt (Be Vietnam Pro + Pill Badge + Bóng đổ mềm, KHÔNG dùng hộp nền đen)
    header_png_path: Optional[Path] = None
    if title_text or badge_label:
        try:
            from core.visual_design import render_video_header_overlay
            header_png_path = output_file.parent / f"temp_hdr_{output_file.stem}.png"
            render_video_header_overlay(
                output_png=header_png_path,
                title=title_text or badge_label,
                part_label=badge_label or "TẬP 1",
                genre=genre or title_text,
                width=1080,
                height=1920
            )'''

new_render_base = '''    # 1. GIỮ NGUYÊN 100% KHUNG HÌNH GỐC CỦA VIDEO (Zero Crop / Zero Stretch / Zero Fit)
    # Tuyệt đối KHÔNG crop, KHÔNG scale ép fit khung hình làm méo video!
    base_vf = "null"

    # Lấy kích thước thực tế của video nền để vẽ Header Overlay vừa vặn hoàn hảo
    vid_probe = probe_media_file(Path(clean_footage_path))
    vid_w = vid_probe.get("width") or 1080
    vid_h = vid_probe.get("height") or 1920

    # 2. Tạo Header Overlay PNG trong suốt khớp đúng kích thước video gốc
    header_png_path: Optional[Path] = None
    if title_text or badge_label:
        try:
            from core.visual_design import render_video_header_overlay
            header_png_path = output_file.parent / f"temp_hdr_{output_file.stem}.png"
            render_video_header_overlay(
                output_png=header_png_path,
                title=title_text or badge_label,
                part_label=badge_label or "TẬP 1",
                genre=genre or title_text,
                width=vid_w,
                height=vid_h
            )'''

old_fallback_vf = 'vf_only_916 = "crop=\'min(iw,ih*9/16)\':\'min(ih,iw*16/9)\':\'(iw-min(iw,ih*9/16))/2\':\'(ih-min(ih,iw*16/9))/2\',scale=1080:1920,setsar=1"'
new_fallback_vf = 'vf_only_916 = "null"  # Giữ nguyên khung hình gốc của video, không crop/scale'

assert old_footage_fn in t_norm, "old_footage_fn not found"
assert old_render_base in t_norm, "old_render_base not found"
assert old_fallback_vf in t_norm, "old_fallback_vf not found"

t_norm = t_norm.replace(old_footage_fn, new_footage_fn)
t_norm = t_norm.replace(old_render_base, new_render_base)
t_norm = t_norm.replace(old_fallback_vf, new_fallback_vf)

final = t_norm.replace("\n", "\r\n")

with open("core/ffmpeg_utils.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated core/ffmpeg_utils.py successfully!")
