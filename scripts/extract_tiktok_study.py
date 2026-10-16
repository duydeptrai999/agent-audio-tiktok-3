import sys
import json
import yt_dlp
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

target_ids = [
    ("pfwpyPeKTn8", "Làm Bánh Kể Chuyện - Cô em thú vị"),
    ("W0HlUFKGuYM", "Làm Bánh Kể Chuyện - Lý Nguyễn Nhi"),
    ("NuIZnjtMXvY", "Túi Mù Audio - Truyện Audio"),
    ("F3rG-3AsrSg", "Kỳ Án 3 Cuộc Gọi Bí Ẩn"),
    ("h-4kKi8DvkE", "Truyện Đêm Khuya Ru Ngủ")
]

study_dir = Path("data/tiktok_study")
study_dir.mkdir(parents=True, exist_ok=True)

ydl_opts = {
    "skip_download": True,
    "writeinfojson": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["vi", "en"],
    "outtmpl": str(study_dir / "%(id)s.%(ext)s"),
    "quiet": True
}

print("🔬 BẮT ĐẦU TRÍCH XUẤT CHI TIẾT CÁC VIDEO KỂ CHUYỆN MẪU...")

analyzed_cases = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid_id, label in target_ids:
        try:
            print(f"\n---> Đang phân tích case study: [{label}] (ID: {vid_id})...")
            url = f"https://www.youtube.com/watch?v={vid_id}"
            info = ydl.extract_info(url, download=False)
            
            case_data = {
                "id": vid_id,
                "label": label,
                "title": info.get("title"),
                "description": info.get("description", "")[:1500],
                "duration": info.get("duration"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
                "tags": info.get("tags", []),
                "categories": info.get("categories", []),
                "channel": info.get("channel"),
            }
            analyzed_cases.append(case_data)
            print(f"  * Tiêu đề thực tế: '{case_data['title']}'")
            print(f"  * Kênh: {case_data['channel']} | Lượt xem: {case_data['view_count']}")
            print(f"  * Thời lượng: {case_data['duration']}s")
            print(f"  * Tags thực tế: {case_data['tags'][:8]}")
            print(f"  * Mô tả (Hook/Tóm tắt):\n{case_data['description'][:300]}...")
        except Exception as e:
            print(f"  * Lỗi khi tải info {vid_id}: {e}")

output_json = study_dir / "analyzed_tiktok_story_cases.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(analyzed_cases, f, ensure_ascii=False, indent=2)

print("\n" + "="*65)
print(f"✅ ĐÃ PHÂN TÍCH VÀ LƯU CHI TIẾT {len(analyzed_cases)} CASE STUDY THỰC TẾ VÀO:")
print(f"👉 {output_json}")
print("="*65)
