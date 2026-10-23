# -*- coding: utf-8 -*-
from pathlib import Path

file_path = Path("core/stories/cycles_41_to_50_masterpieces.py")
content = file_path.read_text(encoding="utf-8")

# Cycle 42 Part 1:
content = content.replace(
    "'Chuyển hai trăm triệu vào ví điện tử này trong mười phút, nếu không clip của nó sẽ lên mạng!'.",
    "'Chuyển hai trăm triệu ngay! Mười phút nữa clip này sẽ lên mạng!'.",
)

# Cycle 42 Part 2:
content = content.replace(
    "'Chị Lam ơi! Em đang ở thư viện trường, tự nhiên tài khoản mạng xã hội của em bị mất quyền truy cập!'.",
    "'Chị Lam ơi! Em đang ở thư viện, tài khoản của em bị mất quyền rồi!'.",
)
content = content.replace(
    "'Mày nghĩ mày khôn hơn tao à? Ảnh nhạy cảm của em mày đã được đồng bộ lên máy chủ đám mây rồi!'.",
    "'Mày khôn hơn tao à? Ảnh của em mày đã lên máy chủ rồi!'.",
)
content = content.replace(
    "'Anh có mười phút để xóa sạch dữ liệu... Trước khi bảo vệ tòa nhà gõ cửa căn hộ ba mươi mốt!'.",
    "'Anh có mười phút để xóa dữ liệu! Bảo vệ đang gõ cửa căn hộ ba mươi mốt đấy!'.",
)

# Cycle 42 Part 3 (add dialogue and short sentences):
old_c42_p3 = """    p3 = \"\"\"Tiếng thở dốc của kẻ lừa đảo nghẹn lại trong cổ họng. Chiếc ly thủy tinh trên bàn làm việc của hắn rơi xuống sàn vỡ toang.

Hắn hoàn toàn không ngờ một chuyên viên đồ họa lại có thể lần ra địa chỉ vật lý chỉ qua một đường link thanh toán giả lập.
Trên màn hình giám sát mạng của tôi, thanh trạng thái hiển thị toàn bộ tệp ảnh rác đang bị xóa vội vã.

Mười lăm phút sau, hình ảnh từ camera giám sát hành lang chung cư gửi về máy tôi.
Lực lượng chức năng sở tại đã tiếp cận căn hộ, thu giữ ba bộ máy tính chuyên dùng để render video Deepfake tống tiền.

Em gái tôi chạy từ thư viện về nhà ôm chầm lấy tôi, hai mắt đỏ hoe.
Tôi xoa đầu con bé, rút thẻ nhớ điện thoại ra niêm phong vào phong bì làm bằng chứng bàn giao.

Bài học công nghệ đã được chứng minh: Dù AI có tinh vi đến đâu, sự thật vật lý và cái tâm trong sạch sẽ luôn đánh bại mọi ảo ảnh dối trá.\"\"\""""

new_c42_p3 = """    p3 = \"\"\"Tiếng thở dốc của kẻ lừa đảo nghẹn lại trong cổ họng. Chiếc ly thủy tinh trên bàn của hắn rơi xuống sàn vỡ toang.

Hắn vội vàng bấm phím xóa dữ liệu trên bàn phím.
Trên màn hình giám sát, thanh trạng thái hiển thị toàn bộ tệp ảnh rác đang biến mất.

Cơ quan điều tra lập tức tiếp cận căn hộ. Ba bộ máy tính render Deepfake bị ngắt nguồn điện và dán tem niêm phong.
Đội trưởng điều tra giơ chiếc còng số tám khóa chặt tay hắn, giọng đanh thép:
'Đừng cử động! Toàn bộ máy chủ của anh đã bị thu giữ!'.

Em gái chạy về nhà ôm chầm lấy tôi, hai mắt đỏ hoe:
'Em sợ quá chị ơi... Em tưởng mình mất hết danh dự rồi!'.
Tôi vỗ vai con bé mỉm cười:
'Không sao rồi. Sự thật luôn đánh bại mọi trò lừa bịp.'.

Tôi rút chiếc thẻ nhớ điện thoại, bỏ vào phong bì niêm phong làm bằng chứng bàn giao.
Bầu trời ngoài cửa sổ bừng sáng tia nắng ấm áp của ngày mới.\"\"\""""

