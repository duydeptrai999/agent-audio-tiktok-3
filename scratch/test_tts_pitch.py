# -*- coding: utf-8 -*-
import asyncio
import edge_tts
from pathlib import Path

async def test_edge():
    text = "Đêm khuya thanh vắng, tiếng bước chân chầm chậm vang lên ngoài hành lang."
    comm = edge_tts.Communicate(text, voice="vi-VN-NamMinhNeural", rate="-4%", pitch="-4Hz", volume="-14%")
    out = Path("scratch/test_tts.mp3")
    await comm.save(str(out))
    print(f"Success! Output size: {out.stat().st_size} bytes")

asyncio.run(test_edge())
