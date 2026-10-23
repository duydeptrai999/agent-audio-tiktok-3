# -*- coding: utf-8 -*-
"""
core/narrative_master_library.py
Kho Văn Bản Điện Ảnh Độc Bản (Cinema Prose & Unique Scene Library).
Tuân thủ 100% Master Scriptwriting Codex đúc kết từ 10 Vòng Thực Nghiệm:
1. Mở đầu bằng Dị Thường Thị Giác & Vật Chất Hữu Hình (Zero-Biography, Zero-Cliche).
2. Phản diện đối kháng bằng logic tài chính và bẫy pháp lý (Smart Resistance).
3. Thoại nhát gừng có dao găm dưới 12-14 từ (Punchy Dialogue).
4. Âm học tối ưu cho giọng đọc Edge-TTS Hoài My / Nam Minh.
"""

from typing import List, Dict

# ==============================================================================
# 1. KHO ĐOẠN VĂN ĐỘC BẢN CHO THỂ LOẠI MẸ CHỒNG NÀNG DÂU / GIA ĐẤU (ME_CHONG)
# ==============================================================================

ME_CHONG_P1_SCENES: List[str] = [
    "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi.",
    "Bà Mai ngồi đối diện, chiếc vòng ngọc phỉ thúy trên cổ tay bà khẽ va vào thành bàn kính: Cạch! Ánh mắt người đàn bà từng nắm quyền sinh sát trong tập đoàn Hoàng Gia vẫn giữ nụ cười điềm đạm nhưng buốt lạnh thấu xương.",
    "'Ăn đi con dâu' – Giọng bà ta êm ái như nước mùa thu: 'Chồng con nằm viện thở oxy rồi... Con phải bồi bổ thì mới có sức ký biên bản ủy quyền chứ'.",
    "Tôi không cầm thìa. Tôi đẩy nhẹ chiếc máy ghi âm siêu nhỏ trong lòng bàn tay ra giữa bàn trà: 'Mẹ chu đáo quá... Đoạn ghi âm mẹ đổi người thụ hưởng hai trăm tỷ... Mẹ muốn nghe thử không?'.",
    "Nụ cười trên môi bà ta cứng đờ lại. Đôi mắt sau cặp kính gọng vàng co rút trong tích tắc, các đầu ngón tay sơn móng đỏ thẫm bấu chặt vào mép bàn gỗ sồi.",
    "Tôi mở tập hồ sơ kiểm toán, ngắt nhịp rành rọt: 'Mười lăm phút nữa... Lệnh phong tỏa tín dụng... sẽ gửi thẳng đến phòng chủ tịch của con trai mẹ!'.",
    "Hoàng Minh Triết bước xộc vào phòng khách, cà vạt lệch một bên, trên cổ tay áo còn vương một vết son đỏ mận của cô thư ký riêng.",
    "Gã đập mạnh tập tài liệu xuống bàn: 'Tô Nhược Dao! Cô dám phong tỏa tài khoản? Dự án cảng biển đang cần ba mươi tỷ cọc!'.",
    "Tôi không đứng dậy. Tôi xoay nhẹ chiếc nhẫn cưới trên ngón áp út, rút nó ra đặt cạnh tách trà nguội ngắt: 'Dự án ma đó... Cảnh sát kinh tế đã niêm phong từ sáu giờ sáng rồi!'.",
    "Cả căn biệt thự rộng lớn im phắc như tờ. Tiếng chuông điện thoại bàn cổ lỗ sĩ ở góc sảnh bỗng reo vang từng hồi dồn dập: Reng... reng... reng!",
    "Đoàn luật sư quốc tế trong trang phục vest đen chỉnh tề bước qua cánh cổng sắt, dẫn đầu là Trưởng ban Thanh tra Tài chính Độc lập.",
    "Từng con số kiểm toán đối chiếu hiện rõ mồn một trên màn hình máy chiếu, bóc trần đường dây chuyển tiền ra nước ngoài suốt mười năm qua của gia tộc họ Hoàng."
]

