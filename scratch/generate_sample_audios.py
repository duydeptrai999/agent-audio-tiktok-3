# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.audio_engine import generate_cinema_tts_audio

sample_gentle_text = """
Tôi ngồi bên ô cửa sổ quán trà nhỏ quen thuộc trên phố cổ, ngắm nhìn từng giọt mưa mùa thu tí tách rơi trên tán cây bàng đỏ rực. Chiếc tách sứ trên tay vẫn còn bốc làn khói ấm, thoang thoảng mùi hoa cúc thơm dịu. Mười năm trước, cũng vào một chiều mưa giăng ngập lối như thế này, có một người đã cẩn thận nhét chiếc ô màu xanh ngọc bích vào cặp sách của tôi rồi chạy vội đi dưới làn mưa rào. Lời hứa năm mười bảy tuổi tưởng như đã ngủ yên trong ký ức, vậy mà mỗi khi mùa thu trở về, trái tim tôi vẫn bồi hồi khôn nguôi như thuở ban đầu.
""".strip()

sample_horror_text = """
Kim đồng hồ vừa điểm đúng hai giờ sáng, cả khu tập thể cũ kỹ chìm sâu vào sự tĩnh mịch lạnh lẽo đến rợn người. Bỗng nhiên, từ sâu bên dưới gầm giường gỗ mục, một âm thanh cào cọt khẽ khàng bắt đầu vang lên. Két... két... từng nhát móng tay khô khốc như đang miết chậm rãi vào thanh gỗ lát sàn. Tôi nín chặt hơi thở, toàn thân cứng đờ dưới lớp chăn mỏng. Khi ánh mắt tôi vừa liếc xuống khe hở chân giường, một đôi mắt đỏ ngầu không hề chớp đang lạnh lùng nhìn thẳng vào tôi từ trong bóng tối u uất.
""".strip()

async def main():
    audio_dir = Path("assets/audio")
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    out_gentle = audio_dir / "sample_gentle_hoaimy_optimized.mp3"
    out_horror = audio_dir / "sample_eerie_horror_namminh_optimized.mp3"
    
    print("🎙️ Đang sinh mẫu giọng NHẸ NHÀNG (Hoài My - Thanh xuân / Chữa lành / Gia đấu)...")
    await generate_cinema_tts_audio(
        text=sample_gentle_text,
        voice="vi-VN-HoaiMyNeural",
        output_path=out_gentle,
        target_speed=1.0,
        genre="Thanh Xuân Vườn Trường"
    )
    print(f"✅ Đã tạo xong: {out_gentle.name} ({out_gentle.stat().st_size} bytes)")
    
    print("🎙️ Đang sinh mẫu giọng KINH DỊ RÙNG RỢN (Nam Minh - Quái đàm / Kỳ án)...")
    await generate_cinema_tts_audio(
        text=sample_horror_text,
        voice="vi-VN-NamMinhNeural",
        output_path=out_horror,
        target_speed=1.0,
        genre="Kinh Dị Rùng Rợn"
    )
    print(f"✅ Đã tạo xong: {out_horror.name} ({out_horror.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
