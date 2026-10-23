# -*- coding: utf-8 -*-
from pathlib import Path

# 1. Update scripts/produce_series.py
p1 = Path("scripts/produce_series.py")
content1 = p1.read_text(encoding="utf-8")
old1 = "def produce_story_videos(story_data: dict, prefix: str, bgm_file: Path):\n    \"\"\"Sản xuất toàn bộ audio và render 3 video cho 1 bộ truyện với B-Roll riêng biệt và Thumbnail riêng từng phần.\"\"\""
new1 = """def produce_story_videos(story_data: dict, prefix: str, bgm_file: Path):
    \"\"\"Sản xuất toàn bộ audio và render 3 video cho 1 bộ truyện với B-Roll riêng biệt và Thumbnail riêng từng phần.\"\"\"
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()"""
if old1 in content1:
    p1.write_text(content1.replace(old1, new1), encoding="utf-8")
    print("Added preflight experience to produce_series.py")

# 2. Update scripts/produce_and_schedule_batch2.py
p2 = Path("scripts/produce_and_schedule_batch2.py")
content2 = p2.read_text(encoding="utf-8")
old2 = "def produce_and_publish_all_batch2(schedule_mode: bool = False):\n    series_list = get_batch2_5_series_data()"
new2 = """def produce_and_publish_all_batch2(schedule_mode: bool = False):
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()
    series_list = get_batch2_5_series_data()"""
if old2 in content2:
    p2.write_text(content2.replace(old2, new2), encoding="utf-8")
    print("Added preflight experience to produce_and_schedule_batch2.py")
