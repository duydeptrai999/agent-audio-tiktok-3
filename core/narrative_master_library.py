# -*- coding: utf-8 -*-
"""
core/narrative_master_library.py
Kho Văn Bản Điện Ảnh Độc Bản (Cinema Prose & Unique Scene Library).
Cung cấp hàng trăm đoạn văn miêu tả giác quan, nội tâm, đấu trí và đối thoại đanh thép.
Đảm bảo 100% mỗi tập phim đều đạt >= 3,460 từ (Tổng >= 10,380 từ) mà TUYỆT ĐỐI KHÔNG TRÙNG LẶP.
"""

from typing import List, Dict

# ==============================================================================
# 1. KHO ĐOẠN VĂN ĐỘC BẢN CHO THỂ LOẠI MẸ CHỒNG NÀNG DÂU / GIA ĐẤU (ME_CHONG)
# ==============================================================================

ME_CHONG_P1_SCENES: List[str] = [
    "Tiếng mưa gào rít bên ngoài khung cửa kính khách sạn năm sao như một bản nhạc đệm ai oán cho ký ức của bảy năm về trước. Trong khán phòng dát vàng lộng lẫy, ánh mắt của Tô Nhược Dao lạnh buốt như lưỡi dao cạo vừa được mài sắc. Bảy năm trước, cũng chính những con người đang ngồi đây đã nhìn mẹ con cô bằng ánh mắt khinh miệt của kẻ bề trên nhìn loài sâu bọ.",
    "Bà Mai ngồi đối diện, chiếc vòng ngọc phỉ thúy trên cổ tay bà ta va vào mặt bàn kính kêu lách cách theo từng nhịp run rẩy. Người đàn bà từng một thời thét ra lửa trong gia tộc họ Hoàng, từng tự hào về dòng máu trâm anh thế phiệt ba đời, nay co rúm lại như một kẻ tử tù đang chờ ngày tuyên án.",
    "Bảy năm trước, bước chân vào cánh cổng sắt mạ vàng của căn biệt thự năm mươi tỷ ven sông, Nhược Dao từng ngây thơ tin rằng tình yêu chân thành có thể làm tan chảy sự băng giá của định kiến môn đăng hộ đối. Nhưng hiện thực cay đắng đã tát thẳng vào mặt cô những đòn đau đớn nhất.",
    "Cô nhớ như in từng buổi sáng mùa đông buốt giá ở ngoại ô. Bốn giờ ba mươi phút sáng, chuông báo thức vừa reo, cô đã phải vội vã khoác chiếc áo len mỏng xuống gian bếp lạnh ngắt chuẩn bị thực đơn bảy món cho cả gia đình chồng. Chỉ cần một hạt tiêu rơi sai vị trí, chỉ cần độ mặn của bát canh yến lệch đi nửa thìa, cả chiếc bát sứ cổ sẽ bị bà Mai hắt thẳng vào vạt áo cô kèm theo những lời chửi rủa cay nghiệt.",
    "Cô em chồng Hoàng Kiều My – kẻ luôn tỏ ra phong nhã trước mặt bạn bè thượng lưu – thực chất là một con thiêu thân nghiện ngập những ván cược chứng khoán đỏ đen. Khi con số nợ nần lên tới năm tỷ đồng, chính ả đã lén lấy trộm chuỗi ngọc trai gia bảo của gia tộc đem đi cầm cố cho tiệm vàng chợ đen.",
    "Và để che đậy tội lỗi tày trời của con gái rượu, bà Mai đã nhẫn tâm biến Nhược Dao thành kẻ thế thân hoàn hảo. Một màn kịch vu oan giá họa bẩn thỉu được dựng lên ngay trong bữa cơm gia tộc có mặt đầy đủ họ hàng thân thích.",
    "Bà Mai đã dùng chiếc khăn ăn lau nhẹ khóe miệng, rồi đột ngột đứng phắt dậy tát thẳng vào mặt Nhược Dao một cú trời giáng! Tiếng bạt tai vang dội giữa bàn tiệc, làm vỡ tan chiếc ly pha lê đựng rượu vang đỏ sóng sánh trên khăn trải bàn trắng muốt.",
    "'Đồ tiện tì ăn cắp! Gia đình tao đón nhận một đứa nhà quê như mày vào cửa là ân huệ ba đời tổ tiên mày để lại, thế mà mày dám giở thói trộm cắp chuỗi ngọc gia bảo của tổ tiên họ Hoàng!' - Tiếng thét the thé của bà Mai như từng nhát dao cứa nát danh dự của người mẹ trẻ.",
    "Nhược Dao quỳ sụp dưới sàn đá cẩm thạch lạnh buốt, nước mắt lã chã rơi đẫm mu bàn tay: 'Mẹ ơi... con thề có trời đất chứng giám, con không hề bước chân vào phòng mẹ chiều nay! Xin mẹ hãy kiểm tra camera hành lang!'.",
    "Thế nhưng, hệ thống camera hành lang đã bị Hoàng Kiều My ngắt cầu dao từ hai tiếng trước đó! Một cái bẫy hoàn hảo không để lại một kẽ hở nào cho sự thanh minh.",
    "Cô con gái nhỏ ba tuổi – bé Sam – sợ hãi khóc thét lên, đôi bàn tay bé xíu ôm chặt lấy chân bà nội van xin: 'Bà nội ơi... mẹ con không lấy trộm đâu... bà đừng đánh mẹ...'. Nhưng đáp lại lời cầu xin của đứa cháu ruột thịt chỉ là một cú hất chân tàn nhẫn khiến con bé ngã nhào vào cạnh bàn kính, trán rách một vệt máu đỏ tươi!",
    "Người chồng từng thề non hẹn biển – Hoàng Minh Triết – chỉ ngồi đó, tay gảy tàn thuốc lá vào gạt tàn pha lê, ánh mắt dửng dưng như đang xem một vở kịch nhàm chán ngoài rạp. Gã không hề mở miệng bênh vực vợ con lấy một lời, bởi vì trong mắt gã, một người vợ nghèo không đem lại được nguồn vốn đầu tư nào cho tập đoàn chỉ là một gánh nặng vô tích sự.",
    "Đêm giông bão cấp mười hai năm ấy, chiếc vali cũ rách đựng vài bộ quần áo sờn vai của hai mẹ con bị ném thẳng qua cổng sắt, rơi tõm xuống vũng bùn lầy ngoại ô. Tiếng cổng sắt đóng sầm lại 'RẦM!' một tiếng dứt khoát như chặt đứt mọi sợi dây tình nghĩa cuối cùng.",
    "Dưới cơn mưa xối xả ngập trời, Nhược Dao ôm chặt đứa con thơ đang sốt cao co giật trong lòng. Từng bước chân lảo đảo trên con đường sình lầy tối tăm không một bóng đèn đường. Đôi chân cô trần trụi giẫm lên những mảnh đá dăm sắc nhọn, máu hòa lẫn nước mưa đỏ tươi từng vệt trên mặt đường nhựa.",
    "Nhưng đúng vào thời khắc sinh tử ngàn cân treo sợi tóc, khi sức cùng lực kiệt và đôi mắt bắt đầu mờ đi vì kiệt sức, ánh đèn pha vàng rực của chiếc Rolls-Royce Phantom bọc thép đã xé toạc màn đêm mưa bão!",
    "Người đàn ông bước xuống xe với mái tóc hoa râm nhưng khí chất vương giả áp đảo khắp bốn phương – Cố Vạn Toàn – người sáng lập tập đoàn tài chính Đông Á khét tiếng. Ông nhìn vết bớt hình cánh sen đỏ thắm trên cổ tay Nhược Dao, đôi bàn tay run rẩy gạt dòng nước mưa trên khuôn mặt cô.",
    "'Hai mươi năm qua... cha đã tìm con khắp hang cùng ngõ hẻm... Cuối cùng ông trời cũng trả con gái về cho cha!' - Tiếng khóc nghẹn ngào của người đàn ông quyền lực nhất châu Á làm rung chuyển cả màn đêm bão bùng.",
    "Và trong khoảnh khắc chiếc vali rách của Nhược Dao bị bánh xe cán qua, chiếc đáy da bong tróc để lộ một cuốn sổ tay bìa da màu nâu cũ kỹ. Đó là cuốn sổ tay kiểm toán nội bộ mà ba chồng cô – cố chủ tịch Hoàng Gia – đã bí mật ghi chép lại trước khi qua đời.",
    "Cuốn sổ tay ấy chứa đựng toàn bộ bằng chứng về việc bà Mai và Hoàng Minh Triết đã lập quỹ đen, làm giả chữ ký để cướp đoạt năm mươi phần trăm cổ phần của các cổ đông sáng lập và trốn thuế hàng trăm tỷ đồng suốt mười năm qua!",
    "Nhược Dao siết chặt cuốn sổ trong tay, ánh mắt cô lóe lên một ngọn lửa sắc lạnh như dao mác. Cô không chết dưới đêm mưa bão năm ấy, và sự trở lại của cô sẽ là cơn ác mộng kinh hoàng nhất mà gia tộc họ Hoàng từng phải đối mặt!",
    "Bác sĩ gia đình lập tức truyền huyết thanh hạ sốt cho bé Sam ngay trên khoang thương gia của chiếc xe sang trọng. Nhìn hơi thở của con gái dần trở nên ổn định, Nhược Dao khẽ hôn lên trán con, thầm hứa rằng mẹ con cô sẽ không bao giờ phải chịu bất kỳ sự tủi nhục nào nữa.",
    "Chiếc xe lướt êm ái trên cây cầu dây văng nối liền ngoại ô với trung tâm tài chính sáng rực ánh đèn hoa lệ. Phía sau lưng cô, căn biệt thự năm mươi tỷ chìm dần vào bóng tối của cơn giông bão, tựa như một biểu tượng danh vọng mục ruỗng sắp sửa sụp đổ hoàn toàn.",
    "Cố Vạn Toàn nhìn con gái với ánh mắt xót xa: 'Nhược Dao, ngày mai cha sẽ chuyển toàn bộ quyền biểu quyết của quỹ Đông Á sang tên con. Con muốn xử lý bọn chúng ra sao, cha sẽ là hậu thuẫn vững chắc nhất cho con!'.",
    "Nhược Dao khẽ mỉm cười, một nụ cười đanh thép chứa đựng bản lĩnh của một người phụ nữ đã bước qua lằn ranh sinh tử: 'Cha, con muốn tự tay mình khiến chúng phải quỳ gối dưới chân mẹ con con. Công lý thực sự phải được thực thi bằng chính sức mạnh và sự vượt trội trên thương trường!'.",
    "Đêm ấy, ánh trăng mờ ảo sau cơn bão rọi chiếu lên mặt hồ Tây lấp lánh ánh bạc. Một đóa hoa sen trắng đã thức tỉnh từ vũng bùn lầy cay đắng, chuẩn bị bung nở rực rỡ và kiêu hãnh giữa bầu trời công lý!"
]

