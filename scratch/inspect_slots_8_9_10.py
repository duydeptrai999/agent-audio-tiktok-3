# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.stories.daily_story_factory import get_daily_10_series

series_list = get_daily_10_series("2026-10-28")
for s in series_list:
    if s["slot_index"] in [8, 9, 10]:
        idx = s["slot_index"]
        key = s["key"]
        prefix = s["prefix"]
        title = s["title"]
        genre = s.get("genre")
        bgm_genre = s.get("bgm_genre")
        voice = s.get("voice")
        print(f"=== SLOT {idx} ===")
        print(f"Key: {key}")
        print(f"Prefix: {prefix}")
        print(f"Title: {title}")
        print(f"Genre: {genre} | BGM Genre: {bgm_genre}")
        print(f"Voice: {voice}")
        for p in s.get("parts", []):
            p_num = p["part_number"]
            badge = p.get("badge_label")
            words = len(p.get("text", "").split())
            print(f"  Part {p_num}: {badge} ({words} words)")
