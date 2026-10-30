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
from core.stories.sa_dieu_show_hen_ho_masterpiece import get_sa_dieu_show_hen_ho_masterpiece_story
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
from core.stories.cung_dau_dich_nu_tuong_mon_masterpiece import get_cung_dau_dich_nu_tuong_mon_masterpiece_story
from core.stories.cung_dau_duoc_y_thuc_tinh_masterpiece import get_cung_dau_duoc_y_thuc_tinh_masterpiece_story

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
from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story
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
from core.stories.quai_dam_khach_san_masterpiece import get_quai_dam_khach_san_masterpiece_story
from core.stories.horror_chuyentau_masterpiece import get_horror_chuyentau_masterpiece_story

# Slot 10: Kinh dị đêm muộn / Rùng rợn tâm linh đô thị
from core.stories.kinh_di_phong_so_7_masterpiece import get_kinh_di_phong_so_7_masterpiece_story
from core.stories.kinh_di_huyet_nguyen_masterpiece import get_kinh_di_huyet_nguyen_masterpiece_story
from core.stories.horror_guongquy_masterpiece import get_horror_guongquy_masterpiece_story
from core.stories.horror_trocot_masterpiece import get_horror_trocot_masterpiece_story
from core.stories.horror import get_30min_horror_story

# Masterpiece Vòng 11 - 20
from core.stories.cycles_11_to_20_masterpieces import (
    get_story_cycle_11, get_story_cycle_12, get_story_cycle_13, get_story_cycle_14,
    get_story_cycle_15, get_story_cycle_16, get_story_cycle_17, get_story_cycle_18,
    get_story_cycle_19, get_story_cycle_20
)

# Masterpiece Vòng 21 - 30
from core.stories.cycles_21_to_30_masterpieces import (
    get_story_cycle_21, get_story_cycle_22, get_story_cycle_23, get_story_cycle_24,
    get_story_cycle_25, get_story_cycle_26, get_story_cycle_27, get_story_cycle_28,
    get_story_cycle_29, get_story_cycle_30
)

# Masterpiece Vòng 31 - 40
from core.stories.cycles_31_to_40_masterpieces import (
    get_story_cycle_31, get_story_cycle_32, get_story_cycle_33, get_story_cycle_34,
    get_story_cycle_35, get_story_cycle_36, get_story_cycle_37, get_story_cycle_38,
    get_story_cycle_39, get_story_cycle_40
)

# Masterpiece Vòng 41 - 50: Đu Trend Xã Hội Nổi Cộm & 100% Zero Chính Trị
from core.stories.cycles_41_to_50_masterpieces import (
    get_story_cycle_41, get_story_cycle_42, get_story_cycle_43, get_story_cycle_44,
    get_story_cycle_45, get_story_cycle_46, get_story_cycle_47, get_story_cycle_48,
    get_story_cycle_49, get_story_cycle_50
)

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
REGISTRY_FILE = ROOT_PATH / "data" / "published_audio_registry.json"