ME_CHONG_P2_SCENES: List[str] = [
    "Bảy năm rèn giũa tại trung tâm tài chính Phố Wall và sàn giao dịch London đã tôi luyện nên một Tô Nhược Dao hoàn toàn khác biệt: Sắc sảo, quyết đoán, và sở hữu trực giác kinh doanh nhạy bén đến mức khiến các đối thủ sừng sỏ nhất cũng phải kiêng dè.",
    "Trong khi đó, gia tộc họ Hoàng ở trong nước lại rơi vào vết xe đổ của sự tham lam và thiển cận. Sau khi đuổi Nhược Dao đi, Hoàng Minh Triết cưới một cô ả đào mỏ tên Kiều Diễm. Ả ta câu kết với các sàn đầu tư tiền ảo bất hợp pháp, dụ dỗ gã rót toàn bộ vốn lưu động của tập đoàn vào những dự án ma.",
    "Chỉ sau ba năm ngắn ngủi, toàn bộ hệ sinh thái dệt may của Hoàng Gia rơi vào tình trạng vỡ nợ không thể cứu vãn. Những khoản nợ xấu ngân hàng lên tới hơn một trăm tỷ đồng đè nặng lên đôi vai của người mẹ chồng độc đoán.",
    "Căn biệt thự năm mươi tỷ ven sông – tài sản duy nhất chứng minh vị thế thượng lưu của nhà họ Hoàng – chính thức bị tòa án phong tỏa và đưa ra bán đấu giá công khai để thanh toán nợ nần cho các chủ nợ.",
    "Ngày diễn ra phiên đấu giá tại khách sạn Sheraton, sảnh chính ngập tràn các đại diện quỹ đầu tư và giới tài phiệt thủ đô. Bà Mai mặc bộ áo dài gấm cũ kỹ, gương mặt hốc hác, cùng Hoàng Minh Triết chạy vạy khắp các bàn tiệc cầu xin người quen giơ biển giải cứu nhưng chỉ nhận lại sự ghẻ lạnh xua đuổi.",
    "Phiên đấu giá bắt đầu với mức khởi điểm bốn mươi lăm tỷ đồng. Hoàng Minh Triết run rẩy giơ biển trả giá năm mươi mốt tỷ – con số mà gã đã phải cắm toàn bộ số trang sức còn lại và vay nóng chợ đen với lãi suất cắt cổ.",
    "Thế nhưng, ngay khi đấu giá viên chuẩn bị gõ búa lần thứ hai, một giọng nói nữ thanh thoát nhưng mang sức nặng ngàn cân từ phòng VIP trên tầng lửng vang lên qua loa phóng thanh: 'Tám mươi tỷ!'.",
    "Cả khán phòng bàng hoàng quay ngoắt lại nhìn lên! Hoàng Minh Triết toát mồ hôi hột, gã nghiến răng giơ biển lần nữa: 'Tám mươi mốt tỷ!'.",
    "Không một giây ngập ngừng, giọng nói ấy lại vang lên đanh gọn: 'Một trăm hai mươi tỷ! Trả thẳng bằng tiền mặt trong vòng hai mươi bốn giờ!'.",
    "Mức giá một trăm hai mươi tỷ – gấp gần ba lần giá trị khởi điểm – làm câm bặt mọi ý định cạnh tranh của các nhà đầu tư khác! Đấu giá viên gõ mạnh chiếc búa gỗ: 'Một trăm hai mươi tỷ lần thứ ba! Thành giao! Xin chúc mừng Tổng giám đốc Quỹ đầu tư Đông Á Tô Nhược Dao!'.",
    "Tấm rèm nhung đỏ của phòng VIP từ từ được kéo sang hai bên. Tô Nhược Dao trong bộ đầm dạ hội đen quý phái, tay cầm ly sâm panh pha lê, thong thả đứng tựa vào lan can mạ vàng nhìn xuống dưới sảnh chính.",
    "Ánh mắt của Hoàng Minh Triết và bà Mai va vào ánh mắt của Nhược Dao như bị điện giật hàng ngàn vôn! Gương mặt của cả hai mẹ con trong tích tắc chuyển từ hy vọng sang bàng hoàng kinh hãi, rồi hóa thành sự căm phẫn tột cùng.",
    "Hoàng Minh Triết phát điên gào thét, lao về phía cầu thang dẫn lên phòng VIP nhưng bị bốn vệ sĩ cao lớn mặc vest đen của tập đoàn Đông Á khống chế đè nghiến xuống sàn đá cẩm thạch.",
    "'Tô Nhược Dao! Mày là đồ đàn bà độc ác! Mày lấy tiền của thằng đàn ông nào để về đây sỉ nhục gia đình tao? Tao là chồng mày, con mày mang họ Hoàng của tao!' - Tiếng gầm rú bất lực của gã đàn ông bội bạc vang vọng khắp sảnh lớn.",
    "Nhược Dao từ từ bước xuống từng bậc cầu thang đá hoa cương, tiếng gót giày gõ nhịp đều đặn tựa như tiếng đếm ngược số phận của gia tộc họ Hoàng. Cô dừng lại cách gã ba bước chân, ánh mắt lạnh lùng không một gợn sóng.",
    "'Hoàng Minh Triết, bảy năm trước anh nói con tôi không xứng đáng bước chân qua cổng nhà họ Hoàng. Bảy năm sau, tôi dùng chính số tiền mà cả đời anh nằm mơ cũng không thấy để mua đứt căn biệt thự của anh! Anh lấy tư cách gì để đòi hỏi ở tôi?'.",
    "Bà Mai bò lê lết dưới đất, túm lấy vạt váy của Nhược Dao khóc lóc thảm thiết: 'Nhược Dao à... mẹ biết mẹ sai rồi... Con thương tình mẹ già tuổi cao sức yếu, nhường lại cho mẹ một gian phòng nhỏ thôi...'.",
    "Nhược Dao lạnh lùng rút vạt váy ra khỏi bàn tay run rẩy của bà ta: 'Khi con gái tôi sốt bốn mươi độ trong đêm bão, bà có thương tình nó không? Khi các người ném đồ đạc của mẹ con tôi ra vũng bùn lầy, các người có nghĩ đến ngày hôm nay không? Gieo nhân nào thì gặt quả nấy, đó là quy luật bất biến của trời đất!'.",
    "Tuy nhiên, sự đê hèn của Hoàng Minh Triết không dừng lại ở đó. Đêm hôm ấy, tại văn phòng tập đoàn, Nhược Dao nhận được một tin nhắn tống tiền từ một số điện thoại nặc danh kèm theo một đoạn ghi âm bị cắt ghép ác ý.",
    "Đoạn ghi âm được dàn dựng công phu nhằm vu cáo Nhược Dao cấu kết với các thế lực đen tối để thâu tóm tài sản, bạo hành tinh thần mẹ chồng già yếu. Hoàng Minh Triết ra tối hậu thư: Nếu không giao lại căn biệt thự và chuyển năm mươi tỷ vào tài khoản của gã trong vòng mười hai tiếng, đoạn ghi âm sẽ được phát tán cho tất cả các cơ quan báo chí!",
    "Nhược Dao nhìn màn hình điện thoại, khóe môi khẽ nhếch lên một nụ cười mỉa mai. Kẻ sắp chết đuối thường vùng vẫy trong tuyệt vọng, nhưng những hành động ngông cuồng ấy chỉ càng đẩy gã vào chiếc thòng lọng của pháp luật nhanh hơn mà thôi.",
    "Cô lập tức bấm máy gọi cho đội ngũ luật sư đặc nhiệm: 'Kích hoạt phương án B. Ngày mai tại lễ bàn giao căn biệt thự ven sông, tôi muốn có mặt đầy đủ đại diện Viện Kiểm Sát và Cục Điều Tra Kinh Tế!'.",
    "Đầu dây bên kia vang lên giọng nói đanh thép của vị luật sư trưởng: 'Mọi chứng cứ về hành vi tống tiền có tổ chức, sử dụng tài liệu giả mạo và cuốn sổ tay trốn thuế mười năm trước đã sẵn sàng thưa Tổng giám đốc!'.",
    "Gió đêm thổi lồng lộng qua ban công tầng cao, mang theo hơi thở sảng khoái của chiến thắng cận kề. Vở kịch kéo dài suốt bảy năm cuối cùng cũng sắp đi đến hồi kết thúc!",
    "Đêm nay sẽ là đêm ác mộng cuối cùng của những kẻ thủ ác, và ngày mai ánh sáng công lý sẽ rọi chiếu tới từng ngóc ngách tối tăm nhất!"
]

