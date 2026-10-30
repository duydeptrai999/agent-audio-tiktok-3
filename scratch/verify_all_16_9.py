import sys
from pathlib import Path
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from core.ffmpeg_utils import probe_media_file, get_ffmpeg_exe
import subprocess

videos = [
    'VID_20261027_s06_slot_06_haomon_part1_final.mp4',
    'VID_20261027_s06_slot_06_haomon_part2_final.mp4',
    'VID_20261027_s06_slot_06_haomon_part3_final.mp4',
    'VID_20261027_s07_slot_07_giadau_part3_final.mp4',
]

ffmpeg = get_ffmpeg_exe()
print("=== KIỂM TOÁN TẤT CẢ VIDEO THÀNH PHẨM 16:9 ===")
all_ok = True
for name in videos:
    p = Path('assets/output') / name
    pr = probe_media_file(p)
    w, h = pr.get('width'), pr.get('height')
    dur = pr.get('duration', 0)
    is_16_9 = (w == 1920 and h == 1080)
    tag = "CHÍNH XÁC 16:9 (1920x1080)" if is_16_9 else "SAI LỆCH!"
    print(f"{name}:")
    print(f"   Độ phân giải: {w}x{h} -> {tag}")
    print(f"   Thời lượng: {dur:.1f}s ({dur/60:.1f} phút) | Có Audio: {pr.get('has_audio')} | Valid: {pr.get('is_valid')}")
    if not is_16_9:
        all_ok = False
        
    frame_p = Path('scratch') / f'frame_{name}.jpg'
    subprocess.run([ffmpeg, '-y', '-ss', '10', '-i', str(p), '-vframes', '1', str(frame_p)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"   Frame kiểm tra: {frame_p.name} (Tồn tại: {frame_p.exists()})")

print("\nKẾT QUẢ CUỐI CÙNG:", "TẤT CẢ 100% ĐẠT CHUẨN 16:9 NGUYÊN BẢN!" if all_ok else "LỖI!")
