import os

import re

import sys

import shutil

import subprocess

from pathlib import Path

from typing import Optional, List

def get_ffmpeg_exe() -> str:

    """Trả về đường dẫn tới binary FFmpeg (từ imageio_ffmpeg hoặc system PATH)"""

    try:

        import imageio_ffmpeg

        exe = imageio_ffmpeg.get_ffmpeg_exe()

        if exe and os.path.exists(exe):

            return exe

    except Exception:

        pass

    

    system_exe = shutil.which("ffmpeg")

    if system_exe:

        return system_exe

    raise RuntimeError("Không tìm thấy FFmpeg binary trên hệ thống.")

def get_vietnamese_font_path() -> str:

    """Tìm font hỗ trợ 100% tiếng Việt (ưu tiên Be Vietnam Pro trong assets/fonts, sau đó tới font hệ thống)"""

    root_fonts = Path(__file__).resolve().parent.parent / "assets" / "fonts"

    candidate_fonts = [

        str(root_fonts / "BeVietnamPro-Bold.ttf"),

        str(root_fonts / "BeVietnamPro-ExtraBold.ttf"),

        r"C:\Windows\Fonts\segoeuib.ttf",  # Segoe UI Bold

        r"C:\Windows\Fonts\arialbd.ttf",   # Arial Bold

        r"C:\Windows\Fonts\tahomabd.ttf",  # Tahoma Bold

        r"C:\Windows\Fonts\arial.ttf"

    ]

    for font in candidate_fonts:

        if os.path.exists(font):

            escaped = font.replace("\\", "/").replace(":", "\\:")

            return escaped

    return ""

def _wrap_title_for_916(title: str, max_chars_per_line: int = 28, max_lines: int = 3) -> List[str]:

    """Ngắt dòng thông minh cho tiêu đề trên khung dọc 9:16 (1080px ngang), chống tràn lề."""

    words = title.split()

    lines: List[str] = []

    cur: List[str] = []

    for w in words:

        candidate = " ".join(cur + [w])

        if len(candidate) <= max_chars_per_line or not cur:

            cur.append(w)

        else:

            lines.append(" ".join(cur))

            cur = [w]

    if cur:

        lines.append(" ".join(cur))

    if len(lines) > max_lines:

        lines = lines[:max_lines]

        if not lines[-1].endswith("..."):

            lines[-1] = lines[-1][:max(10, max_chars_per_line - 3)].rstrip() + "..."

    return lines

