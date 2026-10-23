# -*- coding: utf-8 -*-
import re

c43_p1 = """Chùm sáng tím từ camera điện thoại vừa quét qua đầu đinh ốc treo đồng hồ, một chấm đỏ rực bỗng nhấp nháy phát tín hiệu sóng wifi hai chấm bốn gigahertz ngay trên đầu giường ngủ của tôi.

Căn phòng trọ tầng bốn vừa thuê ban chiều bỗng trở nên lạnh lẽo lạ thường. Tôi tắt toàn bộ đèn tuýp trên trần, kéo chặt tấm rèm cửa sổ dày cộp lại để cô lập hoàn toàn ánh sáng từ ngọn đèn cao áp ngoài ngõ hẻm. Trên màn hình chiếc điện thoại cài phần mềm phân tích phổ vô tuyến mạng nội bộ, một thiết bị phát sóng ẩn danh không tên đang truyền dữ liệu video liên tục với băng thông mười mê-ga-bít mỗi giây về một dải địa chỉ IP tĩnh nội hạt.

Là sinh viên năm cuối khoa Kiến trúc công trình, tôi quá quen thuộc với từng đường gân kết cấu bê tông và hệ thống dây điện âm tường. Chiều nay, lúc trao chìa khóa phòng, gã chủ nhà trọ tên Tài đã nhìn tôi bằng ánh mắt soi mói đáng ngờ. Gã vờ niềm nở dặn dò: 'Phòng này giá rẻ đặc biệt cho nữ sinh ngoan. Chú lắp sẵn quạt thông gió với đồng hồ mới tinh, cấm được tự ý đóng đinh hay đưa bạn trai về ngủ lại đấy nhé!'.

Tôi đặt chiếc ba lô đồ nghề kiến trúc lên bàn, rút ra chiếc kìm cắt mũi nhọn và chiếc đồng hồ vạn năng đo dòng rò. Tôi bắc chiếc ghế gỗ ba chân bước lên, áp tai sát vào mặt số chiếc đồng hồ tròn treo tường. Không hề có tiếng kim giây tích tắc cơ học thông thường, thay vào đó là tiếng rít cao tần của một biến áp nguồn siêu nhỏ đang chuyển đổi dòng điện hai trăm hai mươi vôn sang năm vôn DC.

Dùng mũi kéo inox cậy nhẹ lớp mặt nạ nhựa bảo vệ, mặt số bằng bìa cứng bung ra để lộ một bo mạch điện tử vi sai bằng đốt ngón tay. Ngay chính giữa đinh ốc cố định kim giờ là một ống kính quang học mắt cá chỉ bằng đầu tăm, hướng thẳng xuống mép nệm và cửa phòng tắm. Sợi cáp nguồn siêu mỏng màu đen của nó được luồn khéo léo qua lỗ khoan xuyên tường nối thẳng vào hộp điện quạt gió.

Tôi không giật đứt dây nguồn ngay để tránh kích hoạt cảnh báo ngắt kết nối trên máy chủ của kẻ theo dõi. Tôi lấy một mẩu băng dính điện màu đen trong hộp đồ dán đè kín mít lên mắt kính quang học, chặn đứng luồng hình ảnh truyền đi. Đúng hai phút sau, tiếng bước chân lẹp xẹp từ dưới cầu thang bỗng dừng lại ngay trước cửa phòng tôi!"""

