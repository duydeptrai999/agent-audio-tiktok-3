# -*- coding: utf-8 -*-
from pathlib import Path

content = '''# -*- coding: utf-8 -*-
"""
core/stories/school_romance_vungtrom_masterpiece.py
Bộ Kịch Bản Thanh Xuân Vườn Trường Phong Cách "Vụng Trộm Không Thể Giấu" Chuẩn Master Codex 8.0:
Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ
- Độ dài chuẩn điện ảnh: 3 Tập x ~1.500 - 1.800 từ (Tổng ~4.700 từ / ~30+ phút audio).
- Ngọt ngào, trong trẻo, sâu lắng, cảm xúc thanh xuân chữa lành tâm hồn, không cẩu huyết, không hoạt hình ba xu.
- Giọng đọc chỉ định: vi-VN-HoaiMyNeural (rate="+6%").
"""

from typing import Dict, Any

def get_vungtrom_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ"

    part1_body = """Tiếng ve râm ran xé toạc trưa hè oi ả của thành phố Nam Giang, khi Khương Ninh mười lăm tuổi đứng co ro dưới bóng râm của cây long não ven hồ. Đôi mắt tròn xoe của cô bé đỏ hoe, từng giọt nước mắt ấm ức lăn dài trên gò má trắng ngần nhìn chiếc cặp sách màu hồng bị nhóm bạn gái ngỗ ngược ném chìm nghỉm xuống làn nước đục ngầu.

Tiếng cười đùa chế nhạo của đám thiếu nữ vang lên giòn tan rồi tan biến vào con ngõ vắng, bỏ lại cô bé nhỏ với bộ đồng phục ướt đẫm mồ hôi và nỗi uất ức nghẹn ngào trong lồng ngực. 

Đúng lúc Khương Ninh tuyệt vọng quỳ gối bên bờ cỏ định thò tay vớt chiếc cặp thì một bóng dáng cao ráo, tuấn tú mặc chiếc áo phông trắng đơn sơ bỗng xuất hiện như một tia nắng xé toạc mây mù.

"Em gái nhỏ, nước sâu nguy hiểm, muốn biến thành cá bống à?" - Giọng nói trầm ấm, mang theo chút lười biếng và ý cười quen thuộc vang lên ngay trên đỉnh đầu.

Khương Ninh ngước mắt lên, giọt nước mắt còn đọng trên bờ mi cong vút. Đứng trước mặt cô là Thẩm Dục Trì – người bạn thân cùng lớp đại học của anh trai cô, chàng trai khôi ngô tuấn tú với nụ cười nửa miệng làm xiêu lòng biết bao nữ sinh trong trường.

Chưa kịp để cô ú ớ phân trần, Thẩm Dục Trì đã thong thả cởi chiếc đồng hồ kim loại đặt lên bờ cỏ, không một chút ngần ngại lội thẳng xuống đầm nước ngang hông để vớt chiếc cặp sách sũng nước lên cho cô. Anh bước lên bờ, vắt vạt áo ướt, rồi dùng chiếc khăn tay thơm mùi bạc hà mát lạnh cẩn thận lau sạch những giọt nước mắt lấm lem trên mặt Khương Ninh.

"Ai bắt nạt em gái nhỏ của anh thế? Nói tên ra đây, để anh Dục Trì dạy cho chúng nó một bài học nhớ đời." - Anh khẽ búng nhẹ vào trán cô một cái, đôi mắt hoa đào tràn ngập sự cưng chiều ấm áp.

Buổi chiều hôm ấy, anh dẫn cô vào tiệm trà sữa đối diện cổng trường, mua cho cô ly trà sữa trân châu đường đen nhiều kem béo và một chiếc bánh ngọt dâu tây thơm lừng. Anh ngồi đối diện, chống cằm ngắm nhìn cô bé phồng má nhai trân châu, ngón tay thon dài gõ nhịp trên bàn kính: "Ngoan, ăn hết rồi anh chở về. Chuyện chiếc cặp cứ bảo là do anh trai em nghịch ngợm làm rơi, không ai dám mắng em đâu."

Khoảnh khắc ấy, trong trái tim non nớt của cô bé mười lăm tuổi bỗng nảy mầm một hạt giống kỳ lạ, một thứ cảm xúc trong trẻo, ngọt ngào nhưng lại vô cùng bỏng cháy: Cô đã thích thầm chàng trai lớn hơn mình ba tuổi này mất rồi!

Những ngày tháng sau đó, hình bóng của Thẩm Dục Trì như một thói quen dịu dàng len lỏi vào từng ngóc ngách cuộc sống của Khương Ninh. Mỗi cuối tuần khi anh sang nhà chơi cờ cùng anh trai cô, Khương Ninh luôn lén lút đứng sau rèm cửa phòng khách nhìn lén anh. Anh mặc áo sơ mi kẻ caro phong trần, dáng người cao ráo tựa vào thành ghế, khóe môi luôn phảng phất nụ cười ấm áp. Thỉnh thoảng khi anh ngước lên bắt gặp ánh mắt lén lút của cô, anh lại nháy mắt trêu chọc rồi kín đáo dúi vào túi áo cô vài viên kẹo bạc hà nhập khẩu ngọt lịm. Viên kẹo tan chảy trên đầu lưỡi mang theo vị ngọt ngào và sự ấm áp kỳ diệu, xua tan đi mọi áp lực thi cử và những nỗi buồn vu vơ tuổi mới lớn.

Năm Khương Ninh bước vào kỳ thi tuyển sinh trung học phổ thông căng thẳng, biết cô học yếu môn Toán, Thẩm Dục Trì đã tình nguyện làm gia sư phụ đạo riêng cho cô mỗi tối thứ Bảy. Căn phòng gác mái nhỏ tràn ngập ánh đèn vàng ấm áp và thoang thoảng mùi gỗ trầm. Anh ngồi sát bên cạnh, kiên nhẫn giảng giải từng công thức hình học hóc búa, từng phương trình bậc hai phức tạp mà cô không hiểu. Hơi thở nam tính phảng phất hương xà phòng thơm dịu của anh mỗi lần cúi sát kiểm tra bài vở khiến vành tai Khương Ninh đỏ ửng như quả cà chua chín mộng. Tim cô đập thình thịch như muốn nhảy khỏi lồng ngực, những con số trên trang giấy bỗng chốc nhạt nhòa, chỉ còn lại gương mặt góc cạnh hoàn mỹ với sống mũi cao thẳng tắp của người con trai cô thầm thương trộm nhớ.

Khương Ninh giấu kín bí mật ngọt ngào ấy vào cuốn nhật ký nhỏ có khóa đồng giấu dưới đáy ngăn kéo. Trên từng trang giấy kẻ ô ly, cô cẩn thận nắn nót viết những dòng tâm sự ngây ngô: "Hôm nay anh Dục Trì khen chiếc kẹp tóc hoa cúc của mình đẹp", "Hôm nay anh xoa đầu mình bảo mình là cô bé ngoan nhất trần đời", "Ước gì thời gian trôi thật nhanh để mình mau lớn, để có thể đứng cạnh anh như một người trưởng thành thực thụ". Mục tiêu duy nhất của cô gái nhỏ là nỗ lực học tập thật giỏi, thi đỗ vào đúng ngôi trường Đại học Kiến trúc danh giá tại thành phố Nghi Sơn nơi Thẩm Dục Trì đang theo học những năm cuối.

Trong những năm tháng cấp ba đầy ắp bài vở và áp lực thi cử, mỗi trang sách giáo khoa của Khương Ninh dường như đều in đậm bóng hình của Thẩm Dục Trì. Cô nhớ những buổi chiều tan học muộn, khi hoàng hôn buông xuống nhuộm đỏ cả một góc trời, cô thường đứng nép mình bên hành lang tầng ba nhìn xuống sân bóng rổ. Ở đó, Thẩm Dục Trì với chiếc áo số 7 đang thoăn thoắt dẫn bóng, mồ hôi ướt đẫm vạt áo nhưng nụ cười vẫn rạng rỡ như ánh ban mai. Mỗi cú ném bóng ba điểm chuẩn xác của anh đều khiến cả sân trường hò reo vang dội, và trái tim cô bé nhỏ cũng đập rộn ràng theo từng nhịp bóng.

Cô cẩn thận lưu giữ từng chiếc vé xe buýt của những chuyến xe hai người tình cờ đi chung, từng chiếc vỏ kẹo bạc hà anh đưa, từng mẩu giấy nhớ anh viết vội nhắc cô uống nước ấm khi trời trở lạnh. Đối với Khương Ninh, Thẩm Dục Trì không chỉ là chàng trai cô thích thầm, mà anh còn là nguồn động lực lớn lao nhất thúc đẩy cô không ngừng nỗ lực vươn lên. Cô muốn trở thành một phiên bản tốt hơn của chính mình, muốn bản thân đủ ưu tú và tự tin để một ngày nào đó có thể đường hoàng đứng cạnh anh mà không cảm thấy tự ti hay nhỏ bé.

Thế nhưng, hiện thực cuộc đời chưa bao giờ chiều lòng người. Vào mùa hè năm Khương Ninh mười tám tuổi, ngay trước ngày diễn ra kỳ thi tốt nghiệp trung học phổ thông định mệnh một tuần, cô bất ngờ nghe thấy cuộc trò chuyện giữa anh trai và Thẩm Dục Trì ngoài ban công. Gia đình Thẩm Dục Trì xảy ra biến cố lớn về kinh tế, anh đã nộp hồ sơ xin học bổng toàn phần và quyết định sẽ bay sang Đức du học ngay sau khi hoàn thành lễ tốt nghiệp.

Tin sét đánh ngang tai khiến toàn bộ thế giới màu hồng của Khương Ninh sụp đổ hoàn toàn. Cầm trên tay chiếc cốc thủy tinh đựng đầy những ngôi sao giấy may mắn mà cô đã thức suốt một trăm đêm để gấp tặng anh nhân ngày sinh nhật tuổi hai mươi mốt, Khương Ninh đứng lặng thinh trong bóng tối hành lang, những giọt nước mắt mặn chát trào ra ướt đẫm vạt áo đồng phục.

Cơn gió mùa hạ thổi qua khung cửa sổ làm lay động những nhành hoa giấy tím biếc trước hiên nhà. Thanh xuân của mỗi người con gái đều có một chàng trai tỏa sáng như ánh mặt trời, rực rỡ đến mức khiến ta vừa khát khao chạm tới vừa lo sợ mình sẽ bị thiêu rụi bởi sự rạng ngời ấy. Mối tình đầu thầm kín dẫu mang theo vị ngọt ngào của những viên kẹo bạc hà, nhưng cũng đong đầy những giọt nước mắt nghẹn ngào của những lời yêu chưa một lần dám cất lên thành lời."""

    part1_cliff = """Khương Ninh siết chặt lọ thủy tinh đựng một ngàn ngôi sao giấy trong tay, nhìn bóng lưng cao lớn của Thẩm Dục Trì đang thu dọn hành lý chuẩn bị rời khỏi thành phố, nước mắt cô tuôn rơi như mưa: 'Thẩm Dục Trì... Anh sắp đi thật rồi sao? Vậy còn lời hứa đợi em ở cánh cổng trường đại học thì sao hả anh?!'"""

    part2_body = """Sân bay quốc tế Nam Giang mùa thu năm ấy chìm trong màn mưa phùn ảm đạm và tiếng loa phát thanh vang lên dồn dập báo hiệu chuyến bay đi Frankfurt chuẩn bị cất cánh. 

Khương Ninh đứng lẫn trong dòng người tấp nập, hai bàn tay buốt cóng ôm chặt chiếc hộp quà nhỏ bọc giấy hoa màu tím nhạt. Thẩm Dục Trì kéo chiếc vali đen bước đi giữa đám đông, vóc dáng cao ráo nổi bật giữa biển người. Trước khi bước qua cửa kiểm soát an ninh, anh bỗng dừng bước, quay đầu nhìn quanh như đang tìm kiếm một bóng hình quen thuộc.

Khương Ninh vội vã nép mình sau cây cột bê tông lớn, cắn chặt môi để không bật ra tiếng nấc nghẹn ngào. Cô không dám bước ra đối diện với anh, bởi cô sợ mình sẽ yếu đuối mà van xin anh ở lại, sợ rằng thứ tình cảm đơn phương vụng trộm của mình sẽ trở thành gánh nặng cản trở bước chân tương lai xán lạn của người con trai cô yêu hơn cả sinh mạng. Chiếc móc khóa cỏ bốn lá bằng bạc đan tay – kỷ vật cô chuẩn bị suốt ba tháng ròng – cuối cùng chỉ có thể nhờ anh trai chuyển giao lại cho Thẩm Dục Trì dưới danh nghĩa "món quà may mắn từ em gái nhỏ".

Bốn năm đằng đẵng trôi qua như một cái chớp mắt của thời gian. 

Khương Ninh mười tám tuổi ngây thơ ngày nào giờ đây đã trở thành một cô sinh viên năm cuối xuất sắc của Học viện Báo chí và Truyền thông Nghi Sơn. Cô gái nhỏ cắt tóc ngắn ngang vai, khoác trên mình chiếc áo măng tô màu be trang nhã, đôi mắt trong veo phản chiếu nét điềm đạm và trưởng thành của một người con gái từng đi qua bão giông ký ức.

Suốt bốn năm đại học, Khương Ninh từ chối mọi lời tán tỉnh của những chàng nam sinh hào hoa trong trường. Trong góc sâu thẳm nhất của trái tim cô, vị trí duy nhất ấy vẫn mãi mãi chỉ thuộc về chàng trai với mùi hương bạc hà thanh mát năm mười tám tuổi. Cô lao đầu vào học tập, làm thêm tại các tòa soạn báo, đi thực tế tại các vùng sâu vùng xa, tất cả chỉ để bản thân bận rộn đến mức không còn thời gian để đau lòng mỗi khi nhớ về một người ở cách xa nửa vòng trái đất.

Bốn năm xa cách đằng đẵng ở hai phương trời cách biệt, mỗi lần gió mùa đông bắc tràn về thành phố Nghi Sơn, lòng Khương Ninh lại dấy lên một nỗi nhớ cồn cào da diết. Cô nhớ những ngày tháng ngồi sau xe đạp của Thẩm Dục Trì, gió mùa hạ thổi bay tà áo trắng đồng phục, tiếng cười nói giòn tan rải rác khắp những con ngõ rợp bóng cây long não. 

Ở nước Đức xa xôi tuyết trắng phủ đầy, Thẩm Dục Trì cũng chưa từng có lấy một ngày quên đi hình bóng cô em gái nhỏ với đôi mắt trong veo như làn nước mùa thu. Chiếc móc khóa cỏ bốn lá bằng bạc mà Khương Ninh gửi tặng luôn được anh nâng niu treo ở ngăn kéo bàn làm việc. Mỗi đêm thức trắng trong phòng thí nghiệm kiến trúc, nhìn chiếc móc khóa nhỏ lấp lánh dưới ánh đèn bàn, anh lại mỉm cười tự nhủ phải nỗ lực hoàn thành sớm chương trình nghiên cứu sinh để trở về. Anh muốn trở về bên cô bé ấy, muốn tự tay che chở cho cô qua những giông bão của cuộc đời bằng chính đôi vai vững chãi của một người đàn ông trưởng thành.

Khoảnh khắc định mệnh nơi con hẻm phủ đầy tuyết trắng đêm đông hôm ấy không phải là một sự trùng hợp ngẫu nhiên của số phận. Đó là kết quả của hàng trăm ngày tìm kiếm, dò hỏi tin tức từ anh trai Khương Ninh của Thẩm Dục Trì. Vừa đáp chuyến bay xuống sân bay quốc tế lúc mười giờ đêm, anh thậm chí còn chưa kịp về khách sạn nghỉ ngơi mà đã vội vã lái xe lao thẳng đến tòa soạn báo nơi cô đang thực tập chỉ để được nhìn thấy cô một lần sau bao năm xa cách nghìn trùng!

Vào một đêm mùa đông tuyết rơi dày đặc trên những con phố cổ Nghi Sơn, Khương Ninh tăng ca hoàn thành phóng sự điều tra tại một quán cà phê đến tận một giờ sáng. Khi cô bước ra khỏi con hẻm vắng để tiến về phía trạm xe điện ngầm thì bất ngờ bị hai kẻ say rượu bám theo buông lời trêu ghẹo. Khương Ninh hoảng sợ lùi dần vào góc tường, chiếc túi xách bị giật rơi xuống mặt tuyết trắng xóa. 

Giữa lúc cô tuyệt vọng chuẩn bị bấm số gọi cảnh sát khẩn cấp thì một chiếc xe ô tô xé toạc màn đêm bão tuyết lao vụt tới, phanh két một tiếng ngay sát lề đường!

Cánh cửa xe bật mở, một người đàn ông mặc chiếc áo khoác dạ đen cao cấp bước xuống với phong thái đĩnh đạc và ánh mắt cương nghị. Dưới ánh đèn đường vàng nhạt, gương mặt góc cạnh sắc sảo cùng đôi mắt hoa đào sâu thẳm quen thuộc bỗng chốc đập vào mắt Khương Ninh khiến toàn bộ hơi thở trong lồng ngực cô như ngưng bặt! Là Thẩm Dục Trì! Anh đã trở về từ Đức từ khi nào mà cô không hề hay biết?!

Thẩm Dục Trì nhanh chóng bước tới, một tay kéo Khương Ninh ra sau lưng che chắn, ánh mắt lạnh lùng quét qua hai kẻ say rượu khiến bọn chúng hoảng sợ lùi bước rồi bỏ chạy mất dạng vào bóng đêm. Anh quay lại nhìn Khương Ninh, nhìn đôi bàn tay run rẩy vì lạnh và chóp mũi đỏ ửng của cô, trong đáy mắt anh dâng lên một sự xót xa vô bờ bến."""

    part2_cliff = """Thẩm Dục Trì cởi chiếc khăn choàng len ấm áp trên cổ mình cẩn thận quấn quanh cổ Khương Ninh, bàn tay ấm áp của anh khẽ nâng cằm cô lên, giọng nói trầm khàn đầy xót xa vang lên giữa cơn mưa tuyết: 'Khương Ninh... Em trốn anh suốt bốn năm trời, em có biết anh tìm em cực khổ đến mức nào không?!'"""

    part3_body = """Giữa màn mưa tuyết lạnh buốt của đêm đông Nghi Sơn, hơi ấm từ chiếc khăn choàng len và bàn tay của Thẩm Dục Trì như một ngọn lửa sưởi ấm toàn bộ tâm hồn băng giá của Khương Ninh. 

Cô đứng chết trân tại chỗ, hai hàng nước mắt nóng hổi bỗng chốc vỡ òa tuôn rơi không sao kìm nén nổi. Bốn năm kìm nén, bốn năm che giấu và chôn chặt nỗi nhớ nhung vào tận đáy lòng, giờ đây khi người con trai ấy bằng xương bằng thịt đứng ngay trước mắt, mọi bức tường phòng bị của cô bỗng chốc sụp đổ hoàn toàn.

Thẩm Dục Trì không nói thêm một lời nào, anh dang rộng vòng tay ôm chặt lấy Khương Ninh vào lòng. Chiếc áo khoác dạ dày dặn của anh chắn trọn từng cơn gió tuyết gầm rú ngoài kia. Anh vỗ nhẹ lên lưng cô, cằm tựa vào đỉnh đầu cô, giọng nói nghẹn ngào rung lên từng chặp:

"Đừng khóc nữa, anh về rồi... Từ nay về sau, anh sẽ không bao giờ để em phải một mình đối mặt với hiểm nguy hay cô đơn nữa đâu."

Đêm hôm ấy, anh đưa cô về căn hộ chung cư ấm cúng của mình. Anh tự tay pha cho cô một ly sữa nóng mật ong thơm lừng, bật lò sưởi ấm áp rồi ngồi đối diện ngắm nhìn cô uống từng ngụm nhỏ. Căn phòng yên tĩnh chỉ còn lại tiếng tuyết rơi lộp độp bên ngoài ô cửa kính.

Khương Ninh nhìn quanh căn phòng, bỗng ánh mắt cô dừng lại trên chiếc bàn làm việc gần cửa sổ. Ở đó, chiếc móc khóa cỏ bốn lá bằng bạc đan tay cũ kỹ năm nào được treo cẩn thận ngay bên cạnh chiếc đèn bàn, sáng bóng như vừa được lau chùi mỗi ngày. Và bên cạnh chiếc móc khóa là một chiếc lọ thủy tinh lớn... chứa đầy những ngôi sao giấy may mắn màu hồng mà cô từng ngỡ đã thất lạc năm mười tám tuổi!

"Anh... chiếc lọ ngôi sao này..." - Khương Ninh nghẹn ngào chỉ tay về phía chiếc lọ, giọng run rẩy không thốt nên lời.

Thẩm Dục Trì bước lại gần, mỉm cười dịu dàng:

"Mùa hè năm ấy, trước khi ra sân bay, anh đã quay lại nhà em. Anh trai em đã đưa cho anh chiếc lọ này cùng cuốn nhật ký mà em để quên trên bàn học. Khương Ninh... em có biết khi đọc từng trang nhật ký của em, anh đã tự trách bản thân mình nhiều đến mức nào không? Anh trách mình quá vô tâm, trách mình không nhận ra tình cảm của cô bé ngốc nghếch luôn lén nhìn anh sau rèm cửa sớm hơn. Nhưng lúc đó, gia đình anh gánh khoản nợ lớn, anh sang Đức với hai bàn tay trắng, anh không dám hứa hẹn bất cứ điều gì vì sợ làm lỡ dở tương lai của em..."

Anh quỳ một bên gối xuống trước mặt Khương Ninh, nắm chặt lấy hai bàn tay nhỏ bé của cô đặt lên lồng ngực mình nơi trái tim đang đập rộn ràng:

"Bốn năm qua ở Đức, anh làm việc ngày đêm không ngừng nghỉ, chỉ mong sớm trả hết nợ và tạo dựng được sự nghiệp vững chắc để có thể đường hoàng quay về tìm em. Anh đã từ chối mọi cơ hội định cư ở châu Âu, bởi vì ở nơi đó... không có người con gái anh yêu nhất trần đời!"

Những giọt nước mắt hạnh phúc lăn dài trên khóe mi Khương Ninh. Mười năm thanh xuân, từ một hạt mầm thầm kín dưới bóng râm cây long não thuở thiếu thời, vượt qua bão giông và khoảng cách địa lý nghìn trùng, tình yêu ấy cuối cùng đã đơm hoa kết trái ngọt ngào nhất.

Những tia nắng ban mai dịu dàng xuyên qua rèm cửa sổ, chiếu rọi lên hai chiếc nhẫn cưới bằng bạch kim lấp lánh đặt cạnh nhau trên bàn. Mười năm thanh xuân trôi qua như một cái chớp mắt, từ cô bé mười lăm tuổi rụt rè đứng khóc bên bờ hồ năm nào cho đến người phụ nữ hạnh phúc rạng ngời ngày hôm nay. 

Thẩm Dục Trì từ phía sau nhẹ nhàng ôm lấy eo Khương Ninh, cằm tựa lên bờ vai thon thả của cô, hơi thở ấm áp phả nhẹ bên vành tai: "Em có biết điều anh hối hận nhất trong mười năm qua là gì không?". 

Khương Ninh chớp chớp mắt quay lại nhìn anh: "Là gì hả anh?". 

Thẩm Dục Trì mỉm cười, đôi mắt hoa đào tràn ngập tình yêu thương sâu thẳm: "Anh hối hận vì đã để em phải vụng trộm thích thầm anh quá lâu. Đáng lẽ ra... anh phải là người tỏ tình trước mới đúng!"

Hạnh phúc đích thực trong cuộc đời này đôi khi không cần phải tìm kiếm đâu xa xôi. Nó nằm ngay trong sự kiên định của hai trái tim luôn hướng về nhau qua bao thăng trầm năm tháng. Mối tình thầm kín dưới mái hiên mùa hạ năm ấy, cuối cùng đã viết nên bản tình ca trọn vẹn và rực rỡ nhất cuộc đời!"""

    return {
        "title": story_title,
        "parts": [
            {
                "part_number": 1,
                "badge_label": "Tập 1",
                "title": f"{story_title} - Phần 1",
                "hook": "Khoảnh khắc anh Dục Trì lội xuống đầm nước vớt cặp sách và đưa cho tôi viên kẹo bạc hà, trái tim mười lăm tuổi đã lỡ một nhịp!",
                "body": part1_body,
                "cliffhanger": part1_cliff,
                "call_to_action": "Bấm theo dõi kênh để lắng nghe tiếp bản tình ca thanh xuân ở Tập 2 nhé!",
                "full_text": f"{part1_body}\\n\\n{part1_cliff}\\n\\nBấm theo dõi kênh để lắng nghe tiếp bản tình ca thanh xuân ở Tập 2 nhé!"
            },
            {
                "part_number": 2,
                "badge_label": "Tập 2",
                "title": f"{story_title} - Phần 2",
                "hook": "Bốn năm xa cách nghìn trùng, cuộc hội ngộ định mệnh giữa đêm đông tuyết trắng và chiếc khăn choàng ấm áp!",
                "body": part2_body,
                "cliffhanger": part2_cliff,
                "call_to_action": "Tập cuối sẽ là hồi kết ngọt ngào nhất, đừng quên thả tim và follow nhé!",
                "full_text": f"{part2_body}\\n\\n{part2_cliff}\\n\\nTập cuối sẽ là hồi kết ngọt ngào nhất, đừng quên thả tim và follow nhé!"
            },
            {
                "part_number": 3,
                "badge_label": "Tập 3 (Hồi Kết)",
                "title": f"{story_title} - Tập Cuối",
                "hook": "Bí mật chiếc lọ một ngàn ngôi sao giấy được mở ra và lời tỏ tình ngọt ngào sau mười năm chờ đợi!",
                "body": part3_body,
                "cliffhanger": "Mười năm thanh xuân trọn vẹn!",
                "call_to_action": "Bạn có từng thích thầm ai trong những năm tháng thanh xuân chưa? Hãy để lại bình luận chia sẻ nhé!",
                "full_text": f"{part3_body}\\n\\nBạn có từng thích thầm ai trong những năm tháng thanh xuân chưa? Hãy để lại bình luận chia sẻ nhé!"
            }
        ]
    }
'''

Path("core/stories/school_romance_vungtrom_masterpiece.py").write_text(content, encoding="utf-8")
print("Clean rewrite of school_romance_vungtrom_masterpiece.py successful!")
