import os
import sys
import subprocess
import imageio_ffmpeg

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

output_dir = r"c:\Users\duydo\OneDrive\Tài liệu\idk\Horror_BGM_Audio"
os.makedirs(output_dir, exist_ok=True)
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

horror_tracks = [
    {
        "url": "https://www.youtube.com/watch?v=pT4FY3NrhGg",
        "filename": "01 - Halloween Theme - John Carpenter.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=cv3OPTt5pLQ",
        "filename": "02 - Hello Zepp (Saw Theme) - Charlie Clouser.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=FN6jIvKiYOs",
        "filename": "03 - Tubular Bells (The Exorcist Theme) - Mike Oldfield.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=zcSlcNfThUA",
        "filename": "04 - Tip Toe Thru The Tulips (Insidious) - Tiny Tim.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=gcQVMhL-PgY",
        "filename": "05 - The Murder (Psycho Shower Scene) - Bernard Herrmann.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=jb7MeX7iZE4",
        "filename": "06 - Sweet Dreams Are Made Of Screams - Myuu.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=xADSDapqn9o",
        "filename": "07 - Its Just A Burning Memory - The Caretaker.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=hQZfGa5t4e8",
        "filename": "08 - 13 Angels Standing Guard - ASMZ.mp3"
    },
    {
        "url": "https://www.youtube.com/watch?v=HH_BruxBHq8",
        "filename": "09 - In Essence (Slowed + Reverb) - Ka$tro.mp3"
    }
]

print("=== TAI CAC BAI NHAC KINH DI ===")
for item in horror_tracks:
    out_path = os.path.join(output_dir, item["filename"])
    if os.path.exists(out_path):
        print(f"Da co: {item['filename']}")
        continue
    print(f"Dang tai: {item['filename']}...")
    cmd = [
        "yt-dlp",
        "--ffmpeg-location", ffmpeg_exe,
        "--extractor-args", "youtube:player_client=android,web",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", out_path,
        item["url"]
    ]
    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f"Da xong: {item['filename']}")
    else:
        print(f"Loi tai: {item['filename']}, thu lai voi search...")
        cmd_fallback = [
            "yt-dlp",
            "--ffmpeg-location", ffmpeg_exe,
            "-x",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", out_path,
            f"ytsearch1:{item['filename'].replace('.mp3', '')}"
        ]
        subprocess.run(cmd_fallback)

print("\n>>> KIEM TRA HOAN TAT THU MUC Horror_BGM_Audio <<<")