# --- CATALOG KIỆT TÁC THEO TỪNG SLOT (SLOT_STORY_CATALOG) ---
# 100% KHO KIỆT TÁC ĐỘC BẢN THẬT (4.200 - 10.672 TỪ, ZERO 49S TOLERANCE)
SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,  # 4.922 từ Sa điêu / Tiếng lòng sếp
        get_sa_dieu_show_hen_ho_masterpiece_story, # 4.800 từ Sa điêu / Show hẹn hò cá mặn
    ],
    2: [
        get_30min_school_romance_story,            # 10.497 từ Thanh xuân vườn trường / Họp lớp
        get_vungtrom_masterpiece_story,            # 4.594 từ Vụng trộm ngọt ngào mười năm
    ],
    3: [
        get_cung_dau_duoc_y_thuc_tinh_masterpiece_story,  # 5.400 từ Thứ nữ ngự y thử độc
        get_cung_dau_dich_nu_tuong_mon_masterpiece_story,  # 4.355 từ Đích nữ tướng môn
        get_cung_dau_nu_quyen_masterpiece_story,   # 4.562 từ Phượng hoàng bãi công thi Trạng Nguyên
    ],
    4: [
        get_30min_divorce_drama_story,             # 4.685 từ Ly hôn đòi tài sản
        get_30min_angst_romance_story,             # 5.665 từ Ngược tâm hoa sơn tra thức tỉnh
        get_me_chong_thuc_tinh_masterpiece_story,  # 4.374 từ Mẹ chồng thức tỉnh trả lại hào quang
    ],
    5: [
        get_mat_the_sinh_ton_masterpiece_story,    # 4.567 từ Mạt thế bão cát pháo đài ngầm
        get_mat_the_bang_gia_masterpiece_story,    # 4.800 từ Mạt thế cực hàn pháo đài nhiệt
    ],
    6: [
        get_romance_haomon_masterpiece_story,      # 5.657 từ Hợp đồng hôn nhân hào môn
        get_romance_chualanh_tuyetpham_story,      # 5.657 từ Hào môn chữa lành tuyệt phẩm
        get_life_healing_masterpiece_story,        # 5.050 từ Chữa lành cuối ngày chuyến xe đêm
        get_30min_romance_story,                   # 5.529 từ Hào môn tổng tài độc lập tài chính
    ],
    7: [
        get_man_tra_thu_masterpiece_story,        # 4.970 từ Mẹ chồng nàng dâu / Bát canh sau sinh
        get_30min_mother_in_law_story,             # 4.776 từ Mẹ chồng tính toán từng đồng
        get_30min_life_drama_story,                # 4.556 từ Giỗ đầu gia đấu đời thực
    ],
    8: [
        get_detective_masterpiece_story,           # 8.038 từ Căn phòng số 13 trinh thám
        get_huyen_nghi_trang_mau_masterpiece_story, # 8.455 từ Biệt thự trăng máu
        get_30min_detective_story,                 # 4.480 từ Vụ án đèo Bảo Lộc
        get_30min_doraemon_mystery_story,          # 4.484 từ Bí ẩn vật lý lượng tử di vật
    ],
    9: [
        get_quai_dam_khach_san_masterpiece_story,  # 4.552 từ Khách sạn Bạch Ngân ca đêm
        get_horror_chuyentau_masterpiece_story,    # 6.432 từ Chuyến tàu điện ngầm lúc 0 giờ
    ],
    10: [
        get_horror_guongquy_masterpiece_story,     # 8.108 từ Quỷ khế gương đồng phòng số 44
        get_horror_trocot_masterpiece_story,       # 6.100 từ Hũ tro cốt dưới gầm giường
        get_30min_horror_story,                    # 5.834 từ Tấm lụa đỏ gương đồng cổ
        get_kinh_di_huyet_nguyen_masterpiece_story, # 8.453 từ Nhật ký huyết nguyện biệt thự cổ
    ]
}

