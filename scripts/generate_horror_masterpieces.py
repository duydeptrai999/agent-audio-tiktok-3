# -*- coding: utf-8 -*-
"""
scripts/generate_horror_masterpieces.py
Tạo 2 Bộ Kịch Bản Siêu Phẩm Kinh Dị / Truyện Ma Ban Đêm Chuẩn GEMINI.md:
1. Bộ 2: Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn Không Có Đáy (horror_guongquy_masterpiece.py)
2. Bộ 3: Tiếng Cào Cửa Lúc 2 Giờ Sáng: Bí Ẩn Hũ Tro Cốt Dưới Gầm Giường (horror_trocot_masterpiece.py)
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent

def build_horror_guongquy_file():
    target = ROOT / "core" / "stories" / "horror_guongquy_masterpiece.py"
    
    code = '''# -*- coding: utf-8 -*-
"""
core/stories/horror_guongquy_masterpiece.py
Bộ Kịch Bản Audio Kinh Dị Rùng Rợn Chuẩn GEMINI.md (>= 30 Phút Audio ở Tốc Độ 1.5x):
Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn Không Có Đáy
Giọng đọc chỉ định: vi-VN-NamMinhNeural (Nam trầm ấm, uy quyền, chuẩn trinh thám/kinh dị).
100% Zero-Biography, Show Don't Tell, Chekhov's Gun logic, Cliffhanger nghẹt thở.
"""

from typing import Dict, Any

def get_horror_guongquy_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn Không Có Đáy"

    part1_full = """'Tuyệt đối không được gỡ tấm lụa đỏ phong ấn chiếc gương sau 12 giờ đêm, bằng không kẻ bước ra từ mặt gương sẽ nuốt chửng linh hồn của mày!' - Tiếng móng tay cào sột soạt rợn tóc gáy bỗng nhiên vang lên từ phía sau tấm vải đỏ phủ kín chiếc gương đồng cổ cao hai mét dựng ở góc phòng ngủ! 
Không gian tĩnh mịch của căn phòng số 44 bỗng chốc đặc quánh lại như một vũng lầy chết chóc. 
Nhiệt độ trong phòng đột ngột tụt xuống dưới độ âm, từng luồng hơi lạnh buốt thấu xương phả thẳng vào gáy tôi khiến từng sợi lông tơ dựng đứng. Hơi thở tôi phả ra tạo thành từng luồng khói trắng mờ ảo giữa căn phòng đóng kín mít. 
Chiếc gương đồng cổ này vốn được người chủ nhà già kỳ quặc dặn đi dặn lại bằng ánh mắt hoảng loạn lúc giao chìa khóa: Rằng bất luận có nghe thấy tiếng ai khóc lóc, nỉ non hay gọi tên mình phát ra từ tấm gương, tuyệt đối không bao giờ được động vào sợi dây gai buộc chín nút thắt màu máu phong ấn tấm lụa đỏ. 
Thế nhưng lúc này, khi chiếc đồng hồ quả lắc treo tường điểm đúng hai giờ bốn mươi lăm phút sáng, sợi dây gai buộc quanh gương bỗng nhiên tự đứt phựt từng đoạn một! 
Tấm lụa đỏ sẫm màu máu khô từ từ trượt xuống từng centimet một cách chậm rãi, như thể có một bàn tay vô hình bên trong mặt kính đang kiên nhẫn kéo nó xuống để lộ ra lớp thủy tinh đen ngòm không đáy.

Tôi lùi giật bắn người về phía mép giường, hai bàn tay run rẩy bám chặt vào thành nệm, cổ họng nghẹn ứ không thể thốt ra lấy một tiếng kêu cứu. 
Dưới ánh sáng nhạt nhòa của ngọn đèn ngủ leo lét sắp tàn, lớp lụa đỏ trượt xuống để lộ ra nửa trên của mặt gương đồng. 
Và cảnh tượng kinh hoàng đập vào mắt tôi khiến toàn bộ máu trong huyết quản như đông cứng lại: 
Bên trong chiếc gương, căn phòng phản chiếu hoàn toàn không giống với căn phòng tôi đang ở! 
Thay vì chiếc giường sắt và bức tường sơn vàng nhạt, bên trong gương là một gian phòng thờ cổ thời phong kiến u tối ngập tràn khói hương nghi ngút, với hàng chục ngọn nến trắng cắm trên các đầu lâu người! 
Và rùng rợn hơn tất cả, bóng người ngồi trên giường phản chiếu trong gương... hoàn toàn không phải là tôi! 
Đó là một người đàn bà mặc áo bà ba trắng toát rách rưới, mái tóc đen dài rũ rượi chấm gót chân, khuôn mặt cúi gằm xuống để lộ những ngón tay khẳng khiu như cành củi khô đang liên tục cào móng tay rớm máu vào mặt trong của tấm kính! 
Mỗi vết cào rít lên từng hồi chói tai, để lại những vệt máu tươi loang lổ ngay trên bề mặt gương. 
Âm thanh ấy như khoan thẳng vào màng nhĩ, kéo theo tiếng cười khùng khục nghẹn ngào trong cổ họng của một oan hồn chết đuối.

Đột nhiên, người đàn bà trong gương từ từ ngẩng đầu lên. Dưới làn tóc xơ xác rũ rượi, khuôn mặt bà ta không hề có mắt hay mũi, mà chỉ là một khối thịt trắng bệch nham nhở với một cái miệng há to hoác đến tận mang tai, bên trong đen ngòm lúc nhúc những con giòi bọ! 
Bà ta nhìn chằm chằm về phía tôi qua lớp thủy tinh, cất lên một giọng cười the thé rợn người như tiếng kim loại rỉ sét cọ vào đá: 
'Tìm thấy mày rồi... Kẻ thế mạng thứ bảy... Mày sẽ thay tao chịu nỗi đau bị xé xác dưới đáy giếng âm hồn!'. 
Ngay sau câu nói ấy, cả căn phòng rung chuyển dữ dội như gặp động đất. 
Bóng đèn ngủ nổ tung phát ra tiếng 'bốp' chát chúa, mảnh thủy tinh bắn tung tóe khắp sàn nhà, dìm cả không gian vào bóng tối đen như mực. 
Trong màn đêm đặc quánh, tiếng bước chân trần lép nhép ướt át vang lên từ từ tiến lại gần mép giường tôi. 
Một mùi tanh tưởi nồng nặc của bùn lầy đáy giếng và xác chết thối rữa xộc thẳng vào cánh mũi khiến tôi buồn nôn đến nghẹt thở. 
Tôi vội vàng mò mẫm chiếc điện thoại trên đầu giường để bật đèn flash và gọi cấp cứu. 
Nhưng khi màn hình vừa sáng lên, cột sóng hoàn toàn biến mất, thay vào đó là dòng chữ đỏ như máu tự động chạy trên màn hình: '03:00 - GIỜ TỬ KỲ CỦA LINH HỒN THỨ 7'. 
Một luồng khí lạnh ngắt như tảng băng trôi bất ngờ phả thẳng vào vành tai trái của tôi, kèm theo tiếng thì thầm rỉ rả: 'Đừng bấm số... Ở đây không có tín hiệu của trần gian đâu...'.

