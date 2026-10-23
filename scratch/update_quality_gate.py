# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/stories/script_quality_gate.py")
text = fpath.read_text(encoding="utf-8")

old_forbidden = '''# Danh sách sáo ngữ convert tuyệt đối cấm và từ thay thế thuần Việt
FORBIDDEN_PHRASES = {
    "khí chất bức người": "khí thế áp đảo",
    "bóp nghẹt lồng ngực": "nghẹt thở",
    "máu tươi tuôn xối xả": "chảy máu",
    "cười lạnh một tiếng": "cười nhạt",
    "đứng sững như trời trồng": "chết lặng",
    "thập phần": "vô cùng",
    "bất giác": "vô thức",
    "hơi thở phả vào làn da": "đứng sát ngay bên",
    "như nhìn một con sâu bọ": "khinh miệt",
    "nụ cười nham hiểm độc địa": "nụ cười toan tính",
    "sét đánh ngang tai": "bàng hoàng",
    "đồ tiện tì": "kẻ phản bội",
    "đồ súc sinh": "kẻ vô ơn",
    "tiện nhân": "kẻ trơ trẽn",
    "đồ lăng loàn": "kẻ bội bạc",
    "thằng khốn nạn": "kẻ đê hèn",
    "kinh hoàng tột độ": "tim đập dồn dập",
    "vô cùng sửng sốt": "đồng tử co giật",
    "sợ đến phát điên": "chân run bần bật",
    "mắt mở to như nhìn thấy quái vật": "kinh ngạc",
    "vô cùng tức giận": "ngón tay siết chặt",
    "đau đớn tột cùng": "lồng ngực nghẹn đắng",
    "sợ hãi tột độ": "mồ hôi lạnh chảy dọc sống lưng",
    "hoang mang tột độ": "đồng tử co rút",
    "đau khổ tột cùng": "cắn chặt môi rớm máu",
    "bản án tử hình": "lời cảnh báo lạnh gáy",
    "hận thù ngút trời": "ngọn lửa thù hận",
    "ác mộng kinh hoàng": "hiện thực tàn khốc",
    "chết lặng như bị bàng hoàng": "chết lặng",
}

# Các mẫu mở đầu rập khuôn cấm kỵ
CLICHE_OPENING_PATTERNS = [
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Đúng\s+\d+\s+giờ",
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+hét",
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+thét",
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+xé",
    r"^Đúng\s+\d+\s+giờ\s+(sáng|tối)\s+giữa\s+đêm\s+mưa",
    r"^Trời\s+mưa\s+như\s+trút\s+nước",
    r"^Nếu\s+bạn\s+vô\s+tình",
    r"^Hôm\s+nay\s+tôi\s+sẽ\s+kể",
    r"^Chào\s+các\s+bạn",
    r"^Tôi\s+tên\s+là",
    r"^Sinh\s+ra\s+trong\s+một",
    r"^Đó\s+là\s+một\s+ngày",
]'''

new_forbidden = '''# Danh sách sáo ngữ convert tuyệt đối cấm và từ thay thế thuần Việt
FORBIDDEN_PHRASES = {
    "khí chất bức người": "khí thế áp đảo",
    "bóp nghẹt lồng ngực": "nghẹt thở",
    "máu tươi tuôn xối xả": "chảy máu",
    "cười lạnh một tiếng": "cười nhạt",
    "đứng sững như trời trồng": "chết lặng",
    "thập phần": "vô cùng",
    "bất giác": "vô thức",
    "hơi thở phả vào làn da": "đứng sát ngay bên",
    "như nhìn một con sâu bọ": "khinh miệt",
    "nụ cười nham hiểm độc địa": "nụ cười toan tính",
    "sét đánh ngang tai": "bàng hoàng",
    "đồ tiện tì": "kẻ phản bội",
    "đồ súc sinh": "kẻ vô ơn",
    "tiện nhân": "kẻ trơ trẽn",
    "đồ lăng loàn": "kẻ bội bạc",
    "thằng khốn nạn": "kẻ đê hèn",
    "kinh hoàng tột độ": "tim đập dồn dập",
    "vô cùng sửng sốt": "đồng tử co giật",
    "sợ đến phát điên": "chân run bần bật",
    "mắt mở to như nhìn thấy quái vật": "kinh ngạc",
    "vô cùng tức giận": "ngón tay siết chặt",
    "đau đớn tột cùng": "lồng ngực nghẹn đắng",
    "sợ hãi tột độ": "mồ hôi lạnh chảy dọc sống lưng",
    "hoang mang tột độ": "đồng tử co rút",
    "đau khổ tột cùng": "cắn chặt môi rớm máu",
    "bản án tử hình": "lời cảnh báo lạnh gáy",
    "hận thù ngút trời": "ngọn lửa thù hận",
    "ác mộng kinh hoàng": "hiện thực tàn khốc",
    "chết lặng như bị bàng hoàng": "chết lặng",
    "mình... mình chưa chết": "tôi bàng hoàng mở mắt",
    "mình đã thực sự trọng sinh": "tôi nhìn đồng hồ đếm ngược",
    "lũ súc sinh vô ơn": "những kẻ phản trắc",
    "nhâm nhi ly trà sữa": "nhìn qua camera",
    "nụ cười sắc lạnh thấu xương": "nụ cười toan tính",
    "thẩm băng tuyết thong thả nhấp ngụm rượu vang": "ngón tay lật giở trang hồ sơ",
    "trong ván cờ sinh tử của giới tài phiệt": "trên bàn đàm phán",
    "giá trị đích thực của một con người": "kết quả kinh doanh",
    "mười năm sống trong bùn lầy kiếp trước": "những năm tháng gian khó",
    "từng con số kiểm toán sắc lẹm như những nhát búa": "từng con số kiểm toán đối chiếu",
}

# Các mẫu mở đầu rập khuôn cấm kỵ (4 Tử Huyệt Khiến Khán Giả Lướt Qua Màn Hình)
CLICHE_OPENING_PATTERNS = [
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Đúng\s+\d+\s+giờ",
    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+(hét|thét|xé|gầm|đập|rên)",
    r"^Đúng\s+\d+\s+giờ\s+(sáng|tối)\s+giữa\s+đêm\s+mưa",
    r"^Trời\s+mưa\s+như\s+trút\s+nước",
    r"^Nếu\s+bạn\s+vô\s+tình",
    r"^Hôm\s+nay\s+tôi\s+sẽ\s+kể",
    r"^Chào\s+các\s+bạn",
    r"^Tôi\s+tên\s+là",
    r"^Sinh\s+ra\s+trong\s+một",
    r"^Đó\s+là\s+một\s+ngày",
    r"^Bảy\s+năm\s+(sau|trước)",
    r"^Mười\s+năm\s+(sau|trước)",
    r"^Mình\.\.\.\s*mình\s+(chưa\s+chết|trọng\s+sinh)",
    r"^Tại\s+đám\s+tang\s+của\s+người\s+chồng",
    r"^Trước\s+khi\s+phiên\s+họp",
]'''

norm_text = text.replace("\r\n", "\n")
norm_old = old_forbidden.replace("\r\n", "\n")

if norm_old in norm_text:
    norm_text = norm_text.replace(norm_old, new_forbidden.replace("\r\n", "\n"))
    fpath.write_text(norm_text, encoding="utf-8")
    print("Updated core/stories/script_quality_gate.py successfully!")
else:
    print("Could not find old_forbidden block")