def create_real_clean_footage(output_file: Path, duration: int = 600, is_sleep: bool = False, source_video: Optional[Path] = None) -> str:

    """

    Sử dụng video nền thực tế (Baking, Nature, Craft) chuẩn dọc 9:16 (1080x1920).

    Hỗ trợ thời lượng lên tới 10 phút (600 giây).

    """

    output_file.parent.mkdir(parents=True, exist_ok=True)

    ffmpeg = get_ffmpeg_exe()

    # 1. Nếu có file source_video chỉ định hợp lệ (> 100KB) - GIỮ NGUYÊN KHUNG HÌNH GỐC

    if source_video and Path(source_video).exists() and Path(source_video).stat().st_size > 100000:

        cmd = [

            ffmpeg, "-y",

            "-i", str(source_video),

            "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",

            "-an",

            str(output_file)

        ]

        try:

            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

            return str(output_file)

        except subprocess.TimeoutExpired:

            print(f"[FFmpeg Error] Timeout 180s khi xử lý source video {source_video}")

    # 2. Ưu tiên file baking_vertical.mp4 chuẩn dọc 9:16

    sample_baking = output_file.parent / "baking_vertical.mp4"

    if sample_baking.exists() and sample_baking.stat().st_size > 1000000:

        cmd = [

            ffmpeg, "-y",

            "-i", str(sample_baking),

            "-c:v", "copy",

            "-an",

            str(output_file)

        ]

        try:

            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

            return str(output_file)

        except subprocess.TimeoutExpired:

            print(f"[FFmpeg Error] Timeout 180s khi copy baking footage")

    # 3. Kiểm tra kho video gốc trong raw_downloaded và crop sang 9:16

    raw_dir = output_file.parent / "raw_downloaded"

    if raw_dir.exists():

        raw_candidates = list(raw_dir.glob("*.mp4"))

        if raw_candidates:

            raw_vid = raw_candidates[0]

            cmd = [

                ffmpeg, "-y",

                "-i", str(raw_vid),

                "-vf", vf_916,

                "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",

                "-an",

                str(output_file)

            ]

            try:

                subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

                return str(output_file)

            except subprocess.TimeoutExpired:

                print(f"[FFmpeg Error] Timeout 180s khi crop raw video {raw_vid}")

    # Fallback tạo background gradient chuyển động dọc 9:16 (1080x1920)

    if is_sleep:

        filter_str = (

            "gradients=s=1080x1920:c0=0x08081a:c1=0x121430:c2=0x1c1e40:x0=0:y0=0:x1=1080:y1=1920:r=30,"

            "format=yuv420p"

        )

    else:

        filter_str = (

            "gradients=s=1080x1920:c0=0x0a192f:c1=0x112240:c2=0x233554:x0=0:y0=0:x1=1080:y1=1920:r=30,"

            "format=yuv420p"

        )

    cmd = [

        ffmpeg, "-y",

        "-f", "lavfi",

        "-i", filter_str,

        "-t", str(duration),

        "-c:v", "libx264",

        "-preset", "ultrafast",

        "-pix_fmt", "yuv420p",

        "-r", "30",

        str(output_file)

    ]

    try:

        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

    except subprocess.TimeoutExpired:

        print(f"[FFmpeg Error] Timeout 180s khi render gradient background")

    return str(output_file)

def generate_melodic_bgm(output_mp3: Path, is_sleep: bool = False, duration: int = 60) -> str:

    """Tạo nhạc nền không lời có giai điệu thực thụ (Melodic Piano/Lo-Fi Chords)"""

    import math, struct, wave

    output_mp3.parent.mkdir(parents=True, exist_ok=True)

    sample_rate = 44100

    num_samples = sample_rate * duration

    if is_sleep:

        chords = [

            [261.63, 329.63, 392.00, 493.88],

            [220.00, 261.63, 329.63, 392.00],

            [174.61, 220.00, 261.63, 329.63],

            [196.00, 246.94, 293.66, 329.63],

        ]

        tempo = 3.0

    else:

        chords = [

            [146.83, 174.61, 220.00],

            [116.54, 146.83, 174.61],

            [98.00,  116.54, 146.83],

            [110.00, 138.59, 164.81],

        ]

        tempo = 3.5

    wav_path = str(output_mp3) + ".tmp.wav"

    try:

        with wave.open(wav_path, "w") as wav:

            wav.setnchannels(1)

            wav.setsampwidth(2)

            wav.setframerate(sample_rate)

            frames = bytearray()

            for i in range(num_samples):

                t = i / sample_rate

                chord = chords[int(t / tempo) % len(chords)]

                t_in_chord = t % tempo

                attack = 0.4

                decay = tempo - attack

                env = (t_in_chord / attack) if t_in_chord < attack else math.exp(-2.0 * (t_in_chord - attack) / decay)

                sample = 0.0

                for note_idx, freq in enumerate(chord):

                    s = math.sin(2 * math.pi * freq * t) + 0.35 * math.sin(4 * math.pi * freq * t)

                    arp_env = math.exp(-3.0 * ((t_in_chord + note_idx * 0.2) % 0.8))

                    sample += s * (0.6 * env + 0.4 * arp_env)

                sample = sample / (len(chord) * 1.4)

                lfo = 0.9 + 0.1 * math.sin(2 * math.pi * 0.5 * t)

                val = int(sample * lfo * 18000)

                val = max(-32767, min(32767, val))

                frames.extend(struct.pack("<h", val))

            wav.writeframes(frames)

        ffmpeg = get_ffmpeg_exe()

        cmd = [ffmpeg, "-y", "-i", wav_path, "-c:a", "libmp3lame", "-b:a", "128k", str(output_mp3)]

        try:

            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

        except subprocess.TimeoutExpired:

            print(f"[FFmpeg Error] Timeout 180s khi encode BGM {output_mp3}")

    finally:

        if os.path.exists(wav_path):

            try:

                os.remove(wav_path)

            except Exception:

                pass

    return str(output_mp3)