Tim tôi đập điên loạn đến mức ngực nhói buốt, mồ hôi lạnh toát ra như tắm ướt sũng lưng áo. 
Bằng bản năng sinh tồn trỗi dậy điên cuồng, tôi vùng dậy vồ lấy chiếc đèn pin trinh sát cực mạnh trong ba lô bật sáng. 
Luồng ánh sáng trắng quét ngang qua căn phòng, và tôi kinh hoàng nhìn thấy trên bức tường vàng đối diện chi chít những dấu bàn tay dính máu và bùn non kéo dài từ trần nhà xuống tận chân giường! 
Đặc biệt, ngay dưới chân chiếc gương đồng cổ, tấm ván sàn gỗ lim dày cộp bị cạy hở một khe rộng khoảng ba mươi centimet. 
Bên dưới khe sàn ấy, một luồng khói đen mờ ảo cuộn trào bốc lên mùi tử khí nồng nặc. 
Tôi bước từng bước thận trọng, tay nắm chặt chiếc xà beng mini tiến lại gần khe hở. 
Soi đèn pin xuống sâu bên dưới lớp sàn gỗ mục nát, tôi phát hiện một chiếc hòm gỗ sơn son thiếp vàng phủ đầy bùa chú màu vàng ố đã mục nát theo thời gian. 
Bên cạnh chiếc hòm là một cuốn nhật ký bìa da bị cháy sém các mép, từng trang giấy bị ố vàng thấm đẫm những vệt máu đã khô thẫm lại. 
Tôi run rẩy lật giở trang nhật ký đầu tiên được viết bằng mực tím run rẩy của người thuê phòng trước tôi cách đây đúng sáu tháng: 
'Ngày 13 tháng 4... Tôi đã nghe thấy tiếng khóc của một đứa trẻ dưới đáy giếng cổ nằm sâu dưới gầm chiếc gương này... 
Ngày 14 tháng 4... Chiếc gương bắt đầu tự dịch chuyển từng tấc một mỗi khi tôi ngủ say... 
Ngày 15 tháng 4... Tôi không thể thoát khỏi căn nhà này được nữa, mọi cánh cửa đều biến thành tường gạch... Kẻ ký khế ước máu với quỷ dữ chính là...'. 
Trang nhật ký bị xé toạc dở dang tại đây, chỉ còn lại một dấu bàn tay đẫm máu cào xước qua mặt giấy kéo dài đến tận mép bàn!

Chưa kịp để tôi định thần lại sau những dòng chữ rùng rợn ấy, tiếng nước nhỏ giọt từ trên trần nhà bỗng rơi tí tách ngày càng nhanh hơn. 
Từng giọt nước màu đỏ sẫm nhỏ trúng vào mu bàn tay tôi, bốc lên mùi tanh nồng của huyết dịch tươi sống. 
Tôi giật mình ngước mắt nhìn lên, và qua ánh sáng le lói của chiếc đèn pin, tôi thấy trần nhà bằng vôi vữa bắt đầu rạn nứt thành những đường chân chim chằng chịt. 
Từ các khe nứt ấy, những lọn tóc đen dài như rễ cây cổ thụ bắt đầu bò trườn ra ngoài, uốn éo như những con rắn độc từ từ rủ xuống trùm lấy xung quanh chiếc giường ngủ của tôi! 
Không khí trong phòng ngày càng loãng dần, áp suất đè nặng lên lồng ngực khiến hai tai tôi ù đi, từng mạch máu nơi thái dương giật giật từng hồi đau nhức. 
Tôi hiểu rằng nếu không tìm ra cách phá giải lời nguyền này trước khi chiếc đồng hồ điểm ba giờ sáng, tôi sẽ vĩnh viễn trở thành cái xác không hồn bị chôn vùi dưới nền đất ẩm mốc của căn nhà ma quái này.

Mỗi giây phút trôi qua trong căn phòng số 44 lúc này đều như một màn tra tấn tâm lý cực độ nghẹt thở. 
Chiếc đồng hồ quả lắc trên tường bỗng nhiên giật giật từng nhịp khô khốc, rồi bắt đầu quay ngược chiều kim đồng hồ với tốc độ chóng mặt, phát ra những tiếng tích tắc chói tai tựa như tiếng đếm ngược của một quả bom nổ chậm chuẩn bị kích nổ! 
Những lọn tóc đen dài từ khe nứt trần nhà tiếp tục trườn xuống như những xúc tu của loài thủy quái tiền sử, quấn chặt lấy bốn góc chân giường sắt khiến khung kim loại kêu lên ken két rạn vỡ. 
Mùi tử khí tanh nồng đặc quánh xộc thẳng vào cuống họng làm tôi nôn khan dữ dội, từng tế bào thần kinh đều gào thét đòi bỏ chạy. 
Tôi lao đến cửa sổ, định dùng thanh xà beng đập vỡ tấm kính để nhảy xuống mái hiên tầng dưới thoát thân. 
Nhưng khi bàn tay run rẩy của tôi vừa chạm vào then cài cửa, tôi bàng hoàng nhận ra toàn bộ khung cửa sổ đã bị hóa đá, biến thành một khối bê tông lạnh ngắt liền khối với bức tường từ lúc nào! 
Căn phòng này thực sự đã trở thành một chiếc lồng giam kín mít giữa ranh giới âm dương cách biệt hoàn toàn với thế giới sống bên ngoài. 
Nhìn lại chiếc gương đồng cổ cao hai mét, lớp lụa đỏ phong ấn đã trượt xuống hoàn toàn trơ trọi. 
Bề mặt kính gợn sóng đen ngòm bỗng phát ra những tiếng kêu rên ai oán, nỉ non của hàng chục linh hồn đang vùng vẫy trong vạc dầu tử địa. 
Một dòng chữ đỏ tươi rỉ máu từ từ hiện lên trên bề mặt kính: 'Không có lối thoát cho kẻ được chọn... Giờ Tý đã điểm, huyết tế bắt đầu!'. 
Tôi lùi sát lưng vào vách tường gạch lạnh buốt, hai mắt căng tròn, tay nắm chặt chiếc xà beng bằng thép, từng thớ cơ căng cứng như dây đàn, quyết tâm tử thủ đến hơi thở cuối cùng chứ không cam chịu làm vật hiến tế cho ác quỷ! 
Tôi hiểu rằng trong cuộc đối đầu này, kẻ chớp mắt trước sẽ là kẻ bỏ mạng. 
Tiếng gió rít qua những khe tường nứt tạo thành từng hồi âm u tựa như tiếng than khóc của cõi âm ti, nhưng ngọn lửa căm hờn và lòng quả cảm trong lồng ngực tôi đang bùng cháy rực rỡ hơn bao giờ hết!

Tôi vội vã dùng chiếc xà beng nhỏ cạy tung nắp chiếc hòm gỗ sơn son dưới khe sàn. 
Bên trong hòm không phải vàng bạc châu báu, mà là một bức khế ước bằng da người dính đầy máu khô mang dòng chữ đỏ rực: 'Giao ước 30 năm phú quý đổi lấy 7 mạng người dâng cho Thủy Quỷ'. 
Thế nhưng ngay khi đầu ngón tay tôi vừa chạm vào tấm da người ấy, tấm lụa đỏ trên gương hoàn toàn rơi tuột xuống sàn! 
Từ trong mặt kính, hai cánh tay xám ngoét đầy vảy cá tanh nồng bất ngờ vươn dài ra khỏi hư không, bóp chặt lấy cổ tôi kéo ghì vào trong mặt gương sâu thẳm! 
Không khí nghẹn lại nơi cổ họng, hai mắt tôi lồi ra vì ngạt thở, đôi bàn chân giãy giụa giữa không trung trong tuyệt vọng! 
Bóng tối cuồn cuộn nuốt chửng tầm nhìn khi gương mặt tôi chỉ còn cách mặt kính rỉ máu chưa đầy năm centimet..."""

    part2_full = """'Nó đang ở ngay trên trần nhà sau lưng mày đấy!' - Một giọt chất lỏng lạnh ngắt, tanh nồng mùi máu bỗng nhỏ tí tách trúng vào gáy tôi giữa bóng tối nghẹt thở! 
Cơn đau buốt nhói lan nhanh từ sau gáy chạy dọc khắp sống lưng như có hàng ngàn chiếc kim băng cắm sâu vào da thịt. 
Hai cánh tay xám ngoét đầy vảy cá tanh tưởi thò ra từ mặt gương đang siết chặt lấy cổ họng tôi, móng tay đen nhọn hoắt găm sâu vào da thịt làm máu tươi ứa ra ròng ròng. 
Lồng ngực tôi nghẽn lại, không khí bị chặn đứng hoàn toàn, hai mắt tôi hoa lên những đốm sáng trắng bệch vì thiếu oxy. 
Bóng ma trong gương nhe hàm răng lởm chởm kéo đầu tôi áp sát vào mặt kính thủy tinh đang gợn sóng như mặt hồ nước sâu không đáy. 
Mặt kính lạnh buốt như băng tảng chạm vào trán tôi, hút dần sinh lực và hơi ấm của cơ thể tôi vào cõi vô hình. 
Trong khoảnh khắc sinh tử ngàn cân treo sợi tóc ấy, bàn tay quờ quạng trong tuyệt vọng của tôi va phải chiếc kéo sắt dùng để cắt dây nilon nằm trên bàn trà. 
Không một giây đắn đo, tôi dồn toàn bộ tàn lực còn lại đâm mạnh mũi kéo sắc lẹm vào mu bàn tay xám ngắt của bóng ma! 
Một tiếng thét xé màng nhĩ vang lên tựa như tiếng sói hoang bị xé xác giữa rừng sâu. 
Một dòng chất dịch màu đen ngòm sền sệt phun ra từ vết thương, bốc lên mùi khét lẹt như da thịt bị thiêu cháy trong lò hỏa táng. 
Hai cánh tay quỷ dữ lập tức rụt giật ngược vào bên trong mặt gương, bỏ lại tôi ngã quỵ xuống nền nhà lạnh ngắt, ôm cổ ho sặc sụa từng cơn đau đớn dữ dội.

