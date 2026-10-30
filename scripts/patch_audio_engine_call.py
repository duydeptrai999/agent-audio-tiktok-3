# -*- coding: utf-8 -*-
with open("core/audio_engine.py", "r", encoding="utf-8") as f:
    text = f.read()

old_call = "comm = edge_tts.Communicate(chk_text, voice=voice, pitch=profile_pitch, rate=profile_rate)"
new_call = "comm = edge_tts.Communicate(chk_text, voice=voice)"

if old_call in text:
    text = text.replace(old_call, new_call)
    with open("core/audio_engine.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed audio_engine.py edge_tts call successfully!")
else:
    print("Could not find old_call in audio_engine.py")
