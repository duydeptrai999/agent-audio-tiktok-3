# -*- coding: utf-8 -*-
import re

with open("core/knowledge_base.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace OPENING_HOOK_TEMPLATES_6 block with DIVERSE_HOOK_ARCHETYPES_10 + CHARACTER_UNIVERSES_10 + DIVERSE_RESOLUTIONS_10 + alias
old_hook_block = """# ==============================================================================
# 3. HỆ THỐNG 6 MẪU MỞ MÀN HOOK VÀNG 3-5 GIÂY (GOLDEN HOOKS)
# ==============================================================================
OPENING_HOOK_TEMPLATES_6 = [
    {
        "type": "Xung đột tiền trí (Conflict Frontloaded)",
        "desc": "Mở đầu ngay bằng một cái tát, một vụ kiện tụng hoặc câu quát tháo dằn mặt.",
        "example": "'Mẹ chồng hắt thẳng bát canh gà nóng bỏng vào mặt tôi: Đồ gà mái không biết đẻ trứng, mau ký vào đơn ly hôn rồi cút ra khỏi nhà!'",
        "best_for": ["ME_CHONG", "TRONG_SINH", "NGUOC_TAM"]
    },
    {
        "type": "Nghiền ép thân phận (Identity Inversion / Crushing)",
        "desc": "Hiển thị sự coi thường của đối phương, ngay lập tức báo hiệu thân phận bí mật vượt trội.",
        "example": "'Quản lý hất chiếc thẻ nhân viên rách nát vào ngực tôi: Nơi này tối thiểu chi tiêu 100 triệu, người nghèo như cậu không có tư cách bước vào!' - Mười giây sau, chiếc Maybach của chủ tịch tập đoàn phanh rít trước sảnh...",
        "best_for": ["HAO_MON", "TRONG_SINH", "SA_DIEU"]
    },
    {
        "type": "Nghịch cảnh cực hạn (Extreme Dilemma / Crisis)",
        "desc": "Đẩy nhân vật vào tình huống sinh tử nghẹt thở hoặc phá sản, ung thư giai đoạn cuối.",
        "example": "'Cầm kết quả ung thư giai đoạn cuối trên tay, tôi bước vào nhà thì thấy chồng đang vui vẻ ký hợp đồng mua căn biệt thự 50 tỷ tặng sinh nhật thư ký riêng.'",
        "best_for": ["NGUOC_TAM", "ME_CHONG", "CUU_ROI"]
    },
    {
        "type": "Đảo tự nghịch lý (Retrograde Suspense / Paradox)",
        "desc": "Đưa ra một câu đố bất khả thi hoặc lời cảnh báo rùng mình trong 5s đầu.",
        "example": "'Đúng hai giờ sáng giữa đêm mưa bão, chiếc điện thoại bàn đã cắt dây từ 5 năm trước bỗng reo vang từng hồi đinh tai nhức óc!'",
        "best_for": ["HUYEN_NGHI", "KINH_DI", "VO_HAN"]
    },
    {
        "type": "Ngọt sủng độc tôn (Sweet & Doting Hook)",
        "desc": "Khoảnh khắc che chở thiên vị độc nhất vô nhị trước ánh mắt ngỡ ngàng của đám đông.",
        "example": "'Trước mặt toàn thể giới thượng lưu, vị tổng tài nổi tiếng lạnh lùng tàn nhẫn bỗng quỳ một gối, cẩn thận buộc lại dây giày cho cô gái gả thay.'",
        "best_for": ["HAO_MON", "CUU_ROI"]
    },
    {
        "type": "Trọng sinh thức tỉnh tức thì (Instant Rebirth / Awakening)",
        "desc": "Mở mắt ra ngay tại khoảnh khắc định mệnh của kiếp trước, lập tức hành động thay đổi số phận.",
        "example": "'Mở mắt ra trong đêm tân hôn ngập sắc đỏ, việc đầu tiên tôi làm không phải chờ phu quân vén khăn voan, mà là với lấy bình trà gốm đập vỡ góc phòng để ép mình tỉnh táo!'",
        "best_for": ["TRONG_SINH", "CUNG_DAU", "VO_HAN"]
    }
]"""

new_hook_block = """# ==============================================================================
# 3. MA TRẬN 10 TRƯỜNG PHÁI MỞ ĐẦU ĐỘC BẢN (DIVERSE HOOK ARCHETYPES 10)
# ==============================================================================
# Khắc phục triệt để lỗi "na ná nhau" giữa các audio. Mỗi archetype sở hữu giác quan neo đậu,
# nghịch lý vật lý và chiến thuật kép (Thoáng qua 12-20 từ vs Chi tiết cận cảnh 25-45 từ) riêng biệt.
DIVERSE_HOOK_ARCHETYPES_10 = [
    {
        "archetype_id": 1,
        "name": "Vật chứng pháp y & Kẽ hở thời gian (Forensic Timeline Hook)",
        "type": "Vật chứng pháp y & Kẽ hở thời gian",
        "sensory_anchor": "Mũi kim đồng hồ chết, vết cào dưới móng tay gãy, sợi len vướng khuy áo",
        "desc": "Neo vào vật chứng cơ học ở hiện trường chết chóc, chỉ ra nghịch lý thời gian và mối quan hệ thân nhân bí mật.",
        "example": "'Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, ngay dưới đáy móng tay gãy vụn của cô ấy là sợi len màu xanh cổ vịt - chiếc áo duy nhất tôi mặc trong ngày cưới.'",
        "strategy_a_flash": "Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, ngay dưới đáy móng tay gãy vụn của cô ấy là sợi len màu xanh cổ vịt - chiếc áo duy nhất tôi mặc trong ngày cưới.",
        "strategy_b_detailed": "Mảnh kính vỡ từ mặt đồng hồ Rolex rơi xuống sàn gạch men, phản chiếu kim giây chết cứng ở hai giờ mười bốn phút. Vị điều tra viên trưởng không nhìn thi thể, ông cúi xuống gắp từ kẽ móng tay cháy đen của nạn nhân một mẩu vải len màu xanh cổ vịt. Đó là chiếc áo dệt kim độc bản mẹ chồng vừa tặng tôi vào tiệc đính hôn tối qua.",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM", "NGUOC_TAM"]
    },
    {
        "archetype_id": 2,
        "name": "Âm thanh cơ khí đe dọa cận kề (Mechanical Acoustic Hook)",
        "type": "Âm thanh cơ khí đe dọa cận kề",
        "sensory_anchor": "Tiếng chốt thép ba lớp sập cạch, van xả khí áp lực cao, bọc chăn để lộ đầu búp bê cao su hỏng mắt",
        "desc": "Khoảng cách vật lý tính bằng milimét giữa sinh tử và sự xâm nhập, âm thanh va chạm cơ khí đanh thép.",
        "example": "'Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang.'",
        "strategy_a_flash": "Tiếng còi báo động boong ke vừa hú lên đợt thứ ba, van xả khí cay tự động đã khóa chặt chốt cơ học cuối cùng ngay trước mũi giày ả em họ.",
        "strategy_b_detailed": "Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang: 'Chị Lam ơi! Thằng bé sốt bốn mươi độ rồi, cho em xin mẩu nến và gói mì tôm thôi!'. Tôi không mở cửa. Tôi tựa lưng vào vách thép dày mười lăm phân, ngón tay đặt sẵn trên van xả khí cay áp suất cao. Qua lỗ quan sát hồng ngoại, chiếc bọc chăn bông trên tay ả khẽ xốc xếch, để lộ một góc đầu búp bê cao su hỏng một mắt.",
        "best_for": ["VO_HAN", "MAT_THE", "KINH_DI"]
    },
    {
        "archetype_id": 3,
        "name": "Nghịch lý tương phản trào phúng & Tiếng lòng (Satirical Subtext Hook)",
        "type": "Nghịch lý tương phản trào phúng & Tiếng lòng",
        "sensory_anchor": "Ngòi bút nạm kim cương cách chữ ký một milimét, cà vạt màu cánh sen chấm bi, tiếng lòng bóc phốt sắc lẹm",
        "desc": "Phá tan sự trang nghiêm của giới thượng lưu bằng sự thật trần trụi, hài hước và bóc mẽ âm mưu ngầm.",
        "example": "'Chiếc bút máy nạm kim cương của Lục Cảnh Hoài chỉ còn cách dòng chữ ký bản hợp đồng năm trăm tỷ đúng một milimét, thì một giọng nữ lanh lảnh bỗng dội thẳng vào màng nhĩ anh: Dừng bút lại đồ ngốc!'",
        "strategy_a_flash": "Ngòi bút năm trăm tỷ vừa chạm mặt giấy, tiếng lòng của tôi đã lanh lảnh dội vào tai sếp: 'Ký đi đồ ngốc, ký xong là nhảy lầu tập thể!'.",
        "strategy_b_detailed": "Chiếc bút máy nạm kim cương của Lục Cảnh Hoài chỉ còn cách dòng chữ ký bản hợp đồng năm trăm tỷ đúng một milimét, thì một giọng nữ lanh lảnh bỗng dội thẳng vào màng nhĩ anh: 'Dừng bút lại đồ ngốc! Bản hợp đồng này ký xuống là mất trắng năm trăm tỷ, chưa kể chiếc cà vạt hoa hòe màu cánh sen chấm bi của sếp nhìn y hệt con công đang xòe đuôi!'. Bàn tay đang cầm bút của vị tổng tài khựng lại giữa không trung.",
        "best_for": ["SA_DIEU", "HAI_HUOC", "HAO_MON"]
    },
    {
        "archetype_id": 4,
        "name": "Bạo lực lạnh & Cắt dòng tiền (Cold Violence Financial Hook)",
        "type": "Bạo lực lạnh & Cắt dòng tiền",
        "sensory_anchor": "Chiếc thìa mạ vàng chạm đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng, máy ghi âm mini",
        "desc": "Mẹ chồng - nàng dâu hoặc gia đấu gia tộc: nụ cười điềm đạm ngụy trang âm mưu đoạt tài sản, đáp trả bằng bẫy sao kê.",
        "example": "'Mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng vừa lộ ra dưới đáy bát yến sáu mươi triệu, ngón trỏ của tôi đã bấm nút phát loa ngoài chiếc điện thoại bàn.'",
        "strategy_a_flash": "Mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng vừa lộ ra dưới đáy bát yến sáu mươi triệu, ngón trỏ của tôi đã bấm nút phát loa ngoài chiếc điện thoại bàn.",
        "strategy_b_detailed": "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi. Bà Mai ngồi đối diện, chiếc vòng ngọc phỉ thúy trên cổ tay bà khẽ va vào thành bàn kính: Cạch! Tôi không cầm thìa. Tôi đẩy nhẹ chiếc máy ghi âm siêu nhỏ trong lòng bàn tay ra giữa bàn trà: 'Mẹ chu đáo quá. Nhưng mẹ có muốn nghe thử đoạn ghi âm mẹ chỉ đạo nhân viên bảo hiểm đổi người thụ hưởng hợp đồng hai trăm tỷ sang tên mẹ không?'.",
        "best_for": ["ME_CHONG", "GIA_DAU", "NGUOC_TAM"]
    },
    {
        "archetype_id": 5,
        "name": "Hành động quy tắc hiện trường (In-Action Rule Survival Hook)",
        "type": "Hành động quy tắc hiện trường",
        "sensory_anchor": "Khán phòng ba trăm chỗ niêm phong, bóng áo mưa đen sũng nước ngồi ghế số bốn, ánh đèn chiếu phim",
        "desc": "Dị thường thị giác phá vỡ trật tự không gian quen thuộc, nhân vật phản xạ lập tức theo quy tắc sinh tồn ngầm.",
        "example": "'Luồng sáng trắng từ buồng máy chiếu vừa rọi qua khe kính xuống khán phòng ba trăm chỗ, hàng ghế số bốn vốn niêm phong bỗng có người áo mưa đen ngồi bất động dù ngoài trời nắng ráo suốt ba tuần.'",
        "strategy_a_flash": "Tấm vé rạp phim rách mép vừa rơi xuống chân, bóng áo mưa đen sũng nước ở hàng ghế số bốn đã từ từ quay đầu một trăm tám mươi độ.",
        "strategy_b_detailed": "Luồng sáng trắng từ buồng máy chiếu vừa rọi qua khe kính xuống khán phòng ba trăm chỗ, hàng ghế số bốn vốn niêm phong bỗng có người áo mưa đen ngồi bất động dù ngoài trời nắng ráo suốt ba tuần. Tôi cúi gầm mặt, ngón tay bấu chặt vào cuộn băng dính phản quang trong túi áo khoác, tuyệt đối không chớp mắt nhìn vào chiếc gáy ướt sũng đang xoay ngược lại phía tôi.",
        "best_for": ["KINH_DI", "QUAI_DAM", "HUYEN_NGHI"]
    },
    {
        "archetype_id": 6,
        "name": "Đấu giá bất đối xứng thông tin (Information Asymmetry Auction Hook)",
        "type": "Đấu giá bất đối xứng thông tin",
        "sensory_anchor": "Búa gỗ gõ cắc một trăm tỷ, bút laser rọi bản đồ quy hoạch ngầm, ly rượu vang vỡ tan",
        "desc": "Kẻ thù tự đắc tưởng mình thắng đậm dự án thế kỷ, thực chất đang mua phải bãi rác hóa chất nợ ngập đầu.",
        "example": "'Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm.'",
        "strategy_a_flash": "Tiếng búa gõ cắc một trăm hai mươi tỷ cho bãi rác hóa chất vừa dứt, tôi thong thả buông biển đấu giá xuống mặt bàn bọc nhung đỏ.",
        "strategy_b_detailed": "Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm. Bạch Ngưng Băng ngồi ở hàng ghế VIP đối diện nở nụ cười đắc thắng, giơ cao biển đấu giá một trăm tỷ cho mảnh đất hoang phía nam thành phố. Ả ta không hề biết rằng, dưới lớp cát sâu mười mét của khu đất đó là bãi rác thải hóa chất công nghiệp bị chôn lấp trái phép từ hai mươi năm trước.",
        "best_for": ["TRONG_SINH", "VA_MAT", "HAO_MON"]
    },
    {
        "archetype_id": 7,
        "name": "Dược lý thâm cung & Ngự y cơ mật (Palace Toxicology Hook)",
        "type": "Dược lý thâm cung & Ngự y cơ mật",
        "sensory_anchor": "Trâm bạc nhúng chén hoa cúc sủi bọt xám tro, hương long diên ngạt mũi, tay áo thêu chỉ vàng",
        "desc": "Sự tàn khốc chốn hậu cung được ngụy trang bằng phép tắc và nụ cười hòa nhã của bậc mẫu nghi.",
        "example": "'Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng.'",
        "strategy_a_flash": "Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng.",
        "strategy_b_detailed": "Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng. Thục phi vẫn mỉm cười dịu dàng nâng tách trà lên môi tôi: 'Uống đi con dâu, trà nguội mất ngon'. Dưới ống tay áo thêu chim phượng bằng chỉ vàng lấp lánh, ngón tay đeo móng bạc của bà ta đang khẽ gõ nhịp xuống thành ghế đàn hương, từng nhịp từng nhịp như hồi chuông đòi mạng.",
        "best_for": ["CUNG_DAU", "TRACH_DAU", "NGUOC_TAM"]
    },
    {
        "archetype_id": 8,
        "name": "Âm thanh rợn gáy kinh dị đô thị (Acoustic Urban Horror Hook)",
        "type": "Âm thanh rợn gáy kinh dị đô thị",
        "sensory_anchor": "Tiếng cào móng tay khô khốc dưới dát giường gỗ ép, giọt nước bùn ao rỉ trán, căn hộ tầng bảy không cửa sổ",
        "desc": "Ám ảnh không gian kín và vật lý phi lý trí tại các tòa chung cư cũ hoặc phòng trọ sinh viên.",
        "example": "'Tiếng cào móng tay khô khốc dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh nhỏ thẳng vào giữa trán tôi, mang theo mùi bùn ao tanh tưởi.'",
        "strategy_a_flash": "Tiếng cào móng tay dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh mang mùi bùn ao nhỏ thẳng vào giữa trán tôi.",
        "strategy_b_detailed": "Tiếng cào móng tay khô khốc dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh nhỏ thẳng vào giữa trán tôi, mang theo mùi bùn ao tanh tưởi giữa căn hộ tầng bảy không có cửa sổ. Tôi nín thở, ngón tay bấu chặt vào thanh sắt lan can giường tầng, cố ngăn chiếc răng hàm va vào nhau cầm cập khi nhìn thấy năm ngón tay tím tái đang từ từ luồn qua kẽ ván gỗ.",
        "best_for": ["KINH_DI", "QUAI_DAM", "VO_HAN"]
    },
    {
        "archetype_id": 9,
        "name": "Vật chứng số & Bẻ gãy cơ học học đường (Academic Whistleblower Hook)",
        "type": "Vật chứng số & Bẻ gãy cơ học học đường",
        "sensory_anchor": "Vỏ bút dạ quang vàng gãy làm đôi, thẻ nhớ micro SD 32GB rơi xuống bàn, màn hình in đề thi",
        "desc": "Xung đột trí tuệ học đường khốc liệt: bóc trần đường dây gian lận bằng dữ liệu số và chứng cứ vật lý.",
        "example": "'Vỏ bút dạ quang vừa bẻ gãy rơi chiếc thẻ nhớ ba mươi hai gigabyte chứa camera quay lén phòng in đề thi, tiếng chuông báo giờ thi học bổng đã vang lên.'",
        "strategy_a_flash": "Vỏ bút dạ quang vừa bẻ gãy rơi chiếc thẻ nhớ ba mươi hai gigabyte chứa camera quay lén phòng in đề thi, tiếng chuông báo giờ thi học bổng đã vang lên.",
        "strategy_b_detailed": "Rắc! Thân bút dạ quang màu vàng chanh gãy làm đôi dưới lực bấm của tôi, làm rơi ra chiếc thẻ nhớ micro SD ba mươi hai gigabyte chứa toàn bộ video quay lén phòng in đề thi quốc gia. Thủ khoa khối tự nhiên ngồi bàn trên quay ngoắt lại, cây bút chì kim hai bê trên tay hắn gãy vụn khi nhìn thấy chiếc đầu đọc thẻ nhớ đang cắm thẳng vào cổng USB chiếc máy tính giám thị.",
        "best_for": ["CUU_ROI", "THANH_XUAN", "TRINH_THAM"]
    },
    {
        "archetype_id": 10,
        "name": "Tử huyệt kiểm toán & Niêm phong con dấu (Corporate Forensic Seal Hook)",
        "type": "Tử huyệt kiểm toán & Niêm phong con dấu",
        "sensory_anchor": "Mũi kéo inox bấm đứt chỉ sáp đỏ niêm phong, tập hồ sơ ba mươi tỷ, còi xe thanh tra thuế rú dưới sảnh",
        "desc": "Thương trường khốc liệt: đòn kết liễu vào phút chót bằng niêm phong kiểm toán độc lập và cơ quan chức năng.",
        "example": "'Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong trên tập hồ sơ ba mươi tỷ, tiếng còi xe thanh tra thuế đã rú lên dưới sảnh.'",
        "strategy_a_flash": "Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong trên tập hồ sơ ba mươi tỷ, tiếng còi xe thanh tra thuế đã rú lên dưới sảnh.",
        "strategy_b_detailed": "Tách! Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong sáp đỏ trên tập hồ sơ chuyển giá ba mươi tỷ, tiếng còi xe thanh tra thuế và cảnh sát kinh tế đã rú lên inh ỏi dưới sảnh chính tòa nhà sáu mươi tầng. Vị tổng giám đốc vừa giơ ly rượu mừng bỗng khựng lại, giọt vang đỏ sóng sánh sánh tràn qua mép ly, nhỏ từng giọt đặc quánh xuống chiếc cà vạt lụa Hermes đắt giá của ông ta.",
        "best_for": ["HAO_MON", "VA_MAT", "TRONG_SINH"]
    }
]

# Alias tương thích ngược cho các module cũ
OPENING_HOOK_TEMPLATES_6 = DIVERSE_HOOK_ARCHETYPES_10[:6]

# ==============================================================================
# 3B. MA TRẬN 10 VŨ TRỤ NHÂN VẬT ĐỘC BẢN (10 CHARACTER UNIVERSES)
# ==============================================================================
# Đảm bảo các audio liên tiếp không bị lặp tên nhân vật hay bối cảnh nghề nghiệp
CHARACTER_UNIVERSES_10 = [
    {
        "universe_id": 1,
        "name": "Kiểm Toán Điều Tra & Thị Trường Vốn (Forensic Finance)",
        "domain": "Kiểm toán, ngân hàng đầu tư, chứng khoán",
        "protagonist_names": ["Thẩm Tri Ý", "Phó Trầm Uyên", "Cố Hàn Châu"],
        "antagonist_names": ["Hoàng Minh Triết", "Bà Mai", "Lục Vĩ Khang"],
        "supporting_names": ["Trưởng ban thanh tra Tề", "Luật sư Trần Bách"],
        "conflict_axis": "Chuyển giá xuyên biên giới & Thao túng phát hành trái phiếu",
        "best_for": ["HAO_MON", "ME_CHONG", "TRONG_SINH"]
    },
    {
        "universe_id": 2,
        "name": "Vi Phẫu Thần Kinh & Cấp Cứu Y Khoa (Neuro-Surgical Unit)",
        "domain": "Bệnh viện tuyến cuối, ghép tạng, tế bào gốc",
        "protagonist_names": ["Bác sĩ Lương Thế Vinh", "Bác sĩ Nhã Uyên"],
        "antagonist_names": ["Viện phó Chu Bá Khiêm", "Bác sĩ trưởng Doãn Hạo"],
        "supporting_names": ["Điều dưỡng trưởng Mỹ Linh", "Bệnh nhân lão tướng Phan"],
        "conflict_axis": "Đánh cắp bằng sáng chế mổ vi phẫu & Giả mạo chữ ký hồ sơ hiến tạng",
        "best_for": ["HUYEN_NGHI", "CUU_ROI", "NGUOC_TAM"]
    },
    {
        "universe_id": 3,
        "name": "Boong Ke Kỷ Băng Hà & Kỹ Thuật Sinh Tồn (Arctic Survival)",
        "domain": "Hầm ngầm công nghệ cao, cực hàn mạt thế",
        "protagonist_names": ["Kỹ sư cơ điện Trần Minh", "Nhà nông học Lê Na"],
        "antagonist_names": ["Đội trưởng tuần tra Tiêu Trạch", "Ả em họ Diệp Nhi"],
        "supporting_names": ["Bác sĩ già Nhậm", "Robot giám sát Alpha"],
        "conflict_axis": "Chiếm đoạt nguồn tuần hoàn nhiệt & Phá hoại chốt xả khí độc cách ly",
        "best_for": ["VO_HAN", "MAT_THE", "KINH_DI"]
    },
    {
        "universe_id": 4,
        "name": "Đội Tuyển Olympic Khoa Học Học Đường (Elite Academy)",
        "domain": "Trường nội trú trọng điểm, kỳ thi quốc gia",
        "protagonist_names": ["Nữ sinh nội trú Hạ Vy", "Thiên tài toán học Khang Duy"],
        "antagonist_names": ["Hội trưởng hội học sinh Trịnh Phong", "Tôn phu nhân"],
        "supporting_names": ["Thầy phụ trách in đề Trịnh Hưng", "Giám thị Đỗ"],
        "conflict_axis": "Đường dây tuồn đề thi quốc gia & Tống tiền bằng clip camera giấu kín",
        "best_for": ["CUU_ROI", "THANH_XUAN", "TRINH_THAM"]
    },
    {
        "universe_id": 5,
        "name": "Phục Chế Cổ Vật & Giám Định Ngọc (Heritage Restoration)",
        "domain": "Viện bảo tàng quốc gia, đấu giá cổ vật",
        "protagonist_names": ["Nhà phục chế Nguyễn Hoài Nam", "Nghệ nhân tranh lụa Lâm Diệp"],
        "antagonist_names": ["Trùm buôn đồ giả cổ Tống Khắc Lương", "Đấu giá viên Triệu Phàm"],
        "supporting_names": ["Giáo sư khảo cổ Trần Quốc Bảo", "Lão thợ kim hoàn họ Bùi"],
        "conflict_axis": "Tráo đổi ngọc tỉ truyền quốc bằng đá bột ép polymer phát quang",
        "best_for": ["HUYEN_NGHI", "VA_MAT", "TRONG_SINH"]
    },
    {
        "universe_id": 6,
        "name": "Tàu Hàng Container Viễn Dương (Deep Ocean Cargo)",
        "domain": "Hải trình quốc tế, siêu bão biển sâu",
        "protagonist_names": ["Hoa tiêu trưởng Vũ Đình", "Máy trưởng Quốc Huy"],
        "antagonist_names": ["Thuyền trưởng Đỗ Hồng Long", "Thủy thủ trưởng Sầm Hào"],
        "supporting_names": ["Thủy thủ trẻ Hải Đăng", "Bác sĩ tàu viễn dương"],
        "conflict_axis": "Vận chuyển công-ten-nơ rác phóng xạ trái phép qua vùng biển bão cấp 12",
        "best_for": ["VO_HAN", "HUYEN_NGHI", "KINH_DI"]
    },
    {
        "universe_id": 7,
        "name": "Thái Y Viện & Dược Điển Cung Đình (Imperial Pharmacy)",
        "domain": "Hoàng cung, ngự dược phòng, Đông cung",
        "protagonist_names": ["Nữ ngự y Diệp Uyển Thanh", "Tướng quân Tiêu Khải"],
        "antagonist_names": ["Thục phi Nhan Ngọc Dao", "Thái y viện trưởng Cố Đức Thuận"],
        "supporting_names": ["Cung nữ thân tín Như Ngọc", "Thái tử Tiêu Cảnh Hoan"],
        "conflict_axis": "Dùng độc hoa cà độc dược tẩm vào bánh hoa cúc hãm hại hoàng tự",
        "best_for": ["CUNG_DAU", "TRACH_DAU", "NGUOC_TAM"]
    },
    {
        "universe_id": 8,
        "name": "Khách Sạn Năm Sao & Ẩm Thực Michelin (Luxury Hospitality)",
        "domain": "Đại tiệc ngoại giao, bếp trưởng quốc tế",
        "protagonist_names": ["Giám đốc vận hành Đoàn Bảo Ngọc", "Bếp trưởng Henry Vũ"],
        "antagonist_names": ["Chủ tịch tập đoàn ẩm thực Doãn Thế Hào", "Thanh tra ẩm thực Pierre Đỗ"],
        "supporting_names": ["Phụ bếp trung thành Tiểu Lâm", "Nhà phê bình tự do Mai Phương"],
        "conflict_axis": "Cố tình pha chất gây sốc phản vệ vào món tráng miệng yến tiệc quốc tế",
        "best_for": ["HAO_MON", "SA_DIEU", "VA_MAT"]
    },
    {
        "universe_id": 9,
        "name": "An Ninh Dữ Liệu Số & Mạng Đám Mây (Cyber Forensics)",
        "domain": "Trung tâm an ninh mạng tài chính",
        "protagonist_names": ["Chuyên gia dấu vết số Đặng Quốc Phong", "Nữ hacker mũ trắng Minh Khuê"],
        "antagonist_names": ["Giám đốc công nghệ Tạ Quang", "Hacker chợ đen Bóng Đêm"],
        "supporting_names": ["Trưởng phòng máy chủ Bác Ba", "Cán bộ Cục An ninh mạng"],
        "conflict_axis": "Cài mã độc đào coin và đánh cắp mã OTP của ba triệu người dùng ví điện tử",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM", "VA_MAT"]
    },
    {
        "universe_id": 10,
        "name": "Lưu Trữ Điện Ảnh & Buồng Chiếu Phim Cũ (Cinema Archive)",
        "domain": "Rạp chiếu bóng cổ, bảo tàng phim nhựa",
        "protagonist_names": ["Kỹ thuật viên buồng chiếu Trần Hạo", "Biên kịch độc lập Băng Châu"],
        "antagonist_names": ["Nhà đầu tư giải tỏa Chu Văn Hùng", "Bảo vệ ca đêm Quách Tử"],
        "supporting_names": ["Nghệ nhân lồng tiếng Hoàng Lâm", "Cô bé bán vé dạo"],
        "conflict_axis": "Cuộn phim nhựa 35mm quay lại hiện trường vụ án mạng phòng kín 25 năm trước",
        "best_for": ["KINH_DI", "QUAI_DAM", "HUYEN_NGHI"]
    }
]

# ==============================================================================
# 3C. MA TRẬN 10 CƠ CHẾ KẾT THÚC & LẬT KÈO ĐỘC BẢN (10 DIVERSE RESOLUTIONS)
# ==============================================================================
# Chấm dứt triệt để việc truyện nào cũng kết thúc bằng "công an ập vào" hoặc "thanh tra thuế"
DIVERSE_RESOLUTIONS_10 = [
    {
        "resolution_id": 1,
        "name": "Cháy tài khoản ký quỹ đòn bẩy (Margin Call Liquidation)",
        "mechanism": "Phản diện dốc toàn lực đầu cơ khống, nhân vật chính tháo gỡ đòn bẩy khiến đối phương phá sản tức thì sau 30 giây công bố số liệu.",
        "best_for": ["HAO_MON", "VA_MAT"]
    },
    {
        "resolution_id": 2,
        "name": "Đảo ngược quy tắc sinh tồn (Rule Inversion Trap)",
        "mechanism": "Kích hoạt điều khoản ngầm số 0 trong quy tắc, biến chính kẻ đi săn thành con mồi chịu hình phạt trong không gian kín.",
        "best_for": ["KINH_DI", "QUAI_DAM", "VO_HAN"]
    },
    {
        "resolution_id": 3,
        "name": "Phát trực tiếp dữ liệu ẩn lên màn hình quảng trường (Digital Forensic Stream)",
        "mechanism": "Dữ liệu camera ngầm và ghi âm giao dịch bẩn được truyền phát tự động lên màn hình LED giữa tiệc mừng, không thể cắt sóng.",
        "best_for": ["ME_CHONG", "TRONG_SINH"]
    },
    {
        "resolution_id": 4,
        "name": "Giám định chuỗi gien và vết sáp niêm phong cổ (Forensic Pathology Match)",
        "mechanism": "Vết mực niêm phong và ADN trên di vật lịch sử chỉ ra kẻ giả mạo huyết thống ngay trước hội đồng gia tộc.",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM"]
    },
    {
        "resolution_id": 5,
        "name": "Kích hoạt thư tín thác công chứng 15 năm trước (Time Capsule Will)",
        "mechanism": "Bản di chúc gửi tại ngân hàng Thụy Sĩ có hiệu lực tự động khi phát sinh giao dịch bất thường, vô hiệu hóa toàn bộ quyền sở hữu giả mạo.",
        "best_for": ["NGUOC_TAM", "CUU_ROI"]
    },
    {
        "resolution_id": 6,
        "name": "Phản ứng đổi màu của giấy quỳ thử độc (Chemical Toxic Indicator)",
        "mechanism": "Giọt nước canh nhỏ lên vạt áo thêu ngự ban chuyển sang màu tím than, làm bại lộ thuốc độc ngay trước mặt sứ thần các nước.",
        "best_for": ["CUNG_DAU", "TRACH_DAU"]
    },
    {
        "resolution_id": 7,
        "name": "Trích xuất nhật ký truy cập máy chủ 2h sáng (Server Audit Log Extraction)",
        "mechanism": "Địa chỉ MAC máy tính cá nhân và dấu vân tay trên máy photocopy in đề thi bóc trần thủ phạm gian lận trước hội đồng tuyển sinh.",
        "best_for": ["THANH_XUAN", "CUU_ROI"]
    },
    {
        "resolution_id": 8,
        "name": "Đóng sập cửa áp suất cơ học cách ly (Pressure Isolation Containment)",
        "mechanism": "Khóa van điều áp cô lập kẻ phản trắc ở khoang ngoài khi bão tuyết ập tới, bảo toàn toàn bộ hệ thống dự trữ cho người vô tội.",
        "best_for": ["MAT_THE", "VO_HAN"]
    },
    {
        "resolution_id": 9,
        "name": "Phán quyết hủy giao dịch do lừa dối (Civil Fraud Void Judgment)",
        "mechanism": "Tòa án tuyên bố hợp đồng tặng cho tài sản vô hiệu từ thời điểm xác lập do có hành vi gian dối, thu hồi từng xu tiền bất chính.",
        "best_for": ["GIA_DAU", "ME_CHONG"]
    },
    {
        "resolution_id": 10,
        "name": "Tự thú vì hiểu lầm tiếng lòng là thần dụ (Satirical Psychological Collapse)",
        "mechanism": "Phản diện tưởng bí mật sát hại của mình đã bị thần linh soi xét qua tiếng lòng của nhân vật chính, tự khai ra toàn bộ đồng bọn trước hội trường.",
        "best_for": ["SA_DIEU", "HAI_HUOC"]
    }
]"""

# Normalize newlines for replacement
text_norm = text.replace("\r\n", "\n")
old_hook_norm = old_hook_block.replace("\r\n", "\n")
assert old_hook_norm in text_norm, "Old hook block not found in normalized text!"
text_norm = text_norm.replace(old_hook_norm, new_hook_block)

# 2. Update query_masterclass to select diverse hook, universe, resolution and rotate
old_query_tail = """        # Chọn template hook tương thích nhất
        matched_hook_template = OPENING_HOOK_TEMPLATES_6[0]
        for ht in OPENING_HOOK_TEMPLATES_6:
            if any(gk in ht["best_for"] for gk in target_genre_keys):
                matched_hook_template = ht
                break

        return {
            "status": "CONSULTED_SUCCESS",
            "total_knowledge_pool": self.total_stories,
            "target_genres": target_genre_keys,
            "relevant_cases": brief_cases,
            "golden_rules": GOLDEN_RULES_10,
            "recommended_hook_template": matched_hook_template,
            "satisfaction_matrix": SATISFACTION_MATRIX_5,
            "villain_system": VILLAIN_SYSTEM_4,
            "information_asymmetry": INFORMATION_ASYMMETRY_MODEL,"""

new_query_tail = """        # 4. CHỐNG ĐỒNG HÓA & LỰA CHỌN ĐỘC BẢN (ANTI-HOMOGENIZATION ENGINE):
        # A. Chọn Hook Archetype (Ưu tiên thể loại, loại trừ các ID đã dùng gần đây)
        exclude_archetypes = exclude_archetype_ids or []
        compatible_hooks = [h for h in DIVERSE_HOOK_ARCHETYPES_10 if any(gk in h["best_for"] for gk in target_genre_keys)]
        if not compatible_hooks:
            compatible_hooks = DIVERSE_HOOK_ARCHETYPES_10

        fresh_hooks = [h for h in compatible_hooks if h["archetype_id"] not in exclude_archetypes]
        matched_hook_archetype = fresh_hooks[0] if fresh_hooks else compatible_hooks[0]

        # B. Chọn Vũ Trụ Nhân Vật (10 Character Universes, loại trừ ID đã dùng gần đây)
        exclude_universes = exclude_universe_ids or []
        compatible_universes = [u for u in CHARACTER_UNIVERSES_10 if any(gk in u.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_universes:
            compatible_universes = CHARACTER_UNIVERSES_10
        fresh_universes = [u for u in compatible_universes if u["universe_id"] not in exclude_universes]
        matched_universe = fresh_universes[0] if fresh_universes else compatible_universes[0]

        # C. Chọn Cơ Chế Lật Kèo Độc Bản (10 Diverse Resolutions)
        exclude_res = exclude_resolution_ids or []
        compatible_res = [r for r in DIVERSE_RESOLUTIONS_10 if any(gk in r.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_res:
            compatible_res = DIVERSE_RESOLUTIONS_10
        fresh_res = [r for r in compatible_res if r["resolution_id"] not in exclude_res]
        matched_resolution = fresh_res[0] if fresh_res else compatible_res[0]

        return {
            "status": "CONSULTED_SUCCESS",
            "total_knowledge_pool": self.total_stories,
            "target_genres": target_genre_keys,
            "relevant_cases": brief_cases,
            "golden_rules": GOLDEN_RULES_10,
            "recommended_hook_template": matched_hook_archetype,
            "recommended_hook_archetype": matched_hook_archetype,
            "recommended_character_universe": matched_universe,
            "recommended_resolution": matched_resolution,
            "diverse_hooks_catalog": DIVERSE_HOOK_ARCHETYPES_10,
            "character_universes_catalog": CHARACTER_UNIVERSES_10,
            "diverse_resolutions_catalog": DIVERSE_RESOLUTIONS_10,
            "satisfaction_matrix": SATISFACTION_MATRIX_5,
            "villain_system": VILLAIN_SYSTEM_4,
            "information_asymmetry": INFORMATION_ASYMMETRY_MODEL,"""

old_query_tail_norm = old_query_tail.replace("\r\n", "\n")
assert old_query_tail_norm in text_norm, "old_query_tail not found in normalized text!"
text_norm = text_norm.replace(old_query_tail_norm, new_query_tail)

# 2.1 Update query_masterclass method signature to accept exclusion parameters
old_sig = """    def query_masterclass(
        self,
        topic_title: str = "",
        topic_summary: str = "",
        category: Optional[VideoCategory] = None,
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:"""

new_sig = """    def query_masterclass(
        self,
        topic_title: str = "",
        topic_summary: str = "",
        category: Optional[VideoCategory] = None,
        top_k: int = 3,
        genre_hint: str = "",
        exclude_archetype_ids: Optional[List[int]] = None,
        exclude_universe_ids: Optional[List[int]] = None,
        exclude_resolution_ids: Optional[List[int]] = None
    ) -> Dict[str, Any]:"""

old_sig_norm = old_sig.replace("\r\n", "\n")
assert old_sig_norm in text_norm, "old_sig not found in normalized text!"
text_norm = text_norm.replace(old_sig_norm, new_sig)

# 3. Update consult_before_writing to load recent history for dynamic rotation
old_consult = """    def consult_before_writing(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:
        \"\"\"
        Hàm bắt buộc gọi trước khi biên soạn bất kỳ kịch bản nào.
        Thực hiện tra cứu, lập kế hoạch chỉ dẫn và lưu vết audit log vào data/knowledge_consultations.jsonl.
        Gắn kèm consultation_token duy nhất để làm thẻ bài thông qua Cổng Kiểm Duyệt Tri Thức.
        \"\"\"
        brief = self.query_masterclass(
            topic_title=topic_title,
            topic_summary=topic_summary,
            category=category,
            top_k=top_k,
            genre_hint=genre_hint
        )

        token = f"TOKEN_KB_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.urandom(4).hex()}"
        brief["consultation_token"] = token
        brief["consulted_at"] = datetime.now().isoformat()

        # Ghi log lịch sử tra cứu (Audit Trail)
        consult_log_path = root_dir / "data" / "knowledge_consultations.jsonl"
        consult_log_path.parent.mkdir(parents=True, exist_ok=True)

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "consultation_token": token,
            "query_title": topic_title,
            "target_genres": brief.get("target_genres", []),
            "matched_cases": [c["title"] for c in brief.get("relevant_cases", [])],
            "status": "VERIFIED_BEFORE_WRITING"
        }

        try:
            with open(consult_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\\n")
        except Exception as e:
            logger.warning(f"Không thể ghi log consultation: {e}")

        return brief"""

new_consult = """    def consult_before_writing(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:
        \"\"\"
        Hàm bắt buộc gọi trước khi biên soạn bất kỳ kịch bản nào.
        Tự động tra cứu lịch sử các audio gần nhất để xoay vòng Hook Archetype, Vũ trụ nhân vật và Cơ chế lật kèo,
        triệt tiêu 100% tình trạng các audio bị na ná hay lặp lại mô-típ.
        Gắn kèm consultation_token duy nhất để làm thẻ bài thông qua Cổng Kiểm Duyệt Tri Thức.
        \"\"\"
        consult_log_path = root_dir / "data" / "knowledge_consultations.jsonl"
        recent_archetypes: List[int] = []
        recent_universes: List[int] = []
        recent_resolutions: List[int] = []

        if consult_log_path.exists():
            try:
                with open(consult_log_path, "r", encoding="utf-8") as f:
                    lines = [ln.strip() for ln in f if ln.strip()]
                for line in lines[-6:]:
                    try:
                        record = json.loads(line)
                        if record.get("hook_archetype_id"):
                            recent_archetypes.append(record["hook_archetype_id"])
                        if record.get("universe_id"):
                            recent_universes.append(record["universe_id"])
                        if record.get("resolution_id"):
                            recent_resolutions.append(record["resolution_id"])
                    except Exception:
                        pass
            except Exception as e:
                logger.debug(f"Không thể đọc lịch sử consultation: {e}")

        brief = self.query_masterclass(
            topic_title=topic_title,
            topic_summary=topic_summary,
            category=category,
            top_k=top_k,
            genre_hint=genre_hint,
            exclude_archetype_ids=recent_archetypes,
            exclude_universe_ids=recent_universes,
            exclude_resolution_ids=recent_resolutions
        )

        token = f"TOKEN_KB_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.urandom(4).hex()}"
        brief["consultation_token"] = token
        brief["consulted_at"] = datetime.now().isoformat()

        # Ghi log lịch sử tra cứu (Audit Trail)
        consult_log_path.parent.mkdir(parents=True, exist_ok=True)
        hook_obj = brief.get("recommended_hook_archetype", {})
        univ_obj = brief.get("recommended_character_universe", {})
        res_obj = brief.get("recommended_resolution", {})

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "consultation_token": token,
            "query_title": topic_title,
            "target_genres": brief.get("target_genres", []),
            "matched_cases": [c["title"] for c in brief.get("relevant_cases", [])],
            "hook_archetype_id": hook_obj.get("archetype_id"),
            "hook_archetype_name": hook_obj.get("name"),
            "universe_id": univ_obj.get("universe_id"),
            "universe_name": univ_obj.get("name"),
            "resolution_id": res_obj.get("resolution_id"),
            "resolution_name": res_obj.get("name"),
            "status": "VERIFIED_BEFORE_WRITING"
        }

        try:
            with open(consult_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\\n")
        except Exception as e:
            logger.warning(f"Không thể ghi log consultation: {e}")

        return brief"""

old_consult_norm = old_consult.replace("\r\n", "\n")
assert old_consult_norm in text_norm, "old_consult not found in normalized text!"
text_norm = text_norm.replace(old_consult_norm, new_consult)

# 4. Update format_brief_for_prompt to include Hook Archetype, Universe, and Resolution
old_format = """        lines.append("\\n🎯 10 ĐỊNH LUẬT VÀNG BẮT BUỘC ÁP DỤNG:")"""
new_format = """        hook_rec = brief.get("recommended_hook_archetype", {})
        univ_rec = brief.get("recommended_character_universe", {})
        res_rec = brief.get("recommended_resolution", {})

        if hook_rec:
            lines.append(f"\\n⚡ [ARCHETYPE MỞ ĐẦU ĐỘC BẢN ĐƯỢC CHỈ ĐỊNH]: {hook_rec.get('name')}")
            lines.append(f" * Neo đậu giác quan: {hook_rec.get('sensory_anchor')}")
            lines.append(f" * Mẫu Chiến thuật A (Thoáng qua 12-20 từ): {hook_rec.get('strategy_a_flash')}")
            lines.append(f" * Mẫu Chiến thuật B (Chi tiết cận cảnh 25-45 từ): {hook_rec.get('strategy_b_detailed')}")

        if univ_rec:
            lines.append(f"\\n🎭 [VŨ TRỤ NHÂN VẬT ĐỘC BẢN ĐƯỢC CHỈ ĐỊNH - CHỐNG TRÙNG LẶP]: {univ_rec.get('name')}")
            lines.append(f" * Lĩnh vực bối cảnh: {univ_rec.get('domain')}")
            lines.append(f" * Nhân vật chính đề xuất: {', '.join(univ_rec.get('protagonist_names', []))}")
            lines.append(f" * Phản diện đề xuất: {', '.join(univ_rec.get('antagonist_names', []))}")
            lines.append(f" * Trục xung đột cốt lõi: {univ_rec.get('conflict_axis')}")

        if res_rec:
            lines.append(f"\\n💥 [CƠ CHẾ LẬT KÈO ĐỘC BẢN - CHỐNG CÔNG AN/THUẾ RẬP KHUÔN]: {res_rec.get('name')}")
            lines.append(f" * Cơ chế: {res_rec.get('mechanism')}")

        lines.append("\\n🎯 10 ĐỊNH LUẬT VÀNG BẮT BUỘC ÁP DỤNG:")"""

old_format_norm = old_format.replace("\r\n", "\n")
assert old_format_norm in text_norm, "old_format not found in normalized text!"
text_norm = text_norm.replace(old_format_norm, new_format)

# Write back preserving CRLF
with open("core/knowledge_base.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text_norm)

print("Successfully updated core/knowledge_base.py with CRLF!")
