# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_4_thriller_masterpieces.py
Quy Trình Tự Động Hóa Xuất Bản 4 Bộ Truyện Audio Kịch Tính & Nghẹt Thở (12 Video Full HD):
1. Bộ 1: Kỳ Án Biệt Thự Trăng Máu: Tiếng Gõ Cửa Lúc 2h Sáng (Nam Minh Neural 1.5x)
2. Bộ 2: Huyết Nguyện Lúc Nửa Đêm: Chiếc Gương Âm Dương Biệt Thự Cổ (Nam Minh Neural 1.5x)
3. Bộ 3: Nàng Dâu Thức Tỉnh: Đêm Mưa Bị Đuổi Khỏi Hào Môn (Hoài My Neural 1.5x)
4. Bộ 4: Mạt Thế Kỷ Băng Hà: Tôi Tích Trữ 100 Tỷ Vật Tư Xây Pháo Đài Ấm Áp (Nam Minh Neural 1.5x)

Lịch đăng tự động chuẩn mực:
- Cách 60 phút đăng 1 bộ (Mỗi tiếng bắt đầu 1 bộ mới).
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

STATUS_FILE = ROOT / "data" / "thriller_4series_publishing_status.json"

SERIES_METADATA = [
    {
        "key": "series1_trangmau",
        "prefix": "VID_masterpiece_3_trangmau",
        "title": "Kỳ Án Biệt Thự Trăng Máu: Tiếng Gõ Cửa Của Thám Tử Mất Tích",
        "genre_tag": "#trinhtham #kyan #hinhsu #phapan #huyennghi #audiotruyen",
        "hooks": [
            "Chiếc điện thoại bàn đứt dây bỗng đổ chuông lúc 2h sáng và lời cảnh báo của thám tử đã chết 5 năm.",
            "Mật mã hầm ngầm hé lộ hồ sơ giả mạo hiện trường của vị đội trưởng cảnh sát mẫu mực.",
            "Trọn bộ 3 tập đã lên sóng! Boong tàu bão táp và màn lật tẩy hung thủ thực sự sau 10 năm ẩn mình!"
        ],
        "magnets": [
            "👉 Cuộc gọi từ số máy của người đã khuất 5 năm trước, nếu là bạn bạn có dám nhấc máy? Bình luận 1 (Có) hay 2 (Sợ chạy mất dép) nhé!",
            "👉 Theo bạn kẻ phản bội thực sự là thám tử hay viên cảnh sát trưởng? Bình luận 1 hay 2!",
            "👉 Cái kết này có làm bạn bất ngờ không? Hãy để lại cảm nghĩ về chân tướng vụ án nhé!"
        ]
    },
    {
        "key": "series2_huyetnguyen",
        "prefix": "VID_masterpiece_4_huyetnguyen",
        "title": "Huyết Nguyện Lúc Nửa Đêm: Chiếc Gương Âm Dương Biệt Thự Cổ",
        "genre_tag": "#kinhdi #quaidam #tamlinh #nucuoi #audiotruyen #chuyenday",
        "hooks": [
            "Quy tắc cấm kỵ lúc nửa đêm: Tuyệt đối không được soi chiếc gương đồng phủ vải đỏ trong phòng ngủ.",
            "Bóng trắng bám chặt trần nhà và sự biến mất bí ẩn của gia đình chủ cũ 30 năm trước.",
            "Trọn bộ 3 tập đã lên sóng! Chiếc búa tạ đập vỡ gương quỷ giải thoát lời nguyền truyền kiếp!"
        ],
        "magnets": [
            "👉 Nửa đêm gương trong phòng bỗng tự phát ra tiếng thì thầm, bạn sẽ làm gì? Bình luận 1 (Bật đèn kiểm tra) hay 2 (Trùm chăn ngủ tiếp)!",
            "👉 Bạn có tin vào những quy tắc cấm kỵ tâm linh trong nhà cổ không? Bình luận 1 (Có) hoặc 2 (Mê tín) nhé!",
            "👉 Bạn thấy câu chuyện này rùng rợn ở thang điểm mấy từ 1 đến 10? Bình luận cho mình biết nhé!"
        ]
    },
    {
        "key": "series3_mechong",
        "prefix": "VID_masterpiece_2_mechong",
        "title": "Nàng Dâu Thức Tỉnh: Đêm Mưa Bị Đuổi Khỏi Hào Môn & Bản Lĩnh Tự Chủ 120 Tỷ",
        "genre_tag": "#mechong #giadau #haccuong #nuphucuong #audiotruyen #reviewtruyen",
        "hooks": [
            "Đêm mưa bão bị mẹ chồng đuổi khỏi nhà và sự xuất hiện chấn động của chiếc Rolls-Royce cứu vớt.",
            "Phiên đấu giá 120 tỷ mua đứt căn biệt thự ven sông và cú sụp đổ của gia tộc bội bạc.",
            "Trọn bộ 3 tập đã lên sóng! Nàng dâu thức tỉnh biến biệt thự 50 tỷ thành trung tâm bảo trợ!"
        ],
        "magnets": [
            "👉 Mẹ chồng đuổi nàng dâu đêm mưa vì không đẻ được con trai, đáng trách không? Bình luận 1 (Có) hay 2 (Quá tàn nhẫn)!",
            "👉 Bỏ ra 120 tỷ mua lại nhà của chồng cũ để trả thù, ngầu hay phí tiền? Bình luận 1 hoặc 2 nhé!",
            "👉 Bạn có ủng hộ việc phụ nữ tự chủ tài chính để không bị khinh thường không? Bình luận quan điểm nhé!"
        ]
    },
    {
        "key": "series4_matthe",
        "prefix": "VID_horror_4_chuyentau",
        "title": "Mạt Thế Kỷ Băng Hà: Tôi Tích Trữ 100 Tỷ Vật Tư Xây Pháo Đài Ấm Áp",
        "genre_tag": "#matthe #kybangha #tichtru #sinhton #vohanluu #audiotruyen",
        "hooks": [
            "Nhiệt độ hạ xuống âm 65 độ C, tôi ngồi trong pháo đài ấm áp tích trữ 100 tỷ xem hàng xóm cực phẩm gõ cửa van xin.",
            "Bão tuyết càn quét toàn thành phố, bóc trần bản chất tàn nhẫn của đám người từng cướp đoạt kiếp trước.",
            "Trọn bộ 3 tập đã lên sóng! Pháo đài bất khả xâm phạm và trật tự sinh tồn mới nơi tận thế!"
        ],
        "magnets": [
            "👉 Nếu biết trước tận thế băng giá sắp đến trong 30 ngày, bạn sẽ tích trữ món đồ gì đầu tiên? Bình luận ngay nhé!",
            "👉 Hàng xóm từng hại mình kiếp trước nay đến quỳ xin đồ ăn, bạn có mở cửa không? Bình luận 1 (Không) hay 2 (Cho ít đồ thừa)!",
            "👉 Cảm giác nhìn kẻ ác phải trả giá trong băng giá có thỏa mãn không? Để lại cảm nghĩ nhé!"
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
    return f"{badge} {title}. {hook} {magnet} #audio #xuhuong #kểchuyện #podcast #fyp #tamtrang {tag}"

def run_schedule(interval_parts_min: int = 20, interval_series_min: int = 60, reset: bool = False):
    out_dir = ROOT / "assets" / "output"
    if reset and STATUS_FILE.exists():
        STATUS_FILE.unlink(missing_ok=True)
        print("🔄 Đã reset trạng thái xuất bản 4 bộ thriller!")

    status = load_status()

    if "base_time" not in status:
        status["base_time"] = time.time()
        save_status(status)
    base_time = float(status["base_time"])

    interval_parts_sec = interval_parts_min * 60
    interval_series_sec = interval_series_min * 60

    print("=" * 75)
    print("🚀 [LỊCH TRÌNH TỰ ĐỘNG] XUẤT BẢN 4 BỘ TRUYỆN AUDIO KỊCH TÍNH & NGHẸT THỞ")
    print(f"⏰ Bắt đầu lúc: {datetime.fromtimestamp(base_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Quy luật: Cách {interval_series_min} phút đăng 1 bộ mới. Trong mỗi bộ, 3 tập cách nhau {interval_parts_min} phút.")
    print("=" * 75)

    for s_idx, conf in enumerate(SERIES_METADATA):
        s_key = conf["key"]
        s_title = conf["title"]
        s_start_time = base_time + s_idx * interval_series_sec

        print(f"\n" + "#" * 65)
        print(f"🎬 BỘ {s_idx + 1}/4: {s_title}")
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
    print("🏆 TOÀN BỘ 4 BỘ AUDIO KỊCH TÍNH & NGHẸT THỞ (12 VIDEO) ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 75)

def main():
    parser = argparse.ArgumentParser(description="Auto Scheduler for 4 Thriller Masterpieces")
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