c43_p2 = """Tiếng chìa khóa vạn năng vừa tra vào ổ khóa lách cách, ngón tay tôi đã cắm chiếc thẻ nhớ micro SD ba mươi hai gigabyte vào đầu đọc thẻ máy tính xách tay.

Một tiếng gõ cửa cộc cộc vang lên dồn dập kèm giọng nói khàn khàn đầy sốt ruột của gã chủ trọ ngoài hành lang:
'Cháu Diệp ơi! Cầu dao điện tầng bốn tự dưng bị nhảy áp, chú nghi chập dây quạt thông gió nên vào kiểm tra hộ một lát nhé!'.

Tim tôi đập mạnh một nhịp nhưng các ngón tay vẫn giữ độ chuẩn xác tuyệt đối của một người quen vẽ kỹ thuật. Gã cuống cuồng vì màn hình theo dõi trên điện thoại của gã bỗng dưng tối om như mực. Tôi hít sâu một hơi, cất giọng bình thản đáp vọng ra ngoài:
'Cháu vừa tắm xong đang thay quần áo! Chú đợi mười phút nữa để cháu mặc đồ chỉnh tề đã nhé!'.

Trong khoảng thời gian quý giá đó, tôi bấm mở thư mục gốc của chiếc thẻ nhớ vừa rút từ khe cắm micro camera. Màn hình laptop mười lăm inch lập tức hiện ra hơn năm mươi thư mục con được phân cấp chi tiết theo số phòng từ bốn lẻ một đến bốn lẻ bốn. Hàng trăm tệp video độ phân giải cao ghi lại sinh hoạt riêng tư của các nữ sinh từng thuê trọ suốt hai năm qua hiện rõ mồn một kèm ngày giờ quay chụp.

Kinh khủng hơn, trong một tệp ghi chú có tên danh sách khách thuê, gã lưu đầy đủ số căn cước công dân, trang mạng cá nhân và số điện thoại phụ huynh của từng nạn nhân nhằm mục đích tống tiền khi họ chuyển đi. Máu nóng dồn lên thái dương, tôi lập tức bấm tổ hợp phím sao lưu toàn bộ dữ liệu lên đám mây lưu trữ cá nhân, đồng thời gửi đường link nén dữ liệu cho chị Mai - cựu sinh viên từng ở phòng này năm ngoái.

Bên ngoài cửa, gã chủ trọ không còn đủ kiên nhẫn. Tiếng then cài cửa sắt bắt đầu bị xoay tròn lục cục, gã đang lén dùng chùm chìa khóa phụ để mở chốt trong. Tôi với tay rút chiếc bình xịt hơi cay tự vệ trong túi áo khoác, tay kia cầm chắc thanh thước chữ T bằng nhôm cứng dài một mét, đứng nép sát vào góc chết sau bản lề cửa:
'Chú Tài! Chú dám bước qua ngạch cửa này một bước, tôi sẽ xịt thẳng áp lực vào mắt chú đấy!'."""

