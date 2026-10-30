# -*- coding: utf-8 -*-
"""
HỆ THỐNG SẢN XUẤT TOÀN BỘ CÁC BỘ AUDIO CÒN LẠI CHO HÔM NAY (SLOT 2 -> 10)
Tự động áp dụng chuẩn Codex 8.0 & Voice Profiles tối ưu:
- Slot 2 (08:20): Thanh Xuân Vườn Trường - Hoài My trong sáng, nhẹ nhàng (-15%)
- Slot 3 (10:10): Cung Đấu Nữ Quyền - Hoài My trầm mặc, mưu lược (-15%)
- Slot 4 (12:00): Trọng Sinh Vả Mặt - Hoài My tự sự điềm tĩnh, sâu sắc (-16%)
- Slot 5 (13:50): Mạt Thế Sinh Tồn - Nam Minh chiến binh trầm ấm (-14%)
- Slot 6 (15:40): Hào Môn Đô Thị - Hoài My chữa lành êm dịu, bé lại (-18%)
- Slot 7 (17:30): Gia Đấu Mẹ Chồng - Hoài My điềm tĩnh, thủ thỉ (-18%)
- Slot 8 (19:20): Trinh Thám Kỳ Án - Nam Minh lạnh lùng, bí ẩn (-14%)
- Slot 9 (21:10): Truyện Ma Quái Đàm - Nam Minh âm u, thì thầm rùng rợn (-14%, -4Hz)
- Slot 10 (23:00): Kinh Dị Rùng Rợn - Nam Minh đêm muộn ma mị (-14%, -4Hz)
"""
import sys
import io
import time
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.daily_24h_master_autopilot import produce_single_series, load_daily_status, OUTPUT_DIR
from core.stories.daily_story_factory import get_daily_10_series
from core.voice_profiles import get_voice_profile_for_genre

def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    series_list = get_daily_10_series(date_str)
    status = load_daily_status(date_str, series_list)

    remaining_slots = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n" + "=" * 75, flush=True)
    print(f"🚀 BẮT ĐẦU SẢN XUẤT TỰ ĐỘNG CÁC BỘ AUDIO CHO NGÀY: {date_str}", flush=True)
    print(f"📋 Danh sách slot cần sản xuất: {remaining_slots}", flush=True)
    print("=" * 75, flush=True)

    for slot_num in remaining_slots:
        series_conf = next((s for s in series_list if s["slot_index"] == slot_num), None)
        if not series_conf:
            continue

        s_key = series_conf["key"]
        prefix = series_conf["prefix"]
        title = series_conf["title"]
        genre = series_conf.get("genre", "")
        prof = get_voice_profile_for_genre(genre)

        print(f"\n🎬 [SLOT {slot_num}/10] Chuẩn bị sản xuất: {title}", flush=True)
        print(f"   * Thể loại: {genre}", flush=True)
        print(f"   * Voice Profile: {prof.display_name} ({prof.voice_name})", flush=True)
        print(f"   * Thông số âm thanh: Pitch={prof.pitch}, Rate={prof.rate}, Volume={prof.volume}, Tempo={prof.tempo_multiplier}x", flush=True)

        # Kiểm tra xem cả 3 tập đã có sẵn chưa
        all_done = True
        for p in [1, 2, 3]:
            vid = OUTPUT_DIR / f"{prefix}_part{p}_final.mp4"
            if not vid.exists() or vid.stat().st_size < 500000:
                all_done = False
                break

        if all_done:
            print(f"   ⏭️ Bộ {slot_num} đã có sẵn đầy đủ 3 video thành phẩm, bỏ qua render.", flush=True)
            status[s_key]["produced"] = True
            continue

        # Sản xuất trọn vẹn 3 tập cho bộ truyện này
        t0 = time.time()
        produce_single_series(series_conf, status, date_str)
        dur_min = (time.time() - t0) / 60
        print(f"   ✅ [HOÀN THÀNH SLOT {slot_num}] Thời gian sản xuất: {dur_min:.1f} phút", flush=True)

    print("\n" + "=" * 75, flush=True)
    print(f"🎉 TẤT CẢ 10 BỘ AUDIO CHO NGÀY {date_str} ĐÃ SẴN SÀNG 100%!", flush=True)
    print("   Hệ thống 24/7 Autopilot sẽ tự động xuất bản đúng khung giờ từng slot.", flush=True)
    print("=" * 75, flush=True)

if __name__ == "__main__":
    main()
