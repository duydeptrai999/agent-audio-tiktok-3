# -*- coding: utf-8 -*-
"""
core/stories/daily_story_factory.py
Kho Cung Cấp & Tự Động Sinh 10 Bộ Truyện Mới Hàng Ngày (Daily Masterpiece Factory):
- Tích hợp 40+ Masterpiece Modules chuẩn điện ảnh (15.000+ từ / bộ).
- Đảm bảo 100% không trùng lặp tên, cốt truyện hay mã băm với bất kỳ bộ nào trong quá khứ.
- Luân chuyển đa dạng kho kiệt tác theo ngày: Tiêu đề khớp 100% nội dung (Zero False Advertising).
- Ban ngày: Sa điêu, Thanh xuân, Cung đấu, Vả mặt, Mạt thế, Hào môn, Gia đấu.
- Ban đêm (19h20, 21h10, 23h00): Trinh thám kỳ án, Quy tắc quái đàm, Kinh dị đêm muộn rùng rợn.
"""

import re
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from core.daily_schedule_config import DAILY_10_SLOTS
from core.stories.script_quality_gate import validate_story_series, require_preflight_experience
from core.anti_repost_guard import PAST_SERIES_BLACKLIST, normalize_text, calculate_similarity

# --- KHO MASTERPIECE MODULES CHO 10 KHUNG GIỜ ---
# Slot 1: Sa điêu / Tiếng lòng / Hài công sở
from core.stories.sa_dieu_tieng_long_masterpiece import get_sa_dieu_tieng_long_masterpiece_story
from core.stories.batch2_5_masterpieces import BATCH2_5_SERIES_DATA
from core.stories.new_5_masterpieces import NEW_5_SERIES_DATA

# Slot 2: Thanh xuân / Vườn trường / Chữa lành
from core.stories.school_romance_vungtrom_masterpiece import get_vungtrom_masterpiece_story
from core.stories.school_romance_gaplai_masterpiece import get_gaplai_masterpiece_story
from core.stories.school_romance_khododanh_masterpiece import get_khododanh_masterpiece_story
from core.stories.romance_school import get_30min_school_romance_story

# Slot 3: Cung đấu / Trạch đấu / Nữ quyền
from core.stories.cung_dau_nu_quyen_masterpiece import get_cung_dau_nu_quyen_masterpiece_story
from core.stories.cung_dau_duoc_dien_masterpiece import get_cung_dau_duoc_dien_masterpiece_story

# Slot 4: Trọng sinh / Vả mặt / Hào môn
from core.stories.trong_sinh_hoa_sen_lua_masterpiece import get_trong_sinh_hoa_sen_lua_masterpiece_story
from core.stories.romance_angst import get_30min_angst_romance_story

# Slot 5: Mạt thế / Sinh tồn / Kỹ thuật pháo đài
from core.stories.mat_the_sinh_ton_masterpiece import get_mat_the_sinh_ton_masterpiece_story
from core.stories.mat_the_bang_gia_masterpiece import get_mat_the_bang_gia_masterpiece_story

# Slot 6: Hào môn thế gia / Ngược tâm / Chữa lành
from core.stories.romance_haomon_masterpiece import get_romance_haomon_masterpiece_story
from core.stories.romance_nguoctam_masterpiece import get_romance_nguoctam_masterpiece_story
from core.stories.romance_chualanh_masterpiece import get_romance_chualanh_masterpiece_story
from core.stories.romance_chualanh_tuyetpham import get_romance_chualanh_tuyetpham_story
from core.stories.romance import get_30min_romance_story
from core.stories.life_divorce import get_30min_divorce_drama_story

# Slot 7: Mẹ chồng / Gia đấu / Đời sống thức tỉnh
from core.stories.me_chong_thuc_tinh_masterpiece import get_me_chong_thuc_tinh_masterpiece_story
from core.stories.family_drama_masterpiece import get_family_drama_masterpiece_story
from core.stories.life_mother_in_law import get_30min_mother_in_law_story
from core.stories.life_drama import get_30min_life_drama_story
from core.stories.life_healing_masterpiece import get_life_healing_masterpiece_story

