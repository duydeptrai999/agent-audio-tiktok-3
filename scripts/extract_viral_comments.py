# -*- coding: utf-8 -*-
"""
scripts/extract_viral_comments.py
Trích xuất bình luận của khán giả để hiểu chính xác tâm lý người nghe:
- Họ khen điều gì?
- Đoạn nào khiến họ không dứt ra được?
- Giọng đọc, nhạc nền, cốt truyện cuốn hút họ ở điểm nào?
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

target_videos = [
    ("K5ayZo3ye_U", "Dứa Audio - Tôi Lười Đến Mức Khiến Trà Xanh Trầm Cảm (2.5M views)"),
    ("YFyJHJLxa8k", "Tâm Hồn Ăn Uống - Màn trả thù đã nhất đời tôi (1M views)"),
    ("NuIZnjtMXvY", "Túi Mù Audio - Thiên Kim Giả Bị Ảo Tưởng Nữ Chính (1.1M views)")
]

ydl_opts = {
    "skip_download": True,
    "getcomments": True,
    "max_comments": 20,
    "quiet": True
}

audience_insights = []

print("💬 Đang trích xuất bình luận thực tế của người nghe triệu view...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid_id, label in target_videos:
        print(f"\n---> Khảo sát bình luận: [{label}] (ID: {vid_id})...")
        try:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid_id}", download=False)
            comments = info.get("comments", [])
            comment_texts = []
            for c in comments[:20]:
                text = c.get("text", "")
                author = c.get("author", "")
                likes = c.get("like_count", 0)
                if text:
                    comment_texts.append({"author": author, "text": text, "likes": likes})
            
            audience_insights.append({
                "id": vid_id,
                "label": label,
                "total_comments_fetched": len(comment_texts),
                "top_comments": comment_texts
            })
            print(f"  * Lấy được {len(comment_texts)} bình luận thực tế.")
            for c in comment_texts[:3]:
                print(f"    - [{c['author']}]: {c['text'][:100]}...")
        except Exception as e:
            print(f"  * Lỗi trích xuất bình luận: {e}")

out_comments = Path("data/tiktok_study/audience_comments_insights.json")
with open(out_comments, "w", encoding="utf-8") as f:
    json.dump(audience_insights, f, ensure_ascii=False, indent=2)

print("\n" + "="*70)
print(f"✅ Đã lưu phân tích tâm lý người nghe vào: {out_comments}")
print("="*70)
