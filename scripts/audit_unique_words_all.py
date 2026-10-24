# -*- coding: utf-8 -*-
"""
scripts/audit_unique_words_all.py
Kiểm tra dung lượng THỰC TẾ (sau khi loại bỏ đoạn văn trùng lặp) của toàn bộ các file trong core/stories.
"""
import sys
import importlib
from pathlib import Path

sys.path.insert(0, str(Path(".").resolve()))

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from core.stories.daily_story_factory import clean_and_deduplicate_script

stories_dir = Path("core/stories")
py_files = sorted([f for f in stories_dir.glob("*.py") if f.name not in ["__init__.py", "script_quality_gate.py", "daily_story_factory.py"]])

print("📊 PHÂN TÍCH DUNG LƯỢNG THẬT (ZERO TRÙNG LẶP ĐOẠN VĂN):")
print("=" * 105)
print(f"{'Tên File':<35} | {'Hàm Tạo':<32} | {'P1':<5} {'P2':<5} {'P3':<5} | {'Tổng Từ':<6} {'Thời lượng thật'}")
print("=" * 105)

genuine_long_stories = []

for f in py_files:
    mod_name = f"core.stories.{f.stem}"
    try:
        mod = importlib.import_module(mod_name)
        for attr in dir(mod):
            if attr.startswith("get_") and ("story" in attr or "masterpiece" in attr):
                fn = getattr(mod, attr)
                if callable(fn):
                    try:
                        story = fn()
                        if isinstance(story, dict) and "parts" in story:
                            parts = story["parts"]
                            clean_lens = []
                            for p in parts:
                                raw = p.get("full_text") or p.get("text") or ""
                                clean = clean_and_deduplicate_script(raw)
                                clean_lens.append(len(clean.split()))
                            total = sum(clean_lens)
                            p1 = clean_lens[0] if len(clean_lens) > 0 else 0
                            p2 = clean_lens[1] if len(clean_lens) > 1 else 0
                            p3 = clean_lens[2] if len(clean_lens) > 2 else 0
                            est_min = round(total / 170, 1)
                            
                            is_genuine_30m = (total >= 3500 and min(p1, p2, p3) >= 1000)
                            status = "[CHUẨN THẬT 30P ✅]" if is_genuine_30m else "[BỊ LẶP HOẶC NGẮN ❌]"
                            if is_genuine_30m:
                                genuine_long_stories.append((f.name, attr, total, est_min))
                            print(f"{f.name:<35} | {attr:<32} | {p1:<5} {p2:<5} {p3:<5} | {total:<6} (~{est_min}p) {status}")
                    except Exception:
                        pass
    except Exception:
        pass

print("=" * 105)
print(f"Tổng số bộ đạt chuẩn thật (>= 3,500 từ độc bản 100%): {len(genuine_long_stories)}")
for item in genuine_long_stories:
    print(f"  * {item[0]} -> {item[1]} ({item[2]} từ | ~{item[3]} phút)")
print("=" * 105)
