from pathlib import Path

p = Path("scripts/produce_series.py")
content = p.read_text(encoding="utf-8")

target = """    print("\\n" + "=" * 70)
    print(f"🎬 BẮT ĐẦU SẢN XUẤT TRỌN BỘ: {story_data['title']}")
    print(f"🎙️ Giọng đọc: {story_data['voice']} (Tốc độ 1.5x)")
    print("=" * 70)

    for part in story_data["parts"]:"""

replacement = """    print("\\n" + "=" * 70)
    print(f"🎬 BẮT ĐẦU SẢN XUẤT TRỌN BỘ: {story_data['title']}")
    print(f"🎙️ Giọng đọc: {story_data['voice']} (Tốc độ 1.5x)")
    print("=" * 70)

    # BẮT BUỘC: Đọc kinh nghiệm từ GEMINI.md & 5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md trước khi sản xuất
    from core.stories.script_quality_gate import validate_story_series, require_preflight_experience
    require_preflight_experience()
    story_data = validate_story_series(story_data)

    for part in story_data["parts"]:"""

norm_content = content.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_replacement = replacement.replace("\r\n", "\n")

if norm_target in norm_content:
    updated = norm_content.replace(norm_target, norm_replacement, 1)
    p.write_text(updated, encoding="utf-8")
    print("PATCH PRODUCE_SERIES SUCCESSFUL")
else:
    print("TARGET NOT FOUND IN PRODUCE_SERIES")
