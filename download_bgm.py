import os
import sys
import subprocess
import imageio_ffmpeg

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

output_dir = r"c:\Users\duydo\OneDrive\Tài liệu\idk\TikTok_BGM_Audio"
os.makedirs(output_dir, exist_ok=True)
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

single_tracks = [
    {
        "url": "https://www.youtube.com/watch?v=cbi1Davilac",
        "filename": "01 - Senorita (Instrumental) - 16+ Romance.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=3VdLLGfxfzM",
        "filename": "02 - Thu Qua Dong Sang Ha Nho (Instrumental) - Sad Romance.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=3E6O_p99olk",
        "filename": "03 - Cause I Love You (Instrumental) - Dramatic Romance.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=cPZD4KOI7v0",
        "filename": "04 - Fox Rain Acoustic - Romance BGM.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=6fAQcdy57F8",
        "filename": "05 - Da Lau Khong Gap - Ben Nhau Tron Doi OST.mp3"
    }
]

print("=== 1. TAI CAC BAI DON LE ===")
for item in single_tracks:
    out_path = os.path.join(output_dir, item["filename"])
    if os.path.exists(out_path):
        print(f"Da co: {item['filename']}")
        continue
    print(f"Dang tai: {item['filename']}...")
    cmd = [
        "yt-dlp",
        "--ffmpeg-location", ffmpeg_exe,
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", out_path,
        item["url"]
    ]
    subprocess.run(cmd, check=True)
    print(f"Da xong: {item['filename']}")

print("\n=== 2. TAI VA TACH PLAYLIST TONG HOP ===")
playlist_url = "https://www.youtube.com/watch?v=oEwrAwb_4jM"
full_playlist_file = os.path.join(output_dir, "Playlist_Tong_Hop_Audio.mp3")

if not os.path.exists(full_playlist_file):
    print("Dang tai toan bo video playlist...")
    cmd = [
        "yt-dlp",
        "--ffmpeg-location", ffmpeg_exe,
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", full_playlist_file,
        playlist_url
    ]
    subprocess.run(cmd, check=True)
    print("Da tai xong file playlist tong hop.")

# Danh sach bai can cat theo timestamp:
# [00:00] fallin' flower [03:45] cry for me [08:30] bong la roi [09:48] nguoi yeu bo lo [14:40] nham mat thay mua he [19:16] thieu nien hoa hong
segments = [
    {"name": "06 - Fallin Flower.mp3", "start": "00:00:00", "to": "00:03:45"},
    {"name": "07 - Cry For Me.mp3", "start": "00:03:45", "to": "00:08:30"},
    {"name": "08 - Bong La Roi.mp3", "start": "00:08:30", "to": "00:09:48"},
    {"name": "09 - Nguoi Yeu Bo Lo.mp3", "start": "00:09:48", "to": "00:14:40"},
    {"name": "10 - Nham Mat Thay Mua He.mp3", "start": "00:14:40", "to": "00:19:16"},
    {"name": "11 - Thieu Nien Hoa Hong.mp3", "start": "00:19:16", "to": None}
]

for seg in segments:
    seg_out = os.path.join(output_dir, seg["name"])
    if os.path.exists(seg_out):
        print(f"Da co: {seg['name']}")
        continue
    print(f"Dang cat track: {seg['name']} ({seg['start']} -> {seg['to'] or 'End'})...")
    cut_cmd = [ffmpeg_exe, "-y", "-ss", seg["start"]]
    if seg["to"]:
        cut_cmd.extend(["-to", seg["to"]])
    cut_cmd.extend(["-i", full_playlist_file, "-c", "copy", seg_out])
    subprocess.run(cut_cmd, check=True)
    print(f"Cat xong: {seg['name']}")

print("\n>>> TAT CA FILE DA DUOC TAI VA TACH THANH CONG VAO THU MUC: TikTok_BGM_Audio <<<")
