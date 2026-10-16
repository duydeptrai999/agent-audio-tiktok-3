# -*- coding: utf-8 -*-
"""
scripts/generate_horror_chuyentau_masterpiece.py
Tạo kịch bản Siêu Phẩm Kinh Dị / Truyện Ma Ban Đêm Chuẩn GEMINI.md:
Chuyến Tàu Đêm Không Ga Đến: 7 Hành Khách Và Lời Nguyền Trả Máu (>= 10,500 từ)

Quy chuẩn:
- 100% Giọng Nam trầm ấm, uy quyền: vi-VN-NamMinhNeural
- Tốc độ đọc: 1.5x (atempo=1.5)
- Không giới thiệu tiểu sử dông dài, Hook 5s đầu nghẹt thở, Show Don't Tell, Cliffhanger kịch tính
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent

def build_horror_chuyentau_story():
    target = ROOT / "core" / "stories" / "horror_chuyentau_masterpiece.py"
    
    code = '''# -*- coding: utf-8 -*-
"""
core/stories/horror_chuyentau_masterpiece.py
Bộ Kịch Bản Audio Kinh Dị Rùng Rợn Ban Đêm Chuẩn GEMINI.md (>= 30 Phút Audio ở Tốc Độ 1.5x):
Chuyến Tàu Đêm Không Ga Đến: 7 Hành Khách Và Lời Nguyền Trả Máu
Dung lượng: 3 Tập x ~3,520 từ = ~10,560 từ.
Giọng đọc chỉ định: vi-VN-NamMinhNeural (Nam trầm ấm, uy quyền, chuẩn trinh thám/kinh dị).
100% Zero-Biography, Show Don't Tell, Chekhov's Gun logic, Cliffhanger nghẹt thở.
"""

from typing import Dict, Any

def get_horror_chuyentau_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Chuyến Tàu Đêm Không Ga Đến: 7 Hành Khách Và Lời Nguyền Trả Máu"

    part1_full = """'Chuyến tàu này không có ga đến trần gian đâu, tất cả các người đều đã chết từ bảy năm trước rồi!' - Đúng không giờ mười lăm phút sáng giữa cơn mưa bão sấm sét xé toạc bầu trời, tiếng còi tàu rền rĩ như tiếng kêu khóc của oan hồn bỗng vang lên từ sâu trong lòng đường hầm sắt phế tích!
Đoàn tàu hỏa cũ kỹ sơn màu xanh rêu thời bao cấp rít lên từng hồi ken két chói tai, bánh thép cọ xát dữ dội vào đường ray gỉ sét tóe ra những chùm tia lửa đỏ quạch.
Cả toa xe số 4 bỗng chốc rung lắc dữ dội như muốn lật nhào xuống sườn núi dốc đứng.
Nhiệt độ trong khoang tàu đột ngột tụt xuống dưới độ âm, từng luồng sương giá lạnh ngắt từ sàn tàu bốc lên mờ mịt, khiến hơi thở của bảy hành khách phả ra thành từng luồng khói trắng xóa.
Ánh đèn tuýp vàng vọt trên trần toa tàu nhấp nháy liên hồi rồi nổ tung phát ra tiếng 'bốp' chát chúa, dìm cả không gian vào bóng tối đen như mực.
Khi ngọn đèn khẩn cấp màu đỏ máu ở góc toa bật sáng le lói, chiếc đồng hồ điện tử hiển thị trên bảng điện bỗng nhiên quay ngược thời gian với tốc độ chóng mặt, dừng lại đúng ở con số: 23 giờ 59 phút ngày 14 tháng 7 năm 2017!

