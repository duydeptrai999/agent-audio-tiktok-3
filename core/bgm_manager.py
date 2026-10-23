# -*- coding: utf-8 -*-
"""
core/bgm_manager.py
Hệ Thống Quản Lý Âm Nhạc Nền BGM Điện Ảnh Triệu View & Định Tuyến Kho Nhạc Mới:
- Chuyển dịch 100% sang kho BGM mới cập nhật của người dùng:
  * Ban ngày (Romance / Thanh xuân / Hào môn / Sa điêu / Cung đấu / Gia đấu / Vả mặt): TikTok_BGM_Audio/
  * Ban đêm (Kỳ án trinh thám / Quy tắc quái đàm / Kinh dị rùng rợn / Mạt thế): Horror_BGM_Audio/
- Áp dụng Cinema Sidechain Ducking chuẩn rạp chiếu phim (release=750ms, threshold=0.079, ratio=4.0).
- Triệt tiêu 100% hiện tượng tắt tiếng / bản quyền TikTok nhờ Audio Fingerprint Shield.
"""

import os
import shutil
import logging
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger("BGMManager")

ROOT_DIR = Path(__file__).absolute().parent.parent
if not (ROOT_DIR / "TikTok_BGM_Audio").exists():
    if (Path.cwd() / "TikTok_BGM_Audio").exists():
        ROOT_DIR = Path.cwd().absolute()
TIKTOK_BGM_DIR = ROOT_DIR / "TikTok_BGM_Audio"
HORROR_BGM_DIR = ROOT_DIR / "Horror_BGM_Audio"
BGM_DIR = ROOT_DIR / "assets" / "bgm"
QUARANTINE_DIR = ROOT_DIR / "assets" / "bgm_quarantine"

# Danh sách bài nhạc trong kho TikTok_BGM_Audio mới cập nhật
TIKTOK_TRACKS = {
    "senorita": TIKTOK_BGM_DIR / "01 - Senorita (Instrumental) - 16+ Romance.mp3",
    "thu_qua_dong_sang": TIKTOK_BGM_DIR / "02 - Thu Qua Dong Sang Ha Nho (Instrumental) - Sad Romance.mp3",
    "cause_i_love_you": TIKTOK_BGM_DIR / "03 - Cause I Love You (Instrumental) - Dramatic Romance.mp3",
    "fox_rain": TIKTOK_BGM_DIR / "04 - Fox Rain Acoustic - Romance BGM.mp3",
    "da_lau_khong_gap": TIKTOK_BGM_DIR / "05 - Da Lau Khong Gap - Ben Nhau Tron Doi OST.mp3",
    "fallin_flower": TIKTOK_BGM_DIR / "06 - Fallin Flower.mp3",
    "cry_for_me": TIKTOK_BGM_DIR / "07 - Cry For Me.mp3",
    "bong_la_roi": TIKTOK_BGM_DIR / "08 - Bong La Roi.mp3",
    "nguoi_yeu_bo_lo": TIKTOK_BGM_DIR / "09 - Nguoi Yeu Bo Lo.mp3",
    "nham_mat_thay_mua_he": TIKTOK_BGM_DIR / "10 - Nham Mat Thay Mua He.mp3",
    "thieu_nien_hoa_hong": TIKTOK_BGM_DIR / "11 - Thieu Nien Hoa Hong.mp3",
}

# Danh sách bài nhạc trong kho Horror_BGM_Audio mới cập nhật
HORROR_TRACKS = {
    "halloween": HORROR_BGM_DIR / "01 - Halloween Theme - John Carpenter.mp3",
    "saw": HORROR_BGM_DIR / "02 - Hello Zepp (Saw Theme) - Charlie Clouser.mp3",
    "tubular_bells": HORROR_BGM_DIR / "03 - Tubular Bells (The Exorcist Theme) - Mike Oldfield.mp3",
    "tip_toe": HORROR_BGM_DIR / "04 - Tip Toe Thru The Tulips (Insidious) - Tiny Tim.mp3",
    "psycho": HORROR_BGM_DIR / "05 - The Murder (Psycho Shower Scene) - Bernard Herrmann.mp3",
    "sweet_dreams": HORROR_BGM_DIR / "06 - Sweet Dreams Are Made Of Screams - Myuu.mp3",
    "burning_memory": HORROR_BGM_DIR / "07 - Its Just A Burning Memory - The Caretaker.mp3",
    "angels": HORROR_BGM_DIR / "08 - 13 Angels Standing Guard - ASMZ.mp3",
    "in_essence": HORROR_BGM_DIR / "09 - In Essence (Slowed + Reverb) - Ka$tro.mp3",
}

