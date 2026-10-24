# -*- coding: utf-8 -*-
"""
scripts/wire_tiktok_100_experience.py
Nạp docs/DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md vào script_quality_gate.py
"""
from pathlib import Path

target_file = Path("core/stories/script_quality_gate.py")
content = target_file.read_text(encoding="utf-8")

old_wire = '''EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md"'''

new_wire = '''EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md"
EXPERIENCE_100_TIKTOK_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md"'''

if old_wire in content:
    content = content.replace(old_wire, new_wire)

old_load = '''        print("   Nap thanh cong: GEMINI.md + docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md + docs/50_CYCLES_SCRIPT_EVOLUTION_MASTERCLASS.md (Master Codex 5.0)")'''

new_load = '''        print("   Nap thanh cong: GEMINI.md + docs/DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md (Master Codex 6.0)")'''

if old_load in content:
    content = content.replace(old_load, new_load)

target_file.write_text(content, encoding="utf-8")
print("Wired 100 TikTok audio experience successfully!")