c43_p3 = """Ánh đèn pha xe bán tải của hội nữ sinh và tổ dân phố vừa chiếu thẳng qua khung cửa thông gió, tiếng còi xe bóp dồn dập đã khiến gã chủ trọ đánh rơi chùm chìa khóa xuống sàn gạch.

Cánh cửa phòng bật mở toang, gã chủ trọ bước hụt một nhịp, gương mặt tái mét cắt không còn giọt máu. Trước mắt gã không phải là một nữ sinh hoảng loạn sợ hãi, mà là màn hình máy tính đang phát lặp đi lặp lại đoạn video clip chính gã trèo lên thang gỗ gắn đinh ốc camera giấu kín vào buổi sáng.

Gã lắp bắp, nụ cười giả tạo trên khóe môi giật giật méo xệch:
'Cháu... cháu hiểu lầm rồi! Chú lắp thiết bị cảm biến khói chống cháy nổ để bảo vệ an toàn cho cả xóm trọ thôi mà!'.

'Cảm biến khói mà gắn ống kính mắt cá chĩa thẳng vào giường ngủ và kết nối thẻ nhớ ba mươi hai gigabyte sao?', giọng nói sắc lạnh của nữ luật sư bảo vệ quyền lợi phụ nữ vang lên đanh thép từ đầu cầu thang. Đi ngay phía sau cô là bác tổ trưởng dân phố cùng bốn bạn nữ từng là nạn nhân thuê trọ cũ, trên tay cầm sẵn hợp đồng thuê nhà và biên lai nộp tiền cọc.

Gã chủ trọ hoảng loạn thọc tay vào túi quần toan bấm xóa ứng dụng trên điện thoại di động, nhưng tôi đã nhanh tay giật cầu dao tổng của tầng bốn, ngắt hoàn toàn trạm phát sóng wifi nội bộ. Toàn bộ chứng cứ điện tử và dữ liệu video tống tiền trên thẻ nhớ gốc đã được đồng bộ nguyên vẹn vào USB bảo mật trước sự chứng kiến của biên bản hiện trường tổ dân phố.

Gã khuỵu hai đầu gối xuống nền gạch hoa hành lang, đôi bàn tay run rẩy không còn sức phản kháng. Toàn bộ các phòng trọ trong tòa nhà lập tức bị các cơ quan chức năng tiến hành kiểm tra rà soát toàn diện thiết bị quay lén, giấy phép kinh doanh lưu trú của cơ sở bị đình chỉ ngay trong đêm.

Tôi thu dọn dụng cụ vẽ và hành lý cá nhân, bước lên chiếc xe bán tải của nhóm bạn để chuyển thẳng vào khu ký túc xá an toàn của trường. Ánh đèn đường phố đêm rực rỡ soi bóng những con người dũng cảm đứng lên bảo vệ nhân phẩm của chính mình. Quyền riêng tư là bất khả xâm phạm, và mọi âm mưu hèn hạ núp bóng đinh ốc vô tri sớm muộn cũng sẽ bị ánh sáng công lý phơi bày trọn vẹn."""

c50_p1 = """Mũi búa kiểm định của tôi vừa gõ nhẹ vào vách thạch cao phòng tắm, một khoảng rỗng sâu ba mươi phân đã phát ra tiếng vang rợn người.

Căn biệt thự kiểu Pháp cổ ba tầng ở trung tâm thành phố đang được niêm phong để chuẩn bị đưa ra bán đấu giá tài sản tịch biên thi hành án. Mười năm trước, chủ nhân hợp pháp của cơ ngơi này là bà Đoàn Mỹ Lan, một nữ doanh nhân ngành dược thành đạt, bỗng dưng mất tích bí ẩn không để lại bất kỳ tung tích nào. Toàn bộ giấy tờ sở hữu bất động sản sau đó bị một nhóm đầu cơ bất động sản do gã trùm Mã Khắc đứng đầu thâu tóm qua một hợp đồng ủy quyền giả mạo chữ ký.

Tôi là kỹ sư giám định kết cấu công trình dân dụng độc lập được hội đồng thi hành án chỉ định kiểm định an toàn trước khi bán đấu giá. Trên tay tôi là chiếc máy đo khoảng cách laser Bosch GLM và tập hồ sơ bản vẽ thiết kế hoàn công lưu trữ từ năm 2014. Khi đối chiếu từng bức vách, tôi nhận thấy điểm bất thường chết người tại phòng ngủ master tầng hai: Bức tường ngăn giữa tủ quần áo âm tường và phòng tắm có độ dày thực tế lên tới tám mươi phân, trong khi bản vẽ kết cấu chịu lực gốc chỉ dày bốn mươi phân.

Căn phòng nồng nặc mùi vôi vữa ẩm mốc và hóa chất chống thấm cũ kỹ suốt một thập kỷ. Tôi dùng đầu nhọn của búa kiểm định gõ dọc theo mép chân tường, âm thanh phát ra bỗng chuyển từ tiếng đục đặc của bê tông sang tiếng vang rỗng của một khoang chứa nhân tạo.

Đúng lúc đó, cánh cửa phòng bật mở đánh rầm. Gã trùm môi giới bất động sản Mã Khắc bước vào, miệng phì phèo điếu xì gà, khóe môi nhếch lên nụ cười lạnh:
'Kỹ sư Trần làm việc nhiệt tình quá nhỉ! Biệt thự cũ nát này chiều nay sẽ có lệnh san phẳng để chia lô bán nền. Cậu chỉ cần ký vào biên bản đủ điều kiện tháo dỡ là xong, đừng bới lông tìm vết làm gì cho mệt xác!'.

Hắn tiện tay nhét một chiếc phong bì dày cộm mười triệu tiền mặt vào túi áo bảo hộ của tôi. Tôi rút chiếc phong bì đặt trả lại mép bồn rửa mặt, tay cầm chắc chiếc búa kiểm định:
'Tường sai lệch bản vẽ bốn mươi phân! Theo quy chuẩn kỹ thuật, tôi bắt buộc phải dùng máy khoan rút lõi để kiểm tra kết cấu bên trong!'.
Sắc mặt Mã Khắc lập tức biến sắc, tối sầm lại như mây bão!"""

