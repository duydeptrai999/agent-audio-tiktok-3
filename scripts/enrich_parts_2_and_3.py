# -*- coding: utf-8 -*-
"""
scripts/enrich_parts_2_and_3.py
Bổ sung chiều sâu tâm lý và tình tiết đời thực cho Part 2 và Part 3 để đạt chuẩn >= 1.450 từ/tập.
"""

from pathlib import Path

target_file = Path("core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py")

part2_rich = """Câu hỏi của tôi rơi xuống giữa phòng khách như một gáo nước lạnh tạt thẳng vào mặt Thắng. 

Anh ta sững sờ mất vài giây. Liếc nhìn mẹ đẻ và vợ chồng cậu em họ đang trố mắt nhìn mình, cảm giác sĩ diện của một người đàn ông trụ cột bỗng chốc bị va đập dữ dội. Anh ta cau mày lại, gằn giọng tỏ vẻ bực bội: 

"Mai Chi, em ăn nói kiểu gì trước mặt mẹ và các em thế hả? Vợ chồng lấy nhau thì của chồng công vợ, anh là chủ cái gia đình này, chẳng lẽ anh không có quyền cho em trai anh ở nhờ vài ba tháng sao?".

Mẹ chồng tôi thấy con trai bị chạm nọc liền sấn tới ngay, ngón tay trỏ gầy guộc chỉ thẳng vào mặt tôi, giọng the thé chanh chua: 

"Chị nói thế mà nghe được à? Thằng Thắng nó là con trai trưởng của dòng họ Nguyễn này, nó lấy chị về thì cái nhà này là của hai vợ chồng nó. Chị vừa sinh con xong không lo giữ gìn sức khỏe, vừa về đến cửa đã so đo tính toán từng mét vuông nhà cửa với anh em ruột thịt. Đúng là đồ ích kỷ, bụng dạ hẹp hòi không biết trên dưới!".

Cô vợ của Dũng cũng bĩu môi hùa theo một cách trơ trẽn: 

"Đúng đấy chị dâu ạ, anh Thắng đi làm kiếm tiền nuôi cả cái nhà này, bọn em lên đây ở nhờ có mấy tháng mà chị làm như bọn em đi ăn cướp không bằng. Ở quê người ta đùm bọc nhau từng củ khoai củ sắn, lên thành phố người ta sống bạc bẽo ích kỷ thật đấy".

Tôi nghe từng lời từng chữ của bọn họ, trong lòng chỉ thấy buồn cười cho sự ảo tưởng nực cười và trơ trẽn đến mức khó tin này. Những con người này chưa từng đóng góp một xu cho căn nhà này, nhưng lại tự cho mình cái quyền phán xét và chiếm đoạt tài sản của người khác.

Tôi khẽ đặt chiếc túi bỉm sữa của con xuống chiếc tủ giày cạnh cửa, thong thả rút chiếc điện thoại trong túi xách ra. Tôi mở ứng dụng dữ liệu lưu trữ giấy tờ, mở file bản chụp màu có công chứng đỏ của Giấy chứng nhận quyền sở hữu nhà ở, giơ thẳng màn hình ra trước mặt Thắng và bà mẹ chồng.

"Anh Thắng đi làm kiếm tiền nuôi cả gia đình này sao? Ba năm qua, toàn bộ chi phí sinh hoạt của căn nhà này, từ tiền điện nước ba triệu mỗi tháng, tiền phí quản lý chung cư hai triệu, tiền mua sắm tivi tủ lạnh cho đến từng bữa ăn hàng ngày đều trừ thẳng vào tài khoản lương của tôi. Lương của anh mỗi tháng hai mươi lăm triệu, anh chuyển đều đặn cho mẹ mười lăm triệu gửi tiết kiệm ở quê, mười triệu còn lại anh tiêu xài cá nhân. Trong căn nhà này, ngoài mấy bộ quần áo công sở của anh ra, có cái bóng đèn hay viên gạch nào do tiền của anh mua không? Còn đây là sổ đỏ căn nhà, mời mẹ và các em nhìn cho thật kỹ xem có dòng chữ nào mang tên Nguyễn Văn Thắng không!".

Từng dòng chữ trên màn hình điện thoại hiện lên rõ mồn một từng chữ ký và con dấu đỏ chót của cơ quan quản lý đất đai: Chủ sở hữu duy nhất: Trần Thị Mai Chi. Thời điểm đăng ký quyền sở hữu: Hai năm trước ngày đăng ký kết hôn!

Sắc mặt của Thắng tái mét đi như người vừa bị đánh trúng tim đen. Anh ta lúng túng, hai bàn tay run run không dám chạm vào màn hình. Còn mẹ chồng tôi thì đực mặt ra, đôi mắt trừng trừng nhìn dòng chữ trên màn hình rồi lại quay sang nhìn con trai mình, miệng lắp bắp không nói nên lời.

Cậu em họ Dũng vội vàng rụt hai chân xuống khỏi bàn trà, vẻ mặt ngổ ngáo ban nãy bỗng chốc biến mất hoàn toàn, thay vào đó là sự bối rối và ngượng ngùng cùng cực trước người vợ đang ngơ ngác của mình.

Mẹ chồng tôi im lặng một lúc, nhưng bản tính cay nghiệt và tham lam đã ăn sâu vào máu khiến bà ta không dễ dàng chịu thua. Bà ta chống nạnh, giọng đanh lại đầy vẻ ngang ngược: 

"Sổ đỏ đứng tên chị thì đã sao? Chị lấy con trai tôi, thì chị là người nhà họ Nguyễn! Tài sản của chị cũng là của con trai tôi! Bây giờ chị vừa sinh con gái, không biết điều cung phụng nhà chồng thì sau này đừng hòng ai đỡ đần cho một tay. Tao bảo cho vợ chồng thằng Dũng ở phòng này là phải ở phòng này, chị không có quyền đuổi khách của con trai tao!".

Tôi cười nhạt, lấy tay lướt sang nhóm Zalo dòng họ Nguyễn mà mẹ chồng tôi vừa hớn hở nhắn tin từ sáng sớm. Trong nhóm, bà ta chụp ảnh toàn bộ phòng khách sang trọng của tôi kèm theo dòng tin nhắn khoe mẽ: "Nhà thằng Thắng trên Hà Nội rộng cả trăm mét vuông, tao vừa bảo nó nhường hẳn phòng ngủ đẹp nhất cho vợ chồng thằng Dũng ở rồi. Con cháu họ Nguyễn lên đây cứ yên tâm ăn ở không mất tiền trọ!".

Hóa ra là vì muốn nở mày nở mặt dưới quê, muốn chứng tỏ quyền lực của một bà mẹ chồng có con trai thành đạt, mà bà ta sẵn sàng giẫm đạp lên cuộc sống của chính người con dâu vừa sinh con nhỏ!

Tôi nhìn Thắng, người đàn ông đang cúi gằm mặt không dám nhìn thẳng vào tôi: 

"Thắng, anh giỏi lắm. Tiền lương của mình thì đem giấu kín gửi về quê cho mẹ, tiền của vợ thì đem ra hào phóng làm quà cho họ hàng để lấy danh tiếng. Anh có biết tiền sữa của con tháng trước anh còn bảo tôi tự chi vì anh hết tiền không? Giờ anh dám đem nhà của bố mẹ tôi cho để đi bao che cho thói phông bạt của gia đình anh à?".

Thấy mẹ mình làm càn, Thắng cũng lấy lại chút dũng khí giả tạo. Anh ta bước lại gần tôi, hạ giọng nhưng đầy vẻ đe dọa và áp đặt: 

"Mai Chi, em đừng làm mọi chuyện ầm ĩ lên nữa. Mẹ và các em vừa ở quê lên mệt mỏi, em nhường một bước thì chết ai à? Dù nhà này là của em, nhưng trên danh nghĩa anh là chồng em, em làm bẽ mặt anh trước mặt cả họ như thế, sau này em nhìn mặt bố mẹ anh thế nào?".

Tôi nhìn hai mẹ con họ, khóe môi khẽ nhếch lên thành một nụ cười khinh miệt sâu cay. 

"Tôi nhường một bước? Ba năm qua tôi nhường các người chưa đủ sao? Tôi nhường để mẹ anh coi tôi như người giúp việc không công, nhường để anh coi tiền bạc và công sức của tôi là điều hiển nhiên, nhường để các người dẫn cả họ hàng lên đây giẫm đạp lên đầu tôi ngay ngày tôi vừa sinh con sao?".

Tôi bấm loa ngoài điện thoại gọi thẳng cho bố chồng tôi đang ở dưới quê. Đầu dây bên kia vừa bắt máy, tiếng bố Thắng vang lên ân cần: "Chi à con, con và cháu đã về đến nhà chưa? Bố ở quê bận việc đồng áng không lên đón hai mẹ con được, bố áy náy quá".

Tôi giữ bình tĩnh, cất giọng rõ ràng: "Dạ bố, con vừa về đến nhà rồi ạ. Nhưng hiện tại mẹ và anh Thắng đang dọn toàn bộ đồ đạc của con ra ngoài phòng khách, để nhường phòng ngủ chính cho vợ chồng chú Dũng ở. Mẹ bảo con đẻ con gái nên không có quyền lên tiếng. Con gọi để thưa với bố một tiếng trước khi con nhờ ban quản lý và công an can thiệp ạ".

Đầu dây bên kia im bặt vài giây, rồi tiếng bố chồng tôi gầm lên giận dữ: "Bà Mai! Thằng Thắng! Chúng mày làm cái trò đồi bại gì đấy hả? Cái nhà đấy là của bố mẹ con Chi mua cho nó, chúng mày lấy quyền gì mà đuổi nó ra ngoài? Đứa nào cho phép vợ chồng thằng Dũng lên đấy làm loạn? Chúng mày dẹp ngay cái thói gia trưởng càn quấy ấy đi không thì đừng nhìn mặt tao nữa!".

Tiếng bố chồng quát qua điện thoại khiến bà Mai tái mét mặt mày, còn Thắng thì run rẩy lắp bắp: "Bố... bố hiểu lầm rồi... bọn con...".

Tôi tắt máy. Tôi quay sang nhìn thẳng vào mặt Dũng và cô vợ anh ta, giọng nói dứt khoát như đinh đóng cột: 

"Tôi cho hai người đúng mười lăm phút để thu dọn toàn bộ vali, quần áo và đồ đạc cá nhân ra khỏi căn nhà này. Nếu sau mười lăm phút các người chưa bước ra khỏi cửa, tôi sẽ gọi ban quản lý tòa nhà và công an phường đến lập biên bản về hành vi xâm nhập gia cư bất hợp pháp!".

"Chị... chị dám đuổi chúng tôi à?" - Cô vợ của Dũng thốt lên kinh ngạc, giọng run rẩy.

"Căn nhà này đứng tên tôi, tôi là chủ sở hữu hợp pháp duy nhất. Tôi không mời các người đến, và tôi có toàn quyền yêu cầu các người rời đi ngay lập tức. Đừng để tôi phải dùng biện pháp mạnh!".

Nói xong, tôi bế con gái quay người bước vào phòng ngủ của mình, đóng sầm cửa lại và khóa trái từ bên trong. Để lại ngoài phòng khách một khoảng không gian im bặt, ngột ngạt đến nghẹt thở."""

