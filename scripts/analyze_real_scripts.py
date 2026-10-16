import sys
import re
import json
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def parse_vtt(vtt_path: Path):
    text_lines = []
    seen = set()
    with open(vtt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tách các khối timestamp và text
    blocks = re.split(r'\n\n+', content)
    for b in blocks:
        lines = b.strip().splitlines()
        for l in lines:
            l = l.strip()
            # Bỏ dòng header WEBVTT, timestamp, vị trí
            if not l or 'WEBVTT' in l or '-->' in l or l.isdigit():
                continue
            # Xóa các thẻ HTML <c> hoặc tương tự
            clean_l = re.sub(r'<[^>]+>', '', l).strip()
            if clean_l and clean_l not in seen:
                seen.add(clean_l)
                text_lines.append(clean_l)

    return " ".join(text_lines)

cases = [
    ("W0HlUFKGuYM.vi.vtt", "Làm Bánh Kể Chuyện Tâm Sự (787K views)", "BAKING_STORYTIME"),
    ("rsWEMsObGAU.vi.vtt", "Trang Trí Bánh Kể Chuyện Kỳ Bí (2.2M views)", "BAKING_MYSTERY"),
    ("NuIZnjtMXvY.vi.vtt", "Túi Mù Audio Drama (1.08M views)", "AUDIO_DRAMA"),
    ("F3rG-3AsrSg.vi.vtt", "Kỳ Án Có Thật 10 Phút (211K views)", "TRUE_CRIME")
]

results = []
study_dir = Path("data/tiktok_study")

print("🔍 ĐANG PHÂN TÍCH CHUYÊN SÂU NỘI DUNG THỰC TẾ TỪ TRANSCRIPT...")

for filename, title, genre in cases:
    path = study_dir / filename
    if not path.exists():
        continue

    full_text = parse_vtt(path)
    words = full_text.split()
    sentences = [s.strip() for s in re.split(r'[.!?…]+', full_text) if s.strip()]

    # Trích xuất 100 từ đầu tiên (Opening Hook)
    hook_3s = " ".join(words[:45])
    recap_or_mid = " ".join(words[len(words)//2:len(words)//2 + 50])
    ending = " ".join(words[-60:])

    print(f"\n========================================================")
    print(f"🎬 CASE STUDY: {title} ({genre})")
    print(f" - Tổng số từ: {len(words)} từ | Số câu: {len(sentences)} câu")
    print(f" - 🎯 HOOK MỞ ĐẦU THỰC TẾ (0-10s):")
    print(f"   \"{hook_3s}...\"")
    print(f" - ⚡ BƯỚC NGOẶT / ĐOẠN GIỮA THỰC TẾ:")
    print(f"   \"{recap_or_mid}...\"")
    print(f" - 🏁 KẾT THÚC & KÊU GỌI HÀNH ĐỘNG THỰC TẾ:")
    print(f"   \"{ending}...\"")

    results.append({
        "case_title": title,
        "genre": genre,
        "total_words": len(words),
        "total_sentences": len(sentences),
        "opening_hook_real": hook_3s,
        "mid_transition_real": recap_or_mid,
        "ending_callout_real": ending,
        "sample_excerpt": " ".join(words[:300])
    })

output_file = study_dir / "real_script_analysis.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n✅ Đã lưu phân tích chi tiết vào {output_file}")
