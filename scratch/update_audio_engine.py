# -*- coding: utf-8 -*-
with open('core/audio_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    # Tự động tối ưu Voice Profile theo thể loại: Giọng êm dịu, ấm áp, thủ thỉ, bé lại
    profile_pitch = "-1Hz" if "NamMinh" in voice else "-1Hz"
    profile_rate = "+2%"
    profile_volume = "-15%"
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
            pass"""

replacement = """    # Tự động tối ưu Voice Profile theo thể loại: Giọng êm dịu, ấm áp, thủ thỉ, bé lại hoặc kinh dị rùng rợn
    profile_pitch = "-3Hz" if "NamMinh" in voice else "-1Hz"
    profile_rate = "+1%"
    profile_volume = "-15%"
    if genre:
        try:
            profile = get_voice_profile_for_genre(genre)
            profile_pitch = profile.pitch
            profile_rate = profile.rate
            if getattr(profile, 'volume', None):
                profile_volume = profile.volume
            if voice == "vi-VN-HoaiMyNeural" and "MALE" in profile.profile_id:
                voice = profile.voice_name
            elif voice == "vi-VN-NamMinhNeural" and "FEMALE" in profile.profile_id:
                voice = profile.voice_name
            if target_speed is None or target_speed == 1.15:
                target_speed = profile.tempo_multiplier
        except Exception:
            pass"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/audio_engine.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated core/audio_engine.py")
else:
    print("TARGET NOT FOUND in core/audio_engine.py")
