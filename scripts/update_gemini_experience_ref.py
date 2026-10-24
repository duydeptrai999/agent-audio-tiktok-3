# -*- coding: utf-8 -*-
from pathlib import Path

gemini = Path("GEMINI.md")
content = gemini.read_text(encoding="utf-8")

old_ref = "PHẢI đọc qua `GEMINI.md`, `docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md`"
new_ref = "PHẢI đọc qua `GEMINI.md`, `docs/DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md`, `docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md`"

if old_ref in content:
    content = content.replace(old_ref, new_ref)
    gemini.write_text(content, encoding="utf-8")
    print("Updated GEMINI.md experience ref successfully!")
else:
    print("Old ref not found!")