content = content.replace(old_c42_p3, new_c42_p3)

# Cycle 44 Part 1:
content = content.replace(
    "'Thưa ông Chủ tịch... Tọa độ nông trường của ông trên giấy tờ thực chất là bãi đất ngập mặn bỏ hoang mười năm nay!'.",
    "'Thưa ông Chủ tịch! Tọa độ trang trại thực chất là bãi sình lầy mười năm nay!'.",
)

# Cycle 44 Part 2:
content = content.replace(
    "'Mỗi tháng các vị nhận được tiền lãi vài triệu, thực chất là tiền của người vào sau trả cho người vào trước!'.",
    "'Tiền lãi hàng tháng là tiền của người vào sau trả cho người vào trước!'.",
)

# Cycle 44 Part 3 (dialogue & sentence length):
old_c44_p3 = """    p3 = \"\"\"Tiếng còi xe của cơ quan quản lý thị trường và thanh tra tài chính đã vang lên dồn dập dưới sảnh khách sạn.

Chiếc cặp da của Lý Quốc Trí rơi tuột khỏi tay, hàng trăm bản hợp đồng đầu tư ảo bay tung tóe khắp sàn diễn.
Toàn bộ các tài khoản thanh toán đứng tên công ty ma đã bị phong tỏa khẩn cấp theo yêu cầu của đoàn thanh tra.

Mẹ tôi ôm chặt lấy tôi, nước mắt giàn giụa vì suýt nữa mất trắng khoản tiền dưỡng lão dành dụm cả đời.
Nhiều bác lớn tuổi bước tới bắt chặt tay tôi, nghẹn ngào nói lời cảm ơn vì đã cứu giúp gia đình họ khỏi thảm cảnh nợ nần.

Các tình nguyện viên hỗ trợ hoàn trả lại toàn bộ tiền mặt và sổ tiết kiệm cho các cụ ngay tại bàn tiếp đón.
Lý Quốc Trí cùng đám tay chân cúi gằm mặt bước lên xe chuyên dụng của cơ quan chức năng.

Tôi dắt mẹ bước ra sảnh lớn, đón ngọn gió chiều thu mát rượi thổi qua hàng cây xanh mát.
Tiền bạc kiếm được bằng mồ hôi nước mắt phải được bảo vệ bằng tri thức và sự tỉnh táo, không bao giờ có phép màu làm giàu dễ dàng.\"\"\""""

new_c44_p3 = """    p3 = \"\"\"Tiếng còi xe thanh tra tài chính vang lên dồn dập dưới sảnh khách sạn.

Chiếc cặp da của Lý Quốc Trí rơi tuột khỏi tay. Hàng trăm bản hợp đồng ảo bay tung tóe khắp sàn diễn.
Toàn bộ tài khoản của công ty ma bị phong tỏa khẩn cấp.

Mẹ ôm chặt lấy tôi, nước mắt giàn giụa:
'Mẹ suýt nữa mất trắng số tiền dưỡng lão rồi con ơi!'.
Tôi vỗ tay mẹ mỉm cười trấn an:
'Không sao đâu mẹ. Tiền cọc đã được bảo vệ an toàn rồi!'.

Nhiều bác lớn tuổi bước tới bắt chặt tay tôi:
'Cảm ơn cháu gái! Cháu đã cứu cả gia đình già này rồi!'.

Lý Quốc Trí cùng đám tay chân cúi đầu bước lên xe chuyên dụng.
Tôi dắt mẹ bước ra sảnh lớn, đón ngọn gió chiều thu mát rượi thổi qua hàng cây xanh mát.
Tri thức và sự tỉnh táo chính là lá chắn vững chắc nhất để bảo vệ thành quả lao động của đời người.\"\"\""""

content = content.replace(old_c44_p3, new_c44_p3)

