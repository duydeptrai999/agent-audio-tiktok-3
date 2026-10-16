# -*- coding: utf-8 -*-
"""
core/stories/romance_school.py
Truyện Audio Ngôn Tình Thanh Xuân Vườn Trường 30 Phút:
Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp
Chuẩn độ dài toán học 1.5x: 3 Tập x ~3,480 - 3,520 từ (Tổng ~10,500 từ / >= 30 phút audio thực tế).
100% Zero-Biography Rule: Không giới thiệu lý lịch ("Tôi là...", "Năm nay... tuổi") ở 10 giây đầu.
100% Anti-Dropoff: Mở đầu ngay vào biến cố và giữ nhịp căng thẳng nghẹt thở xuyên suốt cả 3 tập.
Giọng đọc chỉ định: Hoài My (vi-VN-HoaiMyNeural) truyền cảm, nhấn nhá, ngắt nhịp thở chuẩn xác.
"""

from typing import Dict, Any

def get_30min_school_romance_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title and "hôn nhân" not in title.lower() and "quỷ khế" not in title.lower() and "căn phòng số 13" not in title.lower() else "Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp"
    
    part1_body = """'Nếu năm ấy cậu không đứng đợi dưới cơn mưa tầm tã suốt ba tiếng đồng hồ với chiếc áo đồng phục ướt sũng, có lẽ mười năm qua tôi đã không phải sống trong nỗi dằn vặt khôn nguôi này!' - Tiếng nấc nghẹn ngào của cô gái bỗng chốc làm cả khán phòng dạ tiệc họp lớp mười năm sau lặng phắc như tờ!

Những tiếng ly rượu vang va chạm leng keng bỗng chốc ngưng bặt hoàn toàn. Hàng chục ánh mắt của những người bạn học cũ khóa chuyên Toán năm xưa đổ dồn về phía góc bàn, nơi hai bóng hình đang đối diện nhau trong sự ngột ngạt đến nghẹt thở. Mười năm trôi qua kể từ mùa hè rực lửa của kỳ thi đại học năm ấy, người thiếu niên nghèo mặc chiếc áo sơ mi bạc màu với đôi mắt sáng ngời hoài bão ngày nào, giờ đây đã là một kiến trúc sư trưởng danh tiếng lẫy lừng của tập đoàn quốc tế. Anh khoác trên mình bộ vest màu ghi xám sang trọng, toát lên phong thái điềm đạm và quyền uy của một người thành đạt.

Thế nhưng đôi bàn tay của Cố Nam Thành lúc này lại đang run rẩy siết chặt lấy chiếc ly pha lê đến mức các khớp ngón tay trắng bệch. Ánh mắt sâu thẳm đen láy của anh dán chặt vào đôi mắt ngấn lệ của Hạ Mộc Miên - người con gái từng biến mất không một dấu vết ngay trong đêm bế giảng mười năm trước! Khuôn mặt Mộc Miên vẫn thanh tú như một đóa hoa dành dành đầu mùa, nhưng nét ngây thơ trong trẻo tuổi học trò đã được thay bằng vẻ trầm mặc, phong trần của người từng đi qua bão giông cuộc đời.

Chiếc váy dạ hội lụa đen giản dị càng làm nổi bật làn da trắng ngần và sợi dây chuyền mặt cỏ bốn lá bằng bạc cũ kỹ vẫn đeo ngay ngắn nơi xương quai xanh. Đó là kỷ vật duy nhất mà Nam Thành từng dùng toàn bộ tiền làm thêm giao báo suốt ba tháng ròng rã mỗi sáng sớm mùa đông lạnh cóng để mua tặng cô nhân ngày sinh nhật tuổi mười bảy!

Ký ức của những năm tháng thanh xuân thuần khiết bỗng chốc ùa về như một cuốn phim quay chậm trong tâm trí những người có mặt. Năm mười bảy tuổi, lớp học mười hai A nằm trên tầng ba của ngôi trường cổ rợp bóng phượng vĩ đỏ rực. Cố Nam Thành khi ấy là cậu học trò nghèo mồ côi cha, sống cùng người mẹ đau ốm triền miên trong căn nhà cấp bốn dột nát ven bờ sông ngoại thành.

Gia cảnh bần hàn khiến anh luôn mang một vẻ ngoài lạnh lùng, ít nói và khép kín với tất cả mọi người. Mỗi sáng sớm tinh mơ, Nam Thành luôn là người đến lớp đầu tiên để quét dọn phòng học, lau sạch bảng đen và sắp xếp lại từng dãy bàn ghế ngay ngắn. Chiếc áo đồng phục trắng sờn vai của anh luôn được giặt giũ phẳng phiu, thơm mùi xà phòng thơm rẻ tiền mà mẹ anh chắt chiu từng đồng mua ở chợ cóc.

Trái ngược với sự u trầm của Nam Thành, Hạ Mộc Miên lại là cô lớp phó học tập dịu dàng, hoạt bát với nụ cười tỏa nắng như sương mai. Cô là người duy nhất không bao giờ nhìn Nam Thành bằng ánh mắt thương hại hay xa lánh. Ngược lại, Mộc Miên luôn tìm mọi cách để lặng lẽ bước vào thế giới khép kín của cậu bạn cùng bàn kiên cường.

Mỗi buổi sáng, cô luôn lén nhét vào ngăn bàn của anh một chiếc bánh mì kẹp thịt còn nóng hổi, hoặc một chai sữa đậu nành ngọt lịm do chính tay mẹ cô nấu. Khi Nam Thành ngẩng lên ngơ ngác nhìn, Mộc Miên chỉ mỉm cười tinh nghịch, thì thầm: 'Tớ mua thừa một phần, cậu không ăn là lãng phí đấy nhé!'. Nam Thành biết rõ cô đang nói dối để giữ thể diện cho mình. Anh cắn từng miếng bánh mì ấm nóng, nuốt trọn cả sự biết ơn sâu sắc vào tận đáy lòng.

Những buổi chiều tan học muộn, khi sân trường chỉ còn lại tiếng ve râm ran và những tia nắng vàng vọt cuối ngày, hai đứa trẻ lại cùng nhau đạp xe qua những con phố rợp bóng cây xà cừ cổ thụ. Chiếc xe đạp phượng hoàng cà tàng của Nam Thành phát ra tiếng kêu cọt kẹt, nhưng phía sau yên xe, Mộc Miên luôn ngồi nghiêng người, hai tay khẽ túm lấy vạt áo đồng phục của anh, cất tiếng hát trong trẻo như chim sơn ca.

Những ngày trời đổ mưa rào bất chợt, hai đứa cùng nép mình dưới một chiếc ô rách cán, vừa đi vừa cười khúc khích dù gấu quần ướt sũng nước mưa. Những buổi tối mùa đông cúp điện đột ngột, lớp học chìm trong bóng tối dày đặc, hai đứa lại ngồi nép bên bậu cửa sổ, thắp lên một ngọn nến nhỏ le lói để cùng nhau giải những bài toán tích phân hóc búa.

Hơi ấm từ bàn tay lóng ngóng của chàng thiếu niên chạm nhẹ vào mu bàn tay nhỏ nhắn của cô bạn cùng bàn, làm cả hai cùng đỏ ửng mặt dưới ánh nến lung linh. Tim Nam Thành đập thình thịch như đánh trống trong lồng ngực. Anh vội vã rụt tay lại, lúng túng làm rơi cả cây bút mực xuống sàn nhà. Mộc Miên bật cười khúc khích, cúi người nhặt bút giúp anh, mái tóc đen mượt thoảng mùi hương bồ kết vương vấn quanh cánh mũi chàng trai trẻ.

Vào một buổi chiều hoàng hôn rực rỡ trước kỳ thi tốt nghiệp một tháng, khi cả lớp đã về hết, Nam Thành đã dùng mũi compa cẩn thận khắc lên góc mặt bàn gỗ của Mộc Miên một dòng chữ sâu hoắm: 'Đợi tôi đỗ Đại học Kiến trúc, tôi sẽ xây cho cậu một ngôi nhà ngập tràn hoa hồng'. Mộc Miên nhìn dòng chữ ấy, đôi mắt long lanh ngấn lệ vì xúc động. Cô khẽ nắm lấy bàn tay chai sần của anh, gật đầu thì thầm: 'Tớ sẽ đợi... Cho dù bao lâu, tớ cũng nhất định sẽ đợi cậu!'.

Tình cảm học trò thuần khiết và thiêng liêng ấy từng là ngọn hải đăng rực rỡ nhất soi sáng chuỗi ngày tăm tối, nghèo khó của tuổi trẻ Cố Nam Thành. Anh xem lời hứa ấy như kim chỉ nam của cuộc đời mình, ngày đêm vùi đầu vào sách vở, giải hàng nghìn đề thi để quyết tâm chạm tay vào cánh cổng trường đại học mơ ước.

Những ngày ôn thi căng thẳng nhất, Nam Thành nhịn ăn sáng suốt cả tháng trời để gom góp từng đồng mua tặng cô một chiếc kẹp tóc hoa cúc nhỏ bằng kim loại. Còn Mộc Miên lại âm thầm xin mẹ cuộn chỉ đỏ, tỉ mỉ ngồi thêu từng đường kim mũi chỉ lên chiếc áo khoác đồng phục bị sờn rách của anh. Cô thêu một bông hoa nhỏ nơi ngực áo, kèm theo một biểu tượng may mắn bí mật mà chỉ hai người mới hiểu.

Thế nhưng, cuộc đời vốn dĩ chưa bao giờ êm đềm như những trang lưu bút tuổi học trò. Ngay trước kỳ thi đại học ba ngày, một tai họa khủng khiếp từ trên trời giáng xuống đã vỡ vụn hoàn toàn giấc mơ thanh xuân của hai người. Mẹ của Nam Thành - người phụ nữ tần tảo cả đời làm phụ hồ trên các công trường - bất ngờ ngã quỵ từ giàn giáo cao xuống đất vì một cơn nhồi máu cơ tim cấp tính!

Khi Nam Thành hớt hải chạy vào bệnh viện huyện, người mẹ già đã hôn mê sâu trên giường cấp cứu, toàn thân cắm đầy những ống truyền dịch. Bác sĩ trưởng khoa nghiêm nét mặt thông báo một tin sét đánh: 'Mẹ cậu bị suy tim giai đoạn cuối kèm theo chấn thương phổi nặng. Nếu không tiến hành phẫu thuật thay van tim nhân tạo khẩn cấp trong vòng bảy mươi hai giờ tới, bà ấy sẽ không thể qua khỏi. Chi phí phẫu thuật trọn gói là năm trăm triệu đồng!'.

Năm trăm triệu đồng! Một con số thiên văn đối với một cậu học trò nghèo không một xu dính túi! Trong túi quần Nam Thành khi ấy chỉ còn vỏn vẹn ba mươi lăm nghìn đồng tiền làm thêm chưa kịp tiêu. Chàng trai mười tám tuổi gục ngã hoàn toàn, quỳ sụp xuống sàn hành lang bệnh viện lạnh ngắt, hai tay ôm chặt lấy đầu, những giọt nước mắt bất lực trào ra ướt đẫm vạt áo đồng phục. Anh tuyệt vọng nghĩ đến việc ký vào đơn bảo lưu kết quả học tập, từ bỏ kỳ thi đại học để đi vay nặng lãi hoặc bán thận cứu mẹ!

Chính trong khoảnh khắc Nam Thành cận kề bờ vực tuyệt vọng nhất, Lâm Uyển Nhi - cô hoa khôi kiêu kỳ của trường, con gái của viện trưởng bệnh viện tỉnh - đã âm thầm tìm gặp riêng Hạ Mộc Miên tại quán cà phê đối diện cổng bệnh viện. Uyển Nhi từ lâu đã đem lòng say mê tài năng và khí chất kiên cường của Nam Thành, nhưng luôn ôm lòng đố kỵ với tình cảm gắn bó như hình với bóng giữa anh và Mộc Miên.

Ngồi đối diện với Mộc Miên, Uyển Nhi đẩy sang một tờ séc ngân hàng trị giá đúng năm trăm triệu đồng, kèm theo một bản cam kết học bổng du học toàn phần tại Singapore dành cho Nam Thành do quỹ từ thiện của gia đình cô ta bảo trợ. Uyển Nhi nhìn Mộc Miên bằng ánh mắt sắc lạnh như băng tuyết, cất giọng tàn nhẫn:

'Gia đình tôi có thể cứu sống mẹ Nam Thành ngay trong đêm nay, đồng thời bảo đảm cho cậu ấy một tương lai xán lạn nhất mà một kẻ nghèo hèn như cô cả đời cũng không thể mang lại! Nhưng điều kiện duy nhất của tôi là: Cô phải vĩnh viễn biến mất khỏi thành phố này! Ngay sau đêm bế giảng, cô phải cắt đứt toàn bộ liên lạc và rời đi thật xa!'.

Uyển Nhi cười nhạt, buông thêm những lời cay độc như dao cứa vào tim cô gái nhỏ: 'Nếu cô thực sự yêu cậu ấy, hãy buông tay để cậu ấy bay cao! Còn nếu cô ích kỷ giữ cậu ấy lại bên mình, cậu ấy sẽ phải bỏ học đi bốc vác kiếm tiền trả nợ, và mẹ cậu ấy sẽ chết trong đau đớn vì sự cố chấp của cô! Hãy chọn đi: Tình yêu ích kỷ của cô, hay tính mạng của mẹ Nam Thành và tương lai của cậu ấy?'.

Những lời đay nghiến tàn nhẫn ấy như bóp nghẹt từng nhịp thở của Mộc Miên. Nhìn qua khung cửa kính bệnh viện, thấy Nam Thành đang quỳ gối van xin bác sĩ kéo dài thời gian đóng viện phí, trái tim Mộc Miên đau đớn như bị hàng nghìn mảnh thủy tinh đâm nát. Cô cắn chặt môi đến bật máu, hai bàn tay siết chặt tà áo đồng phục đến run rẩy. Vì người con trai mình yêu hơn cả tính mạng, cô gái nhỏ mười tám tuổi năm ấy đã nuốt trọn toàn bộ cay đắng, gật đầu chấp thuận bản giao ước tàn nhẫn ấy!

Để Nam Thành có thể toàn tâm toàn ý bước vào phòng thi mà không vướng bận bất kỳ điều gì, Mộc Miên đã âm thầm giấu kín toàn bộ sự thật đau lòng. Cô giả vờ như không có chuyện gì xảy ra, vẫn mỉm cười động viên anh hoàn thành xuất sắc kỳ thi đại học với số điểm thủ khoa rực rỡ.

Thế nhưng ngay trong đêm liên hoan bế giảng sau kỳ thi, khi Nam Thành háo hức cầm bó hoa dại đứng đợi cô dưới gốc cây phượng vĩ cổ thụ suốt ba tiếng đồng hồ dưới cơn mưa giông tầm tã, Mộc Miên đã không bao giờ xuất hiện nữa. Anh đứng đó trong bóng đêm mịt mùng, mặc cho những hạt mưa quất rát bỏng vào da thịt, đôi mắt đỏ hoe ngóng trông bóng hình quen thuộc của cô bạn cùng bàn.

Anh không hề hay biết rằng, ngay trong buổi tối định mệnh ấy, Mộc Miên đang ngồi trên chuyến xe khách đò muộn, ôm người mẹ ruột cũng đang mắc bạo bệnh lặng lẽ rời khỏi thành phố trong nước mắt lã chã rơi. Sáng hôm sau, khi Nam Thành sốt cao run rẩy tìm đến căn nhà trọ của Mộc Miên, nơi đó chỉ còn lại cánh cửa sắt hoen gỉ bị khóa chặt bằng một ổ khóa lạnh lùng. Cô gái nhỏ đã dọn đi không để lại một dòng thư, không một lời từ biệt!

Chàng thiếu niên mười tám tuổi ngã quỵ ngay trước hiên nhà trọ, cơn sốt cao co giật biến chứng thành viêm phổi nặng khiến anh phải nhập viện cấp cứu suốt hai tuần ròng rã. Trong cơn mê man sốt li bì, anh liên tục gọi tên Mộc Miên trong tuyệt vọng. Khi tỉnh lại, người đầu tiên anh nhìn thấy bên giường bệnh là Lâm Uyển Nhi cùng lời thông báo rằng viện phí của mẹ anh đã được gia đình họ Lâm thanh toán toàn bộ.

Cùng lúc đó, những lời đồn thổi ác ý bắt đầu lan truyền khắp trường học: Rằng Hạ Mộc Miên đã theo một đại gia giàu có chuyển vào phương Nam sinh sống, vứt bỏ người bạn trai nghèo rớt mồng tơi như một món đồ chơi cũ kỹ! Nỗi đau đớn bị người mình yêu sâu đậm nhất phản bội đã hóa thành một vết sẹo đen ngòm, hằn sâu vào tâm can Nam Thành suốt mười năm ròng rã, biến anh thành một người đàn ông lạnh lùng, sắt đá và khép kín trái tim với tất cả mọi người.

Quay trở lại thực tại của đêm dạ tiệc họp lớp mười năm sau, không khí trong khán phòng khách sạn năm sao vẫn ngột ngạt và căng thẳng như một dây cung kéo căng. Đúng lúc này, người lớp trưởng năm xưa bước lên bục sân khấu, hai tay cẩn thận bê một chiếc hộp thiếc gỉ sét phủ đầy bụi bặm thời gian đặt lên giữa bàn trà:

'Các bạn ơi, hôm nay trước khi phá dỡ dãy phòng học cũ để xây dựng trường mới, thầy hiệu trưởng đã tình cờ tìm thấy chiếc hộp Nguyện Ước Thời Gian của khóa mười hai A chúng ta mười năm trước! Mười năm trước trong tiết sinh hoạt cuối cùng, mỗi người trong chúng ta đều đã bí mật viết một bức thư gửi cho người mình thầm thương trộm nhớ nhất, hẹn rằng đúng mười năm sau sẽ cùng nhau mở ra!'.

Tiếng reo hò, vỗ tay của bạn bè xung quanh bỗng chốc vang lên rộn rã. Thế nhưng Mộc Miên lại giật thót mình, bước chân vô thức lùi lại phía sau một bước, lồng ngực đập dồn dập đến mức khó thở. Bởi vì cô biết rõ hơn ai hết, bên trong chiếc hộp thiếc ấy chứa đựng bức thư tỏ tình dài năm trang giấy tập học trò của cô gửi cho Cố Nam Thành, cùng toàn bộ những lời hẹn ước ngây thơ của tuổi mười bảy!

Lâm Uyển Nhi - người giờ đây đang khoác tay Nam Thành với tư cách vị hôn thê môn đăng hộ đối được hai gia đình sắp đặt - khẽ nhếch mép cười khẩy. Cô ta bước tới, cố tình lục lọi trong chiếc hộp thiếc và rút ra một phong bì thư màu xanh nhạt đã ố vàng theo năm tháng:

'Ôi chao, nét chữ nắn nót dịu dàng này chẳng phải của lớp phó học tập Hạ Mộc Miên sao? Để tôi đọc cho cả lớp cùng nghe nhé: Gửi Cố Nam Thành... Nếu sau này cậu trở thành một kiến trúc sư vĩ đại, tớ ước gì có thể làm người đầu tiên bước vào ngôi nhà hoa hồng của cậu...'.

Uyển Nhi ngẩng đầu lên, ánh mắt sắc như dao lam quét qua khuôn mặt tái nhợt của Mộc Miên, cất giọng châm chọc đầy cay nghiệt: 'Mộc Miên à, lời lẽ nghe thật cảm động biết bao! Thế nhưng năm đó vừa thi xong đại học, cô lại nhận tiền của người khác rồi bỏ trốn mất tăm mất tích, bỏ mặc Nam Thành đợi chờ dưới mưa đến mức suýt mất mạng! Mười năm qua cô trốn chui trốn nhủi ở đâu, để hôm nay lại mò về đây đóng vai kẻ si tình đáng thương trước mặt mọi người?'.

Những lời lăng mạ nhục mạ sắc mỏng của Uyển Nhi khiến bạn bè xung quanh bắt đầu xì xào bàn tán, những ánh mắt nhìn Mộc Miên dần chuyển sang sự nghi ngờ và coi thường. Mộc Miên cắn chặt môi đến bật máu, từng giọt nước mắt tủi nhục lăn dài trên gò má gầy guộc. Cô không thể giải thích, bởi vì lời thề bảo mật năm xưa để bảo vệ danh dự cho mẹ Nam Thành vẫn như một sợi xích vô hình khóa chặt lấy cổ họng cô!"""
    part1_cliff = """Cố Nam Thành bước từng bước nặng nề tiến lại gần Mộc Miên. Bóng dáng cao lớn, uy quyền của anh bao trùm lấy thân hình nhỏ bé đang run rẩy của cô gái. Giọng nói của Nam Thành trầm đục, vỡ vụn từng hồi vì nỗi đau đớn kìm nén suốt một thập kỷ:

'Hạ Mộc Miên... Hãy nhìn thẳng vào mắt tôi và trả lời! Tại sao năm đó cậu lại nhẫn tâm bỏ đi không một lời từ biệt? Cậu có biết tôi đã đứng dưới mưa trước cổng nhà cậu suốt một đêm ròng rã, cầu xin cậu xuất hiện dù chỉ một giây không? Mười năm qua, trong mắt cậu, lời hứa năm mười bảy tuổi của chúng ta và tình cảm của tôi thực sự rẻ rúng đến thế sao?'.

Mộc Miên nghẹn ngào lắc đầu trong làn nước mắt nhạt nhòa, hai bàn tay siết chặt lấy chiếc túi xách giả da đã sờn rách mép: 'Nam Thành... Xin cậu đừng hỏi nữa... Tôi không hề phản bội cậu... Chưa từng có một giây phút nào trong đời tôi phản bội cậu cả... Có những chuyện, thà để một mình tôi gánh chịu còn hơn làm tổn thương đến người khác...'.

'Vậy tại sao cô lại bỏ đi? Tại sao lại cắt đứt mọi liên lạc, vứt bỏ toàn bộ những ước hẹn năm xưa?' - Nam Thành gầm lên trong đau đớn cùng cực, lồng ngực anh phập phồng dữ dội, bàn tay anh bất ngờ vươn ra, nắm chặt lấy cổ tay mảnh khảnh của Mộc Miên kéo mạnh về phía mình! Anh muốn nhìn thấy sự ân hận trong mắt cô, muốn nghe một lời giải thích chân thật nhất sau mười năm đằng đẵng chờ đợi trong tuyệt vọng!

Thế nhưng trong lúc hai người giằng co kịch liệt giữa trung tâm khán phòng tiệc, quai chiếc túi xách cũ kỹ đã mục chỉ của Mộc Miên bỗng chốc đứt phựt! Toàn bộ chiếc túi rơi thẳng xuống nền đá cẩm thạch phát ra một tiếng va chạm chát chúa!

Từ bên trong chiếc túi rơi tung tóe khắp mặt sàn: Một cuốn sổ nhật ký bìa xanh đã sờn rách gáy, chiếc kẹp tóc hoa cúc nhỏ bằng kim loại đã gỉ sét của mười năm trước, và hàng chục tờ biên lai chuyển tiền ngân hàng định kỳ đã ố vàng theo năm tháng!

Một tờ biên lai rơi ngay dưới mũi giày da của Cố Nam Thành. Ánh mắt anh vô tình liếc xuống, và toàn bộ huyết quản trong cơ thể anh bỗng chốc đông cứng lại khi nhìn thấy dòng chữ viết tay bằng mực đỏ tươi ngay trên đầu trang biên lai:

'Nội dung chuyển khoản: Mỗi tháng gửi năm triệu đồng chu cấp viện phí điều trị cho mẹ Cố Nam Thành tại viện dưỡng lão Ánh Dương - Tên người gửi: Hạ Mộc Miên'!"""

    part2_body = """'Nội dung chuyển khoản: Mỗi tháng gửi năm triệu đồng chu cấp viện phí điều trị cho mẹ Cố Nam Thành tại viện dưỡng lão Ánh Dương - Tên người gửi: Hạ Mộc Miên!' - Từng con chữ viết tay nắn nót bằng mực đỏ tươi đập thẳng vào mắt Cố Nam Thành như một tia sét rạch ngang bầu trời quang đãng!

Toàn bộ đại sảnh tiệc của khách sạn năm sao bỗng chốc rơi vào một sự im lặng chết chóc. Tiếng gió rít qua khe cửa kính dường như cũng ngưng bặt. Nam Thành đứng chôn chân tại chỗ, cả người cứng đờ như một bức tượng đá. Bàn tay anh đang nắm chặt lấy cổ tay Mộc Miên bỗng chốc mất hết lực, từ từ buông lỏng ra rồi run rẩy dữ dội không cách nào kìm nén nổi.

Đầu óc Nam Thành quay cuồng dữ dội. Mười năm qua, mẹ anh dù được phẫu thuật van tim thành công nhưng sức khỏe suy kiệt nặng nề, phải nằm điều trị nội trú dài hạn tại một viện dưỡng lão cao cấp ở ngoại ô thành phố. Cứ đúng ngày mùng năm hàng tháng, tài khoản viện phí của mẹ anh luôn nhận được một khoản tiền năm triệu đồng chuyển khoản định kỳ từ một nhà hảo tâm ẩn danh, với lời nhắn duy nhất gửi kèm: 'Chúc bác luôn bình an, xin bác giữ gìn sức khỏe để Nam Thành yên tâm học tập và lập nghiệp'.

Nam Thành từng vô số lần đến ngân hàng và ban quản lý viện dưỡng lão để dò hỏi danh tính của vị ân nhân bí ẩn ấy, nhưng nhân viên luôn thông báo rằng người gửi yêu cầu bảo mật thông tin tuyệt đối. Suốt ngần ấy năm tháng, Lâm Uyển Nhi luôn bóng gió ám chỉ rằng đó là quỹ hỗ trợ đặc biệt do tập đoàn y tế của bố cô ta tài trợ cho gia đình anh. Anh đã tin vào điều đó, đã cảm kích gia đình họ Lâm suốt một thập kỷ qua!

Thế nhưng giờ đây, hàng chục tờ biên lai nộp tiền mặt tại bưu điện và ngân hàng với chữ ký tay run rẩy mang tên 'Hạ Mộc Miên' đang nằm vương vãi ngay dưới chân anh. Ngày tháng trên biên lai trải dài liên tục suốt mười năm ròng rã, từ tháng chín năm hai nghìn mười sáu cho đến tận tháng trước! Từng tờ giấy ố vàng vì thời gian, mép giấy nhăn nhúm vì mồ hôi và nước mắt, đã xé toạc hoàn toàn bức màn dối trá đen tối suốt mười năm qua!

Lâm Uyển Nhi đứng bên cạnh tái mét mặt mày, đồng tử co rút lại vì kinh hoàng tột độ. Cô ta nhận ra chiếc bẫy dối trá hoàn hảo mà mình dày công dựng lên suốt một thập kỷ đang đứng trước bờ vực sụp đổ tan tành. Không một giây chần chừ, Uyển Nhi vội vã lao tới, giẫm mạnh gót giày cao gót nhọn hoắt lên xấp biên lai hòng dùng chân giẫm nát chứng cứ!

Cô ta gào lên the thé, giọng nói run rẩy đầy hoảng loạn: 'Nam Thành! Anh đừng có để con nhỏ xảo quyệt này lừa gạt! Mấy tờ giấy rác rưởi này chắc chắn là đồ giả mạo do nó thuê người làm để phá hoại lễ đính hôn của chúng ta! Một đứa con gái nghèo rớt mồng tơi như nó, mười năm qua làm thuê làm mướn còn không đủ ăn, lấy đâu ra năm triệu mỗi tháng suốt mười năm trời? Nó cố tình gài bẫy để vòi tiền của anh đấy! Anh quên rằng năm đó chính bố em đã cứu mạng bác gái sao?'.

'CÂM MIỆNG LẠI!' - Một tiếng gầm kinh thiên động địa vang lên từ cổ họng Cố Nam Thành!

Âm thanh gầm thét xé lòng ấy khiến toàn bộ khách mời trong khán phòng giật bắn mình khiếp sợ. Ánh mắt Nam Thành lúc này đỏ ngầu như máu, trừng trừng nhìn Uyển Nhi với một ngọn lửa cuồng nộ và căm hờn tột cùng chưa từng thấy. Anh vung tay gạt phắt Uyển Nhi sang một bên với một sức mạnh khủng khiếp khiến cô ta ngã dúi dụi xuống sàn thảm nhung, rơi cả chiếc vương miện cài tóc đắt tiền!

'Đừng dùng bàn tay dơ bẩn của cô chạm vào những kỷ vật này!' - Nam Thành nghiến răng thốt ra từng từ lạnh như băng. Người đàn ông quyền lực từng khiến hàng chục đối thủ kinh doanh phải khiếp sợ bỗng quỳ sụp một gối xuống nền đá lạnh ngắt. Đôi bàn tay run rẩy của anh nâng niu nhặt từng tờ hóa đơn chuyển tiền, từng mảnh giấy nhỏ bị rách mép, và nhẹ nhàng lật mở cuốn sổ nhật ký bìa xanh đã mục nát gáy của Hạ Mộc Miên.

Dưới ánh đèn chùm pha lê rực rỡ của khán phòng tiệc, từng trang viết bằng nét mực tím thân thương thuở học trò hiện ra trước mắt Nam Thành. Từng con chữ, từng dòng nhật ký như những nhát dao lam cứa sâu vào từng thớ thịt trong lồng ngực anh:

'Ngày 15 tháng 9 năm 2016... Hôm nay Nam Thành nhập học thủ khoa Đại học Kiến trúc rồi. Mình đứng từ xa nhìn cậu ấy mặc áo sơ mi trắng bước lên bục nhận bằng khen, tim mình thắt lại vì nhớ cậu ấy... Chiều nay mình vừa nhận thêm ca làm ca đêm tại xưởng may gia công giày da. Mười hai tiếng đứng liên tục, lưng đau buốt và ngón tay bị kim đâm chảy máu, nhưng tiền công vừa vặn đủ năm triệu đồng để kịp gửi đóng tiền thuốc trợ tim tháng này cho mẹ Nam Thành... Chỉ cần mẹ cậu ấy sống khỏe mạnh, Nam Thành sẽ không phải bận lòng...'.

'Ngày 24 tháng 12 năm 2018... Đêm Giáng Sinh ở miền biển lạnh buốt đến thấu xương. Gió bấc rít từng hồi qua khe cửa liếp rách nát của hai mẹ con mình. Mình vừa rửa xong ba trăm chiếc bát đĩa dầu mỡ ngoài quán ăn đêm, hai bàn tay tê cóng nứt nẻ rớm máu không thể cầm nổi đôi đũa. Nhưng khi đi ngang qua tiệm điện máy, nhìn thấy hình ảnh Nam Thành trên bản tin thời sự nhận giải nhất Kiến trúc sư trẻ toàn quốc, mình đã đứng dưới mưa tuyết mà bật khóc nức nở vì hạnh phúc... Nam Thành của mình giỏi lắm, cậu ấy đang bước đi trên con đường rực rỡ ánh hào quang... Sự hy sinh trong bóng tối của mình suốt những năm qua hoàn toàn xứng đáng rồi...'.

'Ngày 10 tháng 5 năm 2021... Căn bệnh suy thận giai đoạn cuối của mẹ mình tái phát nặng. Tiền thuốc men của hai người mẹ vượt quá sức chịu đựng của một người con gái côi cút như mình. Nhiều đêm thức trắng bên bàn máy may, ho ra máu vì kiệt sức, mình chỉ ước gì được một lần quay trở lại hành lang lớp mười hai A năm ấy, được nghe tiếng Nam Thành gọi tên mình dưới bóng cây bàng rợp mát... Nhưng mình không thể quay lại... Lời hứa bảo mật với viện trưởng Lâm vẫn là sợi dây xích trói buộc mình... Nếu mình vi phạm, họ sẽ cắt thuốc điều trị của mẹ Nam Thành... Mình phải kiên cường, phải sống tiếp vì cậu ấy...'.

Từng giọt nước mắt nóng hổi của Cố Nam Thành rơi lộp độp xuống những trang nhật ký đã ố vàng, làm nhòe đi những dòng mực tím thân thương. Trái tim người đàn ông như bị một bàn tay vô hình bóp nghẹt đến vỡ vụn.

Trời đất ơi! Mười năm qua, anh đã làm cái gì thế này? Anh đã ôm mối hận thù mù quáng, đã nguyền rủa người con gái mình yêu thương nhất là kẻ tham lam phụ bạc, là kẻ hám tiền bỏ rơi anh trong lúc khốn cùng nhất! Nhưng sự thật tàn nhẫn lại là: Thiên thần nhỏ bé ấy đã âm thầm bán đi cả tuổi thanh xuân tươi đẹp nhất, bán đi cả danh dự, tương lai và sức khỏe của chính mình, cắn răng chịu đựng sự đày đọa nơi đầu đường xó chợ để gom góp từng đồng tiền lẻ nuôi sống người mẹ già của anh, chắp cánh cho ước mơ của đời anh bay cao!

Ký ức nghèo khó thuở thiếu thời lại hiện về xé nát tâm can Nam Thành: Mùa đông năm mười bảy tuổi, Mộc Miên luôn nhường anh chiếc áo khoác ấm duy nhất, còn mình thì co ro trong tấm khăn len mỏng manh. Anh từng thề non hẹn biển sẽ xây cho cô một ngôi nhà hoa hồng ngập tràn hạnh phúc, vậy mà suốt mười năm qua, anh lại để cô phải một mình gồng gánh những bi kịch nghiệt ngã nhất của số phận giữa chốn nhân gian lạnh lẽo!

Để có đủ số tiền năm mươi triệu nộp khoản tạm ứng viện phí đầu tiên năm ấy, Mộc Miên thậm chí đã bán đi chiếc nhẫn ngọc gia bảo của người bà quá cố để lại - kỷ vật thiêng liêng duy nhất mà cô từng nâng niu hơn cả tính mạng mình. Cô đã quỳ dưới mưa bão ngoài cổng bệnh viện suốt một đêm ròng rã, dập đầu đến chảy máu trán để van xin bác sĩ đừng rút ống thở của mẹ anh khi thủ tục bảo hiểm gặp trục trặc!

Cố Nam Thành từ từ đứng dậy. Cả người anh toát ra một luồng sát khí và phẫn nộ ngút trời khiến tất cả mọi người trong khán phòng tiệc phải lùi lại vì kinh sợ. Anh quay phắt người lại, ánh mắt rực lửa nhìn thẳng vào Lâm Uyển Nhi đang ngồi co rúm dưới sàn nhà:

'Lâm Uyển Nhi! Mười năm trước, chính cô và gia đình cô đã dùng tính mạng mẹ tôi ra để ép buộc Mộc Miên phải ký vào bản giao ước tàn nhẫn đó đúng không? Bản hợp đồng từ thiện năm xưa thực chất là một âm mưu bẩn thỉu dùng tiền mua đứt hạnh phúc của hai con người! Gia đình cô đã cướp đi mười năm thanh xuân của cô ấy, cướp đi người con gái tôi yêu nhất, rồi bắt tôi phải mang ơn các người suốt một thập kỷ qua!'.

Uyển Nhi run rẩy bò tới, ôm lấy chân Nam Thành van nài trong nước mắt: 'Nam Thành... Em xin anh... Em làm tất cả những điều đó chỉ vì quá yêu anh thôi! Em muốn anh có một tương lai tốt đẹp, muốn anh thuộc về em... Chẳng lẽ tình cảm mười năm qua em dành cho anh không bằng mấy trang nhật ký rách nát của nó sao?'.

'Tình cảm của cô làm tôi ghê tởm!' - Nam Thành lạnh lùng gạt phắt chân ra, giọng nói đanh thép vang vọng khắp khán phòng tiệc như một bản tuyên án tử hình:

'Hôm nay, trước mặt toàn thể thầy cô, bạn bè và đối tác, tôi xin tuyên bố: Hôn ước giữa Cố Nam Thành này và Lâm Uyển Nhi bị hủy bỏ hoàn toàn và vĩnh viễn! Toàn bộ dự án quy hoạch tổ hợp bệnh viện quốc tế năm trăm tỷ đồng mà tập đoàn tôi đang hợp tác với gia đình họ Lâm sẽ bị đơn phương chấm dứt ngay từ giây phút này! Tôi thà bồi thường hợp đồng, thà phá sản trắng tay, cũng tuyệt đối không bao giờ dây dưa với những kẻ độc ác và dối trá như gia tộc các người!'.

Những lời đanh thép của Nam Thành như một đòn sét đánh giáng thẳng vào tham vọng của gia đình họ Lâm. Khách mời xung quanh đồng loạt xì xào, những ánh mắt nhìn Uyển Nhi giờ đây chỉ còn lại sự khinh bỉ và ghê tởm tột cùng.

Những người bạn học cũ khóa mười hai A năm xưa đứng xung quanh giờ đây đều cúi gằm mặt xuống đất trong sự xấu hổ và ân hận tột cùng. Có người từng vì a dua nịnh hót gia thế giàu sang của nhà họ Lâm mà vô cớ cô lập, buông lời mỉa mai Mộc Miên ngày trước. Có người từng tin sái cổ những lời đồn thổi ác ý của Uyển Nhi rằng Mộc Miên hám giàu bỏ bạn.

Giờ đây, khi sự thật hy sinh mười năm ròng rã vì tình yêu và chữ hiếu của cô gái nhỏ được phơi bày trần trụi dưới ánh đèn pha lê, ai nấy đều cảm thấy một nỗi nhục nhã ê chề gặm nhấm tâm can. Cậu lớp trưởng năm xưa bước tới, nghẹn ngào cúi đầu trước Mộc Miên: 'Mộc Miên à... Thầy cô và bạn bè nợ cậu một lời xin lỗi... Mười năm qua cậu đã phải chịu đựng quá nhiều bất công rồi...'.

Mộc Miên khẽ lắc đầu, những ngón tay run rẩy ôm chặt lấy cuốn nhật ký vào lồng ngực gầy guộc. Trong tâm trí cô, ký ức của những đêm đầu tiên rời xa thành phố lại ùa về rõ mồn một. Đêm ấy, trên chuyến xe khách đò muộn lắc lư trong gió bão, cô ôm người mẹ ruột đang sốt cao co giật chuyển đến một làng chài hẻo lánh phía nam.

Căn phòng trọ mười mét vuông dột nát ven biển ngập ngụa mùi tanh của cá và ẩm mốc của rong rêu. Những đêm đông rét mướt sóng biển gầm rú từng hồi như muốn nuốt chửng căn chòi lá, cô ngồi co ro dưới ánh đèn dầu leo lét, hai bàn tay rướm máu vì vá lưới thuê, vừa khóc vừa viết những dòng tâm sự vào cuốn sổ nhật ký mà không bao giờ dám gửi đi. Mọi đắng cay của kiếp người cô đều đã nếm trải, nhưng chưa từng một giây phút nào cô để bản thân gục ngã, bởi lời hứa giữ cho mẹ Nam Thành sống sót luôn là ngọn lửa sưởi ấm tâm hồn cô giữa giông bão cuộc đời!

Đúng lúc sự thật kinh hoàng vừa được phơi bày ra ánh sáng, một âm thanh chát chúa từ bên ngoài sảnh khách sạn bỗng xé toạc màn đêm: Tiếng còi xe cấp cứu inh ỏi hú vang dồn dập!

Chiếc điện thoại trong túi áo vest của Nam Thành bỗng rung lên bần bật. Anh bấm máy, và đầu dây bên kia vang lên giọng nói gấp gáp, nghẹn ngào của bác sĩ trưởng viện dưỡng lão Ánh Dương:

'Giám đốc Cố! Không xong rồi! Mẹ của cậu vừa lên cơn suy hô hấp cấp tính và trụy tim đột ngột! Hiện tại xe cấp cứu của chúng tôi đang chuyển viện khẩn cấp về Bệnh viện Đa khoa Trung ương! Trong lúc mê sảng cận kề cái chết, bà ấy liên tục nắm chặt lấy tay y tá, khóc lóc gọi tên cô bé Mộc Miên và nhắc đến chiếc áo đồng phục học sinh năm xưa! Tình hình vô cùng nguy kịch, tim bà ấy đã ngừng đập một lần trên xe! Cậu phải đến bệnh viện ngay lập tức!'.

Nam Thành bàng hoàng buông rơi điện thoại. Anh ngẩng đầu lên, ánh mắt hoảng loạn chạm vào ánh mắt ngấn lệ của Mộc Miên. Không một giây chần chừ, Mộc Miên lao tới nắm chặt lấy cánh tay anh: 'Nam Thành! Mau lên! Chúng ta phải đến bệnh viện với bác gái ngay!'.

Bỏ lại sau lưng khán phòng dạ tiệc náo loạn, bỏ lại Lâm Uyển Nhi đang gào khóc thảm thiết trong sự sụp đổ, Nam Thành nắm chặt bàn tay nhỏ bé lạnh ngắt của Mộc Miên, cùng cô lao thẳng ra khỏi sảnh khách sạn.

Bên ngoài trời đang đổ mưa xối xả, sấm chớp rạch ngang bầu trời đêm đen kịt. Nam Thành mở cửa chiếc xe thể thao màu đen, kéo Mộc Miên vào ghế phụ rồi đạp lút chân ga. Chiếc xe lao vun vút vào màn mưa bão mù mịt, vượt qua từng ngã tư đèn đỏ hướng thẳng về phía Bệnh viện Đa khoa Trung ương trong cuộc chạy đua nghẹt thở với tử thần!

Ngồi trên ghế lái, đôi bàn tay của Nam Thành siết chặt lấy vô lăng đến mức gân xanh nổi cuồn cuộn. Gạt nước trên kính chắn gió quất liên hồi nhưng không thể xua đi được màn mưa dày đặc như trút nước. Anh quay sang nhìn Mộc Miên, thấy cô đang chắp hai tay trước ngực, nhắm chặt mắt cầu nguyện cho mẹ anh mà nước mắt tuôn rơi như mưa.

Trái tim Nam Thành nghẹn lại từng cơn đau xé ruột. Anh vươn một tay sang, nắm chặt lấy bàn tay lạnh ngắt của cô, cất giọng trầm khàn nghẹn ngào:

'Mộc Miên... Mười năm qua, anh đã vẽ hàng trăm bản thiết kế công trình lớn nhỏ trên khắp thế giới. Nhưng em có biết không... Ở mỗi một bản vẽ tâm huyết nhất của đời mình, anh đều cố tình thiết kế một khung cửa sổ lớn bằng kính hướng về phía nam - nơi anh luôn ôm một niềm tin mù quáng rằng một ngày nào đó em sẽ trở về... Anh xin lỗi em... Anh nợ em cả một cuộc đời này...'.

Mộc Miên lắc đầu trong nước mắt, những ngón tay nhỏ nhắn siết chặt lấy tay anh: 'Đừng nói nữa Nam Thành... Chỉ cần bác gái bình an, mọi cay đắng mười năm qua của em đều không còn quan trọng nữa... Xin ông trời hãy cứu lấy mẹ...'.

Mười năm hiểu lầm và xa cách dường như đã tan biến hoàn toàn trong từng nhịp thở dồn dập giữa màn mưa đêm bão táp. Hai tâm hồn từng chịu đựng muôn vàn vết thương sâu hoắm giờ đây lại hòa chung một nhịp đập, cùng nhau hướng về người mẹ thân yêu đang chiến đấu giành giật sự sống nơi phòng cấp cứu!"""
    part2_cliff = """Chiếc xe thể thao phanh cháy lốp trước sảnh cấp cứu Bệnh viện Đa khoa Trung ương, tạo thành một vệt dài khét lẹt trên nền đường ướt sũng. Nam Thành và Mộc Miên bật cửa xe lao vào trong màn mưa, quần áo ướt sũng chạy thẳng lên tầng ba khu hồi sức tích cực.

Khi hai người vừa chạy tới trước cửa phòng cấp cứu, cánh cửa kim loại nặng nề bỗng từ từ bật mở. Vị bác sĩ trưởng khoa bước ra, tháo chiếc khẩu trang y tế xuống, lắc đầu buồn bã nhìn Nam Thành:

'Giám đốc Cố... Chúng tôi đã dùng sốc điện tim ba lần và tiêm thuốc trợ tim liều tối đa... Nhưng cơ tim của bà ấy đã bị hoại tử diện rộng... Nhịp tim hiện tại rất yếu, chỉ số sinh tồn đang tụt dốc không phanh... Bà ấy chỉ còn vài phút tỉnh táo cuối cùng thôi... Cậu hãy vào nhìn mặt mẹ lần cuối...'.

Lời thông báo như một nhát búa tạ giáng thẳng vào đầu Nam Thành, khiến anh lảo đảo suýt ngã quỵ xuống sàn hành lang. Nhưng Mộc Miên đã nhanh chóng vòng tay ôm chặt lấy anh, đỡ lấy cơ thể run rẩy của người đàn ông: 'Nam Thành! Em ở bên anh! Chúng ta vào với mẹ mau lên!'.

Hai người vội vã lao vào trong phòng bệnh ngột ngạt mùi thuốc sát trùng. Giữa tiếng máy monitor đo nhịp tim phát ra những tiếng 'tít... tít...' chậm dần và rời rạc, người mẹ già với khuôn mặt hốc hác, làn da xám xịt đang nằm thoi thóp trên giường bệnh trắng toát.

Thế nhưng, ngay khoảnh khắc Hạ Mộc Miên vừa bước chân tới mép giường bệnh, đôi mắt nhắm nghiền của người mẹ già bỗng từ từ hé mở. Nhìn thấy bóng hình cô gái nhỏ năm xưa, khóe mắt nhăn nheo của bà bỗng ứa ra hai hàng nước mắt đục ngầu.

Bàn tay gầy guộc chằng chịt những vết kim tiêm bầm tím của bà run rẩy vươn lên, nắm chặt lấy bàn tay của Mộc Miên. Sau đó, bà dùng chút sức tàn cuối cùng, chậm rãi kéo khóa chiếc túi vải thổ cẩm cũ kỹ luôn đeo trước ngực, rút ra một kỷ vật được bọc cẩn thận qua ba lớp giấy báo khiến Cố Nam Thành chết lặng hoàn toàn:

Đó chính là chiếc áo sơ mi đồng phục học sinh trắng tinh khôi năm mười tám tuổi của Nam Thành, nơi góc ngực áo vẫn còn in hằn bông hoa nhỏ và dòng chữ tỏ tình được thêu tỉ mỉ bằng chỉ đỏ năm nào!"""

    part3_body = """'Chiếc áo đồng phục này... mười năm trước là chính con đã tỉ mỉ thêu dòng chữ hẹn ước lên ngực áo cho thằng Thành, có phải không Mộc Miên?' - Giọng nói thều thào, đứt quãng của người mẹ già trên giường bệnh vang lên giữa tiếng máy đo nhịp tim 'tít... tít...' dồn dập!

Bàn tay gầy guộc như cành củi khô, chằng chịt những vết kim tiêm bầm tím của bà run rẩy vỗ nhẹ lên mu bàn tay Hạ Mộc Miên. Từng giọt nước mắt đục ngầu ứa ra từ khóe mắt nhăn nheo, lăn dài trên gò má hốc hác của người phụ nữ đã đi qua cả một đời lam lũ.

Trong căn phòng cấp cứu ngột ngạt mùi thuốc sát trùng và tiếng oxy thở rít từng hồi, người mẹ già yếu ớt thì thầm kể lại sự thật kinh hoàng bị chôn giấu suốt một thập kỷ qua:

'Mười năm trước... Ngay trước ngày bác bước vào ca phẫu thuật tim sinh tử tại bệnh viện tỉnh... Bác nằm mê man nhưng tai bác vẫn nghe thấy tất cả... Chính mẹ con con bé Lâm Uyển Nhi đã chặn con lại ngoài hành lang phòng bệnh, ép con phải ký vào bản cam kết rời bỏ thằng Thành để đổi lấy năm trăm triệu tiền phẫu thuật cứu mạng bác...'.

Bà thở dốc từng cơn, đôi mắt già nua đỏ hoe nhìn sang Nam Thành đang quỳ sụp bên mép giường: 'Thành à... Con có biết không... Bác biết con bé Mộc Miên này đã cam tâm tình nguyện bán đi cả danh dự, tương lai và tuổi thanh xuân của nó để cứu lấy mạng sống già nua này của mẹ... Suốt mười năm nằm ở viện dưỡng lão, mẹ cất giữ chiếc áo đồng phục này dưới đáy gối... Mẹ không cho ai chạm vào... Mẹ chỉ sợ nếu mẹ chết đi mà chưa kịp nói cho con biết sự thật, mẹ sẽ phải mang theo món nợ ân tình nghìn cân này xuống suối vàng...'.

Bà siết chặt lấy tay Nam Thành, giọng nghẹn ngào như trăn trối: 'Thành ơi... Đời này con có thể thành công, có thể xây dựng hàng trăm tòa nhà chọc trời lộng lẫy... Nhưng nếu con đánh mất người con gái đã vì con mà hy sinh cả cuộc đời này... Thì con sẽ là kẻ thất bại thảm hại nhất trên cõi đời này! Con phải hứa với mẹ... Phải dùng cả tính mạng của con để bù đắp cho con bé suốt quãng đời còn lại!'.

Cố Nam Thành vùi mặt vào đôi bàn tay gầy guộc của mẹ và bàn tay nhỏ bé của Mộc Miên, những giọt nước mắt đàn ông nóng hổi tuôn rơi lã chã không cách nào kìm nén nổi. Lồng ngực anh quặn thắt từng cơn đau đớn tột cùng:

'Con xin lỗi mẹ... Con xin lỗi Mộc Miên... Con là kẻ mù quáng, là kẻ tồi tệ nhất trần đời! Mẹ ơi con hứa... Con thề trước vong linh tổ tiên, con sẽ yêu thương, trân trọng và bảo vệ cô ấy bằng cả sinh mạng này cho đến hơi thở cuối cùng!'.

Như trút bỏ được gánh nặng nghìn cân đã đeo đẳng suốt mười năm dài đằng đẵng, người mẹ già khẽ mỉm cười thanh thản. Một nụ cười mãn nguyện và bình yên hiếm hoi nở trên môi bà sau bao năm tháng chống chọi với bệnh tật đày đọa.

Bà run rẩy nâng bàn tay nhỏ nhắn của Mộc Miên lên, nhẹ nhàng đặt vào lòng bàn tay ấm áp, rắn rỏi của Nam Thành, rồi từ từ khép đôi mi lại chìm vào giấc ngủ an lành.

Và rồi, một điều kỳ diệu của y học đã xảy ra ngay trước mắt mọi người! Những tiếng kêu dồn dập cảnh báo của máy monitor bỗng chốc dịu lại. Đường sóng điện tim chập chờn trên màn hình dần dần hồi phục biên độ, nhịp tim từ con số bốn mươi nguy kịch bỗng từ từ tăng lên năm mươi, sáu mươi rồi ổn định ở mức bảy mươi nhịp một phút! Huyết áp và nồng độ oxy trong máu cũng bắt đầu tăng trưởng trở lại một cách thần kỳ!

Vị bác sĩ trưởng khoa cùng ê-kíp cấp cứu từ bên ngoài hớt hải chạy vào kiểm tra. Sau khi xem xét các chỉ số sinh tồn trên máy móc, vị bác sĩ thở phào nhẹ nhõm, kinh ngạc thốt lên:

'Thật không thể tin nổi! Cơn co thắt động mạch vành cấp tính đã tự động giải tỏa! Bệnh nhân đã vượt qua cơn hiểm nghèo nhất một cách kỳ diệu! Nghị lực sống phi thường và sự an ủi tinh thần to lớn từ gia đình đã giúp bà ấy chiến thắng tử thần! Cậu Cố, mẹ của cậu đã thực sự qua khỏi cơn nguy kịch rồi!'.

Tin vui như một luồng ánh sáng ban mai xua tan đi toàn bộ u ám và tuyệt vọng trong phòng bệnh. Nam Thành và Mộc Miên ôm chặt lấy nhau, nước mắt tuôn rơi nhưng lần này là những giọt nước mắt của sự giải thoát và hạnh phúc tột cùng.

Đúng lúc ấy, cánh cửa phòng bệnh khẽ mở ra. Một bóng dáng người đàn ông lớn tuổi, mái tóc đã bạc phơ như cước, tay chống một cây gậy gỗ bước vào. Đó chính là thầy Hoàng - người thầy chủ nhiệm kính yêu của lớp mười hai A chuyên Toán năm xưa!

Thầy Hoàng nhìn thấy hai đứa học trò cưng của mình đang nắm chặt tay nhau bên giường bệnh, đôi mắt thầy rưng rưng xúc động. Thầy bước tới, mở chiếc cặp da sờn cũ, cẩn thận lấy ra một cuốn học bạ cùng một tập bài thi học sinh giỏi quốc gia năm xưa đặt vào tay Nam Thành:

'Nam Thành à, Mộc Miên à... Thầy vừa nghe tin mẹ em nhập viện nên vội vã bắt xe buýt từ trường cũ lên đây ngay... Hôm nay dọn dẹp phòng truyền thống trước ngày đập trường, thầy đã tìm thấy bài văn đạt giải nhất kỳ thi học sinh giỏi quốc gia năm ấy của Mộc Miên. Đề bài năm đó là: Hãy viết về một tấm gương vượt khó mà em khâm phục nhất...'.

Thầy Hoàng xúc động lau nước mắt, nghẹn ngào kể tiếp: 'Mười năm trước, Mộc Miên đã viết trọn vẹn mười hai trang giấy về hình ảnh người thiếu niên nghèo Cố Nam Thành kiên cường đạp xe dưới mưa, không bao giờ đầu hàng số phận. Cả hai đứa đều là niềm tự hào lớn nhất trong bốn mươi năm đứng trên bục giảng của đời thầy...'.

Thầy nhìn Mộc Miên với ánh mắt trìu mến vô bờ bến: 'Và Nam Thành à, có một điều này suốt mười năm qua thầy luôn giữ kín theo lời thỉnh cầu của Mộc Miên... Hàng năm, cứ vào đúng ngày Nhà giáo Việt Nam hai mươi tháng mười một, trường cũ luôn nhận được một lẵng hoa cẩm chướng trắng gửi ẩn danh từ miền biển phía Nam, kèm theo một lá thư ngắn hỏi thăm sức khỏe của thầy và hỏi thăm xem... cậu học trò Cố Nam Thành đã trở thành một kiến trúc sư thành đạt như ước mơ chưa... Dù ở bất cứ nơi đâu, trái tim con bé này chưa từng một giây phút nào rời xa em cả!'.

Người y tá trưởng gắn bó hơn mười năm tại viện dưỡng lão Ánh Dương - cô Mai - cũng bước vào phòng bệnh với một chiếc hộp gỗ nhỏ trên tay. Cô Mai xúc động nhìn Mộc Miên rồi quay sang nói với Nam Thành:

'Giám đốc Cố à... Có những điều suốt mười năm qua chúng tôi phải giữ bí mật theo di nguyện của cô Mộc Miên đây. Cứ mỗi độ giao mùa hay những đợt gió mùa đông bắc tràn về làm vết mổ tim của bác gái đau nhức, cô Mộc Miên dù ở tận miền biển xa xôi hàng trăm cây số cũng thức trắng đêm sao vàng hạ thổ từng vị thuốc nam gia truyền, tự tay đóng gói cẩn thận gửi bưu điện lên cho bác.

Trong mỗi gói thuốc gửi tới, luôn có một mẩu giấy nhỏ dặn dò bác uống đúng giờ, kèm theo những lời chúc bình an mộc mạc nhất. Bác gái thương cô bé này đến thắt ruột thắt gan. Nhiều đêm bác ngồi bên cửa sổ ôm chiếc áo đồng phục này mà khóc, chỉ mong ông trời cho bác sống đủ lâu để được nhìn thấy hai đứa con đoàn tụ dưới mái nhà ấm êm. Tình cảm sâu nặng của cô Mộc Miên dành cho gia đình cậu thực sự là một kỳ tích hiếm có trên cõi đời này!'.

Nam Thành nghe từng lời kể của cô y tá mà hai hàng nước mắt lại tuôn rơi như mưa. Anh siết chặt bàn tay nhỏ nhắn đầy những vết chai sần của Mộc Miên vào ngực mình, cảm nhận từng nhịp đập thổn thức của trái tim cô. Mười năm thanh xuân của một người con gái đẹp nhất đời người, cô đã dành trọn vẹn từng giọt máu, từng hơi thở để chở che cho mẹ anh và vun đắp cho tương lai của anh!

Những lời tâm sự từ đáy lòng của người thầy chủ nhiệm già như ngọn gió ấm áp thổi bùng lên ngọn lửa tình yêu thiêng liêng trong lòng Nam Thành. Anh ôm chặt lấy Mộc Miên vào lòng, hôn lên mái tóc thơm mùi sương gió của cô, tự hứa với lòng mình sẽ không bao giờ để cô phải chịu thêm bất kỳ một giọt nước mắt tủi hờn nào nữa.

Sáng hôm sau, cơn bão lớn đã tan hoàn toàn. Những tia nắng vàng ươm đầu tiên của một ngày mới rọi chiếu qua khung cửa sổ phòng bệnh, báo hiệu một khởi đầu tươi sáng. Tình trạng sức khỏe của người mẹ già đã ổn định hoàn toàn và được chuyển sang phòng dưỡng bệnh VIP.

Cố Nam Thành nắm chặt bàn tay nhỏ nhắn của Hạ Mộc Miên, cùng cô bước lên xe quay trở lại sân trường cấp ba cũ - nơi từng lưu giữ trọn vẹn những ký ức thanh xuân đẹp đẽ nhất của hai người trước khi ngôi trường được bàn giao để xây mới.

Sân trường buổi sớm mai vắng lặng và thanh bình đến lạ kỳ. Từng vạt nắng sớm xuyên qua kẽ lá rọi xuống mặt sân gạch rêu phong. Dưới bóng cây phượng vĩ cổ thụ đang rực cháy những chùm hoa đỏ thắm cuối mùa, Nam Thành dắt tay Mộc Miên bước lên tầng ba, tiến về phía dãy phòng học lớp mười hai A năm xưa.

Cánh cửa gỗ cọt kẹt mở ra. Khung cảnh quen thuộc vẫn còn nguyên vẹn trong ký ức: Những dãy bàn ghế gỗ mộc mạc, bục giảng phủ bụi phấn trắng, và chiếc bàn học ở góc cuối lớp nơi hai đứa từng ngồi chung suốt ba năm cấp ba.

Nam Thành đưa tay lau sạch lớp bụi trên mặt bàn gỗ. Và dưới ánh nắng ban mai rực rỡ, dòng chữ khắc bằng mũi compa năm mười bảy tuổi bỗng hiện ra rõ mồn một: 'Đợi tôi đỗ Đại học Kiến trúc, tôi sẽ xây cho cậu một ngôi nhà ngập tràn hoa hồng'. Mộc Miên đưa những ngón tay run rẩy sờ lên từng nét khắc sâu hoắm ấy, nước mắt lại trào ra trên khóe mi vì xúc động.

Rời khỏi bệnh viện trong ánh nắng ban mai rực rỡ, trên con đường đưa Mộc Miên trở lại trường xưa, Nam Thành khẽ cho xe chạy chậm lại qua con phố nhỏ rợp bóng bằng lăng tím. Anh dừng xe trước một quán chè hoa cúc và một tiệm sách cũ quen thuộc năm xưa - nơi hai đứa từng ngồi nép bên hiên tránh những cơn mưa rào mùa hạ bất chợt.

Bà cụ chủ tiệm sách già nua nay tóc đã bạc trắng như mây trời, đang ngồi lau bụi trên những kệ sách gỗ cũ. Nhìn thấy hai bóng hình quen thuộc bước vào, bà cụ nheo đôi mắt kèm nhèm nhìn một hồi lâu rồi bất ngờ run run thốt lên: 'Trời ơi... Có phải là hai đứa học trò trường chuyên năm nào hay ngồi đọc chung cuốn sách tích phân dưới mái hiên của bà không?

Mười năm rồi... Bà vẫn nhớ như in thằng bé nghèo hay nhịn ăn sáng mua cho cô bé chiếc kẹp tóc hoa cúc, còn cô bé thì tỉ mỉ ngồi khâu lại từng đường chỉ rách trên áo khoác cho bạn! Hai đứa tìm lại được nhau rồi đấy à? Phúc đức ba đời đấy các con ơi!'.

Lời nói mộc mạc của bà cụ tiệm sách làm Mộc Miên không kìm được xúc động, nép đầu vào bờ vai vững chãi của Nam Thành. Mười năm thời gian có thể làm mờ đi cảnh vật, làm bạc trắng mái tóc của con người, nhưng những ký ức ngọt ngào và ân tình sâu nặng thuở thiếu thời thì vẫn vẹn nguyên như những trang sách mới mở hôm nào.

Nam Thành khẽ mỉm cười, ánh mắt chan chứa sự dịu dàng vô bờ bến. Anh nắm lấy tay cô, dẫn cô bước ra phía sau khuôn viên trường - nơi có một ngọn đồi nhỏ nhìn thẳng ra dòng sông quê thơ mộng.

Tại nơi đó, một công trình nhà hát kính nghệ thuật nguy nga tráng lệ đang được gấp rút hoàn thiện những khâu cuối cùng. Nam Thành chỉ tay về phía tấm biển phối cảnh khổng lồ bằng đồng nguyên khối treo trước cổng công trình:

'Mộc Miên, đây là công trình tâm huyết nhất trong suốt mười năm sự nghiệp kiến trúc của anh. Toàn bộ thiết kế nhà hát kính này đều lấy cảm hứng từ đóa hoa dành dành trắng tinh khôi và chiếc áo đồng phục năm mười bảy tuổi của em. Em nhìn xem... Toàn bộ hệ thống cửa sổ vòm kính của khán phòng này đều được anh thiết kế mở rộng tối đa về hướng nam - nơi mười năm qua anh luôn ngóng chờ em trở về'.

Anh quay sang nhìn cô, giọng nói trầm ấm mà kiên định: 'Ngôi nhà hoa hồng mà năm mười bảy tuổi anh từng hứa với em... Hôm nay anh đã xây xong rồi! Anh đã mua lại toàn bộ khu đồi hoa này và đặt tên là Vườn Ước Mộc Miên, đứng tên sở hữu duy nhất của một mình em! Ở trung tâm nhà hát, anh đã xây một phòng tranh nghệ thuật rộng lớn nhất thành phố, để em có thể tiếp tục theo đuổi ước mơ hội họa mà mười năm trước em từng phải gác lại vì mưu sinh!'.

Mộc Miên ngỡ ngàng nhìn công trình tráng lệ trước mắt, hai bàn tay áp lên miệng vì quá đỗi xúc động. Cô không thể ngờ rằng, người thiếu niên nghèo năm xưa từng bị cuộc đời vùi dập, giờ đây đã thực sự biến mọi lời hứa ngây thơ của tuổi học trò thành một kỳ tích hiện hữu giữa đời thực!

Bước vào không gian nghệ thuật rộng lớn của Vườn Ước Mộc Miên, ánh mắt Mộc Miên choáng ngợp trước hàng chục bức tranh sơn dầu được Nam Thành treo trang trọng dọc theo hành lang ánh sáng. Đó không chỉ là những bức tranh do anh mua lại, mà là toàn bộ những bức phác thảo dang dở mà Mộc Miên từng vẽ trên những trang giấy tập học trò năm xưa!

Suốt mười năm bươn chải nơi đất khách, dù đói khổ cùng cực, Mộc Miên vẫn giữ thói quen vẽ tranh dưới ánh đèn dầu mỗi đêm. Những bức tranh vẽ bóng lưng chàng thiếu niên đạp xe dưới mưa, bức tranh vẽ giàn hoa giấy rực rỡ ngoài ban công lớp mười hai A, bức tranh vẽ ước mơ về một ngôi nhà kính ngập tràn hoa hồng... Tất cả đều được Nam Thành âm thầm tìm kiếm, chuộc lại từ những phòng tranh nhỏ và lồng khung gỗ mạ vàng trang trọng nhất.

Mỗi một bức tranh là một chứng nhân lịch sử cho mối tình khắc cốt ghi tâm của hai con người. Nam Thành đứng bên cạnh cô, nhẹ nhàng ôm lấy eo cô từ phía sau, hơi thở ấm áp phả vào vành tai cô: 'Mộc Miên... Từ nay về sau, em không cần phải vẽ tranh trong bóng tối nữa. Cả khu vườn ước này, cả cuộc đời này của anh, đều thuộc về em!'.

Và rồi, ngay tại trung tâm của Vườn Ước Mộc Miên, dưới cơn mưa cánh hoa phượng đỏ rơi lả tả theo làn gió sớm, người đàn ông quyền lực Cố Nam Thành bỗng từ từ quỳ một gối xuống nền cỏ xanh mướt.

Từ trong túi áo vest, anh trân trọng rút ra một chiếc hộp nhung đỏ thẫm. Bên trong chiếc hộp là một chiếc nhẫn kim cương tinh xảo hình cỏ bốn lá - được chế tác thủ công mô phỏng chính xác từng đường nét của chiếc mặt dây chuyền bạc năm mười bảy tuổi mà cô vẫn đeo trên cổ.

Nam Thành ngẩng đầu lên, ánh mắt đen láy sâu thẳm nhìn thẳng vào mắt Mộc Miên, cất lời cầu hôn chân thành từ tận đáy con tim:

'Hạ Mộc Miên... Mười năm trước tại góc sân trường này, anh từng là một cậu học trò nghèo hèn, không thể cho em một chiếc ô lành lặn dưới cơn mưa bão. Mười năm lỡ hẹn vừa qua là lỗi lầm lớn nhất của cuộc đời anh vì đã không đủ tinh tế để nhận ra sự hy sinh thầm lặng của em.

Nhưng từ ngày hôm nay trở đi, anh không muốn làm cậu bạn cùng bàn của em nữa... Anh muốn làm chồng của em, muốn làm chiếc ô vững chãi nhất che chắn cho em trước mọi giông bão của cuộc đời. Em có đồng ý cùng anh viết tiếp câu chuyện tình yêu dang dở năm mười bảy tuổi này, cùng anh đi hết quãng đời còn lại không?'.

Từng giọt nước mắt hạnh phúc vỡ òa trên khóe mi Mộc Miên. Mọi nỗi đắng cay, tủi nhục và cô đơn của mười năm bươn chải nơi đất khách quê người bỗng chốc tan biến sạch sẽ như bọt xà phòng dưới ánh nắng rực rỡ. Cô nghẹn ngào gật đầu, lao vào vòng tay rắn rỏi, ấm áp của Nam Thành:

'Em đồng ý! Cố Nam Thành... Em đồng ý cùng anh đi đến cuối cuộc đời!'.

Nam Thành đứng dậy, ôm trọn thân hình nhỏ nhắn của Mộc Miên vào lòng, nâng niu trao cho cô một nụ hôn sâu nồng nàn dưới cơn mưa cánh hoa phượng vĩ rơi bay lượn giữa bầu trời xanh biếc.

Những người bạn học cũ khóa mười hai A đứng từ xa vỗ tay reo hò chúc phúc, thầy chủ nhiệm Hoàng mỉm cười gật đầu mãn nguyện. Mười năm thanh xuân trôi qua có thể mang theo nhiều tiếc nuối và nước mắt chia ly, nhưng tình yêu chân thành, sự hy sinh cao cả và lòng thủy chung son sắt cuối cùng cũng đã chiến thắng thời gian, cập bến bờ hạnh phúc trọn vẹn nhất.

Trong phòng tranh của Vườn Ước Mộc Miên, Nam Thành nhẹ nhàng kéo tấm rèm nhung đỏ che phủ bức tranh sơn dầu lớn nhất ở vị trí danh dự. Trước mắt Mộc Miên là bức tranh tái hiện trọn vẹn buổi chiều mưa mười năm trước: Chàng thiếu niên mười bảy tuổi đạp chiếc xe phượng hoàng cà tàng, nghiêng chiếc ô rách che chở cho cô bạn cùng bàn, những hạt mưa lấp lánh phản chiếu ánh đèn đường ấm áp.

Phía dưới bức tranh, chiếc áo đồng phục trắng thêu chỉ đỏ năm xưa được lồng kính trang trọng, như một minh chứng bất tử cho lời hứa thanh xuân không bao giờ phai nhạt. Hai người nắm chặt tay nhau bước ra hiên trường ngập tràn ánh nắng ban mai, mỉm cười chào đón một tương lai rực rỡ và hạnh phúc trọn đời bên nhau."""
    part3_cta = """Nếu được quay trở lại năm 17 tuổi dưới mái trường xưa, bạn có dũng cảm thổ lộ tình cảm chân thành với người mình thầm thương trộm nhớ không? Hãy để lại tâm sự và kỷ niệm thanh xuân đáng nhớ nhất của bạn dưới phần bình luận nhé!"""

    return {
        "title": story_title,
        "genre": "ThanhXuân",
        "voice": "vi-VN-HoaiMyNeural",
        "hook": "'Nếu năm ấy cậu không đứng đợi dưới cơn mưa tầm tã suốt ba tiếng đồng hồ với chiếc áo đồng phục ướt sũng, có lẽ mười năm qua tôi đã không phải sống trong nỗi dằn vặt này!'...",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": f"{story_title} (Tập 1)",
                "hook": "'Nếu năm ấy cậu không đứng đợi dưới cơn mưa tầm tã suốt ba tiếng đồng hồ với chiếc áo đồng phục ướt sũng, có lẽ mười năm qua tôi đã không phải sống trong nỗi dằn vặt này!'...",
                "body": part1_body,
                "cliffhanger": part1_cliff,
                "call_to_action": "Bấm theo dõi ngay để đón xem Tập 2 phát sóng tối nay!",
                "full_text": f"{part1_body}\n\n{part1_cliff}"
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": f"{story_title} (Tập 2)",
                "hook": "'Nội dung chuyển khoản: Mỗi tháng gửi năm triệu đồng chu cấp viện phí điều trị cho mẹ Cố Nam Thành tại viện dưỡng lão Ánh Dương - Tên người gửi: Hạ Mộc Miên!' - Từng con chữ viết tay nắn nót bằng mực đỏ tươi...",
                "body": part2_body,
                "cliffhanger": part2_cliff,
                "call_to_action": "Đón xem Tập 3 - Đại Kết Cục phát sóng tối nay trên kênh!",
                "full_text": f"{part2_body}\n\n{part2_cliff}"
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": f"{story_title} (Tập 3)",
                "hook": "'Chiếc áo đồng phục này... mười năm trước là chính con đã tỉ mỉ thêu dòng chữ hẹn ước lên ngực áo cho thằng Thành, có phải không Mộc Miên?' - Giọng nói thều thào của người mẹ già...",
                "body": part3_body,
                "cliffhanger": "",
                "call_to_action": part3_cta,
                "full_text": f"{part3_body}\n\n{part3_cta}"
            }
        ]
    }