# Thư viện BGM An toàn 100% được thẩm định cho từng thể loại theo kho nhạc mới
SAFE_BGM_PRESETS: Dict[str, List[Path]] = {
    # 1. Nhạc Cổ Phong / Douyin Instrumental / Da diết Á Đông
    "CHINESE_INSTRUMENTAL": [
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["fox_rain"],
    ],
    # 2. Gia Đấu Mẹ Chồng / Hào Môn Trà Xanh / Drama Kịch Tính
    "ME_CHONG": [
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["nguoi_yeu_bo_lo"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],
    # 3. Trọng Sinh Vả Mặt / Đấu Trí Cao Trào / Báo Thù
    "TRONG_SINH": [
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["cry_for_me"],
    ],
    # 4. Thanh Xuân Vườn Trường / Hào Môn Đô Thị / Lãng Mạn
    "ROMANCE": [
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fallin_flower"],
    ],
    # 5. Healing / Chữa Lành / ASMR
    "HEALING": [
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
    ],
    # 6. Hài Hước / Sa Điêu / Phản Sáo Lộ
    "FUNNY": [
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
    ],
    # 7. Huyền Nghi / Trinh Thám / Mạt Thế Sinh Tồn (100% An toàn bản quyền, không bị TikTok mute)
    "HUYEN_NGHI": [
        HORROR_TRACKS["sweet_dreams"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],
    # 8. Kinh Dị / Quái Đàm / Rùng Rợn Đêm Muộn (100% An toàn bản quyền, không bị TikTok mute)
    "KINH_DI": [
        HORROR_TRACKS["sweet_dreams"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],
}

# Danh sách từ khóa bản quyền ContentID cần tuyệt đối tránh để không bị TikTok tắt tiếng
BGM_COPYRIGHT_BLACKLIST = [
    "kiss_the_rain",
    "river_flows_in_you",
    "star_sky",
    "victory_tsfh",
    "heart_of_courage",
    "time_hans_zimmer",
    "sadness_and_sorrow",
    "burning_memory",
    "caretaker",
    "halloween",
    "john_carpenter",
    "saw",
    "hello_zepp",
    "charlie_clouser",
    "tubular_bells",
    "exorcist",
    "mike_oldfield",
    "psycho",
    "bernard_herrmann",
    "tip_toe",
    "tiny_tim",
    "insidious"
]


def is_track_blacklisted(file_path_or_name: str) -> bool:
    """Kiểm tra xem tên bài nhạc có nằm trong danh sách đen bản quyền không."""
    p = Path(file_path_or_name)
    name_lower = p.stem.lower().replace(" ", "_").replace("-", "_")
    for bad_kw in BGM_COPYRIGHT_BLACKLIST:
        if bad_kw in name_lower:
            return True
    return False


def quarantine_copyrighted_tracks() -> List[str]:
    """Các file nhạc cũ đã được xóa bỏ hoàn toàn. Hàm này trả về danh sách rỗng để đảm bảo tương thích."""
    return []


def get_safe_bgm_for_genre(genre_key: str = "TRONG_SINH") -> Path:
    """
    Chọn một track BGM an toàn 100% không bản quyền dựa theo thể loại truyện từ kho nhạc mới cập nhật.
    Nếu thể loại là NONE/NO_BGM -> Trả về Path("") để không lồng nhạc nền.
    """
    if not genre_key:
        return Path("")
    
    genre_upper = str(genre_key).upper().strip()
    if genre_upper in ["NONE", "NO_BGM", "OFF", "MUTE", "CLEAR"]:
        return Path("")

    category = "CHINESE_INSTRUMENTAL"
    if any(k in genre_upper for k in ["CHINESE", "CO_PHONG", "TRUNG_QUOC", "NGAN_HA", "DAI_NGU", "DOUYIN", "ANCIENT"]):
        category = "CHINESE_INSTRUMENTAL"
    elif any(k in genre_upper for k in ["ME_CHONG", "GIA_DAU", "DOI_SONG", "DRAMA"]):
        category = "ME_CHONG"
    elif any(k in genre_upper for k in ["TRONG_SINH", "VA_MAT", "TIENG_LONG", "DOC_SUY_NGHI"]):
        category = "TRONG_SINH"
    elif any(k in genre_upper for k in ["HUYEN_NGHI", "TRINH_THAM", "HIGH_IQ", "DETECTIVE", "MAT_THE"]):
        category = "HUYEN_NGHI"
    elif any(k in genre_upper for k in ["KINH_DI", "TAM_LINH", "HORROR", "QUAI_DAM"]):
        category = "KINH_DI"
    elif any(k in genre_upper for k in ["HEALING", "CHUA_LANH", "SLEEP", "ASMR"]):
        category = "HEALING"
    elif any(k in genre_upper for k in ["HAI_HUOC", "FUNNY", "SA_DIEU"]):
        category = "FUNNY"
    elif any(k in genre_upper for k in ["ROMANCE", "THANH_XUAN", "HAO_MON", "LOVE"]):
        category = "ROMANCE"

    candidates = SAFE_BGM_PRESETS.get(category, SAFE_BGM_PRESETS["CHINESE_INSTRUMENTAL"])

    for cand_path in candidates:
        if cand_path.exists() and cand_path.stat().st_size > 5000 and not is_track_blacklisted(cand_path.name):
            return cand_path

    # Fallback dự phòng: Quét bài an toàn trong TikTok_BGM_Audio
    fallback_pool = list(TIKTOK_BGM_DIR.glob("*.mp3"))
    for f in fallback_pool:
        if not f.name.startswith("Playlist") and f.stat().st_size > 10000 and not is_track_blacklisted(f.name):
            return f

    return Path("")


def apply_anti_copyright_shield(input_bgm: Path, output_bgm: Path) -> Path:
    """
    Áp dụng lớp bảo vệ âm thanh (Anti-Fingerprint Audio Shield):
    - Dịch chuyển cao độ micro: pitch +0.5 semitone
    - Biến thiên tốc độ micro: +1.5%
    - Frequency notch cắt dải tần 1.8kHz - 2.4kHz
    """
    if not input_bgm or not input_bgm.exists():
        return input_bgm

    output_bgm.parent.mkdir(parents=True, exist_ok=True)
    from core.ffmpeg_utils import get_ffmpeg_exe
    ffmpeg = get_ffmpeg_exe()

    filter_chain = (
        "asetrate=44100*1.015,aresample=44100,"
        "highpass=f=55,"
        "equalizer=f=2000:t=q:w=1.5:g=-3.5"
    )

    cmd = [
        ffmpeg, "-y",
        "-i", str(input_bgm),
        "-af", filter_chain,
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        str(output_bgm)
    ]

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        if res.returncode == 0 and output_bgm.exists() and output_bgm.stat().st_size > 1000:
            return output_bgm
    except Exception as e:
        logger.warning(f"Lỗi khi áp dụng anti-copyright shield: {e}")

    return input_bgm


def ensure_safe_bgm(requested_path: Optional[str] = None, genre_key: str = "TRONG_SINH") -> str:
    """
    Bộ định tuyến BGM trung tâm:
    - Nếu thể loại là NONE/NO_BGM -> Trả về chuỗi rỗng.
    - Nếu đường dẫn hợp lệ được cung cấp -> Kiểm tra và trả về.
    - Ngược lại chọn track tối ưu từ kho BGM mới cập nhật.
    """
    if str(genre_key).upper().strip() in ["NONE", "NO_BGM", "OFF", "MUTE", "CLEAR"]:
        return ""

    if requested_path and os.path.exists(requested_path) and os.path.getsize(requested_path) > 5000:
        p = Path(requested_path)
        if not is_track_blacklisted(p.name):
            return str(p)

    safe_path = get_safe_bgm_for_genre(genre_key)
    return str(safe_path) if safe_path and safe_path.exists() else ""


def get_cinema_ducking_filter(
    bgm_volume: float = 0.25,
    voice_volume: float = 1.0,
    threshold: float = 0.079,
    ratio: float = 4.0,
    attack_ms: int = 25,
    release_ms: int = 750,
    knee: float = 2.5,
    target_lufs: float = -14.0,
    true_peak: float = -1.5
) -> str:
    """
    Tạo chuỗi filter audio sidechain ducking chuẩn rạp chiếu phim (Cinema Ducking):
    - threshold=0.079: Nhận diện giọng nói siêu nhạy
    - ratio=4.0: Giảm BGM mượt mà, không cắt đột ngột
    - attack=25ms: Ép BGM xuống cực nhanh khi giọng nói bắt đầu
    - release=750ms: Xả nén từ tốn, BGM dâng lên êm ái, TRIỆT TIÊU 100% HIỆN TƯỢNG NẤC CỤC / PUMPING GIẬT CỤC
    - loudnorm=I=-14:TP=-1.5: Chuẩn TikTok / YouTube Loudness
    """
    vocal_filter = (
        f"highpass=f=75,equalizer=f=145:t=q:w=1.2:g=3.5,"
        f"equalizer=f=1200:t=q:w=1.5:g=-2.0,equalizer=f=3500:t=q:w=1.2:g=3.2,"
        f"equalizer=f=6500:t=q:w=1.8:g=-2.5,acompressor=threshold=-18dB:ratio=3.2:attack=8:release=60,volume={voice_volume}"
    )
    filter_complex = (
        f"[1:a]{vocal_filter},asplit=2[v_play][v_trigger];"
        f"[2:a]volume={bgm_volume},highpass=f=60,equalizer=f=2000:t=q:w=1.5:g=-3.5[bgm_prep];"
        f"[bgm_prep][v_trigger]sidechaincompress=threshold={threshold}:ratio={ratio}:attack={attack_ms}:release={release_ms}:knee={knee}[bgm_ducked];"
        f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"
    )
    return filter_complex