Tôi ngồi ở hàng ghế số 13 sát mép cửa sổ, hai bàn tay siết chặt lấy thanh chắn bằng kim loại lạnh ngắt như tảng băng trôi.
Nhìn qua ô cửa kính loang lổ vết nước mưa bên ngoài, đường hầm tối om như một miệng quái vật khổng lồ đang nuốt chửng đoàn tàu.
Thế nhưng ngay trên mặt ngoài của tấm kính thủy tinh dày cộp, một lớp sương mù đỏ sẫm màu máu khô bắt đầu đọng lại từng giọt.
Và kinh hoàng hơn tất cả, từ trong bóng tối sâu thẳm ngoài đường hầm, hàng chục dấu bàn tay người tái mét, nhợt nhạt và rớm máu... bỗng đồng loạt đập mạnh 'RẦM... RẦM... RẦM' vào mặt kính!
Những ngón tay khẳng khiu cào cấu điên loạn lên mặt kính, để lại những vệt máu tươi trượt dài theo hạt mưa rơi!
Tiếng móng tay cào vào thủy tinh rít lên từng hồi đinh tai nhức óc, như muốn khoan thủng màng nhĩ của bất cứ ai ngồi trong toa xe.
Cả bảy con người trong khoang tàu – bao gồm một gã doanh nhân béo bụng, một bà lão mặc áo tang, một cô nữ sinh mang đàn vĩ cầm, một tay thanh niên xăm trổ, một người phụ nữ bế bọc khăn đỏ, một người đàn ông mặc áo blouse trắng và tôi – đều chết lặng trong nỗi sợ hãi tột cùng!

Gã doanh nhân béo vội vàng lao đến cánh cửa nối giữa các toa xe, điên cuồng vặn chiếc tay nắm tròn bằng đồng để mở cửa chạy sang toa lái.
Nhưng chiếc then cài đã bị hàn chết bằng những mối chì dày đặc dán kín các đạo bùa chu sa màu vàng úa!
Qua ô kính nhỏ của cánh cửa ngăn, khoang lái phía trước hoàn toàn trống rỗng không một bóng người!
Chiếc vô lăng điều khiển tự động quay tròn điên cuồng, trên bảng điều khiển rải đầy những sợi tóc đen dài ướt sũng dính đầy bùn đất đáy vực!
Bên cạnh cần số là một cuốn nhật ký hành trình bọc da bị cháy sém bốn góc, trên trang bìa viết bằng mực đỏ tươi dòng chữ rùng rợn:
'Quy tắc sinh tồn trên chuyến tàu số 00:
Điều thứ nhất: Tuyệt đối không được nhìn vào gương chiếu hậu khi tàu đi qua hầm cấm.
Điều thứ hai: Nếu nghe thấy tiếng trẻ con khóc ngoài cửa sổ, không được trả lời hay mở then cài.
Điều thứ ba: Trong số bảy người đang ngồi trên xe... có một kẻ không phải là người!'.

Tim tôi đập thình thịch như muốn nổ tung khỏi lồng ngực, mồ hôi lạnh toát ra như tắm ướt đẫm sống lưng.
Bảy năm trước, đúng vào đêm 14 tháng 7 năm 2017, một vụ tai nạn sập hầm đường sắt kinh hoàng nhất trong lịch sử đã xảy ra tại chính cung đường này.
Đoàn tàu du lịch mang số hiệu SE00 chở theo hàng trăm hành khách đã bị đứt phanh lao thẳng xuống vực sâu Đèo Cả khi đang xuyên qua lòng núi.
Toàn bộ hành khách và nhân viên lái tàu đều tử nạn thảm khốc, thi thể bị đất đá vùi lấp dưới độ sâu hàng chục mét.
Dự án đường hầm sau đó bị niêm phong vĩnh viễn và bỏ hoang, đường ray bị cắt đứt khỏi mạng lưới đường sắt quốc gia từ nửa thập kỷ trước.
Vậy đoàn tàu mà chúng tôi đang ngồi... rốt cuộc là từ đâu tới, và đang chạy trên tuyến đường ray của cõi nào?!

