# -*- coding: utf-8 -*-
"""
scripts/modernize_narrative_synthesizer.py
Đại tu core/narrative_synthesizer.py theo chuẩn Master Codex 8.0:
1. Xóa sạch sáo ngữ Trung Quốc (Lincoln bọc thép, Thụy Sĩ, Phó Trầm Uyên, Bắc Kinh, Earl Grey).
2. Nạp kho dữ liệu đời thực thuần Việt: Sổ đỏ, sao kê, căn hộ chung cư, khóa vân tay, camera an ninh, đối chất công an phường.
3. Độ dài chuẩn 30 phút tự nhiên (1.400 - 2.200 từ/tập, tổng 4.500 - 6.500 từ).
"""
import sys

TARGET_FILE = "core/narrative_synthesizer.py"

NEW_GENRE_ELEMENTS = '''GENRE_ELEMENTS = {
    "TRONG_SINH": {
        "subjects": [
            "Tôi lẳng lặng rút tờ di chúc có công chứng và sổ đỏ đứng tên mình đặt lên mặt bàn kính phòng khách.",
            "Người chồng cũ run rẩy đưa tay quệt mồ hôi trên trán, ánh mắt căm tức nhưng không thể cãi lại một lời.",
            "Cô em dâu hờ co rúm lại sau lưng mẹ chồng, chiếc túi xách hàng hiệu mua bằng tiền của tôi rơi xuống đất.",
            "Tôi đứng tựa lưng vào mép cửa sổ, ánh mắt điềm tĩnh nhìn thẳng vào bộ mặt bẽ bàng của những kẻ từng đục khoét tiền bạc của mình.",
            "Mẹ chồng ôm ngực thở dốc, vẻ mặt vênh váo thường ngày giờ biến thành sự hoảng loạn tột độ khi biết toàn bộ số tiết kiệm đã bị phong tỏa.",
            "Đại diện văn phòng luật sư mở tập hồ sơ sao kê tài khoản ngân hàng ba năm qua, từng khoản chi tiêu bất minh hiện rõ mồn một.",
            "Bác tổ trưởng dân phố và hai cán bộ công an phường đứng ngoài cửa, lập biên bản yêu cầu những người không có hộ khẩu rời khỏi căn hộ.",
            "Chiếc điện thoại trên bàn vẫn đang bật chế độ ghi âm và phát trực tiếp cho gia đình bên ngoại theo dõi toàn bộ sự việc.",
            "Người bạn trai từng phản bội tôi quỳ sụp xuống van xin được tha thứ, nhưng đáp lại chỉ là sự thờ ơ lạnh lùng của tôi.",
            "Bà hàng xóm tầng trên từng hùa theo nói xấu tôi nay vội vã lảng tránh ánh mắt, xấu hổ kéo cửa phòng lại."
        ],
        "atmospheres": [
            "Cơn mưa rào chiều hạ hắt từng vệt nước dài lên ô cửa kính ban công tầng mười lăm, mang theo hơi gió mát lạnh xua tan đi sự ngột ngạt.",
            "Ánh đèn vàng dịu trong phòng khách rọi xuống mặt bàn trà gỗ sồi, nơi đặt bản hợp đồng đã hoàn tất thủ tục phân chia tài sản.",
            "Không gian trong căn hộ bỗng chốc im phăng phắc, chỉ còn nghe thấy tiếng kim đồng hồ treo tường nhích từng giây chậm rãi.",
            "Mùi cà phê phin đậm đà thơm ngát lan tỏa khắp gian bếp nhỏ, tạo cảm giác thư thái của một cuộc đời hoàn toàn tự do.",
            "Tiếng còi xe tấp nập dưới ngã tư đường phố vọng lên nhè nhẹ, nhắc nhở tôi rằng cuộc sống ngoài kia vẫn đang chuyển mình rực rỡ.",
            "Những giọt nước mắt ấm ức năm xưa nay đã khô cạn, nhường chỗ cho ánh mắt kiên định của một người phụ nữ tự làm chủ vận mệnh.",
            "Không khí ngột ngạt của những màn đấu đá nhỏ nhen trong gia đình chồng cũ giờ đây đã vĩnh viễn bị bỏ lại sau lưng.",
            "Gương mặt tôi phản chiếu trong tấm gương lớn nơi lối vào nhà: Rạng rỡ, tự tin, không còn vương chút u sầu nào của quá khứ.",
            "Tiếng bước chân dứt khoát trên sàn gỗ gõ nhịp đều đặn, báo hiệu từng bước đi vững chắc trên con đường mới độc lập tài chính.",
            "Ánh nắng ban mai rực rỡ tràn ngập khung cửa sổ, báo hiệu một khởi đầu mới tinh khôi và ngập tràn hy vọng."
        ],
        "psychologies": [
            "Công lý đời thực luôn được định đoạt bằng giấy trắng mực đen và sự minh bạch về tài chính, chứ không phải bằng nước mắt ăn vạ.",
            "Một người phụ nữ tự chủ kinh tế và có lòng tự trọng sẽ không bao giờ để bất kỳ ai giẫm đạp lên phẩm giá của mình.",
            "Sự phản bội của những người từng gọi là gia đình là vết sẹo đau đớn, nhưng đó cũng là động lực lớn nhất để thức tỉnh.",
            "Lòng tốt không đi kèm sự tỉnh táo chỉ là mảnh đất màu mỡ cho những kẻ tham lam trục lợi.",
            "Khi bạn dám buông bỏ một mối quan hệ độc hại, cả thế giới tươi đẹp phía trước sẽ tự khắc mở ra chào đón bạn.",
            "Người sống giả tạo và mượn danh nghĩa tình thân để bóc lột người khác sớm muộn cũng sẽ tự tay phá nát tương lai của chính mình.",
            "Sự trả thù văn minh và đỉnh cao nhất không phải là cãi vã, mà là sống một cuộc đời rực rỡ, thành công hơn họ gấp vạn lần.",
            "Giá trị của một con người nằm ở nhân cách và sự nỗ lực chân chính, chứ không thể dùng những trò phông bạt sống ảo để đánh tráo.",
            "Hạnh phúc không nằm ở miệng lưỡi thiên hạ hay sự công nhận của nhà chồng, mà nằm ở sự bình yên trong chính tâm hồn mình.",
            "Cuộc đời này công bằng lắm, kẻ gieo sự dối trá ắt sẽ phải gặt lấy sự bẽ bàng và cô độc khi tấm màn nhung hạ xuống."
        ],
        "actions": [
            "Toàn bộ tài sản hợp pháp đã được bảo vệ trọn vẹn trước pháp luật, khép lại chuỗi ngày nhẫn nhịn cam chịu vô nghĩa.",
            "Ván cờ đời người đã ngã ngũ, những kẻ toan tính đục khoét phải ôm gói hành lý rời đi trong sự nhục nhã ê chề.",
            "Tôi nhẹ nhàng bấm mã số đổi mật khẩu cửa ra vào, khép lại vĩnh viễn cánh cửa dẫn về những tháng ngày tăm tối.",
            "Tiếng bấm còi xe taxi dưới sân chung cư giục giã, họ phải tự mình đối mặt với thực tế khó khăn do chính thói tham lam tạo ra.",
            "Một cuộc sống mới hoàn toàn độc lập và tự do đã chính thức bắt đầu từ ngày hôm nay.",
            "Tôi mỉm cười ôm lấy con gái nhỏ vào lòng, thầm hứa sẽ cho con một môi trường sống lành mạnh và tràn đầy yêu thương.",
            "Sức mạnh của người phụ nữ hiện đại chính là sự tự tin bước đi trên đôi chân của mình mà không cần dựa dẫm vào bất kỳ ai.",
            "Những lời xì xào bàn tán của họ hàng nhà chồng cũ dần tắt lịm trước sự thật rõ ràng không thể chối cãi.",
            "Một tách trà nóng bên khung cửa sổ chiều mưa, tâm hồn thanh thản ngắm nhìn phố phường lung linh ánh đèn.",
            "Và câu chuyện về sự thức tỉnh này sẽ là lời nhắc nhở sâu sắc cho bất kỳ ai đang phải nhẫn nhịn trong một cuộc hôn nhân độc hại!"
        ]
    },
    "ME_CHONG": {
        "subjects": [
            "Tôi bình thản nhấp một ngụm nước ấm, đưa mắt nhìn mẹ chồng đang ngồi vắt chân trên ghế sofa chỉ trích tiền ăn từng bữa.",
            "Bà Mai run rẩy khi nhìn thấy bản sao kê ngân hàng in dày cộp ba mươi trang liệt kê từng khoản tiền tôi gửi về quê sửa nhà.",
            "Chồng tôi ngồi gục đầu xuống bàn ăn, bàn tay bối rối không dám ngẩng lên nhìn thẳng vào mắt vợ.",
            "Cô em chồng vừa mới hôm qua còn đòi mượn xe máy SH của tôi đi hẹn hò, nay lén lút dọn đồ đạc để trốn tránh trách nhiệm.",
            "Đứa con nhỏ của tôi đang ngủ say trong phòng ngủ, tiếng thở đều đặn của con càng thôi thúc tôi phải bảo vệ quyền lợi của hai mẹ con.",
            "Vị luật sư tư vấn hôn nhân bước vào phòng khách, lịch sự đưa ra bản thỏa thuận phân chia tài sản độc lập trước hôn nhân.",
            "Bác tổ trưởng dân phố gật đầu xác nhận: Căn hộ này hoàn toàn thuộc quyền sở hữu riêng của tôi từ trước khi cưới.",
            "Bố mẹ đẻ tôi từ quê lên, không một lời to tiếng cãi vã, chỉ lặng lẽ đứng cạnh làm điểm tựa vững chãi cho con gái.",
            "Mấy người họ hàng nhà chồng từng sang ăn chực nay thấy tình hình căng thẳng liền viện cớ bận việc vội vã ra về.",
            "Anh thợ sửa khóa vừa lắp xong chiếc khóa thông minh vân tay mới, phát ra tiếng tít tít báo hiệu hoàn tất cài đặt."
        ],
        "atmospheres": [
            "Gió chiều luồn qua khe cửa ban công làm bay nhẹ tà rèm trắng, mang theo hơi thở trong lành của một buổi chiều tà yên ả.",
            "Ánh nắng hoàng hôn vàng óng chiếu xiên qua khung kính phòng khách, soi rõ từng biểu cảm bẽ bàng trên khuôn mặt nhà chồng.",
            "Không khí trong căn nhà từng ngột ngạt vì những lời soi mói nay bỗng chốc trở nên nhẹ nhõm và thoáng đãng lạ thường.",
            "Mùi cơm canh nóng hổi mẹ đẻ tôi vừa nấu trong bếp tỏa ra ấm áp, hương vị thân thương của gia đình thực sự.",
            "Tiếng mưa rơi tí tách ngoài cửa sổ như đang gột rửa đi mọi muộn phiền và ấm ức tích tụ suốt bao nhiêu năm qua.",
            "Căn phòng ngủ nhỏ xinh của hai mẹ con ngập tràn ánh sáng êm dịu, nơi bình yên nhất mà không ai có thể xâm phạm.",
            "Bầu không khí căng thẳng ban đầu dần nhường chỗ cho sự thanh thản khi mọi sự thật được phơi bày rõ ràng trước ánh sáng.",
            "Từng góc nhỏ trong căn nhà do chính bàn tay tôi gom góp mua sắm nay đã thực sự thuộc về sự tự do của riêng tôi.",
            "Tiếng xe cộ nhộn nhịp ngoài đại lộ hòa cùng tiếng nhạc piano nhẹ nhàng phát ra từ chiếc loa bluetooth góc phòng.",
            "Một buổi tối đầu tiên sau bao năm tháng tôi có thể đặt lưng xuống giường và có một giấc ngủ thật sâu, không âu lo phiền muộn."
        ],
        "psychologies": [
            "Nhẫn nhịn để giữ gìn hòa khí gia đình là đức tính tốt, nhưng nhẫn nhịn trước sự quá quắt và tham lam chỉ là sự nhu nhược.",
            "Lấy chồng không phải là để làm osin không công cho cả gia đình người khác, phụ nữ xứng đáng được tôn trọng và yêu thương.",
            "Đồng tiền do chính mồ hôi nước mắt mình làm ra thì phải biết cách giữ gìn, đừng để người khác nhân danh tình thân mà chiếm đoạt.",
            "Một người đàn ông không có chính kiến, chỉ biết mù quáng nghe lời mẹ mà hy sinh quyền lợi của vợ con thì không xứng đáng làm chỗ dựa.",
            "Sự thức tỉnh tuy muộn màng nhưng luôn là bước ngoặt cứu rỗi cả cuộc đời của người phụ nữ.",
            "Gia đình chồng tốt hay xấu thể hiện rõ nhất ở cách họ đối xử với con dâu lúc ốm đau và sau khi sinh nở.",
            "Biết ơn và hiếu thảo là đạo lý làm người, nhưng bao bọc cả những kẻ lười biếng ỷ lại thì chỉ tạo thêm gánh nặng cho bản thân.",
            "Khi bạn dám đứng lên bảo vệ chính mình, đối phương mới nhận ra bạn không phải là kẻ dễ dàng bị thao túng.",
            "Bình yên lớn nhất của đời người là tự chủ về tài chính và thanh thản trong lương tâm, không nợ nần ai bất cứ điều gì.",
            "Rời bỏ một cuộc hôn nhân độc hại không phải là thất bại, mà là sự dũng cảm để bắt đầu lại một cuộc đời xứng đáng hơn."
        ],
        "actions": [
            "Hợp đồng thuê nhà đã được thanh lý dứt khoát, toàn bộ đồ đạc của những kẻ ăn bám đã được thu dọn gọn gàng ngoài hành lang.",
            "Mẹ chồng tôi ôm mặt khóc lóc ăn vạ, nhưng những lời phân trần đầy lý lẽ của tôi đã khiến bà không thể tiếp tục diễn trò.",
            "Chồng tôi ký vào lá đơn ly hôn với đôi tay run rẩy, sự hối hận muộn màng hiện rõ trên khuôn mặt thất thần.",
            "Tôi bước ra ban công hít một hơi thật sâu, cảm nhận vị ngọt ngào của sự tự do đang lan tỏa trong từng nhịp thở.",
            "Cánh cửa căn hộ khép lại nhẹ nhàng với tiếng chốt khóa vân tay, ngăn cách toàn bộ sự ồn ào độc hại ở bên ngoài.",
            "Tôi nhẹ nhàng lau giọt nước mắt trên má con gái, từ nay hai mẹ con sẽ có một cuộc sống bình yên và hạnh phúc.",
            "Một cuộc gọi điện thoại cảm ơn gửi đến vị luật sư tận tâm đã giúp tôi bảo vệ toàn bộ quyền lợi hợp pháp.",
            "Bữa cơm gia đình ấm cúng chỉ có tôi, con gái và bố mẹ đẻ, không còn những ánh mắt soi mói hay những lời mỉa mai cay nghiệt.",
            "Những kẻ từng coi thường tôi nay chỉ biết nhìn theo bóng lưng tôi bước đi với sự tiếc nuối và xấu hổ khôn cùng.",
            "Và đây chính là màn đáp trả xứng đáng nhất: Một cuộc đời tự do, kiêu hãnh và ngập tràn hạnh phúc của người phụ nữ biết tự thương lấy mình!"
        ]
    }
}
'''

def main():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "GENRE_ELEMENTS = {"
    end_marker = "def get_thanh_xuan_full_narrative("
    
    idx_start = content.find(start_marker)
    idx_end = content.find(end_marker)
    
    if idx_start == -1 or idx_end == -1:
        print("Markers not found!")
        return

    # Replace old GENRE_ELEMENTS
    updated_content = content[:idx_start] + NEW_GENRE_ELEMENTS + "\n\n" + content[idx_end:]
    
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Successfully modernized {TARGET_FILE} to Master Codex 8.0!")

if __name__ == "__main__":
    main()
