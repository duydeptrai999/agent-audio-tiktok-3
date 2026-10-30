# -*- coding: utf-8 -*-
import os
import shutil

src_dir = "TikTok_BGM_Audio"
dst_dir = "assets/bgm"
os.makedirs(dst_dir, exist_ok=True)

copied = 0
for f in os.listdir(src_dir):
    if f.endswith(".mp3") and not f.endswith(".bak.mp3") and not f.startswith("temp_"):
        src = os.path.join(src_dir, f)
        dst = os.path.join(dst_dir, f)
        shutil.copy2(src, dst)
        copied += 1
        print(f"Copied: {f} -> {dst_dir} ({os.path.getsize(dst)} bytes)")

print(f"\nDone syncing {copied} BGM files to {dst_dir}.")