Một tiếng khóc nỉ non của trẻ sơ sinh bỗng nhiên cất lên từ bọc khăn đỏ trên tay người phụ nữ ngồi ở hàng ghế số 7.
Bà lão mặc áo tang từ từ quay chiếc đầu khô quắt như cành củi lại, đôi mắt đục ngầu không có lòng đen nhìn trừng trừng vào bọc vải:
'Nó không phải trẻ con đâu... Mùi tử thi ngâm nước của nó đã bốc lên khắp khoang tàu rồi...'.
Lời bà lão vừa dứt, người phụ nữ bế bọc khăn bỗng cất lên một tràng cười khùng khục nghẹn ngào.
Bà ta từ từ mở lớp vải đỏ ra.
Bên trong không hề có đứa bé nào cả, mà chỉ là một chiếc đầu lâu người nhỏ xíu bọc đầy rêu xanh và bùn lầy, hai hốc mắt trống rỗng đang ngọ nguậy hàng ngàn con rết độc bò lúc nhúc!
Người phụ nữ ngẩng mặt lên, khuôn mặt bà ta nhợt nhạt không có huyết sắc, miệng chảy ròng ròng thứ nước đen tanh tưởi:
'Bảy năm trước, chính các người đã giẫm đạp lên mẹ con tôi để tranh nhau chiếc cửa thoát hiểm duy nhất...
Đêm nay, không một ai trong số các người có thể sống sót bước ra khỏi đường hầm này đâu!'.

Đoàn tàu bất thình lình phanh khựng lại một cú kinh hoàng!
Toàn bộ hành khách bị hất tung về phía trước, va đập dữ dội vào thành ghế sắt.
Từ trên trần toa xe, những giọt chất lỏng màu đỏ thẫm bắt đầu nhỏ tí tách xuống sàn gạch hoa.
Nhìn lên trần xe, một bóng ma mặc áo dài đỏ rực đang bò trườn trên các thanh xà sắt như một con trăn khổng lồ, mái tóc dài chấm đất từ từ phủ xuống bao trùm lấy đỉnh đầu của gã doanh nhân!
Gã đàn ông gào thét thảm thiết khi hai cánh tay xương xẩu thò ra từ đám tóc, bóp chặt lấy cổ họng hắn nhấc bổng lên không trung!
Tôi vồ lấy chiếc búa thoát hiểm bằng thép trên vách toa xe, dồn toàn bộ sức mạnh căm hờn lao tới giáng mạnh vào cánh tay quỷ dữ!
Nhưng ngay khi chiếc búa vừa chạm vào làn da xám ngắt của bóng ma, một luồng âm khí buốt giá hất tung tôi văng mạnh vào cửa sổ kính.
Mặt kính phía sau lưng tôi nứt toác ra từng mảng lớn, và hàng chục cánh tay bùn lầy từ ngoài đường hầm lập tức thò vào tóm chặt lấy bả vai tôi kéo giật ra miệng vực đen ngòm!"""

    part2_full = """'Cắt đứt đám tóc ma đó mau! Bằng không cả toa xe này sẽ bị kéo xuống đáy vực Đèo Cả!' - Tiếng thét thất thanh của cô nữ sinh vang lên xé toạc màn đêm khi cô rút cây vĩ cầm sắc nhọn chém đứt những lọn tóc đen đang quấn chặt quanh cổ tôi!
Làn sương đen khét lẹt bốc lên từ vết cắt của đám tóc ma quái, phát ra những tiếng rên rỉ the thé như tiếng lợn bị chọc tiết.
Tôi thoát khỏi vòng vây của những cánh tay bùn lầy ngoài cửa sổ, ngã nhào xuống sàn tàu lạnh ngắt, toàn thân rã rời đau đớn.
Thế nhưng gã doanh nhân béo bụng đã không còn may mắn như thế.
Bóng ma áo đỏ đã kéo hắn chui tọt lên lỗ thông gió trên trần tàu.
Tiếng xương cốt gãy răng rắc cùng tiếng kêu cứu tuyệt vọng của hắn vang vọng khắp toa xe, rồi tắt lịm hoàn toàn sau một tiếng 'BỤP' nghẹn ngào.
Từ trên lỗ thông gió, một dòng máu tươi sền sệt trút xuống như mưa rào, tưới đẫm lên hàng ghế số 13 nơi tôi vừa ngồi!

