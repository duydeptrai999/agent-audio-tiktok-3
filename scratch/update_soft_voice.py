# -*- coding: utf-8 -*-
from pathlib import Path

# 1. Update config/settings.py
settings_file = Path("config/settings.py")
code = settings_file.read_text(encoding="utf-8")
code = code.replace(
    'VOICE_SPEED_MULTIPLIER = float(os.getenv("VOICE_SPEED_MULTIPLIER", "1.15"))',
    'VOICE_SPEED_MULTIPLIER = float(os.getenv("VOICE_SPEED_MULTIPLIER", "1.04"))'
)
code = code.replace('TARGET_LUFS = -14.0', 'TARGET_LUFS = -16.5')
code = code.replace(
    'VOICE_VOLUME = 1.0 # Giọng đọc 100%',
    'VOICE_VOLUME = 0.82 # Giọng đọc nhẹ nhàng, bé lại vừa vặn (82%)'
)
code = code.replace('BGM_VOLUME = 0.18', 'BGM_VOLUME = 0.16')
settings_file.write_text(code, encoding="utf-8")
print("Updated config/settings.py!")

# 2. Update core/ffmpeg_utils.py
ffmpeg_file = Path("core/ffmpeg_utils.py")
ff_code = ffmpeg_file.read_text(encoding="utf-8")
old_vocal_filter = 'vocal_filter = f"highpass=f=75,equalizer=f=145:t=q:w=1.2:g=3.5,equalizer=f=1200:t=q:w=1.5:g=-2.0,equalizer=f=3500:t=q:w=1.2:g=3.2,equalizer=f=6500:t=q:w=1.8:g=-2.5,acompressor=threshold=-18dB:ratio=3.2:attack=8:release=60,volume={voice_volume}"'
new_vocal_filter = 'vocal_filter = f"highpass=f=70,equalizer=f=160:t=q:w=1.2:g=1.5,equalizer=f=1000:t=q:w=1.5:g=-1.5,equalizer=f=3200:t=q:w=1.2:g=-1.2,equalizer=f=6000:t=q:w=1.5:g=-2.0,acompressor=threshold=-22dB:ratio=2.2:attack=15:release=120,volume={voice_volume}"'
if old_vocal_filter in ff_code:
    ff_code = ff_code.replace(old_vocal_filter, new_vocal_filter)
    ffmpeg_file.write_text(ff_code, encoding="utf-8")
    print("Updated core/ffmpeg_utils.py vocal filter!")
else:
    print("Warning: old_vocal_filter not found in core/ffmpeg_utils.py")

# 3. Update core/audio_engine.py
audio_file = Path("core/audio_engine.py")
ae_code = audio_file.read_text(encoding="utf-8")

# Update profile defaults
old_profile_setup = '''    # Tự động tối ưu Voice Profile theo thể loại (Pitch Modulation + Native Rate + Studio Mastering)
    profile_pitch = "-2Hz" if "NamMinh" in voice else "+1Hz"
    profile_rate = "+0%"
    if genre:'''

new_profile_setup = '''    # Tự động tối ưu Voice Profile theo thể loại: Giọng êm dịu, ấm áp, thủ thỉ, bé lại
    profile_pitch = "-1Hz" if "NamMinh" in voice else "-1Hz"
    profile_rate = "+2%"
    profile_volume = "-15%"
    if genre:'''

ae_code = ae_code.replace(old_profile_setup, new_profile_setup)

# Pass rate, pitch, volume to edge_tts.Communicate
old_comm = 'comm = edge_tts.Communicate(chk_text, voice=voice)'
new_comm = 'comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate, pitch=profile_pitch, volume=profile_volume)'
ae_code = ae_code.replace(old_comm, new_comm)

old_fallback = 'comm = edge_tts.Communicate(chk_text, voice=fallback_voice)'
new_fallback = 'comm = edge_tts.Communicate(chk_text, voice=fallback_voice, rate=profile_rate, pitch=profile_pitch, volume=profile_volume)'
ae_code = ae_code.replace(old_fallback, new_fallback)

# Smooth atempo filter
old_atempo = '''        # Tua nhẹ atempo để đạt tròn 1.50x
        subprocess.run([
            ffmpeg, "-y",
            "-i", str(raw_merged),
            "-filter:a", f"atempo={atempo_factor}",
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(output_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)'''

new_atempo = '''        # Nếu tốc độ đã được xử lý tự nhiên qua Edge-TTS rate, giữ nguyên âm sắc mượt mà
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
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)'''

ae_code = ae_code.replace(old_atempo, new_atempo)

audio_file.write_text(ae_code, encoding="utf-8")
print("Updated core/audio_engine.py!")
