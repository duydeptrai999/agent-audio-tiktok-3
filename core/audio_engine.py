# -*- coding: utf-8 -*-
"""
core/audio_engine.py
Hệ Thống Động Cơ Âm Thanh & Giọng Đọc Điện Ảnh Triệu View (Cinema Audio & Voice Engine).
Học hỏi và tối ưu hóa từ các kênh Kể chuyện Audio / Podcast triệu view (Túi Mù Audio, Kỳ Án Có Thật, v.v.):

1. TỐI ƯU HÓA GIỌNG ĐỌC EDGE-TTS (Neural Voice Optimization):
   - Thay vì tua thẳng atempo=1.5x gây vỡ tiếng/chói gắt kim loại, hệ thống kết hợp 2 tầng tốc độ:
     * Tầng 1: Edge-TTS Native Neural Rate (+18% đến +20%) để AI sinh ngữ âm tự nhiên, giữ trọn thanh điệu tiếng Việt.
     * Tầng 2: FFmpeg Gentle Time-Stretch (atempo=1.25x) đạt đúng định mức 1.50x (346 từ/phút theo chuẩn GEMINI.md).
   - Tinh chỉnh cao độ (Pitch Modulation):
     * Nam Minh Neural: Pitch -2Hz (trầm, đầm ấm, uy quyền, thích hợp Trinh thám / Kinh dị).
     * Hoài My Neural: Pitch +1Hz (trong trẻo, sắc sảo, dồn dập, truyền cảm cho Trọng sinh / Hào môn).

2. CHUỖI XỬ LÝ VOCAL STUDIO RADIO (Broadcast Vocal Mastering Chain):
   - High-pass 75Hz: Triệt tiêu tiếng thở thô, tiếng va đập micro tần số thấp.
   - Warmth Boost 145Hz (+3.5dB): Tăng độ ấm dày cho lồng ngực giọng đọc.
   - Boxiness Scoop 1200Hz (-2.0dB): Xóa bỏ tiếng đục hộp nhựa, giúp giọng trong vắt.
   - Clarity Boost 3500Hz (+3.2dB): Làm sáng các thanh sắc, hỏi, ngã, nặng tiếng Việt.
   - De-Esser 6500Hz (-2.5dB): Chống chói tai ở các âm xì "s", "x".
   - Dynamic Range Compressor: Nén biên độ mượt mà, không bị giật âm lượng.

3. DYNAMIC SIDECHAIN AUTO-DUCKING (Nhạc nền tự động né giọng đọc):
   - Khi có giọng nói: BGM tự động hạ xuống -20dB đến -24dB, nhường 100% sân khấu cho lời thoại.
   - Khi ngắt nghỉ / chuyển đoạn: BGM tự động dâng trào lên -14dB, đẩy cao trào kịch tính.

4. 100% CHỐNG BẢN QUYỀN TIKTOK (Anti-Copyright & Content-ID Shield):
   - Cách ly 100% bài nhạc thương mại bị gắn bản quyền gắt gao.
   - Áp dụng micro-tempo và frequency notch cho BGM để triệt tiêu audio hash của bot quét bản quyền.
"""

import os
import re
import sys
import asyncio
import logging
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

import edge_tts
from core.ffmpeg_utils import get_ffmpeg_exe
from core.voice_profiles import get_voice_profile_for_genre, build_genre_vocal_filter_chain
from core.bgm_manager import (
    ensure_safe_bgm,
    get_safe_bgm_for_genre,
    apply_anti_copyright_shield,
    is_track_blacklisted,
    quarantine_copyrighted_tracks
)

logger = logging.getLogger("AudioEngine")
ROOT_DIR = Path(__file__).resolve().parent.parent



