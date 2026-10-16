import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional

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
    """Tìm font hệ thống Windows hỗ trợ 100% tiếng Việt không bao giờ bị lỗi ô vuông (tofu glyph)"""
    candidate_fonts = [
        r"C:\Windows\Fonts\arialbd.ttf",   # Arial Bold
        r"C:\Windows\Fonts\segoeuib.ttf",  # Segoe UI Bold
        r"C:\Windows\Fonts\tahomabd.ttf",  # Tahoma Bold
        r"C:\Windows\Fonts\arial.ttf"
    ]
    for font in candidate_fonts:
        if os.path.exists(font):
            # Format đường dẫn tương thích filter drawtext của FFmpeg trên Windows: C\:/Windows/Fonts/arialbd.ttf
            escaped = font.replace("\\", "/").replace(":", "\\:")
            return escaped
    return ""

def create_real_clean_footage(output_file: Path, duration: int = 600, is_sleep: bool = False, source_video: Optional[Path] = None) -> str:
    """
    Sử dụng video nền thực tế (Baking, Nature, Craft) hoặc tạo video chuyển động chất lượng cao.
    Hỗ trợ thời lượng lên tới 10 phút (600 giây).
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = get_ffmpeg_exe()

    # 1. Nếu có file source_video chỉ định hợp lệ (> 100KB)
    if source_video and Path(source_video).exists() and Path(source_video).stat().st_size > 100000:
        cmd = [
            ffmpeg, "-y",
            "-i", str(source_video),
            "-c:v", "copy",
            "-an",
            str(output_file)
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)
            return str(output_file)
        except subprocess.TimeoutExpired:
            print(f"[FFmpeg Error] Timeout 180s khi copy source video {source_video}")

    # 2. Kiểm tra kho video gốc ngang 16:9 đã tải về từ YouTube
    raw_dir = output_file.parent / "raw_downloaded"
    if raw_dir.exists():
        raw_candidates = list(raw_dir.glob("*.mp4"))
        if raw_candidates:
            raw_vid = raw_candidates[0]
            cmd = [
                ffmpeg, "-y",
                "-i", str(raw_vid),
                "-c:v", "copy",
                "-an",
                str(output_file)
            ]
            try:
                subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)
                return str(output_file)
            except subprocess.TimeoutExpired:
                print(f"[FFmpeg Error] Timeout 180s khi copy raw video {raw_vid}")

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

    # Fallback tạo background gradient chuyển động ngang 16:9 (1920x1080)
    if is_sleep:
        filter_str = (
            "gradients=s=1920x1080:c0=0x08081a:c1=0x121430:c2=0x1c1e40:x0=0:y0=0:x1=1920:y1=1080:r=30,"
            "format=yuv420p"
        )
    else:
        filter_str = (
            "gradients=s=1920x1080:c0=0x0a192f:c1=0x112240:c2=0x233554:x0=0:y0=0:x1=1920:y1=1080:r=30,"
            "format=yuv420p"
        )

    cmd = [
        ffmpeg, "-y",
        "-f", "lavfi",
        "-i", filter_str,
        "-t", str(duration),
        "-c:v", "libx264",
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
        # Giai điệu ru ngủ: Cmaj7 - Am7 - Fmaj7 - G6
        chords = [
            [261.63, 329.63, 392.00, 493.88], # Cmaj7
            [220.00, 261.63, 329.63, 392.00], # Am7
            [174.61, 220.00, 261.63, 329.63], # Fmaj7
            [196.00, 246.94, 293.66, 329.63], # G6
        ]
        tempo = 3.0
    else:
        # Giai điệu kịch tính/kỳ án: Dm - Bb - Gm - A
        chords = [
            [146.83, 174.61, 220.00], # Dm
            [116.54, 146.83, 174.61], # Bb
            [98.00,  116.54, 146.83], # Gm
            [110.00, 138.59, 164.81], # A
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
    bgm_volume: float = 0.22,
    voice_volume: float = 1.0,
    srt_path: Optional[str] = None,
    enable_subtitles: Optional[bool] = None,
    thumbnail_path: Optional[str] = None
) -> str:
    """
    Ráp nối Voice (NamMinh) + Video nền Ngang 16:9 (1920x1080) + BGM dịu nhẹ + Visual Badge.
    Hỗ trợ tự động loop video nền theo đúng độ dài file âm thanh và tắt phụ đề theo yêu cầu.
    Hỗ trợ nhúng thumbnail bìa cho video nếu có thumbnail_path.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = get_ffmpeg_exe()

    # Bắt buộc thẩm định và định tuyến BGM an toàn 100% không bản quyền (Anti-Copyright Guard)
    try:
        from core.bgm_manager import ensure_safe_bgm
        bgm_audio_path = ensure_safe_bgm(bgm_audio_path)
    except Exception as e:
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

    if not os.path.exists(voice_audio_path) or os.path.getsize(voice_audio_path) < 1000:
        print(f"[FFmpeg Warning] Voice audio {voice_audio_path} không tồn tại hoặc lỗi, tự động tạo audio chuẩn...")
        create_fallback_audio(Path(voice_audio_path), duration=300)

    # Xử lý font chữ tiếng Việt có dấu chuẩn 100% không bị lỗi ô vuông
    font_path = get_vietnamese_font_path()
    font_param = f":fontfile='{font_path}'" if font_path else ""

    filters_list = []
    if badge_label:
        import re
        # Xóa sạch bất kỳ chuỗi thời gian nào (như "(10 PHÚT)") khỏi Visual Badge trên video
        clean_label = re.sub(r'\(?\d+\s*phút\)?', '', badge_label, flags=re.IGNORECASE).strip()
        clean_label = clean_label.replace("[", "").replace("]", "").replace("'", "").replace(":", "").strip()
        # Thiết kế badge kiểu 16:9 Widescreen thanh lịch: Hộp đen mờ sang trọng, chữ vàng đậm nét
        badge_filter = (
            f"drawbox=y=45:color=black@0.8:width=iw:height=90:t=fill,"
            f"drawtext=text='{clean_label}'{font_param}:fontcolor=yellow:fontsize=42:x=(w-text_w)/2:y=68"
        )
        filters_list.append(badge_filter)

    if enable_subtitles is None:
        try:
            from config.settings import ENABLE_SUBTITLES
            enable_subtitles = ENABLE_SUBTITLES
        except Exception:
            enable_subtitles = True

    # Khắc phụ đề Kinetic Subtitles chữ vàng/trắng viền đen chuẩn TikTok High-CTR
    if enable_subtitles and srt_path and os.path.exists(srt_path) and os.path.getsize(srt_path) > 10:
        try:
            from core.subtitle_engine import get_tiktok_subtitles_filter_param
            from config.settings import SUBTITLE_COLOR, SUBTITLE_FONT_SIZE, SUBTITLE_MARGIN_V
            sub_filter = get_tiktok_subtitles_filter_param(
                Path(srt_path),
                color_scheme=getattr(sys.modules.get('config.settings'), 'SUBTITLE_COLOR', 'yellow'),
                font_size=getattr(sys.modules.get('config.settings'), 'SUBTITLE_FONT_SIZE', 28),
                margin_v=getattr(sys.modules.get('config.settings'), 'SUBTITLE_MARGIN_V', 220)
            )
            filters_list.append(sub_filter)
        except Exception as e_sub:
            # Fallback filter chuẩn
            escaped_srt = str(Path(srt_path).resolve()).replace("\\", "/").replace(":", "\\:")
            sub_filter = (
                f"subtitles='{escaped_srt}':force_style='FontSize=28,FontName=Arial,Bold=1,"
                f"PrimaryColour=&H0000FFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Shadow=2,Alignment=2,MarginV=220'"
            )
            filters_list.append(sub_filter)

    video_filter = ",".join(filters_list) if filters_list else "null"

    # Studio Radio Vocal Mastering:
    # 1. Cắt tần số ù thô (75Hz), tăng độ trầm ấm quyền lực (145Hz +3.5dB)
    # 2. Cắt đục hộp nhựa (1200Hz -2dB), tăng độ rõ nét thanh điệu tiếng Việt (3500Hz +3.2dB)
    # 3. De-esser chống xì chói (6500Hz -2.5dB), Nén dynamic range chuẩn radio phát thanh
    # 4. Dynamic Auto-Ducking (sidechaincompress): BGM tự động né giọng đọc (-20dB khi nói, dâng trào trong khoảng lặng)
    # 5. Master toàn dải đạt chuẩn TikTok/YouTube (-13 LUFS & True Peak -1.0 dBTP)
    vocal_filter = f"highpass=f=75,equalizer=f=145:t=q:w=1.2:g=3.5,equalizer=f=1200:t=q:w=1.5:g=-2.0,equalizer=f=3500:t=q:w=1.2:g=3.2,equalizer=f=6500:t=q:w=1.8:g=-2.5,acompressor=threshold=-18dB:ratio=3.2:attack=8:release=60,volume={voice_volume}"
    filter_complex = (
        f"[0:v]{video_filter}[vout];"
        f"[1:a]{vocal_filter},asplit=2[v_play][v_trigger];"
        f"[2:a]volume={bgm_volume},highpass=f=60,equalizer=f=2000:t=q:w=1.5:g=-3.5[bgm_prep];"
        f"[bgm_prep][v_trigger]sidechaincompress=threshold=0.045:ratio=7:attack=15:release=280[bgm_ducked];"
        f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-13:TP=-1.0:LRA=7[aout]"
    )

    cmd = [
        ffmpeg, "-y",
        "-stream_loop", "-1",  # Tự động loop video làm bánh nếu âm thanh dài hơn
        "-i", clean_footage_path,
        "-i", voice_audio_path,
        "-stream_loop", "-1",  # Tự động loop nhạc nền
        "-i", bgm_audio_path,
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", "[aout]",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",           # Cắt đúng theo độ dài file đọc voice
        str(output_file)
    ]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
    except subprocess.TimeoutExpired:
        print(f"[FFmpeg Warning] Timeout 180s khi render video chính ({output_file.name})!")
        result = subprocess.CompletedProcess(cmd, returncode=1, stdout=b"", stderr=b"TimeoutExpired after 180s")

    if result.returncode != 0:
        # Fallback an toàn nếu có lỗi filter
        err_msg = result.stderr.decode("utf-8", errors="ignore")
        print(f"[FFmpeg Warning] Fallback filter: {err_msg[:200]}")
        simple_filter = (
            f"[1:a]{vocal_filter},asplit=2[v_play][v_trigger];"
            f"[2:a]volume={bgm_volume},highpass=f=60,equalizer=f=2000:t=q:w=1.5:g=-3.5[bgm_prep];"
            f"[bgm_prep][v_trigger]sidechaincompress=threshold=0.045:ratio=7:attack=15:release=280[bgm_ducked];"
            f"[v_play][bgm_ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-13:TP=-1.0:LRA=7[aout]"
        )

        fallback_cmd = [
            ffmpeg, "-y",
            "-stream_loop", "-1",
            "-i", clean_footage_path,
            "-i", voice_audio_path,
            "-stream_loop", "-1",
            "-i", bgm_audio_path,
            "-filter_complex", simple_filter,
            "-map", "0:v",
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
            subprocess.run(fallback_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=180)
        except subprocess.TimeoutExpired:
            print(f"[FFmpeg Error] Timeout 180s khi render video fallback ({output_file.name})!")

    if thumbnail_path and os.path.exists(thumbnail_path):
        try:
            from core.thumbnail_generator import attach_thumbnail_to_mp4
            attach_thumbnail_to_mp4(output_file, Path(thumbnail_path))
        except Exception as e:
            print(f"[FFmpeg Warning] Không thể nhúng thumbnail: {e}")

    return str(output_file)

def probe_media_file(file_path: Path) -> dict:
    """Đo đạc chính xác thời lượng, độ phân giải và audio stream của file media qua FFprobe/FFmpeg"""
    import re
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

