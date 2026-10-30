# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")
import json
from pathlib import Path

from core.daily_schedule_config import DAILY_10_SLOTS
from core.stories.daily_story_factory import get_daily_10_series

def inspect_day(target_date: str):
    fpath = Path(f"data/daily_schedule_status_{target_date}.json")
    if not fpath.exists():
        print(f"File not found: {fpath}")
        return
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)

    series_list = get_daily_10_series(target_date)
    series_map = {s["slot_index"]: s for s in series_list}

    print("=" * 90)
    print(f"📅 CHI TIẾT LỊCH TRÌNH VÀ TIẾN ĐỘ SẢN XUẤT AUDIO: NGÀY {target_date}")
    print("=" * 90)
    
    total_words_day = 0
    total_duration_mins_day = 0

    for s_cfg in DAILY_10_SLOTS:
        idx = s_cfg["slot_index"]
        s_data = series_map.get(idx, {})
        key = s_data.get("key", f"{target_date.replace('-', '')}_slot_{idx:02d}")
        status_info = data.get(key, {})

        time_str = s_cfg["start_time_str"]
        genre = s_cfg["genre"]
        voice = s_cfg["voice"]
        title = status_info.get("title", s_data.get("title", "Chưa đặt tiêu đề"))
        parts = s_data.get("parts", [])
        
        words_count = 0
        if isinstance(parts, list):
            words_count = sum(len(p.get("text", "").split()) for p in parts)
        elif isinstance(parts, dict):
            words_count = sum(len(text.split()) for text in parts.values())
        
        est_minutes = round(words_count / 160.0, 1) if words_count > 0 else 0.0
        total_words_day += words_count
        total_duration_mins_day += est_minutes

        produced = status_info.get("produced", False)
        p1 = status_info.get("part1", False)
        p2 = status_info.get("part2", False)
        p3 = status_info.get("part3", False)

        prod_tag = "✅ ĐÃ SẢN XUẤT" if produced else "⏳ CHỜ TỚI GIỜ"
        pub_tag = f"Part 1: {'[ĐÃ ĐĂNG]' if p1 else '[CHƯA]'} | Part 2: {'[ĐÃ ĐĂNG]' if p2 else '[CHƯA]'} | Part 3: {'[ĐÃ ĐĂNG]' if p3 else '[CHƯA]'}"

        print(f"Slot {idx:02d} | ⏰ {time_str} | Thể loại: {genre} | Giọng: {voice.split('-')[-1]}")
        print(f"   📖 Tiêu đề: {title}")
        print(f"   📊 Quy mô: 3 Tập - Tổng {words_count:,} từ (~{est_minutes} phút audio điện ảnh)")
        print(f"   🎬 Sản xuất: {prod_tag} | TikTok Publish: {pub_tag}")
        print("-" * 90)

    print(f"🌟 TỔNG CỘNG NGÀY {target_date}: {total_words_day:,} từ (~{total_duration_mins_day:.1f} phút = {total_duration_mins_day/60:.1f} giờ audio chuẩn điện ảnh)")
    print("=" * 90 + "\n")

def main():
    inspect_day("2026-10-24")
    inspect_day("2026-10-25")

if __name__ == "__main__":
    main()
