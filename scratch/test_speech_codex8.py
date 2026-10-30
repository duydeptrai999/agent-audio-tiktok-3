import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

import edge_tts

text_sample = """Ngày tôi xuất viện sau khi sinh con gái, mẹ chồng tôi không hề đến đón. 

Mãi đến gần mười một giờ trưa, khi các sản phụ cùng phòng đã được gia đình nội ngoại xúm xít đón về trong tiếng cười rạng rỡ, bà mới gửi cho tôi một tin nhắn ngắn ngủn qua Zalo: Con gái thì bồi bổ tốn kém làm gì, chiều tự bắt xe mà về. 

Chồng tôi khi ấy đang ngồi ở chiếc ghế nhựa bên mép giường bệnh, hai mắt dán chặt vào màn hình điện thoại xem bóng đá ngoại hạng Anh. Thấy tôi lặng người nhìn chằm chằm vào dòng tin nhắn trên màn hình, anh ta ngước mắt lên liếc nhìn một cái rồi buông một câu bâng quơ: 

Mẹ già rồi, tính bà ở quê ăn sóng nói gió quen mồm từ xưa đến nay, em để bụng làm gì cho mệt người. Giờ sinh xong rồi thì thu dọn đồ đạc cá nhân vào túi, anh gọi chiếc xe công nghệ rồi hai mẹ con mình về nhà nghỉ ngơi.

Tôi không khóc, cũng chẳng buồn cãi lại anh ta nửa lời. Tôi chỉ khẽ cúi xuống, cẩn thận chỉnh lại góc chăn bông màu hồng nhạt cho con gái bé bỏng đang ngủ say sưa trong lòng mình. 

Nhiều người phụ nữ khi rơi vào hoàn cảnh đó có lẽ sẽ tủi thân đến mức bật khóc nức nở, sẽ chất vấn người đàn ông bên cạnh xem tình nghĩa vợ chồng suốt ba năm qua rốt cuộc đáng giá bao nhiêu. Nhưng tôi thì khác. Năm năm làm quản lý dự án cho một công ty công nghệ đã rèn luyện cho tôi một cái đầu rất lạnh và một thói quen quan sát thực tế."""

async def test_speech():
    voice = "vi-VN-HoaiMyNeural"
    output_file = Path("assets/audio/test_codex8_hoaimy_natural.mp3")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Synthesizing sample with voice {voice} at rate=+6%...")
    comm = edge_tts.Communicate(text_sample, voice=voice, rate="+6%", pitch="+0Hz")
    await comm.save(str(output_file))
    print(f"DONE! File saved at: {output_file.resolve()} (Size: {output_file.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(test_speech())
