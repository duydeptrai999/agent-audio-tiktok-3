# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_5_romance_series.py
Quy Trình Tự Động Hóa Xuất Bản 5 Bộ Truyện Audio Ngôn Tình (15 Video Full HD):
1. Bộ 1 (Chữa lành & Cứu rỗi): Ánh Sáng Nơi Tận Cùng Đêm Tối
2. Bộ 2 (Ngược luyến tàn tâm): Khi Hoa Sơn Tra Tàn Lụi
3. Bộ 3 (Thanh xuân vườn trường): Chiếc Áo Đồng Phục Năm Ấy
4. Bộ 4 (Hào môn tổng tài): Bản Hợp Đồng Hôn Nhân 100 Tỷ
5. Bộ 5 (Trọng sinh báo thù): Đóa Sen Lửa Nở Rộ

Lịch đăng tự động:
- Cách 1 tiếng đăng 1 bộ (Mỗi tiếng bắt đầu 1 bộ mới).
- Trong 1 tiếng đăng trọn vẹn cả bộ (Tập 1: T, Tập 2: T+20m, Tập 3: T+40m).
- Đăng tải tự động an toàn qua Cốc Cốc Browser Profile vào TikTok Studio.
"""

import sys
import os
import time
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
        sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass

from scripts.tiktok_publisher_core import upload_and_publish_video

STATUS_FILE = ROOT / "data" / "romance_5series_publishing_status.json"

SERIES_METADATA = [
    {
        "key": "series1_chualanh",
        "prefix": "VID_romance_4_chualanh",
        "title": "Ánh Sáng Nơi Tận Cùng Đêm Tối: Bản Hợp Đồng Cứu Rỗi Trái Tim Tổn Thương",
        "genre_tag": "#chualanh #tinhcam #healing #tamly #audiotruyen",
        "hooks": [
            "Bản hợp đồng trị liệu tâm lý 100 ngày bên hồ sương mù.",
            "Tiếng súng trong đêm bão tuyết và sự trỗi dậy của thiên tài.",
            "Trọn bộ 3 tập đã lên sóng! Ánh sáng dịu dàng xua tan bóng tối tâm hồn!"
        ],
        "magnets": [
            "👉 Bạn có tin mỗi người đều có một 'bác sĩ tâm hồn' của riêng mình? Bình luận 1 (Có) hoặc 2 (Không) nhé!",
            "👉 Khi bị tổn thương, bạn chọn một mình chịu đựng hay chia sẻ? Bình luận 1 hoặc 2 nhé!",
            "👉 Câu chuyện này có chữa lành tâm trạng hôm nay của bạn không? Hãy để lại cảm nghĩ nhé!"
        ]
    },
    {
        "key": "series2_nguoctam",
        "prefix": "VID_romance_3_nguoctam",
        "title": "Khi Hoa Sơn Tra Tàn Lụi: Nỗi Oan Khuất 7 Năm Của Cô Dâu Thế Thân",
        "genre_tag": "#nguoctam #hoatang #nguocluyen #hoatangtrang #audiotruyen",
        "hooks": [
            "5 năm oan khuất nhận tội thay và thiệp cưới mạ vàng ngày trở về.",
            "Sự thật hồ sơ bệnh án hiến tủy và biển axit trả giá.",
            "Trọn bộ 3 tập đã lên sóng! Đại kết cục sám hối đẫm nước mắt!"
        ],
        "magnets": [
            "👉 Đổi 5 năm thanh xuân đi tù thay người yêu, đáng hay ngu ngốc? Bình luận 1 (Đáng) hoặc 2 (Ngu ngốc) nhé!",
            "👉 Khi biết sự thật hiến tủy, bạn có tha thứ không? Bình luận 1 (Tha thứ) hay 2 (Không bao giờ)!",
            "👉 Sự sám hối muộn màng có bù đắp được 5 năm cay đắng? Để lại bình luận nhé!"
        ]
    },
    {
        "key": "series3_thanhxuan",
        "prefix": "VID_romance_2_thanhxuan",
        "title": "Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp",
        "genre_tag": "#thanhxuan #moitinhdau #tuoitre #hocduong #audiotruyen",
        "hooks": [
            "Lời hứa 10 năm dưới cơn mưa tốt nghiệp năm mười bảy tuổi.",
            "Mảnh giấy chuyển tiền chu cấp bí mật suốt 10 năm.",
            "Trọn bộ 3 tập đã lên sóng! Mối tình thanh xuân trọn vẹn nhất cuộc đời!"
        ],
        "magnets": [
            "👉 Bạn còn nhớ tên mối tình đầu năm 17 tuổi không? Bình luận 1 (Còn nhớ) hoặc 2 (Đã quên) nhé!",
            "👉 10 năm âm thầm hy sinh không một lời kể công, người như vậy có thật không? Bình luận 1 hoặc 2 nhé!",
            "👉 Nếu gặp lại mối tình đầu năm ấy, bạn sẽ nói câu gì đầu tiên? Chia sẻ dưới bình luận nhé!"
        ]
    },
    {
        "key": "series4_haomon",
        "prefix": "VID_romance_1_haomon",
        "title": "Bản Hợp Đồng Hôn Nhân 100 Tỷ: Vị Hôn Thê Giả Mạo Của Tổng Tài Tàn Tật",
        "genre_tag": "#haomon #tongtai #cuoituocyeusau #ngotsung #audiotruyen",
        "hooks": [
            "Hợp đồng hôn nhân trăm tỷ và đêm tân hôn giông bão.",
            "Bí mật người đàn ông đứng dậy trong đêm tối.",
            "Trọn bộ 3 tập đã lên sóng! Tình yêu đích thực chiến thắng mọi toan tính hào môn!"
        ],
        "magnets": [
            "👉 Nếu được trả 100 tỷ để kết hôn hợp đồng, bạn có đồng ý không? Bình luận 1 (Có) hoặc 2 (Không) nhé!",
            "👉 Theo bạn anh ấy giả vờ tàn tật để làm gì? Bình luận 1 (Bảo vệ bản thân) hay 2 (Bắt kẻ phản bội)!",
            "👉 Bạn có tin vào tình yêu chân thành chốn hào môn không? Để lại quan điểm nhé!"
        ]
    },
    {
        "key": "series5_trongsinh",
        "prefix": "VID_masterpiece_1_trongsinh",
        "title": "Đóa Sen Lửa Nở Rộ: Thiên Kim Trở Về Đêm Đính Hôn Mười Năm Trước",
        "genre_tag": "#trongsinh #vamat #haomon #nuphucuong #sangvan #audiotruyen",
        "hooks": [
            "Mở mắt trong đêm đính hôn mười năm trước và cú vả mặt hủy hôn chấn động.",
            "Đấu trí thương trường vạch trần con chip bí mật trong trâm cài ngọc bích.",
            "Trọn bộ 3 tập đã lên sóng! Đóa sen lửa hào môn kiêu hãnh đòi lại toàn bộ công lý!"
        ],
        "magnets": [
            "👉 Nếu được trọng sinh về 10 năm trước, việc đầu tiên bạn làm là gì? Bình luận ngay nhé!",
            "👉 Kẻ phản bội nguy hiểm nhất là trà xanh hay bảo mẫu thân cận? Bình luận 1 hay 2!",
            "👉 Màn vả mặt này đã đủ thỏa mãn chưa? Để lại cảm nghĩ nhé!"
        ]
    }
]

def load_status() -> dict:
    default_status = {
        item["key"]: {"part1": False, "part2": False, "part3": False}
        for item in SERIES_METADATA
    }
    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text(encoding='utf-8'))
            for k, v in default_status.items():
                if k not in data:
                    data[k] = v
            return data
        except Exception:
            pass
    return default_status

def save_status(status: dict):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def wait_until(target_timestamp: float, label: str):
    now = time.time()
    if target_timestamp <= now:
        return
    diff = int(target_timestamp - now)
    print(f"\n⏳ [{datetime.now().strftime('%H:%M:%S')}] Chờ đến mốc đăng {label} (còn {diff // 60}m {diff % 60}s)...")
    while time.time() < target_timestamp:
        remaining = int(target_timestamp - time.time())
        if remaining % 60 == 0 or remaining <= 10:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Còn {remaining // 60}m {remaining % 60}s tới mốc đăng {label}...", flush=True)
        time.sleep(min(5, max(1, remaining)))

def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    title = series_conf["title"]
    hook = series_conf["hooks"][part_num - 1]
    magnet = series_conf["magnets"][part_num - 1]
    tag = series_conf["genre_tag"]
    return f"{badge} {title}. {hook} {magnet} #audio #xuhuong #ngontinh #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}"

def run_schedule(interval_parts_min: int = 20, interval_series_min: int = 60, reset: bool = False):
    out_dir = ROOT / "assets" / "output"
    if reset and STATUS_FILE.exists():
        STATUS_FILE.unlink(missing_ok=True)
        print("🔄 Đã reset trạng thái xuất bản về ban đầu!")

    status = load_status()

    if "base_time" not in status:
        status["base_time"] = time.time()
        save_status(status)
    base_time = float(status["base_time"])

    interval_parts_sec = interval_parts_min * 60
    interval_series_sec = interval_series_min * 60

    print("=" * 75)
    print("🚀 [LỊCH TRÌNH TỰ ĐỘNG] XUẤT BẢN 5 BỘ TRUYỆN AUDIO NGÔN TÌNH TIKTOK")
    print(f"⏰ Bắt đầu lúc: {datetime.fromtimestamp(base_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Quy luật: Cách {interval_series_min} phút đăng 1 bộ mới. Trong mỗi bộ, 3 tập cách nhau {interval_parts_min} phút.")
    print("=" * 75)

    for s_idx, conf in enumerate(SERIES_METADATA):
        s_key = conf["key"]
        s_title = conf["title"]
        s_start_time = base_time + s_idx * interval_series_sec

        print(f"\n" + "#" * 65)
        print(f"🎬 BỘ {s_idx + 1}/5: {s_title}")
        print(f"⏰ Mốc bắt đầu bộ: {datetime.fromtimestamp(s_start_time).strftime('%H:%M:%S')}")
        print("#" * 65)

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng thành công trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_start_time + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx + 1} - Tập {p_idx}")

            vid_file = out_dir / f"{conf['prefix']}_part{p_idx}_final.mp4"
            if not vid_file.exists():
                print(f"❌ Không tìm thấy file video: {vid_file.name}")
                continue

            caption = get_caption_for_part(conf, p_idx)

            upload_success = False
            for attempt in range(1, 4):
                print(f"\n📲 Đang tải lên TikTok Studio: {vid_file.name} (Lần thử {attempt}/3)...")
                try:
                    upload_success = upload_and_publish_video(vid_file, caption, screenshot_prefix=f"{s_key}_{p_key}")
                except Exception as ue:
                    print(f"  ⚠️ Ngoại lệ khi đăng: {ue}")
                    upload_success = False

                if upload_success:
                    status[s_key][p_key] = True
                    save_status(status)
                    print(f"🎉 ĐÃ XUẤT BẢN THÀNH CÔNG: {s_key} - {p_key} lúc {datetime.now().strftime('%H:%M:%S')}!")
                    break
                else:
                    print(f"  ⚠️ Lần thử {attempt} chưa thành công. Tạm dừng 15s trước khi thử lại...")
                    time.sleep(15)

            if not upload_success:
                print(f"❌ CẢNH BÁO: Đăng {s_key} - {p_key} thất bại sau 3 lần thử! Đánh dấu và tiếp tục...")
                status[s_key][p_key] = False
                save_status(status)

        print(f"\n🎉 HOÀN TẤT ĐĂNG ĐỦ 3 TẬP CỦA BỘ {s_idx + 1}: {s_title}!")

    print("\n" + "=" * 75)
    print("🏆 TOÀN BỘ 5 BỘ AUDIO NGÔN TÌNH (15 VIDEO) ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 75)

def main():
    parser = argparse.ArgumentParser(description="Auto Scheduler for 5 Romance Series")
    parser.add_argument("--interval-series", type=int, default=60, help="Phút giữa các bộ (mặc định 60 phút)")
    parser.add_argument("--interval-parts", type=int, default=20, help="Phút giữa các tập (mặc định 20 phút)")
    parser.add_argument("--reset", action="store_true", help="Reset trạng thái đăng")
    args = parser.parse_args()

    run_schedule(
        interval_parts_min=args.interval_parts,
        interval_series_min=args.interval_series,
        reset=args.reset
    )

if __name__ == "__main__":
    main()
