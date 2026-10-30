# -*- coding: utf-8 -*-
import asyncio
import edge_tts
from pathlib import Path

async def test_param(name, **kwargs):
    text = "Đêm khuya thanh vắng, tiếng bước chân chầm chậm vang lên ngoài hành lang."
    out = Path(f"scratch/test_{name}.mp3")
    try:
        comm = edge_tts.Communicate(text, voice="vi-VN-NamMinhNeural", **kwargs)
        await comm.save(str(out))
        print(f"[{name}] SUCCESS! Size: {out.stat().st_size}")
    except Exception as e:
        print(f"[{name}] FAILED: {type(e).__name__}: {e}")

async def main():
    await test_param("rate_only", rate="-4%")
    await test_param("pitch_hz", pitch="-4Hz")
    await test_param("pitch_pct", pitch="-5%")
    await test_param("vol_pct", volume="-14%")

asyncio.run(main())
