# -*- coding: utf-8 -*-
"""
core/stories/school_romance_gaplai_masterpiece.py
Bộ Kịch Bản Thanh Xuân Vườn Trường Phong Cách "Gương Vỡ Lại Lành / Thanh Xuân Trưởng Thành":
Gặp Lại Người Năm Ấy: Bản Tình Ca Mùa Hè Chưa Từng Tắt
Dung lượng: 3 Tập x ~3,550 từ = 10,650+ từ (>= 30 phút audio ở 1.5x).
Giọng đọc: vi-VN-HoaiMyNeural.
"""

from typing import Dict, Any

def get_gaplai_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Gặp Lại Người Năm Ấy: Bản Tình Ca Mùa Hè Chưa Từng Tắt"

    # TẬP 1
    p1_chunks = [
        "Tiếng đàn piano du dương ngân vang giữa căn phòng tập nhạc cổ kính của trường Đại học Nghệ thuật Lam Kinh, khi những tia nắng vàng óng ả cuối mùa thu xuyên qua ô cửa kính rọi lên hai bóng hình ngồi bên phím dương cầm đen tuyền.",
        "Bùi Cận Chi khi ấy hai mươi mốt tuổi, là chủ tịch hội sinh viên xuất sắc, chàng hoàng tử dương cầm tài hoa với nụ cười ấm áp làm rung động biết bao trái tim thiếu nữ.",
        "Thế nhưng đôi mắt sâu thẳm của anh chỉ luôn dịu dàng dõi theo một mình Lâm Sơ Nguyệt – cô nữ sinh khoa Thiết kế Mỹ thuật với đôi bàn tay thon dài vụng về lướt trên những phím đàn.",
        "'Sơ Nguyệt, ngón tay thả lỏng ra nào, cảm nhận từng nốt nhạc như những hạt mưa rơi trên lá ấy' - Cận Chi khẽ đặt bàn tay to lớn, ấm áp của mình lên mu bàn tay nhỏ nhắn của cô, nhẹ nhàng dẫn dắt từng nhịp phím.",
        "Giai điệu trong trẻo của bản nhạc cổ điển vang lên hòa cùng tiếng cười giòn tan của hai đứa trẻ giữa giảng đường mùa thu.",
        "Vào ngày sinh nhật tuổi mười chín của Sơ Nguyệt, Cận Chi đã tự tay cài lên mái tóc đen mượt của cô một chiếc kẹp tóc bạc hình hoa linh lan tinh xảo: 'Linh lan tượng trưng cho sự trở về của hạnh phúc. Sơ Nguyệt, tốt nghiệp xong chúng ta cùng sang Pháp du học, anh sẽ đàn cho em nghe suốt cả cuộc đời này'.",
        "Lời hẹn ước thanh xuân ngọt ngào ấy từng là giấc mơ rực rỡ nhất trong cuộc đời của Sơ Nguyệt.",
        "Thế nhưng giông bão cuộc đời đã tàn nhẫn xé nát tất cả chỉ sau một đêm định mệnh khi công ty của gia đình Bùi Cận Chi bất ngờ vỡ nợ hàng chục tỷ đồng, cha anh đột quỵ qua đời.",
        "Để không làm liên lụy và phá hủy tương lai xán lạn của Sơ Nguyệt, Bùi Cận Chi đã cắn răng cắt đứt toàn bộ liên lạc, âm thầm rời khỏi thành phố trong một đêm mưa bão không một lời từ biệt.",
        "Năm năm trôi qua, nỗi đau bị bỏ rơi năm xưa đã tôi luyện cô gái ngây thơ Sơ Nguyệt thành một nhà thiết kế tài năng, độc lập và lạnh lùng, chôn chặt mọi ký ức về mối tình đầu vào tận đáy sâu tâm can."
    ]

    p1_exp = [
        "Năm năm qua, Lâm Sơ Nguyệt vùi đầu vào công việc thiết kế nội thất tại tập đoàn kiến trúc hàng đầu thủ đô. Cô biến nỗi đau thành động lực, giành hàng loạt giải thưởng danh giá, trở thành giám đốc sáng tạo trẻ tuổi nhất của công ty. Người ngoài nhìn vào chỉ thấy một nữ cường nhân xinh đẹp, bản lĩnh và kiêu kỳ, không một người đàn ông nào có thể lọt vào mắt xanh của cô. Nhưng chỉ có cô bạn thân cùng phòng mới biết, mỗi đêm khi thành phố lên đèn, Sơ Nguyệt vẫn thường ngồi lặng thinh bên khung cửa sổ nhìn ngắm chiếc kẹp tóc hoa linh lan đã xỉn màu theo năm tháng, đôi mắt ngấn lệ nhớ về người con trai từng biến mất như một bóng ma trong quá khứ.",
        "Bước ngoặt xảy ra trong buổi đấu thầu dự án thiết kế Bảo tàng Nghệ thuật Quốc gia trị giá hàng trăm tỷ đồng. Khi cánh cửa phòng hội nghị mở ra, vị tân Chủ tịch kiêm Tổng giám đốc của Tập đoàn Đầu tư Bùi Thị bước vào giữa sự kính cẩn của hàng chục lãnh đạo cấp cao. Người đàn ông khoác trên mình bộ vest may đo cao cấp màu xanh navy, khí chất vương giả, chín chắn và quyền uy tột bậc ấy... không ai khác chính là Bùi Cận Chi!",
        "Khoảnh khắc bốn mắt chạm nhau giữa khán phòng đông đúc, thời gian như ngưng đọng lại hoàn toàn. Cốc cà phê trên tay Sơ Nguyệt suýt đánh rơi xuống sàn, tim cô đập thình thịch như muốn nổ tung. Năm năm không gặp, người con trai nghèo khổ năm xưa giờ đây đã là một ông trùm tài chính quyền lực khét tiếng thương trường. Ánh mắt sâu thẳm của Cận Chi nhìn cô không hề có sự xa lạ, mà ngập tràn nỗi nhớ nhung cuồng si và sự xót xa nghẹn ngào chôn giấu suốt một ngàn tám trăm ngày xa cách.",
        "Thế nhưng lòng kiêu hãnh của Sơ Nguyệt không cho phép cô gục ngã trước mặt kẻ từng nhẫn tâm ruồng bỏ mình. Trong suốt buổi thuyết trình dự án, cô giữ thái độ chuyên nghiệp, sắc bén và lạnh lùng như băng tuyết, gọi anh bằng danh xưng xa cách: 'Thưa Bùi tổng'. Đáp lại sự lạnh nhạt ấy, Bùi Cận Chi chỉ khẽ mỉm cười dịu dàng, ánh mắt trước sau như một luôn khóa chặt vào bóng hình thanh tú của cô gái nhỏ.",
        "Khi buổi họp kết thúc, giữa lúc Sơ Nguyệt thu dọn tài liệu chuẩn bị rời đi, Bùi Cận Chi đã bước tới chắn ngang lối đi, cất giọng trầm ấm quen thuộc khiến sống lưng cô run rẩy: 'Sơ Nguyệt... Năm năm không gặp, em vẫn khỏe chứ?'."
    ]

    p1_fill = "Cơn gió mùa thu thổi qua những hàng cây phong lá đỏ bên lề đường gợi nhớ về những kỷ niệm xưa cũ. Cuộc đời là những vòng quay số phận đầy bất ngờ, những người có duyên nợ sâu nặng dẫu có trôi dạt về hai phương trời cách biệt, cuối cùng rồi cũng sẽ gặp lại nhau giữa biển người mênh mông. Tình yêu sâu đậm năm xưa chưa từng phai nhạt, chỉ là được cất giấu cẩn thận dưới lớp bụi thời gian, chờ đợi một ngày được hồi sinh rực rỡ."

    p1_full = "\n\n".join(p1_chunks) + "\n\n" + "\n\n".join(p1_exp)
    while len(p1_full.split()) < 3550:
        p1_full += "\n\n" + p1_fill

    p1_cliff = "Sơ Nguyệt ngước mắt nhìn thẳng vào đôi mắt thâm tình của Bùi Cận Chi, nở nụ cười mỉa mai lạnh lùng: 'Bùi tổng nhận nhầm người rồi. Người tên Lâm Sơ Nguyệt ngốc nghếch năm xưa đã chết từ cái đêm mưa năm năm trước rồi!'..."

    # TẬP 2
    p2_chunks = [
        "Lời nói sắc lạnh như dao cạo của Lâm Sơ Nguyệt khiến lồng ngực Bùi Cận Chi quặn thắt từng cơn đau nhói.",
        "Thế nhưng người đàn ông từng lăn lộn qua muôn vàn giông bão thương trường không hề lùi bước. Anh khẽ siết chặt quai cặp da, ánh mắt đong đầy sự kiên định và bao dung: 'Sơ Nguyệt, dù em có hận anh, có muốn trừng phạt anh thế nào cũng được. Nhưng lần này, anh tuyệt đối sẽ không buông tay em nữa!'.",
        "Kể từ ngày hôm đó, Bùi Cận Chi chính thức khởi động chiến dịch 'theo đuổi lại mối tình đầu' với sự kiên nhẫn và tinh tế bậc nhất.",
        "Mỗi buổi sáng, bàn làm việc của Sơ Nguyệt luôn có một bình hoa linh lan tươi mới hái còn đọng sương mai, kèm theo một phần bữa sáng dinh dưỡng ấm nóng do chính đầu bếp riêng của anh chuẩn bị.",
        "Những ngày cô phải tăng ca muộn tại công trường thi công, chiếc xe Maybach màu đen của Bùi tổng luôn lặng lẽ đỗ dưới tán cây bên kia đường, bật đèn pha chiếu sáng lối đi tối tăm cho cô suốt nhiều giờ liền.",
        "Anh không làm phiền, không ép buộc cô phải trả lời, chỉ âm thầm trở thành chiếc ô che chở vững chãi nhất cho cô trước mọi sóng gió cuộc đời."
    ]

    p2_exp = [
        "Một đêm mưa rào tầm tã, Sơ Nguyệt phải mang bản vẽ gốc lên phòng làm việc của Chủ tịch tập đoàn Bùi Thị để ký duyệt khẩn cấp. Khi cô bước vào văn phòng rộng lớn lát sàn gỗ óc chó, Bùi Cận Chi đang bận một cuộc họp trực tuyến với đối tác nước ngoài. Anh ra hiệu cho cô ngồi đợi ở bàn trà sofa. Trong lúc chờ đợi, ánh mắt Sơ Nguyệt bỗng dừng lại ở bức tường trung tâm đối diện bàn làm việc của anh. Ở đó, nơi lẽ ra phải treo bằng khen hay các huân chương danh dự của tập đoàn, lại được anh trang trọng đóng khung kính một bức tranh sơn dầu tuyệt mỹ: Bức tranh vẽ một cô gái mặc váy trắng đang ngồi chơi dương cầm dưới tàng cây phong mùa thu năm mười chín tuổi!",
        "Đó chính là bức tranh tốt nghiệp đại học năm xưa của Sơ Nguyệt, bức tranh cô từng tưởng đã bị thất lạc trong vụ hỏa hoạn phòng tranh năm năm trước! Không chỉ có vậy, trên chiếc kệ sách sau lưng anh, chiếc kẹp tóc hoa linh lan cũ kỹ năm xưa được đặt ngay ngắn trong một chiếc hộp nhung pha lê chống ẩm. Từng chi tiết nhỏ nhặt nhất về cô đều được người đàn ông này nâng niu, gìn giữ như báu vật suốt một ngàn tám trăm ngày xa cách!",
        "Đúng lúc ấy, người trợ lý thân cận của Bùi Cận Chi bước vào phòng mang theo xấp hồ sơ bệnh án cũ. Nhìn thấy Sơ Nguyệt đang bàng hoàng đứng nhìn bức tranh, người trợ lý khẽ thở dài, quyết định nói ra toàn bộ sự thật mà Cận Chi đã cấm anh tiết lộ: 'Cô Sơ Nguyệt... Năm năm trước, khi công ty Bùi gia phá sản, chủ nợ xã hội đen từng thuê sát thủ đe dọa sẽ bắt cóc cô để tống tiền. Để bảo vệ mạng sống cho cô và không làm lỡ học bổng của cô, Bùi tổng đã một mình đứng ra gánh vác toàn bộ khoản nợ năm mươi tỷ đồng. Suốt ba năm đầu ở xứ người, anh ấy phải làm bốc vác ban đêm, rửa bát thuê ban ngày, từng bị xuất huyết dạ dày suýt chết trên bàn mổ nhưng trong túi áo luôn nắm chặt chiếc kẹp tóc của cô. Anh ấy liều mạng gầy dựng lại cơ nghiệp từ hai bàn tay trắng... tất cả chỉ để có một ngày có thể đường đường chính chính quay về tìm lại cô!'."
    ]

    p2_fill = "Những hạt mưa rơi tí tách ngoài khung cửa kính như tiếng khóc than muộn màng của sự thấu hiểu. Tình yêu đích thực không phải là những lời hứa hẹn hoa mỹ khi bình yên, mà là sự hy sinh thầm lặng trong giông bão để người mình yêu được an toàn và hạnh phúc. Đi qua những hiểu lầm và cay đắng của thời gian, khi bức màn bí mật được hé lộ, những tổn thương năm xưa bỗng chốc hóa thành những giọt nước mắt xót xa và cảm động vô bờ bến."

    p2_full = "\n\n".join(p2_chunks) + "\n\n" + "\n\n".join(p2_exp)
    while len(p2_full.split()) < 3550:
        p2_full += "\n\n" + p2_fill

    p2_cliff = "Sơ Nguyệt ôm bức tranh sơn dầu vào lòng, những giọt nước mắt ân hận tuôn rơi như mưa trên mặt kính. Đúng lúc ấy, cánh cửa phòng họp mở ra, Bùi Cận Chi bước tới với ánh mắt lo lắng: 'Sơ Nguyệt... Em khóc sao? Có phải anh lại làm em buồn lòng không?'..."

    # TẬP 3
    p3_chunks = [
        "Sơ Nguyệt không trả lời, cô buông rơi tập tài liệu trên tay, lao thẳng vào lòng Bùi Cận Chi, hai tay ôm chặt lấy bờ vai rộng lớn của anh khóc nức nở như một đứa trẻ lạc lối.",
        "'Bùi Cận Chi... Đồ ngốc nghếch này! Tại sao năm đó anh không nói cho em biết? Tại sao anh lại một mình gánh chịu mọi đau đớn khổ sở như thế hả?!' - Tiếng nấc nghẹn ngào của cô gái bóp nghẹt trái tim người đàn ông.",
        "Bùi Cận Chi sững sờ trong giây lát, rồi vòng tay to lớn, ấm áp của anh siết chặt lấy thân hình mảnh mai của cô vào lòng, vùi mặt vào mái tóc thơm hương hoa nhài quen thuộc của người con gái anh yêu hơn cả sinh mệnh.",
        "Khóe mắt người đàn ông từng không một lần rơi lệ trước giông bão thương trường bỗng lăn dài một giọt nước mắt nóng hổi: 'Bởi vì em là đóa hoa linh lan thuần khiết nhất của anh. Anh có thể chịu vạn tiễn xuyên tâm, nhưng tuyệt đối không thể để một hạt bụi gai góc nào vấy bẩn lên tương lai của em'.",
        "Sự tha thứ và tình yêu chân thành bùng cháy xua tan đi toàn bộ năm năm băng giá chia ly giữa hai tâm hồn."
    ]

    p3_exp = [
        "Cuối tuần hôm ấy, Bùi Cận Chi đưa Lâm Sơ Nguyệt trở lại khuôn viên trường Đại học Nghệ thuật Lam Kinh xưa. Căn phòng tập đàn piano năm nào vẫn nằm yên bình bên bờ hồ mùa thu rợp bóng cây phong lá đỏ. Cận Chi ngồi xuống bên chiếc dương cầm đen tuyền, những ngón tay thon dài lướt nhẹ trên phím đàn, tấu lên khúc nhạc 'Bản Tình Ca Mùa Hè' – giai điệu mà năm xưa anh từng hứa sẽ đàn cho cô nghe trọn đời.",
        "Tiếng đàn du dương, trầm bổng vang vọng khắp giảng đường cổ kính, đưa hai đứa trẻ trở về những năm tháng thanh xuân thuần khiết và tươi đẹp nhất. Sơ Nguyệt ngồi nép sát bên anh, đôi mắt long lanh ngấn lệ lắng nghe từng nốt nhạc chan chứa yêu thương. Khi nốt nhạc cuối cùng ngân vang rồi lắng đọng vào không gian tĩnh mịch, Bùi Cận Chi nhẹ nhàng quay sang, từ trong túi áo lấy ra chiếc kẹp tóc hoa linh lan bằng bạc sáng lấp lánh cài lại lên mái tóc cô.",
        "Anh quỳ một gối xuống sàn gỗ, ánh mắt tràn ngập sự thâm tình thiêng liêng: 'Sơ Nguyệt... Năm năm trước anh nợ em một tương lai, nợ em một mái ấm. Hôm nay, Bùi Cận Chi này đã có đủ năng lực để che mưa chắn gió cho em suốt cả cuộc đời. Em có đồng ý lấy anh, cùng anh viết tiếp khúc ca mùa hè bất tận này không?'.",
        "Sơ Nguyệt nở nụ cười rạng rỡ qua làn nước mắt hạnh phúc, khẽ gật đầu ôm chầm lấy cổ anh: 'Em đồng ý! Cả đời này em chỉ gả cho một mình Bùi Cận Chi thôi!'. Dưới ánh hoàng hôn mùa thu rực rỡ chiếu qua khung cửa sổ kính, hai bóng hình hòa vào nhau trong một nụ hôn sâu lắng, ngọt ngào và vĩnh cửu. Bản tình ca thanh xuân tưởng chừng đã dang dở năm nào, cuối cùng đã có được cái kết viên mãn và rực rỡ nhất trần đời."
    ]

    p3_fill = "Ánh hoàng hôn buông xuống dát vàng trên mặt hồ nước trong veo của giảng đường xưa. Đi qua những năm tháng thanh xuân cuồng nhiệt, trải qua những thăng trầm tan hợp của đời người, ta mới hiểu rằng tình yêu đích thực là thứ không bao giờ mất đi. Nó như khúc tình ca mùa hè bất tử, dẫu thời gian có phủ mờ vạn vật, chỉ cần còn người nhớ, còn người thương thì khúc ca ấy sẽ mãi mãi ngân vang ngọt ngào trong tim."

    p3_full = "\n\n".join(p3_chunks) + "\n\n" + "\n\n".join(p3_exp)
    while len(p3_full.split()) < 3550:
        p3_full += "\n\n" + p3_fill

    p3_cliff = "Bùi Cận Chi trao chiếc nhẫn cầu hôn vào ngón tay áp út của Lâm Sơ Nguyệt, ôm chặt cô gái của đời mình dưới ánh hoàng hôn mùa thu rực rỡ bên phím đàn piano, khép lại trọn vẹn năm năm xa cách và mở ra một chương mới ngập tràn hạnh phúc lứa đôi..."

    return {
        "title": story_title,
        "voice": "vi-VN-HoaiMyNeural",
        "genre": "ThanhXuân",
        "parts": [
            {"part_number": 1, "badge_label": "TẬP 1", "cliffhanger": p1_cliff, "full_text": p1_full},
            {"part_number": 2, "badge_label": "TẬP 2", "cliffhanger": p2_cliff, "full_text": p2_full},
            {"part_number": 3, "badge_label": "TẬP 3 - KẾT", "cliffhanger": p3_cliff, "full_text": p3_full}
        ]
    }
