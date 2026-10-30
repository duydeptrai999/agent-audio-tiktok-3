# -*- coding: utf-8 -*-
import asyncio
import edge_tts
import os

async def test():
    text = "Tôi ngồi bên ô cửa sổ quán trà nhỏ quen thuộc trên phố cổ, ngắm nhìn từng giọt mưa mùa thu tí tách rơi trên tán cây bàng đỏ rực."
    comm = edge_tts.Communicate(text, voice='vi-VN-HoaiMyNeural', pitch='-1Hz', rate='+1%', volume='-15%')
    await comm.save('test_hoaimy.mp3')
    print('File size:', os.path.getsize('test_hoaimy.mp3'))

asyncio.run(test())
