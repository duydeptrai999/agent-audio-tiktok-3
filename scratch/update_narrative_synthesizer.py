# -*- coding: utf-8 -*-
from pathlib import Path
import re

fpath = Path("core/narrative_synthesizer.py")
text = fpath.read_text(encoding="utf-8")

# Thay thế các hook cũ trong narrative_synthesizer.py
replacements = [
    # me_chong
    (
        r'''"hook":\s*"'Nếu bảy năm trước bà không ném vali đồ[^"]+"''',
        '"hook": "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi."'
    ),
    (
        r'''"title":\s*"Tập 1:\s*Đêm Mưa Bị Đuổi Khỏi Hào Môn & Thân Thế Thật",\s*"hook":\s*"'Nếu bảy năm trước[^"]+"''',
        '"title": "Tập 1: Bát Yến Chưng Dưới Đáy Bản Khế Ước",\n                "hook": "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi."'
    ),
    (
        r'''"title":\s*"Tập 2:\s*Màn Đấu Giá 120 Tỷ & Âm Mưu Tống Tiền",\s*"hook":\s*"Bảy năm sau đêm mưa bão[^"]+"''',
        '"title": "Tập 2: Màn Sao Kê Tài Khoản Hai Trăm Tỷ",\n                "hook": "Bản sao kê tài khoản hai trăm tỷ vừa ném xuống bàn trà, ánh mắt run rẩy của bà mẹ chồng đã không còn nét kiêu kỳ ngày trước."'
    ),
    (
        r'''"title":\s*"Tập 3:\s*Đại Kết Cục Viên Mãn & Bản Lĩnh Phụ Nữ Tự Chủ",\s*"hook":\s*"Ngày Tô Nhược Dao chính thức tiếp quản[^"]+"''',
        '"title": "Tập 3: Đại Kết Cục Phong Tỏa Tài Sản",\n                "hook": "Lệnh phong tỏa tài sản và thu hồi căn biệt thự vừa được dán lên cổng chính, bà mẹ chồng đã sụp đổ hoàn toàn trước các vị cổ đông sáng lập."'
    ),
    # huyen_nghi
    (
        r'''"hook":\s*orig\.get\("hook",\s*"'Sự thật chỉ có một[^"]+"\),''',
        '"hook": orig.get("hook", "Mũi dao vừa cậy bật góc viên gạch men số mười ba, bức di thư dính máu khô đã rơi tuột xuống lòng bàn tay tôi."),'
    ),
    # kinh_di
    (
        r'''"hook":\s*orig\.get\("hook",\s*"'Quy tắc thứ nhất khi thuê căn biệt thự[^"]+"\),''',
        '"hook": orig.get("hook", "Tiếng cào móng tay dưới gầm chiếc giường gỗ ép vừa dừng lại, mùi bùn ao tanh nồng đã xộc thẳng vào cánh mũi tôi!"),'
    ),
    # nguoc_tam
    (
        r'''"hook":\s*orig\.get\("hook",\s*"'Tôi đã dùng năm năm thanh xuân[^"]+"\),''',
        '"hook": orig.get("hook", "Tờ giấy xác nhận ung thư vừa rơi xuống bàn ăn, người chồng mười năm vẫn thong thả gắp miếng cá hồi cho cô thư ký riêng."),'
    ),
    # hao_mon
    (
        r'''"hook":\s*orig\.get\("hook",\s*"'Ký vào đây! Tôi cho cô 100 tỷ[^"]+"\),''',
        '"hook": orig.get("hook", "Mũi bút máy vừa chạm vào bản hợp đồng một trăm tỷ, vết son đỏ mận trên cổ tay áo anh ta đã tố cáo tất cả."),'
    ),
    # cuu_roi
    (
        r'''"hook":\s*orig\.get\("hook",\s*"'Nếu cô bước qua cánh cửa này[^"]+"\),''',
        '"hook": orig.get("hook", "Chiếc ô đen vừa che nghiêng qua vạt áo ướt đẫm của tôi giữa ngã tư đường, bức thư tuyệt mệnh trong túi áo tôi đã bị ai đó rút đi."),'
    ),
    # sa_dieu hook variable
    (
        r'''hook\s*=\s*"'Tôi nắm chặt vạt áo Tạ Duệ[^"]+"''',
        'hook = "Tập hồ sơ ba mươi tỷ bị sếp tổng ném đánh xoạch xuống bàn họp, nhưng trong đầu anh ta đang gào thét vì đói lử lả và quên mang giấy vệ sinh."'
    ),
    # cung_dau hook variable
    (
        r'''hook\s*=\s*"'Hoàng thượng, thần thiếp xin tự phế phượng vị[^"]+"''',
        'hook = "Chiếc trâm bạc của tôi vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng."'
    ),
    # vo_han hook variable
    (
        r'''hook\s*=\s*"'Nhiệt độ ngoài trời hạ xuống âm 65 độ C[^"]+"''',
        'hook = "Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang."'
    )
]

for pat, repl in replacements:
    text = re.sub(pat, repl, text)

# Dọn dẹp synthetic markers trong GENRE_ELEMENTS
text = text.replace("Thẩm Băng Tuyết thong thả nhấp ngụm rượu vang đỏ, khóe môi khẽ cong lên một nét cười lạnh thấu xương.", "Ngón tay tôi lật nhẹ góc bản hợp đồng ba mươi tỷ, để lộ dòng chữ ký giả mạo của người cha đã khuất.")
text = text.replace("Trong ván cờ sinh tử của giới tài phiệt, kẻ yếu đuối rơi nước mắt chỉ nhận lại sự giẫm đạp không thương tiếc.", "Tiếng bước chân gấp gáp của đoàn thanh tra thuế vang lên trên nền đá hoa cương sáng bóng.")
text = text.replace("Mười năm sống trong bùn lầy kiếp trước đã tôi luyện cho tôi một trái tim sắt đá, không còn chỗ cho lòng trắc ẩn mù quáng.", "Từng con số kiểm toán đối chiếu hiện rõ mồn một trên màn hình máy chiếu phòng họp.")
text = text.replace("Từng con số kiểm toán sắc lẹm như những nhát búa đóng chặt vào cỗ quan tài chôn vùi dã tâm của kẻ phản trắc.", "Mũi kéo inox bấm đứt sợi chỉ niêm phong với một tiếng tách dứt khoát.")

fpath.write_text(text, encoding="utf-8")
print("Updated core/narrative_synthesizer.py successfully!")
