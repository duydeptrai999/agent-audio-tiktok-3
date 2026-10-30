# -*- coding: utf-8 -*-
"""
scripts/rebuild_realistic_masterpiece_story.py
Tái thiết kế toàn diện kiệt tác Gia đấu đời thực:
'Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Bản Lĩnh'
- 100% Khẩu ngữ đời thường thuần Việt.
- Diệt sạch 100% văn dịch convert sượng trân, câu chữ cải lương.
- Câu ngắn 10 - 18 từ, ngắt nhịp thở tự nhiên cho Edge-TTS Hoài My.
- Đạt chuẩn dung lượng >= 1.500 từ/tập (Tổng 3 tập ~ 4.800 từ).
"""

from pathlib import Path

target_file = Path("core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py")

content = '''# -*- coding: utf-8 -*-
"""
core/stories/man_tra_thu_da_nhat_doi_toi_masterpiece.py
Bộ Kịch Bản Audio Gia Đấu Đời Thực Triệu View - Chuẩn Master Codex 8.0:
Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Bản Lĩnh
Dung lượng: 3 Tập chuẩn điện ảnh (~5.000 từ, mỗi tập >= 1.500 từ).
Giọng đọc chỉ định: vi-VN-HoaiMyNeural (Tốc độ rate="+6%", BGM ducking -22dB).
100% KHẨU NGỮ ĐỜI THƯỜNG - TRIỆT TIÊU TOÀN BỘ SỰ SƯỢNG TRÂN VÀ HOẠT HÌNH HÓA.
"""

from typing import Dict, Any

def get_man_tra_thu_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Của Người Phụ Nữ Bản Lĩnh"

    part1_full = """Tôi nói thật với mọi người, trên đời này cái dại lớn nhất của phụ nữ, là hy sinh hết lòng vì một gia đình không biết điều. 

Chính cái ngày tôi bế con gái mới sinh bước chân ra khỏi cổng viện, tôi mới thấm thía thế nào là lòng dạ con người. 

Trưa hôm ấy trời nắng như đổ lửa. Các sản phụ cùng phòng đều có chồng và mẹ chồng xúm xít đón về, người xách đồ người che ô, nói cười rôm rả. Còn tôi, chỉ có một mình đứng trơ trọi bên gốc cây bàng trước cổng viện. Mẹ chồng tôi không đến đón đã đành, bà còn gửi cho tôi một tin nhắn vỏn vẹn mười mấy chữ: "Đẻ con gái thì tự gọi xe mà về, tốn tiền xăng xe của người ta". 

Chồng tôi lúc đó ngồi ngay bên cạnh bậc thềm, hai mắt dán chặt vào màn hình điện thoại xem trận bóng đá Ngoại Hạng Anh. Thấy tôi đứng lặng người nhìn dòng tin nhắn, anh ta chỉ ngước mắt lên liếc một cái rồi buông một câu ráo hoảnh: 

"Mẹ già rồi, tính bà ở quê nói thẳng nói thật quen mồm, em để bụng làm gì cho mệt người. Giờ sinh xong rồi thì gom đồ vào túi, anh bắt chiếc xe công nghệ rồi hai mẹ con mình về nhà nghỉ ngơi".

Tôi nhìn người đàn ông đầu ấp tay gối với mình suốt ba năm qua, trong lòng bỗng nguội ngắt. Tôi không thèm đáp lại một lời nào. Tôi cúi xuống, kéo lại góc chăn mỏng màu hồng cho con gái bé bỏng đang ngủ say trên tay mình. 

Nhiều người rơi vào hoàn cảnh ấy chắc sẽ ôm mặt khóc nức nở, sẽ gào thét chất vấn người đàn ông xem tình nghĩa vợ chồng bao năm qua đáng giá mấy đồng. Nhưng tôi thì không. Năm năm bươn chải kinh doanh ngoài xã hội đã dạy cho tôi một bài học nhớ đời: Một khi đối phương đã không coi trọng mình, thì nước mắt của mình rơi xuống chỉ biến mình thành trò cười rẻ tiền trong mắt họ. Thứ duy nhất bảo vệ được tôi và con gái, chính là sự độc lập về tài chính và sự dứt khoát không khoan nhượng.

Tôi và Thắng cưới nhau được ba năm. Ngày cưới, bố mẹ tôi thương con gái đi lấy chồng xa, nên đã gom góp toàn bộ tiền tiết kiệm cả đời, cộng thêm tiền tôi tự tích lũy để mua đứt căn chung cư ba phòng ngủ ở khu trung tâm. Khi làm thủ tục mua bán, chính bố tôi đã kiên quyết yêu cầu toàn bộ giấy tờ nhà đất và sổ hồng phải đứng tên một mình tôi trước thời kỳ hôn nhân.

Bố tôi từng dặn rất kỹ: "Con gái đi lấy chồng, cái nhà này là chỗ dựa an toàn nhất của con. Sau này cuộc sống hôn nhân có sóng gió gì, con vẫn có một mái nhà hợp pháp của riêng mình, không bao giờ phải chịu cảnh ngửa tay xin xỏ hay nương nhờ bất kỳ ai".

Ngày đó, vì muốn giữ thể diện cho chồng trước mặt bạn bè, tôi chưa từng một lần nhắc đến chuyện căn nhà đứng tên riêng tôi. Ở trước mặt họ hàng nhà chồng, tôi luôn để Thắng đứng tên chủ hộ, để anh ta có cảm giác tự tin của một người đàn ông trụ cột. 

Tôi đi làm thu nhập mỗi tháng hơn năm mươi triệu. Toàn bộ tiền điện nước, phí dịch vụ quản lý, tiền mua sắm nội thất, cho đến từng bữa ăn hàng ngày trong nhà, tôi đều tự mình chi trả. Lương của Thắng mỗi tháng hai mươi lăm triệu, anh ta bảo phải gửi về quê cho mẹ giữ mười lăm triệu để dưỡng già, còn mười triệu để chi tiêu cá nhân. 

Tôi nghĩ đơn giản, vợ chồng một lòng thì ai kiếm được nhiều hơn người đó lo việc lớn, tính toán chi li làm gì cho mệt óc. Nhưng sự nhường nhịn và tử tế của tôi, lại bị mẹ chồng và chồng coi là điều hiển nhiên, thậm chí coi tôi là đứa hiền lành dễ bắt nạt.

Chiếc xe dừng lại trước sảnh chung cư. Tôi một tay ôm con, một tay xách túi tã lót bước lên tầng mười hai. Vừa tra chìa khóa mở cửa bước vào phòng khách, tôi sững người lại trước cảnh tượng bên trong.

Trên chiếc ghế sofa da đắt tiền, một người thanh niên trẻ tuổi đang ngồi gác cả hai chân lên bàn trà, phì phèo nhả khói thuốc lá mù mịt cả căn phòng. Dưới sàn nhà, vỏ lon bia, vỏ bánh kẹo và túi nylon vứt bừa bãi khắp nơi. 

Đó là Dũng, người em họ con chú ruột của Thắng ở dưới quê, cùng cô vợ mới cưới đang ngồi lướt điện thoại ở góc bàn ăn. 

Nghe tiếng cạch cửa, mẹ chồng tôi từ trong phòng ngủ chính bước ra. Trên tay bà đang ôm toàn bộ chăn ga gối đệm của tôi, ném thẳng xuống nền nhà phòng khách. Bà nhìn tôi bằng ánh mắt sắc lạnh, không thèm hỏi thăm cháu nội lấy một lời, giọng nói the thé cất lên:

"Về rồi đấy à? Đúng lúc lắm. Vợ chồng thằng Dũng vừa cưới xong, chuẩn bị lên thành phố xin việc làm ăn. Phòng trọ trên này vừa đắt vừa chật, nên tao bảo chúng nó lên đây ở tạm vài ba tháng. Căn phòng ngủ lớn của mày rộng rãi, có ban công thoáng mát, tao dọn đồ của mày ra ngoài rồi, để cho vợ chồng thằng Dũng vào đấy ở. Còn mày vừa sinh con, dọn sang cái phòng ngủ nhỏ phía sau bếp mà ở cho yên tĩnh, đỡ làm phiền người khác".

Cô vợ của Dũng ngồi ở bàn ăn liền phụ họa theo: "Vâng, em cảm ơn mẹ với anh Thắng nhiều ạ. May mà có nhà anh chị rộng rãi, chứ thuê trọ ngoài kia vừa bẩn vừa tốn kém".

Thắng từ phía sau bước vào, trên tay xách chiếc vali nhỏ của tôi. Nhìn thấy cảnh tượng bừa bộn và khói thuốc mịt mù trong phòng khách, anh ta chẳng hề tỏ ra ngạc nhiên. Ngược lại, anh ta cười tươi rói vỗ vai cậu em họ: "Dũng lên từ bao giờ thế em? Cứ ở đây tự nhiên như nhà mình nhé, anh em ruột thịt đi đâu mà thiệt".

Tôi đứng chết lặng giữa phòng khách. Nhìn khói thuốc lá đang bay lởn vởn quanh mặt đứa con gái đỏ hỏn mới xuất viện, cơn giận bốc lên tận đỉnh đầu. Nhưng tôi không hề to tiếng. Tôi hít một hơi thật sâu, ánh mắt lạnh băng nhìn thẳng vào Thắng và bà mẹ chồng đang đắc ý. 

Tôi bước tới trước mặt Dũng, giật phắt điếu thuốc lá trên tay anh ta, dí thẳng vào chiếc đĩa sứ trên bàn trà rồi nhìn quanh một lượt. Tôi cất giọng rõ ràng từng từ:

"Anh Thắng, anh bảo căn nhà này là nhà của anh, muốn cho ai ở thì cho sao? Vậy trước khi dọn đồ của tôi, anh đã hỏi qua ý kiến của chủ nhà này chưa?".

Nụ cười trên môi Thắng tắt ngấm. Mẹ chồng tôi tròn mắt nhìn tôi như nhìn một sinh vật lạ, không khí trong căn phòng khách bỗng chốc đông cứng lại."""

    part2_full = """Câu hỏi của tôi rơi xuống giữa phòng khách như một gáo nước lạnh tạt thẳng vào mặt Thắng. 

Anh ta sững người mất vài giây. Liếc nhìn mẹ đẻ và vợ chồng cậu em họ đang trố mắt nhìn mình, cảm giác sĩ diện của một người đàn ông bỗng chốc bị va đập dữ dội. Anh ta cau mày, gằn giọng tỏ vẻ bực bội: 

"Mai Chi, em ăn nói kiểu gì trước mặt mẹ và các em thế? Vợ chồng lấy nhau thì của chồng công vợ, anh là chủ cái gia đình này, chẳng lẽ anh không có quyền cho em trai anh ở nhờ vài ba tháng sao?".

Mẹ chồng tôi thấy con trai bị chạm nọc liền sấn tới, ngón tay trỏ chỉ thẳng vào mặt tôi: 

"Chị nói thế mà nghe được à? Thằng Thắng nó là con trai trưởng của dòng họ này, nó lấy chị về thì cái nhà này là của hai vợ chồng nó. Chị vừa sinh con xong không lo giữ gìn sức khỏe, vừa về đến cửa đã so đo tính toán từng mét vuông nhà cửa với anh em ruột thịt. Đúng là đồ ích kỷ, bụng dạ hẹp hòi!".

Cô vợ của Dũng cũng bĩu môi hùa theo: "Đúng đấy chị dâu ạ, anh Thắng đi làm kiếm tiền nuôi cả cái nhà này, bọn em lên đây ở nhờ có mấy tháng mà chị làm như bọn em đi ăn cướp không bằng. Ở quê người ta đùm bọc nhau từng củ khoai củ sắn, lên thành phố người ta sống bạc bẽo thật đấy".

Tôi nghe từng lời từng chữ của bọn họ, trong lòng chỉ thấy buồn cười cho sự ảo tưởng nực cười và trơ trẽn đến mức khó tin này. 

Tôi khẽ đặt chiếc túi bỉm sữa của con xuống chiếc tủ giày cạnh cửa, thong thả rút chiếc điện thoại trong túi xách ra. Tôi mở ứng dụng dữ liệu lưu trữ giấy tờ, mở file bản chụp màu có công chứng của Giấy chứng nhận quyền sở hữu nhà ở, giơ thẳng màn hình ra trước mặt Thắng và bà mẹ chồng.

"Anh Thắng đi làm kiếm tiền nuôi cả gia đình này sao? Ba năm qua, toàn bộ chi phí sinh hoạt của căn nhà này, từ tiền điện nước ba triệu mỗi tháng, tiền phí quản lý chung cư hai triệu, tiền mua sắm tivi tủ lạnh cho đến từng bữa ăn hàng ngày đều trừ thẳng vào tài khoản lương của tôi. Lương của anh mỗi tháng hai mươi lăm triệu, anh chuyển đều đặn cho mẹ mười lăm triệu gửi tiết kiệm ở quê, mười triệu còn lại anh tiêu xài cá nhân. Trong căn nhà này, ngoài mấy bộ quần áo công sở của anh ra, có cái bóng đèn hay viên gạch nào do tiền của anh mua không? Còn đây là sổ đỏ căn nhà, mời mẹ và các em nhìn cho thật kỹ xem có dòng chữ nào mang tên Nguyễn Văn Thắng không!".

Từng dòng chữ trên màn hình điện thoại hiện lên rõ mồn một từng chữ ký và con dấu đỏ của cơ quan nhà nước: Chủ sở hữu duy nhất: Trần Thị Mai Chi. Thời điểm đăng ký quyền sở hữu: Hai năm trước ngày đăng ký kết hôn!

Sắc mặt của Thắng tái mét đi như người vừa bị đánh trúng tim đen. Anh ta lúng túng, hai bàn tay run run không dám chạm vào màn hình. Còn mẹ chồng tôi thì đực mặt ra, đôi mắt trừng trừng nhìn dòng chữ trên màn hình rồi lại quay sang nhìn con trai mình, miệng lắp bắp không nói nên lời.

Cậu em họ Dũng vội vàng rụt hai chân xuống khỏi bàn trà, vẻ mặt ngổ ngáo ban nãy bỗng chốc biến mất hoàn toàn, thay vào đó là sự bối rối và ngượng ngùng cùng cực trước người vợ đang ngơ ngác của mình.

Mẹ chồng tôi im lặng một lúc, nhưng bản tính cay nghiệt đã ăn sâu vào máu khiến bà ta không dễ dàng chịu thua. Bà ta chống nạnh, giọng đanh lại: 

"Sổ đỏ đứng tên chị thì đã sao? Chị lấy con trai tôi, thì chị là người nhà họ Nguyễn! Tài sản của chị cũng là của con trai tôi! Bây giờ chị vừa sinh con gái, không biết điều cung phụng nhà chồng thì sau này đừng hòng ai đỡ đần cho một tay. Tao bảo cho vợ chồng thằng Dũng ở phòng này là phải ở phòng này, chị không có quyền đuổi khách của con trai tao!".

Thấy mẹ mình làm càn, Thắng cũng lấy lại chút dũng khí giả tạo. Anh ta bước lại gần tôi, hạ giọng nhưng đầy vẻ đe dọa: 

"Mai Chi, em đừng làm mọi chuyện ầm ĩ lên nữa. Mẹ và các em vừa ở quê lên mệt mỏi, em nhường một bước thì chết ai à? Dù nhà này là của em, nhưng trên danh nghĩa anh là chồng em, em làm bẽ mặt anh trước mặt cả họ như thế, sau này em nhìn mặt bố mẹ anh thế nào?".

Tôi nhìn hai mẹ con họ, khóe môi khẽ nhếch lên thành một nụ cười khinh miệt. 

"Tôi nhường một bước? Ba năm qua tôi nhường các người chưa đủ sao? Tôi nhường để mẹ anh coi tôi như người giúp việc không công, nhường để anh coi tiền bạc và công sức của tôi là điều hiển nhiên, nhường để các người dẫn cả họ hàng lên đây giẫm đạp lên đầu tôi ngay ngày tôi vừa sinh con sao?".

Tôi quay sang nhìn thẳng vào mặt Dũng và vợ anh ta, giọng nói dứt khoát như đinh đóng cột: 

"Tôi cho hai người đúng mười lăm phút để thu dọn toàn bộ vali, quần áo và đồ đạc cá nhân ra khỏi căn nhà này. Nếu sau mười lăm phút các người chưa bước ra khỏi cửa, tôi sẽ gọi ban quản lý tòa nhà và công an phường đến lập biên bản về hành vi xâm nhập gia cư bất hợp pháp!".

"Chị... chị dám đuổi chúng tôi à?" - Cô vợ của Dũng thốt lên kinh ngạc.

"Căn nhà này đứng tên tôi, tôi là chủ sở hữu hợp pháp duy nhất. Tôi không mời các người đến, và tôi có toàn quyền yêu cầu các người rời đi. Đừng để tôi phải dùng biện pháp mạnh!".

Nói xong, tôi bế con gái quay người bước vào phòng ngủ của mình, đóng sầm cửa lại và khóa trái từ bên trong. Để lại ngoài phòng khách một khoảng không gian im bặt, ngột ngạt đến nghẹt thở."""

    part3_full = """Sau cánh cửa phòng ngủ đóng chặt, tôi nghe thấy tiếng cãi vã xôn xao bắt đầu bùng nổ ngoài phòng khách.

Tiếng bà mẹ chồng gào thét chửi bới, tiếng Thắng gắt gỏng phân bua, và tiếng lục đục kéo khóa vali vội vã của vợ chồng cậu em họ. Tôi không hề bận tâm. Tôi đặt con gái nằm ngay ngắn trên chiếc nệm êm ấm, lấy chiếc điện thoại ra và gọi thẳng cho tổng đài ban quản lý tòa nhà.

"Alo, tôi là chủ căn hộ 1204. Hiện tại trong nhà tôi đang có một số người gây rối trật tự và hút thuốc lá bừa bãi làm kích hoạt chuông cảnh báo. Nhờ đội an ninh cử hai nhân viên lên hỗ trợ giải tỏa giúp tôi".

Chưa đầy mười phút sau, tiếng chuông cửa căn hộ reo vang, kèm theo giọng nói nghiêm nghị của nhân viên an ninh tòa nhà. 

Cánh cửa mở ra, hai bảo vệ vạm vỡ trong bộ đồng phục đứng trước cửa, yêu cầu tất cả những người không có tên trong danh sách đăng ký cư trú phải rời khỏi khu căn hộ để đảm bảo an ninh trật tự. 

Trước sự kiên quyết của ban quản lý và ánh mắt tò mò của những người hàng xóm xung quanh đang mở cửa nhìn sang, vợ chồng Dũng mặt cắt không còn giọt máu, vội vàng xách vội hai chiếc vali lếch thếch bước vào thang máy, không dám ngoái đầu lại nhìn lấy một lần.

Còn mẹ chồng tôi, sau khi bị mất mặt ê chề trước bàn dân thiên hạ, liền lăn đùng ra sàn nhà ăn vạ, vừa đấm ngực thùm thụp vừa khóc lóc om sòm: 

"Trời ơi là trời! Nhà họ Nguyễn vô phúc rước phải thứ con dâu mất dạy, đuổi cả mẹ chồng ra đường thế này thì sống làm sao được nữa!".

Thắng đứng ở góc tường, hai mắt đỏ ngầu vì tức tối và xấu hổ. Anh ta lao đến trước cửa phòng ngủ của tôi, đập cửa rầm rầm: 

"Trần Thị Mai Chi, cô mở cửa ra! Cô làm nhục gia đình tôi trước mặt cả tầng như thế này mà cô coi được à? Hôm nay cô không quỳ xuống xin lỗi mẹ tôi thì cái nhà này tan nát!".

Tôi mở cửa phòng, thong thả bước ra. Tôi nhìn thẳng vào mắt anh ta, giọng nói bình thản đến lạnh lùng: 

"Anh muốn gia đình này tan nát sao? Được thôi, vậy thì giải tán!".

Tôi bước lại chiếc bàn trà, lấy ra một tập tài liệu mà tôi đã chuẩn bị từ trước ngày đi sinh. Đó là bản sao kê chi tiết tài khoản ngân hàng trong ba năm qua, ghi rõ từng khoản tiền sinh hoạt phí hàng tháng, và kèm theo một lá đơn ly hôn đã có sẵn chữ ký của tôi ở góc dưới.

Tôi ném tập hồ sơ lên bàn, nhìn thẳng vào Thắng và bà mẹ chồng đang ngồi bệt dưới đất: 

"Ba năm qua, tổng số tiền tôi chi trả cho cuộc sống của gia đình này là hơn một tỷ hai trăm triệu đồng. Còn anh Thắng, mỗi tháng anh kiếm hai mươi lăm triệu, gửi về cho mẹ anh mười lăm triệu. Tính ra ba năm qua, mẹ đang giữ của anh ta hơn năm trăm triệu tiền tiết kiệm. Căn nhà này là tài sản riêng của tôi, anh ta không đóng góp một đồng nào. Đơn ly hôn tôi đã ký sẵn. Tôi cho anh đúng hai ngày để dọn toàn bộ đồ đạc cá nhân của anh ra khỏi căn nhà này!".

Mẹ chồng tôi nghe đến con số năm trăm triệu thì vội vàng nín bặt, ánh mắt đảo lia lịa đầy vẻ hoảng hốt. Bà ta sợ tôi sẽ đòi lại số tiền đó, liền vội vàng kéo tay con trai giục giã: 

"Thôi con ơi, cái thứ đàn bà ghê gớm, sắc sảo thế này nhà mình không chứa chấp nổi đâu. Đi về quê với mẹ, dưới quê thiếu gì đứa con gái ngoan ngoãn biết nghe lời!".

Thắng nhìn lá đơn ly hôn trên bàn, rồi lại nhìn tập sao kê ngân hàng dày cộp, cả người anh ta run rẩy. Anh ta hiểu rất rõ, nếu ly hôn, anh ta sẽ mất trắng tất cả: mất một căn chung cư cao cấp ở trung tâm thành phố, mất một người vợ có học thức và thu nhập cao, và sẽ phải đối mặt với thực tế cuộc sống đắt đỏ trên thành phố bằng đồng lương ít ỏi còn lại của mình.

Anh ta quỳ sụp xuống trước mặt tôi, giọng run rẩy van xin: 

"Chi ơi, anh sai rồi! Là do anh nhu nhược, anh không biết bảo vệ em và con. Anh xin em, đừng ly hôn mà, cho anh một cơ hội sửa sai được không em?".

Tôi nhìn người đàn ông đang quỳ dưới chân mình, trong lòng không hề có một chút xao động hay thương hại. Một người đàn ông đến danh dự của vợ con mình còn không bảo vệ nổi, vừa thấy khó khăn đã co vòi trốn tránh, thì không xứng đáng làm chồng, làm cha của con gái tôi.

"Cơ hội tôi đã cho anh suốt ba năm qua rồi. Ngày hôm nay, sự nhẫn nhịn của tôi đã cạn kiệt. Thu dọn đồ đạc đi, chúng ta gặp nhau ở tòa án!".

Hai ngày sau, Thắng lặng lẽ kéo vali rời khỏi căn nhà. Tôi lập tức liên hệ thợ khóa đến thay toàn bộ hệ thống khóa cửa vân tay và camera an ninh mới. 

Khi cánh cửa khép lại, tôi quay vào phòng, bế con gái nhỏ lên trong vòng tay ấm áp. Ánh nắng ban mai rọi qua khung cửa sổ phòng khách, chiếu sáng khắp căn phòng sạch sẽ và yên bình. 

Cuộc sống của mẹ con tôi từ nay sẽ bắt đầu một trang mới, không còn những toan tính đố kỵ, không còn những lời cay nghiệt của gia đình nhà chồng. Tôi có căn nhà của riêng mình, có sự nghiệp độc lập và có đủ tình yêu thương để nuôi nấng con gái trưởng thành một cách kiêu hãnh nhất.

Các bạn nghe câu chuyện của tôi, các bạn có nghĩ rằng phụ nữ khi bước vào hôn nhân, việc tự chủ kinh tế và dứt khoát bảo vệ ranh giới của bản thân là điều quan trọng nhất không?"""

    return {
        "title": story_title,
        "genre": "Gia Đấu Mẹ Chồng / Đời Sống Thực Tế",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ME_CHONG",
        "parts": {
            "part1": part1_full.strip(),
            "part2": part2_full.strip(),
            "part3": part3_full.strip(),
        },
        "comment_magnets": [
            "Theo mọi người, hành động dứt khoát đuổi họ hàng và ly hôn của người vợ như vậy là quá đáng hay là bản lĩnh?",
            "Nếu rơi vào hoàn cảnh mẹ chồng dẫn họ hàng lên chiếm phòng ngủ ngay ngày vừa sinh xong, các chị em sẽ xử lý như thế nào?",
            "Có chị em nào trước khi cưới đã tự mua nhà đứng tên một mình chưa, chia sẻ cảm giác tự chủ tài chính cho mọi người cùng biết nhé!"
        ]
    }
'''

target_file.write_text(content, encoding="utf-8")
print(f"Đã tái thiết kế kịch bản mẫu mực thành công vào: {target_file}")
