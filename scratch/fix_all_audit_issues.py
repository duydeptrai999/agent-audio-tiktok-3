# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

c21_file = Path("core/stories/cycles_21_to_30_masterpieces.py")
text = c21_file.read_text(encoding="utf-8")

# Cycle 22 Part 3:
text = text.replace(
    "Cơ quan thanh tra môi trường lập tức phong tỏa toàn bộ khu đất phía Tây để phục vụ công tác điều tra vi phạm xử lý chất thải độc hại",
    "Cơ quan thanh tra môi trường lập tức phong tỏa toàn bộ khu đất phía Tây, phục vụ điều tra xử lý chất thải độc hại"
)

# Cycle 23 Part 2:
text = text.replace(
    "'Nạn nhân là y tá trưởng. Cô ấy nắm giữ chứng từ anh đánh tráo thuốc ung thư giả suốt ba năm qua!'",
    "'Nạn nhân là y tá trưởng. Cô ấy nắm giữ chứng từ anh tráo thuốc ung thư giả suốt ba năm!'"
)

# Cycle 23 Part 3:
text = text.replace(
    "Lời cảnh báo lạnh gáy được đề nghị tại phiên tòa sơ thẩm đối với kẻ đội lốt thiên thần áo trắng để trục lợi trên sinh mạng người bệnh nghèo",
    "Lời cảnh báo lạnh gáy được đề nghị tại tòa sơ thẩm đối với kẻ đội lốt thiên thần áo trắng, trục lợi trên người bệnh nghèo"
)

# Cycle 24 Part 1:
text = text.replace(
    "'Mẹ chu đáo quá. Nhưng bát yến này mẹ nên để dành cho cô cháu gái họ của mẹ thì hơn.'",
    "'Mẹ chu đáo quá! Bát yến này mẹ nên để dành cho cô cháu gái họ của mẹ!'"
)
text = text.replace(
    "'Thưa bà Lục. Giám đốc chi nhánh ngân hàng vừa thông báo lệnh phong tỏa toàn bộ tài khoản bảo lãnh một trăm tỷ của công ty bà!'",
    "'Thưa bà Lục! Giám đốc ngân hàng vừa thông báo phong tỏa tài khoản bảo lãnh một trăm tỷ của công ty bà!'"
)

# Cycle 24 Part 2:
text = text.replace(
    "'Nhà họ Lục? Mẹ quên rằng tám mươi phần trăm vốn điều lệ ban đầu là tài sản thừa kế của mẹ ruột tôi để lại sao?'",
    "'Nhà họ Lục? Tám mươi phần trăm vốn điều lệ là tài sản thừa kế của mẹ ruột tôi để lại!'"
)
text = text.replace(
    "'Chơi bời qua đường. Mà dám lén lút rút ba mươi tỷ mua cổ phần cho con riêng của cô ta sao?'",
    "'Chơi bời qua đường? Mà dám lén lút rút ba mươi tỷ mua cổ phần cho con riêng sao?'"
)

# Cycle 24 Part 3:
text = text.replace(
    "'Từ hôm nay. Tôi là Đoàn Bảo Ngọc của chính mình, không phải là con dâu ngoan ngoãn của bất kỳ ai!'",
    "'Từ hôm nay! Tôi là Đoàn Bảo Ngọc, không phải con dâu ngoan ngoãn của bất kỳ ai!'"
)
text = text.replace(
    "Toàn bộ hợp đồng bảo lãnh tín chấp giữa tôi và tập đoàn của nhà họ Lục chính thức bị hủy bỏ theo điều khoản vi phạm nghĩa vụ trung thực tài chính",
    "Toàn bộ hợp đồng bảo lãnh tín chấp giữa tôi và tập đoàn họ Lục chính thức bị hủy bỏ, chấm dứt mọi nghĩa vụ tài chính"
)
text = text.replace(
    "Bà Mai buộc phải bán tống bán tháo căn biệt thự cổ để thanh toán các khoản nợ đáo hạn ngân hàng trước nguy cơ phá sản",
    "Bà Mai buộc phải bán tống bán tháo căn biệt thự cổ, thanh toán các khoản nợ đáo hạn ngân hàng trước nguy cơ phá sản"
)

# Cycle 25 Part 1:
text = text.replace(
    "'Thưa Phó tổng. Toàn bộ ổ cứng máy chủ lưu trữ bản thiết kế ba mươi tầng ngầm đã bị kẻ gian tháo trộm lúc ba giờ sáng!'",
    "'Thưa Phó tổng! Ổ cứng máy chủ lưu trữ bản thiết kế ba mươi tầng ngầm đã bị tháo trộm lúc ba giờ sáng!'"
)

