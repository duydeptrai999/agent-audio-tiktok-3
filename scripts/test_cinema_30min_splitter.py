# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.cinema_30min_splitter import Cinema30MinSplitter
from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story

story = get_man_tra_thu_masterpiece_story()

# Dùng trích đoạn 150 từ của mỗi tập để test nhanh pipeline ghép nối
p1_sample = " ".join(story["parts"]["part1"].split()[:150])
p2_sample = " ".join(story["parts"]["part2"].split()[:150])
p3_sample = " ".join(story["parts"]["part3"].split()[:150])

sample_story = {
    "title": "Màn Trả Thù Đã Nhất Đời Tôi - Bản Mẫu 3 Phần",
    "parts": {
        "part1": p1_sample,
        "part2": p2_sample,
        "part3": p3_sample
    }
}

splitter = Cinema30MinSplitter()
result = splitter.build_full_30min_package(sample_story)

print("\n" + "=" * 80)
print("KẾT QUẢ KIỂM THỬ ĐỘNG CƠ 30 PHÚT & TÁCH 3 PHẦN:")
print("=" * 80)
print(f"Tiêu đề: {result['title']}")
print(f"Tổng số từ: {result['total_words']}")
print(f"Master Audio (Bản Trọn Bộ): {result['master_audio_30min']}")
for p in result["parts"]:
    print(f"  - Tập {p['part_number']} ({p['words_count']} từ): {p['audio_path']}")
print("=" * 80)
print("PIPELINE TEST THÀNH CÔNG RỰC RỠ!")
