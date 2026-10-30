# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.daily_24h_master_autopilot import produce_single_series, load_daily_status
from core.stories.daily_story_factory import get_daily_10_series

date_str = "2026-10-25"
series_list = get_daily_10_series(date_str)
s4 = next(s for s in series_list if s["slot_index"] == 4)

status = load_daily_status(date_str, series_list)
print(f"🎬 Bắt đầu sản xuất sớm Bộ 4: {s4['title']} với GIỌNG ĐỌC NHẸ NHÀNG TỐI ƯU...")
produce_single_series(s4, status, date_str)
print("✅ HOÀN TẤT SẢN XUẤT BỘ 4!")
