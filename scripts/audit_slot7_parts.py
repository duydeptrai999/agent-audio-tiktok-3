# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from pathlib import Path
from core.video_audit_engine import VideoAuditEngine

def main():
    prefix = 'VID_20261024_s07_slot_07_giadau'
    title = 'Màn Trả Thù Đã Nhất Đời Tôi: Bát Canh Sau Sinh Của Mẹ Chồng Và Căn Chung Cư Đứng Tên Tôi'

    for p in [1, 2, 3]:
        v = Path(f'assets/output/{prefix}_part{p}_final.mp4')
        a = Path(f'assets/audio/{prefix}_part{p}_cinema.mp3')
        passed, report, metrics = VideoAuditEngine.audit_video_before_publish(
            video_path=v,
            audio_path=a,
            title=title,
            prefix=prefix,
            part_num=p,
            caption=f'Tập {p}: {title}'
        )
        tag = "PASSED ✅" if passed else "FAILED ❌"
        print(f"=== PART {p} AUDIT: {tag} ===")
        print(f"File: {v.name} ({v.stat().st_size / 1024 / 1024:.2f} MB)")
        print(f"Duration: {metrics.get('duration')}s ({float(metrics.get('duration', 0))/60:.2f} mins)")
        print(f"Resolution: {metrics.get('resolution')} | Bitrate: {metrics.get('bitrate_kbps')} kbps")
        print(f"Voice Clarity: {metrics.get('voice_clarity_score')} | BGM Ducking: {metrics.get('bgm_ducking_score')}dB")
        if not passed:
            print("Errors:", metrics.get('errors'))
        print("-" * 60)

if __name__ == "__main__":
    main()
