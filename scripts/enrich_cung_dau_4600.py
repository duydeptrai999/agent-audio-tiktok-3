# -*- coding: utf-8 -*-
"""
scripts/enrich_cung_dau_4600.py
Bổ sung chi tiết đấu trí, y thuật pháp y hoàng cung và chiến thuật quân sự vào cung_dau_nu_quyen_masterpiece.py
để đạt độ dài hoàn hảo >= 4,600 từ (~27 phút audio).
"""
from pathlib import Path

file_path = Path("core/stories/cung_dau_nu_quyen_masterpiece.py")
content = file_path.read_text(encoding="utf-8")

# Thêm chi tiết vào Part 1
part1_expansion = """
Tôi chỉ tay vào góc thềm điện, nơi một cung nữ thân cận của Thục phi đang lén lút lau mồ hôi trán: 'Ngươi tên là Xuân Đào, đúng không? Hôm qua giờ Thân, ai là người lén lút gặp gỡ tiểu thái giám phòng ngự mộc ở ngự hoa viên? Mảnh vụn gỗ đào còn vương trên mép gấu váy của ngươi, mùi chu sa thượng phẩm vẫn chưa tan hết trên đầu ngón tay. Ngươi có dám để viện thẩm tra ngự tiền kiểm tra bột màu dưới móng tay ngươi không?'.

Cung nữ Xuân Đào nghe vậy sợ hãi run rẩy như cầy sấy, ngã quỵ xuống đất dập đầu lia lịa. Liễu Y Nhiên biến sắc vội vàng quát lớn: 'Con tiện tì này, ngươi dám tư thông với kẻ ngoài để hại ta sao? Bệ hạ, xin người lập tức ban chết cho ả!'.

Tôi cười nhạt: 'Thục phi vội vàng giết người diệt khẩu như vậy, chẳng lẽ sợ ả khai ra chủ mưu thực sự đằng sau?'.
"""

if "Liễu Y Nhiên nghe vậy giật thót mình" in content:
    content = content.replace("Liễu Y Nhiên nghe vậy giật thót mình", part1_expansion + "\nLiễu Y Nhiên nghe vậy giật thót mình")

# Thêm chi tiết vào Part 2
part2_expansion = """
Tôi lật giở từng trang tài liệu, giọng nói vang vọng khắp điện Kim Loan: 'Không chỉ có bạc trắng, mà ngay cả ba vạn bao lương thảo của quân đội phương bắc cũng bị hoán đổi thành thóc mốc trộn cát vàng. Trên mỗi bao tải đều có ấn triện của phủ Tả tướng và con dấu xuất kho của Lục bộ. Các ngài ngồi trong kinh thành ăn sơn hào hải vị, mặc gấm vóc lụa là, có từng nghĩ đến cảnh binh sĩ nơi biên cương ăn cháo loãng cầm hơi, chịu rét mướt để bảo vệ giang sơn cho các ngài hưởng lạc hay không?'.

Từng đại thần trong triều cúi gầm mặt, không một ai dám ho he nửa lời. Ánh mắt Tiêu Triệt bốc hỏa, hắn đập mạnh tay xuống ngai vàng rồng làm nứt cả thành ngai: 'Khốn kiếp! Quân lương tiền tuyến mà cũng dám bớt xén! Người đâu, lập tức phong tỏa phủ Tả tướng, cách chức điều tra toàn bộ quan lại liên quan!'.
"""

if "Cả triều đình chấn động xôn xao!" in content:
    content = content.replace("Cả triều đình chấn động xôn xao!", part2_expansion + "\nCả triều đình chấn động xôn xao!")

# Thêm chi tiết vào Part 3
part3_expansion = """
Trong màn sương tuyết dày đặc, tôi giương thanh cung sắt sáu mươi cân, mũi tên đồng xé toạc không khí cắm phập vào yết hầu tên phó tướng chỉ huy cánh tả của địch. Kỵ binh Đại Tề thừa thắng xông lên, tiếng trống trận rền vang như sấm sét đánh sập ý chí kháng cự của quân Hãn tộc.

Tôi không đuổi cùng giết tận những hàng binh đã buông vũ khí. Tôi hạ lệnh mở kho thóc của thành trì bị chiếm đóng, chia phát lương thực cho dân chúng nghèo đói và băng bó vết thương cho thương binh. Nghĩa cử nhân đạo và kỷ luật thép của quân Đại Tề khiến bách tính phương bắc cảm động rơi lệ, đồng lòng tiếp tế lương thảo và dẫn đường cho quân ta truy kích tàn quân giặc đến tận chân núi Thiên Sơn.
"""

if "Tôi không dùng lối đánh biển người trực diện liều mạng." in content:
    content = content.replace("Tôi không dùng lối đánh biển người trực diện liều mạng.", part3_expansion + "\nTôi không dùng lối đánh biển người trực diện liều mạng.")

file_path.write_text(content, encoding="utf-8")
print("Enriched cung_dau_nu_quyen_masterpiece.py successfully!")