# Cycle 25 Part 2:
text = text.replace(
    "'Bản thiết kế này là công sức ba năm của viện nghiên cứu, không thể để lọt vào tay đối thủ cạnh tranh!'",
    "'Bản thiết kế là công sức ba năm của viện. Không thể để lọt vào tay đối thủ cạnh tranh!'"
)
text = text.replace(
    "'Lâm Diệp. Cậu nghĩ chiếc thẻ nhớ mã hóa này có thể qua mắt được cổng kiểm tra an ninh sân bay sao?'",
    "'Lâm Diệp! Cậu nghĩ chiếc thẻ nhớ mã hóa này có thể qua mắt được an ninh sân bay sao?'"
)

# Cycle 25 Part 3:
text = text.replace(
    "'Các người không thể bắt tôi. Tôi có quyền miễn trừ ngoại giao theo thỏa thuận hợp tác quốc tế!'",
    "'Các người không thể bắt tôi! Tôi có quyền miễn trừ ngoại giao theo thỏa thuận quốc tế!'"
)
text = text.replace(
    "'Quyền miễn trừ đã bị tước bỏ từ khoảnh khắc ông kích hoạt mã độc đánh cắp bí mật quốc gia!'",
    "'Quyền miễn trừ bị tước bỏ từ khoảnh khắc ông kích hoạt mã độc đánh cắp bí mật quốc gia!'"
)

# Cycle 26 Part 1:
text = text.replace(
    "'Thuyền trưởng. Siêu bão cấp mười sáu đang áp sát, mạn tàu số ba xuất hiện vết nứt dài bốn mét!'",
    "'Thuyền trưởng! Siêu bão cấp mười sáu đang áp sát, mạn tàu số ba xuất hiện vết nứt dài bốn mét!'"
)

# Cycle 26 Part 2:
text = text.replace(
    "'Quốc Huy. Cậu điên rồi sao? Cắt xích container mạn phải sẽ làm tàu mất cân bằng lật úp ngay lập tức!'",
    "'Quốc Huy! Cậu điên rồi sao? Cắt xích mạn phải sẽ làm tàu mất cân bằng lật úp ngay!'"
)

# Cycle 27 Part 1:
text = text.replace(
    "'Diệp thái y. Bát canh hạt sen này là tấm lòng của bản cung, ngươi dám nghi ngờ có độc sao?'",
    "'Diệp thái y! Bát canh này là tấm lòng của bản cung, ngươi dám nghi ngờ có độc sao?'"
)
text = text.replace(
    "'Vi thần không dám. Nhưng bột chu sa kết tủa dưới đáy chén là vật cấm ngự dược của tiên đế!'",
    "'Vi thần không dám! Bột chu sa kết tủa dưới đáy chén là vật cấm ngự dược của tiên đế!'"
)

# Cycle 27 Part 2:
text = text.replace(
    "'Thục phi nương nương. Ngũ thạch tán ngâm trong rượu hoa cúc sẽ phát tác sau đúng một tuần hương!'",
    "'Thục phi nương nương! Ngũ thạch tán ngâm rượu hoa cúc sẽ phát tác sau đúng một tuần hương!'"
)
text = text.replace(
    "'Nhan Ngọc Dao. Ngươi nghĩ hoàng thượng sẽ tin lời một thái y hèn mọn như ngươi sao?'",
    "'Nhan Ngọc Dao! Ngươi nghĩ hoàng thượng sẽ tin lời một ngự y hèn mọn như ngươi sao?'"
)

# Cycle 27 Part 3:
text = text.replace(
    "'Bản cung là mẫu thân của tam hoàng tử. Kẻ nào dám bước vào tẩm điện lục soát ngự dược?'",
    "'Bản cung là mẫu thân tam hoàng tử! Kẻ nào dám bước vào tẩm điện lục soát ngự dược?'"
)
text = text.replace(
    "Chiếu chỉ phế truất Thục phi cùng toàn bộ gia tộc họ Nhan lập tức được ban bố khắp lục cung trước sự bàng hoàng của bá quan",
    "Chiếu chỉ phế truất Thục phi cùng gia tộc họ Nhan lập tức được ban bố khắp lục cung, tống giam toàn bộ vây cánh"
)

