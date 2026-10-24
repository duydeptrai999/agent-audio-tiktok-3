# -*- coding: utf-8 -*-
"""
scripts/fetch_full_100_plus_cases.py
Thu thập bổ sung để đạt tối thiểu 100 - 110 case study audio truyện viral triệu view thực tế tại Việt Nam
"""
import sys
import json
from pathlib import Path
import yt_dlp

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

raw_file = Path("data/tiktok_study/viral_100_raw_cases.json")
existing_cases = []
seen_ids = set()

if raw_file.exists():
    with open(raw_file, "r", encoding="utf-8") as f:
        existing_cases = json.load(f)
        for c in existing_cases:
            if c.get("id"):
                seen_ids.add(c["id"])

print(f"📦 Đang có sẵn: {len(existing_cases)} case study.")

additional_queries = [
    ("truyện audio tâm lý tội phạm hồ sơ kỳ án", 6),
    ("truyện zhihu hào môn tổng tài audio", 6),
    ("kể chuyện đêm khuya truyện ngắn chữa lành audio", 6),
    ("truyện audio ngôn tình ngược trước sủng sau", 6),
    ("làm bánh nghe kể chuyện tiktok triệu tim", 6),
    ("kỳ án có thật kinh dị việt nam audio", 6)
]

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

new_added = 0

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q, limit in additional_queries:
        print(f"\n---> Tìm kiếm bổ sung: '{q}' (Target: {limit})...")
        try:
            res = ydl.extract_info(f"ytsearch{limit}:{q}", download=False)
            entries = res.get("entries", [])
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
                existing_cases.append(item)
                new_added += 1
                print(f"  + [{len(existing_cases)}] {item['title'][:55]}... ({item['duration']}s | {item['view_count']} views)")
        except Exception as err:
            print(f"  * Lỗi: {err}")

out_path = Path("data/tiktok_study/viral_full_100_cases.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(existing_cases, f, ensure_ascii=False, indent=2)

print("\n" + "="*70)
print(f"✅ TỔNG CỘNG ĐÃ CÓ: {len(existing_cases)} CASE STUDY AUDIO TRUYỆN VIRAL (Bổ sung mới: {new_added})!")
print(f"💾 File lưu tại: {out_path}")
print("="*70)
