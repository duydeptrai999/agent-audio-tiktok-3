# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.stories.daily_story_factory import get_daily_10_series
from core.voice_profiles import get_voice_profile_for_genre

series = get_daily_10_series('2026-10-26')
print(f"Total slots for 2026-10-26: {len(series)}\n")
for s in series:
    words = sum(len(p['text'].split()) for p in s['parts'])
    genre = s.get('genre', '')
    voice = s.get('voice', '')
    profile = get_voice_profile_for_genre(genre)
    print(f"Slot {s['slot_index']:02d} ({s['start_time_str']}): {s['title']}")
    print(f"   Thể loại: {genre}")
    print(f"   Voice: {voice} -> Profile: {profile.profile_id} ({profile.display_name})")
    print(f"   Pitch: {profile.pitch} | Rate: {profile.rate} | Vol: {profile.volume} | Tempo: {profile.tempo_multiplier}")
    print(f"   Tổng từ: {words:,} từ (3 tập)")
    for p in s['parts']:
        p_w = len(p['text'].split())
        print(f"      - Tập {p['part_number']}: {p_w:,} từ")
    print()