# Cycle 47 Part 3 (dialogue):
content = content.replace(
    "'Nhờ sự nhạy bén và dũng cảm của anh mà chúng tôi triệt phá được đường dây nguy hiểm này!'.",
    "'Nhờ sự dũng cảm của anh mà đường dây này đã bị triệt phá!'.",
)

# Cycle 48 Part 3 (props & dialogue):
old_c48_p3 = """    p3 = \"\"\"Tiếng cạch vang lên, cửa chính của chiếc xe khách bung mở an toàn.

Hơn hai mươi lao động trẻ hoảng loạn nhưng trật tự ùa xuống mặt đường nhựa, chạy dạt về phía trạm kiểm soát giao thông cách đó năm trăm mét.
Tôi dùng dây dù trói chặt ba tên tội phạm vào vô lăng chiếc xe khách, ngắt cầu chì bơm nhiên liệu để ngăn chúng bỏ chạy.

Ánh đèn pha của chiếc xe tuần tra giao thông rọi sáng rực khúc cua đèo hiểm trở.
Lực lượng chức năng lập tức có mặt tiếp quản hiện trường, thu giữ ba bộ biển số xe giả cất giấu dưới cốp xe.

Cậu bé lúc nãy chạy lại ôm chặt lấy tôi, nước mắt giàn giụa: 'Cháu cảm ơn chú tài xế... Nếu không có chú chắc chúng cháu bị bán qua biên giới mất rồi!'.
Tôi vỗ vai cậu bé, đưa cho cậu chiếc bánh mì dự phòng trong túi áo: 'Về quê học hành cho đàng hoàng, đừng bao giờ tin vào việc nhẹ lương cao con nhé.'.

Tôi khoác chiếc ba lô bạc màu, bước tiếp trên con đường quốc lộ rạng rỡ ánh ban mai.
Lương tâm và trách nhiệm của người cầm lái trên mỗi chặng đường là giữ trọn sự bình an cho những số phận đồng hành.\"\"\""""

new_c48_p3 = """    p3 = \"\"\"Tiếng cạch vang lên, cửa sắt của chiếc xe khách bung mở an toàn.

Hơn hai mươi lao động trẻ ùa xuống mặt đường nhựa.
Tôi dùng chiếc cờ lê thép và sợi dây dù siết chặt ba tên tội phạm vào vô lăng xe.
Chiếc bình cứu hỏa mini được đặt ngay cửa xe để phòng thủ.

Ánh đèn pha rọi sáng rực khúc cua đèo hiểm trở.
Lực lượng tuần tra giao thông lập tức có mặt tiếp quản chiếc xe khách và ba bộ biển số giả dưới cốp xe.

Cậu bé chạy lại ôm lấy tôi, run rẩy:
'Cảm ơn chú! Chúng cháu suýt bị bán qua biên giới rồi!'.
Tôi đưa cho cậu chiếc bánh mì dự phòng:
'Về quê đi con! Đừng bao giờ tin vào việc nhẹ lương cao!'.

Tôi khoác chiếc ba lô bạc màu, bước tiếp trên con đường quốc lộ rạng rỡ ánh ban mai.
Lương tâm của người cầm lái là giữ trọn sự bình an cho mọi hành khách.\"\"\""""

content = content.replace(old_c48_p3, new_c48_p3)

# Cycle 49 Part 1:
content = content.replace(
    "'Bác sĩ kiểm tra giấy chứng nhận kiểm dịch nhanh hộ tôi. Chú mèo này bị gãy chân cần sang nước ngoài điều trị chuyên sâu!', hắn gõ ngón tay sốt ruột lên bàn inox.",
    "'Ký giấy kiểm dịch nhanh hộ tôi! Chú mèo này cần đi nước ngoài gấp!', hắn gõ ngón tay lên bàn inox.",
)
content = content.replace(
    "'Tôi kiểm tra dị vật bên dưới đệm lót để đảm bảo an toàn sinh học cho chuyến bay.'.",
    "'Tôi kiểm tra dị vật dưới đệm lót để đảm bảo an toàn.'.",
)