def create_real_bgm(output_file: Path, duration: int = 600, is_sleep: bool = False) -> str:

    """Tạo nhạc nền không lời có giai điệu du dương/kịch tính kéo dài tới 10 phút"""

    output_file.parent.mkdir(parents=True, exist_ok=True)

    return generate_melodic_bgm(output_file, is_sleep=is_sleep, duration=60)

def create_fallback_audio(output_file: Path, duration: int = 15) -> str:

    """Tạo audio MP3 chuẩn làm fallback an toàn tuyệt đối khi mạng gặp sự cố tạm thời"""

    output_file.parent.mkdir(parents=True, exist_ok=True)

    ffmpeg = get_ffmpeg_exe()

    cmd = [

        ffmpeg, "-y",

        "-f", "lavfi",

        "-i", "anoisesrc=c=pink:r=44100:a=0.01,lowpass=f=300",

        "-t", str(duration),

        "-c:a", "libmp3lame",

        "-b:a", "128k",

        str(output_file)

    ]

    try:

        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)

    except subprocess.TimeoutExpired:

        print(f"[FFmpeg Error] Timeout 180s khi tạo fallback audio {output_file}")

    return str(output_file)

def render_playable_video(

    output_file: Path,

    voice_audio_path: str,

    clean_footage_path: str,

    bgm_audio_path: str,

    badge_label: str = "",

    bgm_volume: float = 0.08,

    voice_volume: float = 0.96,

    srt_path: Optional[str] = None,

    enable_subtitles: Optional[bool] = None,

    thumbnail_path: Optional[str] = None,

    title_text: str = "",

    genre: str = ""

) -> str:

    """

    Ráp nối Voice (Hoài My / Nam Minh) + Video nền Dọc 9:16 (1080x1920 Full-Screen) + BGM Ducking -22dB + Header Overlay + Kinetic Subtitles.

    Tuân thủ 100% chuẩn Master Codex 8.0:

    - Tự động chuyển hóa mọi nguồn video nền về khung dọc 1080x1920 (9:16), xóa sạch viền đen trên điện thoại.

    - Đặt Header Overlay trong suốt (font Be Vietnam Pro + Pill Badge + bóng đổ mềm, KHÔNG có hộp nền đen) ở vùng Safe Zone phía trên.

    - Đặt Phụ đề động (Kinetic Captions) ở 1/3 dưới màn hình (Safe Zone).

    """

    output_file.parent.mkdir(parents=True, exist_ok=True)

    ffmpeg = get_ffmpeg_exe()

    has_bgm = bool(bgm_audio_path) and str(bgm_audio_path).lower() not in ["none", "", "null"] and bgm_volume > 0.01

    if has_bgm:

        try:

            from core.bgm_manager import ensure_safe_bgm

            bgm_audio_path = ensure_safe_bgm(bgm_audio_path)

        except Exception:

            if not os.path.exists(bgm_audio_path) or os.path.getsize(bgm_audio_path) < 1000:

                bgm_base = Path(__file__).resolve().parent.parent / "assets" / "bgm"

                for cand in [

                    bgm_base / "suspense" / "tiktok_horror_suspense.mp3",

                    bgm_base / "chill" / "chill_instrumental.mp3",

                    bgm_base / "chill" / "chopin_romance.mp3",

                    bgm_base / "test_bgm.mp3"

                ]:

                    if cand.exists() and cand.stat().st_size > 1000:

                        bgm_audio_path = str(cand)

                        break

        if not os.path.exists(bgm_audio_path) or os.path.getsize(bgm_audio_path) < 1000:

            has_bgm = False

    if not os.path.exists(voice_audio_path) or os.path.getsize(voice_audio_path) < 1000:

        print(f"[FFmpeg Warning] Voice audio {voice_audio_path} không tồn tại hoặc lỗi, tự động tạo audio chuẩn...")

        create_fallback_audio(Path(voice_audio_path), duration=300)

    # 1. GIỮ NGUYÊN 100% KHUNG HÌNH GỐC CỦA VIDEO (Zero Crop / Zero Stretch / Zero Fit)

    # Tuyệt đối KHÔNG crop, KHÔNG scale ép fit khung hình làm méo video!

    base_vf = "null"

    # Lấy kích thước thực tế của video nền để vẽ Header Overlay vừa vặn hoàn hảo

    vid_probe = probe_media_file(Path(clean_footage_path))

    vid_w = vid_probe.get("width") or 1920
    vid_h = vid_probe.get("height") or 1080

    # 2. Tạo Header Overlay PNG trong suốt khớp đúng kích thước video gốc

    header_png_path: Optional[Path] = None

    if title_text or badge_label:

        try:

            from core.visual_design import render_video_header_overlay

            header_png_path = output_file.parent / f"temp_hdr_{output_file.stem}.png"

            render_video_header_overlay(

                output_png=header_png_path,

                title=title_text or badge_label,

                part_label=badge_label or "TẬP 1",

                genre=genre or title_text,

                width=vid_w,

                height=vid_h

            )

        except Exception as hdr_err:

            print(f"[FFmpeg Warning] Không thể tạo header PNG overlay ({hdr_err}), dùng khung hình sạch.")

            header_png_path = None

    if enable_subtitles is None:

        try:

            from config.settings import ENABLE_SUBTITLES

            enable_subtitles = ENABLE_SUBTITLES

        except Exception:

            enable_subtitles = True

    # 3. Khắc phụ đề động Kinetic Subtitles ở 1/3 dưới màn hình (Safe Zone)

    sub_filter = ""

    if enable_subtitles and srt_path and os.path.exists(srt_path) and os.path.getsize(srt_path) > 10:

        try:

            from core.subtitle_engine import get_tiktok_subtitles_filter_param

            sub_filter = get_tiktok_subtitles_filter_param(

                Path(srt_path),

                color_scheme=getattr(sys.modules.get('config.settings'), 'SUBTITLE_COLOR', 'yellow'),

                font_size=getattr(sys.modules.get('config.settings'), 'SUBTITLE_FONT_SIZE', 16),

                margin_v=getattr(sys.modules.get('config.settings'), 'SUBTITLE_MARGIN_V', 68)

            )

        except Exception:

            escaped_srt = str(Path(srt_path).resolve()).replace("\\", "/").replace(":", "\\:")

            sub_filter = (

                f"subtitles='{escaped_srt}':force_style='FontSize=16,FontName=Arial,Bold=1,"

                f"PrimaryColour=&H0000FFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,Alignment=2,MarginV=68'"

            )

    has_hdr = header_png_path is not None and header_png_path.exists()

    hdr_idx = (3 if has_bgm else 2) if has_hdr else -1

    if has_hdr and sub_filter:

        v_chain = f"[0:v]{base_vf}[v_base];[v_base][{hdr_idx}:v]overlay=0:0,{sub_filter}[vout]"

    elif has_hdr:

        v_chain = f"[0:v]{base_vf}[v_base];[v_base][{hdr_idx}:v]overlay=0:0[vout]"

    elif sub_filter:

        v_chain = f"[0:v]{base_vf},{sub_filter}[vout]"

    else:

        v_chain = f"[0:v]{base_vf}[vout]"

    # 4. Nạp tham số Sidechain Ducking chuẩn điện ảnh (BGM -22dB đến -24dB theo Codex 8.0)

    ducking_thresh = 0.079

    ducking_ratio = 4.0

    ducking_attack = 25

    ducking_release = 750

    ducking_knee = 2.5

    target_lufs = -16.0

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

    # Studio Radio Vocal Mastering: Giọng trong trẻo, ấm áp, rõ từng chữ ngay từ giây 0.0

    vocal_filter = (

        f"highpass=f=75,"

        f"equalizer=f=150:t=q:w=1.2:g=2.2,"

        f"equalizer=f=1100:t=q:w=1.5:g=-1.5,"

        f"equalizer=f=3300:t=q:w=1.2:g=2.5,"

        f"equalizer=f=6500:t=q:w=1.5:g=-2.2,"

        f"acompressor=threshold=-20dB:ratio=2.6:attack=12:release=100,"

        f"volume={voice_volume}"

    )

    if genre:

        try:

            from core.voice_profiles import get_voice_profile_for_genre, build_genre_vocal_filter_chain

            prof = get_voice_profile_for_genre(genre)

            vocal_filter = build_genre_vocal_filter_chain(prof, voice_volume=voice_volume)

        except Exception:

            pass

    if has_bgm:

        filter_complex = (

            f"{v_chain};"

            f"[1:a]{vocal_filter},asplit=2[v_play][v_trigger];"

            f"[2:a]silenceremove=start_periods=1:start_duration=0:start_threshold=-38dB,volume={bgm_volume},highpass=f=70,equalizer=f=1800:t=q:w=1.2:g=-4.5[bgm_prep];"

            f"[bgm_prep][v_trigger]sidechaincompress=threshold={ducking_thresh}:ratio={ducking_ratio}:attack={ducking_attack}:release={ducking_release}:knee={ducking_knee}[bgm_ducked];"

            f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"

        )

        cmd = [

            ffmpeg, "-y",

            "-stream_loop", "-1",

            "-i", clean_footage_path,

            "-i", voice_audio_path,

            "-stream_loop", "-1",

            "-i", bgm_audio_path,

        ]

        if has_hdr:

            cmd.extend(["-i", str(header_png_path)])

        cmd.extend([

            "-filter_complex", filter_complex,

            "-map", "[vout]",

            "-map", "[aout]",

            "-c:v", "libx264",

            "-preset", "ultrafast",

            "-pix_fmt", "yuv420p",

            "-c:a", "aac",

            "-b:a", "192k",

            "-shortest",

            str(output_file)

        ])

    else:

        filter_complex = (

            f"{v_chain};"

            f"[1:a]{vocal_filter},loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"

        )

        cmd = [

            ffmpeg, "-y",

            "-stream_loop", "-1",

            "-i", clean_footage_path,

            "-i", voice_audio_path,

        ]

        if has_hdr:

            cmd.extend(["-i", str(header_png_path)])

        cmd.extend([

            "-filter_complex", filter_complex,

            "-map", "[vout]",

            "-map", "[aout]",

            "-c:v", "libx264",

            "-preset", "ultrafast",

            "-pix_fmt", "yuv420p",

            "-c:a", "aac",

            "-b:a", "192k",

            "-shortest",

            str(output_file)

        ])

    try:

        try:

            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)

        except subprocess.TimeoutExpired:

            print(f"[FFmpeg Warning] Timeout 600s khi render video chính ({output_file.name})!")

            result = subprocess.CompletedProcess(cmd, returncode=1, stdout=b"", stderr=b"TimeoutExpired after 600s")

        if result.returncode != 0:

            err_msg = result.stderr.decode("utf-8", errors="ignore")

            print(f"[FFmpeg Warning] Fallback filter: {err_msg[:200]}")

            vf_only_916 = "null"  # Giữ nguyên khung hình gốc của video, không crop/scale

            if has_bgm:

                simple_filter = (

                    f"[0:v]{vf_only_916}[vout];"

                    f"[1:a]{vocal_filter},asplit=2[v_play][v_trigger];"

                    f"[2:a]volume={bgm_volume},highpass=f=70,equalizer=f=1800:t=q:w=1.2:g=-4.5[bgm_prep];"

                    f"[bgm_prep][v_trigger]sidechaincompress=threshold={ducking_thresh}:ratio={ducking_ratio}:attack={ducking_attack}:release={ducking_release}:knee={ducking_knee}[bgm_ducked];"

                    f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"

                )

                fallback_cmd = [

                    ffmpeg, "-y",

                    "-stream_loop", "-1",

                    "-i", clean_footage_path,

                    "-i", voice_audio_path,

                    "-stream_loop", "-1",

                    "-i", bgm_audio_path,

                    "-filter_complex", simple_filter,

                    "-map", "[vout]",

                    "-map", "[aout]",

                    "-c:v", "libx264",

                    "-preset", "ultrafast",

                    "-pix_fmt", "yuv420p",

                    "-c:a", "aac",

                    "-b:a", "192k",

                    "-shortest",

                    str(output_file)

                ]

            else:

                simple_filter = (

                    f"[0:v]{vf_only_916}[vout];"

                    f"[1:a]{vocal_filter},loudnorm=I={target_lufs}:TP={true_peak}:LRA=8[aout]"

                )

                fallback_cmd = [

                    ffmpeg, "-y",

                    "-stream_loop", "-1",

                    "-i", clean_footage_path,

                    "-i", voice_audio_path,

                    "-filter_complex", simple_filter,

                    "-map", "[vout]",

                    "-map", "[aout]",

                    "-c:v", "libx264",

                    "-preset", "ultrafast",

                    "-pix_fmt", "yuv420p",

                    "-c:a", "aac",

                    "-b:a", "192k",

                    "-shortest",

                    str(output_file)

                ]

            try:

                subprocess.run(fallback_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=600)

            except subprocess.TimeoutExpired:

                print(f"[FFmpeg Error] Timeout 600s khi render video fallback ({output_file.name})!")

    finally:

        if header_png_path is not None and header_png_path.exists():

            try:

                header_png_path.unlink(missing_ok=True)

            except Exception:

                pass

    return str(output_file)

