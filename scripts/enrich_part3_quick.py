# -*- coding: utf-8 -*-
from pathlib import Path

target_file = Path("core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py")
text = target_file.read_text(encoding="utf-8")

extra_p3 = """
Trước khi rời đi, bà mẹ chồng còn nán lại bên chiếc tủ lạnh của tôi, định với tay ôm mấy hộp yến sào và sâm bổ dưỡng mà bố mẹ đẻ mua biếu tôi hồi đầu tuần. Tôi bước tới, lạnh lùng chặn tay bà ta lại: 

"Bác dừng tay lại! Từng hộp yến sào, từng giỏ quà bổ dưỡng này là do bố mẹ ruột của cháu mua cho cháu tẩm bổ sau sinh, hóa đơn mua hàng ghi rõ tên cháu. Trong căn nhà này, ngoài mấy bộ quần áo cũ của anh Thắng, không có bất kỳ thứ gì thuộc về người nhà bác. Bác đừng để cháu phải gọi bảo vệ lên lập biên bản về hành vi chiếm đoạt tài sản!".

Bà Mai giật nảy mình rụt tay lại, mặt đỏ bừng vì xấu hổ và tức tối. Đúng lúc đó, điện thoại của Thắng rung lên bần bật. Đó là hàng loạt tin nhắn từ nhóm Zalo họ hàng dưới quê. Hóa ra vợ chồng Dũng sau khi bị đuổi xuống sảnh chung cư đã lập tức nhắn tin kể khổ, bêu rếu rằng anh Thắng giàu sang bạc bẽo, để vợ đuổi em họ ra đường. Những người họ hàng từng tâng bốc Thắng ban sáng giờ đây quay sang mắng nhiếc anh ta là kẻ bất tài, sợ vợ, làm mất mặt dòng họ. 

Thắng nhìn vào màn hình điện thoại, cay đắng nhận ra cái danh hão mà anh ta cố công xây dựng bấy lâu nay đã hoàn toàn sụp đổ chỉ sau một buổi trưa. Người đàn ông ấy ôm đầu ngồi sụp xuống bậc thềm, bất lực trong đống đổ nát do chính sự nhu nhược của mình tạo ra.
"""

marker = '"Cơ hội tôi đã cho anh suốt ba năm qua rồi. Ngày hôm nay, sự nhẫn nhịn của tôi đã cạn kiệt. Thu dọn đồ đạc đi, chúng ta gặp nhau ở tòa án!".'

text_norm = text.replace("\r\n", "\n")
marker_norm = marker.replace("\r\n", "\n")
extra_norm = extra_p3.replace("\r\n", "\n")

if marker_norm in text_norm:
    text_norm = text_norm.replace(marker_norm, marker_norm + "\n" + extra_norm)
    target_file.write_text(text_norm, encoding="utf-8")
    print("Enriched Part 3 successfully!")
else:
    print("Marker not found in text!")