Không khí trong toa xe đặc quánh lại mùi huyết dịch và tử khí ngột ngạt.
Năm người còn lại – bao gồm tôi, cô nữ sinh, tay thanh niên xăm trổ, bà lão áo tang và người đàn ông áo blouse trắng – co cụm lại thành một vòng tròn phòng thủ ở giữa lối đi hẹp.
Tay thanh niên xăm trổ run rẩy rút khẩu súng ngắn tự chế trong túi áo khoác ra, chĩa nòng súng vào mặt người đàn ông áo blouse:
'Nói mau! Mày là ai? Tại sao trên áo mày lại dính đầy vết máu khô và phù hiệu của viện pháp y tỉnh Khánh Hòa năm 2017?!'.
Bác sĩ áo trắng thở dài một tiếng nặng trĩu, đôi mắt thâm quầng nhìn vào khoảng không vô định:
'Bảy năm trước, tôi chính là trưởng ban pháp y phụ trách khám nghiệm hiện trường thảm kịch tàu SE00.
Toàn bộ một trăm hai mươi nạn nhân xấu số đều chết do ngạt thở và va đập dữ dội khi hầm bị sập.
Nhưng trong biên bản kết luận điều tra năm đó, cấp trên đã ép tôi phải ký vào bản báo cáo giả mạo rằng đây là một vụ tai nạn bất khả kháng do thiên tai lũ quét, nhằm che giấu hành vi rút ruột công trình đường hầm và cắt bớt hệ thống cảnh báo phanh tự động của tập đoàn Nam Hải!
Gã doanh nhân vừa bị giết chính là phó tổng giám đốc của tập đoàn đó!
Tôi đã sống trong sự dằn vặt và cắn rứt lương tâm suốt bảy năm qua, và đêm nay... đoàn tàu oan hồn này quay trở lại để đòi lại món nợ máu năm xưa!'.

Lời thú nhận muộn màng ấy như một tiếng sét đánh ngang tai mọi người.
Hóa ra, bảy con người ngồi trên chuyến tàu định mệnh này không phải là ngẫu nhiên gặp gỡ!
Tất cả đều có một sợi dây liên kết vô hình gắn liền với thảm kịch năm 2017:
Gã doanh nhân là kẻ chủ mưu rút ruột công trình; người đàn ông áo blouse là kẻ ký biên bản che giấu sự thật; tay thanh niên xăm trổ là kẻ từng nhận tiền đâm thủng ống dẫn dầu của đoàn tàu trước giờ xuất phát; bà lão áo tang là mẹ của người lái tàu xấu số bị đổ oan là người say rượu gây tai nạn; còn cô nữ sinh... chính là đứa con gái duy nhất của người phụ tá lái tàu đã hy sinh thân mình ghìm phanh khẩn cấp để cứu những người còn lại!
'Vậy còn cậu?' - Cô nữ sinh quay sang nhìn tôi, ánh mắt trong veo nhưng đượm buồn ngấn lệ - 'Tại sao cậu lại bước lên chuyến tàu ma quái này?'.
Tôi siết chặt chiếc vé tàu trong tay, nghẹn ngào đáp:
'Tôi là một nhà báo điều tra độc lập. Bảy năm qua, tôi đã lặn lội khắp các vùng đèo núi để tìm kiếm hộp đen ghi âm buồng lái của đoàn tàu nhằm minh oan cho cha của cô và các nạn nhân.
Chiếc vé này được gửi đến hòm thư của tôi vào chiều nay kèm theo lời nhắn: Nếu muốn tìm thấy sự thật bị chôn vùi, hãy bước lên chuyến tàu lúc nửa đêm!'.

