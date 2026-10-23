# -*- coding: utf-8 -*-
with open('core/stories/daily_story_factory.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        for offset in range(len(catalog)):
            idx = (start_offset + offset) % len(catalog)
            candidate_fn = catalog[idx]
            cand_story = candidate_fn() if callable(candidate_fn) else candidate_fn
            cand_title = cand_story.get("title", "")
            if is_title_allowed(cand_title, published_set):
                chosen_story = cand_story
                break"""

replacement = """        for offset in range(len(catalog)):
            idx = (start_offset + offset) % len(catalog)
            candidate_fn = catalog[idx]
            cand_story = candidate_fn() if callable(candidate_fn) else candidate_fn
            cand_title = cand_story.get("title", "")
            if is_title_allowed(cand_title, published_set):
                # Kiểm tra độ dài: tối thiểu 400 từ mỗi part để đảm bảo thời lượng audio >= 100s
                parts = cand_story.get("parts", [])
                if parts:
                    lens = [len((p.get("full_text") or p.get("text") or "").split()) for p in parts]
                else:
                    lens = [len(cand_story.get(f"part{i}", "").split()) for i in (1, 2, 3)]
                if not lens or min(lens) >= 400:
                    chosen_story = cand_story
                    break"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/stories/daily_story_factory.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Added min word validation to daily_story_factory.py!")
else:
    print("ERROR: Target not found!")
