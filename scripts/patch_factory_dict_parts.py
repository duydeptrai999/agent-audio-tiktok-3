# -*- coding: utf-8 -*-
import sys

TARGET = "core/stories/daily_story_factory.py"
with open(TARGET, "r", encoding="utf-8") as f:
    text = f.read()

old_block1 = '''            if is_title_allowed(cand_title, published_set):
                parts = cand_story.get("parts", [])
                if not parts and ("part1" in cand_story or "part2" in cand_story):
                    parts = [
                        {"part_number": 1, "text": cand_story.get("part1", "")},
                        {"part_number": 2, "text": cand_story.get("part2", "")},
                        {"part_number": 3, "text": cand_story.get("part3", "")}
                    ]'''

new_block1 = '''            if is_title_allowed(cand_title, published_set):
                parts = cand_story.get("parts", [])
                if isinstance(parts, dict):
                    parts = [
                        {"part_number": 1, "text": parts.get("part1", "")},
                        {"part_number": 2, "text": parts.get("part2", "")},
                        {"part_number": 3, "text": parts.get("part3", "")}
                    ]
                elif not parts and ("part1" in cand_story or "part2" in cand_story):
                    parts = [
                        {"part_number": 1, "text": cand_story.get("part1", "")},
                        {"part_number": 2, "text": cand_story.get("part2", "")},
                        {"part_number": 3, "text": cand_story.get("part3", "")}
                    ]'''

old_block2 = '''        parts_list = []
        parts_source = chosen_story.get("parts", [])
        if not parts_source and ("part1" in chosen_story or "part2" in chosen_story):
            parts_source = [
                {"part_number": 1, "text": chosen_story.get("part1", "")},
                {"part_number": 2, "text": chosen_story.get("part2", "")},
                {"part_number": 3, "text": chosen_story.get("part3", "")}
            ]'''

new_block2 = '''        parts_list = []
        parts_source = chosen_story.get("parts", [])
        if isinstance(parts_source, dict):
            parts_source = [
                {"part_number": 1, "text": parts_source.get("part1", "")},
                {"part_number": 2, "text": parts_source.get("part2", "")},
                {"part_number": 3, "text": parts_source.get("part3", "")}
            ]
        elif not parts_source and ("part1" in chosen_story or "part2" in chosen_story):
            parts_source = [
                {"part_number": 1, "text": chosen_story.get("part1", "")},
                {"part_number": 2, "text": chosen_story.get("part2", "")},
                {"part_number": 3, "text": chosen_story.get("part3", "")}
            ]'''

if old_block1 in text and old_block2 in text:
    text = text.replace(old_block1, new_block1).replace(old_block2, new_block2)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(text)
    print("Patched daily_story_factory.py successfully!")
else:
    print("Could not find target blocks in daily_story_factory.py!")