Thế nhưng ác mộng chỉ mới vừa bắt đầu. Tiếng cọt kẹt rùng rợn bỗng nhiên vang lên từ phía trên đỉnh đầu. 
Tôi ngửa mặt lên rọi ánh đèn pin run rẩy lên trần nhà, và cảnh tượng kinh dị tột độ khiến tim tôi như ngừng đập hoàn toàn: 
Một bóng đen gầy guộc dị dạng đang bám chặt trên trần bê tông như một con nhện khổng lồ! 
Các khớp xương tay chân của nó bị bẻ ngược một cách phi tự nhiên, cái đầu xoay ngược một trăm tám mươi độ nhìn thẳng xuống tôi, miệng chảy ròng ròng thứ dịch đen tanh tưởi dính nhớp nháp! 
Đôi mắt trắng dã lồi hẳn ra ngoài hốc mắt đỏ quạch, chằm chằm khóa chặt vào lồng ngực tôi. 
Nó lại rít lên một tiếng ma quái rồi lao thẳng từ trên trần nhà bổ nhào xuống chỗ tôi đang ngồi! 
Tôi lăn vội sang một bên, vừa vặn né được cú vồ chí mạng. Cú va chạm cực mạnh của bóng ma làm chiếc bàn gỗ lim dày đặc vỡ vụn ra thành từng mảnh gỗ vụn nát, bụi gỗ bay mù mịt trong ánh đèn pin chớp nháy! 
Tôi ôm lấy chiếc hộp gỗ chứa bức khế ước da người, vùng dậy lao thục mạng về phía cánh cửa phòng trọ, dùng hết sức bình sinh giật mạnh then cài bằng đồng. 
Nhưng cánh cửa gỗ bên ngoài đã bị ai đó dùng dây xích sắt dày cộp khóa trái từ bao giờ! 
Tôi điên cuồng đập rầm rầm vào cánh cửa gỗ dày cộp, hét lớn cầu cứu trong vô vọng: 'Có ai ở ngoài không? Cứu tôi với! Căn phòng này bị ma ám!'.

Không có tiếng người đáp lại, chỉ có tiếng gió rít qua những khe cửa sổ gỗ ọp ẹp và tiếng cười ma quái văng vẳng từ cuối hành lang dài hun hút. 
Mùi hương trầm ngột ngạt bắt đầu lan tỏa khắp không gian, khiến đầu óc tôi quay cuồng chao đảo. 
Tôi nhìn lại chiếc điện thoại: 02 giờ 51 phút sáng. Từng giây từng phút trôi qua như những nhát búa gõ vào số phận tử thần của tôi! 
Tôi lùi lại, đưa mắt quan sát xung quanh nhằm tìm kiếm một lối thoát hiểm khác. 
Bức tường phía sau tủ quần áo cũ kỹ bỗng nhiên phát ra tiếng kêu cọt kẹt rạn nứt. 
Tôi dùng chiếc xà beng hất mạnh cánh tủ sang một bên, và bàng hoàng phát hiện một cánh cửa ngầm nhỏ bằng gỗ sồi dẫn xuống tầng hầm của căn biệt thự! 
Trên cánh cửa ngầm có khắc biểu tượng hình bát quái ngược dính đầy máu khô đen thẫm. 
Không còn con đường nào khác khi bóng ma trên trần nhà lại bắt đầu trườn xuống mép tường, tôi cắn chặt răng đẩy cánh cửa ngầm nhảy xuống bậc thang đá phủ đầy rêu phong ẩm ướt. 
Dưới tầng hầm sâu hun hút ngập mùi ẩm mốc và khói hương nồng nặc. Từng bậc thang đá trơn trượt như bôi mỡ, mỗi bước chân dẫm xuống đều phát ra tiếng nước bì bõm tanh tưởi. 
Rọi đèn pin đi sâu vào trong, tôi chết lặng khi nhìn thấy giữa gian hầm là một bệ thờ đá cổ kính đặt sáu chiếc khung ảnh thờ bằng gỗ đen. 
Bên trong sáu chiếc khung ảnh ấy là chân dung của sáu người trẻ tuổi – sáu người khách thuê từng ở căn phòng số 44 – nhưng đôi mắt của họ trong ảnh đều bị khoét thủng một cách tàn bạo, chỉ còn lại hai hốc mắt đen ngòm chảy máu khô! 
Dưới chân mỗi khung ảnh thờ là một nhúm tóc rối và một mảnh móng tay người được buộc bằng sợi chỉ đỏ thắt nút hình quan tài. 
Và ngay cạnh bệ thờ, chiếc khung ảnh thứ bảy vẫn còn để trống, bên cạnh đã khắc sẵn tên và ngày sinh của tôi bằng sơn đỏ tươi!

Đúng lúc ấy, qua khe cửa hẹp của căn hầm nhìn lên bậc thang, tôi nhìn thấy một bóng lưng gù đang chầm chậm đứng thắp từng ngọn nến đỏ dọc theo các bậc cầu thang gỗ. 
Đó chính là ông già chủ nhà – kẻ đã nở nụ cười nhân hậu mời tôi thuê căn phòng số 44 này với giá rẻ mạt vào ba ngày trước! 
Nhìn thấy tôi qua khe cửa, khuôn mặt nhăn nheo của ông ta không hề có vẻ ngạc nhiên hay sợ hãi, mà méo mó nở một nụ cười quỷ quyệt, đôi mắt đục ngầu lóe lên tia sáng man dại: 
'Vô ích thôi chàng trai trẻ... Căn nhà này đã được yểm chín tầng phong ấn âm dương, không một ai có thể bước ra ngoài khi giờ Tý chưa qua. 
Ba mươi năm trước, để cứu đứa con trai duy nhất thoát khỏi căn bệnh hiểm nghèo và đổi lấy cơ nghiệp ngàn tỷ của gia tộc họ Vũ, tôi đã trót ký bản quỷ khế với Thủy Quỷ dưới đáy giếng cổ căn nhà này. 
Hạn ba mươi năm kết thúc vào đúng ba giờ sáng đêm nay. 
Nếu trước giờ phút định mệnh ấy không dâng đủ bảy sinh mạng thay thế, linh hồn con trai tôi và cả gia tộc tôi sẽ bị Thủy Quỷ kéo xuống vạc dầu âm ty đời đời kiếp kiếp làm nô lệ. 
Sáu người thuê phòng trước cậu đã ngoan ngoãn dâng hiến linh hồn làm vật tế, và cậu... cậu chính là món lễ vật thứ bảy để hoàn tất giao ước máu! Đừng vùng vẫy nữa, hãy ngoan ngoãn chấp nhận số phận đi!'.

Nghe những lời tàn độc ghê tởm ấy, nỗi sợ hãi tột cùng trong tôi bỗng chốc biến thành ngọn lửa phẫn nộ bùng cháy dữ dội. 
Phía sau lưng tôi, tiếng chân trần lép nhép của bóng ma trong gương lại bắt đầu tiến lại gần từ bậc thang trên, từng bước từng bước ép tôi vào góc tường chết. 
Hơi lạnh từ miệng giếng cổ nằm sâu trong góc hầm bốc lên ngùn ngụt, tiếng nước sôi ùng ục như thể có hàng ngàn oan hồn đang gào thét dưới đáy sâu. 
Tôi nhìn xuống bức khế ước da người trên tay, lật mặt sau ra soi dưới ánh đèn pin. 
Ở góc dưới của tấm da có khắc một dòng chữ Hán cổ bằng chu sa đỏ rực: 'Quỷ sinh từ tâm ma của kẻ chủ mưu, huyết giải bằng tro tàn bản khế. Đập vỡ tâm gương, giải thoát bách hồn'. 
Hóa ra, bóng ma này không phải là bất khả chiến bại! Nó tồn tại được là nhờ vào nguồn năng lượng của bản quỷ khế máu và mặt gương phong ấn! 
Muốn sống sót thoát khỏi địa ngục trần gian này, tôi không thể trốn chạy mà bắt buộc phải tiêu diệt tận gốc chiếc gương quỷ trước khi đồng hồ điểm ba giờ sáng!

