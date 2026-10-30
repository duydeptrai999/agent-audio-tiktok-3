import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")
from core.ffmpeg_utils import probe_media_file

print("=== assets/output ===")
for p in sorted(Path("assets/output").glob("*.mp4"), key=lambda x: x.stat().st_mtime, reverse=True)[:10]:
    pr = probe_media_file(p)
    w, h = pr.get("width"), pr.get("height")
    ratio = f"{w}:{h}" if w and h else "unknown"
    is_16_9 = abs(w/h - 16/9) < 0.05 if w and h else False
    is_9_16 = abs(w/h - 9/16) < 0.05 if w and h else False
    print(f"{p.name}: {w}x{h} ({'16:9' if is_16_9 else ('9:16' if is_9_16 else ratio)}) - {p.stat().st_size} bytes - {p.stat().st_mtime}")

print("\n=== Check publisher logs / state ===")
for p in Path("data").glob("*.*"):
    print(p.name, p.stat().st_size)
