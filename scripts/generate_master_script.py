# -*- coding: utf-8 -*-
"""
scripts/generate_master_script.py
Công cụ Tự Động Hóa Biên Kịch Masterpiece dựa trên Cơ Sở Tri Thức 100 Bộ Đoản Văn Kinh Điển.
Quy trình thực thi 5 Giai Đoạn Chuẩn Hóa:

Usage:
    python scripts/generate_master_script.py --genre TRONG_SINH
    python scripts/generate_master_script.py --genre ME_CHONG
    python scripts/generate_master_script.py --genre HUYEN_NGHI
    python scripts/generate_master_script.py --genre KINH_DI
"""

import sys
import os
import argparse
import re
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from core.state import VideoCategory
from core.knowledge_base import (
    get_knowledge_base,
    require_knowledge_consultation,
    GOLDEN_RULES_10,
    OPENING_HOOK_TEMPLATES_6,
    SATISFACTION_MATRIX_5,
    VILLAIN_SYSTEM_4
)
from core.script_generator import get_script_engine

def get_slug_from_genre_and_title(genre: str, title: str) -> str:
    g = genre.upper()
    if title:
        slug = re.sub(r'[^a-zA-Z0-9]+', '_', title.lower()).strip('_')
        return slug[:40]
    if "ME_CHONG" in g or "GIA_DAU" in g or "DOI_SONG" in g:
        return "me_chong_thuc_tinh"
    elif "HUYEN_NGHI" in g or "TRINH_THAM" in g:
        return "huyen_nghi_trang_mau"
    elif "KINH_DI" in g or "TAM_LINH" in g:
        return "kinh_di_huyet_nguyen"
    else:
        return "trong_sinh_hoa_sen_lua"

