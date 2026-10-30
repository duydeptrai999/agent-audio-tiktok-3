# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from pathlib import Path
import subprocess
import imageio_ffmpeg
from scripts.daily_24h_master_autopilot import probe_media_file

def main():
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    concat_list = Path('assets/output/concat_list_s07_master.txt')
    p1 = Path('assets/output/VID_20261024_s07_slot_07_giadau_part1_final.mp4')
    p2 = Path('assets/output/VID_20261024_s07_slot_07_giadau_part2_final.mp4')
    p3 = Path('assets/output/VID_20261024_s07_slot_07_giadau_part3_final.mp4')
    out_master = Path('assets/output/VID_20261024_s07_slot_07_giadau_MASTER_30MIN_FULL.mp4')

    with open(concat_list, 'w', encoding='utf-8') as f:
        f.write(f"file '{p1.resolve().as_posix()}'\n")
        f.write(f"file '{p2.resolve().as_posix()}'\n")
        f.write(f"file '{p3.resolve().as_posix()}'\n")

    res = subprocess.run([
        ffmpeg, '-y', '-f', 'concat', '-safe', '0',
        '-i', str(concat_list),
        '-c', 'copy',
        str(out_master)
    ], capture_output=True, text=True)

    try:
        concat_list.unlink()
    except:
        pass

    if res.returncode == 0:
        info = probe_media_file(out_master)
        dur = float(info.get('duration', 0))
        size_mb = out_master.stat().st_size / 1024 / 1024
        print(f"✅ Master 30-Minute Video: {out_master.name} | Size: {size_mb:.2f} MB | Duration: {dur:.1f}s ({dur/60:.2f} mins)")
    else:
        print("❌ Failed:", res.stderr[:500])

if __name__ == "__main__":
    main()