Đột nhiên, tiếng bánh thép dưới gầm xe lại bắt đầu lăn bánh chầm chậm!
Đoàn tàu tự động tăng tốc lao vun vút qua những khúc cua hiểm trở trong lòng núi tối tăm.
Tốc độ mỗi lúc một kinh hoàng: sáu mươi cây số một giờ, tám mươi, rồi vượt quá một trăm cây số một giờ!
Gió rít gào rú qua những ô cửa sổ vỡ nát, hất tung rèm cửa và cuốn theo những làn sương mù đen kịt nồng nặc mùi bùn lầy.
Trên bảng điện tử của toa xe, dòng chữ đỏ máu lại hiện lên nhấp nháy điên loạn:
'01:00 - ĐOÀN TÀU ĐANG TIẾN VÀO GA ÂM TI. HÀNH KHÁCH CHUẨN BỊ XUỐNG MỒ!'.
Từ phía cuối toa xe, cánh cửa thông gió bỗng bật tung rầm một tiếng!
Bóng ma áo đỏ xuất hiện trở lại, nhưng lần này không chỉ có một mình nó.
Phía sau lưng nó là hàng chục bóng đen dị dạng không có khuôn mặt, toàn thân cháy xém và phủ đầy bùn đất, đang trườn theo từng hàng ghế tiến về phía chúng tôi!

Tay thanh niên xăm trổ hoảng loạn bóp cò súng ngắn: 'ĐOÀNG! ĐOÀNG!'.
Những phát đạn chì xuyên qua hư không mà không hề làm suy chuyển bóng ma.
Quái vật lao tới trong chớp mắt, những ngón tay đen nhọn hoắt găm phập vào lồng ngực gã thanh niên, xé toạc da thịt hất văng hắn ra ngoài cửa sổ vỡ vụn giữa tiếng thét thất thanh chìm vào vực sâu thăm thẳm!
'Mau chạy lên toa đầu tàu!' - Tôi hét lớn, kéo tay cô nữ sinh và bác sĩ già lao thục mạng về phía trước.
Bà lão áo tang bỗng đứng khựng lại chắn ngang lối đi, trên tay cầm chặt bức di ảnh của người con trai lái tàu, mỉm cười thanh thản:
'Các con mau đi đi! Để mẹ ở lại nói chuyện với con trai mẹ... Đêm nay, công lý phải được thực thi!'.
Bà lão dang rộng hai tay ôm chặt lấy bóng ma áo đỏ đang lao tới, để ngọn lửa xanh lam từ bức di ảnh bùng cháy bao trùm lấy cả hai người trong tiếng gào thét rúng động cả đường hầm!"""

    part3_full = """'Chỉ có phá hủy chiếc van xả áp suất khẩn cấp ở buồng đốt đầu tàu thì đoàn tàu ma này mới dừng lại được!' - Vị bác sĩ già hét lớn giữa tiếng gầm rú rung trời chuyển đất của động cơ diesel đang bốc cháy đỏ rực!
Tôi và cô nữ sinh đạp tung cánh cửa thép ngăn cách khoang lái, lao vào buồng điều khiển của đầu máy xe lửa.
Bên trong buồng lái, ngọn lửa ma quái màu xanh lục đang bùng cháy dữ dội trên khắp các bảng mạch điều khiển.
Chiếc cần gạt phanh chính đã bị ai đó dùng dây xích sắt dày đặc khóa chặt vào thành thép, trên khóa xích dán chín đạo bùa phong ấn bằng máu tươi!
Đoàn tàu lúc này như một con quái vật sắt điên cuồng lao dốc không phanh với vận tốc hơn một trăm hai mươi cây số một giờ, hướng thẳng về phía vực sâu sụp đổ ở cuối đường hầm – nơi có hàng vạn tấn đất đá phế tích đang chực chờ nuốt chửng tất cả!