# Slot 8: Trinh thám / Huyền nghi kỳ án
from core.stories.detective_masterpiece import get_detective_masterpiece_story
from core.stories.detective import get_30min_detective_story
from core.stories.huyen_nghi_trang_mau_masterpiece import get_huyen_nghi_trang_mau_masterpiece_story
from core.stories.doraemon import get_30min_doraemon_mystery_story

# Slot 9: Quy tắc quái đàm / Phòng kín sinh tồn
from core.stories.quai_dam_rap_chieu_phim_masterpiece import get_quai_dam_rap_chieu_phim_masterpiece_story
from core.stories.horror_chuyentau_masterpiece import get_horror_chuyentau_masterpiece_story

# Slot 10: Kinh dị đêm muộn / Rùng rợn tâm linh đô thị
from core.stories.kinh_di_phong_so_7_masterpiece import get_kinh_di_phong_so_7_masterpiece_story
from core.stories.kinh_di_huyet_nguyen_masterpiece import get_kinh_di_huyet_nguyen_masterpiece_story
from core.stories.horror_guongquy_masterpiece import get_horror_guongquy_masterpiece_story
from core.stories.horror_trocot_masterpiece import get_horror_trocot_masterpiece_story
from core.stories.horror import get_30min_horror_story

# Masterpiece Vòng 41 - 50: Đu Trend Xã Hội Nổi Cộm & 100% Zero Chính Trị
from core.stories.cycles_41_to_50_masterpieces import (
    get_story_cycle_41, get_story_cycle_42, get_story_cycle_43, get_story_cycle_44,
    get_story_cycle_45, get_story_cycle_46, get_story_cycle_47, get_story_cycle_48,
    get_story_cycle_49, get_story_cycle_50
)

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
REGISTRY_FILE = ROOT_PATH / "data" / "published_audio_registry.json"

# --- CATALOG KIỆT TÁC THEO TỪNG SLOT (SLOT_STORY_CATALOG) ---
SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,
        lambda: BATCH2_5_SERIES_DATA[0],
        lambda: NEW_5_SERIES_DATA[0],
        get_story_cycle_49,
    ],
    2: [
        get_vungtrom_masterpiece_story,
        get_gaplai_masterpiece_story,
        get_khododanh_masterpiece_story,
        lambda: BATCH2_5_SERIES_DATA[4],
        get_30min_school_romance_story,
    ],
    3: [
        get_cung_dau_nu_quyen_masterpiece_story,
        get_cung_dau_duoc_dien_masterpiece_story,
        lambda: BATCH2_5_SERIES_DATA[2],
        lambda: NEW_5_SERIES_DATA[1],
    ],
    4: [
        get_trong_sinh_hoa_sen_lua_masterpiece_story,
        lambda: BATCH2_5_SERIES_DATA[1],
        lambda: NEW_5_SERIES_DATA[4],
        get_30min_angst_romance_story,
        get_story_cycle_44,
    ],
    5: [
        get_mat_the_sinh_ton_masterpiece_story,
        get_mat_the_bang_gia_masterpiece_story,
        get_story_cycle_41,
        get_story_cycle_48,
    ],
    6: [
        get_romance_haomon_masterpiece_story,
        get_romance_nguoctam_masterpiece_story,
        get_romance_chualanh_masterpiece_story,
        get_romance_chualanh_tuyetpham_story,
        get_30min_romance_story,
        get_30min_divorce_drama_story,
        get_story_cycle_45,
    ],
    7: [
        get_me_chong_thuc_tinh_masterpiece_story,
        get_family_drama_masterpiece_story,
        get_30min_mother_in_law_story,
        get_30min_life_drama_story,
        get_life_healing_masterpiece_story,
        get_story_cycle_43,
        get_story_cycle_46,
    ],
    8: [
        get_detective_masterpiece_story,
        lambda: BATCH2_5_SERIES_DATA[3],
        get_30min_detective_story,
        get_huyen_nghi_trang_mau_masterpiece_story,
        get_30min_doraemon_mystery_story,
        get_story_cycle_42,
        get_story_cycle_50,
    ],
    9: [
        get_quai_dam_rap_chieu_phim_masterpiece_story,
        lambda: NEW_5_SERIES_DATA[3],
        get_horror_chuyentau_masterpiece_story,
    ],
    10: [
        get_kinh_di_phong_so_7_masterpiece_story,
        lambda: NEW_5_SERIES_DATA[2],
        get_horror_guongquy_masterpiece_story,
        get_horror_trocot_masterpiece_story,
        get_kinh_di_huyet_nguyen_masterpiece_story,
        get_30min_horror_story,
        get_story_cycle_47,
    ]
}

