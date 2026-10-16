# -*- coding: utf-8 -*-
"""
core/stories/life_drama.py
Truyện Audio Đời Sống / Gia Đình / Drama 30 Phút:
Bí Mật Dưới Nền Bếp: Tấm Di Chúc 10 Năm Của Người Cha Bị Đầu Độc
Chuẩn độ dài: 3 Tập x 1,520 - 1,550 từ (~4,600 từ / ~33 phút audio).
100% Không giới thiệu lý lịch ("Tôi là...", "Năm nay... tuổi").
Căng thẳng, đấu trí gia tộc, kịch tính nghẹt thở liên tục ở cả 3 tập.
"""

from typing import Dict, Any

def get_30min_life_drama_story(title: str = "") -> Dict[str, Any]:
    story_title = title if title and "hôn nhân" not in title.lower() and "quỷ khế" not in title.lower() and "căn phòng số 13" not in title.lower() else "Bí Mật Dưới Nền Bếp: Tấm Di Chúc 10 Năm Của Người Cha Bị Đầu Độc"
    
    part1_body = (
        "'Đập vỡ nền bếp này ra! Tao biết chắc chắn chiếc hộp di chúc của ông già đang giấu dưới lớp bê tông này!' - "
        "Tiếng búa tạ mười cân giáng 'RẦM' một nhát trời giáng xuống sàn gạch men phát ra tiếng nổ chát chúa xé toạc màn đêm tĩnh mịch của căn nhà cổ ba gian! "
        "Bụi vôi vữa và mảnh gạch vỡ bay tung tóe khắp gian bếp ẩm thấp ngột ngạt. "
        "Gương mặt người anh cả đỏ gay vì men rượu, đôi mắt vằn lên những tia máu hung tợn như một con thú săn mồi đang phát điên vì khối tài sản hai trăm tỷ đồng. "
        "Bên cạnh gã, người chị dâu khoác trên mình chiếc áo lông thú đắt tiền nhưng khuôn mặt lại méo mó, nanh ác, liên tục thúc giục: "
        "'Đập mạnh vào anh! Ngày mai là phiên tòa phân chia di sản rồi, nếu không tìm thấy bản di chúc gốc đó trước rạng sáng mai thì mảnh đất vàng mặt phố hai trăm tỷ này sẽ bị đứa con gái út mang đi đấu giá từ thiện mất!'. "
        "Hai gã bảo kê xăm trổ bặm trợn đứng chắn ngang ngưỡng cửa, tay cầm tuýp sắt sáng loáng đe dọa bẻ gãy tay bất kỳ ai dám can thiệp. "
        "Tôi cắn chặt môi đến rớm máu, hai tay siết chặt chiếc xẻng sắt chắn ngang trước chiếc giường tre ọp ẹp nơi người mẹ già bị tai biến nằm bất động. "
        "Mười năm trước, người cha già kính yêu của tôi bỗng nhiên đột tử sau một cơn đau quặn thắt ruột gan giữa đêm khuya. "
        "Cái chết bất thường của ông bị người anh cả cấu kết với vị bác sĩ trạm xá biến thành một cơn đột quỵ do tuổi già, để rồi chỉ đúng ba ngày sau đám tang, gã anh cả đã ngang nhiên chiếm đoạt toàn bộ sổ đỏ khu đầm tôm và biệt thự ven sông, đẩy hai mẹ con tôi xuống sống chui rúc trong gian bếp dột nát này. "
        "Cha tôi vốn là một lương y mẫu mực, cả đời cần lao gây dựng nên trang trại dược liệu quý rộng hơn một trăm hecta ven đồi. "
        "Thế nhưng người con trai trưởng mà ông từng tự hào gửi gắm kỳ vọng lại sa đọa vào các canh bạc trực tuyến xuyên biên giới, nợ nần chồng chất hàng chục tỷ đồng. "
        "Mười năm trời ròng rã, mẹ con tôi phải ăn cơm thừa canh cặn, ngày ngày nhìn đôi vợ chồng độc ác kia tiêu xài phung phí trên mồ hôi nước mắt của cha để lại. "
        "Người chị dâu thậm chí còn vừa chìa ra một tập hợp đồng giả mạo, ép tôi ký giấy chuyển nhượng quyền sử dụng đất và đe dọa sẽ tống mẹ tôi vào một trại tâm thần tư nhân hẻo lánh trên núi để độc chiếm toàn bộ căn nhà thờ tổ. "
        "Trên giường bệnh, người mẹ già run rẩy nắm lấy ngón tay tôi, ánh mắt bà hướng về phía chân cột bếp lim nơi cha từng bí mật khắc biểu tượng hoa sen chìm làm dấu hiệu. "
        "Thế nhưng cây kim trong bọc lâu ngày cũng phải lòi ra, mười năm cắn răng chịu đựng tủi nhục của tôi chính là để chờ đợi giây phút vạch trần tội ác tày trời này!\n\n"
        "Nhát búa thứ tư bổ xuống làm thủng một mảng bê tông lớn ngay sát chân cột bếp bằng gỗ lim. "
        "Dưới ánh đèn pin loang loáng, một lớp than củi và vôi bột dày ba mươi centimet hiện ra – cách thức bảo quản đồ vật gia truyền chống ẩm mốc của cha tôi từ thời kháng chiến. "
        "Người anh cả quẳng chiếc búa tạ sang một bên, lao bổ xuống hố đất điên cuồng cào bới như kẻ điên dại. "
        "Đầu ngón tay gã va phải một vật kim loại phát ra tiếng 'keng' đanh gọn. "
        "Đó là một chiếc hộp sắt tây bọc chì chống ẩm, bên ngoài bị rỉ sét đóng thành từng mảng dày cộp, được khóa chặt bằng một ổ khóa đồng cổ ba số. "
        "'Tìm thấy rồi! Tìm thấy bảo bối của ông già rồi!' - Người chị dâu nhảy cẫng lên mừng rỡ, hai mắt sáng quắc lên tia tham lam tột độ. "
        "Nhưng khi chiếc xà beng bẩy tung nắp hộp sắt, thứ rơi ra bên ngoài sàn gạch không phải là vàng ròng hay sổ đỏ ngân hàng như bọn họ hằng thèm khát. "
        "Bên trong chiếc hộp là một cuốn sổ tay bìa da màu nâu đã ố vàng theo năm tháng, một chiếc thẻ nhớ chuyên dụng chống nước, và rùng rợn hơn tất cả: một lọ thủy tinh nhỏ chứa thứ bột màu trắng đục dán nhãn niêm phong của nhà thuốc độc dược học cổ truyền! "
        "Kèm theo đó là cuốn nhật ký bệnh án ghi chép tỉ mỉ từng ngày của cha tôi bằng nét bút mực tím: "
        "'Ngày 10 tháng 7 năm 2016... Tay chân bắt đầu tê bại sau mỗi lần uống trà sen do con dâu pha... "
        "Ngày 20 tháng 7... Bác sĩ đầu ngành xét nghiệm máu phát hiện nồng độ thạch tín tích tụ... Tôi không ngờ đứa con trai mình dứt ruột đẻ ra lại có thể nhẫn tâm đến mức này... "
        "Ngày 28 tháng 7... Tôi đã bí mật sao lưu dữ liệu camera giấu kín vào chiếc thẻ nhớ này, và chôn giấu toàn bộ mẫu phẩm dưới nền bếp – nơi chỉ có con gái út Phương Thảo mới biết... "
        "Nếu tôi chết đột ngột, chiếc chìa khóa bạc đeo trên cổ con gái út chính là mật mã giải cứu danh dự gia tộc!'. "
        "Và trang cuối cùng là bức di thư viết bằng máu trước lúc lâm chung: "
        "'Gửi con gái út Phương Thảo... Nếu một ngày cha đột ngột ra đi vì trụy tim sau bữa ăn, con hãy dùng chiếc chìa khóa này mở ngăn kéo bàn thờ gia tiên... "
        "Kẻ ngày ngày bỏ thạch tín liều thấp vào ấm trà hoa cúc của cha... chính là đứa con trai trưởng bất hiếu mà cha từng yêu thương nhất!'.\n\n"
        "Không gian gian bếp bỗng chốc đông cứng lại như một hầm băng tử thần! "
        "Từng lời từng chữ trong bức di thư như một bản án tử hình xé toạc bộ mặt giả nhân giả nghĩa của hai kẻ thủ ác. "
        "Khuôn mặt người anh cả tái mét như một cái xác không hồn, bàn tay gã run rẩy đánh rơi lọ bột trắng xuống sàn nhà phát ra tiếng kêu khô khốc. "
        "Mười năm qua, gã luôn tự xưng là người con hiếu thảo trước họ hàng, nhưng thực chất chính gã và người đàn bà độc ác kia đã tẩm thạch tín vào thức ăn của cha ruột từng chút một để chiếm đoạt quyền thừa kế trước khi ông kịp sang tên tài sản cho tôi! "
        "Tôi nhìn chằm chằm vào hai kẻ sát nhân bằng ánh mắt căm hờn tột độ, giọng nói đanh thép xé toạc sự tĩnh mịch: "
        "'Trần Mạnh! Chị dâu! Hai người có còn là con người nữa không? Cha đã nuôi nấng anh ăn học thành tài, cho anh nhà cao cửa rộng, vậy mà hai người nỡ lòng nào hạ độc giết chết chính cha ruột của mình?'. "
        "Người chị dâu sau phút bàng hoàng bỗng lộ rõ bản chất ác quỷ, ánh mắt mụ ta lóe lên tia sát khí điên cuồng: "
        "'Mạnh! Đừng để nó sống sót rời khỏi căn nhà này! Nếu chuyện lọ thuốc độc này lọt ra ngoài, cả hai chúng ta sẽ phải dựa cột bắn! Giết nó đi! Chôn xác nó ngay dưới nền bếp này cùng với tấm di chúc!'.\n\n"
        "Người anh cả gầm lên một tiếng man dại, gã vồ lấy khẩu súng săn hai nòng tự chế giấu sau cánh cửa bếp, họng súng đen ngòm lạnh ngắt chĩa thẳng vào giữa trán tôi! "
        "Tiếng lên đạn 'cạch' một tiếng sắc lạnh vang lên giữa tiếng mưa rào bắt đầu đổ xuống mái tôn ẩm mốc. "
        "Trên chiếc giường tre, người mẹ già nhìn thấy họng súng chĩa vào con gái út thì cố gắng gượng dậy, đôi môi run rẩy phát ra những tiếng 'ú ớ' nghẹn ngào đau đớn, hai hàng nước mắt đục ngầu lăn dài trên gò má nhăn nheo. "
        "Gió mưa quất từng đợt lạnh buốt qua khe cửa sổ vỡ, ngọn đèn dầu lay lắt sắp tàn như chính mạng sống của hai mẹ con tôi giữa nanh vuốt của bầy quỷ dữ đội lốt người thân."
    )
    
    part1_cliff = (
        "Người anh cả siết nhẹ ngón tay vào cò súng, ánh mắt đỏ ngầu mất hết nhân tính gầm lên man rợ: "
        "'Mày đã nhìn thấy thứ không nên thấy! Đêm nay cái xác của mày sẽ bị chôn sống ngay dưới nền bếp này để vĩnh viễn không một ai có thể lật lại bản án mười năm trước!'."
    )
    
    part2_body = (
        "'Mày đã nhìn thấy thứ không nên thấy! Đêm nay cái xác của mày sẽ bị chôn sống ngay dưới nền bếp này để vĩnh viễn không một ai có thể lật lại bản án mười năm trước!' - "
        "Họng súng săn hai nòng đen ngòm dí sát vào trán tôi, mùi thuốc súng khen khét xộc thẳng vào mũi giữa tiếng sấm chớp đùng đoàng! "
        "Trong tích tắc quyết định giữa sự sống và cái chết, tôi không hề nao núng hay van xin lòng thương xót của kẻ đã mất hết tính người. "
        "Bằng sự nhanh nhạy của một cô gái quen lao động đồng áng, tôi giả vờ hoảng sợ lùi lại một bước, tay trái quờ trúng ấm nước sôi đang reo sùng sục trên bếp củi, hắt thẳng một gáo nước nóng bỏng vào mặt người anh cả! "
        "Kẻ thủ ác rú lên một tiếng thét đau đớn xé họng, hai tay ôm lấy khuôn mặt phỏng rát buông rơi khẩu súng săn xuống sàn nhà! "
        "Phát súng cướp cò nổ 'ĐOÀNG' một tiếng chát chúa, chùm đạn ghém bắn tung toé lên xà nhà làm ngói vỡ rơi lộp độp! "
        "Tận dụng khoảnh khắc hỗn loạn, tôi vớ lấy nắm bột ớt khô ném thẳng vào mắt mụ chị dâu đang lao tới cản đường, khiến mụ ta ngã dúi dụi ôm mắt gào khóc thảm thiết.\n\n"
        "Tôi nhanh như cắt chộp lấy chiếc hộp sắt bọc chì và chiếc thẻ nhớ chứa chứng cứ nhét vào ba lô chống nước. "
        "Không một giây do dự, tôi cõng người mẹ già bại liệt lên lưng, dùng chiếc khăn rằn buộc chặt mẹ vào ngực mình rồi đạp tung cánh cửa sau của gian bếp, lao thẳng vào màn mưa bão trắng trời! "
        "Bùn đất trơn trượt của con đường đê ven sông như muốn níu chặt lấy từng bước chân nặng trĩu của tôi. "
        "Phía sau lưng, ánh đèn pin vàng vọt quét loang loáng qua những bụi tre gai, kèm theo tiếng gầm rú của xe máy địa hình và tiếng con chó săn béc-giê hung dữ sủa inh ỏi: "
        "'Đuổi theo! Thả chó ra cắn chết nó! Nó cõng bà già không chạy xa được đâu! Kẻ nào cướp lại được chiếc hộp sắt tao thưởng nóng một tỷ đồng!'. "
        "Tiếng quát tháo của người anh cả cùng đám tay sai xã hội đen vang lên gắt gao từng hồi, khoảng cách giữa hai bên ngày càng thu hẹp chỉ còn chưa đầy năm mươi mét!\n\n"
        "Con chó săn béc-giê lao vút qua bờ ruộng ngập nước, nhe hàm răng sắc nhọn chồm lên định cắn vào bắp chân tôi! "
        "Tôi nhanh trí rút nắm rơm khô thủ sẵn trong túi áo, quẹt que diêm bùng cháy rồi ném thẳng vào mõm con thú dữ. "
        "Ngọn lửa bùng lên làm con chó săn hoảng loạn quay đầu tháo chạy trong tiếng rên ẳng ẳng. "
        "Ở khúc rẽ vào cống ngập nước, gã anh cả điều khiển chiếc xe bán tải lao thẳng tới định tông chết hai mẹ con tôi! "
        "Tôi ôm chặt mẹ trượt người xuống bờ đê dốc đứng phủ đầy bùn non, lách qua rãnh thoát nước hẹp nơi chiếc xe bán tải bị sa lầy bánh xe quay tít mù mịt khói đen. "
        "Chúng tôi phải băng qua chiếc cầu khỉ bằng tre bắc ngang qua con kênh thủy nông đang cuồn cuộn nước lũ. "
        "Từng nhịp cầu tre rung lên bần bật dưới sức gió gầm rú và sức nặng của hai mẹ con, chỉ cần sẩy chân một tấc là cả hai sẽ bị dòng nước xoáy cuốn phăng ra sông lớn. "
        "Phía sau lưng, ba chiếc xe máy của đám đàn em bật đèn pha quét loang loáng trên mặt nước. "
        "Tôi nín thở cõng mẹ trượt xuống vạt cỏ năng rậm rạp ven sông, ngâm mình dưới làn nước lạnh buốt cắt da cắt thịt, hai tay giữ chặt chiếc ba lô chứa tài liệu khô ráo trên đỉnh đầu. "
        "Tiếng bước chân bì bõm của những kẻ truy đuổi lướt qua cách chỗ chúng tôi nấp chưa đầy hai mét trong tiếng gió rít gào. "
        "Chờ cho đoàn người đi khuất về phía cầu cống, tôi cõng mẹ luồn vào căn lều canh vịt bỏ hoang ven đầm sen, xé vội chiếc bao tải gai quấn chặt lấy bàn chân tím tái của mẹ để chống rét. "
        "Dòng nước lũ lạnh buốt cắt da cắt thịt, rác rưởi và cành cây gai cứa vào bắp chân tôi tóe máu, nhưng tôi vẫn nghiến răng cõng mẹ đi từng bước vững chãi. "
        "Trên lưng tôi, người mẹ già vòng đôi tay run rẩy ôm chặt lấy cổ con gái, thì thào trong nước mắt: 'Thảo ơi... Bỏ mẹ lại đi con... Chạy một mình mới sống được con ơi... Mẹ sống thừa thãi mười năm nay rồi...'. "
        "Tôi cắn chặt môi đến bật máu, nước mắt hòa cùng nước mưa mặn chát: 'Không bao giờ! Dù có chết con cũng phải đưa mẹ ra khỏi đây! Con phải bắt những kẻ hại cha phải đền tội trước pháp luật!'. "
        "Lợi dụng địa hình bụi rậm ven đầm sen quen thuộc từ thuở ấu thơ, tôi luồn lách qua con lạch nhỏ ngập nước ngang hông, cõng mẹ bò qua rãnh thoát nước dẫn vào trạm y tế xã cũ đã bỏ hoang nhiều năm nằm trơ trọi giữa cánh đồng. "
        "Tôi đóng chặt cánh cửa gỗ mục nát, chèn chiếc giường sắt cũ chặn ngang cửa ra vào, đặt mẹ nằm an toàn vào góc phòng khuất gió, dùng chiếc chăn chiên cũ phủ lên sưởi ấm cho mẹ.\n\n"
        "Trong bóng tối le lói của chiếc đèn màn hình điện thoại, tôi cắm chiếc thẻ nhớ của cha vào cổng chuyển đổi kết nối với máy tính bảng cũ. "
        "Và cảnh tượng hiện ra trên màn hình khiến toàn bộ uất hận trong lòng tôi dâng trào tột độ: "
        "Đó là đoạn video trích xuất từ camera bí mật giấu trong hốc mắt tượng Phúc Lộc Thọ trên bàn thờ gia tiên cách đây mười năm! "
        "Hình ảnh đen trắng ghi lại rõ mồn một cảnh tượng vào lúc mười một giờ đêm ngày 15 tháng 8 năm 2016: "
        "Người chị dâu lén lút rút từ túi áo ra một lọ bột màu trắng, đổ trọn vào ấm trà hoa cúc của cha tôi, trong khi người anh cả đứng ngoài cửa canh chừng với ánh mắt lạnh tanh không một chút do dự! "
        "Sau đó là cảnh cha tôi ôm ngực quằn quại trong đau đớn, còn hai kẻ nghịch tử đứng trơ mắt nhìn cho đến khi hơi thở của ông tắt hẳn mới bắt đầu giả vờ gào khóc gọi người cấp cứu! "
        "Cuối video còn có đoạn ghi âm giọng nói run rẩy của cha tôi gửi lời từ biệt con gái út, căn dặn con phải sống lương thiện và bảo vệ mẹ già. "
        "Tôi lập tức kết nối dữ liệu mạng 4G chập chờn giữa cơn giông bão, tải toàn bộ tệp video và bản chụp nhật ký lên hệ thống lưu trữ đám mây của Viện Kiểm Sát Nhân Dân Tối Cao và gửi một bản sao lưu sang số điện thoại của Trưởng Công an huyện! "
        "Màn hình thông báo đồng bộ thành công một trăm phần trăm! Mẹ tôi khẽ mở mắt, bàn tay run rẩy siết nhẹ lấy ngón tay tôi như muốn truyền thêm sức mạnh kiên cường. "
        "Tội ác tày trời giết cha đoạt tài sản đã được lưu trữ vĩnh viễn trên không gian mạng, không một thế lực đen tối nào có thể xóa bỏ hay bưng bít được nữa!\n\n"
        "Thế nhưng chưa kịp để tôi thở phào nhẹ nhõm, tiếng rầm rầm kinh hoàng bỗng vang lên từ bên ngoài cánh cửa trạm y tế! "
        "Mùi xăng nồng nặc bốc lên sặc sụa qua các khe cửa gỗ ọp ẹp. "
        "Bên ngoài hiên, người chị dâu với khuôn mặt băng bó chằng chịt đang điên cuồng tưới từng can xăng năm lít lên vách gỗ, trên tay lăm lăm chiếc bật lửa ga rực sáng ánh lửa vàng ma quái: "
        "'Con khốn Phương Thảo! Mày trốn trong đó xem đoạn video thú vị lắm đúng không? "
        "Một mồi lửa đêm nay sẽ thiêu rụi cả trạm y tế này thành tro tàn! Cả mày, cả bà già liệt giường lẫn chiếc thẻ nhớ đó sẽ biến mất vĩnh viễn khỏi cõi đời này!'."
    )
    
    part2_cliff = (
        "Ngọn lửa bốc lên ngùn ngụt bén vào vách gỗ trạm xá, khói đen đặc quánh cuộn tròn tràn ngập căn phòng hẹp khiến hai mẹ con tôi sặc sụa nghẹt thở. "
        "Cánh cửa chính đã bị lửa bao vây hoàn toàn, trần nhà bắt đầu sụp xuống từng mảng than hồng rực lửa. "
        "Trong khoảnh khắc sinh tử ngàn cân treo sợi tóc, tiếng còi xe tuần tra của công an huyện bỗng rú vang xé toạc màn mưa đêm từ đầu làng!"
    )
    
    part3_body = (
        "'Một mồi lửa đêm nay sẽ thiêu rụi cả trạm y tế này thành tro tàn! Cả mày, cả bà già liệt giường lẫn chiếc thẻ nhớ đó sẽ biến mất vĩnh viễn khỏi cõi đời này!' - "
        "Tiếng cười the thé man dại của người chị dâu vang lên giữa biển lửa đỏ rực đang liếm láp từng thanh xà gồ gỗ mục nát của trạm xá bỏ hoang! "
        "Khói đen dày đặc cuộn trào mù mịt, nhiệt độ trong phòng tăng vọt khiến da thịt tôi bỏng rát, hai mắt cay xè không thể mở ra. "
        "Thế nhưng, kẻ thủ ác không ngờ rằng tôi đã chuẩn bị sẵn sàng cho tình huống xấu nhất! "
        "Ngay từ lúc bước vào trạm xá, tôi đã phát hiện một bình cứu hỏa bột dạng bọt tuyết còn nguyên chốt an toàn nằm sau cánh tủ thuốc cấp cứu. "
        "Tôi giật mạnh chốt sắt, ôm chặt vòi phun xịt một luồng bọt trắng cực mạnh thẳng vào tâm ngọn lửa đang bùng lên nơi khung cửa sổ phía sau phòng! "
        "Áp lực bọt tuyết lạnh ngắt dập tắt đám cháy trong tích tắc, mở ra một lối thoát hiểm an toàn dẫn ra con mương nhỏ ngập nước.\n\n"
        "Tôi cõng mẹ lao qua làn khói đen mịt mù nhảy xuống bờ mương. "
        "Đúng lúc ấy, người anh cả cầm chiếc rựa sắc lẹm từ góc tối lao bổ tới định chém gục hai mẹ con tôi để phi tang chứng cứ! "
        "'ĐỨNG IM! BUÔNG VŨ KHÍ XUỐNG!' - Tiếng quát đanh thép như sấm sét vang lên từ lực lượng cảnh sát hình sự huyện vừa ập tới! "
        "Hai chiến sĩ công an quật ngã gã anh cả xuống vũng bùn lầy, tước chiếc rựa sắc lẹm trên tay gã và bẻ quặt hai tay tra còng số tám sáng loáng. "
        "Người chị dâu đang cầm can xăng định bỏ trốn qua cánh đồng cũng bị lực lượng dân quân bao vây bắt sống tại trận trong tiếng gào khóc tuyệt vọng. "
        "Hóa ra khi trốn chạy qua đầm sen, tôi đã bấm gọi khẩn cấp cho đường dây nóng 113 và chia sẻ vị trí trực tiếp định vị GPS cho lực lượng công an xã! "
        "Chiếc xe cứu thương lập tức đưa mẹ tôi và tôi về bệnh viện đa khoa trung ương để cấp cứu ngạt khói và điều trị vết bỏng.\n\n"
        "Tám giờ sáng hôm sau, tại hội trường lớn của Tòa án Nhân dân tỉnh, phiên tòa xét xử tranh chấp quyền thừa kế di sản của cha tôi diễn ra trong sự theo dõi nghẹt thở của hàng trăm người dân và báo chí truyền thông. "
        "Họ hàng dòng tộc nội ngoại đều tề tựu đông đủ, ai nấy đều ngỡ ngàng khi nhìn thấy hai bị cáo Trần Mạnh và người vợ bị áp giải ra trước vành móng ngựa trong trang phục phạm nhân. "
        "Trước sự chứng kiến của Hội đồng xét xử và toàn thể dòng họ, tôi bước lên bục nhân chứng, giao nộp chiếc hộp sắt bọc chì, lọ bột thạch tín nguyên vẹn và chiếc thẻ nhớ lưu trữ video mười năm trước. "
        "Đặc biệt, vị bác sĩ trạm xá năm xưa – nay đã già yếu và dằn vặt lương tâm – cũng được triệu tập ra trước tòa. "
        "Ông ta quỳ sụp xuống thú nhận toàn bộ sự thật: Rằng chính vợ chồng Trần Mạnh đã đưa cho ông ta năm trăm triệu đồng để làm giả giấy chứng tử, ghi nguyên nhân chết là tai biến mạch máu não nhằm hợp thức hóa việc chôn cất vội vã trong vòng hai mươi bốn giờ! "
        "Chủ hiệu thuốc đông y thị trấn cũng mang sổ sách ghi chép mười năm trước ra đối chất, chứng minh người chị dâu đã nhiều lần giả mạo chữ ký mua thạch tín cô đặc với lý do diệt chuột đồng.\n\n"
        "Màn hình lớn của tòa án bật sáng: Đoạn video sắc nét ghi lại trọn vẹn cảnh hai kẻ bất hiếu đổ thuốc độc vào ấm trà của cha già được phát công khai trước công chúng! "
        "Luật sư bào chữa của bị cáo cố gắng bao biện rằng đoạn video có thể là sản phẩm dàn dựng kỹ thuật số, nhưng chuyên gia giám định tội phạm công nghệ cao đã trình bày chữ ký điện tử mã hóa SHA-256 nguyên bản từ thẻ nhớ, chứng minh tệp dữ liệu được tạo đúng vào đêm định mệnh năm 2016 và không hề qua bất kỳ chỉnh sửa nào! "
        "Cả phòng xử án ồ lên trong kinh hoàng và phẫn nộ tột độ! Những tiếng nguyền rủa, những giọt nước mắt xót xa của các bô lão trong họ rơi lã chã vì thương tiếc người cha quá cố đã phải chết oan uổng dưới tay chính đứa con ruột thịt mà ông hằng tin tưởng. "
        "Kết quả khai quật mẫu tóc và mẫu xương của cha tôi được Viện Khoa học Hình sự công bố: Hàm lượng thạch tín tích tụ vượt mức cho phép gấp hai mươi lần – hoàn toàn trùng khớp với loại độc dược chứa trong lọ thủy tinh giấu dưới nền bếp! "
        "Trước những bằng chứng thép không thể chối cãi, người anh cả sụp quỳ xuống sàn đá cẩm thạch của tòa án, run rẩy đập đầu thú tội trong tiếng khóc nấc nghẹn ngào hối hận muộn màng. "
        "Bản án thích đáng lập tức được tuyên: Hai kẻ thủ ác phải nhận mức án tù chung thân và hai mươi năm tù giam vì tội giết người có tổ chức và hủy hoại chứng cứ! "
        "Đồng thời, tòa án chính thức công bố bản di chúc hợp pháp mười năm trước của cha tôi: "
        "Toàn bộ khối tài sản hai trăm tỷ đồng bao gồm khu đầm tôm và các bất động sản giá trị đều được trao quyền thừa kế duy nhất cho tôi và mẹ tôi.\n\n"
        "Ngay sau khi bản án được tuyên, vị tộc trưởng tám mươi tuổi của dòng họ Trần run rẩy chống chiếc gậy đồng bước lên giữa phòng xử án. "
        "Ánh mắt cụ rực lên ngọn lửa căm phẫn, giáng mạnh đầu gậy xuống nền đá cẩm thạch phát ra tiếng 'chát' đanh thép: "
        "'Nghịch tử Trần Mạnh! Từ giây phút này trở đi, tên của mày và người đàn bà độc ác kia sẽ bị xóa bỏ vĩnh viễn khỏi gia phả dòng tộc họ Trần! "
        "Mày không xứng đáng mang họ của tổ tiên, không bao giờ được phép bước chân vào từ đường bái lạy hương hồn cha ông nữa!'. "
        "Cả phòng xử án đồng thanh vỗ tay tán đồng trước sự trừng phạt nghiêm khắc của dòng họ dành cho kẻ đại nghịch bất đạo.\n\n"
        "Thế nhưng ngay tại phiên tòa, tôi đã đưa ra một quyết định khiến tất cả mọi người có mặt đều phải cúi đầu thán phục: "
        "Tôi xin trích một trăm năm mươi tỷ đồng từ khối tài sản thừa kế để thành lập Quỹ Từ Thiện Y Tế mang tên người cha kính yêu, chuyên hỗ trợ chi phí điều trị và thuốc men miễn phí cho các bệnh nhân nghèo bị ung thư và tai biến trên khắp cả nước; năm mươi tỷ còn lại dùng để xây dựng một viện dưỡng lão khang trang tại quê nhà để chăm sóc những người già neo đơn không nơi nương tựa. "
        "Lời phát biểu của vị thẩm phán chủ tọa phiên tòa vang vọng khắp khán phòng: 'Đạo làm con, lấy chữ Hiếu làm đầu. Kẻ vì tiền tài mà đánh mất lương tri, sát hại đấng sinh thành, ắt phải chịu sự trừng phạt nghiêm khắc nhất của pháp luật và lương tâm cắn rứt suốt đời'. "
        "Khi chiếc xe lăn đưa mẹ tôi rời khỏi cổng tòa án dưới ánh nắng vàng rực rỡ của ngày mới, hàng trăm bà con chòm xóm đã đứng hai bên đường rạng rỡ tặng những đóa hoa sen trắng tinh khôi chúc mừng sự hồi sinh của gia đình tôi. "
        "Mẹ tôi mỉm cười thanh thản, hai dòng nước mắt hạnh phúc lăn dài trên gò má nhăn nheo, bàn tay ấm áp nắm chặt lấy tay tôi. "
        "Mười năm oan khuất cuối cùng đã được gột rửa sạch sẽ, linh hồn của cha nơi chín suối giờ đây đã có thể mỉm cười an nghỉ. "
        "Những gian nan thử thách đã tôi luyện cho tôi một ý chí sắt đá, và hơn hết là niềm tin bất diệt vào chân lý cuộc sống. "
        "Trên đời này, tiền tài danh vọng dù có chất cao như núi cũng không thể mua được tình mẫu tử, phụ tử thiêng liêng. "
        "Lòng tham vô đáy và sự bất hiếu sớm muộn cũng sẽ phải trả giá đắt trước luật pháp và luật nhân quả, chỉ có lòng hiếu thảo, sự chính trực và tình yêu thương chân thành mới là báu vật trường tồn vĩnh cửu với thời gian."
    )
    
    part3_cta = "Bạn có suy nghĩ gì về cái giá đắt mà những kẻ bất hiếu phải trả trong câu chuyện này? Hãy để lại bình luận và chia sẻ cảm nghĩ của bạn nhé!"
    
    return {
        "title": story_title,
        "hook": "'Đập vỡ nền bếp này ra! Tao biết chắc chắn chiếc hộp di chúc của ông già đang giấu dưới lớp bê tông này!' - Tiếng búa tạ giáng xuống chát chúa...",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": f"{story_title} (Tập 1 - Chiếc Hộp Sắt Dưới Nền Bếp)",
                "hook": "'Đập vỡ nền bếp này ra! Tao biết chắc chắn chiếc hộp di chúc của ông già đang giấu dưới lớp bê tông này!' - Tiếng búa tạ giáng xuống chát chúa...",
                "body": part1_body,
                "cliffhanger": part1_cliff,
                "call_to_action": "Bấm theo dõi ngay để không bỏ lỡ Tập 2 - Cuộc Trốn Chạy Giữa Mưa Bão!",
                "full_text": f"{part1_body}\n\n{part1_cliff}"
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": f"{story_title} (Tập 2 - Rượt Đuổi Đêm Bão & Đoạn Video Vạch Mặt)",
                "hook": "'Mày đã nhìn thấy thứ không nên thấy! Đêm nay cái xác của mày sẽ bị chôn sống ngay dưới nền bếp này!' - Họng súng săn hai nòng dí sát vào trán!...",
                "body": part2_body,
                "cliffhanger": part2_cliff,
                "call_to_action": "Đón xem Tập 3 - Đại Kết Cục Công Lý Trước Tòa Án tối nay!",
                "full_text": f"{part2_body}\n\n{part2_cliff}"
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": f"{story_title} (Tập 3 - Bản Án Chung Thân & Quỹ Từ Thiện 200 Tỷ)",
                "hook": "'Một mồi lửa đêm nay sẽ thiêu rụi cả trạm y tế này thành tro tàn! Cả mày và chiếc thẻ nhớ đó sẽ biến mất!' - Biển lửa đỏ rực bùng lên nghẹt thở!...",
                "body": part3_body,
                "cliffhanger": "",
                "call_to_action": part3_cta,
                "full_text": f"{part3_body}\n\n{part3_cta}"
            }
        ]
    }