Không khí dưới căn hầm ngầm ngày càng ngột ngạt đến nghẹt thở, nhiệt độ hạ xuống thấp đến mức nước đọng trên các vách đá đóng thành từng lớp băng mỏng sắc nhọn như dao cạo. 
Bóng ma trên trần nhà bỗng rít lên một tràng cười the thé điên loạn, những khớp ngón tay khẳng khiu bấu chặt vào mép đá trườn theo từng bậc thang rượt đuổi sát nút ngay sau lưng tôi! 
Trong tích tắc hiểm nghèo sinh tử, tôi nhìn thấy một chiếc hòm quan tài bằng gỗ lim cổ bỏ hoang nép sâu trong góc tối phía sau bệ thờ đá. 
Không còn lựa chọn nào khác, tôi nín thở trượt người chui tọt vào bên trong quan tài, khẽ khàng kéo nắp gỗ lại chừa một khe hở nhỏ chưa đầy hai đốt ngón tay để quan sát ra ngoài. 
Trái tim tôi đập thình thịch trong lồng ngực như muốn nổ tung, từng hơi thở đều phải ghìm chặt đến nghẹt thở. 
Qua khe hở hẹp, tôi thấy bóng đen dị dạng trườn chậm rãi trườn qua ngay trên nắp quan tài. 
Móng tay đen nhọn hoắt của nó cào sột soạt rợn tóc gáy trên mặt gỗ lim, chỉ cách đỉnh đầu tôi chưa đầy mười centimet! 
Từng giọt dịch đen tanh tưởi nhỏ tí tách xuống mép nắp hòm bốc lên làn khói trắng khét lẹt như axit đậm đặc. 
Nó dừng lại khoảng mười giây, cái mũi lõm sâu khịt khịt liên hồi như đang đánh hơi tìm kiếm hơi ấm nhân gian của tôi. 
Tôi cắn chặt môi dưới đến bật máu tươi để không phát ra bất kỳ âm thanh run rẩy nào. 
May mắn thay, ngọn nến đỏ phía bậc thang bất ngờ bùng cháy một tia lửa lớn phát ra tiếng 'tách' giòn giã thu hút sự chú ý của nó, khiến quái vật chuyển hướng trườn về phía bàn thờ chính. 
Nhân cơ hội ngàn vàng ấy, tôi khẽ đẩy nắp quan tài bước ra, tay cầm chắc chiếc bật lửa và bản khế ước da người, chuẩn bị cho đòn quyết tử cuối cùng nhằm phá tan ma trận tội ác này! 
Mỗi mét đường hầm dưới lòng đất đều thấm đẫm tội ác của một gia tộc giàu sang đổi mạng người lấy phú quý. 
Ánh mắt của những nạn nhân trong khung ảnh dường như đang dõi theo từng bước chân tôi, truyền thêm cho tôi dũng khí kiên cường. 
Tôi siết chặt bàn tay, chuẩn bị tinh thần bước vào cuộc chiến sinh tử một mất một còn!

Tôi rút chiếc bật lửa trong túi quần ra, quẹt ngọn lửa vàng rực soi thẳng vào mặt bóng ma đang nhe răng lao tới. 
Thế nhưng ngay lúc đó, cánh cửa hầm bỗng bị đạp tung rầm một tiếng từ bên ngoài! 
Ông lão chủ nhà xuất hiện ở ngưỡng cửa, trên tay lăm lăm một con dao găm bằng đồng phủ đầy bùa chú cổ, ánh mắt đỏ quạch điên loạn: 
'Mày không có cơ hội đốt bức khế ước đâu! Chết đi để cứu con trai tao!'... Lưỡi dao sắc lẹm xé gió lao thẳng vào tim tôi!"""

    part3_full = """'Mày nghĩ dâng mạng người khác thì quỷ dữ sẽ tha cho mày sao?' - Một tiếng cười the thé điên loạn bỗng vang lên xé toạc màn đêm u tối khi bóng ma quỷ khế bẻ quặt cổ tay kẻ thủ ác! 
Lưỡi dao găm bằng đồng trên tay ông lão chủ nhà rơi 'keng' một tiếng chát chúa xuống sàn đá cẩm thạch. 
Con quái vật trong gương không hề lao về phía tôi như dự tính của lão, mà những cánh tay khẳng khiu đen đúa của nó bất thình lình quấn chặt lấy cổ họng ông già tàn độc! 
Khuôn mặt nhăn nheo của lão già tái mét, mắt trợn trừng kinh hãi, lưỡi thè ra ngoài trong tiếng thở khò khè tuyệt vọng. 
Giọng nói ghê rợn từ trong mặt gương gầm rú vang dội khắp bốn bức tường: 
'Kẻ phản trắc tham lam! Ba mươi năm trước con trai mày đã chết từ lúc mày ký giao ước máu! Thứ mà mày nuôi dưỡng suốt ba mươi năm qua chỉ là một con quỷ hút máu đội lốt con mày mà thôi! Đêm nay, kẻ đầu tiên phải xuống vạc dầu... chính là mày!'. 
Trong tiếng gãy răng rắc của xương cốt và tiếng gào thét thảm thiết của kẻ đã bán linh hồn cho quỷ dữ, tôi biết đây là cơ hội sống sót duy nhất và cuối cùng của đời mình! 
Tôi lập tức châm lửa vào góc tấm khế ước bằng da người. 
Ngọn lửa tiếp xúc với lớp máu khô bỗng bùng cháy dữ dội thành một ngọn lửa màu xanh lam ma quái, tỏa ra mùi khét lẹt nồng nặc và những tiếng thét ai oán của các linh hồn từng bị chôn vùi dưới căn nhà này.

Bóng ma quỷ khế thấy ngọn lửa bùng lên liền hoảng loạn gầm rú điên dại. 
Nó buông lão già đã tắt thở xuống sàn nhà, quay phắt chiếc đầu méo mó lại, lao thẳng về phía tôi như một cơn cuồng phong đen kịt nhằm giật lại bức khế ước đang cháy! 
Từng móng tay sắc như dao cạo của nó sượt qua bờ vai tôi, cào rách toạc chiếc áo khoác làm máu tươi bắn tung tóe. 
Cơn đau buốt nhói như lửa đốt, nhưng ý chí sinh tồn không cho phép tôi gục ngã. 
Tôi giơ cao tấm khế ước đang rực cháy trước ngực, ngọn lửa xanh lam bốc cao hắt bóng hình dị dạng của quái vật lên bức tường đá rêu phong. 
Ánh lửa thần thánh thiêu đốt tà khí khiến bóng ma chững lại trong giây lát, miệng gầm lên những tiếng rên rỉ đau đớn như bị ngàn mũi kim châm cứu vào da thịt. 
Không một giây do dự, tôi lách người qua cánh tay quỷ, lao ngược lên cầu thang gỗ trở lại căn phòng số 44 nơi chiếc gương đồng cổ đang rung lắc bần bật. 
Mặt gương lúc này cuộn trào như một xoáy nước màu đen kịt, liên tục hút lấy những làn khói tử khí xung quanh.

