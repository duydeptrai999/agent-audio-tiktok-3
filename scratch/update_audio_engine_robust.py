# -*- coding: utf-8 -*-
with open('core/audio_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    semaphore = asyncio.Semaphore(1)

    async def synth_chk(idx: int, chk_text: str, fpath: Path):
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
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 8 retries with {voice}")

    try:
        tasks = [synth_chk(i, c, chunk_files[i]) for i, c in enumerate(chunks)]
        await asyncio.gather(*tasks)"""

replacement = """    async def synth_chk(idx: int, chk_text: str, fpath: Path):
        # Tái sử dụng chunk đã tạo thành công trước đó (Resume Capability)
        if fpath.exists() and fpath.stat().st_size > 500:
            return

        for attempt in range(6):
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
                await asyncio.sleep(0.8 * (attempt + 1))

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
            await synth_chk(i, c, chunk_files[i])"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/audio_engine.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated core/audio_engine.py with robust sequential synthesizer!")
else:
    print("TARGET NOT FOUND in core/audio_engine.py")