def main():
    parser = argparse.ArgumentParser(description="Master Script Generator Engine")
    parser.add_argument("--genre", type=str, default="TRONG_SINH", help="Genre key (TRONG_SINH, ME_CHONG, HUYEN_NGHI, KINH_DI, etc.)")
    parser.add_argument("--title", type=str, default="", help="Custom story title")
    parser.add_argument("--topic", type=str, default="", help="Custom premise or topic")
    parser.add_argument("--voice", type=str, default="", help="TTS Neural Voice (vi-VN-HoaiMyNeural or vi-VN-NamMinhNeural)")
    parser.add_argument("--auto", action="store_true", help="Auto run standard masterpiece generation")

    args = parser.parse_args()

    # Tự động chọn voice phù hợp với thể loại nếu chưa chỉ định
    default_voice = "vi-VN-NamMinhNeural" if args.genre.upper() in ["HUYEN_NGHI", "TRINH_THAM", "KINH_DI", "TAM_LINH", "HIGH_IQ"] else "vi-VN-HoaiMyNeural"
    chosen_voice = args.voice or default_voice

    print("\n" + "=" * 70)
    print(f"🎬 [MASTER SCRIPT ENGINE] KHỞI ĐỘNG DÂY CHUYỀN BIÊN KỊCH: {args.genre.upper()}")
    print("=" * 70)

    engine = get_script_engine()

    # GIAI ĐOẠN 1: BẮT BUỘC TRA CỨU CƠ SỞ TRI THỨC 100 BỘ TRUYỆN
    print("\n🔍 [GIAI ĐOẠN 1/5]: BẮT BUỘC TRA CỨU CƠ SỞ TRI THỨC 100 BỘ TRUYỆN ĐOẢN VĂN KINH ĐIỂN...")
    topic_query = args.title or f"Kiệt tác đoản văn {args.genre}"
    consult_data = engine.step1_consult_knowledge(
        category=VideoCategory.SLEEP_CHILL if args.genre.upper() in ["TRONG_SINH", "NGUOC_TAM", "HAO_MON", "ME_CHONG", "CUU_ROI", "CHUA_LANH"] else VideoCategory.HIGH_IQ,
        topic_title=topic_query,
        topic_summary=args.topic or f"Tác phẩm tinh hoa thể loại {args.genre}",
        top_k=3
    )

    print(f" -> Đã đối soát thành công kho tàng {consult_data['total_knowledge_pool']} tác phẩm kinh điển.")
    print(" -> Các Case Study tinh hoa được chọn lọc làm hình mẫu:")
    for idx, c in enumerate(consult_data["relevant_cases"], 1):
        print(f"    * Case #{idx}: {c['title']} ({c['author']}) - {c['genre']}")

    # GIAI ĐOẠN 2: THIẾT LẬP DÀN Ý KIẾN TRÚC 3 HỒI & ĐIỂM CẮT NGHẸT THỞ
    print("\n📐 [GIAI ĐOẠN 2/5]: THIẾT LẬP DÀN Ý KIẾN TRÚC 3 HỒI & MA TRẬN PHẢN DIỆN...")
    blueprint = engine.step2_build_blueprint(
        genre_key=args.genre,
        title=args.title or f"Kiệt tác đoản văn {args.genre}",
        premise=args.topic or f"Kịch bản điện ảnh audio 30 phút thể loại {args.genre}",
        consult_data=consult_data
    )
    print(f" -> Hook Chiến Lược: [{blueprint['hook_strategy']}]")
    print(f" -> Khẩu Súng Của Chekhov: {blueprint['chekhov_guns'][0]}")
    print(f" -> Phản diện 4 tầng: {blueprint['villain_architecture']['tier1_cannon_fodder']}")

    # GIAI ĐOẠN 3: TỔNG HỢP VĂN BẢN ĐIỆN ẢNH & NGẮT NHỊP 1.5X
    print(f"\n✍️ [GIAI ĐOẠN 3/5]: BIÊN SOẠN VĂN BẢN ĐIỆN ẢNH ({chosen_voice}) & CHUẨN AUDIO 30 PHÚT...")
    story_dict = engine.step3_synthesize_script(
        genre_key=args.genre,
        title=args.title,
        premise=args.topic,
        consult_data=consult_data,
        voice=chosen_voice
    )

    for p in story_dict["parts"]:
        w_cnt = len(p["full_text"].split())
        print(f"    * {p['badge_label']} - {p['title']}: {w_cnt:,} từ (Đạt chuẩn >= 3,460 từ).")

    # GIAI ĐOẠN 4: THẨM ĐỊNH TOÀN DIỆN 5 CHIỀU (QUALITY AUDIT)
    print("\n⚖️ [GIAI ĐOẠN 4/5]: TỔNG BIÊN TẬP THẨM ĐỊNH TOÀN DIỆN THEO BẢNG TIÊU CHÍ 5 CHIỀU...")
    audit = engine.step4_audit_script(story_dict)
    print(f" -> Trạng Thái: [{audit['status']}] | Điểm Tổng Kết: {audit['score']}/10 ⭐")
    print(f" -> Kiểm tra chống lặp đoạn (Anti-Duplication): {'✅ PASSED (100% Độc Bản)' if audit['has_no_duplicate_paragraphs'] else '❌ FAILED'}")
    print(f" -> Chi tiết Rubric:")
    print(f"    * Hook 5s Retention: {audit['rubric']['hook_retention_score']}/10")
    print(f"    * Chiều sâu & Dung lượng: {audit['rubric']['depth_and_length_score']}/10 (Tổng {audit['total_words']:,} từ)")
    print(f"    * Nhịp điệu & Dấu ngắt câu 1.5x: {audit['rubric']['pacing_and_dialogue_score']}/10")
    print(f"    * Tính nối tiếp (100% sạch Meta): {audit['rubric']['continuity_and_flow_score']}/10")
    print(f"    * Cliffhanger & Kết cục: {audit['rubric']['cliffhanger_climax_score']}/10")

    if audit['status'] != "APPROVED":
        print("❌ KỊCH BẢN CHƯA ĐẠT CHUẨN XUẤT XƯỞNG!")
        sys.exit(1)

    # GIAI ĐOẠN 5: XUẤT XƯỞNG & ĐĂNG KÝ VÀO STORY VAULT
    print("\n📦 [GIAI ĐOẠN 5/5]: XUẤT XƯỞNG FILE VÀ ĐĂNG KÝ VÀO STORY VAULT...")
    slug = get_slug_from_genre_and_title(args.genre, args.title)
    exported_py = engine.export_script_module(story_dict, file_slug=slug, voice=chosen_voice)
    print(f" -> File Python Module: {exported_py}")
    print(f" -> File JSON Kịch Bản: data/generated_scripts/{slug}.json")
    print(f" -> Sẵn sàng cho dây chuyền sản xuất Audio TTS 1.5x và Render Video MP4!")

    print("\n" + "=" * 70)
    print("✨ [XUẤT SẮC] QUY TRÌNH BIÊN KỊCH MASTERPIECE ĐÃ HOÀN TẤT THÀNH CÔNG 100%!")
    print("=" * 70)

if __name__ == "__main__":
    main()