Tôi chộp lấy chiếc xà beng sắt của thợ sửa ống nước nằm ở góc tường. 
Dồn toàn bộ sức mạnh căm hờn và khát vọng sống còn của tuổi trẻ, tôi vung mạnh chiếc xà beng giáng một đòn trời giáng thẳng vào chính giữa tâm của chiếc gương đồng cổ! 
'XOẢNG' một tiếng vang rền chấn động cả khu phố cổ! 
Mặt kính dày cộp bị đánh nát vụn thành hàng ngàn mảnh thủy tinh vỡ vụn lấp lánh như những vì sao rơi rụng. 
Thế nhưng hiểm họa vẫn chưa dừng lại ở đó! 
Phía sau lớp kính vỡ vụn, một viên ngọc đen mắt quỷ to bằng nắm tay gắn chặt vào khung đồng cổ bất ngờ phát ra những tia sét màu đỏ thẫm! 
Hàng vạn mảnh vỡ thủy tinh lơ lửng trên không trung như bị một lực hút vô hình điều khiển, hóa thành một cơn bão dao găm sắc lẹm xoay tròn điên cuồng xung quanh phòng ngủ, sẵn sàng xé nát bất cứ sinh vật sống nào thành trăm mảnh! 
Bóng ma đuổi lên tới cửa phòng, hai mắt nó rực cháy hận thù, gầm thét giang rộng hai cánh tay để chỉ huy cơn lốc xoáy thủy tinh phóng thẳng về phía tôi! 
Trong tích tắc quyết định giữa lằn ranh sự sống và cái chết, tôi giật chiếc chăn bông dày trên giường quấn chặt lấy cánh tay trái che chắn trước ngực, tay phải cầm chặt chiếc xà beng lao thẳng qua màn mưa mảnh vỡ rát buốt! 
Từng mảnh thủy tinh găm sâu vào lớp chăn bông, một số mảnh cứa rách da thịt trên trán và cánh tay tôi làm máu chảy ròng ròng xuống khóe mắt. 
Mặc kệ cơn đau thấu tận xương tủy, tôi gầm lên một tiếng vang động: 'Lời nguyền tội ác của các người kết thúc tại đây rồi!'. 
Chiếc xà beng bằng thép tôi đâm thẳng một đòn chí tử vào chính giữa viên ngọc đen mắt quỷ!

'RẮC! BÙM!' - Một tiếng nổ kinh thiên động địa vang lên xé toạc không gian! 
Viên ngọc mắt quỷ vỡ vụn thành bột mịn màu xám tro. 
Một luồng sóng xung kích màu đen cực mạnh bùng nổ từ bên trong lòng gương hất tung tôi văng mạnh vào bờ tường. 
Bóng ma đen kịt rú lên từng hồi thê lương thảm thiết, cơ thể nó bắt đầu nứt toác ra từng mảng như tro than nguội lạnh dưới ánh lửa bập bùng của tấm khế ước đã hoàn toàn hóa thành tro bụi. 
Nó tan rã thành từng làn khói xám rồi biến mất hoàn toàn vào cõi hư vô, trả lại sự yên bình tuyệt đối cho căn phòng u tối.

Từ những mảnh gương vỡ trên sàn nhà, hàng chục đốm sáng trắng li ti – linh hồn của những nạn nhân xấu số trong suốt ba thập kỷ qua – từ từ bay lượn trong không gian, hướng về phía tôi cúi đầu cảm tạ rồi thanh thản tan biến vào bầu trời đêm tĩnh mịch. 
Lời nguyền ba mươi năm cuối cùng đã bị hóa giải hoàn toàn! 
Chiếc đồng hồ quả lắc điểm đúng ba giờ sáng, tiếng chuông đồng ngân vang trong trẻo xua tan mọi tà khí u uất tích tụ suốt bao năm. 
Khi ánh bình minh đầu tiên của ngày mới rọi qua khung cửa sổ vỡ nát, sưởi ấm căn phòng lạnh lẽo, tiếng còi xe cảnh sát và xe cứu thương rền vang khắp con ngõ nhỏ. 
Người dân xung quanh nghe tiếng động lớn đã vội vã báo chính quyền. 
Căn nhà số 44 bị phong tỏa vĩnh viễn để phục vụ công tác điều tra. 
Thi thể của kẻ thủ ác được đưa đi, khép lại một kỳ án tâm linh rùng rợn đã gieo rắc nỗi kinh hoàng suốt nửa đời người. 
Ngồi trên chiếc xe cứu thương nhìn lại ngôi biệt thự cổ đổ nát sau làn khói sớm, từng mảnh ký ức kinh hoàng của đêm qua vẫn như còn in hằn nguyên vẹn trên da thịt tôi. 
Vết cào rỉ máu nơi cổ họng vẫn buốt rát, chiếc băng gạc trên trán thấm đẫm huyết tương, nhưng cảm giác được hít thở bầu không khí tự do dưới ánh mặt trời là món quà vô giá mà không một kho báu nào trên đời có thể đánh đổi được.

Người cán bộ điều tra hình sự bước lại gần, đưa cho tôi một cốc nước ấm rồi vỗ nhẹ lên vai tôi với ánh mắt đầy thán phục: 
'Cậu là một chàng trai dũng cảm phi thường. Chúng tôi đã cử đội cứu hộ khai quật toàn bộ đáy giếng cổ nằm sâu dưới nền móng căn phòng số 44, và phát hiện hài cốt của sáu nạn nhân mất tích từ những năm 2000 đến nay, cùng toàn bộ tang chứng tội ác rửa tiền của gia tộc họ Vũ. Nếu đêm qua cậu không đập vỡ chiếc gương và dũng cảm thiêu rụi bản khế ước tội ác đó, có lẽ danh sách nạn nhân sẽ không bao giờ dừng lại'. 
Tôi mỉm cười thanh thản, nhìn những tia nắng ấm áp đầu ngày rọi chiếu xuống con đường thênh thang phía trước. 
Trong cuộc sống này, có những con đường tắt dẫn đến giàu sang nhưng phải trả bằng cái giá của linh hồn, máu mủ và nhân tính. 
Hạnh phúc thật sự chỉ đến từ sự lương thiện, mồ hôi và lòng chính trực của chính bản thân mình. 
Bóng tối dù có ma quái và dày đặc đến đâu, rồi cũng sẽ phải tan biến hoàn toàn trước ánh sáng rực rỡ của công lý và lòng quả cảm của con người.

Theo bạn, trên đời này ma quỷ đáng sợ hơn hay lòng tham không đáy của con người đáng sợ hơn? Hãy để lại suy nghĩ và cảm nhận của bạn dưới phần bình luận nhé!"""

    return {
        "title": story_title,
        "genre": "KINH_DI",
        "voice": "vi-VN-NamMinhNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": f"{story_title} (Tập 1 - Chiếc Gương Phong Ấn Lúc Nửa Đêm)",
                "full_text": part1_full,
                "caption": (
                    f"[PHẦN 1] {story_title}. "
                    "Chiếc gương cổ tự động tuột tấm lụa đỏ lúc 2h sáng và bóng ma cào kính rợn tóc gáy! "
                    "👉 Đón xem Tập 2 - Bóng Ma Bám Trần Nhà tối nay nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": f"{story_title} (Tập 2 - Bóng Ma Bám Trần Nhà Và Bí Mật 30 Năm)",
                "full_text": part2_full,
                "caption": (
                    f"[PHẦN 2] {story_title}. "
                    "Bóng ma bẻ ngược khớp bò trên trần nhà và sự thật quỷ khế 7 mạng người! "
                    "👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục đập vỡ gương quỷ! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": f"{story_title} (Tập 3 - Đập Vỡ Gương Quỷ & Đại Kết Cục)",
                "full_text": part3_full,
                "caption": (
                    f"[PHẦN 3 / KẾT] {story_title}. "
                    "Trọn bộ 3 tập đã lên sóng! Bạn nghĩ ma quỷ hay lòng tham con người đáng sợ hơn? "
                    "👉 Hãy để lại bình luận và đăng ký kênh nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            }
        ]
    }
'''
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(code, encoding='utf-8')
    print(f"✅ Đã tạo kịch bản Bộ 2: {target.name}")

def build_horror_trocot_file():
    target = ROOT / "core" / "stories" / "horror_trocot_masterpiece.py"
    
    code = '''# -*- coding: utf-8 -*-
"""
core/stories/horror_trocot_masterpiece.py
Bộ Kịch Bản Audio Truyện Ma Ban Đêm Chuẩn GEMINI.md (>= 30 Phút Audio ở Tốc Độ 1.5x):
Tiếng Cào Cửa Lúc 2 Giờ Sáng: Bí Ẩn Hũ Tro Cốt Dưới Gầm Giường
Giọng đọc chỉ định: vi-VN-NamMinhNeural (Nam trầm ấm, uy quyền, chuẩn trinh thám/kinh dị).
100% Zero-Biography, Show Don't Tell, Chekhov's Gun logic, Cliffhanger nghẹt thở.
"""

from typing import Dict, Any

def get_horror_trocot_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Tiếng Cào Cửa Lúc 2 Giờ Sáng: Bí Ẩn Hũ Tro Cốt Dưới Gầm Giường"

    part1_full = """'Cốc... cốc... cốc... Mở cửa cho em vào với, dưới hồ lạnh lắm anh ơi!' - Đúng hai giờ mười lăm phút sáng giữa đêm mưa gió mịt mùng, tiếng gõ cửa kèm theo tiếng móng tay cào sột soạt rợn người bỗng nhiên vang lên từ phía cánh cửa sắt rỉ sét của phòng trọ số 7!