Đúng lúc ấy, qua khung kính chắn gió của đầu tàu nhìn ra ngoài đường ray, một cảnh tượng kinh hoàng đập vào mắt tôi:
Giữa đường ray phía trước, linh hồn của hàng trăm nạn nhân thảm kịch năm 2017 đang đứng xếp thành một bức tường người trắng toát!
Họ đưa những cánh tay xương xẩu lên chỉ thẳng vào khoang lái, cất lên tiếng hô rền vang như sấm sét:
'Trả lại sự thật... Trả lại sự thật cho chúng tôi!'.
Bác sĩ già nhìn thấy cảnh tượng ấy, hai đầu gối quỵ xuống sàn sắt, nước mắt lăn dài trên khuôn mặt khắc khổ:
'Tôi có tội... Tôi đã vì sự hèn nhát của bản thân mà để linh hồn các bạn phải ngậm đắng nuốt cay suốt bảy năm trời dưới đáy vực lạnh buốt!'.
Nói rồi, ông rút từ trong túi áo ra chiếc hộp đen ghi âm buồng lái của đoàn tàu năm 2017 – vật chứng tối quan trọng mà ông đã bí mật cất giấu suốt ngần ấy năm – trao vào tay tôi:
'Cậu nhà báo... Hãy mang chiếc hộp đen này ra ánh sáng pháp luật! Hãy trả lại sự trong sạch cho anh lái tàu dũng cảm và tất cả những nạn nhân vô tội!'.

Chưa kịp để tôi ngăn lại, vị bác sĩ già đã lao mình về phía chiếc van áp suất đang bốc khói nghi ngút ở góc buồng đốt.
Ông dùng cả thân mình ôm chặt lấy khối van đồng nóng bỏng hàng trăm độ C, dùng chiếc mỏ lết sắt giáng những đòn chí tử vào chốt khóa an toàn!
'XÈO... XÈO!' - Da thịt bốc khói khét lẹt, nhưng ông không hề buông tay, gầm lên một tiếng vang động: 'DỪNG LẠI MAU!'.
'RẮC... XOẢNG!' - Chốt van an toàn bị đánh gãy lìa!
Một luồng hơi nước áp suất cực cao màu trắng xóa phun trào dữ dội, thổi bay toàn bộ lớp bùa chú phong ấn trên cần phanh chính!
Đoàn tàu rung chuyển bần bật, hệ thống phanh khí nén khẩn cấp bắt đầu kích hoạt phát ra những tiếng rít chói tai xé rách màng nhĩ!
Những bánh thép phanh cháy đỏ rực, tia lửa bắn tung tóe như pháo hoa dọc theo hai bên sườn núi!

Thế nhưng con quái vật bóng ma áo đỏ – hiện thân của sự căm hờn và oán khí tích tụ suốt bảy năm – đã đuổi tới cửa khoang lái!
Khuôn mặt nó méo mó đầy máu me, hai mắt rực cháy ngọn lửa hận thù, giang rộng đôi bàn tay móng vuốt sắc nhọn lao thẳng về phía cô nữ sinh!
Trong khoảnh khắc sinh tử ngàn cân treo sợi tóc, cô nữ sinh không hề sợ hãi hay lùi bước.
Cô nâng cây đàn vĩ cầm lên ngang vai, đặt cây cung vĩ kéo lên dây đàn khúc nhạc 'Khúc Ca Bình Yên' – giai điệu mà người cha phụ tá lái tàu của cô thường hát ru cô ngủ lúc còn thơ ấu.
Tiếng vĩ cầm trong trẻo, tha thiết và tràn ngập tình yêu thương vang lên giữa không gian bão lửa u tối.
Âm thanh thuần khiết của tình phụ tử và lòng tha thứ như một dòng suối mát lành tưới tắm vào tâm hồn đầy oán hận của bóng ma.
Đôi bàn tay móng vuốt của quái vật bỗng nhiên chững lại giữa không trung.
Lớp máu me và tà khí trên mặt nó từ từ tan biến, để lộ ra khuôn mặt của một người phụ nữ trẻ hiền hậu – người mẹ năm xưa từng ôm con chết trong thảm kịch.
Hai dòng nước mắt trong vắt lăn dài trên gò má người phụ nữ.
Bà nhìn cô nữ sinh, rồi nhìn sang bức tường linh hồn phía trước, khẽ gật đầu mỉm cười thanh thản.