def probe_media_file(file_path: Path) -> dict:

    """Đo đạc chính xác thời lượng, độ phân giải và audio stream của file media qua FFprobe/FFmpeg"""

    ffmpeg = get_ffmpeg_exe()

    try:

        res = subprocess.run([ffmpeg, "-i", str(file_path)], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, timeout=180)

        dur_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)

        duration_sec = 0.0

        if dur_match:

            h, m, s = dur_match.groups()

            duration_sec = int(h) * 3600 + int(m) * 60 + float(s)

            

        dim_match = re.search(r"Video:.*,\s*(\d{3,4})x(\d{3,4})", res.stderr)

        width, height = (0, 0)

        if dim_match:

            width, height = int(dim_match.group(1)), int(dim_match.group(2))

            

        has_audio = "Audio:" in res.stderr

        return {

            "duration": duration_sec,

            "width": width,

            "height": height,

            "has_audio": has_audio,

            "is_valid": duration_sec > 1.0

        }

    except subprocess.TimeoutExpired:

        return {"duration": 0.0, "width": 0, "height": 0, "has_audio": False, "is_valid": False, "error": "TimeoutExpired after 180s"}

    except Exception as e:

        return {"duration": 0.0, "width": 0, "height": 0, "has_audio": False, "is_valid": False, "error": str(e)}

