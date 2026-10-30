# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path("core/ffmpeg_utils.py")
text = p.read_text(encoding="utf-8")
text = text.replace("\r\r\n", "\n").replace("\r\n", "\n")

# Collapse 3 or more newlines into 2
text = re.sub(r"\n{3,}", "\n\n", text)

# Replace probe defaults: if width/height probe fails or returns 0, default to 1920x1080 (16:9 native)
old_line_1 = 'vid_w = vid_probe.get("width") or 1080\n    vid_h = vid_probe.get("height") or 1920'
old_line_2 = 'vid_w = vid_probe.get("width") or 1080\n\n    vid_h = vid_probe.get("height") or 1920'
new_line = 'vid_w = vid_probe.get("width") or 1920\n    vid_h = vid_probe.get("height") or 1080'

if old_line_1 in text:
    text = text.replace(old_line_1, new_line)
elif old_line_2 in text:
    text = text.replace(old_line_2, new_line)
else:
    # regex fallback
    text = re.sub(
        r'vid_w\s*=\s*vid_probe\.get\("width"\)\s*or\s*1080\s*\n\s*vid_h\s*=\s*vid_probe\.get\("height"\)\s*or\s*1920',
        'vid_w = vid_probe.get("width") or 1920\n    vid_h = vid_probe.get("height") or 1080',
        text
    )

p.write_text(text, encoding="utf-8", newline="\n")
print("Done fixing core/ffmpeg_utils.py!")