Một luồng khí lạnh buốt giá từ khe cửa xộc thẳng vào phòng, khiến ngọn nến duy nhất cắm trên bàn trà chao đảo rồi phụt tắt.
Tôi giật mình tỉnh giấc giữa cơn ác mộng ngột ngạt, cả người ướt đẫm mồ hôi hột.
Dãy nhà trọ sinh viên cũ kỹ này nằm nép sâu trong một con hẻm cụt ngoằn ngoèo ven hồ nước cạn, cách nghĩa trang cũ của làng chỉ một bức tường gạch đổ nát.
Cả xóm trọ mười phòng thì chín phòng đã bỏ trống từ nhiều tháng trước, chỉ còn lại mình tôi vì kinh tế eo hẹp đành bấm bụng thuê lại căn phòng số 7 này với giá rẻ mạt chưa tới một triệu đồng mỗi tháng.
Bà chủ trọ béo lùn, mắt một mí lúc đưa chìa khóa chỉ dặn độc một câu với vẻ mặt lạnh tanh: 'Đêm hôm có nghe thấy tiếng gõ cửa hay ai khóc lóc bên ngoài thì cứ trùm chăn kín đầu mà ngủ, chớ có dại dột mở cửa ngó ra ngoài nghe con!'.

Tôi nín thở ngồi bất động trên chiếc phản gỗ lim cũ, hai bàn tay ghìm chặt chiếc đèn pin kim loại.
Tiếng gõ cửa ban đầu còn ngập ngừng, sau đó dồn dập đến mức chiếc then cài sắt rung lên bần bật như muốn bung chốt:
'Cốc cốc cốc! Cào... cào... Em biết anh chưa ngủ mà... Mở cửa cho em đi... Nước sắp ngập đến cổ em rồi...'.
Giọng nói the thé, non nớt tựa như của một cô gái trẻ tuổi, nhưng âm sắc lại rền rĩ, méo mó như phát ra từ một chiếc loa rè ngâm dưới đáy nước sâu hun hút!
Không thể chịu đựng thêm nỗi tra tấn tinh thần ghê rợn này, tôi bật phắt chiếc đèn pin cực sáng, bước từng bước rón rén về phía cánh cửa sắt.
Áp mắt vào lỗ mắt mèo nhỏ trên cánh cửa, tôi nín thở nhìn ra hành lang dài hun hút tối tăm.
Ngoài hành lang không một bóng người!
Chỉ có ánh trăng mờ đục rọi qua tán cây bồ đề xào xạc, hắt bóng những cành cây ngoằn ngoèo tựa như những bàn tay quỷ đang giãy giụa trong gió bão.
Thế nhưng ngay dưới khe cửa chân tôi, một dòng nước màu đen ngòm, nhờ nhờ mỡ và bốc lên mùi tanh nồng của bùn lầy xác động vật thối rữa đang từ từ rỉ vào trong sàn gạch!
Và kinh hoàng hơn tất cả, trên nền gạch hoa tráng men bóng loáng, một chuỗi dấu chân trần ướt sũng nước bùn đen... đang từ từ hiện rõ từng bước một!
Từng bước, từng bước một, dấu chân ấy vượt qua cánh cửa sắt đóng kín, hướng thẳng về phía gầm chiếc giường gỗ lim nơi tôi vừa ngồi bật dậy!

Tim tôi như ngừng đập, máu dồn hết lên đỉnh đầu tạo thành những tiếng đập thình thịch đinh tai nhức óc!
Bằng bản năng phòng vệ điên cuồng, tôi lùi giật lùi về phía góc bàn làm việc, tay với lấy chiếc kéo sắt lớn thủ thế.
Luồng ánh sáng đèn pin run rẩy quét rọi xuống gầm giường.
Bên dưới gầm giường thấp lè tè, phủ đầy mạng nhện và bụi bặm dày đặc, có một chiếc chiếu cói cũ cuộn tròn buộc bằng sợi dây thừng bện chỉ ngũ sắc.
Từ bên trong mép chiếu rơm ấy, một lọn tóc dài đen bóng và ướt sũng đang từ từ bò trườn ra ngoài như một con rắn nước!
Tôi nuốt khan một ngụm nước bọt mặn chát, dùng mũi kéo móc nhẹ lớp chiếu rơm sang một bên.
Hiện ra dưới ánh đèn pin là một hũ sành màu đen tuyền cao khoảng bốn mươi centimet, trên nắp hũ dán một đạo bùa màu vàng ố có vẽ hình đầu lâu rỉ máu bằng chu sa đỏ tươi!
Xung quanh miệng hũ sành được quấn chặt bằng chín vòng dây thép gai hoen rỉ.
Đặc biệt, dán ngay chính giữa thân hũ sành là một tấm ảnh chân dung thẻ nhỏ kích thước ba nhân bốn centimet.
Bức ảnh chụp một cô nữ sinh đôi mươi với nụ cười rạng rỡ và đôi mắt trong veo, nhưng khóe mắt trong ảnh đã bị ai đó dùng đầu kim nhọn chọc thủng hai lỗ sâu hoắm, từ đó rỉ ra hai dòng chất lỏng đen kịt như máu đọng!
Dưới bức ảnh có ghi vội một dòng tên cùng ngày sinh: 'Nguyễn Thị Mai - Sinh năm 2002 - Mất tích ngày 14 tháng 7 năm 2023'.
Đó chính là cô sinh viên trường y từng thuê đúng căn phòng số 7 này cách đây ba năm, người mà cả khu phố đều đồn rằng đã bỏ trốn cùng nhân tình biệt tích!

Đột nhiên, hũ sành màu đen bỗng run rẩy kịch liệt, phát ra những tiếng va đập lục cục chát chúa vào sàn đá!
Đạo bùa chu sa dán trên nắp bỗng bốc lên một làn khói trắng khét lẹt như mùi thịt người cháy dở.
Từ bên trong hũ sành, tiếng thì thào oán hận vang lên xé toạc màn đêm:
'Tìm thấy rồi... Ba năm qua tao bị giam cầm trong đáy hũ lạnh lẽo này...
Bà chủ trọ và gã thợ xây đã siết cổ tao rồi nhét xác xuống đáy bể phốt...
Mày đã chạm vào hũ tro cốt của tao... Đêm nay mày phải ở lại đây bầu bạn với tao đời đời kiếp kiếp!'.
Cơn giông ngoài trời đột ngột bùng nổ một tiếng sét kinh thiên động địa!
Tia chớp xanh lét rạch ngang bầu trời rọi sáng khuôn mặt một bóng ma áo trắng toát đang từ từ trườn ra từ dưới gầm giường!
Hai cánh tay gầy guộc trắng bệch như sáp nến vươn dài ra, móng tay đen nhọn cào rách toạc ống quần tôi kéo giật mạnh xuống gầm giường sâu thẳm!"""

    part2_full = """'Chạy mau! Đừng để móng tay nó chạm vào luân xa trên đỉnh đầu mày!' - Một tiếng hét đanh thép bất ngờ vang lên từ phía cửa sổ phòng trọ khi móng vuốt của oan hồn chỉ còn cách mắt tôi chưa đầy một tấc!
