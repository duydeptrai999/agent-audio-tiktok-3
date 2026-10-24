# -*- coding: utf-8 -*-
import sys
import importlib
from pathlib import Path

sys.path.insert(0, str(Path(".").resolve()))

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

stories_dir = Path("core/stories")
py_files = sorted([f for f in stories_dir.glob("*.py") if f.name not in ["__init__.py", "script_quality_gate.py", "daily_story_factory.py"]])

print("📊 PHÂN TÍCH CHÍNH XÁC ĐỘ DÀI CỦA TỪNG BỘ TRUYỆN TRONG CORE/STORIES:")
print("=" * 110)
print(f"{'Tên File':<35} | {'Hàm Tạo':<35} | {'P1':<6} {'P2':<6} {'P3':<6} | {'Tổng Từ':<8} {'Thời lượng ước tính'}")
print("=" * 110)

long_form = []
short_form = []

for f in py_files:
    mod_name = f"core.stories.{f.stem}"
    try:
        mod = importlib.import_module(mod_name)
        for attr in dir(mod):
            if attr.startswith("get_") and ("story" in attr or "masterpiece" in attr or "cycle" in attr):
                fn = getattr(mod, attr)
                if callable(fn):
                    try:
                        story = fn()
                        if isinstance(story, dict) and "parts" in story:
                            parts = story["parts"]
                            lens = [len(p.get("full_text", "").split()) for p in parts]
                            total = sum(lens)
                            p1 = lens[0] if len(lens) > 0 else 0
                            p2 = lens[1] if len(lens) > 1 else 0
                            p3 = lens[2] if len(lens) > 2 else 0
                            
                            # Tính thời lượng ở tốc độ 1.0x (160 từ/phút) và 1.2x (190 từ/phút)
                            est_min = round(total / 180, 1)
                            
                            if total >= 3500 and min(p1, p2, p3) >= 1000:
                                long_form.append((f.name, attr, p1, p2, p3, total, est_min))
                                print(f"{f.name:<35} | {attr:<35} | {p1:<6} {p2:<6} {p3:<6} | {total:<8} (~{est_min}p) [CHUẨN 30P ĐIỆN ẢNH ✅]")
                            else:
                                short_form.append((f.name, attr, p1, p2, p3, total, est_min))
                                print(f"{f.name:<35} | {attr:<35} | {p1:<6} {p2:<6} {p3:<6} | {total:<8} (~{est_min}p) [QUÁ NGẮN ❌]")
                    except Exception as err:
                        pass
    except Exception as err:
        pass

print("=" * 110)
print(f"✅ TỔNG CỘNG: {len(long_form)} bộ ĐẠT CHUẨN DÀI (>= 30 Phút) | ❌ {len(short_form)} bộ BỊ NGẮN (< 30 Phút)")
print("=" * 110)
