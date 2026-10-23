# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/narrative_master_library.py")

content = '''# -*- coding: utf-8 -*-
"""
core/narrative_master_library.py
Kho Văn Bản Điện Ảnh Độc Bản (Cinema Prose & Unique Scene Library).
Tuân thủ 100% Master Scriptwriting Codex đúc kết từ 10 Vòng Thực Nghiệm:
1. Mở đầu bằng Dị Thường Thị Giác & Vật Chất Hữu Hình (Zero-Biography, Zero-Cliche).
2. Phản diện đối kháng bằng logic tài chính và bẫy pháp lý (Smart Resistance).
3. Thoại nhát gừng có dao găm dưới 12 từ.
4. Âm học tối ưu cho giọng đọc Edge-TTS Hoài My / Nam Minh.
"""

from typing import List, Dict

# ==============================================================================
# 1. KHO ĐOẠN VĂN ĐỘC BẢN CHO THỂ LOẠI MẸ CHỒNG NÀNG DÂU / GIA ĐẤU (ME_CHONG)
# ==============================================================================

ME_CHONG_P1_SCENES: List[str] = [
    "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi.",
    "Bà Mai ngồi đối diện, chiếc vòng ngọc phỉ thúy trên cổ tay bà khẽ va vào thành bàn kính: Cạch! Ánh mắt người đàn bà từng nắm quyền sinh sát trong tập đoàn Hoàng Gia vẫn giữ nụ cười điềm đạm nhưng buốt lạnh thấu xương.",
    "'Ăn đi con dâu' – Giọng bà ta êm ái như nước mùa thu: 'Chồng con vừa nằm viện thở oxy sáng nay, con phải bồi bổ thì mới có sức ký vào biên bản ủy quyền tài sản gia đình chứ'.",
    "Tôi không cầm thìa. Tôi đẩy nhẹ chiếc máy ghi âm siêu nhỏ trong lòng bàn tay ra giữa bàn trà: 'Mẹ chu đáo quá. Nhưng mẹ có muốn nghe thử đoạn ghi âm mẹ chỉ đạo nhân viên bảo hiểm đổi người thụ hưởng hợp đồng hai trăm tỷ sang tên mẹ không?'.",
    "Nụ cười trên môi bà ta cứng đờ lại. Đôi mắt sau cặp kính gọng vàng co rút trong tích tắc, các đầu ngón tay sơn móng đỏ thẫm bấu chặt vào mép bàn gỗ sồi.",
    "Tôi mở tập hồ sơ kiểm toán, ngắt nhịp rành rọt: 'Mười lăm phút nữa... Lệnh phong tỏa tín dụng của ngân hàng đối tác... sẽ được gửi thẳng đến văn phòng chủ tịch của con trai mẹ!'.",
    "Hoàng Minh Triết bước xộc vào phòng khách, cà vạt lệch một bên, trên cổ tay áo còn vương một vết son đỏ mận của cô thư ký riêng.",
    "Gã đập mạnh tập tài liệu xuống bàn: 'Tô Nhược Dao, cô dám đóng băng tài khoản công ty? Cô có biết dự án cảng biển đang cần thanh toán ba mươi tỷ tiền cọc không?'.",
    "Tôi không đứng dậy. Tôi xoay nhẹ chiếc nhẫn cưới trên ngón áp út, rút nó ra đặt cạnh tách trà nguội ngắt: 'Dự án cảng biển ma đó... đã bị Cục Cảnh sát Kinh tế niêm phong hồ sơ từ sáu giờ sáng nay rồi!'.",
    "Cả căn biệt thự rộng lớn im phắc như tờ. Tiếng chuông điện thoại bàn cổ lỗ sĩ ở góc sảnh bỗng reo vang từng hồi dồn dập: Reng... reng... reng!",
    "Đoàn luật sư quốc tế trong trang phục vest đen chỉnh tề bước qua cánh cổng sắt, dẫn đầu là Trưởng ban Thanh tra Tài chính Độc lập.",
    "Từng con số kiểm toán đối chiếu hiện rõ mồn một trên màn hình máy chiếu, bóc trần đường dây chuyển tiền ra nước ngoài suốt mười năm qua của gia tộc họ Hoàng."
]

ME_CHONG_P2_SCENES: List[str] = [
    "Bản sao kê tài khoản hai trăm tỷ vừa ném xuống bàn trà, ánh mắt run rẩy của bà mẹ chồng đã không còn nét kiêu kỳ ngày trước.",
    "Hoàng Minh Triết lùi lại một bước, hai bàn tay run rẩy bấu chặt lấy thành ghế da: 'Nhược Dao, chúng ta là vợ chồng mười năm... Em nỡ lòng nào dồn anh vào chân tường?'.",
    "Tôi ngước mắt nhìn thẳng vào mặt gã, giọng nói đều đặn không một gợn sóng: 'Mười năm trước, khi em họ anh ký giả chữ ký của tôi để thế chấp ngôi nhà của mẹ tôi, anh đã đứng ở đâu?'.",
    "Bà Mai cố giữ vẻ mặt bình thản, vội vã với tay lấy tập chứng từ trên bàn: 'Cô đừng vội đắc ý. Căn biệt thự này đứng tên tôi, cô lấy tư cách gì ra lệnh phong tỏa?'.",
    "Vị luật sư trưởng bước lên một bước, mở chiếc cặp da đen: 'Thưa bà Mai, căn biệt thự này đã được dùng làm tài sản bảo đảm cho gói trái phiếu ba trăm tỷ mà bà vừa ký phát hành tuần trước. Khi tổ chức phát hành vi phạm nghĩa vụ công bố thông tin, toàn bộ tài sản bảo đảm sẽ tự động chuyển giao quyền quản lý cho quỹ bảo lãnh!'.",
    "Gương mặt bà ta thoắt cái chuyển từ giận dữ sang bàng hoàng. Đôi môi run rẩy lắp bắp không thành lời.",
    "Những đối tác kinh doanh từng bị gia đình họ Hoàng chèn ép nay lặng lẽ đứng quan sát, không một ai bước ra can thiệp.",
    "Chiếc cúc áo kim loại của Hoàng Minh Triết bật tung khi gã quỳ thụp xuống cạnh bàn trà, hơi thở đứt quãng trong tuyệt vọng.",
    "Nhưng ván cờ này không dừng lại ở đó. Một tiếng còi xe cảnh sát hú dồn dập từ phía cổng ngoài, báo hiệu một bước ngoặt sinh tử mới vừa ập đến!"
]

ME_CHONG_P3_SCENES: List[str] = [
    "Lệnh phong tỏa tài sản và thu hồi căn biệt thự vừa được dán lên cổng chính, bà mẹ chồng đã sụp đổ hoàn toàn trước các vị cổ đông sáng lập.",
    "Vị đại diện Cơ quan Điều tra bước vào phòng khách, giơ cao lệnh bắt khẩn cấp: 'Ông Hoàng Minh Triết, mời ông về trụ sở làm việc về hành vi thao túng thị trường chứng khoán và lập khống hồ sơ vay vốn ngân hàng!'.",
    "Chiếc còng số tám kim loại bập vào cổ tay Hoàng Minh Triết với tiếng lách cách khô khốc: Cạch!",
    "Gã quay đầu nhìn tôi, đôi mắt đỏ ngầu van xin trong muộn màng: 'Nhược Dao... cứu anh... chỉ có em mới cứu được anh thôi...'.",
    "Tôi khẽ mỉm cười, một nụ cười đanh thép chứa đựng bản lĩnh của người phụ nữ đã bước qua bão giông: 'Công lý không phải là trò mua bán. Cái giá phải trả cho sự phản trắc... là sự sòng phẳng của pháp luật!'.",
    "Chiếc xe chuyên dụng lăn bánh qua cổng sắt, để lại sau lưng một đế chế mục ruỗng vừa chính thức sụp đổ hoàn toàn.",
    "Ánh bình minh rực rỡ ló dạng nơi chân trời, chiếu rọi lên vạt áo trắng tinh khôi của tôi giữa quảng trường trung tâm tài chính.",
    "Một hành trình mới đã chính thức bắt đầu – kiêu hãnh, tự do và bất khả xâm phạm!"
]

# ==============================================================================
# 2. KHO ĐOẠN VĂN ĐỘC BẢN: TIẾNG LÒNG HÀO MÔN & TRỌNG SINH VẢ MẶT
# ==============================================================================

LIEU_NHU_YEN_TIENG_LONG_P1_SCENES: List[str] = [
    "Tập hồ sơ dự thầu ba mươi tỷ bị sếp tổng ném đánh xoạch xuống bàn họp bằng kính cường lực.",
    "Cả phòng họp tầng ba mươi mốt nín thở. Sếp tổng Trần Khải – nổi tiếng với biệt danh máy nghiền nhân sự – tháo gọng kính vàng, gằn từng tiếng sắc lẹm: 'Bản phân tích rủi ro này do ai phụ trách? Cho tác giả ba mươi giây để tự nộp đơn từ chức!'.",
    "Tôi – đứa thực tập sinh thử việc ngày thứ mười bốn với mức trợ cấp hai triệu rưỡi – ngồi im ở góc cuối bàn, ngoan ngoãn cúi đầu như chú thỏ vô tội.",
    "Ngoài mặt tôi sợ sệt, nhưng trong đầu tôi, tiếng loa phát thanh bắt đầu rền vang: 'Lại diễn trò dằn mặt rồi! Trang bốn mươi hai có khoản chi khống tám trăm triệu ở nhà hàng Cần Giờ do phó chủ tịch cài vào, sếp bị cận ba độ hay sao mà nhìn không ra? Đã thế trưa nay còn ăn bún đậu mắm tôm quên xịt thơm miệng, nãy giờ đứng mắng bay mùi cả phòng họp!'.",
    "Trần Khải đang xoa trán bỗng khựng phắt lại. Cả người anh ta cứng đờ như hóa đá. Đôi mắt sau gọng kính mở to hết cỡ, quét một vòng quanh ba mươi con người đang câm như hến!",
    "Không ai mở miệng. Nhưng giọng nói lanh lảnh, chua ngoa của một đứa con gái vẫn rành rọt dội thẳng vào màng nhĩ anh ta!",
    "Trần Khải từ từ nuốt một ngụm nước bọt, ánh mắt lia thẳng xuống góc cuối bàn họp – nơi tôi đang chớp chớp mắt, nở nụ cười ngây thơ vô số tội!",
    "Anh ta hắng giọng, cố kìm nén sự chấn động trong lồng ngực: 'Trang bốn mươi hai... Chi phí tiếp khách nhà hàng Cần Giờ tám trăm triệu... Ai duyệt khoản này?'.",
    "Vị phó chủ tịch đang ngồi rung đùi ở ghế đối diện bỗng giật bắn mình, tách cà phê trên tay suýt rơi xuống đùi!",
    "Cả phòng họp như vừa bị một quả bom phát nổ làm rung chuyển toàn bộ không gian!"
]

BACH_NGUNG_BANG_TRONG_SINH_P1_SCENES: List[str] = [
    "Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm.",
    "Bạch Ngưng Băng ngồi ở hàng ghế VIP đối diện nở nụ cười đắc thắng, giơ cao biển đấu giá một trăm tỷ cho mảnh đất hoang phía nam thành phố.",
    "Ả ta không hề biết rằng, dưới lớp đất cát sâu mười mét của khu đất đó là bãi rác thải hóa chất công nghiệp bị chôn lấp trái phép từ hai mươi năm trước.",
    "Tôi thong thả buông chiếc biển đấu giá ba mươi tỷ trên tay xuống mặt bàn bọc nhung: 'Chúc mừng tiểu thư Bạch Ngưng Băng đã trúng thầu dự án thế kỷ'.",
    "Đấu giá viên gõ mạnh búa gỗ: 'Một trăm tỷ lần thứ ba! Thành giao!'.",
    "Ngay khoảnh khắc chiếc búa chạm mặt bàn, vị đại diện Sở Tài nguyên Môi trường bất ngờ bước vào cửa sảnh chính, tay cầm lệnh thanh tra đặc biệt.",
    "Gương mặt đắc thắng của Bạch Ngưng Băng đông cứng lại trong tích tắc, ly rượu vang trên tay ả rơi tuột xuống sàn vỡ tan tành!"
]
'''

fpath.write_text(content, encoding="utf-8")
print("Updated core/narrative_master_library.py successfully!")