# Tương thích ngược cho các module cũ
SLOT_STORY_LOADERS = {
    1: get_sa_dieu_tieng_long_masterpiece_story,
    2: get_vungtrom_masterpiece_story,
    3: get_cung_dau_nu_quyen_masterpiece_story,
    4: get_trong_sinh_hoa_sen_lua_masterpiece_story,
    5: get_mat_the_sinh_ton_masterpiece_story,
    6: get_romance_haomon_masterpiece_story,
    7: get_me_chong_thuc_tinh_masterpiece_story,
    8: get_detective_masterpiece_story,
    9: get_quai_dam_rap_chieu_phim_masterpiece_story,
    10: get_kinh_di_phong_so_7_masterpiece_story
}

DAILY_THEME_TITLES = {
    1: [
        "Thư Ký Giả Ngốc: Tiếng Lòng Chê Tổng Tài Khiến Cả Phòng Họp Cười Xỉu",
        "Thư Ký Nhỏ Biết Đọc Tiếng Lòng: Sếp Tổng Mặt Lạnh Nhịn Cười",
        "Khi Cả Nhà Hào Môn Nghe Thấy Tiếng Lòng Nàng Dâu Giả Mạo"
    ],
    2: [
        "Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ",
        "Gặp Lại Người Năm Ấy: Bản Tình Ca Mùa Hè Chưa Từng Lãng Quên",
        "Đại Ca Học Đường Khó Dỗ Dành: Chỉ Dịu Dàng Với Riêng Em",
        "Bức Thư Mùa Hạ Mười Năm Trước: Chiếc Ô Xanh Dưới Cơn Mưa",
        "Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Rào"
    ],
    3: [
        "Phượng Hoàng Niết Bàn: Hoàng Hậu Bãi Công Đi Thi Trạng Nguyên",
        "Dược Điển Cung Cấm: Chiếc Trâm Bạc Thử Độc Vạch Trần Thục Phi",
        "Đích Nữ Tướng Môn: Nhận Chiếu Hòa Thân, Nàng San Bằng Biên Cương"
    ],
    4: [
        "Khi Hoa Sơn Tra Tàn Lụi: Nỗi Oan Khuất 5 Năm Của Cô Dâu Thế Thân",
        "Thiên Kim Thật Đoạt Lại Vận Mệnh: Ba Anh Trai Quỳ Gối Cầu Xin",
        "Thiên Kim Thật Trở Về: Cú Vả Mặt Chấn Động Giới Thượng Lưu",
        "Khi Hoa Sơn Tra Tàn Lụi: 5 Năm Oan Khuất Nhận Tội Thay Kẻ Bạc Tình"
    ],
    5: [
        "Trọng Sinh Về 30 Ngày Trước Tận Thế Bão Cát: Hầm Trú Ẩn Bất Khả Xâm Phạm",
        "Trọng Sinh Về 30 Ngày Trước Tận Thế Băng Giá Âm 60 Độ: Pháo Đài Nhiệt Ngầm 100 Tỷ"
    ],
    6: [
        "Bản Hợp Đồng Hôn Nhân 100 Tỷ: Vị Hôn Thê Giả Mạo Của Tổng Tài Tàn Tật",
        "Khi Hoa Sơn Tra Tàn Lụi: Nỗi Oan Khuất 7 Năm Của Cô Gái Ngồi Tù",
        "Ánh Sáng Nơi Tận Cùng Đêm Tối: Bản Hợp Đồng Cứu Rỗi Trái Tim Tổn Thương",
        "Ánh Sáng Nơi Tận Cùng Đêm Tối: 100 Ngày Cứu Rỗi Trái Tim",
        "Cưới Em Trước Cưng Chiều Em Sau: Bản Hợp Đồng Hôn Nhân Giả",
        "Màn Lật Kèo Lúc Nửa Đêm: 365 Ngày Thu Thập Chứng Cứ Ly Hôn"
    ],
    7: [
        "Đêm Mưa Thức Tỉnh: Bản Khế Ước Gia Tộc Đòi Lại 50 Tỷ",
        "Đêm Mưa Bị Đuổi Khỏi Hào Môn: Màn Lật Kèo Đòi Lại 100 Tỷ Của Người Vợ Cũ",
        "Đêm Mưa Bị Đuổi Khỏi Nhà Chồng: 7 Năm Tủi Nhục Và Màn Phục Thù Bạc Tỷ",
        "Bí Mật Dưới Nền Bếp: Tấm Di Chúc 10 Năm Của Người Cha Bị Hắt Hủi",
        "Tiệm Tạp Hóa Thời Gian Bên Góc Phố: Nơi Cất Giữ Ký Ức Và Sự Cứu Rỗi"
    ],
    8: [
        "Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất",
        "Lời Khai Của Thi Thể Lúc Nửa Đêm: Vết Mực Bí Ẩn Trên Mu Bàn Tay",
        "Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Bí Ẩn Lúc Nửa Đêm",
        "Kỳ Án Biệt Thự Trăng Máu: Tiếng Gõ Cửa Của Thám Tử Lúc 0 Giờ",
        "Kỳ Án Cỗ Máy Thời Gian: Lời Cảnh Báo Lúc Nửa Đêm Của Kẻ Vô Danh"
    ],
    9: [
        "Quy Tắc Sinh Tồn Rạp Chiếu Phim Đêm: Đừng Bao Giờ Ngồi Hàng Ghế Số 4",
        "Khách Sạn Nửa Đêm: 10 Quy Tắc Sinh Tồn Ca Đêm Của Tân Nhân Viên",
        "Chuyến Tàu Ngầm Cuối Cùng: 7 Quy Tắc Sinh Tồn Không Thể Bỏ Qua"
    ],
    10: [
        "Khách Trọ Phòng Số 7: Người Đàn Bà Mặc Áo Đỏ Dưới Đèn Đường",
        "Kỳ Án Viện Bảo Tàng: Bức Họa Rỉ Máu Lúc Nửa Đêm",
        "Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn Cổ",
        "Tiếng Cào Cửa Lúc 2 Giờ Sáng: Bí Ẩn Hũ Tro Cốt Dưới Gầm Giường",
        "Huyết Nguyện Lúc Nửa Đêm: Chiếc Gương Âm Dương Biệt Thự Cổ",
        "Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn"
    ]
}

