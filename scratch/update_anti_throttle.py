# -*- coding: utf-8 -*-
with open('core/audio_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        for attempt in range(6):
            try:
                # Ưu tiên rate tự nhiên, không truyền pitch/volume vào SSML để triệt tiêu 100% lỗi NoAudioReceived
                if attempt < 3 and profile_rate:
                    comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate)
                else:
                    comm = edge_tts.Communicate(chk_text, voice=voice)
                await asyncio.wait_for(comm.save(str(fpath)), timeout=40.0)
                if fpath.exists() and fpath.stat().st_size > 500:
                    await asyncio.sleep(0.2)
                    return
            except Exception as e:
                await asyncio.sleep(0.8 * (attempt + 1))"""

replacement = """        for attempt in range(8):
            try:
                # Ưu tiên rate tự nhiên, không truyền pitch/volume vào SSML để triệt tiêu 100% lỗi NoAudioReceived
                if attempt < 4 and profile_rate:
                    comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate)
                else:
                    comm = edge_tts.Communicate(chk_text, voice=voice)
                await asyncio.wait_for(comm.save(str(fpath)), timeout=40.0)
                if fpath.exists() and fpath.stat().st_size > 500:
                    await asyncio.sleep(1.0)  # Giãn cách lịch sự chống bị máy chủ Edge-TTS bóp băng thông
                    return
            except Exception as e:
                # Giãn cách theo cấp số nhân để máy chủ Microsoft giải phóng rate-limit
                await asyncio.sleep(3.5 * (attempt + 1))"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/audio_engine.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated core/audio_engine.py with anti-throttle backoff!")
else:
    print("TARGET NOT FOUND in core/audio_engine.py")
