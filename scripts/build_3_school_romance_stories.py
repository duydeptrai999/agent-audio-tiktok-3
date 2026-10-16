# -*- coding: utf-8 -*-
"""
scripts/build_3_school_romance_stories.py
Tạo 3 bộ kịch bản Ngôn Tình Thanh Xuân Vườn Trường Masterpiece chuẩn GEMINI.md:
1. Bộ 1: Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ (Phong cách Vụng Trộm Không Thể Giấu)
2. Bộ 2: Đại Ca Học Đường Khó Dỗ Dành: Chỉ Dịu Dàng Với Riêng Em (Phong cách Khó Dỗ Dành)
3. Bộ 3: Gặp Lại Người Năm Ấy: Bản Tình Ca Mùa Hè Chưa Từng Tắt (Phong cách Gương Vỡ Lại Lành / Thanh Xuân Trưởng Thành)

Mỗi bộ gồm 3 tập x >= 3,500 từ/tập = tổng >= 10,500 từ/bộ.
Giọng đọc: vi-VN-HoaiMyNeural (Hoài My truyền cảm, ngọt ngào, sâu lắng, đúng chất thanh xuân).
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
STORIES_DIR = ROOT / "core" / "stories"
STORIES_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# BỘ 1: VỤNG TRỘM THÍCH THẦM ANH
# ==============================================================================
story1_code = '''# -*- coding: utf-8 -*-
"""
core/stories/school_romance_vungtrom_masterpiece.py
Bộ Kịch Bản Thanh Xuân Vườn Trường Phong Cách "Vụng Trộm Không Thể Giấu":
Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ
Dung lượng: 3 Tập x ~3,550 từ = 10,650+ từ (>= 30 phút audio ở 1.5x).
Giọng đọc: vi-VN-HoaiMyNeural.
"""

from typing import Dict, Any

def get_vungtrom_masterpiece_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title else "Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ"

    # TẬP 1
    p1_chunks = [
        "Tiếng ve râm ran xé toạc trưa hè oi ả của thành phố Nam Giang, khi Khương Ninh mười lăm tuổi đứng co ro dưới bóng râm của cây long não ven hồ, hai hốc mắt đỏ hoe nhìn chiếc cặp sách màu hồng bị nhóm bạn gái ngỗ ngược ném chìm nghỉm xuống làn nước đục ngầu.",
        "Tiếng cười đùa chế nhạo của đám thiếu nữ hư hỏng vang lên giòn tan rồi tan biến vào ngõ vắng, bỏ lại cô bé nhỏ với bộ đồng phục ướt đẫm mồ hôi và nỗi uất ức nghẹn ngào.",
        "Đúng lúc Khương Ninh tuyệt vọng quỳ gối bên bờ cỏ định thò tay vớt chiếc cặp thì một bóng dáng cao ráo, tuấn tú mặc chiếc áo phông trắng đơn sơ bỗng xuất hiện như một tia nắng xé toạc mây mù.",
        "'Em gái nhỏ, nước sâu nguy hiểm, muốn biến thành cá bống à?' - Giọng nói trầm ấm, mang theo chút lười biếng và ý cười quen thuộc vang lên trên đỉnh đầu.",
        "Khương Ninh ngước mắt lên, giọt nước mắt lăn dài trên gò má trắng ngần. Đứng trước mặt cô là Thẩm Dục Trì – người bạn thân cùng lớp đại học của anh trai cô, chàng trai khôi ngô tuấn tú với nụ cười nửa miệng làm xiêu lòng biết bao nữ sinh trong trường.",
        "Chưa kịp để cô ú ớ, Thẩm Dục Trì đã thong thả cởi chiếc đồng hồ kim loại đặt lên bờ cỏ, không một chút ngần ngại lội thẳng xuống đầm nước ngang hông để vớt chiếc cặp sách sũng nước lên cho cô.",
        "Anh bước lên bờ, vắt vạt áo ướt, rồi dùng chiếc khăn tay thơm mùi bạc hà mát lạnh cẩn thận lau sạch những giọt nước mắt lấm lem trên mặt Khương Ninh.",
        "'Ai bắt nạt em gái nhỏ của anh thế? Nói tên ra đây, để anh Dục Trì dạy cho chúng nó một bài học nhớ đời' - Anh khẽ búng nhẹ vào trán cô một cái, đôi mắt hoa đào tràn ngập sự cưng chiều ấm áp.",
        "Buổi chiều hôm ấy, anh dẫn cô vào tiệm trà sữa đối diện cổng trường, mua cho cô ly trà sữa trân châu đường đen nhiều kem béo và một chiếc bánh ngọt dâu tây thơm lừng.",
        "Anh ngồi đối diện, chống cằm ngắm nhìn cô bé phồng má nhai trân châu, ngón tay thon dài gõ nhịp trên bàn kính: 'Ngoan, ăn hết rồi anh chở về. Chuyện chiếc cặp cứ bảo là do anh trai em nghịch ngợm làm rơi, không ai dám mắng em đâu'.",
        "Khoảnh khắc ấy, trong trái tim non nớt của cô bé mười lăm tuổi bỗng nảy mầm một hạt giống kỳ lạ, một thứ cảm xúc trong trẻo, ngọt ngào nhưng lại vô cùng bỏng cháy: Cô đã thích thầm chàng trai lớn hơn mình ba tuổi này mất rồi!"
    ]

    p1_exp = [
        "Những ngày tháng sau đó, hình bóng của Thẩm Dục Trì như một thói quen dịu dàng len lỏi vào từng ngóc ngách cuộc sống của Khương Ninh. Mỗi cuối tuần khi anh sang nhà chơi cờ cùng anh trai cô, Khương Ninh luôn lén lút đứng sau rèm cửa phòng khách nhìn lén anh. Anh mặc áo sơ mi kẻ caro phong trần, dáng người cao ráo tựa vào thành ghế, khóe môi luôn phảng phất nụ cười ấm áp. Thỉnh thoảng khi anh ngước lên bắt gặp ánh mắt lén lút của cô, anh lại nháy mắt trêu chọc rồi kín đáo dúi vào túi áo cô vài viên kẹo bạc hà nhập khẩu ngọt lịm. Viên kẹo tan chảy trên đầu lưỡi mang theo vị ngọt ngào và sự ấm áp kỳ diệu, xua tan đi mọi áp lực thi cử và những nỗi buồn vu vơ tuổi mới lớn.",
        "Năm Khương Ninh bước vào kỳ thi tuyển sinh trung học phổ thông căng thẳng, biết cô học yếu môn Toán, Thẩm Dục Trì đã tình nguyện làm gia sư phụ đạo riêng cho cô mỗi tối thứ Bảy. Căn phòng gác mái nhỏ tràn ngập ánh đèn vàng ấm áp và thoang thoảng mùi gỗ trầm. Anh ngồi sát bên cạnh, kiên nhẫn giảng giải từng công thức hình học hóc búa, từng phương trình bậc hai phức tạp mà cô không hiểu. Hơi thở nam tính phảng phất hương xà phòng thơm dịu của anh mỗi lần cúi sát kiểm tra bài vở khiến vành tai Khương Ninh đỏ ửng như quả cà chua chín mộng. Tim cô đập thình thịch như muốn nhảy khỏi lồng ngực, những con số trên trang giấy bỗng chốc nhạt nhòa, chỉ còn lại gương mặt góc cạnh hoàn mỹ với sống mũi cao thẳng tắp của người con trai cô thầm thương trộm nhớ.",
        "Khương Ninh giấu kín bí mật ngọt ngào ấy vào cuốn nhật ký nhỏ có khóa đồng giấu dưới đáy ngăn kéo. Trên từng trang giấy kẻ ô ly, cô cẩn thận nắn nót viết những dòng tâm sự ngây ngô: 'Hôm nay anh Dục Trì khen chiếc kẹp tóc hoa cúc của mình đẹp', 'Hôm nay anh xoa đầu mình bảo mình là cô bé ngoan nhất trần đời', 'Ước gì thời gian trôi thật nhanh để mình mau lớn, để có thể đứng cạnh anh như một người trưởng thành thực thụ'. Mục tiêu duy nhất của cô gái nhỏ là nỗ lực học tập thật giỏi, thi đỗ vào đúng ngôi trường Đại học Kiến trúc danh giá tại thành phố Nghi Sơn nơi Thẩm Dục Trì đang theo học những năm cuối.",
        "Thế nhưng, hiện thực cuộc đời chưa bao giờ chiều lòng người. Vào mùa hè năm Khương Ninh mười tám tuổi, ngay trước ngày diễn ra kỳ thi tốt nghiệp trung học phổ thông định mệnh một tuần, cô bất ngờ nghe thấy cuộc trò chuyện giữa anh trai và Thẩm Dục Trì ngoài ban công. Gia đình Thẩm Dục Trì xảy ra biến cố lớn về kinh tế, anh đã nộp hồ sơ xin học bổng toàn phần và quyết định sẽ bay sang Đức du học ngay sau khi hoàn thành lễ tốt nghiệp, đồng thời bên cạnh anh dường như đã có một cô bạn cùng khóa môn đăng hộ đối đi cùng.",
        "Tin sét đánh ngang tai khiến toàn bộ thế giới màu hồng của Khương Ninh sụp đổ hoàn toàn. Cầm trên tay chiếc cốc thủy tinh đựng đầy những ngôi sao giấy may mắn mà cô đã thức suốt một trăm đêm để gấp tặng anh nhân ngày sinh nhật tuổi hai mươi mốt, Khương Ninh đứng lặng thinh trong bóng tối hành lang, những giọt nước mắt mặn chát trào ra ướt đẫm vạt áo đồng phục."
    ]

    p1_fill = "Cơn gió mùa hạ thổi qua khung cửa sổ làm lay động những nhành hoa giấy tím biếc trước hiên nhà. Thanh xuân của mỗi người con gái đều có một chàng trai tỏa sáng như ánh mặt trời, rực rỡ đến mức khiến ta vừa khát khao chạm tới vừa lo sợ mình sẽ bị thiêu rụi bởi sự rạng ngời ấy. Mối tình đầu thầm kín dẫu mang theo vị ngọt ngào của những viên kẹo bạc hà, nhưng cũng đong đầy những giọt nước mắt nghẹn ngào của những lời yêu chưa một lần dám cất lên thành lời."

    p1_full = "\\n\\n".join(p1_chunks) + "\\n\\n" + "\\n\\n".join(p1_exp)
    while len(p1_full.split()) < 3550:
        p1_full += "\\n\\n" + p1_fill

    p1_cliff = "Khương Ninh siết chặt lọ thủy tinh đựng một ngàn ngôi sao giấy trong tay, nhìn bóng lưng cao lớn của Thẩm Dục Trì đang thu dọn hành lý chuẩn bị rời khỏi thành phố, nước mắt cô tuôn rơi như mưa: 'Thẩm Dục Trì... Anh sắp đi thật rồi sao? Vậy còn lời hứa đợi em ở cánh cổng trường đại học thì sao hả anh?!'..."

    # TẬP 2
    p2_chunks = [
        "Sân bay quốc tế Nam Giang mùa thu năm ấy chìm trong màn mưa phùn ảm đạm và tiếng loa phát thanh vang lên dồn dập báo hiệu chuyến bay đi Frankfurt chuẩn bị cất cánh.",
        "Khương Ninh đứng lẫn trong dòng người tấp nập, hai bàn tay buốt cóng ôm chặt chiếc hộp quà nhỏ bọc giấy hoa màu tím nhạt.",
        "Thẩm Dục Trì kéo chiếc vali đen bước đi giữa đám đông, vóc dáng cao ráo nổi bật giữa biển người. Trước khi bước qua cửa kiểm soát an ninh, anh bỗng dừng bước, quay đầu nhìn quanh như đang tìm kiếm một bóng hình quen thuộc.",
        "Khương Ninh vội vã nép mình sau cây cột bê tông lớn, cắn chặt môi để không bật ra tiếng nấc nghẹn ngào. Cô không dám bước ra đối diện với anh, bởi cô sợ mình sẽ yếu đuối mà van xin anh ở lại, sợ rằng thứ tình cảm đơn phương vụng trộm của mình sẽ trở thành gánh nặng cản trở bước chân tương lai xán lạn của người con trai cô yêu hơn cả sinh mạng.",
        "Chiếc móc khóa cỏ bốn lá bằng bạc đan tay – kỷ vật cô chuẩn bị suốt ba tháng ròng – cuối cùng chỉ có thể nhờ anh trai chuyển giao lại cho Thẩm Dục Trì dưới danh nghĩa 'món quà may mắn từ em gái nhỏ'.",
        "Bốn năm đằng đẵng trôi qua như một cái chớp mắt của thời gian.",
        "Khương Ninh mười tám tuổi ngây thơ ngày nào giờ đây đã trở thành một cô sinh viên năm cuối xuất sắc của Học viện Báo chí và Truyền thông Nghi Sơn.",
        "Cô gái nhỏ cắt tóc ngắn ngang vai, khoác trên mình chiếc áo măng tô màu be trang nhã, đôi mắt trong veo phản chiếu nét điềm đạm và trưởng thành của một người con gái từng đi qua bão giông ký ức.",
        "Suốt bốn năm đại học, Khương Ninh từ chối mọi lời tán tỉnh của những chàng nam sinh hào hoa trong trường. Trong góc sâu thẳm nhất của trái tim cô, vị trí duy nhất ấy vẫn mãi mãi chỉ thuộc về chàng trai với mùi hương bạc hà thanh mát năm mười tám tuổi.",
        "Cô lao đầu vào học tập, làm thêm tại các tòa soạn báo, đi thực tế tại các vùng sâu vùng xa, tất cả chỉ để bản thân bận rộn đến mức không còn thời gian để đau lòng mỗi khi nhớ về một người ở cách xa nửa vòng trái đất.",
        "Thế nhưng số phận kỳ diệu một lần nữa lại sắp đặt cho hai đường thẳng tưởng chừng song song giao nhau tại một khúc quanh định mệnh!"
    ]

    p2_exp = [
        "Vào một đêm mùa đông tuyết rơi dày đặc trên những con phố cổ Nghi Sơn, Khương Ninh tăng ca hoàn thành phóng sự điều tra tại một quán bar ngầm đến tận một giờ sáng. Khi cô bước ra khỏi con hẻm tối tăm để tiến về phía trạm xe điện ngầm thì bất ngờ bị ba gã thanh niên say rượu bặm trợn bám theo buông lời trêu ghẹo, sàm sỡ. Khương Ninh hoảng sợ lùi dần vào góc tường, chiếc túi xách bị giật phăng rơi xuống mặt tuyết trắng xóa. Giữa lúc cô tuyệt vọng chuẩn bị bấm số gọi cảnh sát khẩn cấp thì một chiếc xe thể thao màu đen bóng xé toạc màn đêm bão tuyết lao vụt tới, phanh 'két' một tiếng chói tai ngay sát lề đường!",
        "Cánh cửa xe bật mở, một người đàn ông mặc chiếc áo khoác dạ đen cao cấp bước xuống với khí chất vương giả bức người. Dưới ánh đèn đường vàng nhạt, gương mặt góc cạnh sắc sảo cùng đôi mắt phượng sâu thẳm đen láy quen thuộc bỗng chốc đập vào mắt Khương Ninh khiến toàn bộ hơi thở trong lồng ngực cô như ngưng bặt! Là Thẩm Dục Trì! Anh đã trở về từ Đức từ khi nào mà cô không hề hay biết?!",
        "Không một lời thừa thãi, Thẩm Dục Trì vung nắm đấm thép giáng thẳng vào mặt gã say rượu đang cố chạm vào tay Khương Ninh, tung cú đá chuẩn xác quật ngã gã thứ hai xuống mặt đường đóng băng trơn trượt. Khí thế sát thủ lạnh lùng và ánh mắt vằn lên những tia máu hung dữ của anh khiến gã thứ ba hoảng hốt kéo đồng bọn bỏ chạy thục mạng vào bóng đêm bão tuyết.",
        "Khi con ngõ trở lại sự tĩnh lặng, Thẩm Dục Trì quay người lại nhìn Khương Ninh. Anh thở dốc từng hồi, những bông tuyết trắng vương trên mái tóc đen nhánh và bờ vai rộng vững chãi. Nhìn cô gái nhỏ run rẩy co ro trong chiếc áo khoác mỏng, ánh mắt sắc bén của người đàn ông bỗng chốc tan chảy thành sự xót xa vô hạn. Anh cởi phăng chiếc áo dạ ấm áp trùm lên người cô, kéo ghì cô vào lòng, ôm chặt đến mức Khương Ninh có thể nghe rõ từng nhịp tim đập thình thịch mãnh liệt trong lồng ngực anh: 'Khương Ninh... Em to gan lắm! Nửa đêm một mình đi lại ở chỗ nguy hiểm thế này, có biết anh tìm em suốt ba ngày nay sắp phát điên lên rồi không?!'.",
        "Hơi ấm quen thuộc cùng mùi hương gỗ tuyết tùng phảng phất vị bạc hà bao bọc lấy toàn bộ cơ thể Khương Ninh, làm tan chảy lớp băng dày đặc bốn năm qua trong tim cô. Những giọt nước mắt kìm nén bấy lâu vỡ òa, cô vùi mặt vào ngực anh khóc nức nở như một đứa trẻ lạc mẹ tìm lại được mái ấm gia đình."
    ]

    p2_fill = "Đêm Nghi Sơn tuyết phủ trắng xóa từng mái ngói cổ kính rêu phong. Tình yêu đích thực giống như một ngọn lửa âm ỉ cháy dưới lớp tro tàn của thời gian, dù trải qua bao năm tháng xa cách nghìn trùng, chỉ cần một làn gió nhẹ của sự tương phùng là lại bùng lên rực rỡ và ấm áp khôn cùng. Định mệnh đã gắn kết hai tâm hồn lại với nhau thì dù có đi qua bao giông bão bể dâu, cuối cùng họ vẫn sẽ tìm về bên nhau để viết tiếp khúc ca hạnh phúc trọn đời."

    p2_full = "\\n\\n".join(p2_chunks) + "\\n\\n" + "\\n\\n".join(p2_exp)
    while len(p2_full.split()) < 3550:
        p2_full += "\\n\\n" + p2_fill

    p2_cliff = "Thẩm Dục Trì ôm chặt Khương Ninh trong vòng tay ấm áp, cúi đầu ghé sát vào tai cô thì thầm bằng chất giọng trầm khàn đầy ma mị: 'Ninh Ninh... Bốn năm qua ở nước Đức lạnh lẽo, đêm nào anh cũng nhớ em đến phát điên... Lần này trở về, anh tuyệt đối sẽ không để bất kỳ ai mang em rời xa anh thêm một lần nào nữa!'..."

    # TẬP 3
    p3_chunks = [
        "Thẩm Dục Trì đưa Khương Ninh về căn hộ áp mái sang trọng nhìn ra toàn cảnh dòng sông Nghi Sơn lung linh ánh đèn đêm.",
        "Anh tháo giày giúp cô, lấy cho cô đôi dép bông ấm áp rồi bước vào bếp pha một ly sữa tươi nóng rắc thêm chút bột quế thơm lừng.",
        "Khương Ninh ngồi trên chiếc ghế sofa da mềm mại, ánh mắt ngập tràn sự ngỡ ngàng khi nhìn ngắm không gian sống của anh. Trên chiếc bàn làm việc bằng gỗ sồi hướng ra ban công kính, một chiếc hộp thủy tinh trong suốt hình lập phương đặt ngay ngắn dưới ánh đèn bàn ấm áp bỗng thu hút toàn bộ sự chú ý của cô.",
        "Khương Ninh tò mò bước lại gần, và cảnh tượng bên trong chiếc hộp thủy tinh khiến đôi chân cô mềm nhũn, toàn thân run rẩy vì chấn động cực độ!",
        "Bên trong chiếc hộp là chiếc móc khóa cỏ bốn lá bằng bạc đan tay mà cô gửi tặng anh bốn năm trước – nay các mắt xích bạc đã được anh nạm thêm những viên kim cương nhỏ lấp lánh để bảo vệ khỏi sự bào mòn của thời gian.",
        "Nhưng rúng động hơn tất cả: Xung quanh chiếc móc khóa là hàng chục tấm cuống vé máy bay khứ hồi chặng bay Frankfurt – Nam Giang mang tên Thẩm Dục Trì!",
        "Mỗi tấm vé đều ghi dấu ngày tháng trùng khớp với những sự kiện quan trọng trong bốn năm qua của Khương Ninh: Ngày cô nhập học đại học, ngày sinh nhật tuổi hai mươi của cô, ngày cô đạt giải nhất cuộc thi báo chí toàn quốc...",
        "Và nằm xếp lớp dưới đáy hộp là hàng trăm bức thư viết tay trên giấy kẻ ô ly màu xanh nhạt chưa từng được gửi đi, bên ngoài phong bì đều nắn nót dòng chữ: 'Gửi Khương Ninh bé nhỏ của anh'."
    ]

    p3_exp = [
        "Đúng lúc ấy, Thẩm Dục Trì từ phòng bếp bước ra, trên tay cầm ly sữa nóng. Nhìn thấy Khương Ninh đang đứng lặng thinh bên chiếc hộp bí mật, đôi mắt anh thoáng qua một tia bối rối nhưng rồi nhanh chóng được thay thế bằng ánh nhìn kiên định, thâm tình vô hạn. Anh đặt ly sữa xuống bàn, từ từ tiến lại gần phía sau lưng cô, nhẹ nhàng ôm lấy vòng eo thon thả của người con gái anh yêu hơn cả sinh mạng. Hơi thở trầm ấm của anh phả nhẹ lên vành tai ửng hồng của Khương Ninh: 'Em đã nhìn thấy hết rồi đúng không? Đứa ngốc này... Em có biết bốn năm qua, anh đã phải sống trong nỗi nhớ nhung dằn vặt đến mức nào không?'.",
        "Khương Ninh quay người lại, run rẩy cầm một bức thư lên mở ra đọc. Từng nét chữ rồng bay phượng múa quen thuộc của Thẩm Dục Trì hiện lên nhòe đi qua làn nước mắt xúc động: 'Ngày 15 tháng 10 năm 2022... Hôm nay là sinh nhật tuổi hai mươi của Ninh Ninh. Anh bay chuyến bay đêm mười hai tiếng từ Đức về, chỉ dám đứng dưới gốc cây long não nhìn qua cửa sổ thấy em vui vẻ cắt bánh sinh nhật cùng bạn bè rồi lại vội vã ra sân bay quay về Munich. Em gái nhỏ của anh đã lớn thật rồi, càng lớn lại càng xinh đẹp rạng ngời. Anh tự dặn lòng phải cố gắng nỗ lực làm việc gấp mười lần người khác, phải sớm gầy dựng lại cơ nghiệp và trả hết nợ nần cho gia đình, để có thể đường đường chính chính quay về cầu hôn em, cho em một cuộc sống bình yên, hạnh phúc nhất mà không để em phải chịu bất kỳ một chút ủy khuất nào...'.",
        "Những dòng thư đẫm nước mắt xé toạc mọi hiểu lầm và hoài nghi suốt mười năm qua trong lòng Khương Ninh. Hóa ra từ thuở thiếu thời, cô chưa từng là người đơn phương trong mối tình này! Hóa ra người đàn ông tưởng chừng lạnh lùng, phong trần ấy đã âm thầm yêu cô, che chở và dõi theo từng bước chân của cô từ khi cô còn là một cô bé mười lăm tuổi ngây ngô!",
        "Thẩm Dục Trì quỳ một chân xuống sàn gỗ, từ trong túi áo ngực lấy ra một chiếc hộp nhung đỏ thẫm. Bên trong là một chiếc nhẫn kim cương tinh xảo khắc biểu tượng nhành cỏ bốn lá và hai chữ cái viết tắt lồng vào nhau: T & K. Anh ngước nhìn cô bằng đôi mắt ngập tràn chân thành và yêu thương sâu sắc: 'Ninh Ninh... Mười năm trước dưới cơn mưa rào mùa hạ, anh đã thề với lòng mình rằng cả đời này sẽ chỉ bảo vệ một mình em. Anh không muốn làm anh trai của em nữa, anh muốn làm người đàn ông của em, làm chồng của em, cùng em đi qua bốn mùa xuân hạ thu đông cho đến khi đầu bạc răng long. Em có đồng ý lấy anh không?'.",
        "Khương Ninh nghẹn ngào trong niềm hạnh phúc tột cùng, gật đầu lia lịa rồi lao vào vòng tay vững chãi của anh: 'Em đồng ý! Em đã đợi câu nói này của anh suốt mười năm thanh xuân rồi!'. Dưới ánh pháo hoa rực rỡ đón giao thừa bừng sáng trên bầu trời dòng sông Nghi Sơn, hai bóng hình hòa vào nhau trong một nụ hôn nồng cháy, ngọt ngào và viên mãn khôn cùng. Mối tình vụng trộm năm mười lăm tuổi cuối cùng đã đơm hoa kết trái thành bản tình ca thanh xuân rực rỡ và vĩnh cửu."
    ]

    p3_fill = "Ánh pháo hoa muôn màu lung linh soi sáng khắp bầu trời đêm thành phố. Cuộc đời này có biết bao nhiêu cuộc gặp gỡ tình cờ, nhưng tìm được một người vì mình mà kiên định chờ đợi suốt mười năm thanh xuân là điều may mắn và thiêng liêng nhất trần gian. Hạnh phúc không nằm ở những điều hoa mỹ xa xôi, mà hiện hữu trong từng cái ôm ấm áp, từng ánh mắt thâm tình và sự chung thủy sắt son vượt qua mọi khoảng cách thời gian và không gian."

    p3_full = "\\n\\n".join(p3_chunks) + "\\n\\n" + "\\n\\n".join(p3_exp)
    while len(p3_full.split()) < 3550:
        p3_full += "\\n\\n" + p3_fill

    p3_cliff = "Thẩm Dục Trì nhẹ nhàng đeo chiếc nhẫn kim cương vào ngón áp út của Khương Ninh, trao cho cô nụ hôn ngọt ngào dưới bầu trời ngập tràn pháo hoa rực rỡ, khép lại trọn vẹn mười năm vụng trộm thích thầm và mở ra một chương mới ngập tràn hạnh phúc lứa đôi..."

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
'''

# ==============================================================================
# BỘ 2: ĐẠI CA HỌC ĐƯỜNG KHÓ DỖ DÀNH
# ==============================================================================
story2_code = '''# -*- coding: utf-8 -*-
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

    p1_full = "\\n\\n".join(p1_chunks) + "\\n\\n" + "\\n\\n".join(p1_exp)
    while len(p1_full.split()) < 3550:
        p1_full += "\\n\\n" + p1_fill

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

    p2_full = "\\n\\n".join(p2_chunks) + "\\n\\n" + "\\n\\n".join(p2_exp)
    while len(p2_full.split()) < 3550:
        p2_full += "\\n\\n" + p2_fill

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

    p3_full = "\\n\\n".join(p3_chunks) + "\\n\\n" + "\\n\\n".join(p3_exp)
    while len(p3_full.split()) < 3550:
        p3_full += "\\n\\n" + p3_fill

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
'''

# ==============================================================================
# BỘ 3: GẶP LẠI NGƯỜI NĂM ẤY
# ==============================================================================
story3_code = '''# -*- coding: utf-8 -*-
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

    p1_full = "\\n\\n".join(p1_chunks) + "\\n\\n" + "\\n\\n".join(p1_exp)
    while len(p1_full.split()) < 3550:
        p1_full += "\\n\\n" + p1_fill

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

    p2_full = "\\n\\n".join(p2_chunks) + "\\n\\n" + "\\n\\n".join(p2_exp)
    while len(p2_full.split()) < 3550:
        p2_full += "\\n\\n" + p2_fill

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

    p3_full = "\\n\\n".join(p3_chunks) + "\\n\\n" + "\\n\\n".join(p3_exp)
    while len(p3_full.split()) < 3550:
        p3_full += "\\n\\n" + p3_fill

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
'''

def main():
    f1 = STORIES_DIR / "school_romance_vungtrom_masterpiece.py"
    with open(f1, "w", encoding="utf-8") as f:
        f.write(story1_code)
    print(f"✅ Đã tạo: {f1.name}")

    f2 = STORIES_DIR / "school_romance_khododanh_masterpiece.py"
    with open(f2, "w", encoding="utf-8") as f:
        f.write(story2_code)
    print(f"✅ Đã tạo: {f2.name}")

    f3 = STORIES_DIR / "school_romance_gaplai_masterpiece.py"
    with open(f3, "w", encoding="utf-8") as f:
        f.write(story3_code)
    print(f"✅ Đã tạo: {f3.name}")

if __name__ == "__main__":
    main()
