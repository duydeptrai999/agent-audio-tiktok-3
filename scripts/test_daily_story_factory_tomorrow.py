# -*- coding: utf-8 -*-
"""
scripts/test_daily_story_factory_tomorrow.py
Kiểm tra danh sách 10 bộ truyện được tạo ra cho ngày mai:
- Độ dài từng tập P1, P2, P3
- Tổng từ
- Thời lượng ước tính (phút)
- Trạng thái kiểm duyệt quality_audit_passed
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(".").resolve()))

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from core.stories.daily_story_factory import get_daily_10_series

target_date = "2026-10-25"
print(f"🎬 ĐANG KHỞI CHẠY KIỂM THỬ TẠO 10 BỘ TRUYỆN CHO NGÀY MAI ({target_date})...")
print("=" * 115)

series_list = get_daily_10_series(target_date)

passed_count = 0

for s in series_list:
    slot = s["slot_index"]
    title = s["title"]
    genre = s["genre"]
    voice = s["voice"]
    parts = s["parts"]
    lens = [len(p["text"].split()) for p in parts]
    total_words = sum(lens)
    est_duration = round(total_words / 170, 1) # ~170 từ/phút ở tốc độ chuẩn 1.05x
    passed = s.get("quality_audit_passed", False)
    
    status_tag = "[ĐẠT CHUẨN 30P ĐIỆN ẢNH ✅]" if passed and est_duration >= 20.0 else "[KHÔNG ĐẠT ❌]"
    if passed and est_duration >= 20.0:
        passed_count += 1
        
    print(f"Slot {slot:02d} ({s['start_time_str']}) | {genre[:18]:<18} | P1: {lens[0]:<5} P2: {lens[1]:<5} P3: {lens[2]:<5} | Tổng: {total_words:<6} từ (~{est_duration}p) | {status_tag}")
    print(f"   -> Tiêu đề: {title[:75]}")

print("=" * 115)
print(f"KẾT QUẢ: {passed_count}/10 bộ truyện ĐẠT CHUẨN ĐIỆN ẢNH >= 20-60 PHÚT (ZERO 49S)!")
