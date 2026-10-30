import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read the full 100 cases file
with open('docs/FILE_KINH_NGHIEM_SAN_XUAT_AUDIO_TIKTOK_TRIEU_VIEW.md', 'r', encoding='utf-8') as f:
    source_content = f.read()

# Verify how many cases are present
cases = re.findall(r'### 🎧 Case Study #(\d+):', source_content)
print(f"Loaded {len(cases)} cases from source file.")

# Check the sections in source_content
print("Source length:", len(source_content))

# Now let's enhance the frontmatter and chapters with Master Codex 8.0:
# 1. Anti-Cringe & Human-Ear Manifesto (Triệt tiêu hoàn toàn bệnh hoạt hình ba xu, mẹ chồng 3 cổ gà, 4 vệ sĩ bọc thép).
# 2. Spoken Vietnamese & Natural Inner Monologue (Túi Mù & Dứa Audio style).
# 3. 5 Multi-Dimensional Pillars.
# 4. ALL 100 Case Studies (#001 to #100).
# 5. 6-Subagent Optimization Matrix.

# Let's inspect where Phần 2 (100 cases) starts in source_content
split_p2 = "## PHẦN 2: KHO BÁU 100 CASE STUDY AUDIO TRIỆU VIEW THỰC CHIẾN TẠI VIỆT NAM"
if split_p2 in source_content:
    print("Found Phần 2 marker!")
    parts = source_content.split(split_p2)
    part1_and_intro = parts[0]
    cases_and_rest = split_p2 + parts[1]
    print("Intro length:", len(part1_and_intro))
    print("Cases and rest length:", len(cases_and_rest))
else:
    print("Marker not found, please check header.")
