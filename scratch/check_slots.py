# -*- coding: utf-8 -*-
import sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.voice_profiles import get_voice_profile_for_genre

series = get_daily_10_series('2026-10-25')
for s in series:
    total_w = sum(len(p['text'].split()) for p in s['parts'])
    profile = get_voice_profile_for_genre(s['genre'])
    sched = s.get('scheduled_time', s.get('time_slot', 'N/A'))
    print(f"Slot {s['slot_index']:02d} [{sched}]: {s['genre']} | {s['title']}")
    print(f"    Words: {total_w} | Voice: {profile.voice_name} ({profile.profile_id}) | Rate: {profile.rate} | Pitch: {profile.pitch} | Vol: {profile.volume}")


