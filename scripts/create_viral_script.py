# -*- coding: utf-8 -*-
"""
scripts/create_viral_script.py

Công Cụ Biên Kịch Triệu View Trực Tiếp (Flagship Viral Script Generator).
Quy trình khép kín 5 giai đoạn tích hợp Cơ Sở Tri Thức 100 Kiệt Tác Đoản Văn Trung Quốc:
1. Tra cứu Tri Thức & Đối chuẩn Masterpiece Case Study (Knowledge Consultation Gate).
2. Lập Dàn Ý Kiến Trúc 3 Hồi & Điểm Cắt Nghẹt Thở (Master Blueprint & Chekhov's Guns).
3. Biên Soạn Kịch Bản Điện Ảnh Chuẩn Dung Lượng & Âm Học Edge-TTS (Cinema Synthesis).
4. Thẩm Định Tự Động 6 Chiều Khắt Khe (Mandatory Quality Audit & Anti-Homogenization).
5. Xuất Bản & Đăng Ký Vào Story Vault (Automated Module & Metadata Export).

Cách sử dụng:
    python scripts/create_viral_script.py --genre TRONG_SINH --title "Tên kịch bản" --premise "Tóm tắt ý tưởng"
    python scripts/create_viral_script.py --genre ME_CHONG --voice vi-VN-HoaiMyNeural
    python scripts/create_viral_script.py --genre HUYEN_NGHI --voice vi-VN-NamMinhNeural
"""

import os
import sys
import argparse
import json
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.script_generator import MasterScriptEngine
from core.knowledge_base import get_knowledge_base, format_brief_for_prompt
from core.stories.script_quality_gate import require_preflight_experience

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("CreateViralScript")


def main():
    parser = argparse.ArgumentParser(description="Tạo kịch bản audio TikTok triệu view từ Cơ sở tri thức 100 tác phẩm kinh điển")
    parser.add_argument(
        "--genre",
        type=str,
        default="TRONG_SINH",
        choices=[
            "TRONG_SINH", "NGUOC_TAM", "HUYEN_NGHI", "ME_CHONG",
            "HAO_MON", "KINH_DI", "SA_DIEU", "CUNG_DAU", "CUU_ROI", "VO_HAN"
        ],
        help="Thể loại truyện ngắn (10 thể loại kinh điển)"
    )
    parser.add_argument("--title", type=str, default="", help="Tiêu đề tùy chọn")
    parser.add_argument("--premise", type=str, default="", help="Ý tưởng hoặc tiền đề kịch tính")
    parser.add_argument("--voice", type=str, default="vi-VN-HoaiMyNeural", help="Giọng đọc Edge-TTS (Hoài My / Nam Minh)")
    parser.add_argument("--export-json", action="store_true", help="Xuất thêm file JSON chi tiết")
    args = parser.parse_args()

    print("\n" + "=" * 90)
    print("🚀 KHỞI ĐỘNG XƯỞNG BIÊN KỊCH TỰ ĐỘNG TRIỆU VIEW (VIRAL SCRIPT CREATOR)")
    print(f"   Thể loại: {args.genre} | Giọng đọc: {args.voice}")
    if args.title:
        print(f"   Tiêu đề tùy biến: {args.title}")
    print("=" * 90 + "\n")

    # 1. Kích hoạt Cổng Kinh Nghiệm Bắt Buộc
    require_preflight_experience()
    kb = get_knowledge_base()

    # 2. Khởi tạo Động cơ biên kịch
    engine = MasterScriptEngine()

    # 3. Thực thi chu trình 5 giai đoạn hoàn chỉnh
    print("\n[GIAI ĐOẠN 1-5] Đang phân tích tri thức đối chuẩn, lập dàn ý và tổng hợp kịch bản...")
    result = engine.generate_full_masterpiece(
        genre_key=args.genre,
        title=args.title,
        premise=args.premise,
        voice=args.voice
    )

    consult_data = result["consult_data"]
    story = result["story"]
    audit = result["audit"]
    exported_py = result["exported_py"]

    # 4. Hiển thị báo cáo kết quả chi tiết
    print("\n" + "=" * 90)
    print("✨ SẢN XUẤT KỊCH BẢN MASTERPIECE HOÀN TẤT THÀNH CÔNG!")
    print("=" * 90)
    print(f"📖 Tiêu đề: {story.get('title')}")
    print(f"🎭 Thể loại: {story.get('genre')} | Giọng đọc: {story.get('voice')}")
    print(f"🔑 Thẻ bài Tri Thức (Token): {consult_data.get('consultation_token')}")
    
    cases = consult_data.get("relevant_cases", [])
    if cases:
        print(f"🏆 Tác phẩm đối chuẩn tham chiếu: {cases[0].get('title')} ({cases[0].get('id')})")
        print(f"   - Đạo cụ vật lý mỏ neo: {', '.join(cases[0].get('tangible_props', []))}")
        print(f"   - Công thức điểm sảng: {cases[0].get('shuangdian_formula', 'N/A')}")

    print("\n📊 THỐNG KÊ DUNG LƯỢNG & ĐIỂM SỐ KIỂM ĐỊNH:")
    print(f"   - Tổng số từ: {audit.get('total_words', 0):,} từ (Đạt chuẩn 30 phút audio tại nhịp 1.5x)")
    for idx, count in enumerate(audit.get('part_word_counts', []), 1):
        print(f"     * Tập {idx}: {count:,} từ")
    print(f"   - Điểm kiểm định chất lượng: {audit.get('score', 0):.2f}/10.0 ({audit.get('status')})")
    print(f"   - Chống trùng lặp đoạn văn: {'ĐẠT (100% Độc bản)' if audit.get('has_no_duplicate_paragraphs') else 'CẢNH BÁO'}")

    print(f"\n💾 Tệp mã nguồn kịch bản đã xuất: {exported_py}")

    # Xuất JSON nếu được yêu cầu
    if args.export_json:
        json_path = Path(exported_py).with_suffix(".json")
        json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"📄 Tệp JSON chi tiết đã lưu: {json_path}")

    print("=" * 90 + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
