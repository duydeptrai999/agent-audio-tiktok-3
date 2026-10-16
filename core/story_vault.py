# -*- coding: utf-8 -*-
"""
core/story_vault.py
Kho Kịch Bản Truyện Audio Dài 30 Phút Đa Thể Loại (3 Tập x 10+ Phút / >= 4,500 - 5,500 Từ).
Hệ thống kịch bản chuyên sâu theo chuẩn cấu trúc tiểu thuyết audio TikTok triệu view:

1. NGÔN TÌNH:
   - Thanh Xuân Vườn Trường: Chiếc Áo Đồng Phục Năm Ấy (~5,200 từ / ~30+ phút)
   - Truyện Ngược / Ngược Tâm: Khi Hoa Sơn Tra Tàn Lụi (~5,300 từ / ~30+ phút)
   - Hào Môn Tổng Tài: Cưới Em Trước Cưng Chiều Em Sau (~5,600 từ / ~31+ phút)

2. ĐỜI SỐNG / DRAMA GIA ĐÌNH:
   - Mẹ Chồng Nàng Dâu: Đêm Mưa Bị Đuổi Khỏi Nhà Chồng (~5,200 từ / ~30+ phút)
   - Ngoại Tình & Đấu Trí Ly Hôn: Màn Lật Kèo Lúc Nửa Đêm (~5,200 từ / ~30+ phút)
   - Tranh Chấp Di Chúc Gia Tộc: Bí Mật Dưới Nền Bếp (~4,600 từ / ~30+ phút)

3. KINH DỊ / TÂM LINH:
   - Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn (~5,950 từ / ~33+ phút)

4. TRINH THÁM / ĐẤU TRÍ PHÁ ÁN (Kiểu Conan & Sherlock Holmes):
   - Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Bí Ẩn Lúc Nửa Đêm (~4,650 từ / ~33+ phút)

5. DORAEMON / KỲ BÍ VIỄN TƯỞNG:
   - Kỳ Án Cỗ Máy Thời Gian: Lời Cảnh Báo Lúc Nửa Đêm (~4,650 từ / ~33+ phút)

100% Zero-Biography Rule: Tuyệt đối không đọc lý lịch tuổi tác ("Tôi là... năm nay... tuổi") ở 10 giây đầu.
100% Anti-Dropoff: Mở đầu ngay vào biến cố và giữ nhịp căng thẳng nghẹt thở xuyên suốt cả 3 tập.
"""

from typing import Dict, Any

from core.stories.horror import get_30min_horror_story
from core.stories.detective import get_30min_detective_story
from core.stories.romance import get_30min_romance_story
from core.stories.romance_school import get_30min_school_romance_story
from core.stories.romance_angst import get_30min_angst_romance_story
from core.stories.life_drama import get_30min_life_drama_story
from core.stories.life_mother_in_law import get_30min_mother_in_law_story
from core.stories.life_divorce import get_30min_divorce_drama_story
from core.stories.detective_masterpiece import get_detective_masterpiece_story
from core.stories.family_drama_masterpiece import get_family_drama_masterpiece_story
from core.stories.trong_sinh_hoa_sen_lua_masterpiece import get_trong_sinh_hoa_sen_lua_masterpiece_story
from core.stories.me_chong_thuc_tinh_masterpiece import get_me_chong_thuc_tinh_masterpiece_story
from core.stories.huyen_nghi_trang_mau_masterpiece import get_huyen_nghi_trang_mau_masterpiece_story
from core.stories.kinh_di_huyet_nguyen_masterpiece import get_kinh_di_huyet_nguyen_masterpiece_story