c50_p2 = """Mã Khắc vung tay hất văng chiếc máy đo laser trên bàn của tôi xuống sàn gạch hoa vỡ tan thành nhiều mảnh.

Hai gã bảo kê cao lớn từ ngoài hành lang lù lù bước vào, chắn kín lối ra vào duy nhất của căn phòng ngủ tầng hai. Gã nghiến răng ken két, gằn từng giọng đe dọa:
'Mày muốn sống để về ăn cơm với gia đình không? Tao nói lại lần cuối: Chiều nay máy xúc sẽ ủi phẳng căn nhà này! Không có khoan cắt gì hết!'.

Tôi lùi lại một bước, tựa lưng vào mép bàn đá cẩm thạch kiên cố. Tay phải tôi bí mật bấm vào đầu chiếc bút ký tên cài ở túi áo ngực - thiết bị ghi âm kỹ thuật số chuyên dụng của giám định viên đã kích hoạt và đang đồng bộ trực tiếp dữ liệu âm thanh qua vệ tinh về văn phòng công chứng. Trên giá đỡ kim loại cạnh tường, chiếc máy khoan rút lõi công suất ba nghìn oát đã được tôi đấu nối sẵn vào nguồn điện dự phòng.

Tôi nhìn thẳng vào đôi mắt vằn tia máu của Mã Khắc, giọng nói đanh thép không hề nao núng:
'Ông sốt sắng muốn ủi phẳng căn biệt thự này trước bốn giờ chiều... Không phải vì tiến độ dự án, mà vì ông sợ chiếc máy khoan rút lõi sẽ bóc trần bí mật mười năm trước ông giấu sau bức tường thạch cao này đúng không? Giấy phép tháo dỡ của ông hoàn toàn vô giá trị khi chưa có chữ ký nghiệm thu của tôi!'.

Lời vừa dứt, tiếng còi xe thanh tra tư pháp bỗng vang lên dồn dập từ dưới sân cổng sắt! Luật sư Thục Quyên, đại diện quyền lợi pháp lý cho người thừa kế duy nhất của bà Đoàn Mỹ Lan, cùng hai cán bộ thi hành án bước nhanh lên cầu thang.

'Ông Mã Khắc! Phiên bán đấu giá và lệnh tháo dỡ chiều nay đã bị tòa án đình chỉ khẩn cấp theo yêu cầu bảo lưu chứng cứ!', giọng luật sư Quyên vang lên đanh thép.

Mã Khắc giật nảy mình thối lui hai bước, trán lấm tấm mồ hôi hột. Tận dụng giây phút đó, tôi nhấc chiếc máy khoan rút lõi bê tông công nghiệp mũi kim cương một trăm mười milimét, cắm nguồn điện và ấn mạnh vào tâm bức tường nghi vấn. Mũi khoan xoay tít rít lên dữ dội, lớp bụi thạch cao trắng xóa tuôn ra rào rào, để lộ một cánh cửa thép bọc chì niêm phong kín mít sau lớp vữa!"""

