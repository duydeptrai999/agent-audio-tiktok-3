# -*- coding: utf-8 -*-
"""
scripts/gather_tiktok_viral_100.py
Thu thập và phân tích chi tiết 50 - 100 video audio truyện ngắn / Zhihu / Kể chuyện viral triệu view tại Việt Nam
"""
import sys
import os
import json
from pathlib import Path
import yt_dlp

# Đảm bảo in tiếng Việt chuẩn trên Windows console
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

queries = [
    ("truyện zhihu vả mặt trà xanh audio tiktok", 10),
    ("truyện zhihu mẹ chồng nàng dâu audio", 10),
    ("truyện zhihu trọng sinh báo thù audio", 10),
    ("truyện zhihu kinh dị quái đàm audio", 10),
    ("truyện zhihu trinh thám kỳ án audio", 10),
    ("truyện zhihu thanh xuân cứu rỗi audio", 10),
    ("làm bánh kể chuyện tiktok triệu view", 10),
    ("kỳ án có thật hồ sơ vụ án tiktok", 10),
    ("tâm sự đêm khuya truyện ngắn audio tiktok", 10),
    ("truyện zhihu sa điêu hài hước audio", 10)
]

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

all_entries = []
seen_ids = set()

print("🔍 Đang bắt đầu thu thập 100 case study audio truyện viral...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q, limit in queries:
        print(f"\n---> Khảo sát từ khóa: '{q}' (Target: {limit})...")
        try:
            res = ydl.extract_info(f"ytsearch{limit}:{q}", download=False)
            entries = res.get("entries", [])
            count = 0
            for e in entries:
                vid_id = e.get("id")
                if not vid_id or vid_id in seen_ids:
                    continue
                seen_ids.add(vid_id)
                item = {
                    "query": q,
                    "id": vid_id,
                    "title": e.get("title"),
                    "url": e.get("url") or f"https://www.youtube.com/watch?v={vid_id}",
                    "duration": e.get("duration"),
                    "view_count": e.get("view_count"),
                    "uploader": e.get("uploader"),
                    "description": e.get("description", "")
                }
                all_entries.append(item)
                count += 1
                print(f"  [{len(all_entries)}] {item['title'][:60]}... ({item['duration']}s | {item['view_count']} views)")
        except Exception as err:
            print(f"  * Lỗi khi query '{q}': {err}")

out_path = Path("data/tiktok_study/viral_100_raw_cases.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_entries, f, ensure_ascii=False, indent=2)

print("\n" + "="*70)
print(f"✅ ĐÃ THU THẬP TỔNG CỘNG {len(all_entries)} CASE STUDY AUDIO TRUYỆN VIRAL!")
print(f"💾 File lưu tại: {out_path}")
print("="*70)
