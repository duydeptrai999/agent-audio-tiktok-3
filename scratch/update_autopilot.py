# -*- coding: utf-8 -*-
with open("scripts/daily_24h_master_autopilot.py", "r", encoding="utf-8") as f:
    content = f.read()

# Normalize to \n for matching
c_norm = content.replace("\r\n", "\n")

old_caption_func = '''def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    title = series_conf["title"]
    part_custom_caption = ""
    for p in series_conf.get("parts", []):
        if p.get("part_number") == part_num:
            part_custom_caption = (p.get("caption") or "").strip()
            break
    if part_custom_caption and len(part_custom_caption) > 15:
        desc = part_custom_caption
    else:
        hooks = series_conf.get("hooks", [])
        magnets = series_conf.get("magnets", [])
        hook = hooks[min(part_num - 1, len(hooks) - 1)] if hooks else ""
        magnet = magnets[min(part_num - 1, len(magnets) - 1)] if magnets else ""
        desc = f"{hook} {magnet}".strip()
    tag = series_conf.get("genre_tag", "#audiotruyen #podcast #fyp")
    return f"{badge} {title}. {desc} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}".strip()'''

new_caption_func = '''def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    from core.visual_design import split_title, classify_genre_style

    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    raw_title = series_conf.get("title", "")
    main_title, sub_title = split_title(raw_title)

    # Lấy mô tả theo tập (hook / câu hỏi kích thích thảo luận)
    part_custom_caption = ""
    for p in series_conf.get("parts", []):
        if p.get("part_number") == part_num:
            part_custom_caption = (p.get("caption") or "").strip()
            break

    if part_custom_caption and len(part_custom_caption) > 15:
        desc = part_custom_caption
    else:
        hooks = series_conf.get("hooks", [])
        hook = hooks[min(part_num - 1, len(hooks) - 1)] if hooks else ""
        if "—" in hook:
            desc = hook.split("—", 1)[1].strip()
        elif "-" in hook and not hook.startswith("-"):
            desc = hook.split("-", 1)[1].strip()
        elif hook:
            desc = hook.replace("«", "").replace("»", "").strip()
            if len(desc) > 120:
                desc = desc[:120].rsplit(" ", 1)[0] + "..."
        else:
            desc = sub_title.strip() if sub_title else "Audio Đời Thực • Cắm tai nghe cảm nhận trọn vẹn."

    # Hashtags ngắn gọn, chuẩn xu hướng theo thể loại
    genre_tag_map = {
        "horror": "#kinhdi #quaidam",
        "detective": "#trinhtham #kyan",
        "survival": "#matthe #sinhton",
        "comedy": "#sadieu #haihuoc",
        "palace": "#cungdau #cophong",
        "revenge": "#vamat #trongsinh",
        "family": "#giadau #mechong",
        "rich": "#haomon #tongtai",
        "romance": "#thanhxuan #chualanh",
    }
    genre_style = classify_genre_style(f"{series_conf.get('genre', '')} {raw_title}")
    genre_tags = genre_tag_map.get(genre_style, "#truyenngan")

    caption_lines = [
        f"{badge} {main_title}",
        f"📖 {sub_title}" if sub_title else "",
        f"💬 {desc}" if desc else "",
        "👉 Cắm tai nghe thưởng thức trọn bộ tại kênh!",
        f"#audiotruyen #kechuyen #xuhuong #fyp {genre_tags}"
    ]
    return "\\n".join([line for line in caption_lines if line])'''

old_thumb_block = '''        # 3. Thumbnail 9:16 chuẩn lưới hồ sơ TikTok
        if not part_thumb.exists() or part_thumb.stat().st_size < 5000:
            try:
                generate_part_thumbnail(
                    source_video_or_image=slice_path,
                    output_thumb_path=part_thumb,
                    story_title=title,
                    part_label=f"TẬP {p_num}" if p_num < 3 else "TẬP 3 - KẾT",
                    genre_tag=f"#{genre_name}"
                )
            except Exception:
                pass'''

new_thumb_block = '''        # 3. Chuẩn hóa bao bì (Zero Distortion): Không tạo thumbnail ảnh tĩnh rời để tránh bị kéo dãn méo hình.
        # TikTok Studio tự động lấy frame trực tiếp từ video gốc 1080x1920 có sẵn Header Title & Mô Tả sắc nét.'''

old_upload_thumb = 'thumbnail_path=part_thumb_file if part_thumb_file.exists() else None,'
new_upload_thumb = 'thumbnail_path=None,  # Không upload cover ảnh tĩnh; TikTok lấy native frame 1080x1920 sắc nét,'

assert old_caption_func in c_norm, "Caption func not found"
assert old_thumb_block in c_norm, "Thumb block not found"
assert old_upload_thumb in c_norm, "Upload thumb not found"

c_norm = c_norm.replace(old_caption_func, new_caption_func)
c_norm = c_norm.replace(old_thumb_block, new_thumb_block)
c_norm = c_norm.replace(old_upload_thumb, new_upload_thumb)

# Restore CRLF
final_content = c_norm.replace("\n", "\r\n")

with open("scripts/daily_24h_master_autopilot.py", "w", encoding="utf-8") as f:
    f.write(final_content)

print("SUCCESS: Updated daily_24h_master_autopilot.py!")