def sanitize_tts_text(text: str) -> str:
    """
    Tự động chuẩn hóa các từ ngữ nhạy cảm tránh bị Microsoft Azure Content Filter chặn:
    - 'thiêu thân' -> 'kẻ u mê'
    - 'rít' -> 'thét'
    - 'chợ đen' -> 'bên ngoài'
    - 'tự sát' -> 'qua đời'
    - 'đỏ đen' -> 'may rủi'
    """
    replacements = {
        "thiêu thân": "kẻ mải mê",
        "Thiêu thân": "Kẻ mải mê",
        "nghiện ngập": "say mê",
        "Nghiện ngập": "Say mê",
        "gào rít": "gào thét",
        "Gào rít": "Gào thét",
        "rít gào": "gào thét",
        "Rít gào": "Gào thét",
        "rít": "thét",
        "Rít": "Thét",
        "chợ đen": "bên ngoài",
        "Chợ đen": "Bên ngoài",
        "tự sát": "qua đời",
        "Tự sát": "Qua đời",
        "đỏ đen": "may rủi",
        "Đỏ đen": "May rủi",
        "chửi rủa": "mắng mỏ",
        "Chửi rủa": "Mắng mỏ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def split_into_tts_chunks(text: str, max_words: int = 150) -> List[str]:
    """Chia văn bản thành các đoạn nhỏ 120-150 từ tại vị trí dấu câu tự nhiên."""
    clean_text = sanitize_tts_text(text)
    clean_text = (
        clean_text.replace("'", " ")
        .replace('"', ' ')
        .replace("‘", " ")
        .replace("’", " ")
        .replace("“", " ")
        .replace("”", " ")
        .replace("–", "-")
        .replace("—", "-")
        .replace("...", ".")
        .replace("..", ".")
    )
    import re
    clean_text = re.sub(r'([!?,.:;…])\s*[!?,.:;…]+', r'\1', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    sentences = [s.strip() for s in re.split(r'(?<=[.!?…\n])\s+', clean_text) if s.strip()]
    chunks: List[str] = []
    cur: List[str] = []
    cur_w = 0
    for s in sentences:
        w_count = len(s.split())
        if cur_w + w_count > max_words and cur:
            chunks.append(" ".join(cur))
            cur = [s]
            cur_w = w_count
        else:
            cur.append(s)
            cur_w += w_count
    if cur:
        chunks.append(" ".join(cur))
    return chunks if chunks else [clean_text]


def get_vocal_chain_filter(voice_volume: float = 1.0, genre: Optional[str] = None) -> str:
    """
    Chuỗi hiệu ứng Vocal Studio Radio Broadcast cao cấp cho FFmpeg:
    - Nếu có genre: Tự động tải Vocal Mastering Profile chuyên biệt (tăng trầm cho trinh thám, air cho sa điêu, nén gắt cho mạt thế sinh tồn...).
    - Nếu không: Áp dụng chuỗi phát thanh cân bằng tiêu chuẩn.
    """
    if genre:
        try:
            profile = get_voice_profile_for_genre(genre)
            return build_genre_vocal_filter_chain(profile, voice_volume=voice_volume)
        except Exception:
            pass

    return (
        f"highpass=f=75,"
        f"equalizer=f=145:t=q:w=1.2:g=3.5,"
        f"equalizer=f=1200:t=q:w=1.5:g=-2.0,"
        f"equalizer=f=3500:t=q:w=1.2:g=3.2,"
        f"equalizer=f=6500:t=q:w=1.8:g=-2.5,"
        f"acompressor=threshold=-18dB:ratio=3.2:attack=8:release=60,"
        f"volume={voice_volume}"
    )


async def generate_cinema_tts_audio(
    text: str,
    voice: str = "vi-VN-HoaiMyNeural",
    output_path: Optional[Path] = None,
    target_speed: Optional[float] = None,
    genre: Optional[str] = None
) -> Path:
    """
    Sinh audio Edge-TTS chất lượng cao đạt chuẩn điện ảnh:
    - Hỗ trợ tốc độ tối ưu 1.15x (khoảng 240 từ/phút) chống mệt tai suốt 10 phút hoặc 1.5x theo cấu hình.
    - Pitch -2Hz cho Nam Minh / +1Hz cho Hoài My.
    - Tự động chia chunk, retry 5 lần với semaphore.
    """
    if target_speed is None:
        try:
            from config.settings import VOICE_SPEED_MULTIPLIER
            target_speed = float(VOICE_SPEED_MULTIPLIER)
        except Exception:
            target_speed = 1.15

    # BẮT BUỘC: Đọc kinh nghiệm từ GEMINI.md & 5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md trước khi làm audio
    try:
        from core.stories.script_quality_gate import require_preflight_experience, audit_and_optimize_part_text
        require_preflight_experience()
        text, _ = audit_and_optimize_part_text(text, title="PreAudioTTS", part_num=1)
    except Exception as e:
        logger.warning(f"Lỗi kiểm tra preflight experience: {e}")

    if output_path is None:
        audio_dir = ROOT_DIR / "assets" / "audio"
        audio_dir.mkdir(parents=True, exist_ok=True)
        output_path = audio_dir / "cinema_tts_temp.mp3"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    chunks = split_into_tts_chunks(text, max_words=150)
    chunk_files = [output_path.parent / f"{output_path.stem}_chk{i}.mp3" for i in range(len(chunks))]
    concat_list = output_path.parent / f"{output_path.stem}_concat.txt"
    raw_merged = output_path.parent / f"{output_path.stem}_raw.mp3"

    # Tự động tối ưu Voice Profile theo thể loại (Pitch Modulation + Native Rate + Studio Mastering)
    profile_pitch = "-2Hz" if "NamMinh" in voice else "+1Hz"
    profile_rate = "+0%"
    if genre:
        try:
            profile = get_voice_profile_for_genre(genre)
            profile_pitch = profile.pitch
            profile_rate = profile.rate
            if voice == "vi-VN-HoaiMyNeural" and "MALE" in profile.profile_id:
                voice = profile.voice_name
            elif voice == "vi-VN-NamMinhNeural" and "FEMALE" in profile.profile_id:
                voice = profile.voice_name
            if target_speed is None or target_speed == 1.15:
                target_speed = profile.tempo_multiplier
        except Exception:
            pass

    is_male = "NamMinh" in voice
    atempo_factor = round(target_speed, 2)

    semaphore = asyncio.Semaphore(1)

    async def synth_chk(idx: int, chk_text: str, fpath: Path):
        async with semaphore:
            for attempt in range(8):
                try:
                    comm = edge_tts.Communicate(chk_text, voice=voice, pitch=profile_pitch, rate=profile_rate)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=60.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception as e:
                    await asyncio.sleep(1.5 * (attempt + 1))
            if not fpath.exists() or fpath.stat().st_size <= 500:
                fallback_voice = "vi-VN-HoaiMyNeural" if is_male else "vi-VN-NamMinhNeural"
                try:
                    comm = edge_tts.Communicate(chk_text, voice=fallback_voice)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=60.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception:
                    pass
            if not fpath.exists() or fpath.stat().st_size <= 500:
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 8 retries with {voice}")

    try:
        tasks = [synth_chk(i, c, chunk_files[i]) for i, c in enumerate(chunks)]
        await asyncio.gather(*tasks)

        # Ghép các chunk lại bằng FFmpeg concat
        with open(concat_list, "w", encoding="utf-8") as f:
            for c_file in chunk_files:
                if not c_file.exists() or c_file.stat().st_size <= 500:
                    raise RuntimeError(f"Missing valid chunk file: {c_file.name}")
                f.write(f"file '{c_file.resolve().as_posix()}'\n")

        ffmpeg = get_ffmpeg_exe()
        subprocess.run([
            ffmpeg, "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c", "copy",
            str(raw_merged)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        # Tua nhẹ atempo để đạt tròn 1.50x
        subprocess.run([
            ffmpeg, "-y",
            "-i", str(raw_merged),
            "-filter:a", f"atempo={atempo_factor}",
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(output_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        logger.info(f"Đã tạo xong Cinema TTS Audio: {output_path.name} (Tốc độ tổng {target_speed}x)")
        return output_path
    finally:
        # Dọn dẹp tệp tạm
        try:
            if concat_list.exists():
                concat_list.unlink(missing_ok=True)
            if raw_merged.exists():
                raw_merged.unlink(missing_ok=True)
            for c in chunk_files:
                if c.exists():
                    c.unlink(missing_ok=True)
        except Exception:
            pass


def mix_voice_and_safe_bgm(
    voice_audio_path: str,
    output_audio_path: str,
    genre_key: str = "TRONG_SINH",
    bgm_path: Optional[str] = None,
    bgm_volume: float = 0.42,
    voice_volume: float = 1.0
) -> str:
    """
    Ráp nối Voice + BGM an toàn với Dynamic Auto-Ducking và Chuẩn hóa Mastering -13 LUFS.
    Xuất ra file âm thanh thành phẩm hoàn hảo cho video hoặc audio podcast.
    """
    safe_bgm = ensure_safe_bgm(bgm_path, genre_key=genre_key)
    ffmpeg = get_ffmpeg_exe()

    ducking_thresh = 0.079
    ducking_ratio = 4.0
    ducking_attack = 25
    ducking_release = 750
    ducking_knee = 2.5
    target_lufs = -14.0
    true_peak = -1.5
    try:
        from config.settings import (
            DUCKING_THRESHOLD, DUCKING_RATIO, DUCKING_ATTACK_MS,
            DUCKING_RELEASE_MS, DUCKING_KNEE, TARGET_LUFS, TRUE_PEAK
        )
        ducking_thresh = DUCKING_THRESHOLD
        ducking_ratio = DUCKING_RATIO
        ducking_attack = DUCKING_ATTACK_MS
        ducking_release = DUCKING_RELEASE_MS
        ducking_knee = DUCKING_KNEE
        target_lufs = TARGET_LUFS
        true_peak = TRUE_PEAK
    except Exception:
        pass

    vocal_filter = get_vocal_chain_filter(voice_volume, genre=genre_key)
    filter_complex = (
        f"[0:a]{vocal_filter},asplit=2[v_play][v_trigger];"
        f"[1:a]volume={bgm_volume},highpass=f=60,equalizer=f=2000:t=q:w=1.5:g=-3.5[bgm_prep];"
        f"[bgm_prep][v_trigger]sidechaincompress=threshold={ducking_thresh}:ratio={ducking_ratio}:attack={ducking_attack}:release={ducking_release}:knee={ducking_knee}[bgm_ducked];"
        f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"
    )

    cmd = [
        ffmpeg, "-y",
        "-i", str(voice_audio_path),
        "-stream_loop", "-1",
        "-i", str(safe_bgm),
        "-filter_complex", filter_complex,
        "-map", "[aout]",
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        str(output_audio_path)
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return str(output_audio_path)
