import asyncio
import os
import re
import sys
import subprocess
import tempfile
import edge_tts
import imageio_ffmpeg

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

async def test_dur(text: str, label: str):
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp.close()
    try:
        await edge_tts.Communicate(text, "vi-VN-HoaiMyNeural", rate="+4%").save(tmp.name)
        res = subprocess.run([ffmpeg, "-i", tmp.name], capture_output=True, text=True)
        m = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}\.\d+)", res.stderr)
        if m:
            h, mn, s = m.groups()
            dur = float(h) * 3600 + float(mn) * 60 + float(s)
            print(f"{label} ({len(text.split())} words): {dur:.2f}s | '{text}'")
    finally:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)

async def main():
    print("=== OLD HOOK TEMPLATES ===")
    await test_dur("Ngay đêm tân hôn, tôi mở tủ quần áo ra... thì thấy cô bạn thân đang khỏa thân trốn bên trong!", "Old T1")
    await test_dur("Mẹ chồng hắt thẳng bát canh nóng vào mặt tôi: 'Đồ cau điếc! Mau ký đơn ly hôn rồi cút khỏi nhà tao!'.", "Old T2")
    await test_dur("Mẹ chồng ném xấp séc mười tỷ vào mặt tôi: 'Cầm tiền rồi biến khỏi mắt con trai tôi ngay lập tức!'.", "Old T3")
    
    print("\n=== NEW CALIBRATED HOOK TEMPLATES ===")
    await test_dur("Đêm tân hôn, tôi chết lặng thấy bạn thân trốn trong tủ quần áo!", "New T1")
    await test_dur("Mẹ chồng hắt canh nóng, bắt tôi ly hôn rồi cút khỏi nhà!", "New T2")
    await test_dur("Mẹ chồng ném mười tỷ ép tôi rời xa con trai bà ngay lập tức!", "New T3")

if __name__ == "__main__":
    asyncio.run(main())
