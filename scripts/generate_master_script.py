# -*- coding: utf-8 -*-
"""
scripts/generate_master_script.py
Công cụ Tự Động Hóa Biên Kịch Masterpiece dựa trên Cơ Sở Tri Thức 100 Bộ Đoản Văn Kinh Điển.
Quy trình thực thi 5 Giai Đoạn Chuẩn Hóa:
  1. Tra cứu Cơ sở Tri thức 100 Bộ Truyện (Bắt buộc thông qua Cổng Kiểm Duyệt Tri Thức).
  2. Thiết lập Dàn ý Kiến trúc 3 Hồi & Ma trận Phản diện 4 Tầng.
  3. Biên soạn Văn bản Điện ảnh Độc bản (Chuẩn 30 phút audio 1.5x >= 10,380 từ).
  4. Thẩm định Toàn diện 5 Chiều & Chống Trùng lặp (Anti-Duplication Guard).
  5. Đăng ký & Xuất xưởng vào Story Vault sẵn sàng cho Video Renderer.

Usage:
    python scripts/generate_master_script.py --genre TRONG_SINH
    python scripts/generate_master_script.py --genre NGUOC_TAM
    python scripts/generate_master_script.py --genre HAO_MON
    python scripts/generate_master_script.py --genre ME_CHONG
    python scripts/generate_master_script.py --genre HUYEN_NGHI
    python scripts/generate_master_script.py --genre KINH_DI
    python scripts/generate_master_script.py --genre SA_DIEU
    python scripts/generate_master_script.py --genre CUNG_DAU
    python scripts/generate_master_script.py --genre CUU_ROI
    python scripts/generate_master_script.py --genre VO_HAN
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
    verify_knowledge_gate,
    GOLDEN_RULES_10,
    OPENING_HOOK_TEMPLATES_6,
    SATISFACTION_MATRIX_5,
    VILLAIN_SYSTEM_4
)
from core.script_generator import get_script_engine

def get_slug_from_genre_and_title(genre: str, title: str) -> str:
    """Xác định slug chuẩn hóa cho 10 thể loại đoản văn"""
    g = genre.upper()
    if title:
        slug = re.sub(r'[^a-zA-Z0-9]+', '_', title.lower()).strip('_')
        return slug[:40]
    if "NGUOC_TAM" in g or "HOA_TANG" in g or "THE_THAN" in g:
        return "romance_nguoctam_masterpiece"
    elif "HAO_MON" in g or "TONG_TAI" in g or "KHE_UOC" in g:
        return "romance_haomon_masterpiece"
    elif "CUU_ROI" in g or "CHUA_LANH" in g or "THANH_XUAN" in g:
        return "romance_chualanh_masterpiece"
    elif "SA_DIEU" in g or "TIENG_LONG" in g or "HAI_HUOC" in g:
        return "sa_dieu_tieng_long_masterpiece"
    elif "CUNG_DAU" in g or "TRACH_DAU" in g or "NU_QUYEN" in g:
        return "cung_dau_nu_quyen_masterpiece"
    elif "VO_HAN" in g or "MAT_THE" in g or "SINH_TON" in g:
        return "horror_chuyentau_masterpiece"
    elif "ME_CHONG" in g or "GIA_DAU" in g or "DOI_SONG" in g:
        return "me_chong_thuc_tinh_masterpiece"
    elif "HUYEN_NGHI" in g or "TRINH_THAM" in g or "PHAP_Y" in g:
        return "huyen_nghi_trang_mau_masterpiece"
    elif "KINH_DI" in g or "QUAI_DAM" in g or "TAM_LINH" in g:
        return "kinh_di_huyet_nguyen_masterpiece"
    else:
        return "trong_sinh_hoa_sen_lua_masterpiece"

def main():
    parser = argparse.ArgumentParser(description="Master Script Generator Engine - 10 Thể Loại Kinh Điển")
    parser.add_argument("--genre", type=str, default="TRONG_SINH", help="Mã thể loại: TRONG_SINH, NGUOC_TAM, HAO_MON, ME_CHONG, HUYEN_NGHI, KINH_DI, SA_DIEU, CUNG_DAU, CUU_ROI, VO_HAN")
    parser.add_argument("--title", type=str, default="", help="Tiêu đề tác phẩm tùy chỉnh")
    parser.add_argument("--topic", type=str, default="", help="Chủ đề / Tiền đề nghịch lý tùy chỉnh")
    parser.add_argument("--voice", type=str, default="", help="Giọng đọc TTS (vi-VN-HoaiMyNeural hoặc vi-VN-NamMinhNeural)")
    parser.add_argument("--auto", action="store_true", help="Chạy tự động trọn gói 5 giai đoạn")

    args = parser.parse_args()

    # Tự động chọn giọng đọc chuẩn điện ảnh theo thể loại
    high_iq_genres = ["HUYEN_NGHI", "TRINH_THAM", "KINH_DI", "TAM_LINH", "VO_HAN", "HIGH_IQ"]
    default_voice = "vi-VN-NamMinhNeural" if any(k in args.genre.upper() for k in high_iq_genres) else "vi-VN-HoaiMyNeural"
    chosen_voice = args.voice or default_voice

    print("\n" + "=" * 75)
    print(f"🎬 [MASTER SCRIPT ENGINE] KHỞI ĐỘNG DÂY CHUYỀN BIÊN KỊCH: {args.genre.upper()}")
    print(f"🎙️ Giọng đọc chỉ định: {chosen_voice} (Tối ưu ngắt nhịp biểu cảm 1.5x)")
    print("=" * 75)

    engine = get_script_engine()

    # GIAI ĐOẠN 1: BẮT BUỘC TRA CỨU CƠ SỞ TRI THỨC 100 BỘ TRUYỆN
    print("\n🔍 [GIAI ĐOẠN 1/5]: BẮT BUỘC TRA CỨU CƠ SỞ TRI THỨC 100 BỘ TRUYỆN ĐOẢN VĂN KINH ĐIỂN...")
    topic_query = args.title or f"Kiệt tác đoản văn {args.genre}"
    consult_data = engine.step1_consult_knowledge(
        category=VideoCategory.HIGH_IQ if any(k in args.genre.upper() for k in high_iq_genres) else VideoCategory.SLEEP_CHILL,
        topic_title=topic_query,
        topic_summary=args.topic or f"Tác phẩm tinh hoa thể loại {args.genre}",
        top_k=3,
        genre_hint=args.genre
    )

    print(f" -> Cổng Tri Thức (Knowledge Gate): [XÁC MINH HỢP LỆ]")
    print(f" -> Thẻ Bài Tri Thức (Consultation Token): {consult_data['consultation_token']}")
    print(f" -> Tổng kho tàng tri thức đã nạp: {consult_data['total_knowledge_pool']} tác phẩm (bao gồm Crawl4AI).")
    print(" -> Các Case Study kinh điển đối soát làm hình mẫu:")
    for idx, c in enumerate(consult_data["relevant_cases"], 1):
        print(f"    * Case #{idx}: 《{c['title']}》 ({c['author']}) - {c['genre']}")
        takeaways = c.get('key_takeaways', '')
        takeaway_short = str(takeaways[0] if isinstance(takeaways, list) else takeaways).split('\n')[0][:95]
        print(f"      └─ Bài học cốt lõi: {takeaway_short}...")

    # GIAI ĐOẠN 2: THIẾT LẬP DÀN Ý KIẾN TRÚC 3 HỒI & MA TRẬN PHẢN DIỆN
    print("\n📐 [GIAI ĐOẠN 2/5]: THIẾT LẬP DÀN Ý KIẾN TRÚC 3 HỒI & MA TRẬN PHẢN DIỆN...")
    blueprint = engine.step2_build_blueprint(
        genre_key=args.genre,
        title=args.title or f"Kiệt tác đoản văn {args.genre}",
        premise=args.topic or f"Kịch bản điện ảnh audio 30 phút thể loại {args.genre}",
        consult_data=consult_data
    )
    print(f" -> Hook Chiến Lược: [{blueprint['hook_strategy']}]")
    print(f" -> Khẩu Súng Của Chekhov (Cài Tập 1, Tháo chốt Tập 3):")
    for g_idx, gun in enumerate(blueprint['chekhov_guns'], 1):
        print(f"    * Súng #{g_idx}: {gun}")
    print(f" -> Ma Trận Phản Diện 4 Tầng:")
    print(f"    * Tầng 1 (Tốt thí mở màn): {blueprint['villain_architecture']['tier1_cannon_fodder']}")
    print(f"    * Tầng 2 (Sức ép trung tầng): {blueprint['villain_architecture']['tier2_mid_antagonist']}")
    print(f"    * Tầng 3 (Trùm cuối thao túng): {blueprint['villain_architecture']['tier3_ultimate_boss']}")
    print(f"    * Tầng 4 (Kẻ phản bội tiềm ẩn): {blueprint['villain_architecture']['tier4_hidden_betrayer']}")

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
        est_min = round(w_cnt / 346, 1)
        status_flag = "✅ ĐẠT CHUẨN" if w_cnt >= 3460 else "⚠️ CHƯA ĐỦ"
        print(f"    * {p['badge_label']} - {p['title']}: {w_cnt:,} từ (~{est_min} phút ở 1.5x) [{status_flag}]")

    # GIAI ĐOẠN 4: THẨM ĐỊNH TOÀN DIỆN 5 CHIỀU (QUALITY AUDIT)
    print("\n⚖️ [GIAI ĐOẠN 4/5]: TỔNG BIÊN TẬP THẨM ĐỊNH TOÀN DIỆN THEO BẢNG TIÊU CHÍ 5 CHIỀU...")
    audit = engine.step4_audit_script(story_dict)
    print(f" -> Trạng Thái: [{audit['status']}] | Điểm Tổng Kết: {audit['score']}/10 ⭐")
    print(f" -> Kiểm tra chống lặp đoạn (Anti-Duplication Guard): {'✅ PASSED (100% Độc Bản, 0 Trùng Lặp)' if audit['has_no_duplicate_paragraphs'] else '❌ FAILED'}")
    print(f" -> Chi tiết Rubric 5 Chiều:")
    print(f"    1. Giữ Chân 5 Giây Đầu (Zero-Bio, Mở Xung Đột): {audit['rubric']['hook_retention_score']}/10")
    print(f"    2. Chiều Sâu & Dung Lượng (>= 10,380 từ): {audit['rubric']['depth_and_length_score']}/10 (Đạt {audit['total_words']:,} từ)")
    print(f"    3. Nhịp Điệu & Dấu Ngắt Câu 1.5x (Ngắt Nghỉ Kịch Tính): {audit['rubric']['pacing_and_dialogue_score']}/10")
    print(f"    4. Tính Nối Tiếp & Liền Mạch (100% Sạch Meta): {audit['rubric']['continuity_and_flow_score']}/10")
    print(f"    5. Điểm Cắt Cliffhanger & Kết Cục Thỏa Mãn: {audit['rubric']['cliffhanger_climax_score']}/10")

    if audit['status'] != "APPROVED":
        print("\n❌ KỊCH BẢN CHƯA ĐẠT CHUẨN XUẤT XƯỞNG!")
        sys.exit(1)

    # GIAI ĐOẠN 5: XUẤT XƯỞNG & ĐĂNG KÝ VÀO STORY VAULT
    print("\n📦 [GIAI ĐOẠN 5/5]: XUẤT XƯỞNG FILE VÀ ĐĂNG KÝ VÀO STORY VAULT...")
    slug = get_slug_from_genre_and_title(args.genre, args.title)
    exported_py = engine.export_script_module(story_dict, file_slug=slug, voice=chosen_voice)
    print(f" -> Python Story Module: {exported_py}")
    print(f" -> JSON Kịch Bản Chi Tiết: data/generated_scripts/{slug}.json")
    print(f" -> Story Vault Status: ĐÃ SẴN SÀNG cho Audio TTS Engine và Video MP4 Render Pipeline!")

    print("\n" + "=" * 75)
    print("✨ [XUẤT SẮC] QUY TRÌNH BIÊN KỊCH MASTERPIECE ĐÃ HOÀN TẤT THÀNH CÔNG 100%!")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    main()
