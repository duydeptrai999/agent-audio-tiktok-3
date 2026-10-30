# -*- coding: utf-8 -*-
with open("core/ffmpeg_utils.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_probe = """    vid_probe = probe_media_file(Path(clean_footage_path))
    vid_w = vid_probe.get("width") or 1080
    vid_h = vid_probe.get("height") or 1920"""

new_probe = """    vid_probe = probe_media_file(Path(clean_footage_path))
    vid_w = vid_probe.get("width") or 1920
    vid_h = vid_probe.get("height") or 1080"""

assert old_probe in t_norm, "old_probe not found"
t_norm = t_norm.replace(old_probe, new_probe)

final = t_norm.replace("\n", "\r\n")
with open("core/ffmpeg_utils.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated core/ffmpeg_utils.py fallbacks to 1920x1080!")