part3_rich = """Sau cánh cửa phòng ngủ đóng chặt, tôi nghe thấy tiếng cãi vã xôn xao bắt đầu bùng nổ ngoài phòng khách.

Tiếng bà mẹ chồng gào thét chửi bới con dâu ghê gớm, tiếng Thắng gắt gỏng phân bua trong bất lực, và tiếng lục đục kéo khóa vali vội vã của vợ chồng cậu em họ. Tôi không hề bận tâm. Tôi đặt con gái nằm ngay ngắn trên chiếc nệm êm ấm, lấy chiếc điện thoại ra và gọi thẳng cho ban quản lý tòa nhà.

"Alo, tôi là chủ căn hộ 1204. Hiện tại trong nhà tôi đang có một số người gây rối trật tự và hút thuốc lá bừa bãi làm kích hoạt chuông cảnh báo. Nhờ đội an ninh cử hai nhân viên lên hỗ trợ giải tỏa giúp tôi".

Chưa đầy mười phút sau, tiếng chuông cửa căn hộ reo vang, kèm theo giọng nói nghiêm nghị của nhân viên an ninh tòa nhà. 

Cánh cửa mở ra, hai bảo vệ vạm vỡ trong bộ đồng phục đứng trước cửa, yêu cầu tất cả những người không có tên trong danh sách đăng ký cư trú phải rời khỏi khu căn hộ để đảm bảo an ninh trật tự. 

Trước sự kiên quyết của ban quản lý và ánh mắt tò mò của những người hàng xóm xung quanh đang mở cửa nhìn sang, vợ chồng Dũng mặt cắt không còn giọt máu. Họ vội vàng xách hai chiếc vali lếch thếch bước vào thang máy, không dám ngoái đầu lại nhìn lấy một lần vì quá xấu hổ. Bấy giờ họ mới hiểu, cái mác "anh Thắng thành đạt" chỉ là vỏ bọc rỗng tuếch, còn người nắm giữ thực quyền chính là người chị dâu mà họ vừa tỏ thái độ khinh khi.

Còn mẹ chồng tôi, sau khi bị mất mặt ê chề trước bàn dân thiên hạ, liền lăn đùng ra sàn nhà ăn vạ, vừa đấm ngực thùm thụp vừa khóc lóc om sòm: 

"Trời ơi là trời! Nhà họ Nguyễn vô phúc rước phải thứ con dâu mất dạy, đuổi cả mẹ chồng ra đường thế này thì sống làm sao được nữa!".

Thắng đứng ở góc tường, hai mắt đỏ ngầu vì tức tối và xấu hổ tột độ. Anh ta lao đến trước cửa phòng ngủ của tôi, đập cửa rầm rầm: 

"Trần Thị Mai Chi, cô mở cửa ra! Cô làm nhục gia đình tôi trước mặt cả tầng như thế này mà cô coi được à? Hôm nay cô không quỳ xuống xin lỗi mẹ tôi thì cái nhà này tan nát!".

Tôi mở cửa phòng, thong thả bước ra ngoài. Tôi nhìn thẳng vào mắt anh ta, giọng nói bình thản đến lạnh lùng: 

"Anh muốn gia đình này tan nát sao? Được thôi, vậy thì giải tán!".

Tôi bước lại chiếc bàn trà, lấy ra một tập tài liệu mà tôi đã chuẩn bị kỹ càng từ trước ngày đi sinh. Đó là bản sao kê chi tiết tài khoản ngân hàng trong ba năm qua, ghi rõ từng khoản tiền sinh hoạt phí hàng tháng, và kèm theo một lá đơn ly hôn đã có sẵn chữ ký dứt khoát của tôi ở góc dưới.

Tôi đặt tập hồ sơ lên bàn, nhìn thẳng vào Thắng và bà mẹ chồng đang ngồi bệt dưới đất: 

"Ba năm qua, tổng số tiền tôi chi trả cho cuộc sống của gia đình này là hơn một tỷ hai trăm triệu đồng. Còn anh Thắng, mỗi tháng anh kiếm hai mươi lăm triệu, gửi về cho mẹ anh mười lăm triệu. Tính ra ba năm qua, mẹ đang giữ của anh ta hơn năm trăm triệu tiền tiết kiệm. Căn nhà này là tài sản riêng của tôi, anh ta không đóng góp một đồng nào. Đơn ly hôn tôi đã ký sẵn. Tôi cho anh đúng hai ngày để dọn toàn bộ đồ đạc cá nhân của anh ra khỏi căn nhà này!".

Mẹ chồng tôi nghe đến con số năm trăm triệu thì vội vàng nín bặt tiếng khóc, ánh mắt đảo lia lịa đầy vẻ hoảng hốt. Bà ta sợ tôi sẽ đòi lại số tiền đó để chia tài sản, liền vội vàng kéo tay con trai giục giã: 

"Thôi con ơi, cái thứ đàn bà ghê gớm, sắc sảo thế này nhà mình không chứa chấp nổi đâu. Đi về quê với mẹ, dưới quê thiếu gì đứa con gái ngoan ngoãn biết nghe lời!".

Nhưng Thắng thì không ngu ngốc đến mức đó. Anh ta nhìn lá đơn ly hôn trên bàn, rồi lại nhìn tập sao kê ngân hàng dày cộp, cả người anh ta run rẩy. Anh ta hiểu rất rõ, nếu ly hôn, anh ta sẽ mất trắng tất cả: mất một căn chung cư cao cấp ở trung tâm thành phố, mất một người vợ có học thức và thu nhập cao, và sẽ phải đối mặt với thực tế cuộc sống đắt đỏ trên thành phố bằng đồng lương ít ỏi còn lại của mình. Năm trăm triệu kia ở dưới quê thì to, nhưng trên thành phố này ngay cả một nửa mảnh đất cắm dùi cũng không mua nổi!

Anh ta quỳ sụp xuống trước mặt tôi, hai tay ôm lấy đầu gối tôi, giọng run rẩy van xin trong nước mắt: 

"Chi ơi, anh sai rồi! Là do anh nhu nhược, anh ngu muội nghe lời mẹ xúi giục, anh không biết bảo vệ em và con. Anh xin em, đừng ly hôn mà, cho anh một cơ hội sửa sai được không em? Từ nay tiền lương anh sẽ nộp hết cho em, mẹ anh anh sẽ bảo bà về quê ngay, không bao giờ để bà can thiệp vào chuyện nhà mình nữa!".

Bà mẹ chồng thấy con trai quỳ gối xin lỗi con dâu thì nhảy dựng lên như phải bỏng: "Mày làm cái gì thế hả Thắng? Đứng dậy ngay! Đàn ông đầu đội trời chân đạp đất, sao lại đi quỳ lạy cái thứ đàn bà đuổi mẹ đuổi em?".

Tôi nhìn người đàn ông đang quỳ dưới chân mình, trong lòng không hề có một chút xao động hay thương hại nào. Một người đàn ông đến danh dự của vợ con mình còn không bảo vệ nổi, vừa thấy khó khăn đã co vòi trốn tránh, đến khi mất quyền lợi mới vội vàng quỳ lạy van xin, thì không xứng đáng làm chồng, làm cha của con gái tôi.

"Cơ hội tôi đã cho anh suốt ba năm qua rồi. Ngày hôm nay, sự nhẫn nhịn của tôi đã cạn kiệt. Thu dọn đồ đạc đi, chúng ta gặp nhau ở tòa án!".

Hai ngày sau, Thắng lặng lẽ kéo vali rời khỏi căn nhà trong sự bẽ bàng tột cùng. Tôi lập tức liên hệ thợ khóa đến thay toàn bộ hệ thống khóa cửa vân tay và camera an ninh mới. 

Khi cánh cửa khép lại, tôi quay vào phòng, bế con gái nhỏ lên trong vòng tay ấm áp. Ánh nắng ban mai rọi qua khung cửa sổ phòng khách, chiếu sáng khắp căn phòng sạch sẽ và yên bình. 

Cuộc sống của mẹ con tôi từ nay sẽ bắt đầu một trang mới, không còn những toan tính đố kỵ, không còn những lời cay nghiệt của gia đình nhà chồng. Tôi có căn nhà của riêng mình, có sự nghiệp độc lập và có đủ tình yêu thương để nuôi nấng con gái trưởng thành một cách kiêu hãnh nhất.

Các bạn nghe câu chuyện của tôi, các bạn có nghĩ rằng phụ nữ khi bước vào hôn nhân, việc tự chủ kinh tế và dứt khoát bảo vệ ranh giới của bản thân là điều quan trọng nhất không?"""