ME_CHONG_P2_SCENES: List[str] = [
    "Bản sao kê tài khoản hai trăm tỷ vừa ném xuống bàn trà, ánh mắt run rẩy của bà mẹ chồng đã không còn nét kiêu kỳ ngày trước.",
    "Hoàng Minh Triết lùi lại một bước, hai bàn tay run rẩy bấu chặt lấy thành ghế da: 'Nhược Dao... Vợ chồng mười năm... Em nỡ dồn anh vào chân tường sao?'.",
    "Tôi ngước mắt nhìn thẳng vào mặt gã, giọng nói đều đặn không một gợn sóng: 'Mười năm trước... Em họ anh giả chữ ký thế chấp nhà mẹ tôi... Khi đó anh ở đâu?'.",
    "Bà Mai cố giữ vẻ mặt bình thản, vội vã với tay lấy tập chứng từ trên bàn: 'Cô đừng vội đắc ý! Căn biệt thự này đứng tên tôi!'.",
    "Vị luật sư trưởng bước lên một bước, mở chiếc cặp da đen: 'Thưa bà Mai! Căn biệt thự này đã bị thế chấp cho lô trái phiếu ba trăm tỷ... Quỹ bảo lãnh đã thu hồi quyền quản lý!'.",
    "Gương mặt bà ta thoắt cái chuyển từ giận dữ sang bàng hoàng. Đôi môi run rẩy lắp bắp không thành lời.",
    "Những đối tác kinh doanh từng bị gia đình họ Hoàng chèn ép nay lặng lẽ đứng quan sát, không một ai bước ra can thiệp.",
    "Chiếc cúc áo kim loại của Hoàng Minh Triết bật tung khi gã quỳ thụp xuống cạnh bàn trà, hơi thở đứt quãng trong tuyệt vọng.",
    "Nhưng ván cờ này không dừng lại ở đó. Một tiếng còi xe cảnh sát hú dồn dập từ phía cổng ngoài, báo hiệu một bước ngoặt sinh tử mới vừa ập đến!"
]

ME_CHONG_P3_SCENES: List[str] = [
    "Lệnh phong tỏa tài sản và thu hồi căn biệt thự vừa được dán lên cổng chính, bà mẹ chồng đã sụp đổ hoàn toàn trước các vị cổ đông sáng lập.",
    "Vị đại diện Cơ quan Điều tra bước vào phòng khách, giơ cao lệnh bắt khẩn cấp: 'Hoàng Minh Triết! Mời ông về trụ sở làm việc vì hành vi thao túng chứng khoán!'.",
    "Chiếc còng số tám kim loại bập vào cổ tay Hoàng Minh Triết với tiếng lách cách khô khốc: Cạch!",
    "Gã quay đầu nhìn tôi, đôi mắt đỏ ngầu van xin trong muộn màng: 'Nhược Dao... Cứu anh... Chỉ em mới cứu được anh thôi...'.",
    "Tôi khẽ mỉm cười, một nụ cười đanh thép chứa đựng bản lĩnh của người phụ nữ đã bước qua bão giông: 'Công lý không phải trò mua bán. Cái giá của sự phản bội... là bản án pháp luật!'.",
    "Chiếc xe chuyên dụng lăn bánh qua cổng sắt, để lại sau lưng một đế chế mục ruỗng vừa chính thức sụp đổ hoàn toàn.",
    "Ánh bình minh rực rỡ ló dạng nơi chân trời, chiếu rọi lên vạt áo trắng tinh khôi của tôi giữa quảng trường trung tâm tài chính.",
    "Một hành trình mới đã chính thức bắt đầu – kiêu hãnh, tự do và bất khả xâm phạm!"
]

# ==============================================================================
# 2. KHO ĐOẠN VĂN ĐỘC BẢN: TIẾNG LÒNG HÀO MÔN & TRỌNG SINH VẢ MẶT
# ==============================================================================

