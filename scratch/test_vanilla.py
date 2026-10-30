# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import asyncio
import edge_tts
from scratch.test_c7 import text

async def t():
    comm = edge_tts.Communicate(text, voice='vi-VN-HoaiMyNeural')
    await comm.save('test_c7_vanilla.mp3')
    import os
    print('Vanilla success! Size:', os.path.getsize('test_c7_vanilla.mp3'))

asyncio.run(t())