# Read existing file to keep imports and structure
content = Path("core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py").read_text(encoding="utf-8")
part1_start = content.find('part1_full = """') + len('part1_full = """')
part1_end = content.find('"""\n\n    part2_full = """')
part1_text = content[part1_start:part1_end].strip()

code_content = f'''# -*- coding: utf-8 -*-
"""
core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py
Bộ Kịch Bản Audio Gia Đấu Đời Thực Triệu View - Chuẩn Master Codex 8.0:
Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Bản Lĩnh
Dung lượng: 3 Tập chuẩn điện ảnh (~4.600 từ, mỗi tập >= 1.450 từ).
Giọng đọc chỉ định: vi-VN-HoaiMyNeural (Tốc độ rate="+6%", BGM ducking -22dB).
100% KHẨU NGỮ ĐỜI THƯỜNG - TRIỆT TIÊU TOÀN BỘ SỰ SƯỢNG TRÂN VÀ HOẠT HÌNH HÓA.
"""

from typing import Dict, Any

def get_man_tra_thu_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Bản Lĩnh"

    part1_full = """{part1_text}"""

    part2_full = """{part2_rich.strip()}"""

    part3_full = """{part3_rich.strip()}"""

    return {{
        "title": story_title,
        "genre": "Gia Đấu Mẹ Chồng / Đời Sống Thực Tế",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ME_CHONG",
        "parts": {{
            "part1": part1_full.strip(),
            "part2": part2_full.strip(),
            "part3": part3_full.strip(),
        }},
        "comment_magnets": [
            "Theo mọi người, hành động dứt khoát đuổi họ hàng và ly hôn của người vợ như vậy là quá đáng hay là bản lĩnh?",
            "Nếu rơi vào hoàn cảnh mẹ chồng dẫn họ hàng lên chiếm phòng ngủ ngay ngày vừa sinh xong, các chị em sẽ xử lý như thế nào?",
            "Có chị em nào trước khi cưới đã tự mua nhà đứng tên một mình chưa, chia sẻ cảm giác tự chủ tài chính cho mọi người cùng biết nhé!"
        ]
    }}
'''

target_file.write_text(code_content, encoding="utf-8")
print("Saved fully enriched masterpiece successfully!")