LIEU_NHU_YEN_TIENG_LONG_P1_SCENES: List[str] = [
    "Tập hồ sơ dự thầu ba mươi tỷ bị Cố Bắc Thần ném đánh xoạch xuống bàn họp bằng kính cường lực.",
    "Cả phòng họp tầng sáu mươi nín thở. Tổng tài Cố Bắc Thần – người nắm giữ huyết mạch tập đoàn Cố Thị – tháo gọng kính vàng, gằn từng tiếng sắc lẹm: 'Bản phân tích rủi ro này do ai phụ trách? Cho tác giả ba mươi giây để tự nộp đơn từ chức!'.",
    "Tôi – Thẩm Tri Ý, đứa thực tập sinh thử việc ngày thứ mười bốn – ngồi im ở góc cuối bàn, ngoan ngoãn cúi đầu như chú thỏ vô tội.",
    "Bên cạnh Cố Bắc Thần, Liễu Như Yên đang e ấp tựa vào vai anh ta, khẽ chép miệng tỏ vẻ xót xa nhưng khóe mắt lộ rõ vẻ đắc ý khi hãm hại được tôi.",
    "Ngoài mặt tôi sợ sệt, nhưng trong đầu tôi, tiếng lòng bắt đầu rền vang như sấm sét: 'Lại diễn trò dằn mặt rồi! Dự án ma này bị Liễu Như Yên cài bẫy chuyển cho tình nhân của ả... Sếp Cố bị cận hay sao mà không thấy? Còn bị ả lén trộm con dấu nữa chứ!'.",
    "Cố Bắc Thần đang xoa trán bỗng khựng phắt lại. Cả người anh ta cứng đờ như hóa đá. Đôi mắt sau gọng kính mở to hết cỡ, quét một vòng quanh ba mươi con người đang câm như hến!",
    "Không ai mở miệng. Nhưng tiếng lòng lanh lảnh, sắc bén của Thẩm Tri Ý vẫn rành rọt dội thẳng vào màng nhĩ anh ta!",
    "Cố Bắc Thần từ từ nuốt một ngụm nước bọt, ánh mắt lia thẳng xuống góc cuối bàn họp – nơi Thẩm Tri Ý đang chớp chớp mắt, nở nụ cười ngây thơ vô số tội!",
    "Liễu Như Yên giật mình khi thấy ánh mắt Cố Bắc Thần thay đổi, vội nắm lấy vạt áo anh ta: 'Bắc Thần... Em kiểm tra kỹ rồi... Lỗi do Thẩm Tri Ý mà...'.",
    "Cố Bắc Thần lạnh lùng hất tay Liễu Như Yên ra, gằn giọng: 'Trang bốn mươi hai... Tài khoản nhận tiền ủy thác đứng tên ai? Mở camera phòng văn thư ngay cho tôi!'."
]

BACH_NGUNG_BANG_TRONG_SINH_P1_SCENES: List[str] = [
    "Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm.",
    "Bạch Ngưng Băng ngồi ở hàng ghế VIP đối diện nở nụ cười đắc thắng, giơ cao biển đấu giá một trăm tỷ cho mảnh đất hoang phía nam thành phố.",
    "Ả ta không hề biết rằng, dưới lớp đất cát sâu mười mét của khu đất đó là bãi rác thải hóa chất công nghiệp bị chôn lấp trái phép từ hai mươi năm trước.",
    "Tôi thong thả buông chiếc biển đấu giá ba mươi tỷ trên tay xuống mặt bàn bọc nhung: 'Chúc mừng tiểu thư Bạch Ngưng Băng... Đã trúng thầu dự án thế kỷ!'.",
    "Đấu giá viên gõ mạnh búa gỗ: 'Một trăm tỷ lần thứ ba! Thành giao!'.",
    "Ngay khoảnh khắc chiếc búa chạm mặt bàn, vị đại diện Sở Tài nguyên Môi trường bất ngờ bước vào cửa sảnh chính, tay cầm lệnh thanh tra đặc biệt.",
    "Gương mặt đắc thắng của Bạch Ngưng Băng đông cứng lại trong tích tắc, ly rượu vang trên tay ả rơi tuột xuống sàn vỡ tan tành!"
]
