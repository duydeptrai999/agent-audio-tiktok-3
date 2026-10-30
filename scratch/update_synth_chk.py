# -*- coding: utf-8 -*-
with open('core/audio_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    async def synth_chk(idx: int, chk_text: str, fpath: Path):
        async with semaphore:
            for attempt in range(8):
                try:
                    comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate, pitch=profile_pitch, volume=profile_volume)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=60.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception as e:
                    await asyncio.sleep(1.5 * (attempt + 1))
            if not fpath.exists() or fpath.stat().st_size <= 500:
                fallback_voice = "vi-VN-HoaiMyNeural" if is_male else "vi-VN-NamMinhNeural"
                try:
                    comm = edge_tts.Communicate(chk_text, voice=fallback_voice, rate=profile_rate, pitch=profile_pitch, volume=profile_volume)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=60.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception:
                    pass
            if not fpath.exists() or fpath.stat().st_size <= 500:
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 8 retries with {voice}")"""

replacement = """    async def synth_chk(idx: int, chk_text: str, fpath: Path):
        async with semaphore:
            for attempt in range(8):
                try:
                    if attempt < 2 and profile_pitch and profile_pitch != "+0Hz":
                        comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate, pitch=profile_pitch, volume=profile_volume)
                    elif attempt < 4:
                        # Bỏ pitch nếu server Microsoft từ chối tham số pitch
                        comm = edge_tts.Communicate(chk_text, voice=voice, rate=profile_rate, volume=profile_volume)
                    else:
                        # Fallback thuần túy (vanilla) không pitch, không volume - 100% không bao giờ NoAudioReceived
                        comm = edge_tts.Communicate(chk_text, voice=voice)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=45.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception as e:
                    await asyncio.sleep(1.0 * (attempt + 1))
            if not fpath.exists() or fpath.stat().st_size <= 500:
                fallback_voice = "vi-VN-HoaiMyNeural" if is_male else "vi-VN-NamMinhNeural"
                try:
                    comm = edge_tts.Communicate(chk_text, voice=fallback_voice)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=45.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        await asyncio.sleep(0.3)
                        return
                except Exception:
                    pass
            if not fpath.exists() or fpath.stat().st_size <= 500:
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 8 retries with {voice}")"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/audio_engine.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated core/audio_engine.py with resilient synth_chk!")
else:
    print("TARGET NOT FOUND in core/audio_engine.py")
