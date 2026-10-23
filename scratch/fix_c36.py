# -*- coding: utf-8 -*-
from pathlib import Path

c31_file = Path("core/stories/cycles_31_to_40_masterpieces.py")
text31 = c31_file.read_text(encoding="utf-8")

text31 = text31.replace(
    "Phó tùy viên Triệu Bân đẩy tập hồ sơ miễn trừ tư pháp qua mép bàn tròn bằng kính cường lực:\n'Tần Dịch... Ký giải tỏa tài khoản ngay, Viktor sẽ cắt ngòi nổ sau khi bay!'.",
    "Phó tùy viên Triệu Bân đẩy tập hồ sơ miễn trừ tư pháp qua mép bàn tròn bằng kính cường lực.\n'Tần Dịch... Ký giải tỏa tài khoản ngay, Viktor sẽ cắt ngòi nổ sau khi bay!'."
)

text31 = text31.replace(
    "Tôi tựa lưng vào ghế da, chiếc bút máy nẹp vàng trên tay xoay tròn nhịp nhàng theo chiều kim đồng hồ.",
    "Tôi tựa lưng vào ghế da. Chiếc bút máy nẹp vàng trên tay xoay tròn nhịp nhàng theo chiều kim đồng hồ."
)

text31 = text31.replace(
    "Tôi nhìn thẳng vào mắt Viktor qua màn hình đàm phán vệ tinh mã hóa:\n'Thả cháu bé ra cửa khẩu số ba trước, tôi mới ký điều khoản giải ngân cuối cùng.'.",
    "Tôi nhìn thẳng vào mắt Viktor qua màn hình đàm phán vệ tinh mã hóa.\n'Thả cháu bé ra cửa khẩu số ba trước, tôi mới ký điều khoản giải ngân cuối cùng.'."
)

text31 = text31.replace(
    "Tên trùm khủng bố gõ báng súng ngắn xuống bàn phát ra tiếng cộc khô khốc:\n'Mày có hai phút để ký... Nếu không tòa nhà này biến thành tro!'.",
    "Tên trùm khủng bố gõ báng súng ngắn xuống bàn phát ra tiếng cộc khô khốc.\n'Mày có hai phút để ký... Nếu không tòa nhà này biến thành tro!'."
)

c31_file.write_text(text31, encoding="utf-8")
print("Updated Cycle 36 Part 1 in core/stories/cycles_31_to_40_masterpieces.py")
