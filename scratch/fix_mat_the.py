# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/stories/mat_the_sinh_ton_masterpiece.py")
text = fpath.read_text(encoding="utf-8")

old_p1_start = """    part1_full = \"\"\"Kim nhiệt kế ngoài trời gắn trên khung cửa sổ phòng ngủ của Lâm Tiêu Lam đang chỉ đúng sáu mươi độ C!

Cát bụi phóng xạ đỏ rực rào rào dội xuống mặt kính như một cơn mưa đạn. Kiếp trước, chính người chú ruột Lâm Quốc Hùng và ả em họ Lâm Thiến Thiến đã nhẫn tâm đẩy cô ra khỏi cửa hầm vào giữa cơn bão cát thiêu đốt này chỉ để cướp hai chai nước khoáng cuối cùng!

Lâm Tiêu Lam bàng hoàng bật dậy khỏi giường, lồng ngực phập phồng thở dốc. Chiếc đồng hồ điện tử đầu giường nhấp nháy dòng số xanh biếc: Ngày hai mươi hai tháng chín! Đúng ba mươi ngày trước giờ tận thế!

Nhiệt độ phòng lúc này vẫn đang là hai mươi lăm độ C mát mẻ từ chiếc điều hòa êm ái.

Mình... mình chưa chết? Mình đã thực sự trọng sinh rồi sao?"""

new_p1_start = """    part1_full = \"\"\"Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang:
'Chị Lam ơi! Thằng bé sốt bốn mươi độ rồi, cho em xin mẩu nến và gói mì tôm thôi!'.

Tôi không mở cửa. Tôi tựa lưng vào vách thép dày mười lăm phân, ngón tay đặt sẵn trên van xả khí cay áp suất cao.

Qua lỗ quan sát hồng ngoại, chiếc bọc chăn bông trên tay ả em họ khẽ xốc xếch, để lộ một góc đầu búp bê cao su hỏng một mắt. 

Và ngay phía sau lưng ả, hai gã đàn ông lực lưỡng đang nép sát góc tường, tay lăm lăm hai chiếc xà beng kim loại sáng loáng.

Tôi bấm micro liên lạc gắn ngoài cửa, giọng lạnh tanh:
'Lâm Thiến Thiến, búp bê cao su mà cũng biết sốt bốn mươi độ sao? Đếm ngược ba giây... lùi lại khỏi bậc thềm, hoặc toàn bộ khí cay sẽ xịt thẳng vào mặt hai người bạn sau lưng cô!'.

Ba mươi ngày trước giờ tận thế bão cát, Lâm Tiêu Lam đã dùng toàn bộ một trăm tỷ tiền mặt để gia cố căn hầm ngầm ba tầng kiên cố này."""

if old_p1_start in text:
    text = text.replace(old_p1_start, new_p1_start)
    fpath.write_text(text, encoding="utf-8")
    print("Fixed mat_the_sinh_ton_masterpiece.py successfully!")
else:
    print("Could not find old_p1_start in mat_the_sinh_ton_masterpiece.py")