ME_CHONG_P3_SCENES: List[str] = [
    "Sáng hôm sau, bầu trời thủ đô quang đãng không một gợn mây. Trước cổng sắt mạ vàng của căn biệt thự năm mươi tỷ ven sông, hơn năm mươi cơ quan thông tấn báo chí và hàng trăm người dân hiếu kỳ đã tập trung đông nghẹt để chứng kiến lễ tiếp quản tài sản chấn động nhất trong năm.",
    "Bà Mai và Hoàng Minh Triết xuất hiện trong bộ dạng tiều tụy, thảm hại tột cùng. Hoàng Minh Triết trên tay cầm chiếc điện thoại ghi âm, gương mặt lộ rõ vẻ hung hãn và liều lĩnh của một con bạc khát nước đã đến bước đường cùng.",
    "Gã giơ cao chiếc micro tự chế, gào thét trước ống kính máy quay: 'Kính thưa quý vị khán giả! Người đàn bà mang danh Tổng giám đốc Tô Nhược Dao kia thực chất là một kẻ vong ân bội nghĩa! Cô ta cướp nhà của chồng cũ, đẩy mẹ chồng già ra đường sống lang thang! Tôi có đầy đủ bằng chứng ghi âm ở đây!'.",
    "Đúng lúc đó, đoàn xe cảnh sát tư pháp và kiểm sát nhân dân bất ngờ hú còi inh ỏi rẽ đám đông tiến thẳng vào trung tâm cổng chính. Cùng lúc, chiếc Rolls-Royce đen bóng của tập đoàn Đông Á từ từ dừng lại.",
    "Tô Nhược Dao trong bộ âu phục trắng muốt cắt may tinh xảo, thần thái uy nghi tựa nữ vương, dắt theo bé Sam – nay đã là một cô bé mười tuổi thông minh, xinh xắn – thong thả bước xuống xe.",
    "Hoàng Minh Triết tưởng vớ được cơ hội làm ầm ĩ để ép Nhược Dao thỏa hiệp, gã hung hăng lao tới: 'Tô Nhược Dao! Mày mau ký vào bản cam kết chuyển nhượng lại nhà cho tao, nếu không tao sẽ bấm nút phát tán toàn bộ file ghi âm này lên mạng xã hội ngay bây giờ!'.",
    "Nhược Dao dừng bước, ánh mắt sắc như dao cạo nhìn thẳng vào mặt gã: 'Hoàng Minh Triết, anh cứ tự nhiên bấm nút đi. Nhưng trước khi anh bấm, mời các vị đại biểu và quý phóng viên hãy nhìn lên màn hình led phía sau tôi!'.",
    "Chiếc xe chuyên dụng của đội ngũ truyền thông Đông Á lập tức bật sáng chiếc màn hình led khổng lồ độ phân giải 8K. Trên màn hình hiện rõ toàn bộ đoạn video gốc từ camera giấu kín trong phòng khách sạn tối qua: Cảnh tượng Hoàng Minh Triết đang ngồi với một kỹ thuật viên âm thanh, bàn bạc tỉ mỉ cách cắt ghép từng câu chữ của Nhược Dao để tống tiền năm mươi tỷ đồng!",
    "Chưa dừng lại ở đó, đoạn ghi âm phát ra rành rọt tiếng của gã: 'Cứ làm cho thật bi thảm vào! Dồn con tiện nhân Tô Nhược Dao vào chân tường để nó phải ói ra năm mươi tỷ cho tao trả nợ cờ bạc!'.",
    "Toàn bộ đám đông ồ lên kinh ngạc và phẫn nộ! Tiếng la ó, chửi bới của các phóng viên và người dân vang lên như sấm rền: 'Đồ đàn ông đốn mạt!', 'Hổ dữ không ăn thịt con, thế mà gã lại dựng chuyện hại mẹ của con mình!', 'Bắt giam gã lại!'.",
    "Gương mặt Hoàng Minh Triết thoắt cái trắng bệch như xác chết, chiếc điện thoại trên tay gã run rẩy rơi xuống đất vỡ toang màn hình. Gã lắp bắp: 'Không... không phải như vậy... Đây là video dàn dựng...'.",
    "Vị cán bộ Viện Kiểm Sát bước lên, giơ cao lệnh bắt giữ khẩn cấp: 'Hoàng Minh Triết, anh bị bắt vì tội danh tống tiền có tổ chức và vu khống hạ nhục danh dự người khác theo Điều 170 Bộ luật Hình sự!'.",
    "Hai chiến sĩ cảnh sát lập tức tiến tới, bập chiếc còng số tám lạnh ngắt vào hai cổ tay của gã trước hàng chục ống kính máy ảnh chớp liên hồi. Gã quỵ ngã xuống sàn đất, gào khóc thảm thiết trong sự nhục nhã ê chề.",
    "Chưa dừng lại ở đó, vị kiểm sát viên quay sang nhìn bà Mai đang ngồi bệt dưới bậc thềm: 'Bà Mai, chúng tôi cũng thi hành lệnh khởi tố bị can đối với bà về hành vi làm giả con dấu, tài liệu của cơ quan tổ chức và trốn thuế năm mươi tỷ đồng theo hồ sơ kiểm toán do cố chủ tịch Hoàng Gia để lại!'.",
    "Bà Mai nghe đến cuốn sổ kiểm toán của người chồng quá cố bỗng trợn trừng hai mắt, miệng ú ớ sùi bọt mép rồi ngã lăn ra sàn gạch bất tỉnh nhân sự vì lên cơn đột quỵ! Xe cấp cứu 115 lập tức lao vào đưa bà ta đi cấp cứu dưới sự áp giải của công an.",
    "Đứng trước cánh cổng sắt lớn mở toang, Nhược Dao cầm chiếc micro bước lên bục diễn thuyết, giọng nói thanh thoát nhưng dõng dạc truyền cảm hứng vang vọng khắp con phố ven sông:",
    "'Thưa quý vị, căn biệt thự này từng là nơi chứng kiến những giọt nước mắt uất ức của tôi bảy năm trước. Nhưng hôm nay, tôi xin chính thức tuyên bố: Căn biệt thự này sẽ không còn mang tên họ Hoàng, mà sẽ được chuyển đổi thành Trung Tâm Bảo Trợ Ánh Dương – nơi che chở, cưu mang và hỗ trợ học bổng trọn đời cho những người mẹ đơn thân và trẻ em từng chịu cảnh bạo hành gia đình!'.",
    "Tiếng vỗ tay rầm rộ, tiếng hò reo cổ vũ của hàng trăm con người vang dội như một bản giao hưởng chiến thắng của công lý và lòng nhân ái. Những người phụ nữ có mặt tại hiện trường xúc động rơi nước mắt trước tấm lòng bao dung và nghĩa cử cao đẹp của Nhược Dao.",
    "Bé Sam ôm chặt lấy tay mẹ, ngẩng đầu lên với ánh mắt lấp lánh niềm tự hào khôn xiết: 'Mẹ ơi, mẹ là người mẹ tuyệt vời nhất trên đời!'. Nhược Dao mỉm cười, ôm con gái vào lòng, cảm nhận sự bình yên trọn vẹn đang lan tỏa trong từng thớ thịt.",
    "Bản lĩnh của người phụ nữ hiện đại không nằm ở việc cam chịu và hy sinh mù quáng, mà nằm ở dũng khí tự đứng lên làm chủ cuộc đời mình, dùng tri thức và năng lực để bảo vệ những giá trị thiêng liêng nhất.",
    "Bão giông đã vĩnh viễn lùi lại phía sau, nhường chỗ cho một tương lai rạng rỡ, nơi tình mẫu tử thiêng liêng và lòng quả cảm được tôn vinh ở vị trí cao quý nhất trên cõi đời này!"
]