# Cycle 28 Part 1:
text = text.replace(
    "'Thưa thầy. Đây không phải tài liệu quay cóp, mà là toàn bộ video ghi lại cảnh hội trưởng Trịnh tuồn đề thi ra ngoài lúc hai giờ sáng!'",
    "'Thưa thầy! Đây là toàn bộ video ghi lại cảnh hội trưởng Trịnh tuồn đề thi ra ngoài lúc hai giờ sáng!'"
)

# Cycle 28 Part 3:
text = text.replace(
    "Kết quả điều tra của Bộ Giáo dục xác nhận đường dây tuồn đề thi trị giá hàng tỷ đồng do gia đình Trịnh Phong cầm đầu chính thức bị triệt phá",
    "Kết quả điều tra xác nhận đường dây tuồn đề thi trị giá hàng tỷ đồng do gia đình Trịnh Phong cầm đầu, chính thức bị triệt phá"
)

# Cycle 29 Part 1:
text = text.replace(
    "'Kỹ sư Minh. Mở van khoang thực phẩm ra, nếu không tôi cắt đứt toàn bộ đường dẫn dưỡng khí!'",
    "'Kỹ sư Minh! Mở van khoang thực phẩm ra, nếu không tôi cắt đứt toàn bộ đường dẫn dưỡng khí!'"
)
text = text.replace(
    "'Tiếc cho anh. Kho hạt giống đã được niêm phong vào khoang thoát hiểm tự hành mười lăm phút trước!'",
    "'Tiếc cho anh! Kho hạt giống đã niêm phong vào khoang thoát hiểm tự hành mười lăm phút trước!'"
)

# Cycle 29 Part 2:
text = text.replace(
    "'Các người đã lén cắt đường điện của buồng ươm mầm, làm chết rét hàng vạn cây giống cứu sinh của nhân loại!'",
    "'Các người đã lén cắt đường điện buồng ươm, làm chết rét hàng vạn cây giống cứu sinh của nhân loại!'"
)
text = text.replace(
    "'Tôi không giết các người. Tôi chỉ để các người tự nếm trải cái lạnh âm năm mươi độ của khoang ngoài!'",
    "'Tôi không giết các người! Hãy tự nếm trải cái lạnh âm năm mươi độ của khoang ngoài!'"
)

# Cycle 29 Part 3:
text = text.replace(
    "Tiêu Trạch và đám phản trắc bị tước vũ khí và áp giải về tòa án sinh tồn ngầm để xét xử về tội phá hoại nguồn sống nhân loại",
    "Tiêu Trạch và đám phản trắc bị tước vũ khí, áp giải về tòa án sinh tồn ngầm để xét xử về tội phá hoại nguồn sống nhân loại"
)

# Cycle 30 Part 1:
text = text.replace(
    "'Cha mày vừa qua đời hôm qua, năm mươi mốt phần trăm cổ phần này thuộc quyền giám hộ của chú mày!'",
    "'Cha mày vừa qua đời hôm qua! Cổ phần này thuộc quyền giám hộ của chú mày!'"
)
text = text.replace(
    "'Luật sư Weber. Xin mời ông đọc nội dung bản di chúc tín thác được niêm phong mười lăm năm trước!'",
    "'Luật sư Weber! Mời ông đọc bản di chúc tín thác được niêm phong mười lăm năm trước!'"
)

# Cycle 30 Part 2:
text = text.replace(
    "'Ông Lục Minh. Câu nói vừa rồi của ông đã được hệ thống ghi âm tự động lưu lại làm chứng cứ tiêu hủy tài liệu chứng khoán!'",
    "'Ông Lục Minh! Lời nói của ông đã được hệ thống ghi âm tự động lưu lại làm chứng cứ tiêu hủy tài liệu!'"
)
text = text.replace(
    "Toàn bộ năm mươi mốt phần trăm cổ phần biểu quyết của tập đoàn tự động chuyển giao vào tài khoản tín thác đứng tên duy nhất của tôi",
    "Toàn bộ cổ phần biểu quyết của tập đoàn tự động chuyển giao vào tài khoản tín thác, đứng tên duy nhất của tôi"
)

# Cycle 30 Part 3:
text = text.replace(
    "Lục Minh cùng toàn bộ vây cánh trong ban giám đốc bị đình chỉ công tác để phục vụ công tác thanh tra tài chính toàn diện",
    "Lục Minh cùng toàn bộ vây cánh trong ban giám đốc bị đình chỉ công tác, phục vụ công tác thanh tra tài chính toàn diện"
)
text = text.replace(
    "Những khoản tiền biển thủ hơn hai trăm tỷ trong các dự án đầu tư ảo bị cơ quan chức năng phong tỏa và thu hồi về ngân khố tập đoàn",
    "Những khoản tiền biển thủ hơn hai trăm tỷ trong các dự án đầu tư ảo, bị cơ quan chức năng phong tỏa và thu hồi về ngân khố"
)

