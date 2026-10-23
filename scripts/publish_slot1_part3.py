# -*- coding: utf-8 -*-
import sys
import json
import time
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.tiktok_publisher_core import upload_and_publish_video
from core.video_audit_engine import VideoAuditEngine
from core.anti_repost_guard import AntiRepostGuard
from core.stories.daily_story_factory import get_daily_10_series

def main():
    date_str = "2026-10-20"
    series_list = get_daily_10_series(date_str)
    s1 = series_list[0]
    
    vid_file = ROOT / "assets" / "output" / "VID_20261020_s01_slot_01_sadieu_part3_final.mp4"
    audio_file = ROOT / "assets" / "audio" / "VID_20261020_s01_slot_01_sadieu_part3_15x.mp3"
    thumb_file = ROOT / "assets" / "thumbnails" / "VID_20261020_s01_slot_01_sadieu_part3_thumb.jpg"
    
    title = s1["title"]
    badge = "[TẬP 3 - KẾT]"
    hook = s1["hooks"][2]
    magnet = s1["magnets"][2]
    tag = s1["genre_tag"]
    caption = f"{badge} {title}. {hook} {magnet} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}"
    
    print("=" * 70)
    print(f"🚀 XUẤT BẢN ĐỘC LẬP TẬP 3 (KẾT): {title}")
    print(f"📝 Caption: {caption}")
    print("=" * 70)
    
    # 1. Audit
    passed, report, metrics = VideoAuditEngine.audit_video_before_publish(
        video_path=vid_file,
        audio_path=audio_file if audio_file.exists() else None,
        title=title,
        prefix="VID_20261020_s01_slot_01_sadieu",
        part_num=3,
        caption=caption
    )
    print(report)
    if not passed:
        print("❌ Audit thất bại!")
        return False
        
    # 2. Upload
    success = upload_and_publish_video(
        video_path=vid_file,
        caption=caption,
        screenshot_prefix="20261020_slot_01_sadieu_part3",
        thumbnail_path=None
    )
    
    if success:
        status_file = ROOT / "data" / f"daily_schedule_status_{date_str}.json"
        if status_file.exists():
            status = json.loads(status_file.read_text(encoding="utf-8"))
            s_key = "20261020_slot_01_sadieu"
            if s_key in status:
                status[s_key]["part3"] = True
                status["_meta"]["last_published_timestamp"] = time.time()
                status["_meta"]["last_published_time_str"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                status["_meta"]["last_series_completed_timestamp"] = time.time()
                status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
                print("💾 Đã cập nhật status file: part3 = True, last_series_completed_timestamp updated!")
                
        try:
            AntiRepostGuard.register_successful_publish(
                title=title,
                caption=caption,
                video_path=vid_file,
                audio_path=audio_file if audio_file.exists() else None
            )
        except Exception:
            pass
            
        for f in [vid_file, audio_file, thumb_file]:
            if f.exists():
                try:
                    f.unlink()
                    print(f"🗑️ Đã xóa: {f.name}")
                except Exception:
                    pass
        print(f"\n🎉 HOÀN TẤT TRỌN VẸN 3 TẬP CỦA BỘ 1: {title}!")
        return True
    else:
        print("❌ Đăng bài thất bại!")
        return False

if __name__ == "__main__":
    main()