c50_p3 = """Cánh cửa sắt của chiếc két âm tường bọc chì vừa được mũi khoan kim cương cậy tung khóa cơ học, chiếc hộp kim loại chống ẩm mười năm trước bỗng lộ ra nguyên vẹn.

Bên trong hộp kim loại là tập di chúc viết tay nguyên bản có dấu lăn tay của nữ doanh nhân Đoàn Mỹ Lan, cùng một chiếc thẻ nhớ ghi âm lời trăn trối cuối cùng. Toàn bộ sự thật bị chôn vùi suốt một thập kỷ bỗng chốc được bóc trần hoàn toàn: Mười năm trước, chính Mã Khắc và đường dây làm giả giấy tờ đã ép buộc nạn nhân ký vào các hợp đồng ủy quyền khống, sau đó bí mật đổ bê tông che lấp toàn bộ két sắt lưu trữ hồ sơ tài sản gốc hòng xóa sạch mọi dấu vết trước khi sang tên.

Mã Khắc đứng chôn chân tại chỗ, gương mặt xám ngoét không còn một tia huyết sắc. Đôi bàn tay của gã run rẩy buông thõng khi biên bản hiện trường được lập tức ký kết dưới sự chứng kiến của lực lượng chức năng. Chiếc còng số tám bập tanh tách vào cổ tay gã và đồng bọn, chấm dứt hoàn toàn mười năm tác oai tác quái của băng nhóm đầu cơ bất động sản lừa đảo.

Toàn bộ khối tài sản trị giá hơn một trăm hai mươi tỷ cùng quyền sở hữu căn biệt thự cổ được tòa án phán quyết trao trả lại toàn vẹn cho người con gái của nữ doanh nhân quá cố.

Luật sư Thục Quyên siết chặt tay tôi, đôi mắt ngấn lệ xúc động:
'Cảm ơn kỹ sư Trần! Nếu không có sự kiên định và mũi khoan chuẩn xác của anh, có lẽ công lý và di nguyện của người đã khuất mãi mãi bị chôn vùi dưới lớp gạch đá đổ nát chiều nay!'.

Tôi mỉm cười, lau sạch lớp bụi thạch cao vương trên chiếc búa kiểm định:
'Lương tâm nghề nghiệp và thước đo kỹ thuật không bao giờ cho phép tôi thỏa hiệp với bất kỳ sự dối trá nào.'.

Tôi thu dọn dụng cụ đo đạc, bước chân ra khỏi cổng vòm biệt thự cổ kính. Ánh nắng chiều vàng rực rỡ chiếu rọi qua từng tán lá xà cừ, quét sạch không khí u uất của mười năm oan khuất. Sự thật có thể bị che giấu tạm thời dưới lớp vôi vữa, nhưng công lý và lẽ phải sẽ luôn đứng vững trước dòng chảy của thời gian."""

with open('core/stories/cycles_41_to_50_masterpieces.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace C43
pattern43 = r'(def get_story_cycle_43\(title: str = ""\) -> Dict\[str, Any\]:\s+t = title or "[^"]+"\s+p1 = """)[^"]+("""\s+p2 = """)[^"]+("""\s+p3 = """)[^"]+("""\s+res =)'
repl43 = rf'\g<1>{c43_p1}\g<2>{c43_p2}\g<3>{c43_p3}\g<4>'
text = re.sub(pattern43, repl43, text)

# Replace C50
pattern50 = r'(def get_story_cycle_50\(title: str = ""\) -> Dict\[str, Any\]:\s+t = title or "[^"]+"\s+p1 = """)[^"]+("""\s+p2 = """)[^"]+("""\s+p3 = """)[^"]+("""\s+res =)'
repl50 = rf'\g<1>{c50_p1}\g<2>{c50_p2}\g<3>{c50_p3}\g<4>'
text = re.sub(pattern50, repl50, text)

with open('core/stories/cycles_41_to_50_masterpieces.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Cycles 43 and 50 expanded!")