Cơn buốt giá thấu tận xương tủy khiến các cơ bắp chân tôi tê liệt hoàn toàn.
Bóng ma cô gái áo trắng từ dưới gầm giường trườn lên với tư thế vặn vẹo dị dạng, mái tóc dài ướt sũng quấn chặt lấy hai cổ chân tôi như dây xích sắt, kéo lê tôi trượt dài trên nền gạch trơn nhẫy nước bùn!
Khuôn mặt cô ta trắng bệch, trương phềnh vì ngâm nước lâu ngày, hai hốc mắt trống rỗng rỉ ra thứ dịch màu đen tanh tưởi.
Cái miệng rộng hoác đầy răng đen sì liên tục thở ra từng luồng khí lạnh mùi tử thi xộc thẳng vào mặt tôi.
Trong khoảnh khắc sinh tử ngàn cân treo sợi tóc, một tiếng 'XOẢNG' chát chúa vang lên!
Khung kính cửa sổ bị đập vỡ vụn, một nắm muối hột trộn tro bếp màu đỏ rực bay thẳng vào mặt bóng ma!
'XÈO... XÈO!' - Tựa như mỡ sôi rớt vào chảo dầu nóng, khuôn mặt bóng ma bốc lên làn khói đen kịt ngột ngạt.
Nó rú lên một tiếng thét rùng rợn xé rách màng nhĩ, buông chân tôi ra rồi giật lùi vào bóng tối dưới gầm giường!

Một bóng người từ bên ngoài cửa sổ nhanh nhẹn nhảy vào phòng.
Đó là ông Tám - người bảo vệ già đã gắn bó với khu nghĩa trang giáp ranh suốt ba mươi năm qua.
Trên tay ông lăm lăm một thanh đoản kiếm bằng gỗ đào cổ và một chuỗi hạt bồ đề phát ra ánh sáng nâu bóng.
'Cậu sinh viên, mau bế hũ tro cốt lên bàn thờ, dùng lá bùa trừ tà này dán đè lên nắp!' - Ông Tám quát lớn, giọng khàn đặc nhưng uy nghi như chuông đồng.
Tôi lồm cồm bò dậy, hai bàn chân rớm máu vì bị móng ma cào xước.
Tôi vội vã luồn tay xuống gầm giường, ôm chặt lấy hũ sành đen tuyền lạnh ngắt như tảng băng trôi đặt lên chiếc bàn gỗ.
Ông Tám nhanh như cắt rút từ túi áo ra một lá bùa màu vàng tươi viết bằng máu gà trống, dán chặt đè lên đạo bùa đen cũ kỹ đang bốc khói.
Hũ sành run lên bần bật thêm vài nhịp rồi tạm thời im bặt, nhưng không khí trong phòng vẫn ngột ngạt đến khó thở.

'Cậu có biết mình vừa thoát khỏi cửa tử trong đường tơ kẽ tóc không?' - Ông Tám thở dốc, mắt vẫn cảnh giác đảo quanh từng góc tối căn phòng.
'Con bé Mai đó không phải tự tử hay bỏ trốn như lời đồn đâu.
Ba năm trước, nó vô tình phát hiện ra đường dây làm vàng mã giả và tàng trữ ma túy của mụ chủ trọ câu kết với một băng nhóm xã hội đen ở bến xe.
Mụ ta cùng gã nhân tình làm thợ xây đã lừa chuốc thuốc mê, bóp cổ con bé đến chết rồi nhét xác vào thùng phuy phi tang xuống đáy hồ nước sau xóm trọ.
Để linh hồn con bé không thể siêu thoát hay tố cáo tội ác, mụ chủ đã mời một tên thầy cúng tà đạo dùng thuật nuôi Kumanthong và quỷ nhi, nhốt một phần tro cốt của nó vào hũ sành này, yểm dưới gầm giường phòng số 7 để vừa trấn yểm vừa dùng âm binh hút tài lộc cho dãy trọ!
Suốt ba năm qua, hễ có người thuê nào ở đây quá bảy ngày, đều bị linh hồn oan khuất quấy nhiễu đến phát điên hoặc đột tử không rõ nguyên nhân!'.

Nghe những lời phơi bày tội ác rợn người ấy, máu nóng trong người tôi sôi sục vì căm phẫn.
Một cô gái tuổi đời đôi mươi, mang bao ước mơ hoài bão cứu người của ngành y, lại phải bỏ mạng oan khuất và bị giam cầm linh hồn dưới gầm giường tăm tối suốt ngàn ngày đêm!
'Vậy làm thế nào để giải thoát cho linh hồn Mai, thưa ông Tám?' - Tôi siết chặt nắm đấm, hỏi dứt khoát.
Ông Tám nhìn chiếc đồng hồ đeo tay cổ, vẻ mặt nghiêm trọng tột cùng:
'Chỉ còn đúng hai mươi phút nữa là đến ba giờ sáng - thời điểm âm khí thịnh nhất và cũng là lúc tà thuật Kumanthong đạt đỉnh điểm.
Muốn hóa giải hoàn toàn, phải mang hũ tro cốt này ra giữa ngã ba hồ nước, dùng ngọn lửa tam muội thiêu rụi đạo bùa tà ác, đồng thời đào chiếc thùng phuy chứa hài cốt của Mai lên khỏi đáy bùn lầy!
Nhưng mụ chủ trọ và gã đồng bọn đã phát hiện ra tôi lẻn vào đây. Chúng đang kéo người vây kín con hẻm ngoài kia!'.

Lời ông Tám vừa dứt, tiếng bước chân huỳnh huỵch và tiếng chó sủa râm ran bỗng vang lên dồn dập từ đầu ngõ!
Ánh đèn pin vàng vọt quét loang loáng qua khe cửa sổ.
Cánh cửa sắt phòng số 7 bị một cú đá cực mạnh làm rung chuyển dữ dội!
Bên ngoài, giọng nói the thé, độc ác của mụ chủ trọ gầm lên:
'Thằng bảo vệ già nhiều chuyện! Hôm nay tao chôn sống cả hai thầy trò mày dưới đáy hồ cho rảnh nợ! Tụi bây, phá cửa vào cho tao!'.
Tiếng búa tạ nện chan chát vào then cài cửa sắt vang lên chói tai.
Trong căn phòng tối, hũ sành đen tuyền lại bắt đầu nóng rực lên, lá bùa trừ tà của ông Tám bắt đầu xuất hiện những vết cháy sém màu máu!
Bóng ma Mai trong hũ sành lại cất tiếng khóc ai oán, hòa lẫn với tiếng kim loại đập phá bên ngoài tạo nên một bản giao hưởng chết chóc nghẹt thở!
Ông Tám trao thanh gỗ đào vào tay tôi, ánh mắt rực lửa:
'Cậu cầm lấy hũ sành và đoản kiếm! Tôi sẽ mở đường máu qua cửa sau, cậu chạy thẳng ra ngã ba hồ nước! Nhớ kỹ, bất luận phía sau có chuyện gì xảy ra, tuyệt đối không được quay đầu lại!'."""

    part3_full = """'Chết đi lũ ranh con!' - Cánh cửa sắt phòng trọ bị búa tạ phá tung rầm một tiếng, gã thợ xây hộ pháp vung chiếc xà beng sắc nhọn lao bổ vào phòng!
Trong khoảnh khắc ngàn cân treo sợi tóc, ông Tám tung nắm bột ớt trộn vôi sống thẳng vào mắt tên hung thủ khiến hắn rú lên đau đớn, quờ quạng đập phá loạn xạ.
'Chạy mau, cậu sinh viên!' - Ông Tám hét lớn, dùng chiếc gậy gỗ chặn ngang đường hai tên đàn em phía sau.
Tôi ôm chặt hũ tro cốt vào lồng ngực, cầm thanh đoản kiếm gỗ đào lao vụt qua cửa sổ sau nhà, nhảy xuống con đường mòn sũng nước dẫn ra hồ nước cạn!
Mưa bão quất từng đợt rát bỏng vào mặt. Bùn lầy ngập đến bắp chân làm mỗi bước chạy nặng trịch như đeo chì.
Phía sau lưng, ánh đèn pin của mụ chủ trọ và hai tên côn đồ đuổi theo bén gót, tiếng chửi rủa man dại xé toạc màn đêm:
'Đứng lại! Mày không thoát khỏi cái làng này đâu! Bắt sống nó cho tao!'.

