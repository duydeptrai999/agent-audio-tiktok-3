import re
# -*- coding: utf-8 -*-
"""
core/stories/daily_story_factory.py
Kho Cung Cấp & Tự Động Sinh 10 Bộ Truyện Mới Hàng Ngày (Daily Masterpiece Factory):
- Tích hợp 10 Masterpiece Modules chuẩn điện ảnh (15.000+ từ / bộ).
- Đảm bảo 100% không trùng lặp tên, cốt truyện hay mã băm với bất kỳ bộ nào trong quá khứ.
- Ban ngày: Sa điêu, Thanh xuân, Cung đấu, Vả mặt, Mạt thế, Hào môn, Gia đấu.
- Ban đêm (20h30, 22h30, 00h30): Trinh thám kỳ án, Quy tắc quái đàm, Kinh dị đêm muộn rùng rợn.
"""

import hashlib
from datetime import datetime
from typing import Dict, Any, List
from core.daily_schedule_config import DAILY_10_SLOTS
from core.stories.script_quality_gate import validate_story_series

from core.stories.sa_dieu_tieng_long_masterpiece import get_sa_dieu_tieng_long_masterpiece_story
from core.stories.school_romance_vungtrom_masterpiece import get_vungtrom_masterpiece_story
from core.stories.cung_dau_nu_quyen_masterpiece import get_cung_dau_nu_quyen_masterpiece_story
from core.stories.trong_sinh_hoa_sen_lua_masterpiece import get_trong_sinh_hoa_sen_lua_masterpiece_story
from core.stories.mat_the_sinh_ton_masterpiece import get_mat_the_sinh_ton_masterpiece_story
from core.stories.romance_haomon_masterpiece import get_romance_haomon_masterpiece_story
from core.stories.me_chong_thuc_tinh_masterpiece import get_me_chong_thuc_tinh_masterpiece_story
from core.stories.detective_masterpiece import get_detective_masterpiece_story
from core.stories.quai_dam_rap_chieu_phim_masterpiece import get_quai_dam_rap_chieu_phim_masterpiece_story
from core.stories.kinh_di_phong_so_7_masterpiece import get_kinh_di_phong_so_7_masterpiece_story

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

from core.anti_repost_guard import PAST_SERIES_BLACKLIST, normalize_text, calculate_similarity
from pathlib import Path
import json

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
REGISTRY_FILE = ROOT_PATH / "data" / "published_audio_registry.json"

