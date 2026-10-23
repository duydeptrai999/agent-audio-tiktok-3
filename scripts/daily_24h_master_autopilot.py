# -*- coding: utf-8 -*-
"""
scripts/daily_24h_master_autopilot.py
Hệ Thống Tự Động Hóa Vận Hành 24/7/365 Xuất Bản 10 Bộ Audio Mới Mỗi Ngày (30 Video Full HD):
- Chạy ngầm vĩnh viễn (Infinite Autonomous Daemon).
- Tự động chuyển ngày, tự động sinh 10 bộ truyện mới mỗi ngày.
- 10 khung giờ rải đều cả ngày, 3 khung giờ đêm chuyên trị Kinh Dị / Quái Đàm / Trinh Thám.
- Bảo vệ giãn cách: 20 phút/tập, nghỉ tối thiểu 80 phút giữa 2 bộ.
- Xóa sạch video/audio ngay sau khi đăng thành công (Zero Footprint).
"""

import os
import sys
import time
import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

DATA_DIR = ROOT / "data"
LOG_FILE = DATA_DIR / "autopilot_247.log"

class RobustLoggerTee:
    def __init__(self, target_stream, log_path: Path):
        self.stream = target_stream
        self.log_path = log_path
        self.log_file = None
        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            self.log_file = open(self.log_path, "a", encoding="utf-8", buffering=1)
        except Exception:
            pass

    def write(self, msg):
        if self.stream:
            try:
                self.stream.write(msg)
                self.stream.flush()
            except Exception:
                pass
        if self.log_file:
            try:
                self.log_file.write(msg)
                self.log_file.flush()
            except Exception:
                pass

    def flush(self):
        if self.stream:
            try:
                self.stream.flush()
            except Exception:
                pass
        if self.log_file:
            try:
                self.log_file.flush()
            except Exception:
                pass

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
        sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass

sys.stdout = RobustLoggerTee(sys.stdout, LOG_FILE)
sys.stderr = RobustLoggerTee(sys.stderr, LOG_FILE)

from core.audio_engine import generate_cinema_tts_audio
from core.ffmpeg_utils import render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME
from scripts.tiktok_publisher_core import upload_and_publish_video
from core.daily_schedule_config import (
    DAILY_10_SLOTS,
    INTERVAL_PARTS_SECONDS,
    MIN_SERIES_REST_SECONDS,
    PLANNED_SERIES_REST_SECONDS
)
from core.stories.daily_story_factory import get_daily_10_series
from core.stories.script_quality_gate import validate_story_series
from core.anti_repost_guard import AntiRepostGuard
from core.video_audit_engine import VideoAuditEngine

DATA_DIR = ROOT / "data"
AUDIO_DIR = ROOT / "assets" / "audio"
OUTPUT_DIR = ROOT / "assets" / "output"
THUMB_DIR = ROOT / "assets" / "thumbnails"
SCRIPTS_DIR = DATA_DIR / "generated_scripts"