# Cycle 49 Part 3 (sentence length):
old_c49_p3 = """    p3 = \"\"\"Lực lượng chức năng có mặt tại phòng khám chỉ sau chưa đầy bảy phút.

Bạch Hạo bị tra tay vào còng số tám cùng toàn bộ tang vật chất cấm và chiếc lồng mèo bọc chì đặc chủng.
Kiểm tra nhanh điện thoại của đối tượng, cơ quan điều tra phát hiện cả một đường dây buôn lậu quốc tế chuyên lợi dụng hình ảnh yêu thương động vật để qua mặt hải quan sân bay.

Chú mèo mướp nhỏ được tôi lưu lại phòng khám chăm sóc, tắm rửa sạch sẽ mùi hóa chất độc hại.
Mai Lan bế chú mèo trên tay, đôi mắt lấp lánh niềm vui: 'May quá anh Trọng ơi, em bé này không bị bọn xấu lợi dụng nữa rồi!'.

Sáng hôm sau, phòng khám nhận được thư khen ngợi của chi cục kiểm dịch và lực lượng phòng chống tội phạm.
Tôi gắn chiếc vòng cổ nhỏ xinh khắc tên 'May Mắn' vào cổ chú mèo nhỏ, nhìn nó tung tăng đùa nghịch cuộn len dưới nắng sớm.

Tình yêu thương động vật phải xuất phát từ sự chân thành và thánh thiện, bất kỳ ai lấy danh nghĩa cứu trợ để làm điều phi pháp đều không thể thoát khỏi lưới trời lồng lộng.\"\"\""""

new_c49_p3 = """    p3 = \"\"\"Lực lượng chức năng có mặt tại phòng khám sau bảy phút.

Bạch Hạo bị tra tay vào còng số tám. Toàn bộ gói bột trắng và chiếc lồng mèo bọc chì bị niêm phong.
Chiếc điện thoại của đối tượng chứa toàn bộ tin nhắn liên lạc với đường dây buôn lậu quốc tế.
Chúng chuyên lợi dụng mác cứu trợ thú cưng để qua mắt kiểm tra an ninh sân bay.

Chú mèo mướp nhỏ được lưu lại phòng khám chăm sóc chu đáo.
Mai Lan bế chú mèo trên tay mỉm cười:
'May quá anh Trọng ơi! Bé mèo được an toàn rồi!'.
Tôi xoa đầu chú mèo nhỏ:
'Đúng vậy. Kẻ xấu đã phải trả giá rồi.'.

Tôi gắn chiếc vòng cổ nhỏ xinh khắc tên May Mắn vào cổ chú mèo.
Chú mèo tung tăng đùa nghịch cuộn len dưới nắng sớm ấm áp.
Lòng nhân ái chân chính sẽ luôn đẩy lùi mọi hành vi đen tối.\"\"\""""

content = content.replace(old_c49_p3, new_c49_p3)

# Cycle 50 Part 1:
content = content.replace(
    "'Kỹ sư Trần đo đạc xong chưa? Căn này chiều nay tôi trúng đấu giá rồi, đừng bới lông tìm vết làm gì!'.",
    "'Kỹ sư Trần đo xong chưa? Đừng bới lông tìm vết làm gì!'.",
)
content = content.replace(
    "'Tường nhà dày hơn bản vẽ bốn mươi phân. Tôi phải khoan lấy mẫu lõi bê tông để kiểm định chất lượng.'.",
    "'Tường dày hơn bản vẽ bốn mươi phân! Tôi phải khoan lấy mẫu lõi bê tông!'.",
)

