# -*- coding: utf-8 -*-
with open("core/ffmpeg_utils.py", "r", encoding="utf-8") as f:
    text = f.read()

t_clean = text.replace("\r\r\n", "\n").replace("\r\n", "\n")

# Update probe fallbacks
t_clean = t_clean.replace(
    'vid_w = vid_probe.get("width") or 1080\n    vid_h = vid_probe.get("height") or 1920',
    'vid_w = vid_probe.get("width") or 1920\n    vid_h = vid_probe.get("height") or 1080'
)

with open("core/ffmpeg_utils.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(t_clean)

print("Cleaned core/ffmpeg_utils.py line endings and updated fallbacks!")