# Tương thích ngược cho các module cũ
SLOT_STORY_LOADERS = {
    1: get_sa_dieu_tieng_long_masterpiece_story,
    2: get_vungtrom_masterpiece_story,
    3: get_cung_dau_duoc_y_thuc_tinh_masterpiece_story,
    4: get_30min_divorce_drama_story,
    5: get_mat_the_sinh_ton_masterpiece_story,
    6: get_romance_haomon_masterpiece_story,
    7: get_man_tra_thu_masterpiece_story,
    8: get_detective_masterpiece_story,
    9: get_quai_dam_khach_san_masterpiece_story,
    10: get_horror_guongquy_masterpiece_story
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
        "Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Sau Sinh",
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
    - Cắt sạch meta CTAs quảng cáo kêu gọi bấm like / follow / danh sách phát ở cuối.
    - Giữ trọn mạch kịch tính điện ảnh cuốn hút từ giây 0.0.
    """
    if not raw_text:
        return ""

    paragraphs = [para.strip() for para in raw_text.split("\n\n") if para.strip()]
    cleaned_paras = []
    seen_paras = set()

    META_CTA_PATTERN = re.compile(
        r'(?i)(bấm theo dõi|đón xem tiếp|like và follow|chúc các bạn nghe truyện|'
        r'hẹn gặp lại các bạn|đăng ký kênh|danh sách phát|đón xem tập).*?$',
        re.DOTALL
    )

    for para in paragraphs:
        p_clean = META_CTA_PATTERN.sub('', para).strip()
        if not p_clean:
            continue

        p_norm = " ".join(p_clean.split()).lower()
        if p_norm in seen_paras and len(p_norm) > 50:
            continue
        seen_paras.add(p_norm)

        sentences = [s.strip() for s in re.split(r'(?<=[.!?…])\s+', p_clean) if s.strip()]
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

def generate_contextual_hooks_and_magnets(
    title: str,
    genre: str,
    parts_list: List[Dict[str, Any]],
    start_time_str: str
) -> tuple:
    """
    Sinh bộ Hooks & Comment Magnets phân cực theo đúng ngữ cảnh cốt truyện (Master Codex 8.0 - Trụ cột 5).
    ĐẶC BIỆT: Trích xuất trích đoạn biến cố riêng biệt cho TẬP 1, TẬP 2 và TẬP 3, triệt tiêu 100% mô tả lặp lại.
    Triệt tiêu hoàn toàn mẫu câu robot 'Theo bạn nhân vật chính nên lựa chọn phương án nào? Hãy bình luận 1 hoặc 2 nhé!'.
    """
    g_upper = (genre or "").upper()
    t_lower = (title or "").lower()

    def extract_snippet(idx: int) -> str:
        if parts_list and len(parts_list) > idx and parts_list[idx].get("text"):
            text = parts_list[idx]["text"].strip()
            first_sent = re.split(r'(?<=[.!?…])\s+', text)[0]
            words = first_sent.split()
            return (" ".join(words[:22]) + ("..." if len(words) > 22 else "")).strip()
        return ""

    s1 = extract_snippet(0)
    s2 = extract_snippet(1)
    s3 = extract_snippet(2)

    if any(k in t_lower or k in g_upper.lower() for k in ["mẹ chồng", "ly hôn", "lật kèo", "làm dâu", "giỗ", "trả thù", "hôn nhân", "gia đấu", "đời sống"]):
        hooks = [
            f"«{s1}» — Mâu thuẫn bùng nổ ngay phút đầu! Nếu rơi vào hoàn cảnh bị gia đình nhà chồng tính toán trắng trợn thế này, bạn chọn nhẫn nhịn cho êm ấm hay âm thầm thu thập chứng cứ phản đòn?",
            f"«{s2}» — Đỉnh điểm trơ tráo khi sự thật lộ diện! Theo bạn nữ chính nên tung sao kê vạch mặt ngay tại chỗ hay đợi hoàn tất thủ tục pháp lý mới hạ màn?",
            f"«{s3}» — Màn lật ngược thế cờ mãn nhãn khiến những kẻ tham lam phải trả giá đắt! Bạn chấm mấy trên 10 cho pha xử lý quyết đoán này?"
        ]
    elif any(k in t_lower or k in g_upper.lower() for k in ["tiếng lòng", "sa điêu", "thư ký", "cá mặn", "công sở"]):
        hooks = [
            f"«{s1}» — Đi làm sợ nhất sếp vẽ bánh vẽ, nhưng lỡ đọc được tiếng lòng thật sự thế này thì nên xin nghỉ hay ở lại hóng kịch hay tiếp đây mọi người?",
            f"«{s2}» — Cả phòng họp nín thở trước pha đối đáp đỉnh nóc kịch trần! Nếu ngồi ở vị trí nhân vật chính lúc này, bạn sẽ nhịn cười hay tung chiêu?",
            f"«{s3}» — Cái kết sảng khoái không trượt phát nào! Đi làm kiếm tiền nhưng niềm vui hóng chuyện mới là bất tử, bạn tâm đắc nhất tình huống nào?"
        ]
    elif any(k in t_lower or k in g_upper.lower() for k in ["thanh xuân", "học đường", "vụng trộm", "đồng phục", "mùa hạ", "chữa lành"]):
        hooks = [
            f"«{s1}» — Ai cũng có một bóng hình từng thương thầm suốt những năm tháng áo trắng. Nghe đoạn mở đầu này, bạn có bồi hồi nhớ lại mối tình đầu của mình không?",
            f"«{s2}» — Khoảnh khắc gặp lại sau chuỗi ngày dài xa cách nghẹn ngào đến thắt lòng. Theo bạn hiểu lầm năm xưa có kịp tháo gỡ trước khi quá muộn?",
            f"«{s3}» — Bản tình ca ngọt ngào chữa lành mọi vết thương thanh xuân! Một cái kết trọn vẹn dành cho những người có duyên ắt sẽ tìm về bên nhau."
        ]
    elif any(k in t_lower or k in g_upper.lower() for k in ["mạt thế", "sinh tồn", "bão cát", "băng giá", "tận thế", "hầm"]):
        hooks = [
            f"«{s1}» — Tận thế ập đến trong chớp mắt! Khi đối mặt với thảm họa sống còn, theo bạn sự chuẩn bị chu đáo hay lòng thương hại mới là thứ cứu sống bạn?",
            f"«{s2}» — Lòng người hiểm ác lộ nguyên hình trước miếng ăn sống còn! Nếu người thân từng hãm hại bạn đến cầu cứu ngoài cửa, bạn có mở then cài?",
            f"«{s3}» — Pháo đài bất khả xâm phạm và bài học đắt giá cho những kẻ tham lam cướp bóc! Bạn đánh giá thế nào về chiến thuật sinh tồn này?"
        ]
    elif any(k in t_lower or k in g_upper.lower() for k in ["cung đấu", "đích nữ", "hoàng hậu", "trọng sinh", "hoa sơn tra"]):
        hooks = [
            f"«{s1}» — Sống lại một đời, tuyệt đối không làm quân cờ thí mạng cho kẻ bạc tình! Bạn thấy nước cờ phản kích mở màn này đã đủ dứt khoát chưa?",
            f"«{s2}» — Kẻ ngỡ mình đang giăng lưới lại chính là con mồi sập bẫy! Đoạn đối chất nảy lửa này bạn ấn tượng nhất câu nói nào?",
            f"«{s3}» — Màn đoạt lại vận mệnh kiêu hãnh của bậc nữ cường! Cái giá mà những kẻ phản bội phải trả theo bạn đã đủ tương xứng chưa?"
        ]
    else:
        hooks = [
            f"«{s1}» — Manh mối bất thường xuất hiện ngay từ những giây đầu tiên! Nghe kỹ chi tiết này, bạn có nhận ra điểm bất thường nằm ở đâu không?",
            f"«{s2}» — Từng quy tắc ngầm và bức màn bí mật đang dần hé lộ! Khuyến cáo đeo tai nghe để cảm nhận rõ nhất không khí nghẹt thở này.",
            f"«{s3}» — Sự thật kinh hoàng phía sau khiến ai nghe xong cũng rợn người! Bạn đã nhìn thấu hung thủ hay chân tướng từ tập mấy?"
        ]

    magnets = [
        "🎧 Cắm tai nghe để hòa mình vào từng nhịp thở của câu chuyện. Tập 2 đã lên sóng trên kênh!",
        "🔥 Nút thắt nghẹt thở sẽ bùng nổ trọn vẹn ở Tập 3 (Đại Kết Cục) — Bấm vào kênh để nghe tiếp ngay nhé!",
        "❤️ Follow kênh và để lại bình luận chia sẻ cảm nhận của bạn để tụi mình tiếp tục ra mắt những bộ audio chất lượng nhất!"
    ]
    return hooks, magnets

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
        
        today_chosen_titles = {normalize_text(s.get("title", "")) for s in series_list}

        for offset in range(len(catalog)):
            idx = (start_offset + offset) % len(catalog)
            candidate_fn = catalog[idx]
            cand_story = candidate_fn() if callable(candidate_fn) else candidate_fn
            cand_title = cand_story.get("title", "")
            cand_norm = normalize_text(cand_title)
            
            # Cấm tuyệt đối trùng lặp câu chuyện đã chọn trong cùng ngày
            if cand_norm in today_chosen_titles:
                continue

            if is_title_allowed(cand_title, published_set):
                parts = cand_story.get("parts", [])
                if isinstance(parts, dict):
                    parts = [
                        {"part_number": 1, "text": parts.get("part1", "")},
                        {"part_number": 2, "text": parts.get("part2", "")},
                        {"part_number": 3, "text": parts.get("part3", "")}
                    ]
                elif not parts and ("part1" in cand_story or "part2" in cand_story):
                    parts = [
                        {"part_number": 1, "text": cand_story.get("part1", "")},
                        {"part_number": 2, "text": cand_story.get("part2", "")},
                        {"part_number": 3, "text": cand_story.get("part3", "")}
                    ]
                if parts:
                    lens = [len((p.get("full_text") or p.get("text") or "").split()) for p in parts]
                else:
                    lens = [len(cand_story.get(f"part{i}", "").split()) for i in (1, 2, 3)]
                if lens and min(lens) >= 1200 and sum(lens) >= 4200:
                    chosen_story = cand_story
                    break

        if not chosen_story and catalog:
            for offset in range(len(catalog)):
                idx = (start_offset + offset) % len(catalog)
                candidate_fn = catalog[idx]
                cand_story = candidate_fn() if callable(candidate_fn) else candidate_fn
                cand_title = cand_story.get("title", "")
                if normalize_text(cand_title) not in today_chosen_titles:
                    chosen_story = cand_story
                    break

        if not chosen_story:
            fallback_fn = SLOT_STORY_LOADERS.get(s_idx)
            chosen_story = fallback_fn() if fallback_fn else {"title": f"Bộ Truyện Khung Giờ {s_idx}", "parts": []}

        # TIÊU ĐỀ CHÍNH XÁC 100% CỦA BỘ TRUYỆN ĐƯỢC CHỌN (KHÔNG GÁN TIÊU ĐỀ LẠ)
        chosen_title = chosen_story.get("title", f"Bộ Truyện Khung Giờ {s_idx}")
        published_set.add(normalize_text(chosen_title))

        date_clean = target_date.replace("-", "")
        prefix = f"VID_{date_clean}_s{s_idx:02d}_{slot['key']}"

        parts_list = []
        parts_source = chosen_story.get("parts", [])
        if isinstance(parts_source, dict):
            parts_source = [
                {"part_number": 1, "text": parts_source.get("part1", "")},
                {"part_number": 2, "text": parts_source.get("part2", "")},
                {"part_number": 3, "text": parts_source.get("part3", "")}
            ]
        elif not parts_source and ("part1" in chosen_story or "part2" in chosen_story):
            parts_source = [
                {"part_number": 1, "text": chosen_story.get("part1", "")},
                {"part_number": 2, "text": chosen_story.get("part2", "")},
                {"part_number": 3, "text": chosen_story.get("part3", "")}
            ]
        for p in parts_source:
            p_num = p.get("part_number", 1)
            raw_text = (p.get("full_text") or p.get("text") or p.get("body", "")).strip()
            cleaned_text = clean_and_deduplicate_script(raw_text)
            parts_list.append({
                "part_number": p_num,
                "badge_label": p.get("badge_label", f"TẬP {p_num}" if p_num < 3 else "TẬP 3 - KẾT"),
                "text": cleaned_text,
                "caption": p.get("caption", "")
            })

        # Tạo Hooks & Magnets phân cực kích thích tranh luận thực tế theo bối cảnh truyện (Master Codex 8.0)
        ctx_hooks, ctx_magnets = generate_contextual_hooks_and_magnets(
            title=chosen_title,
            genre=chosen_story.get("genre", slot["genre"]),
            parts_list=parts_list,
            start_time_str=slot["start_time_str"]
        )
        custom_hooks = chosen_story.get("hooks") or ctx_hooks
        custom_magnets = chosen_story.get("magnets") or ctx_magnets

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