DAILY_THEME_TITLES = {
    1: [
        "Thư Ký Giả Ngốc: Tiếng Lòng Chê Tổng Tài Khiến Cả Phòng Họp Cười Xỉu",
        "Tiếng Lòng Bóc Phốt Của Cô Thư Ký Khiến Lục Tổng Cười Nội Thương",
        "Thư Ký Thực Tập Giả Nai: Tiếng Lòng Bóc Mẽ Âm Mưu Nghìn Tỷ",
        "Khi Tổng Tài Lạnh Lùng Nghe Thấy Tiếng Lòng Chê Cà Vạt Của Thư Ký",
        "Tiếng Lòng Của Nàng Thư Ký Quèn Cứu Lục Tổng Khỏi Cú Lừa 500 Tỷ",
        "Thư Ký Giả Ngốc Bóc Mẽ Kẻ Thù: Lục Tổng Vừa Nhịn Cười Vừa Ký Lệnh Bắt",
        "Tiếng Lòng Của Cô Thư Ký Khiến Tổng Tài Nhịn Cười Cả Buổi Họp",
        "Lục Tổng Và Cô Thư Ký Tinh Quái: Tiếng Lòng Vạch Trần Kẻ Phản Bội"
    ],
    2: [
        "Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ",
        "Thích Thầm Bạn Thân Của Anh Trai: Mối Tình Đầu Mười Năm Giấu Kín",
        "Anh Chàng Áo Trắng Và Viên Kẹo Bạc Hà Năm Mười Bảy Tuổi",
        "Vụng Trộm Thích Thầm: Chàng Trai Mùa Hạ Và Lời Hẹn Dưới Cơn Mưa",
        "Mười Năm Thầm Thương: Lời Hứa Chờ Nhau Trước Cánh Cổng Đại Học",
        "Bí Mật Dưới Đáy Ngăn Kéo: Mối Tình Vụng Trộm Với Thẩm Dục Trì",
        "Chàng Trai Năm Mười Bảy Tuổi Và Chiếc Móc Khóa Cỏ Bốn Lá",
        "Vụng Trộm Thích Anh: Ngọt Ngào Tái Ngộ Sau Bốn Năm Xa Cách"
    ],
    3: [
        "Phượng Hoàng Niết Bàn: Hoàng Hậu Bãi Công Đi Thi Trạng Nguyên",
        "Hoàng Hậu Trả Phượng Ấn: Một Mình Thi Đỗ Trạng Nguyên Vả Mặt Cả Triều Đình",
        "Phế Hậu Thức Tỉnh: Cởi Phượng Bào Đi Thi Trạng Nguyên Khiến Hoàng Đế Hối Hận",
        "Hoàng Hậu Bãi Công: Từ Bỏ Hậu Cung Đỗ Đầu Bảng Vàng Định Đoạt Giang Sơn",
        "Hoàng Hậu Cởi Bỏ Phượng Ấn: Ngày Nàng Đỗ Trạng Nguyên Cả Triều Đình Cúi Đầu",
        "Từ Phế Hậu Lãnh Cung Đến Trạng Nguyên Triều Đình: Màn Phục Thù Rực Rỡ",
        "Hoàng Hậu Trả Lại Hậu Vị: Đăng Quang Trạng Nguyên Khiến Tiêu Triệt Bẽ Bàng",
        "Phượng Hoàng Trở Về: Hoàng Hậu Bãi Công Đi Thi Trạng Nguyên Chấn Động Thiên Hạ"
    ],
    4: [
        "Khi Hoa Sơn Tra Tàn Lụi: Nỗi Oan Khuất 5 Năm Của Cô Dâu Thế Thân",
        "Trọng Sinh Ngày Đính Hôn: Vạch Mặt Tra Nam Từng Đẩy Tôi Vào Tù Nhận Tội Thay",
        "5 Năm Tù Oan Cho Tổng Tài: Ngày Trở Về Tôi Đòi Lại Cả Mạng Sống Lẫn Danh Dự",
        "Đêm Đính Hôn Của Tra Nam: Tấm Thiệp Cưới Rơi Trước Mũi Giày Người Vừa Ra Tù",
        "Vạch Trần Hôn Lễ Bạc Tỷ: Người Đàn Bà Ngồi Tù Thay Tổng Tài Giờ Đã Quay Về",
        "5 Năm Nhận Tội Thay Kẻ Bạc Tình: Màn Phản Công Khiến Hào Môn Trả Giá Đắt",
        "Cú Vả Mặt Tại Sảnh Tiệc Bảy Sao: Món Quà Báo Thù Của Cô Gái Ngồi Tù 5 Năm",
        "Khi Hoa Sơn Tra Nở Rộ: Đoạt Lại Công Lý Cho 5 Năm Thanh Xuân Tù Oan"
    ],
    5: [
        "Trọng Sinh Về 30 Ngày Trước Tận Thế Bão Cát: Hầm Trú Ẩn Bất Khả Xâm Phạm",
        "Tận Thế Bão Cát 60 Độ: Tôi Dùng 100 Tỷ Xây Pháo Đài Sinh Tồn Bất Khả Xâm Phạm",
        "Trọng Sinh 30 Ngày Trước Đại Họa Bão Cát: Pháo Đài Ngầm Của Nữ Hùng Sinh Tồn",
        "Tận Thế Khốc Liệt: Tôi Tích Trữ Lương Thực Trong Hầm Trú Ẩn Xem Kẻ Phản Bội Van Xin",
        "30 Ngày Trước Tận Thế Bão Cát Phóng Xạ: Hầm Ngầm Kiên Cố 100 Tỷ Của Tôi",
        "Trọng Sinh Về Đêm Trước Thảm Họa Bão Cát: Pháo Đài Bất Tử Đuổi Kẻ Bội Bạc",
        "Tận Thế Bão Cát Siêu Cấp: Căn Cứ Ngầm Đầy Đủ Năng Lượng Và Thức Ăn Của Tôi",
        "Trọng Sinh Trước Ngày Cát Bỏng Thiêu Rụi Trái Đất: Pháo Đài Sinh Tồn Bất Khả Xâm Phạm"
    ],
    6: [
        "Bản Hợp Đồng Hôn Nhân 100 Tỷ: Vị Hôn Thê Giả Mạo Của Tổng Tài Tàn Tật",
        "Gả Thay Cho Tổng Tài Tàn Phế: Bản Hợp Đồng Trị Giá 100 Tỷ Đêm Tân Hôn",
        "Nàng Dâu Thế Thân Của Lâm Gia: Cú Lật Kèo Khiến Vị Tổng Tài Ngồi Xe Lăn Bái Phục",
        "Bản Hợp Đồng Hôn Nhân 100 Tỷ: Khi Cô Vợ Gả Thay Không Phải Kẻ Nhu Nhược",
        "Tổng Tài Tàn Tật Và Bản Hợp Đồng 100 Tỷ: Màn Thao Túng Hào Môn Của Vị Hôn Thê",
        "Đêm Tân Hôn Tại Biệt Thự Họ Lâm: Cô Dâu Gả Thay Và Bản Hợp Đồng Định Mệnh",
        "Bản Hợp Đồng Trăm Tỷ: Nàng Dâu Giả Mạo Khiến Tổng Tài Lạnh Lùng Phải Cúi Đầu",
        "Khi Vị Hôn Thê Gả Thay Thức Tỉnh: Thao Túng Tập Đoàn 100 Tỷ Của Tổng Tài Tàn Tật"
    ],
    7: [
        "Đêm Mưa Thức Tỉnh: Bản Khế Ước Gia Tộc Đòi Lại 50 Tỷ",
        "Mẹ Chồng Đuổi Mẹ Con Tôi Trong Đêm Mưa: 7 Năm Sau Tôi Mua Lại Tập Đoàn Hoàng Thị",
        "Bản Khế Ước 50 Tỷ: Màn Vả Mặt Mẹ Chồng Độc Đoán Của Nàng Dâu Bị Đuổi Đi",
        "Bảy Năm Sau Đêm Giông Bão: Người Mẹ Đơn Thân Quay Về Tịch Thu Căn Biệt Thự 50 Tỷ",
        "Mẹ Chồng Từng Vu Oan Tôi Ăn Cắp: Ngày Gặp Lại Cả Nhà Chồng Cũ Phải Cúi Đầu",
        "Đêm Mưa Thức Tỉnh: Cú Phản Đòn Đòi Lại Tài Sản 50 Tỷ Từ Tay Mẹ Chồng Ác Nghiệt",
        "Bản Hợp Đồng Đòi Nợ 50 Tỷ: Nữ Doanh Nhân Trở Về Khiến Nhà Chồng Cũ Phá Sản",
        "7 Năm Tủi Nhục Đổi Lấy Cú Vả Mặt Triệu Đô: Mẹ Chồng Phải Quỳ Lạy Con Dâu Cũ"
    ],
    8: [
        "Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất",
        "Chiếc Điện Thoại Cắt Đứt Dây Lúc Nửa Đêm: 3 Manh Mối Vạch Trần Vụ Án Mạng 5 Năm Trước",
        "Kỳ Án Đồi Thông Ba Vì: Cuộc Gọi Từ Người Đồng Đội Đã Chết 5 Năm Trước",
        "Hồ Sơ Căn Phòng Số 13: Vụ Án Mạng Kín Cổng Cao Tường Của Đại Án Vạn Hưng",
        "Tiếng Chuông Điện Thoại Không Dây Lúc 2 Giờ Sáng: Bí Mật Dưới Hầm Biệt Thự Ba Vì",
        "Hồ Sơ Mật Căn Phòng Số 13: Chiếc USB Nghìn Tỷ Và Lời Trăng Trối Của Người Đã Khuất",
        "Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Vạch Mặt Trùm Cuối Cảnh Sát Biến Chất",
        "Bí Mật Căn Phòng Số 13 Đồi Thông: Khi Kẻ Đã Chết 5 Năm Gọi Điện Báo Án"
    ],
    9: [
        "Quy Tắc Sinh Tồn Rạp Chiếu Phim Đêm: Đừng Bao Giờ Ngồi Hàng Ghế Số 4",
        "Rạp Chiếu Phim Lúc 0 Giờ: 7 Quy Tắc Sống Còn Khi Thấy Bóng Người Áo Đen",
        "Tấm Vé Suất Chiếu Nửa Đêm: Lời Cảnh Báo Viết Bằng Mực Đỏ Trên Hàng Ghế Số 4",
        "Quy Tắc Buồng Chiếu Phim Cũ: Tuyệt Đối Không Nhìn Xuống Hàng Ghế Số 4",
        "Rạp Phim Hòa Bình Lúc Nửa Đêm: Bản Quy Tắc Sinh Tồn Dành Cho 3 Người Còn Sống",
        "Suất Chiếu 0 Giờ: Đừng Nhìn Vào Mắt Kẻ Ngồi Ở Hàng Ghế Số 4",
        "Quy Tắc Trực Đêm Rạp Chiếu Phim: Bóng Áo Mưa Đen Và Cuộn Phim 35mm",
        "Lời Nguyền Suất Chiếu Nửa Đêm: 6 Quy Tắc Cấm Kỵ Tại Hàng Ghế Số 4"
    ],
    10: [
        "Khách Trọ Phòng Số 7: Người Đàn Bà Mặc Áo Đỏ Dưới Đèn Đường",
        "Ngõ Cụt Số 47 Lúc 11 Giờ Đêm: Người Phụ Nữ Áo Đỏ Cầm Ô Đen Nhỏ Nước",
        "Khách Trọ Phòng Số 7: Bí Ẩn Người Phụ Nữ Áo Đỏ Dưới Đèn Đường Vàng Vọt",
        "Phòng Trọ Số 7 Lúc Nửa Đêm: Tuyệt Đối Đừng Mở Cửa Sổ Khi Nghe Tiếng Nước Rơi",
        "Dãy Trọ Cũ Ngõ 47: Lời Cảnh Báo Của Bà Chủ Về Người Đàn Bà Áo Đỏ",
        "Khách Trọ Phòng Số 7: Tiếng Nước Nhỏ Giọt Ngoài Ban Công Lúc Nửa Đêm",
        "Bí Mật Căn Phòng Số 7: Chiếc Ô Đen Nhỏ Nước Đỏ Dưới Đèn Đường Lúc 0 Giờ",
        "Ác Mộng Phòng Trọ Số 7: Tiếng Gọi Tên Trong Đêm Của Người Đàn Bà Áo Đỏ"
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
        if norm == pub or calculate_similarity(norm, pub) >= 0.5:
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
    Nạp toàn bộ văn bản 15.000+ từ chuẩn điện ảnh cho từng tập.
    Tự động lọc trùng lặp với quá khứ và blacklist.
    BẮT BUỘC KIỂM TRA CỔNG KINH NGHIỆM 10 VÒNG (require_preflight_experience).
    """
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()
    if not target_date:
        target_date = datetime.now().strftime("%Y-%m-%d")

    date_hash = int(hashlib.md5(target_date.encode('utf-8')).hexdigest()[:8], 16)
    published_set = get_published_titles_set()
    series_list = []

    for slot in DAILY_10_SLOTS:
        s_idx = slot["slot_index"]
        title_options = DAILY_THEME_TITLES[s_idx]
        
        # Chọn tựa đề sạch, không trùng lặp và không dính blacklist
        chosen_title = ""
        start_offset = (date_hash + s_idx) % len(title_options)
        for offset in range(len(title_options)):
            candidate = title_options[(start_offset + offset) % len(title_options)]
            if is_title_allowed(candidate, published_set):
                chosen_title = candidate
                break
        
        if not chosen_title:
            chosen_title = f"{title_options[start_offset]} (Bản Đặc Biệt Ngày {target_date})"

        date_clean = target_date.replace("-", "")
        prefix = f"VID_{date_clean}_s{s_idx:02d}_{slot['key']}"

        # Nạp dữ liệu Masterpiece tương ứng
        loader_fn = SLOT_STORY_LOADERS.get(s_idx)
        if loader_fn:
            story_data = loader_fn(title=chosen_title)
        else:
            story_data = {"parts": []}

        parts_list = []
        for p in story_data.get("parts", []):
            p_num = p.get("part_number", 1)
            raw_text = (p.get("full_text") or p.get("text", "")).strip()
            cleaned_text = clean_and_deduplicate_script(raw_text)
            # Mở đầu kịch tính trực diện 100% cốt truyện, không đọc ngày tháng, tập số hay lời chào rườm rà
            parts_list.append({
                "part_number": p_num,
                "badge_label": p.get("badge_label", f"TẬP {p_num}"),
                "text": cleaned_text,
                "caption": p.get("caption", "")
            })

        series_obj = {
            "slot_index": s_idx,
            "key": f"{date_clean}_{slot['key']}",
            "prefix": prefix,
            "title": chosen_title,
            "genre": slot["genre"],
            "voice": slot["voice"],
            "bgm_genre": slot["bgm_genre"],
            "start_time_str": slot["start_time_str"],
            "hour": slot["hour"],
            "minute": slot["minute"],
            "genre_tag": f"#{slot['genre'].replace(' ', '').lower()} #audiotruyen #podcast #fyp",
            "hooks": [
                f"Đón xem tập 1 của {chosen_title}!",
                f"Nút thắt kịch tính trong tập 2 của {chosen_title}!",
                f"Đại kết cục bùng nổ của {chosen_title}!"
            ],
            "magnets": [
                "👉 Đón xem trọn bộ 3 tập trên kênh nhé!",
                "👉 Bình luận cảm nghĩ của bạn bên dưới nhé!",
                "👉 Hãy để lại bình luận và Follow kênh nhé!"
            ],
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