for d in [DATA_DIR, AUDIO_DIR, OUTPUT_DIR, THUMB_DIR, SCRIPTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def get_status_file(date_str: str) -> Path:
    return DATA_DIR / f"daily_schedule_status_{date_str}.json"

def load_daily_status(date_str: str, series_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    status_file = get_status_file(date_str)
    default_status = {
        "_meta": {
            "date": date_str,
            "last_published_timestamp": 0.0,
            "last_published_time_str": "",
            "last_series_completed_timestamp": 0.0
        }
    }
    for s in series_list:
        default_status[s["key"]] = {
            "slot_index": s["slot_index"],
            "title": s["title"],
            "part1": False,
            "part2": False,
            "part3": False,
            "produced": False
        }
    if status_file.exists():
        try:
            saved = json.loads(status_file.read_text(encoding='utf-8'))
            for k, v in default_status.items():
                if k not in saved:
                    saved[k] = v
                elif isinstance(v, dict) and isinstance(saved[k], dict):
                    if not saved[k].get("produced", False) and "title" in v:
                        saved[k]["title"] = v["title"]
                    for sub_k, sub_v in v.items():
                        if sub_k not in saved[k]:
                            saved[k][sub_k] = sub_v
            return saved
        except Exception:
            pass
    return default_status

def save_daily_status(date_str: str, status: Dict[str, Any]):
    status_file = get_status_file(date_str)
    status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def produce_single_series(series_data: Dict[str, Any], status: Dict[str, Any], date_str: str):
    """Sản xuất 3 tập video của 1 bộ truyện nếu chưa có."""
    s_key = series_data["key"]
    prefix = series_data["prefix"]

    # Kiểm tra xem các tập chưa đăng có đầy đủ file video chưa
    all_needed_exist = True
    for part in series_data.get("parts", []):
        p_num = part["part_number"]
        if not status.get(s_key, {}).get(f"part{p_num}", False):
            p_vid = OUTPUT_DIR / f"{prefix}_part{p_num}_final.mp4"
            if not p_vid.exists() or p_vid.stat().st_size < 500000:
                all_needed_exist = False
                break

    if status.get(s_key, {}).get("produced", False) and all_needed_exist:
        return

    # Master Quality Gate: Đọc quy chuẩn GEMINI.md & thẩm định kịch bản trước khi sản xuất audio
    series_data = validate_story_series(series_data)

    prefix = series_data["prefix"]
    title = series_data["title"]
    voice = series_data.get("voice", "vi-VN-HoaiMyNeural")
    bgm_genre = series_data.get("bgm_genre", "ROMANCE")
    bgm_file = "" if str(bgm_genre).upper() in ["NONE", "NO_BGM", "OFF", ""] else get_safe_bgm_for_genre(bgm_genre)

    print(f"\n🎬 [SẢN XUẤT] Bắt đầu dựng {title} (Slot {series_data['slot_index']}/10)...")
    
    # Lưu kịch bản
    script_file = SCRIPTS_DIR / f"{prefix}.json"
    if not script_file.exists():
        script_file.write_text(json.dumps(series_data, indent=2, ensure_ascii=False), encoding='utf-8')

    for part in series_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        part_audio = AUDIO_DIR / f"{prefix}_part{p_num}_15x.mp3"
        part_video = OUTPUT_DIR / f"{prefix}_part{p_num}_final.mp4"
        part_thumb = THUMB_DIR / f"{prefix}_part{p_num}_thumb.jpg"

        # 1. Audio TTS 1.5x
        if not part_audio.exists() or part_audio.stat().st_size < 10000:
            print(f"  🎙️ Đang sinh audio {voice} cho Tập {p_num}...")
            asyncio.run(generate_cinema_tts_audio(
                text=part["text"],
                voice=voice,
                output_path=part_audio,
                target_speed=1.50
            ))

        if part_video.exists() and part_video.stat().st_size > 500000:
            print(f"  ⏭️ Tập {p_num} đã có sẵn video thành phẩm, bỏ qua render.")
            continue

        # 2. B-Roll slice
        probe = probe_media_file(part_audio)
        dur = probe.get("duration", 300.0)
        slice_path = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        # 3. Thumbnail
        if not part_thumb.exists() or part_thumb.stat().st_size < 5000:
            try:
                generate_part_thumbnail(
                    source_video_or_image=slice_path,
                    output_thumb_path=part_thumb,
                    story_title=title,
                    part_label=f"TẬP {p_num}",
                    genre_tag=f"#{series_data.get('genre', 'AudioTruyện')}"
                )
            except Exception:
                pass

        # 4. Video MP4 1080p (Bao gồm Title Banner nổi bật 0.5s đầu, TUYỆT ĐỐI KHÔNG BẬT PHỤ ĐỀ)
        print(f"  🎥 Đang render video 1080p cho Tập {p_num}...")
        render_playable_video(
            output_file=part_video,
            voice_audio_path=str(part_audio),
            clean_footage_path=str(slice_path),
            bgm_audio_path=str(bgm_file),
            badge_label=badge,
            bgm_volume=BGM_VOLUME if bgm_file else 0.0,
            voice_volume=VOICE_VOLUME,
            enable_subtitles=False,
            thumbnail_path=None,  # Độc lập, không nhúng attached_pic
            title_text=title
        )

    status[s_key]["produced"] = True
    save_daily_status(date_str, status)
    print(f"  ✅ Đã sẵn sàng trọn vẹn 3 tập của: {title}!")

def wait_until(target_timestamp: float, label: str):
    now = time.time()
    if target_timestamp <= now:
        return
    diff = int(target_timestamp - now)
    print(f"\n⏳ [{datetime.now().strftime('%H:%M:%S')}] Chờ đến mốc đăng {label} (còn {diff // 3600}h {(diff % 3600) // 60}m {diff % 60}s)...", flush=True)
    last_print = time.time()
    while time.time() < target_timestamp:
        remaining = int(target_timestamp - time.time())
        if (time.time() - last_print >= 30) or remaining <= 10:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Còn {remaining // 3600}h {(remaining % 3600) // 60}m {remaining % 60}s tới mốc {label}...", flush=True)
            last_print = time.time()
        time.sleep(min(2, max(0.5, remaining)))

def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    title = series_conf["title"]
    part_custom_caption = ""
    for p in series_conf.get("parts", []):
        if p.get("part_number") == part_num:
            part_custom_caption = (p.get("caption") or "").strip()
            break
    if part_custom_caption and len(part_custom_caption) > 15:
        desc = part_custom_caption
    else:
        hooks = series_conf.get("hooks", [])
        magnets = series_conf.get("magnets", [])
        hook = hooks[min(part_num - 1, len(hooks) - 1)] if hooks else ""
        magnet = magnets[min(part_num - 1, len(magnets) - 1)] if magnets else ""
        desc = f"{hook} {magnet}".strip()
    tag = series_conf.get("genre_tag", "#audiotruyen #podcast #fyp")
    return f"{badge} {title}. {desc} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}".strip()

def run_one_day_cycle(target_date: str = ""):
    """Vận hành trọn vẹn chu kỳ 10 bộ truyện trong 1 ngày."""
    if not target_date:
        target_date = datetime.now().strftime("%Y-%m-%d")

    now = datetime.now()
    series_list = get_daily_10_series(target_date)
    status = load_daily_status(target_date, series_list)

    print("=" * 85)
    print(f"🚀 [24/7 AUTOPILOT] KÍCH HOẠT LỊCH TRÌNH 10 BỘ AUDIO MỚI CHO NGÀY: {target_date}")
    print(f"⏰ Thời điểm khởi động: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📋 Quy mô: 10 Bộ Truyện x 3 Tập = 30 Video 1080p | Giãn cách: 20p/tập, nghỉ 65p giữa 2 bộ")
    print(f"🌙 Ban đêm (19h20, 21h10, 23h00): Trinh Thám Kỳ Án, Quy Tắc Quái Đàm & Kinh Dị Rùng Rợn | Xong trước 0h")
    print("=" * 85)

    base_day = datetime.strptime(target_date, "%Y-%m-%d")

    for s_idx, conf in enumerate(series_list):
        s_key = conf["key"]
        s_title = conf["title"]
        prefix = conf["prefix"]
        slot_num = conf["slot_index"]
        h = conf["hour"]
        m = conf["minute"]

        # Xử lý slot thời gian trong ngày (tất cả 10 slot từ 06:30 đến 23:00 đều hoàn tất trước 0h)
        if h < 5:
            scheduled_start_dt = (base_day + timedelta(days=1)).replace(hour=h, minute=m, second=0, microsecond=0)
        else:
            scheduled_start_dt = base_day.replace(hour=h, minute=m, second=0, microsecond=0)

        s_start_ts = scheduled_start_dt.timestamp()

        # 🛡️ BẢO VỆ NGUYÊN TẮC: Nghỉ tối thiểu 60-80 phút sau khi kết thúc bộ trước
        last_series_comp = status["_meta"].get("last_series_completed_timestamp", 0.0)
        if last_series_comp > 0:
            min_series_start = last_series_comp + MIN_SERIES_REST_SECONDS
            if s_start_ts < min_series_start:
                s_start_ts = min_series_start

        # Kiểm tra xem bộ này đã xong cả 3 tập chưa
        if all(status[s_key].get(f"part{i}", False) for i in [1, 2, 3]):
            print(f"\n✅ Bộ {slot_num}/10 ({s_title}) đã hoàn tất xuất bản trước đó. Bỏ qua.")
            continue

        # Sản xuất video trước cho bộ này nếu chưa có
        produce_single_series(conf, status, target_date)

        print(f"\n" + "#" * 70)
        print(f"🎬 BỘ {slot_num}/10: {s_title} ({conf['genre']})")
        print(f"⏰ Dự kiến bắt đầu: {datetime.fromtimestamp(s_start_ts).strftime('%H:%M:%S')} | Giọng: {conf['voice']}")
        print("#" * 70)

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_start_ts + (p_idx - 1) * INTERVAL_PARTS_SECONDS

            # 🛡️ BẢO VỆ TUYỆT ĐỐI GIAO THỨC 20 PHÚT: Cách tập trước ít nhất 1.200 giây
            last_pub = status["_meta"].get("last_published_timestamp", 0.0)
            if last_pub > 0:
                min_safe_ts = last_pub + INTERVAL_PARTS_SECONDS
                if target_ts < min_safe_ts:
                    target_ts = min_safe_ts

            wait_until(target_ts, f"Bộ {slot_num} - Tập {p_idx}")

            vid_file = OUTPUT_DIR / f"{prefix}_part{p_idx}_final.mp4"
            part_thumb_file = THUMB_DIR / f"{prefix}_part{p_idx}_thumb.jpg"
            part_audio_file = AUDIO_DIR / f"{prefix}_part{p_idx}_15x.mp3"

            if not vid_file.exists() or vid_file.stat().st_size < 500000:
                print(f"⚠️ Chưa có video hoặc file lỗi: {vid_file.name}. Dựng lại ngay...")
                produce_single_series(conf, status, target_date)

            if not vid_file.exists():
                print(f"❌ Không tìm thấy video: {vid_file.name}. Bỏ qua...")
                continue

            caption = get_caption_for_part(conf, p_idx)

            # 🛡️ KIỂM DUYỆT TOÀN DIỆN MASTER AUDIT (Hình ảnh Full HD, Âm thanh đủ tiếng & Chống lặp lại audio cũ)
            print(f"\n🔍 [PRE-PUBLISH MASTER AUDIT] Bắt đầu thẩm định chất lượng: {vid_file.name}...")
            is_audit_passed, audit_report, metrics = VideoAuditEngine.audit_video_before_publish(
                video_path=vid_file,
                audio_path=part_audio_file,
                title=conf["title"],
                prefix=prefix,
                part_num=p_idx,
                caption=caption
            )
            print(audit_report)
            if not is_audit_passed:
                print(f"🚨 [AUDIT THẤT BẠI] HỦY BỎ ĐĂNG VIDEO NÀY ĐỂ BẢO VỆ CHẤT LƯỢNG KÊNH!")
                continue

            upload_success = False
            for attempt in range(1, 4):
                print(f"\n📲 Đang tải lên TikTok Studio: {vid_file.name} (Lần thử {attempt}/3)...")
                try:
                    clean_series_title = s_title.split(":")[0].strip() if ":" in s_title else s_title
                    playlist_title = f"[TRỌN BỘ] {clean_series_title}"[:30]
                    upload_success = upload_and_publish_video(
                        video_path=vid_file,
                        caption=caption,
                        screenshot_prefix=f"{s_key}_{p_key}",
                        thumbnail_path=part_thumb_file if part_thumb_file.exists() else None,
                        playlist_name=playlist_title,
                        enable_auto_captions=False
                    )
                except Exception as ue:
                    print(f"  ⚠️ Lỗi khi đăng: {ue}")
                    upload_success = False

                if upload_success:
                    status[s_key][p_key] = True
                    status["_meta"]["last_published_timestamp"] = time.time()
                    status["_meta"]["last_published_time_str"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_daily_status(target_date, status)
                    print(f"🎉 ĐÃ XUẤT BẢN THÀNH CÔNG: {s_key} - {p_key} lúc {datetime.now().strftime('%H:%M:%S')}!")

                    # Đăng ký vào registry
                    try:
                        AntiRepostGuard.register_successful_publish(
                            title=conf["title"],
                            prefix=prefix,
                            part_num=p_idx,
                            audio_path=part_audio_file,
                            video_path=vid_file
                        )
                    except Exception:
                        pass

                    # 🧹 XÓA FILE TỨC THÌ (Zero Footprint)
                    if vid_file.exists():
                        vid_file.unlink(missing_ok=True)
                        print(f"  🗑️ Đã xóa video: {vid_file.name}")
                    if part_audio_file.exists():
                        part_audio_file.unlink(missing_ok=True)
                        print(f"  🗑️ Đã xóa audio: {part_audio_file.name}")
                    if part_thumb_file.exists():
                        part_thumb_file.unlink(missing_ok=True)
                        print(f"  🗑️ Đã xóa thumbnail: {part_thumb_file.name}")
                    break
                else:
                    time.sleep(15)

            if not upload_success:
                print(f"❌ CẢNH BÁO: Đăng {s_key} - {p_key} thất bại sau 3 lần thử!")

        # 🧹 Khi đăng trọn vẹn cả 3 tập của bộ -> Xóa kịch bản JSON & Cập nhật mốc nghỉ
        all_parts_posted = all(status[s_key].get(f"part{i}", False) for i in [1, 2, 3])
        if all_parts_posted:
            status["_meta"]["last_series_completed_timestamp"] = time.time()
            save_daily_status(target_date, status)
            script_json_file = SCRIPTS_DIR / f"{prefix}.json"
            if script_json_file.exists():
                script_json_file.unlink(missing_ok=True)
                print(f"  🗑️ Đã xóa kịch bản JSON của bộ: {script_json_file.name}")

        print(f"\n🎉 HOÀN TẤT BỘ {slot_num}/10: {s_title}!")

    print("\n" + "=" * 85)
    print(f"🏆 CHU KỲ 10 BỘ AUDIO NGÀY {target_date} ĐÃ HOÀN THÀNH TOÀN BỘ!")
    print("=" * 85)

def get_current_broadcast_date() -> str:
    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    yesterday_str = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Nếu đang ở rạng sáng (0h - 5h) nhưng hôm qua đã hoàn thành trọn vẹn 10 bộ, chuyển sang ngày hôm nay ngay
    if now.hour < 5:
        yesterday_file = get_status_file(yesterday_str)
        if yesterday_file.exists():
            try:
                y_status = json.loads(yesterday_file.read_text(encoding='utf-8'))
                completed_count = sum(1 for k, v in y_status.items() if isinstance(v, dict) and v.get("part1") and v.get("part2") and v.get("part3"))
                if completed_count >= 10:
                    return today_str
            except Exception:
                pass
        return yesterday_str
    return today_str

def run_247_infinite_autopilot():
    """Hàm chạy vĩnh viễn không dừng 24/7/365."""
    print("🌟 KÍCH HOẠT HỆ THỐNG VẬN HÀNH 24/7 TỰ ĐỘNG HÓA VĨNH VIỄN 🌟")
    while True:
        b_date_str = get_current_broadcast_date()
        all_done = False
        try:
            run_one_day_cycle(b_date_str)
            all_done = True
        except Exception as e:
            print(f"⚠️ Ngoại lệ trong chu kỳ ngày {b_date_str}: {e}")
            time.sleep(30)
            continue

        # Chỉ ngủ nghỉ khi toàn bộ 10 bộ của ngày phát sóng đã hoàn tất trọn vẹn
        if all_done:
            now = datetime.now()
            if now.hour < 6:
                next_6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
            else:
                next_6am = (now + timedelta(days=1)).replace(hour=6, minute=0, second=0, microsecond=0)

            seconds_to_wait = int((next_6am - now).total_seconds())
            if seconds_to_wait > 0:
                print(f"\n💤 [NGỦ NGHỈ ĐÊM] Hệ thống tạm nghỉ {seconds_to_wait // 3600}h {(seconds_to_wait % 3600) // 60}m tới 06:00 sáng để bắt đầu ngày mới...")
                time.sleep(seconds_to_wait)
            else:
                time.sleep(60)

def acquire_process_lock():
    PID_FILE = DATA_DIR / "autopilot.pid"
    if PID_FILE.exists():
        try:
            old_pid = int(PID_FILE.read_text(encoding='utf-8').strip())
            import psutil
            if psutil.pid_exists(old_pid) and old_pid != os.getpid():
                proc = psutil.Process(old_pid)
                if "python" in proc.name().lower():
                    print(f"⚠️ [PID Lock] Autopilot đang chạy ngầm với PID {old_pid}. Dừng phiên bản trùng lặp.")
                    sys.exit(0)
        except Exception:
            pass
    PID_FILE.write_text(str(os.getpid()), encoding='utf-8')

def main():
    acquire_process_lock()
    parser = argparse.ArgumentParser(description="24/7 Master Autopilot: 10 Audio Series Daily")
    parser.add_argument("--once", action="store_true", help="Chỉ chạy chu kỳ của ngày hôm nay rồi dừng")
    parser.add_argument("--date", type=str, default="", help="Chạy ngày cụ thể YYYY-MM-DD")
    args = parser.parse_args()

    if args.once:
        run_one_day_cycle(args.date)
    else:
        run_247_infinite_autopilot()

if __name__ == "__main__":
    main()