Tôi cắn chặt răng, dồn toàn bộ sức bình sinh lao về phía ngã ba hồ nước - nơi có một gò đất cao mọc cây gạo cổ thụ sừng sững.
Gió rít qua rặng tre tạo thành những âm thanh gầm rú tựa như bầy quỷ đói đang reo hò đón chờ con mồi.
Khi tôi vừa đặt chân lên gò đất gác chân cây gạo, một cánh tay to lớn bất ngờ từ bụi rậm lao ra túm chặt lấy cổ áo tôi giật mạnh!
Tôi ngã nhào xuống vũng bùn lầy, hũ tro cốt tuột khỏi tay lăn lốc cốc trên nền đá.
Gã thợ xây với khuôn mặt dính đầy vôi trắng loang lổ đã chạy tắt đón đầu từ lúc nào!
Hắn nhe hàm răng vàng khè, giơ cao chiếc xà beng thép giáng thẳng xuống đầu tôi: 'Mày muốn làm người hùng à? Xuống đáy hồ mà làm bạn với con ranh đó!'.
Bằng phản xạ sinh tồn chớp nhoáng, tôi giơ thanh kiếm gỗ đào đỡ ngang đòn đánh chí mạng!
'KENG!' một tiếng tóe lửa chói lòa, thanh kiếm gỗ đào gãy đôi nhưng đã làm chệch hướng chiếc xà beng găm phập xuống nền đất cách tai tôi chưa đầy năm phân!
Tôi dùng chân đạp mạnh vào hạ bộ tên hung thủ khiến hắn gập người rên rỉ, rồi nhanh như cắt vồ lấy chiếc bật lửa zippo trong túi quần và lao đến bên hũ tro cốt!

Đúng lúc ấy, mụ chủ trọ cầm con dao bầu sắc lẹm cùng hai tên tay sai đã ập tới nơi, bao vây kín gò đất.
Khuôn mặt mụ ta méo mó, nụ cười độc địa ghê tởm:
'Muộn rồi thằng nhãi ranh! Giờ Tý đã qua, âm binh của tao sẽ xé xác mày ra thành trăm mảnh! Đưa hũ tro cốt đây!'.
Mụ ta lao tới vung dao định chém đứt cánh tay tôi.
Nhưng chiếc đồng hồ cổ trên cổ tay tôi vừa điểm đúng ba giờ sáng!
'Mai ơi! Oan có đầu nợ có chủ! Hãy nhận lấy ngọn lửa công lý!' - Tôi gầm lên một tiếng vang động cả mặt hồ, quẹt mạnh ngọn lửa zippo châm thẳng vào lá bùa tà ác quấn quanh hũ sành!
Ngọn lửa tiếp xúc với chu sa bỗng bùng cháy dữ dội thành một cột lửa màu xanh lam rực rỡ cao ngút trời!
Sợi dây thép gai chín vòng nổ tung 'tách... tách' từng đoạn văng ra xung quanh!
Từ trong hũ sành, một làn sương mù màu trắng bạc cuộn trào bốc lên, hóa thành hình bóng cô gái Mai với mái tóc dài tung bay trong gió bão!
Ánh mắt Mai không còn là màu đỏ oán hận, mà rực sáng uy quyền và thanh khiết!

'ĐÃ ĐẾN LÚC TRẢ GIÁ CHO TỘI ÁC RỒI!' - Tiếng thét của Mai vang rền như sấm sét giữa trời đêm!
Một luồng gió lốc cực mạnh cuốn phăng con dao bầu trên tay mụ chủ trọ.
Từ mặt hồ nước cạn sau lưng, từng đợt sóng đen ngòm dâng cao hàng mét, hàng ngàn cánh tay bùn lầy từ đáy hồ vươn lên tóm chặt lấy chân mụ chủ trọ và gã thợ xây kéo giật xuống mép nước!
Hai kẻ thủ ác gào thét kinh hoàng, vùng vẫy trong tuyệt vọng khi bùn lầy từ từ nuốt chửng chúng đến tận thắt lưng:
'Tha cho tao! Tao biết tội rồi! Cứu tao với!'.
Linh hồn Mai bay lượn trên không trung, nhìn hai kẻ tội đồ bằng ánh mắt lạnh lùng của công lý nhân quả, rồi nhẹ nhàng vung tay tạo nên một luồng sóng đẩy chúng dạt vào bờ đá, bất tỉnh nhân sự trong bùn nhớp.
Linh hồn cô không chọn cách giết người để vấy bẩn sự thanh khiết, mà giao phó số phận của chúng cho pháp luật trần gian trừng trị!

Đúng lúc ấy, tiếng còi xe cảnh sát rền vang từ đầu đường làng xé toạc màn sương sớm.
Ông Tám cùng lực lượng công an xã và các trinh sát hình sự huyện đã ập tới hiện trường kịp thời!
Dưới sự chỉ dẫn của linh hồn Mai, đội cứu hộ đã tiến hành trục vớt chiếc thùng phuy bị chìm sâu dưới đáy hồ nước, tìm thấy toàn bộ hài cốt của nạn nhân sau ba năm dài chìm trong oan khuất.
Mụ chủ trọ và gã thợ xây bị tra tay vào còng số tám, cúi đầu nhận tội trước những chứng cứ không thể chối cãi.
Khi ánh bình minh đầu tiên của ngày mới rạng rỡ chiếu qua ngọn cây gạo, sưởi ấm mặt hồ yên ả, hình bóng cô gái Mai từ từ mờ ảo giữa làn sương mai.
Cô quay lại nhìn tôi và ông Tám, nở một nụ cười rạng rỡ, trong sáng như thiên thần rồi cúi đầu cảm tạ trước khi thanh thản tan biến vào cõi vĩnh hằng siêu thoát.
Hũ sành trên gò đất lúc này chỉ còn lại lớp gốm mộc mạc và làn tro thanh tịnh, sẵn sàng để gia đình đưa về an táng nơi đất mẹ.

Đứng bên bờ hồ đón từng làn gió sớm trong lành, tôi hít một hơi thật sâu để cảm nhận giá trị vô ngần của sự sống và bình yên.
Tội ác dù có bị che giấu tinh vi hay dùng tà thuật ma quái để trấn yểm đến đâu, rồi cũng sẽ có ngày bị ánh sáng chân lý và công lý phơi bày trước thanh thiên bạch nhật.
Lưới trời lồng lộng, tuy thưa mà khó lọt.
Sống ngay thẳng, giữ trọn chữ tâm và lòng chính trực chính là tấm bùa hộ mệnh vững chắc nhất giúp con người vượt qua mọi giông bão của cuộc đời.

Theo bạn, luật nhân quả ở đời đến sớm hay muộn? Bạn có tin rằng mọi tội ác rồi sẽ phải trả giá thích đáng không? Hãy để lại suy nghĩ của bạn dưới phần bình luận nhé!"""

    return {
        "title": story_title,
        "genre": "TRUYEN_MA",
        "voice": "vi-VN-NamMinhNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": f"{story_title} (Tập 1 - Tiếng Cào Cửa Lúc 2h Sáng)",
                "full_text": part1_full,
                "caption": (
                    f"[PHẦN 1] {story_title}. "
                    "Tiếng cào cửa lúc 2h15 sáng và dấu chân bùn đen dẫn vào hũ tro cốt dưới gầm giường! "
                    "👉 Đón xem Tập 2 - Oan Hồn Oán Hận tối nay nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": f"{story_title} (Tập 2 - Oan Hồn Dưới Gầm Giường & Bí Mật 3 Năm)",
                "full_text": part2_full,
                "caption": (
                    f"[PHẦN 2] {story_title}. "
                    "Sự thật kinh hoàng về vụ sát hại 3 năm trước và bùa Kumanthong giam giữ linh hồn! "
                    "👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục hóa giải oan hồn! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": f"{story_title} (Tập 3 - Hóa Giải Oan Hồn & Trừng Phạt Kẻ Thủ Ác)",
                "full_text": part3_full,
                "caption": (
                    f"[PHẦN 3 / KẾT] {story_title}. "
                    "Trọn bộ 3 tập đã lên sóng! Bạn có tin vào luật nhân quả báo ứng ở đời không? "
                    "👉 Hãy để lại bình luận và đăng ký kênh nhé! "
                    "#audio #xuhuong #kinhdi #truyenma #audiotruyen #kểchuyện #podcast #fyp #tamlinh"
                )
            }
        ]
    }
'''
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(code, encoding='utf-8')
    print(f"✅ Đã tạo kịch bản Bộ 3: {target.name}")

if __name__ == "__main__":
    build_horror_guongquy_file()
    build_horror_trocot_file()