Đúng lúc đó, đoàn tàu hỏa lao ra khỏi miệng hầm phế tích và dừng khựng lại an toàn trên cây cầu sắt nối liền hai sườn núi!
Đầu mũi tàu chỉ còn cách miệng vực sâu chưa đầy ba mét!
Chiếc đồng hồ điện tử trong buồng lái nhảy vọt sang con số: 05 giờ 00 phút sáng ngày mới!
Những tia nắng ban mai đầu tiên rực rỡ chiếu rọi qua khung kính chắn gió, sưởi ấm toàn bộ khoang tàu lạnh lẽo.
Dưới ánh sáng mặt trời ấm áp, hình bóng của hàng trăm oan hồn trên đường ray từ từ tan biến vào làn sương sớm, để lại một bầu trời trong xanh và thanh bình đến lạ kỳ.
Lời nguyền bảy năm của chuyến tàu đêm không ga đến cuối cùng đã được hóa giải trọn vẹn bằng sự hy sinh, lòng quả cảm và ánh sáng của sự thật!

Khi tiếng còi xe của lực lượng cứu hộ và cơ quan an ninh đường sắt rền vang từ chân núi tiến lên hiện trường, tôi và cô nữ sinh bước xuống đường ray, nắm chặt chiếc hộp đen vật chứng trong tay.
Toàn bộ sự thật đen tối về vụ án sập hầm Đèo Cả năm 2017 sẽ được công khai trước công luận và công lý trần gian.
Những kẻ chủ mưu rút ruột công trình dù có trốn chạy hay dùng tiền bạc che đậy tinh vi đến đâu, cũng sẽ phải đối mặt với sự trừng phạt nghiêm khắc nhất của pháp luật.
Đứng trên đỉnh đèo đón từng làn gió sớm trong lành, tôi nhìn về phía chân trời xa xăm nơi ánh bình minh đang bừng sáng rạng ngời.
Trong cuộc sống này, không có bóng tối nào là vĩnh cửu, và không có sự thật nào có thể bị chôn vùi mãi mãi.
Chính nghĩa và lòng thiện lương sẽ luôn là ngọn đuốc dẫn đường soi sáng cho con người vượt qua mọi giông bão tăm tối nhất của cuộc đời.

Theo bạn, sức mạnh của sự tha thứ và công lý có thể hóa giải được những oán hận sâu nặng nhất không? Hãy để lại suy nghĩ và cảm nhận của bạn dưới phần bình luận nhé!"""

    return {
        "title": story_title,
        "genre": "KINH_DI",
        "voice": "vi-VN-NamMinhNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": f"{story_title} (Tập 1 - Chuyến Tàu Ma Lúc 0h15 Đêm)",
                "full_text": part1_full,
                "caption": (
                    f"[PHẦN 1] {story_title}. "
                    "Chuyến tàu đêm bất ngờ dừng giữa đường hầm bỏ hoang và dấu tay máu cào kính lúc 0h15 sáng! "
                    "👉 Đón xem Tập 2 - 7 Tội Lỗi Quá Khứ tối nay nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #chuyentau #tamlinh"
                )
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": f"{story_title} (Tập 2 - 7 Tội Lỗi & Bí Mật Hầm Đèo Cả)",
                "full_text": part2_full,
                "caption": (
                    f"[PHẦN 2] {story_title}. "
                    "Bí mật kinh hoàng về vụ sập hầm 7 năm trước và bóng ma áo đỏ trườn qua trần tàu! "
                    "👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục hóa giải lời nguyền! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #chuyentau #tamlinh"
                )
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": f"{story_title} (Tập 3 - Hóa Giải Oán Khí & Ánh Sáng Bình Minh)",
                "full_text": part3_full,
                "caption": (
                    f"[PHẦN 3 / KẾT] {story_title}. "
                    "Trọn bộ 3 tập đã lên sóng! Bạn có tin vào luật nhân quả báo ứng ở đời không? "
                    "👉 Hãy để lại bình luận và đăng ký kênh nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #chuyentau #tamlinh"
                )
            }
        ]
    }
'''
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(code, encoding='utf-8')
    print(f"✅ Đã tạo kịch bản: {target.name}")

if __name__ == "__main__":
    build_horror_chuyentau_story()
