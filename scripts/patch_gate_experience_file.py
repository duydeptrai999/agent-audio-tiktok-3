# -*- coding: utf-8 -*-
import sys

target_file = 'core/stories/script_quality_gate.py'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_str1 = 'EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md"'
new_str1 = '''EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md"
if not EXPERIENCE_100_FILE.exists():
    EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md"'''

old_str2 = 'Nạp thành công SIÊU FILE TOÀN TẬP: docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md'
new_str2 = 'Nạp thành công SIÊU FILE TOÀN TẬP: docs/DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md'

if old_str1 in content and old_str2 in content:
    content = content.replace(old_str1, new_str1)
    content = content.replace(old_str2, new_str2)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated script_quality_gate.py successfully!')
else:
    print('Target strings not found!')
