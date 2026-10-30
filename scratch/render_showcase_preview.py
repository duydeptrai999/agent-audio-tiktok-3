import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from core.ffmpeg_utils import get_ffmpeg_exe

ffmpeg = get_ffmpeg_exe()
audio = Path("assets/audio/showcase_codex8_hoaimy_cinema.mp3")
video = Path("assets/footage/baking_vertical.mp4")
output = Path("assets/output/showcase_codex8_preview.mp4")
output.parent.mkdir(parents=True, exist_ok=True)

# Combine video (looping) and audio, cropped/scaled to 1080x1920 (9:16), duration matching audio
cmd = [
    ffmpeg, "-y",
    "-ss", "10", # skip intro
    "-i", str(video),
    "-i", str(audio),
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
    str(output)
]

print("Rendering showcase preview video (35s)...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if res.returncode == 0:
    print(f"SUCCESS! Output created: {output.resolve()} (Size: {output.stat().st_size} bytes)")
else:
    print(f"ERROR: {res.stderr}")