# Cycle 50 Part 2:
content = content.replace(
    "'Mày không muốn sống nữa à? Chiều nay đấu giá xong căn này sẽ bị san phẳng làm trung tâm thương mại! Không có bê tông lõi nào hết!'.",
    "'Mày muốn chết à? Chiều nay căn này sẽ bị san phẳng! Không có khoan cắt gì hết!'.",
)
content = content.replace(
    "'Anh vội vã phá dỡ căn biệt thự này... Vì sợ người ta phát hiện thứ giấu sau bức tường thạch cao đúng không?', tôi nhìn thẳng vào mắt Mã Khắc.",
    "'Anh vội phá dỡ biệt thự này... Vì sợ lộ thứ giấu sau bức tường đúng không?', tôi nhìn thẳng vào mắt Mã Khắc.",
)
content = content.replace(
    "'Ông Mã Khắc... Phiên đấu giá chiều nay đã bị đình chỉ theo lệnh khẩn cấp của viện kiểm sát!', tiếng luật sư Quyên vang lên dõng dạc.",
    "'Ông Mã Khắc! Phiên đấu giá chiều nay đã bị đình chỉ khẩn cấp!', tiếng luật sư Quyên vang lên dõng dạc.",
)

# Cycle 50 Part 3:
old_c50_p3 = """    p3 = \"\"\"Chiếc két sắt mini được kéo ra ngoài ánh sáng trước sự chứng kiến của cơ quan điều tra và đại diện pháp lý.

Bên trong két sắt là tập di chúc viết tay nguyên bản của nữ doanh nhân cùng một chiếc máy ghi âm kỹ thuật số lưu giữ lời trăng trối.
Mười năm trước, chính Mã Khắc và đồng bọn đã lập hồ sơ ủy quyền giả mạo hòng chiếm đoạt toàn bộ cơ nghiệp của gia đình nạn nhân.
Mọi chứng cứ tội ác bị thời gian chôn giấu suốt một thập kỷ bỗng chốc sáng tỏ hoàn toàn.

Mã Khắc cùng hai gã bảo kê bị tra tay vào còng số tám, cúi gằm mặt áp giải xuống xe cảnh sát giữa sự chứng kiến của đông đảo người dân.
Toàn bộ khối tài sản biệt thự và cổ phần trị giá hàng trăm tỷ được tuyên trả lại cho người thừa kế hợp pháp.

Luật sư Thục Quyên bắt chặt tay tôi, đôi mắt đỏ hoe vì xúc động:
'Cảm ơn kỹ sư Trần... Sự trung thực và ngọn búa của anh đã trả lại công lý cho người đã khuất.'.

Tôi thu dọn dụng cụ đo đạc, bước ra khỏi cánh cổng sắt hoa văn cổ kính của ngôi biệt thự.
Ánh hoàng hôn vàng rực buông xuống những tán cây cổ thụ, thanh lọc không gian u tối suốt mười năm ròng.
Công lý có thể đến muộn, nhưng dưới ánh sáng của sự thật và lương tri, không tội ác nào có thể bị che giấu mãi mãi.\"\"\""""

new_c50_p3 = """    p3 = \"\"\"Chiếc két sắt mini bọc chì được kéo ra ngoài ánh sáng.

Bên trong két là tập di chúc viết tay nguyên bản cùng chiếc máy ghi âm lưu lời trăng trối.
Mười năm trước, Mã Khắc đã lập hồ sơ giả mạo chiếm đoạt cơ nghiệp nạn nhân.
Mọi chứng cứ tội ác suốt một thập kỷ bỗng chốc sáng tỏ hoàn toàn.

Mã Khắc cùng đồng bọn bị tra tay vào còng số tám.
Toàn bộ khối tài sản trăm tỷ được tuyên trả lại cho người thừa kế hợp pháp.

Luật sư Thục Quyên bắt chặt tay tôi, rưng rưng:
'Cảm ơn kỹ sư Trần! Anh đã trả lại công lý cho người đã khuất!'.
Tôi bắt tay luật sư mỉm cười:
'Đó là trách nhiệm của ngọn búa giám định.'.

Tôi thu dọn dụng cụ đo đạc, bước ra khỏi cánh cổng sắt cổ kính.
Ánh hoàng hôn buông xuống những tán cây cổ thụ, thanh lọc không gian u tối suốt mười năm ròng.
Sự thật và lương tri sẽ luôn chiến thắng mọi âm mưu gian xảo.\"\"\""""

content = content.replace(old_c50_p3, new_c50_p3)

file_path.write_text(content, encoding="utf-8")
print("Successfully polished all stories in core/stories/cycles_41_to_50_masterpieces.py!")
