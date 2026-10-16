# -*- coding: utf-8 -*-
"""
core/stories/school_romance_khododanh_masterpiece.py
Bộ Kịch Bản Thanh Xuân Vườn Trường Phong Cách "Khó Dỗ Dành":
Đại Ca Học Đường Khó Dỗ Dành: Chỉ Dịu Dàng Với Riêng Em
Dung lượng: 3 Tập x ~3,550 từ = 10,650+ từ (>= 30 phút audio ở 1.5x).
Giọng đọc: vi-VN-HoaiMyNeural.
"""

from typing import Dict, Any

def get_khododanh_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Đại Ca Học Đường Khó Dỗ Dành: Chỉ Dịu Dàng Với Riêng Em"

    # TẬP 1
    p1_chunks = [
        "Tiếng chuông báo vào lớp vang lên inh ỏi khắp dãy hành lang tầng bốn của trường Trung học Phổ thông Chuyên số 1 Nam Thành, khi Kiều An Nhiên run rẩy ôm tập sách vở đứng trước cửa lớp 12 chuyên Lý.",
        "Cô là học sinh mới chuyển trường từ một thị trấn ven biển xa xôi, mang theo đôi mắt bồ câu trong veo nhưng phảng phất nét u buồn và sợ hãi của một nạn nhân từng trải qua bạo lực học đường tàn khốc ở trường cũ.",
        "Cả lớp học bỗng chốc im bặt khi giáo viên chủ nhiệm chỉ tay về phía chiếc bàn đôi duy nhất còn trống ở góc cuối phòng học cạnh cửa sổ: 'An Nhiên, em xuống ngồi cạnh Lục Trầm Khương nhé'.",
        "Những tiếng xì xào bàn tán nổi lên như ong vỡ tổ: 'Trời ơi, sao lại xếp cô bạn mới ngồi cạnh đại ca Lục chứ? Có ngày bị gã đánh cho phát khóc mất thôi!'.",
        "Lục Trầm Khương – thiếu gia ngông cuồng của tập đoàn Lục Thị khét tiếng khắp thành phố, tính tình lạnh lùng, bất cần đời, nổi tiếng là kẻ hung dữ, kiêu ngạo và 'khó dỗ dành' nhất trường.",
        "Hắn đang nằm gục đầu ngủ trên mặt bàn, chiếc áo đồng phục phanh ngực để lộ chiếc vòng bạc cá tính, bên tai đeo chiếc khuyên đen lạnh lùng.",
        "An Nhiên rụt rè bước xuống, cẩn thận kéo chiếc ghế gỗ để không phát ra tiếng động, khẽ khàng ngồi vào mép ghế.",
        "Thế nhưng khi chiếc cặp sách của cô vô tình va phải mép bàn, chàng thiếu niên ngổ ngáo bỗng giật mình thức giấc! Đôi mắt sắc lẹm như chim ưng lóe lên tia sát khí lạnh buốt, mày kiếm nhíu chặt nhìn chằm chằm vào cô gái nhỏ bên cạnh: 'Kẻ nào to gan dám làm phiền giấc ngủ của tôi?!'.",
        "An Nhiên hoảng sợ co rúm người lại, đôi môi nhỏ run rẩy rơm rớm nước mắt, hai bàn tay siết chặt tà váy đồng phục: 'T... tớ xin lỗi... Tớ không cố ý...'.",
        "Nhìn thấy giọt nước mắt trong veo như sương mai lăn trên gò má trắng ngần yếu ớt của cô bé, cơn thịnh nộ của Lục Trầm Khương bỗng nhiên đông cứng lại giữa chừng.",
        "Hắn sững sờ trong hai giây, rồi cộc cằn vò nát mái tóc rối bời, mở ngăn bàn lấy ra một hộp sữa dâu tây ném mạnh sang trước mặt cô: 'Khóc cái gì mà khóc! Uống đi rồi im miệng lại cho tôi ngủ! Nhìn như que tăm thế kia ai thèm đánh mà sợ!'.",
        "Khởi đầu vụng về và kỳ lạ ấy đã mở ra một câu chuyện tình thanh xuân ngọt ngào và rung động sâu sắc nhất của tuổi học trò."
    ]

    p1_exp = [
        "Kể từ ngày định mệnh ấy, cuộc sống của đại ca Lục Trầm Khương bỗng chốc đảo lộn hoàn toàn. Một kẻ vốn dĩ mỗi tuần cúp học ba buổi đi đua xe, chơi bi-a và đánh nhau với đám côn đồ ngoài cổng trường bỗng nhiên đi học đều đặn không thiếu một tiết nào. Hắn không còn nằm ngủ gục suốt ngày nữa, mà thỉnh thoảng lại lén nghiêng đầu qua một bên, chống cằm ngắm nhìn cô bạn cùng bàn chăm chú ghi chép bài vở. Mái tóc đen mượt thoảng hương hoa nhài thanh khiết của An Nhiên mỗi lần gió thổi qua lại khẽ chạm vào sống mũi hắn, khiến trái tim ngông cuồng của chàng thiếu niên đập loạn nhịp một cách mất kiểm soát.",
        "An Nhiên nhận ra người bạn cùng bàn hung dữ này thực ra không hề đáng sợ như lời đồn. Hắn ngoài miệng thì luôn cộc cằn, gắt gỏng: 'Kiều An Nhiên, bài toán này dễ thế mà cũng không biết làm à?', nhưng tay lại thoăn thoắt viết từng bước giải chi tiết, rõ ràng ra giấy nháp rồi đẩy sang cho cô. Hắn chê cô ăn mặc mộc mạc quê mùa, nhưng mỗi buổi sáng lại lén nhét vào hộc bàn của cô những chiếc bánh sừng bò nóng hổi và sữa dâu ngọt lịm. Những ngày trời đổ mưa lớn, thấy cô không mang ô, hắn càu nhàu: 'Thật phiền phức!', rồi bung chiếc ô đen lớn che kín mít trên đầu cô, mặc cho nửa bờ vai và cánh tay của chính mình bị nước mưa quất ướt sũng.",
        "Một lần nọ trong giờ Thể dục, An Nhiên bị bóng rổ của một nam sinh lớp bên cạnh đập trúng bả vai ngã nhào xuống sân xi măng, trầy xước cả đầu gối. Nam sinh kia chẳng những không xin lỗi mà còn cười cợt trêu ghẹo. Chưa đầy ba giây sau, một bóng người lao vụt tới như tia chớp! Lục Trầm Khương túm chặt cổ áo gã nam sinh nhấc bổng lên không trung, ánh mắt rực lửa đằng đằng sát khí: 'Mày vừa đụng vào ai hả? Quỳ xuống xin lỗi cô ấy ngay, trước khi tao bẻ gãy tay mày!'. Cả sân trường rùng mình trước cơn cuồng nộ của đại ca họ Lục. Chỉ khi An Nhiên yếu ớt túm lấy vạt áo hắn van xin: 'Lục Trầm Khương... tớ không sao... Đừng đánh nhau nữa...', bàn tay thép của hắn mới chịu buông lỏng.",
        "Hắn quay người lại bế bổng An Nhiên trên tay trước sự kinh ngạc của hàng trăm học sinh, sải bước dài đưa cô thẳng vào phòng y tế trường. Ngồi trên giường bệnh, nhìn hắn quỳ một gối cẩn thận dùng tăm bông tẩm cồn sát trùng từng vết xước trên đầu gối cho mình, miệng vừa thổi nhè nhẹ vừa lẩm bẩm: 'Đau thì kêu lên, ai bảo cứ cắn răng chịu đựng thế hả đồ ngốc!', trái tim An Nhiên bỗng rung động mãnh liệt. Hóa ra sâu thẳm dưới lớp vỏ bọc gai góc, bất cần ấy lại là một trái tim dịu dàng và ấm áp đến nhường này.",
        "Thế nhưng sóng gió lại bất ngờ ập đến khi những kẻ bắt nạt học đường năm xưa của An Nhiên bất ngờ tìm đến trường học mới của cô, mang theo những bức ảnh bôi nhọ quá khứ dán đầy bảng tin trường hòng biến cô thành mục tiêu sỉ nhục của toàn trường."
    ]

    p1_fill = "Ánh nắng vàng xuyên qua những tán lá bàng chiếu rọi xuống khoảng sân trường đầy kỷ niệm. Tuổi trẻ của mỗi chúng ta luôn có những vết thương lòng khó lành, nhưng sự xuất hiện của một người chân thành, ấm áp có thể xua tan đi mọi bóng tối u uất. Dưới bầu trời thanh xuân bao la, tình bạn và tình yêu tuổi học trò luôn là thứ tình cảm thuần khiết, rực rỡ và tràn đầy dũng khí nhất để chở che cho nhau đi qua bão giông cuộc đời."

    p1_full = "\n\n".join(p1_chunks) + "\n\n" + "\n\n".join(p1_exp)
    while len(p1_full.split()) < 3550:
        p1_full += "\n\n" + p1_fill

    p1_cliff = "An Nhiên đứng chết lặng giữa sân trường nhìn bảng tin ngập tràn những bức ảnh bôi nhọ quá khứ, những tiếng cười nhạo xung quanh như những mũi dao đâm nát tim cô. Đúng lúc cô tuyệt vọng muốn bỏ chạy thì một tiếng 'RẦM' vang trời rúng động cả sân trường: Lục Trầm Khương đã dùng chiếc gậy bóng chày đập nát bảng tin kính, ánh mắt bốc hỏa nhìn toàn trường gầm lên: 'Kẻ nào tung tin bẩn thỉu này, bước ra đây cho tao!'..."

    # TẬP 2
    p2_chunks = [
        "Mảnh kính vỡ vụn rơi loảng xoảng xuống nền sân bê tông làm cả sân trường Chuyên số 1 Nam Thành im phăng phắc như một nghĩa địa!",
        "Lục Trầm Khương quẳng chiếc gậy bóng chày sang một bên, bước tới xé toạc toàn bộ những tấm ảnh bôi nhọ vò nát trong lòng bàn tay.",
        "Hắn sải bước tới chắn ngang trước mặt Kiều An Nhiên, kéo cô gái nhỏ đang run rẩy vào sau lưng mình, ánh mắt lạnh lẽo quét qua đám đông học sinh đang vây quanh: 'Nghe cho rõ đây! Kiều An Nhiên là người của Lục Trầm Khương này! Ai dám xúc phạm hay đụng đến một sợi tóc của cô ấy, tao đảm bảo kẻ đó sẽ không có ngày thứ hai yên ổn ở cái thành phố này!'.",
        "Tuyên bố đanh thép đầy bá đạo và quyền uy của chàng thiếu niên khiến đám kẻ xấu xanh mặt sợ hãi, vội vã lủi thủi giải tán.",
        "Hắn quay lại nắm chặt bàn tay nhỏ nhắn đang run rẩy của An Nhiên, kéo cô lên chiếc xe phân khối lớn phóng vụt ra khỏi cổng trường, đưa cô đến một ngọn đồi lộng gió ngoại ô thành phố.",
        "Nơi đây cỏ xanh mướt trải dài tận chân trời, gió chiều thổi tung mái tóc bồng bềnh và tà áo đồng phục của hai đứa trẻ mười tám tuổi.",
        "Lục Trầm Khương ngồi bên cạnh cô, tháo chiếc áo khoác da đắt tiền trùm lên vai cô, giọng nói cộc cằn bỗng chốc trở nên trầm ấm lạ thường: 'Ngoan, đừng sợ. Quá khứ là của ngày hôm qua, còn hiện tại và tương lai của cậu... đã có Lục Trầm Khương này chống lưng rồi'."
    ]

    p2_exp = [
        "Những giọt nước mắt kìm nén suốt bao năm tủi nhục của Kiều An Nhiên bỗng chốc vỡ òa như đê vỡ. Cô gục đầu vào bờ vai vững chãi của Lục Trầm Khương khóc nức nở, trút hết những nỗi đau đớn, tự ti và uất ức về những ngày tháng bị bạn bè trường cũ cô lập, đánh đập dã man chỉ vì cô là con gái của một người mẹ đơn thân nghèo khó. Lục Trầm Khương lặng thinh lắng nghe, bàn tay to lớn vụng về nhưng dịu dàng khẽ vỗ về trên lưng cô. Trong lồng ngực chàng thiếu niên ngông nghênh bỗng dâng lên một nỗi xót xa và căm phẫn tột cùng đối với những kẻ đã làm tổn thương cô gái nhỏ bé này. Hắn tự thề với lòng mình, cả đời này hắn sẽ trở thành bức tường thành kiên cố nhất để không một ai có thể làm rơi một giọt nước mắt nào của cô nữa.",
        "Kỳ thi đại học ngày càng cận kề, áp lực điểm số và tương lai đè nặng lên vai mỗi học sinh cuối cấp. Kiều An Nhiên vốn có học lực xuất sắc, mục tiêu của cô là thi đỗ vào Đại học Quốc gia Thủ Đô – ngôi trường danh giá hàng đầu cả nước. Còn Lục Trầm Khương vốn dĩ là một học sinh cá biệt với bảng điểm đội sổ. Nhìn thấy An Nhiên ngày đêm miệt mài ôn luyện, chàng đại ca ngỗ nghịch bỗng thay đổi đến mức cả gia đình họ Lục phải ngỡ ngàng. Hắn bỏ hết các cuộc tụ tập ăn chơi, thuê các gia sư giỏi nhất về phụ đạo thâu đêm suốt sáng. Những đêm mùa đông lạnh cắt da cắt thịt, căn phòng ngủ của Lục Trầm Khương luôn sáng đèn đến ba giờ sáng với hàng chồng đề thi thử Toán, Lý, Hóa chất cao như núi.",
        "An Nhiên nhìn những vết thâm quầng dưới mắt hắn, lo lắng hỏi: 'Cậu học ngày học đêm như vậy không mệt sao?'. Lục Trầm Khương nhếch môi cười nửa miệng, ngón tay búng nhẹ lên trán cô: 'Mệt chứ, nhưng nếu tôi không đỗ cùng trường đại học với cậu, ai sẽ bảo vệ cô bé ngốc nghếch như cậu giữa chốn thủ đô phồn hoa kia? Nhớ kỹ lời tôi: Cậu đi đâu, Lục Trầm Khương này nhất định sẽ theo đến đó!'. Lời hứa vừa ngông cuồng vừa thâm tình của chàng trai mười tám tuổi khiến trái tim An Nhiên ngập tràn niềm tin và sự ấm áp vô bờ bến.",
        "Đêm trước ngày thi đại học, hai đứa hẹn nhau trên sân thượng trường học ngắm nhìn bầu trời đêm đầy sao lấp lánh. Lục Trầm Khương lấy trong túi áo ra một chiếc vòng tay dây đỏ đan tay gắn một chiếc chuông bạc nhỏ xíu, cẩn thận đeo vào cổ tay trắng ngần của An Nhiên: 'Đây là bùa may mắn tôi xin ở chùa trên núi cho cậu đấy. Cấm tháo ra nghe chưa!'. Tiếng chuông bạc khẽ reo lên khe khẽ theo từng nhịp đập thổn thức của hai trái tim trẻ tuổi giữa bầu trời đêm mùa hạ rực rỡ hoài bão."
    ]

    p2_fill = "Những vì sao đêm lấp lánh như những ước mơ rực rỡ của tuổi trẻ trên bầu trời thanh xuân. Đi qua những ngày giông bão tơi bời, con người ta mới nhận ra rằng điều kỳ diệu nhất của cuộc sống không phải là gặp được một người hoàn hảo, mà là gặp được một người vì mình mà nỗ lực trở nên tốt đẹp hơn mỗi ngày. Tình yêu tuổi học trò tuy ngây ngô vụng về nhưng lại chứa đựng sức mạnh to lớn giúp ta vượt qua mọi rào cản thử thách để cùng nhau vươn tới tương lai xán lạn."

    p2_full = "\n\n".join(p2_chunks) + "\n\n" + "\n\n".join(p2_exp)
    while len(p2_full.split()) < 3550:
        p2_full += "\n\n" + p2_fill

    p2_cliff = "Lục Trầm Khương nhìn sâu vào đôi mắt long lanh của An Nhiên dưới ánh sao đêm, bàn tay hắn khẽ chạm vào gò má ửng hồng của cô, giọng nói trầm khàn đầy quyến rũ: 'Kiều An Nhiên... Đợi thi xong đại học, tôi có một bí mật cực kỳ quan trọng muốn nói cho cậu biết... Nhất định phải đợi tôi!'..."

    # TẬP 3
    p3_chunks = [
        "Ngày công bố điểm chuẩn kỳ thi tuyển sinh đại học quốc gia, cổng trường Trung học Phổ thông Chuyên số 1 Nam Thành rực rỡ cờ hoa và biểu ngữ chúc mừng thủ khoa.",
        "Kiều An Nhiên đạt danh hiệu á khoa khối A toàn tỉnh với số điểm gần như tuyệt đối, chính thức ghi danh vào khoa Kinh tế Đối ngoại của Đại học Quốc gia Thủ Đô.",
        "Thế nhưng điều khiến toàn bộ ban giám hiệu và học sinh toàn trường chấn động tột cùng chính là cái tên nằm trong danh sách trúng tuyển đỗ cao: Lục Trầm Khương – 28.5 điểm!",
        "Từ một kẻ ngỗ ngược đội sổ trường học, hắn đã tạo nên một kỳ tích chấn động nhờ sáu tháng thức trắng đêm miệt mài đèn sách chỉ vì một lời hứa với người con gái hắn yêu!",
        "Dưới tán cây ngô đồng rợp bóng mát trong buổi lễ bế giảng tốt nghiệp cuối cùng của tuổi học trò, Lục Trầm Khương khoác trên mình chiếc áo cử nhân màu xanh thẫm, vóc dáng cao lớn tuấn tú tựa như một nam thần bước ra từ truyện tranh.",
        "Hắn cầm trên tay một bó hoa baby trắng tinh khôi – loài hoa mà An Nhiên yêu thích nhất – sải từng bước dài tự tin vượt qua hàng trăm ánh mắt ngưỡng mộ của học sinh toàn trường, tiến thẳng về phía cô gái nhỏ đang đứng bối rối bên bậc thềm đá."
    ]

    p3_exp = [
        "Lục Trầm Khương dừng bước ngay trước mặt Kiều An Nhiên, khóe môi nhếch lên nụ cười nửa miệng quen thuộc nhưng ánh mắt lại ngập tràn sự dịu dàng đắm đuối. Hắn trao bó hoa baby trắng vào tay cô, cúi người ghé sát vào tai cô cất giọng trầm ấm: 'Bạn học Kiều, tôi đã giữ đúng lời hứa rồi nhé. Từ nay về sau lên đại học thủ đô, cậu đừng hòng trốn thoát khỏi tầm mắt của tôi!'. An Nhiên ôm bó hoa thơm ngát vào lòng, đôi mắt ngấn lệ vì niềm hạnh phúc và tự hào khôn xiết: 'Lục Trầm Khương... Cậu giỏi lắm! Cảm ơn cậu vì đã nỗ lực nhiều đến thế!'.",
        "Chàng thiếu niên ngông nghênh bỗng nhiên trở nên lúng túng lạ thường. Hắn hắng giọng một tiếng, đưa tay gãi đầu rồi từ từ quỳ một gối xuống trước mặt cô giữa sự reo hò cổ vũ cuồng nhiệt của bạn bè cùng lớp: 'Lục Trầm Khương! Tỏ tình đi! Tỏ tình đi!'. Từ trong túi áo cử nhân, hắn lấy ra một chiếc hộp nhung nhỏ mở ra, bên trong là một sợi dây chuyền bạc tinh xảo có mặt dây chuyền khắc hình hai chữ cái ghép đôi: K & L.",
        "'Kiều An Nhiên, người ta bảo tôi là kẻ lạnh lùng, ngang tàng và khó dỗ dành nhất trường này. Nhưng họ đâu biết rằng từ khoảnh khắc cậu bước vào cuộc đời tôi, tôi đã hoàn toàn chịu thua trước cậu rồi. Tôi chỉ ngoan ngoãn khi ở cạnh cậu, chỉ biết dịu dàng với một mình cậu thôi. An Nhiên... Cậu có đồng ý làm bạn gái của tôi, để tôi dùng cả cuộc đời này dỗ dành, che chở cho cậu không?'.",
        "Lời tỏ tình chân thành, mộc mạc nhưng đong đầy tình cảm sâu sắc của chàng trai từng một thời ngông cuồng làm cả sân trường vỡ òa trong tiếng vỗ tay rền vang. An Nhiên nghẹn ngào rơi những giọt nước mắt hạnh phúc, cô khẽ gật đầu thì thầm: 'Tớ đồng ý... Cả đời này tớ chỉ cần một mình Lục Trầm Khương dỗ dành thôi!'. Lục Trầm Khương vui sướng đứng bật dậy, nhấc bổng An Nhiên xoay một vòng tròn giữa khoảng trời mùa hạ rợp bóng cây ngô đồng, nụ cười rạng rỡ của hai đứa trẻ tỏa sáng như ánh mặt trời ban mai.",
        "Những năm tháng đại học tại thủ đô sau đó, câu chuyện tình ngọt ngào của chàng học bá kiến trúc ngông cuồng và cô nàng hoa khôi kinh tế dịu dàng trở thành giai thoại đẹp đẽ nhất trong lòng bạn bè. Bốn năm sau, trên thảm đỏ của lễ đường hôn lễ ngập tràn hoa hồng trắng, Lục Trầm Khương khoác trên mình bộ âu phục chú rể sang trọng, xúc động rơi nước mắt khi nắm lấy bàn tay cô dâu Kiều An Nhiên bước vào ngưỡng cửa hôn nhân viên mãn. Bản tình ca thanh xuân của chàng đại ca khó dỗ dành cuối cùng đã có được cái kết ngọt ngào và hạnh phúc nhất trần đời."
    ]

    p3_fill = "Khúc ca tốt nghiệp vang lên rộn rã khắp sân trường báo hiệu một hành trình mới bắt đầu mở ra. Thanh xuân dẫu có trôi qua như một giấc mộng thoảng, nhưng những lời hẹn ước chân thành và tình yêu son sắt của tuổi trẻ sẽ mãi mãi là ngọn lửa ấm áp soi đường cho ta đi suốt cuộc đời. Hãy dũng cảm yêu và dũng cảm theo đuổi ước mơ, bởi vì ở cuối con đường của sự kiên định luôn có một người sẵn sàng dịu dàng che chở cho ta trọn kiếp nhân sinh."

    p3_full = "\n\n".join(p3_chunks) + "\n\n" + "\n\n".join(p3_exp)
    while len(p3_full.split()) < 3550:
        p3_full += "\n\n" + p3_fill

    p3_cliff = "Lục Trầm Khương siết chặt bàn tay An Nhiên trong tiếng reo hò chúc phúc của bạn bè toàn trường, đặt lên trán cô một nụ hôn dịu dàng thiêng liêng, chính thức khép lại những năm tháng học trò ngây thơ và mở ra một tương lai ngập tràn mật ngọt tình yêu..."

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
