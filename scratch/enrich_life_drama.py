# -*- coding: utf-8 -*-
with open('core/stories/life_drama.py', 'r', encoding='utf-8') as f:
    text = f.read()

part1_enrichment = """
Ký ức về những ngày tháng gian truân thuở ấy như những thước phim quay chậm nhói buốt nơi lồng ngực. Năm hai mươi hai tuổi, vừa tốt nghiệp đại học với tấm bằng loại giỏi, tôi đã nhận được học bổng toàn phần thạc sĩ công nghệ tại Nhật Bản. Đó là ước mơ cả đời tôi ấp ủ, là cánh cửa mở ra một tương lai xán lạn và rộng mở. 

Thế nhưng đúng vào ngày tôi chuẩn bị làm thủ tục xin visa, bố tôi bất ngờ ngã quỵ trong gian bếp sau cơn tai biến. Nhìn người cha cả đời tần tảo sớm hôm nuôi hai anh em ăn học nay nằm bất động trên giường bệnh, nửa thân người co quắp, ánh mắt đờ đẫn không thể nói thành lời, tôi đã cắn chặt môi xé nát lá thư báo trúng tuyển học bổng. 

Tôi quyết định ở lại thành phố, từ bỏ tương lai rực rỡ để ngày ngày cận kề bên giường bệnh của bố. Suốt mười năm thanh xuân tươi đẹp nhất của người con gái, trong khi bạn bè cùng trang lứa mải mê hẹn hò, đi du lịch, phấn đấu thăng tiến và lập gia đình êm ấm, thì thế giới của tôi chỉ thu bé lại trong bốn bức tường ẩm thấp và mùi thuốc sát trùng nồng nặc.

Mỗi buổi sáng, tôi phải thức dậy từ năm giờ để nấu cháo xay nhuyễn, massage từng khớp tay khớp chân cho bố đỡ bị teo cơ, rồi mới vội vã phóng xe máy đến công ty làm việc. Chiều tối tan ca, tôi lại tất tả chạy về nhà lo cơm nước, tắm rửa, thay bỉm cho bố, rồi thức trắng đêm đến một hai giờ sáng bên chiếc máy tính xách tay nhận thêm các dự án lập trình ngoài giờ để kiếm thêm tiền trang trải viện phí.

Trong khi đó, anh Tuấn và chị Hạnh sống trong căn hộ chung cư cao cấp cách nhà bố chưa đầy ba cây số, nhưng số lần ghé qua nhà chỉ đếm trên đầu ngón tay. Mỗi lần tôi gọi điện bảo bố trở trời đau nhức xương khớp cần tiền mua thuốc bổ, chị Hạnh lại chua ngoa qua điện thoại: "Bố già rồi thì bệnh tật là chuyện đương nhiên, cô cứ làm quá lên để vòi tiền anh em! Chúng tôi còn phải lo tiền học trường quốc tế cho con, làm gì có tiền dư mà ném qua cửa sổ!". 

Thậm chí có những tháng bố phải nhập viện cấp cứu vì viêm phổi nặng, tiền viện phí thiếu hụt hàng chục triệu đồng, tôi phải muối mặt đi vay mượn bạn bè từng đồng một, thì trên trang cá nhân của chị dâu lại liên tục đăng ảnh đi ăn buffet tôm hùm, khoe chiếc nhẫn kim cương mới tậu và những chuyến nghỉ dưỡng sang chảnh tại Phú Quốc!
"""

part2_enrichment = """
Bác ruột tôi – ông Trần Quốc Đại – run run cầm tập hồ sơ bệnh án và xấp hóa đơn viện phí dày cộm lên xem. Đôi bàn tay gầy guộc đầy vết đồi mồi của người cựu chiến binh già run rẩy theo từng dòng chữ:

"Đây... đây là hóa đơn tiền phẫu thuật thông tắc mạch máu não tháng tư năm kia... Một trăm bốn mươi triệu đồng! Người nộp tiền: Trần Thu Hà! Còn đây là tiền mua máy thở oxy tại nhà, tiền thuốc điều trị huyết áp mỗi tháng ba triệu sáu... Toàn bộ mười năm ròng rã, không sót một tháng nào, đều là con bé Hà tự tay ký tên đóng tiền!"

Ông Đại ngước đôi mắt ngấn lệ nhìn quanh gian nhà cổ, rồi nhìn sang bức di ảnh của bố tôi trên bàn thờ, giọng nghẹn ngào rung lên từng chập:

"Các bác, các chú trong họ nhìn xem! Con gái người ta hy sinh cả mười năm thanh xuân, không màng đến hạnh phúc riêng tư, cắn răng làm lụng ngày đêm để nuôi bố nằm liệt giường. Còn thằng con trai trưởng được ăn học đến nơi đến chốn, được bố cho hai mảnh đất tiền tỷ ở quê, thì đến một viên thuốc hạ sốt cho bố cũng chưa từng mua lấy một lần! Đã thế hôm nay lại còn kéo vợ về đây giở trò bỉ ổi, ép tay người hấp hối điểm chỉ để cướp nốt căn nhà hương hỏa! Thử hỏi dưới suối vàng, chú An có nhắm nổi mắt hay không?"

Tiếng sụt sùi của mấy người cô, người thím ngồi quanh bàn bắt đầu vang lên. Có người thím họ từng nhiều lần sang phụ tôi trở mình cho bố, lúc này cũng đứng dậy gạt nước mắt phân trần:

"Tôi làm chứng cho con bé Hà! Mười năm qua, trời mưa hay trời nắng, cứ đêm hôm bố trở bệnh là một mình con bé cõng bố lên xe cấp cứu. Nhiều đêm đông rét căm căm, con bé vừa thức canh truyền dịch cho bố vừa ngồi bệt dưới sàn gạch gõ máy tính làm việc kiếm tiền. Bát cháo loãng nó cũng nhường bố ăn phần đặc, còn nó chỉ ăn vội gói mì tôm sống. Anh em họ hàng ai có mắt cũng nhìn thấy, có lòng thì phải biết thương lấy nó, chứ sao lại nỡ đối xử tàn nhẫn và cạn tình cạn nghĩa như phường cướp cạn thế này!"
"""

target1 = "Tôi nhìn bộ mặt tham lam, trơ trẽn của anh trai và chị dâu, tôi từ tốn bước xuống bậc thềm"
text = text.replace(target1, part1_enrichment.strip() + "\n\n" + target1)

target2 = "Chị Hạnh run bắn người lên, hai môi mấp máy nhưng không thể cãi lại được nửa lời."
text = text.replace(target2, part2_enrichment.strip() + "\n\n" + target2)

with open('core/stories/life_drama.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Enriched Part 1 & Part 2 in life_drama.py!")
