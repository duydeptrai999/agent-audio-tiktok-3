import sys
import json
import yt_dlp

# Reconfigure output to UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

queries = [
    "kể chuyện làm bánh tiktok",
    "baking storytime tiktok việt nam",
    "audio truyện ngắn tiktok triệu view",
    "kỳ án có thật tiktok",
    "kể chuyện đêm khuya ru ngủ tiktok",
    "truyện tâm sự reddit làm bánh tiktok"
]

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

all_found = []
print("🔍 BẮT ĐẦU CÀO VÀ KHẢO SÁT CÁC VIDEO THỰC TẾ TRÊN MẠNG...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q in queries:
        try:
            print(f"\n---> Tìm kiếm từ khóa: '{q}'")
            res = ydl.extract_info(f"ytsearch4:{q}", download=False)
            for entry in res.get("entries", []):
                title = entry.get("title") or "N/A"
                vid_id = entry.get("id")
                url = entry.get("url") or f"https://www.youtube.com/watch?v={vid_id}"
                duration = entry.get("duration") or 0
                views = entry.get("view_count") or 0
                
                item = {
                    "query": q,
                    "title": title,
                    "id": vid_id,
                    "url": url,
                    "duration": duration,
                    "views": views
                }
                all_found.append(item)
                print(f"  * [Đã tìm thấy] {title} (ID: {vid_id})")
        except Exception as e:
            print(f"  * Lỗi khi tìm '{q}': {e}")

output_path = "data/real_tiktok_cases.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_found, f, ensure_ascii=False, indent=2)

print("\n" + "="*60)
print(f"✅ ĐÃ THU THẬP THÀNH CÔNG {len(all_found)} VIDEO KỂ CHUYỆN AUDIO THỰC TẾ!")
print(f"💾 Đã lưu danh sách vào {output_path}")
print("="*60)
