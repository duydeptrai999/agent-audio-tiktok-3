# -*- coding: utf-8 -*-
with open("scripts/pre_produce_night_slots.py", "r", encoding="utf-8") as f:
    c = f.read()

c_norm = c.replace("\r\n", "\n")

old_block = '''            # 3. Tạo Thumbnail độc lập
            if not part_thumb.exists() or part_thumb.stat().st_size < 5000:
                try:
                    generate_part_thumbnail(
                        source_video_or_image=slice_path,
                        output_thumb_path=part_thumb,
                        story_title=title,
                        part_label=f"TẬP {p_num}",
                        genre_tag=f"#{s.get('genre', 'TrinhThám')}"
                    )
                    print(f"  🖼️ Đã tạo thumbnail: {part_thumb.name}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi tạo thumbnail: {e}")'''

new_block = '''            # 3. Chuẩn hóa bao bì (Zero Distortion): Không tạo thumbnail ảnh tĩnh rời để tránh bị kéo dãn.
            # TikTok lấy trực tiếp frame gốc 1080x1920 từ video thành phẩm có sẵn Header Title & Mô Tả sắc nét.'''

assert old_block in c_norm, "Old block not found"
c_norm = c_norm.replace(old_block, new_block)
final = c_norm.replace("\n", "\r\n")

with open("scripts/pre_produce_night_slots.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated pre_produce_night_slots.py successfully!")
