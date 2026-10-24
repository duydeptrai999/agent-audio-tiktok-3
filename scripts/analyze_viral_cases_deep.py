# -*- coding: utf-8 -*-
"""
scripts/analyze_viral_cases_deep.py
Trích xuất chi tiết nội dung, hook, transcript, mô tả và cấu trúc của các video top viral 1M+ views
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
with open(raw_file, "r", encoding="utf-8") as f:
    cases = json.load(f)

# Sắp xếp theo view_count giảm dần
sorted_cases = sorted(cases, key=lambda x: x.get("view_count") or 0, reverse=True)

top_cases = sorted_cases[:25] # 25 video đỉnh nhất từ 300k đến 2.5M views

print(f"🔬 Đang phân tích sâu {len(top_cases)} video triệu view...")

ydl_opts = {
    "skip_download": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["vi"],
    "quiet": True
}

detailed_analysis = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, c in enumerate(top_cases, 1):
        vid_id = c["id"]
        title = c["title"]
        views = c["view_count"]
        duration = c["duration"]
        url = c["url"]
        print(f"\n[{idx}/{len(top_cases)}] Đang phân tích: {title[:50]}... ({views:,} views | {duration}s)")
        
        try:
            info = ydl.extract_info(url, download=False)
            desc = info.get("description", "")
            tags = info.get("tags", [])
            channel = info.get("channel", "")
            like_count = info.get("like_count", 0)
            
            # Phân tích hook từ mô tả hoặc tiêu đề
            first_lines = [line.strip() for line in desc.split("\n") if line.strip()][:5]
            
            analysis_item = {
                "id": vid_id,
                "title": title,
                "channel": channel,
                "views": views,
                "likes": like_count,
                "duration_seconds": duration,
                "duration_minutes": round(duration / 60, 1) if duration else 0,
                "tags": tags[:10],
                "description_preview": "\n".join(first_lines),
                "url": url
            }
            detailed_analysis.append(analysis_item)
            print(f"   -> Kênh: {channel} | Likes: {like_count:,} | Thời lượng: {round(duration/60, 1)} phút")
        except Exception as e:
            print(f"   -> Lỗi trích xuất: {e}")

out_deep = Path("data/tiktok_study/top_viral_deep_analysis.json")
with open(out_deep, "w", encoding="utf-8") as f:
    json.dump(detailed_analysis, f, ensure_ascii=False, indent=2)

print("\n" + "="*70)
print(f"✅ Hoàn tất phân tích chuyên sâu {len(detailed_analysis)} kiệt tác triệu view!")
print(f"💾 File lưu tại: {out_deep}")
print("="*70)