def get_story_by_category(category_or_topic: str = "", title: str = "") -> Dict[str, Any]:
    """
    Tự động định tuyến lấy kịch bản 30 phút theo thể loại hoặc từ khóa chủ đề:
    - TRONG_SINH / VA_MAT: Trọng sinh báo thù, đóa sen lửa hào môn, vả mặt trà xanh.
    - THANH_XUAN / VUON_TRUONG: Ngôn tình thanh xuân vườn trường, mối tình đầu, áo đồng phục.
    - NGUOC_TAM / TRUYEN_NGUOC / NGUOC_LUYEN: Ngôn tình ngược tâm, nhận tội thay, hoa sơn tra.
    - ME_CHONG / NANG_DAU / ME_CHONG_NANG_DAU: Drama mẹ chồng nàng dâu độc hại, đêm mưa bị đuổi.
    - NGOAI_TINH / LY_HON / TIEU_TAM: Drama ngoại tình, vạch mặt tiểu tam, đấu trí ly hôn.
    - DOI_SONG / DRAMA / GIA_DINH: Drama gia đình, tranh giành di chúc dưới nền bếp.
    - NGON_TINH / HAO_MON / ROMANCE: Ngôn tình tổng tài, hợp đồng 100 tỷ, cưới trước yêu sau.
    - KINH_DI / TAM_LINH: Truyện kinh dị, quỷ khế căn nhà 44, chiếc gương âm hồn.
    - DORAEMON / VIEN_TUONG: Viễn tưởng kỳ bí cỗ máy thời gian, cánh cửa thần kỳ.
    - TRINH_THAM / CONAN / HOLMES (mặc định): Trinh thám hình sự phá án đấu trí.
    """
    cat = (category_or_topic or "").lower()
    
    # 0. Kiệt tác chuẩn >= 10,380 từ (GEMINI.md Audio 30 Phút)
    if any(k in cat for k in ["trong_sinh", "trọng sinh", "vả mặt", "hoa sen lửa", "thẩm băng tuyết", "sen lửa"]):
        return get_trong_sinh_hoa_sen_lua_masterpiece_story(title)

    if any(k in cat for k in ["gia_dau", "gia đấu", "masterpiece_drama", "50 tỷ", "tô nhược dao", "biệt thự"]):
        return get_family_drama_masterpiece_story(title)

    if any(k in cat for k in ["masterpiece_detective", "detective_masterpiece", "kiệt tác", "masterpiece"]):
        return get_detective_masterpiece_story(title)

    # 1. Ngôn tình - Thanh xuân vườn trường
    if any(k in cat for k in ["thanh_xuan", "vuon_truong", "thanh xuân", "vườn trường", "học đường", "đồng phục", "học sinh", "nguyện ước", "mối tình đầu"]):
        return get_30min_school_romance_story(title)

    # 2. Ngôn tình - Ngược tâm / Ngược luyến tàn tâm
    if any(k in cat for k in ["nguoc_tam", "truyen_nguoc", "ngược", "ngược tâm", "ngược luyến", "sơn tra", "nhận tội thay", "oan khuất", "tàn tạ", "vụn vỡ"]):
        return get_30min_angst_romance_story(title)

    # 3. Drama đời sống - Mẹ chồng nàng dâu (Kiệt tác 10,632 từ độc bản)
    if any(k in cat for k in ["me_chong", "nang_dau", "mẹ chồng", "nàng dâu", "nhà chồng", "mẹ chồng nàng dâu", "đuổi khỏi nhà"]):
        return get_me_chong_thuc_tinh_masterpiece_story(title)

    # 4. Drama đời sống - Ngoại tình & Đấu trí ly hôn
    if any(k in cat for k in ["ngoai_tinh", "ly_hon", "tiểu tam", "ngoại tình", "ly hôn", "thư ký", "phản bội", "chồng ngoại tình", "lật kèo"]):
        return get_30min_divorce_drama_story(title)

    # 5. Tâm linh / Kinh dị (Kiệt tác 10,630 từ độc bản)
    if any(k in cat for k in ["kinh_di", "tam_linh", "kinh dị", "tâm linh", "huyết ấn", "mộ cổ", "quỷ", "ma", "rùng rợn", "nguyền", "gương", "căn nhà số 44"]):
        return get_kinh_di_huyet_nguyen_masterpiece_story(title)
        
    # 6. Đời sống / Gia đình / Drama chung (Di chúc)
    if any(k in cat for k in ["doi_song", "drama", "gia_dinh", "đời sống", "gia đình", "di chúc", "nền bếp", "thừa kế", "anh em"]):
        return get_30min_life_drama_story(title)
        
    # 7. Ngôn tình / Hào môn chung (Hợp đồng tổng tài)
    if any(k in cat for k in ["ngon_tinh", "romance", "hao_mon", "ngôn tình", "hào môn", "tổng tài", "hợp đồng", "cưới", "yêu sau", "100 tỷ"]):
        return get_30min_romance_story(title)
        
    # 8. Doraemon / Viễn tưởng
    if any(k in cat for k in ["doraemon", "thời gian", "cánh cửa", "bảo bối", "viễn tưởng", "lâm minh", "omega"]):
        return get_30min_doraemon_mystery_story(title)
        
    # 9. Huyền nghi / Trinh thám / Conan / Holmes (Default) - Kiệt tác 10,672 từ độc bản
    if any(k in cat for k in ["huyen_nghi", "huyền nghi", "trinh_tham", "trinh thám", "trăng máu"]):
        return get_huyen_nghi_trang_mau_masterpiece_story(title)
    return get_detective_masterpiece_story(title)


__all__ = [
    "get_30min_horror_story",
    "get_30min_detective_story",
    "get_30min_romance_story",
    "get_30min_school_romance_story",
    "get_30min_angst_romance_story",
    "get_30min_life_drama_story",
    "get_30min_mother_in_law_story",
    "get_30min_divorce_drama_story",
    "get_30min_doraemon_mystery_story",
    "get_detective_masterpiece_story",
    "get_family_drama_masterpiece_story",
    "get_trong_sinh_hoa_sen_lua_masterpiece_story",
    "get_me_chong_thuc_tinh_masterpiece_story",
    "get_huyen_nghi_trang_mau_masterpiece_story",
    "get_kinh_di_huyet_nguyen_masterpiece_story",
    "get_story_by_category",
]