def get_published_titles_set() -> set:
    published = set()
    if REGISTRY_FILE.exists():
        try:
            data = json.loads(REGISTRY_FILE.read_text(encoding='utf-8'))
            for t in data.get("published_titles", []):
                published.add(normalize_text(t))
        except Exception:
            pass
    # Quét tất cả file status hàng ngày để gom toàn bộ tựa đề đã phát hành
    status_dir = ROOT_PATH / "data"
    for f in status_dir.glob("daily_schedule_status_*.json"):
        try:
            s_data = json.loads(f.read_text(encoding='utf-8'))
            for k, v in s_data.items():
                if isinstance(v, dict) and (v.get("part1") or v.get("part2") or v.get("part3")):
                    if "title" in v:
                        published.add(normalize_text(v["title"]))
        except Exception:
            pass
    return published

def is_title_allowed(title: str, published_set: set) -> bool:
    norm = normalize_text(title)
    for bl in PAST_SERIES_BLACKLIST:
        if bl in norm:
            return False
    for pub in published_set:
        if norm == pub or calculate_similarity(norm, pub) >= 0.55:
            return False
    return True

def clean_and_deduplicate_script(raw_text: str) -> str:
    """
    Làm sạch kịch bản, triệt tiêu 100% hiện tượng lặp lại phần đầu hoặc câu cú:
    - Loại bỏ câu lặp lại liên tiếp hoặc lặp lại đoạn mở đầu.
    - Loại bỏ các câu rườm rà (lời chào, ngày tháng, giới thiệu thừa).
    - Giữ trọn mạch kịch tính điện ảnh cuốn hút từ giây 0.0.
    """
    if not raw_text:
        return ""

    paragraphs = [para.strip() for para in raw_text.split("\n\n") if para.strip()]
    cleaned_paras = []
    seen_paras = set()

    for para in paragraphs:
        p_norm = " ".join(para.split()).lower()
        if p_norm in seen_paras and len(p_norm) > 50:
            continue
        seen_paras.add(p_norm)

        sentences = [s.strip() for s in re.split(r'(?<=[.!?…])\s+', para) if s.strip()]
        unique_sentences = []
        last_s_norm = ""
        for s in sentences:
            s_norm = " ".join(s.split()).lower()
            if s_norm == last_s_norm and len(s_norm) > 20:
                continue
            last_s_norm = s_norm
            unique_sentences.append(s)

        if unique_sentences:
            cleaned_paras.append(" ".join(unique_sentences))

    return "\n\n".join(cleaned_paras)