c21_file.write_text(text, encoding="utf-8")
print("Successfully updated core/stories/cycles_21_to_30_masterpieces.py")

# Update Cycle 36 Part 1 in core/stories/cycles_31_to_40_masterpieces.py
c31_file = Path("core/stories/cycles_31_to_40_masterpieces.py")
text31 = c31_file.read_text(encoding="utf-8")

old_c36_p1 = """    p1 = \"\"\"Bảy mươi triệu đô la tiền chuộc vừa được xác nhận chuyển khoản vào tài khoản ủy thác thì chiếc vali bọc thép chứa con tin đã bị cài kíp nổ áp suất ngược, kim đồng hồ đếm ngược chỉ còn bốn phút mười lăm giây.

Không gian bên trong căn phòng họp lãnh sự quán ngột ngạt như buồng kín không có dưỡng khí.
Phó tùy viên Triệu Bân đẩy tập hồ sơ miễn trừ tư pháp qua mép bàn tròn bằng kính cường lực:
'Tần Dịch... Ký giải tỏa tài khoản ngay, Viktor sẽ cắt ngòi nổ sau khi bay!'.

Tôi tựa lưng vào ghế da, chiếc bút máy nắp vàng trên tay xoay tròn nhịp nhàng theo chiều kim đồng hồ.
Ống mực bên trong chiếc bút là hợp chất mực nhạy nhiệt gốc axit amin, sẽ bay hơi không để lại dấu vết sau ba mươi phút.

Tôi nhìn thẳng vào mắt Viktor qua màn hình đàm phán vệ tinh mã hóa:
'Thả cháu bé ra cửa khẩu số ba trước, tôi mới ký điều khoản giải ngân cuối cùng.'.

Tên trùm khủng bố gõ báng súng ngắn xuống bàn phát ra tiếng cắc khô khốc:
'Mày có hai phút để ký... Nếu không tòa nhà này biến thành tro!'.

Tôi thong thả mở nắp bút máy, đặt ngòi bút sắc lẹm xuống dòng chữ ký của ngân hàng trung ương!\"\"\""""

new_c36_p1 = """    p1 = \"\"\"Bảy mươi triệu đô la tiền chuộc vừa được xác nhận chuyển khoản vào tài khoản ủy thác thì chiếc vali bọc thép chứa con tin đã bị cài kíp nổ áp suất ngược, kim đồng hồ đếm ngược chỉ còn bốn phút mười lăm giây.

Không gian bên trong căn phòng họp lãnh sự quán ngột ngạt như buồng kín không có dưỡng khí.
Phó tùy viên Triệu Bân đẩy tập hồ sơ miễn trừ tư pháp qua mép bàn tròn bằng kính cường lực.
'Tần Dịch... Ký giải tỏa tài khoản ngay, Viktor sẽ cắt ngòi nổ sau khi bay!'.

Tôi tựa lưng vào ghế da. Chiếc bút máy nắp vàng trên tay xoay tròn nhịp nhàng theo chiều kim đồng hồ.
Ống mực bên trong chiếc bút là hợp chất mực nhạy nhiệt gốc axit amin, sẽ bay hơi không để lại dấu vết sau ba mươi phút.

Tôi nhìn thẳng vào mắt Viktor qua màn hình đàm phán vệ tinh mã hóa.
'Thả cháu bé ra cửa khẩu số ba trước, tôi mới ký điều khoản giải ngân cuối cùng.'.

Tên trùm khủng bố gõ báng súng ngắn xuống bàn phát ra tiếng cắc khô khốc.
'Mày có hai phút để ký... Nếu không tòa nhà này biến thành tro!'.

Tôi thong thả mở nắp bút máy, đặt ngòi bút sắc lẹm xuống dòng chữ ký của ngân hàng trung ương!\"\"\""""

if old_c36_p1 in text31:
    text31 = text31.replace(old_c36_p1, new_c36_p1)
    c31_file.write_text(text31, encoding="utf-8")
    print("Successfully updated Cycle 36 Part 1 in core/stories/cycles_31_to_40_masterpieces.py")
else:
    print("Warning: old_c36_p1 not found in c31")
