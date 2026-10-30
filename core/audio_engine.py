# -*- coding: utf-8 -*-
"""
core/audio_engine.py
Hệ Thống Động Cơ Âm Thanh & Giọng Đọc Điện Ảnh Triệu View (Cinema Audio & Voice Engine - Master Codex 8.0).
Học hỏi và tối ưu hóa từ 100 kênh Kể chuyện Audio / Podcast triệu view (Túi Mù Audio, Dứa Audio, AnAn Audio, Truyện Audio TTH):

1. TỐI ƯU HÓA GIỌNG ĐỌC EDGE-TTS CHUẨN CODEX 8.0 (Natural Neural Voice Prosody):
   - Tuyệt đối KHÔNG tua 1.5x gây méo tiếng:
     * Giọng Nữ `vi-VN-HoaiMyNeural`: rate="+5%" đến "+8%" (160 - 170 từ/phút), ấm áp, truyền cảm, châm biếm sâu cay.
     * Giọng Nam `vi-VN-NamMinhNeural`: rate="+3%" đến "+6%" (150 - 160 từ/phút), trầm ấm, đĩnh đạc, bí ẩn.
   - Tự động chữa dứt điểm lỗi dấu chấm / ba chấm giữa câu trước chữ thường khiến Edge-TTS bị khựng nhịp giữa câu.

2. CHUỖI XỬ LÝ VOCAL STUDIO RADIO (Broadcast Vocal Mastering Chain):
   - High-pass 75Hz: Triệt tiêu tiếng thở thô, tiếng va đập micro tần số thấp.
   - Warmth Boost 145Hz (+3.5dB): Tăng độ ấm dày cho lồng ngực giọng đọc.
   - Boxiness Scoop 1200Hz (-2.0dB): Xóa bỏ tiếng đục hộp nhựa, giúp giọng trong vắt.
   - Clarity Boost 3500Hz (+3.2dB): Làm sáng các thanh sắc, hỏi, ngã, nặng tiếng Việt.
   - De-Esser 6500Hz (-2.5dB): Chống chói tai ở các âm xì "s", "x".
   - Dynamic Range Compressor: Nén biên độ mượt mà, không bị giật âm lượng.

3. DYNAMIC SIDECHAIN AUTO-DUCKING (-22dB đến -24dB):
   - Nhạc nền cố định ở ngưỡng -22dB đến -24dB (volume=0.08), nhỏ hơn giọng đọc ít nhất 18dB, không át tiếng.

4. 100% CHỐNG BẢN QUYỀN TIKTOK (Anti-Copyright & Content-ID Shield):
   - Cách ly 100% bài nhạc thương mại bị gắn bản quyền gắt gao.
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
from core.voice_profiles import (
    get_voice_profile_for_genre,
    build_genre_vocal_filter_chain,
    parse_dialogue_roles,
    select_voice_and_prosody_for_script,
    VoiceProfile
)
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
        "trả thù": "đáp trả",
        "Trả thù": "Đáp trả",
        "bẩn thỉu": "xấu xa",
        "Bẩn thỉu": "Xấu xa",
        "thiêu đốt da thịt": "lạnh buốt tâm can",
        "Thiêu đốt da thịt": "Lạnh buốt tâm can",
        "thiêu đốt": "áp đảo",
        "Thiêu đốt": "Áp đảo",
        "giết người": "hại người",
        "Giết người": "Hại người",
        "chết chóc": "tang thương",
        "Chết chóc": "Tang thương",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def split_into_tts_chunks(text: str, max_words: int = 120) -> List[str]:
    """Chia văn bản thành các đoạn nhỏ 90-120 từ tại vị trí dấu câu tự nhiên, giữ nhịp thở truyền cảm."""
    clean_text = sanitize_tts_text(text)
    # Chuyển gạch ngang phân cách mệnh đề thành dấu phẩy để Edge-TTS lấy nhịp thở tự nhiên
    clean_text = re.sub(r'\s+[–—-]\s+', ', ', clean_text)
    clean_text = (
        clean_text.replace("'", " ")
        .replace('"', ' ')
        .replace("‘", " ")
        .replace("’", " ")
        .replace("“", " ")
        .replace("”", " ")
        .replace("–", ",")
        .replace("—", ",")
    )
    # Chữa dứt điểm lỗi dấu ba chấm / dấu chấm giữa câu đi trước chữ thường khiến Edge-TTS đọc khựng giọng
    clean_text = re.sub(
        r'(?:\.\.\.|…|\.\.|\.)\s+([a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ])',
        r', \1',
        clean_text
    )
    clean_text = clean_text.replace("...", ".").replace("..", ".")
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


def get_vocal_chain_filter(voice_volume: float = 1.0, genre: Optional[str] = None, scene_mood: str = "normal") -> str:
    """
    Chuỗi hiệu ứng Vocal Studio Radio Broadcast cao cấp cho FFmpeg:
    - Nếu có genre: Tự động tải Vocal Mastering Profile chuyên biệt.
    - Nếu không: Áp dụng chuỗi phát thanh cân bằng tiêu chuẩn.
    """
    if genre:
        try:
            profile = get_voice_profile_for_genre(genre)
            return build_genre_vocal_filter_chain(profile, voice_volume=voice_volume, scene_mood=scene_mood)
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
    Sinh audio Edge-TTS chất lượng cao đạt chuẩn điện ảnh (GEMINI.md Master Codex 8.0):
    - HoaiMyNeural: rate="+5%" đến "+8%" (mặc định +6%).
    - NamMinhNeural: rate="+3%" đến "+6%" (mặc định +4%).
    - Tự động chia chunk, retry với giãn cách an toàn.
    """
    if target_speed is None:
        try:
            from config.settings import VOICE_SPEED_MULTIPLIER
            target_speed = float(VOICE_SPEED_MULTIPLIER)
        except Exception:
            target_speed = 1.06

    # BẮT BUỘC: Đọc kinh nghiệm từ GEMINI.md & kiểm duyệt văn bản trước khi làm audio
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
    chunks = split_into_tts_chunks(text, max_words=120)
    chunk_files = [output_path.parent / f"{output_path.stem}_chk{i}.mp3" for i in range(len(chunks))]
    concat_list = output_path.parent / f"{output_path.stem}_concat.txt"
    raw_merged = output_path.parent / f"{output_path.stem}_raw.mp3"

    # Tự động phân tích nội dung kịch bản + thể loại để khớp 100% Giọng Đọc & Tốc Độ Nhịp Thở (Codex 8.0)
    try:
        prosody_info = select_voice_and_prosody_for_script(text=text, genre=genre or "", explicit_voice=voice)
        voice = prosody_info["voice"]
        profile_rate = prosody_info["rate"]
    except Exception:
        profile_rate = "+4%" if "NamMinh" in voice else "+6%"

    is_male = "NamMinh" in voice
    # Khi target_speed <= 1.08, tốc độ đã được Edge-TTS xử lý tự nhiên qua rate (+4%..+7%), không dùng atempo tránh méo tiếng
    atempo_factor = 1.0 if (target_speed is None or target_speed <= 1.08) else round(target_speed, 2)

    async def synth_chk(idx: int, chk_text: str, fpath: Path):
        # Tái sử dụng chunk đã tạo thành công trước đó (Resume Capability)
        if fpath.exists() and fpath.stat().st_size > 500:
            return

        for attempt in range(8):
            try:
                # Dọn dẹp file hỏng hoặc 0-byte từ lần thử trước nếu có
                if fpath.exists() and fpath.stat().st_size <= 500:
                    try:
                        fpath.unlink(missing_ok=True)
                    except Exception:
                        pass
                # Ưu tiên rate tự nhiên, không truyền pitch/volume vào SSML để triệt tiêu 100% lỗi NoAudioReceived
                if attempt < 4 and profile_rate:
                    comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate)
                else:
                    comm = edge_tts.Communicate(chk_text, voice=voice)
                await asyncio.wait_for(comm.save(str(fpath)), timeout=40.0)
                if fpath.exists() and fpath.stat().st_size > 500:
                    await asyncio.sleep(1.0)  # Giãn cách lịch sự chống bị máy chủ Edge-TTS bóp băng thông
                    return
            except Exception:
                # Dọn dẹp file dang dở nếu lỗi
                if fpath.exists() and fpath.stat().st_size <= 500:
                    try:
                        fpath.unlink(missing_ok=True)
                    except Exception:
                        pass
                # Giãn cách theo cấp số nhân để máy chủ Microsoft giải phóng rate-limit
                await asyncio.sleep(3.5 * (attempt + 1))

        # Cứu hộ khẩn cấp bằng giọng đối lập thuần túy nếu mọi nỗ lực thất bại
        if not fpath.exists() or fpath.stat().st_size <= 500:
            fallback_voice = "vi-VN-HoaiMyNeural" if is_male else "vi-VN-NamMinhNeural"
            try:
                comm = edge_tts.Communicate(chk_text, voice=fallback_voice)
                await asyncio.wait_for(comm.save(str(fpath)), timeout=40.0)
                if fpath.exists() and fpath.stat().st_size > 500:
                    await asyncio.sleep(0.2)
                    return
            except Exception:
                pass

        if not fpath.exists() or fpath.stat().st_size <= 500:
            raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after retries with {voice}")

    try:
        # Xử lý tuần tự ổn định 100%, chống nghẽn websocket
        for i, c in enumerate(chunks):
            await synth_chk(i, c, chunk_files[i])

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

        # Nếu tốc độ đã được xử lý tự nhiên qua Edge-TTS rate, giữ nguyên âm sắc mượt mà
        if abs(atempo_factor - 1.0) > 0.04:
            subprocess.run([
                ffmpeg, "-y",
                "-i", str(raw_merged),
                "-filter:a", f"atempo={atempo_factor}",
                "-c:a", "libmp3lame", "-b:a", "192k",
                str(output_path)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        else:
            subprocess.run([
                ffmpeg, "-y",
                "-i", str(raw_merged),
                "-c:a", "libmp3lame", "-b:a", "192k",
                str(output_path)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        logger.info(f"Đã tạo xong Cinema TTS Audio: {output_path.name} (Rate {profile_rate})")
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


async def generate_multi_role_cinema_tts_audio(
    text: str,
    genre: str = "TRONG_SINH",
    output_path: Optional[Path] = None,
    target_speed: Optional[float] = None
) -> Path:
    """
    Sinh audio diễn đọc ĐA VAI DIỄN (Multi-Role Voice Acting) đạt chuẩn Hollywood.
    """
    if output_path is None:
        audio_dir = ROOT_DIR / "assets" / "audio"
        audio_dir.mkdir(parents=True, exist_ok=True)
        output_path = audio_dir / "cinema_multi_role_tts_temp.mp3"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    segments = parse_dialogue_roles(text, default_genre=genre)

    if len(segments) <= 1:
        return await generate_cinema_tts_audio(
            text=text,
            genre=genre,
            output_path=output_path,
            target_speed=target_speed
        )

    ffmpeg = get_ffmpeg_exe()
    temp_files: List[Path] = []
    concat_list = output_path.parent / f"{output_path.stem}_multirole_concat.txt"
    merged_raw = output_path.parent / f"{output_path.stem}_multirole_raw.mp3"

    semaphore = asyncio.Semaphore(1)

    async def synth_segment(idx: int, profile: VoiceProfile, seg_clean: str, raw_p: Path, proc_p: Path):
        async with semaphore:
            success = False
            for attempt in range(4):
                try:
                    comm = edge_tts.Communicate(seg_clean, voice=profile.voice_name, pitch=profile.pitch, rate=profile.rate)
                    await asyncio.wait_for(comm.save(str(raw_p)), timeout=30.0)
                    if raw_p.exists() and raw_p.stat().st_size > 200:
                        success = True
                        break
                except Exception:
                    await asyncio.sleep(0.5 * (attempt + 1))

            if not success:
                try:
                    comm = edge_tts.Communicate(seg_clean, voice=profile.voice_name)
                    await asyncio.wait_for(comm.save(str(raw_p)), timeout=30.0)
                    if raw_p.exists() and raw_p.stat().st_size > 200:
                        success = True
                except Exception:
                    pass

            if not success:
                raise RuntimeError(f"Failed to synthesize segment {idx}: {seg_clean[:30]}")

            rb_pitch = profile.rubberband_pitch if profile.rubberband_pitch else 1.0
            if abs(rb_pitch - 1.0) > 0.01:
                rb_filter = f"rubberband=pitch={rb_pitch:.3f}:tempo=1.0"
                subprocess.run([
                    ffmpeg, "-y",
                    "-i", str(raw_p),
                    "-filter:a", rb_filter,
                    "-c:a", "libmp3lame", "-b:a", "192k",
                    str(proc_p)
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            else:
                proc_p = raw_p

            return proc_p

    try:
        final_seg_files: List[Path] = []
        for idx, (profile, seg_text) in enumerate(segments):
            seg_clean = sanitize_tts_text(seg_text).strip()
            if not seg_clean:
                continue

            seg_raw_path = output_path.parent / f"{output_path.stem}_seg_{idx}_raw.mp3"
            seg_processed_path = output_path.parent / f"{output_path.stem}_seg_{idx}_proc.mp3"
            temp_files.extend([seg_raw_path, seg_processed_path])

            final_p = await synth_segment(idx, profile, seg_clean, seg_raw_path, seg_processed_path)
            if final_p.exists() and final_p.stat().st_size > 200:
                final_seg_files.append(final_p)

        if not final_seg_files:
            return await generate_cinema_tts_audio(text=text, genre=genre, output_path=output_path, target_speed=target_speed)

        with open(concat_list, "w", encoding="utf-8") as f:
            for sf in final_seg_files:
                f.write(f"file '{sf.resolve().as_posix()}'\n")

        subprocess.run([
            ffmpeg, "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c", "copy",
            str(merged_raw)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        final_tempo = target_speed if (target_speed and target_speed > 1.08) else 1.0
        if abs(final_tempo - 1.0) > 0.04:
            subprocess.run([
                ffmpeg, "-y",
                "-i", str(merged_raw),
                "-filter:a", f"atempo={final_tempo:.2f}",
                "-c:a", "libmp3lame", "-b:a", "192k",
                str(output_path)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        else:
            subprocess.run([
                ffmpeg, "-y",
                "-i", str(merged_raw),
                "-c:a", "libmp3lame", "-b:a", "192k",
                str(output_path)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        logger.info(f"Đã tạo xong Multi-Role Cinema TTS Audio ({len(final_seg_files)} vai diễn): {output_path.name}")
        return output_path
    finally:
        try:
            if concat_list.exists():
                concat_list.unlink(missing_ok=True)
            if merged_raw.exists():
                merged_raw.unlink(missing_ok=True)
            for f in set(temp_files):
                if f.exists():
                    f.unlink(missing_ok=True)
        except Exception:
            pass


def mix_voice_and_safe_bgm(
    voice_audio_path: str,
    output_audio_path: str,
    genre_key: str = "TRONG_SINH",
    bgm_path: Optional[str] = None,
    bgm_volume: float = 0.08,
    voice_volume: float = 1.0
) -> str:
    """
    Ráp nối Voice + BGM an toàn với Dynamic Auto-Ducking (-22dB Codex 8.0) và Chuẩn hóa Mastering -14 LUFS.
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