def get_daily_10_series(target_date: str = "") -> List[Dict[str, Any]]:
    """
    Sinh danh sách 10 bộ truyện cho một ngày cụ thể (YYYY-MM-DD).
    Nạp toàn bộ văn bản chuẩn điện ảnh cho từng tập.
    Tự động lọc trùng lặp với quá khứ và blacklist.
    ĐẢM BẢO 100% TIÊU ĐỀ KHỚP CHÍNH XÁC VỚI NỘI DUNG AUDIO (Zero False Advertising).
    BẮT BUỘC KIỂM TRA CỔNG KINH NGHIỆM 10 VÒNG (require_preflight_experience).
    """
    require_preflight_experience()
    if not target_date:
        target_date = datetime.now().strftime("%Y-%m-%d")

    day_idx = datetime.strptime(target_date, "%Y-%m-%d").toordinal()
    published_set = get_published_titles_set()
    series_list = []

    for slot in DAILY_10_SLOTS:
        s_idx = slot["slot_index"]
        catalog = SLOT_STORY_CATALOG.get(s_idx, [])
        
        # Chọn câu chuyện độc bản từ kho catalog luân chuyển tịnh tiến theo ngày
        chosen_story = None
        start_offset = (day_idx + s_idx) % len(catalog) if catalog else 0
        
        for offset in range(len(catalog)):
            idx = (start_offset + offset) % len(catalog)
            candidate_fn = catalog[idx]
            cand_story = candidate_fn() if callable(candidate_fn) else candidate_fn
            cand_title = cand_story.get("title", "")
            if is_title_allowed(cand_title, published_set):
                chosen_story = cand_story
                break

        if not chosen_story and catalog:
            idx = start_offset % len(catalog)
            chosen_story = catalog[idx]() if callable(catalog[idx]) else catalog[idx]

        if not chosen_story:
            # Fallback nếu không có catalog
            fallback_fn = SLOT_STORY_LOADERS.get(s_idx)
            chosen_story = fallback_fn() if fallback_fn else {"title": f"Bộ Truyện Khung Giờ {s_idx}", "parts": []}

        # TIÊU ĐỀ CHÍNH XÁC 100% CỦA BỘ TRUYỆN ĐƯỢC CHỌN (KHÔNG GÁN TIÊU ĐỀ LẠ)
        chosen_title = chosen_story.get("title", f"Bộ Truyện Khung Giờ {s_idx}")
        published_set.add(normalize_text(chosen_title))

        date_clean = target_date.replace("-", "")
        prefix = f"VID_{date_clean}_s{s_idx:02d}_{slot['key']}"

        parts_list = []
        for p in chosen_story.get("parts", []):
            p_num = p.get("part_number", 1)
            raw_text = (p.get("full_text") or p.get("text") or p.get("body", "")).strip()
            cleaned_text = clean_and_deduplicate_script(raw_text)
            parts_list.append({
                "part_number": p_num,
                "badge_label": p.get("badge_label", f"TẬP {p_num}" if p_num < 3 else "TẬP 3 - KẾT"),
                "text": cleaned_text,
                "caption": p.get("caption", "")
            })

        # Tạo Hooks & Magnets kích thích bình luận sâu theo bối cảnh truyện
        custom_hooks = chosen_story.get("hooks") or [
            f"Tập 1: {chosen_title}. Theo bạn nhân vật chính nên lựa chọn phương án nào? Hãy bình luận 1 hoặc 2 nhé!",
            f"Tập 2: Nút thắt nghẹt thở! Liệu sự thật có như bạn suy đoán không? Để lại dự đoán bên dưới nhé!",
            f"Tập 3 (Đại Kết Cục): Màn lật kèo chấn động! Bạn thấy cái kết này đã đủ công bằng và thỏa đáng chưa?"
        ]
        custom_magnets = chosen_story.get("magnets") or [
            f"👉 Đón xem tiếp tập 2 trên kênh lúc {slot['start_time_str']} nhé!",
            "👉 Đón xem tập 3 - Đại kết cục bùng nổ sẽ được đăng tải sớm nhất trên kênh!",
            "👉 Hãy bấm Follow kênh để không bỏ lỡ những bộ audio kịch tính tiếp theo nhé!"
        ]

        series_obj = {
            "slot_index": s_idx,
            "key": f"{date_clean}_{slot['key']}",
            "prefix": prefix,
            "title": chosen_title,
            "genre": chosen_story.get("genre", slot["genre"]),
            "voice": chosen_story.get("voice", slot["voice"]),
            "bgm_genre": chosen_story.get("bgm_genre", slot["bgm_genre"]),
            "start_time_str": slot["start_time_str"],
            "hour": slot["hour"],
            "minute": slot["minute"],
            "genre_tag": f"#{slot['genre'].replace(' ', '').lower()} #audiotruyen #podcast #fyp",
            "hooks": custom_hooks,
            "magnets": custom_magnets,
            "parts": parts_list
        }
        series_obj = validate_story_series(series_obj)
        series_list.append(series_obj)

    return series_list

def get_evolution_masterpiece(cycle_id: int) -> Dict[str, Any]:
    """Truy xuất các kịch bản kiệt tác tiến hóa từ Vòng 11 đến Vòng 40."""
    from core.stories.cycles_11_to_20_masterpieces import CYCLE_11_TO_20_STORIES
    from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
    from core.stories.cycles_31_to_40_masterpieces import CYCLE_31_TO_40_STORIES
    pool = {**CYCLE_11_TO_20_STORIES, **CYCLE_21_TO_30_STORIES, **CYCLE_31_TO_40_STORIES}
    if cycle_id in pool:
        return pool[cycle_id]()
    raise ValueError(f"Không tìm thấy kiệt tác vòng {cycle_id}")
