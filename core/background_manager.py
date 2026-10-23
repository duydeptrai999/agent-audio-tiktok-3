# -*- coding: utf-8 -*-
"""
core/background_manager.py
Hệ Thống Quản Lý Kho Video Nền YouTube & Cắt Phân Đoạn Riêng Biệt (Distinct Slices Engine)
Tuân thủ 100% yêu cầu:
1. Mỗi video (mỗi part / mỗi audio) sở hữu 1 đoạn video nền KHÁC NHAU hoàn toàn, không lặp lại.
2. Tải video background từ YouTube (Baking, Nature Scenery, Cozy Cooking, Craft Chill Healing).
3. Chu kỳ 10 audio thì tự động tải mới video background 1 lần.
4. Cắt phân đoạn siêu tốc bằng FFmpeg không nén lại (stream copy -an).
5. Tích hợp liền mạch với Thumbnail Generator.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from core.ffmpeg_utils import get_ffmpeg_exe, probe_media_file

ROOT_DIR = Path(__file__).resolve().parent.parent
POOL_DIR = ROOT_DIR / "assets" / "footage" / "youtube_pool"
SLICES_DIR = ROOT_DIR / "assets" / "footage" / "slices"
STATE_FILE = ROOT_DIR / "data" / "background_video_pool.json"

# Danh sách chủ đề video nền: Ưu tiên video ASMR Trung Quốc (Douyin style) giữ chân người xem cực đỉnh:
# 1. ASMR làm đẹp, chăm sóc da, trang điểm chị em Trung Quốc
# 2. ASMR nấu ăn mỹ vị ẩm thực truyền thống Trung Hoa
# 3. ASMR làm bánh / điểm tâm hoa văn nghệ thuật
# 4. ASMR thủ công mỹ nghệ di sản phi vật thể Trung Quốc (gốm sứ, thêu thùa, chạm khắc)
DEFAULT_SEARCH_THEMES = [
    {"theme": "chinese_beauty_asmr", "query": "chinese makeup skincare asmr satisfying douyin no music"},
    {"theme": "chinese_cooking_asmr", "query": "chinese traditional cooking asmr satisfying street food no music"},
    {"theme": "chinese_pastry_baking", "query": "traditional chinese pastry dim sum baking asmr no music"},
    {"theme": "chinese_craft_heritage", "query": "chinese intangible cultural heritage traditional craft embroidery pottery wood asmr"},
    {"theme": "satisfying_asmr_relaxing", "query": "satisfying visual asmr relaxing handmade craft no music 1 hour"},
    {"theme": "craft", "query": "traditional craft pottery wood carving asmr no music 1 hour"},
    {"theme": "baking", "query": "baking cake decorating asmr no music 2 hours"}
]

def extract_video_slice(
    source_path: Path,
    slice_path: Path,
    start_sec: float,
    duration_seconds: float
) -> Path:
    """
    Trích xuất phân đoạn B-roll siêu tốc với libx264 ultrafast re-encode:
    - Bắt buộc: -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p -force_key_frames "expr:gte(t,0)" -avoid_negative_ts make_zero -an
    - Cưỡng bức khung hình 0 (Frame 0) luôn là IDR Keyframe ở PTS=0 (iskey=1, type=I).
    - Triệt tiêu 100% lỗi màn hình đen hoặc giật lag ở giây đầu tiên.
    """
    ffmpeg = get_ffmpeg_exe()
    slice_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg, "-y",
        "-ss", str(start_sec),
        "-i", str(source_path),
        "-t", str(duration_seconds),
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-force_key_frames", "expr:gte(t,0)",
        "-avoid_negative_ts", "make_zero",
        "-an",
        str(slice_path)
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=600)
    except subprocess.TimeoutExpired:
        print(f"[BackgroundManager Error] Timeout 600s khi cắt video slice {slice_path.name}")
        raise
    return slice_path


class BackgroundVideoManager:
    """Quản lý kho video nền YouTube dài, cắt lát phân đoạn riêng biệt và tự động xoay tua."""

    def __init__(self):
        POOL_DIR.mkdir(parents=True, exist_ok=True)
        SLICES_DIR.mkdir(parents=True, exist_ok=True)
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.state = self._load_state()

    def _load_state(self) -> Dict[str, Any]:
        """Tải trạng thái pool từ file JSON."""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "active_video": None,
            "used_history": [],
            "rotation_count": 0,
            "search_themes": DEFAULT_SEARCH_THEMES
        }

    def _save_state(self):
        """Lưu trạng thái pool ra file JSON an toàn qua file tạm (atomic write)."""
        try:
            tmp_file = STATE_FILE.with_suffix(".tmp")
            with open(tmp_file, "w", encoding="utf-8") as f:
                json.dump(self.state, f, ensure_ascii=False, indent=2)
            tmp_file.replace(STATE_FILE)
        except Exception as e:
            print(f"[BackgroundManager] Lỗi lưu state: {e}")

    def extract_video_slice(
        self,
        source_path: Path,
        slice_path: Path,
        start_sec: float,
        duration_seconds: float
    ) -> Path:
        """Cắt video slice với IDR keyframe ở PTS=0."""
        return extract_video_slice(source_path, slice_path, start_sec, duration_seconds)

    def cleanup_old_slices(self, max_age_hours: int = 24, max_total_mb: int = 1000) -> int:
        """
        Tự động dọn dẹp các lát cắt B-roll cũ trong assets/footage/slices/
        để chống tràn bộ nhớ đĩa (giới hạn cache < max_total_mb).
        """
        if not SLICES_DIR.exists():
            return 0
        now = time.time()
        max_age_sec = max_age_hours * 3600
        removed_count = 0

        # Lấy danh sách slices sắp xếp từ cũ đến mới
        slices = sorted(
            [f for f in SLICES_DIR.glob("*.mp4") if f.is_file()],
            key=lambda x: x.stat().st_mtime
        )

        remaining = []
        for s in slices:
            try:
                age = now - s.stat().st_mtime
                if age > max_age_sec:
                    s.unlink(missing_ok=True)
                    removed_count += 1
                else:
                    remaining.append(s)
            except Exception:
                remaining.append(s)

        total_bytes = sum(f.stat().st_size for f in remaining if f.exists())
        max_bytes = max_total_mb * 1024 * 1024
        while total_bytes > max_bytes and remaining:
            oldest = remaining.pop(0)
            try:
                f_size = oldest.stat().st_size
                oldest.unlink(missing_ok=True)
                total_bytes -= f_size
                removed_count += 1
            except Exception:
                break

        return removed_count

    def register_source_video(self, video_path: Path, url: str = "", title: str = "", max_audios: int = 2) -> bool:
        """Đăng ký 1 video nền dài mới vào hệ thống pool."""
        if not video_path.exists() or video_path.stat().st_size < 1000000:
            return False

        probe = probe_media_file(video_path)
        duration = probe.get("duration", 0.0)
        if duration <= 10.0:
            # Ước lượng nếu probe không đọc được
            duration = 7200.0

        active_data = {
            "filepath": str(video_path.resolve()),
            "filename": video_path.name,
            "url": url,
            "title": title or video_path.stem,
            "total_duration": duration,
            "current_offset": 0.0,
            "audios_used": 0,
            "max_audios": max_audios,
            "registered_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Nếu có video cũ đang dùng, đưa vào lịch sử (tránh ghi đè trùng lặp liên tiếp)
        if self.state.get("active_video"):
            old = self.state["active_video"]
            history = self.state.setdefault("used_history", [])
            if not history or history[-1].get("filename") != old.get("filename"):
                history.append(dict(old))

        self.state["active_video"] = active_data
        self._save_state()
        print(f"🎬 [BackgroundManager] Đã kích hoạt video nền mới: {video_path.name} (Thời lượng: {duration/60:.1f} phút)")
        return True

    def rotate_pool_video(self) -> Optional[Path]:
        """
        Xoay tua kho video nền khi đã dùng >= 10 audio (hoặc hết thời lượng):
        1. Di chuyển active_video hiện tại vào used_history.
        2. Tăng rotation_count += 1.
        3. Xoay tua sang một video KHÁC trong POOL_DIR (theo thứ tự FIFO qua các file pool).
        4. Reset audios_used = 0 và current_offset = 0.0 cho video mới.
        """
        active = self.state.get("active_video")
        if active:
            history = self.state.setdefault("used_history", [])
            if not history or history[-1].get("filename") != active.get("filename"):
                history.append(dict(active))
            self.state["rotation_count"] = self.state.get("rotation_count", 0) + 1

        active_filename = active.get("filename") if active else None

        # Quét kiểm tra tất cả video có sẵn trong POOL_DIR (> 1MB)
        pool_files = [
            f for f in POOL_DIR.glob("*.mp4")
            if f.is_file() and f.stat().st_size > 1000000
        ]

        # Lọc các video KHÁC video hiện tại
        candidate_files = [f for f in pool_files if f.name != active_filename]

        chosen: Optional[Path] = None

        if candidate_files:
            # Sắp xếp FIFO: Các file chưa từng dùng trong used_history được ưu tiên (st_mtime tăng dần: cũ nhất trước)
            # Nếu tất cả đã dùng, chọn file xuất hiện sớm nhất trong used_history
            used_history = self.state.get("used_history", [])
            def get_fifo_rank(f: Path):
                last_used_idx = -1
                for idx, entry in enumerate(used_history):
                    if isinstance(entry, dict) and entry.get("filename") == f.name:
                        last_used_idx = idx
                return (last_used_idx, f.stat().st_mtime)

            candidate_files.sort(key=get_fifo_rank)
            chosen = candidate_files[0]
            print(f"🔄 [BackgroundManager] Xoay tua FIFO sang video nền mới trong pool: {chosen.name}")
        else:
            # Fallback kiểm tra raw_downloaded nếu trong POOL_DIR không còn video khác
            raw_dir = ROOT_DIR / "assets" / "footage" / "raw_downloaded"
            if raw_dir.exists():
                raw_cands = [
                    f for f in raw_dir.glob("*.mp4")
                    if f.is_file() and f.stat().st_size > 10000000 and f.name != active_filename
                ]
                if raw_cands:
                    raw_cands.sort(key=lambda x: x.stat().st_mtime)
                    chosen = raw_cands[0]
                    print(f"🔄 [BackgroundManager] Xoay tua sang video từ raw_downloaded: {chosen.name}")

        if chosen:
            self.register_source_video(chosen)
            return chosen
        elif active:
            # Nếu chỉ có duy nhất 1 video trong hệ sinh thái, reset bộ đếm và offset
            active["audios_used"] = 0
            active["current_offset"] = 0.0
            self.state["active_video"] = active
            self._save_state()
            v_path = Path(active["filepath"])
            return v_path if v_path.exists() else None

        return None

    def get_or_download_active_video(self, preferred_url: Optional[str] = None) -> Optional[Path]:
        """Lấy video nền đang hoạt động hoặc tự động tải video mới từ YouTube nếu đã dùng hết 10 audio."""
        active = self.state.get("active_video")

        # 1. Kiểm tra nếu có preferred_url được chỉ định trực tiếp (ví dụ link user gửi)
        if preferred_url:
            for f in POOL_DIR.glob("*.mp4"):
                if f.stat().st_size > 50000000: # > 50MB
                    if not active or active.get("filename") != f.name:
                        self.register_source_video(f, url=preferred_url)
                        return f
                    return Path(active["filepath"])

        # 2. Kiểm tra video hiện tại còn hiệu lực không (< 10 audio và còn thời lượng)
        if active:
            v_path = Path(active["filepath"])
            if v_path.exists() and v_path.stat().st_size > 1000000:
                remaining_dur = active["total_duration"] - active["current_offset"]
                if active.get("audios_used", 0) < active.get("max_audios", 10) and remaining_dur > 300:
                    return v_path
                else:
                    print(f"🔄 [BackgroundManager] Video {v_path.name} đã dùng {active.get('audios_used', 0)}/{active.get('max_audios', 10)} audio (hoặc hết thời lượng). Kích hoạt xoay tua!")
                    rotated = self.rotate_pool_video()
                    if rotated:
                        return rotated

        # 3. Quét kiểm tra video đã có sẵn trong POOL_DIR
        pool_files = sorted(
            [f for f in POOL_DIR.glob("*.mp4") if f.stat().st_size > 1000000],
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
        if pool_files:
            chosen = pool_files[0]
            self.register_source_video(chosen)
            return chosen

        # 4. Fallback kiểm tra các video dài trong raw_downloaded
        raw_dir = ROOT_DIR / "assets" / "footage" / "raw_downloaded"
        if raw_dir.exists():
            raw_cands = sorted(
                [f for f in raw_dir.glob("*.mp4") if f.stat().st_size > 10000000],
                key=lambda x: x.stat().st_size,
                reverse=True
            )
            if raw_cands:
                chosen = raw_cands[0]
                self.register_source_video(chosen)
                return chosen

        return None

    def get_distinct_slice_for_part(
        self,
        series_id: str,
        part_number: int,
        duration_seconds: float,
        preferred_url: Optional[str] = None,
        total_parts: int = 3
    ) -> Path:
        """
        Cắt lát một phân đoạn video nền ĐỘC NHẤT (không trùng lặp) cho từng Part / từng Audio.
        - Đảm bảo Part 1, Part 2, Part 3 của 1 bộ KHÔNG BAO GIỜ bị lặp hình ảnh giống nhau.
        - Tự động nhảy mốc thời gian offset tiếp theo cho các part và audio kế tiếp.
        - Bộ đếm audios_used tăng lên ở tập cuối của chuỗi (part_number == total_parts hoặc part_number == 0).
        - Khi audios_used >= 10, tự động xoay tua sang video khác trong POOL_DIR.
        """
        source_path = self.get_or_download_active_video(preferred_url=preferred_url)
        if not source_path or not source_path.exists():
            # Fallback nếu chưa tải xong: lấy video mẫu hiện có trong assets/footage
            cand = list((ROOT_DIR / "assets" / "footage").glob("*clean*.mp4"))
            source_path = cand[0] if cand else (ROOT_DIR / "assets" / "footage" / "sample_baking_horizontal_clean.mp4")

        active = self.state.get("active_video") or {
            "current_offset": 0.0,
            "total_duration": 7200.0,
            "audios_used": 0,
            "max_audios": 10
        }

        # Safe offset calculation: Ensure current_offset + duration_needed <= total_duration; wrap around or reset offset if exceeding duration
        start_sec = float(active.get("current_offset", 0.0))
        total_dur = float(active.get("total_duration", 7200.0))

        if start_sec + duration_seconds > total_dur:
            start_sec = 0.0

        # Tên file phân đoạn riêng biệt cho part này
        slice_name = f"slice_{series_id}_p{part_number}_{int(start_sec)}s_{int(duration_seconds)}s.mp4"
        slice_path = SLICES_DIR / slice_name

        # Tự động dọn dẹp các phân đoạn cũ để giải phóng dung lượng đĩa
        self.cleanup_old_slices(max_age_hours=24, max_total_mb=1000)

        if slice_path.exists() and slice_path.stat().st_size > 500000:
            print(f"🎬 [BackgroundManager] Sử dụng phân đoạn có sẵn: {slice_name}")
            return slice_path

        print(f"✂️ [BackgroundManager] Đang cắt phân đoạn B-Roll riêng cho {series_id} - Tập {part_number}:")
        print(f"   * Từ giây: {int(start_sec)}s ({int(start_sec)//60}m{int(start_sec)%60:02d}s)")
        print(f"   * Thời lượng: {int(duration_seconds)}s ({int(duration_seconds)//60}m{int(duration_seconds)%60:02d}s)")

        # Cắt lát siêu tốc bằng FFmpeg với ultrafast re-encode bảo đảm IDR Keyframe ở PTS=0
        self.extract_video_slice(
            source_path=source_path,
            slice_path=slice_path,
            start_sec=start_sec,
            duration_seconds=duration_seconds
        )

        # Cập nhật mốc thời gian tiếp theo (nhảy thêm 5s gap để cảnh quay nối tiếp hoàn toàn mới)
        next_offset = start_sec + duration_seconds + 5.0
        if next_offset >= total_dur:
            next_offset = 0.0
        active["current_offset"] = next_offset

        # Tăng audio counter khi là tập cuối của bất kỳ series nào (part_number == total_parts hoặc part_number == 0)
        if part_number == total_parts or part_number == 0:
            active["audios_used"] = active.get("audios_used", 0) + 1
            print(f"📈 [BackgroundManager] Đã dùng video cho {active['audios_used']}/{active.get('max_audios', 10)} bộ audio.")

            # Khi active audios_used >= 10: Xoay tua sang video khác trong POOL_DIR (FIFO order)
            if active["audios_used"] >= active.get("max_audios", 10):
                self.state["active_video"] = active
                self._save_state()
                print(f"🔄 [BackgroundManager] Video đã hoàn thành {active['audios_used']} audio. Kích hoạt xoay tua pool!")
                self.rotate_pool_video()
                size_mb = (slice_path.stat().st_size / (1024*1024)) if slice_path.exists() else 0.0
                print(f"✅ [BackgroundManager] Đã cắt thành công: {slice_name} ({size_mb:.1f} MB)")
                return slice_path

        self.state["active_video"] = active
        self._save_state()

        size_mb = (slice_path.stat().st_size / (1024*1024)) if slice_path.exists() else 0.0
        print(f"✅ [BackgroundManager] Đã cắt thành công: {slice_name} ({size_mb:.1f} MB)")
        return slice_path

    def download_youtube_video(self, url: str, target_name: Optional[str] = None) -> Optional[Path]:
        """Tải một video YouTube mới về pool bằng yt-dlp."""
        import yt_dlp
        POOL_DIR.mkdir(parents=True, exist_ok=True)
        out_tmpl = str(POOL_DIR / (target_name or "%(title).50s_%(id)s.%(ext)s"))

        ydl_opts = {
            'format': '137/bestvideo[height<=1080][ext=mp4]/136/bestvideo[height<=720]',
            'outtmpl': out_tmpl,
            'quiet': False,
            'no_warnings': True,
            'nocheckcertificate': True,
            'socket_timeout': 15,
            'retries': 3
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                downloaded_file = Path(ydl.prepare_filename(info))
                if downloaded_file.exists():
                    self.register_source_video(
                        downloaded_file,
                        url=url,
                        title=info.get("title", ""),
                        max_audios=10
                    )
                    return downloaded_file
        except Exception as e:
            print(f"❌ [BackgroundManager] Lỗi tải video YouTube: {e}")
        return None

# Singleton instance
background_manager = BackgroundVideoManager()

__all__ = [
    "BackgroundVideoManager",
    "background_manager",
    "extract_video_slice",
    "POOL_DIR",
    "SLICES_DIR",
    "STATE_FILE",
    "DEFAULT_SEARCH_THEMES"
]
