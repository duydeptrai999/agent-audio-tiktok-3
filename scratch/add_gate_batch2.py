# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("scripts/produce_and_schedule_batch2.py")
text = p.read_text(encoding="utf-8")
old = 'def produce_all_batch2_series():\n    """Sản xuất toàn bộ 5 bộ audio Batch 2 (15 video MP4 1080p)."""'
new = '''def produce_all_batch2_series():
    """Sản xuất toàn bộ 5 bộ audio Batch 2 (15 video MP4 1080p)."""
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()'''
if old in text:
    p.write_text(text.replace(old, new), encoding="utf-8")
    print("Added preflight experience to produce_and_schedule_batch2.py successfully")
else:
    print("Target not found in produce_and_schedule_batch2.py")
