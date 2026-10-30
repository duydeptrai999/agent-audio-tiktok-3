import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from core.ffmpeg_utils import get_ffmpeg_exe

ffmpeg = get_ffmpeg_exe()
vocal = Path("assets/audio/test_codex8_hoaimy_natural.mp3")
bgm = Path("TikTok_BGM_Audio/04 - Fox Rain Acoustic - Romance BGM.mp3")
output = Path("assets/audio/showcase_codex8_hoaimy_cinema.mp3")

# We mix vocal (volume=1.0) and BGM (ducked at -22dB, volume=0.08)
cmd = [
    ffmpeg, "-y",
    "-i", str(vocal),
    "-stream_loop", "-1", "-i", str(bgm),
    "-filter_complex",
    "[0:a]volume=1.0[vocal];"
    "[1:a]volume=0.08[bgm];"
    "[vocal][bgm]amix=inputs=2:duration=first:dropout_transition=2[out]",
    "-map", "[out]",
    "-c:a", "libmp3lame", "-b:a", "192k",
    str(output)
]

print("Mixing vocal and ducked BGM...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if res.returncode == 0:
    print(f"SUCCESS! Output created: {output.resolve()} (Size: {output.stat().st_size} bytes)")
else:
    print(f"ERROR: {res.stderr}")
