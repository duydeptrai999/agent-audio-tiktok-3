import sys

with open('core/stories/cycles_21_to_30_masterpieces.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Target start and end lines for cycle 28
start_marker = "def get_story_cycle_28(title: str = \"\") -> Dict[str, Any]:"
end_marker = "    return validate_story_series(res)"

# Find start
idx_start = text.find(start_marker)
if idx_start == -1:
    print("Start marker not found")
    sys.exit(1)

# Find the next return validate_story_series(res) after idx_start
idx_end = text.find(end_marker, idx_start)
if idx_end == -1:
    print("End marker not found")
    sys.exit(1)
idx_end += len(end_marker)

new_func = """def get_story_cycle_28(title: str = "") -> Dict[str, Any]:
    t = title or "Bản Nhạc Cello Bị Cắt Dây: Đoạn Ghi Âm Trong Phòng Chờ Vạch Trần Kẻ Giả Mạo"

    p1 = \"\"\"'Cô tưởng chỉ cần cầm cây vĩ cầm này là có thể ngồi vào vị trí độc tấu danh giá đó sao?' - Giọng nói the thé cay nghiệt của đàn chị Phương Thảo vang lên sau cánh gà nhà hát thành phố, kèm theo tiếng kéo khóa hộp đàn đánh cạch một tiếng chát chúa.

Hội trường ba nghìn chỗ ngồi bên ngoài đã bắt đầu chật kín khán giả và giới mộ điệu. Bản hợp xướng mùa thu chuẩn bị bấm giờ khai mạc sau mười lăm phút nữa. Tôi bước vội vào góc phòng thay đồ, bàng hoàng nhìn thấy bốn dây đàn của cây cello gia bảo do ông nội để lại đã bị nới lỏng toàn bộ chốt hãm, một sợi dây la thậm chí còn bị khía một vết cứa ngầm sắc lẹm bằng dao rọc giấy.

Phương Thảo đứng khoanh tay dựa vào khung cửa sổ, khóe môi nhếch lên nụ cười giễu cợt đầy ác ý: 'Cây đàn hỏng rồi thì tự giác rút lui nhường suất độc tấu lại cho tôi đi. Đừng để chút nữa ra sân khấu đứt dây đàn giữa chừng làm trò cười cho cả ban giám khảo quốc tế!'.

Tôi không hề tỏ ra hoảng loạn hay rơi một giọt nước mắt nào như ả mong đợi. Tôi bình thản kéo ghế ngồi xuống, mở chiếc hộp phụ kiện lấy ra bộ dây dự phòng bằng thép cao cấp mà tôi luôn mang theo bên mình. Đôi tay tôi thoăn thoắt tra từng đầu dây vào chốt đàn, ngón tay miết căng chỉnh từng vòng quay chuẩn xác đến từng milimet.

Tôi ngước nhìn Phương Thảo, ánh mắt đanh thép và lạnh lùng: 'Chị Thảo, chị nghĩ phá hoại nhạc cụ của người khác là có thể nâng tầm ngón đàn thô kệch của chị lên sao?'.

Ả giật nảy mình, sắc mặt lập tức biến đổi: 'Cô... Cô nói bậy bạ gì đó? Tôi vào đây lấy đồ biểu diễn thôi, đàn của cô tự hỏng thì liên quan gì đến tôi!'.

Tôi rút chiếc điện thoại thông minh từ túi áo khoác đồng phục, bật đoạn video quay cận cảnh đang hiển thị trên màn hình: 'Camera giám sát của phòng phục trang không quay được góc khuất này, nhưng chiếc máy ghi hình góc rộng tôi đặt trên nóc tủ đã ghi lại trọn vẹn cảnh chị rút dao rọc giấy cứa dây đàn của tôi lúc mười tám giờ ba mươi phút!'."\"\"

    p2 = \"\"\"Sắc mặt Phương Thảo tái mét, bàn tay run rẩy toan lao tới giật lấy chiếc điện thoại trên tay tôi: 'Mày dám gài bẫy tao? Xóa ngay đoạn video đó đi, bằng không tao sẽ khiến mày không thể tốt nghiệp nổi ở học viện âm nhạc này!'.

Tôi nhanh nhẹn nghiêng người né tránh cú vồ của ả, cất điện thoại vào túi rồi khóa chặt dây kéo lại. Cùng lúc đó, cánh cửa phòng thay đồ bật mở, thầy hiệu trưởng viện âm nhạc và hai thành viên trong hội đồng giám khảo quốc tế bước vào.

Chứng kiến bộ dạng lấm lét của Phương Thảo cùng chiếc dao rọc giấy rơi leng keng trên sàn nhà, thầy hiệu trưởng nghiêm giọng: 'Có chuyện gì ồn ào ở đây trước giờ biểu diễn vậy?'.

Tôi bình tĩnh cúi chào ban giám khảo, đặt cây đàn cello đã được thay dây căng chỉnh hoàn hảo lên giá đỡ, rồi trình chiếu lại đoạn video bằng chứng trước mặt hội đồng nghệ thuật: 'Thưa các thầy cô, thí sinh Phương Thảo đã cố tình phá hoại nhạc cụ biểu diễn của em nhằm độc chiếm vị trí solist trong đêm diễn mở màn hôm nay'.

Trước bằng chứng video sắc nét từng góc cạnh và vết cắt trên sợi dây đàn cũ, Phương Thảo run rẩy sụp xuống sàn nhà, nước mắt giàn giụa cầu xin sự tha thứ trong muộn màng. Hội đồng nghệ thuật lập tức ra quyết định đình chỉ tư cách tham gia đêm diễn và chuyển hồ sơ kỷ luật của Phương Thảo sang hội đồng nhà trường xử lý."\"\"

    p3 = \"\"\"Tiếng chuông báo hiệu đêm diễn vang lên ba tiếng ngân dài, ánh đèn sân khấu vòm lung linh chiếu rọi khắp khán phòng ba nghìn người. 

Tôi ôm cây đàn cello bước ra bục biểu diễn trung tâm trong tiếng vỗ tay nồng nhiệt của khán giả. Đứng dưới ánh đèn rực rỡ, tôi nhắm mắt lại, hít một hơi thật sâu để tâm trí tĩnh lặng như mặt hồ mùa thu. Từng ngón tay tôi lướt nhẹ trên phím đàn, cây vĩ kéo lên những thanh âm trầm bổng, thánh thót và tràn đầy nội lực, xao xuyến triệu con tim người nghe.

Giai điệu bản concerto vang lên hào hùng rồi lắng đọng sâu lắng, dẫn dắt người nghe đi qua từng cung bậc cảm xúc của tình yêu và sự kiên cường vượt qua nghịch cảnh. Khi nốt nhạc cuối cùng ngân vang rồi tan vào không gian tĩnh lặng, cả hội trường ba nghìn khán giả đồng loạt đứng dậy vỗ tay vang dội suốt năm phút không dứt.

Các vị giám khảo quốc tế bước lên sân khấu trao chiếc cúp danh dự cho màn trình diễn xuất sắc nhất mùa giải. Tôi mỉm cười nhìn lên trần vòm lung linh ánh sáng, trong lòng dâng trào niềm kiêu hãnh: Tài năng chân chính và sự lương thiện sẽ luôn vượt qua mọi âm mưu hèn hạ để tỏa sáng rực rỡ nhất!."\"\"

    res = {
        "title": t,
        "genre": "THANH_XUAN",
        "voice": "vi-VN-HoaiMyNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": "Tập 1: Chiếc Cello Bị Khía Vết Dao Rọc Giấy",
                "hook": "'Cô tưởng chỉ cần cầm cây vĩ cầm này là có thể ngồi vào vị trí độc tấu danh giá đó sao?' - Giọng nói the thé cay nghiệt của đàn chị Phương Thảo vang lên sau cánh gà nhà hát.",
                "body": p1,
                "cliffhanger": "Đoạn video bí mật trên nóc tủ hiển thị rõ nét... Kẻ phá hoại đàn cello tái mét mặt mày!",
                "call_to_action": "Bấm theo dõi đón xem Tập 2: Màn bóc trần kẻ thủ ác trước mặt hội đồng giám khảo quốc tế!",
                "full_text": p1
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": "Tập 2: Bằng Chứng Thép Trước Ban Giám Khảo",
                "hook": "Sắc mặt Phương Thảo tái mét, bàn tay run rẩy toan lao tới giật lấy chiếc điện thoại trên tay tôi.",
                "body": p2,
                "cliffhanger": "Hội đồng nghệ thuật đình chỉ tư cách biểu diễn... Kẻ giả mạo sụp đổ trong tủi nhục!",
                "call_to_action": "Bấm theo dõi đón xem Tập 3: Tiếng đàn cello thăng hoa rực rỡ trước ba nghìn khán giả!",
                "full_text": p2
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3",
                "title": "Tập 3: Chiếc Cúp Danh Dự Và Tràng Vỗ Tay Bất Tận",
                "hook": "Tiếng chuông báo hiệu đêm diễn vang lên ba tiếng ngân dài, ánh đèn sân khấu vòm lung linh chiếu rọi.",
                "body": p3,
                "cliffhanger": "Tài năng chân chính và sự lương thiện luôn luôn vượt qua nghịch cảnh để tỏa sáng kiêu hãnh!",
                "call_to_action": "Thả tim nếu bạn tin rằng người sống đàng hoàng sẽ luôn nhận được kết quả xứng đáng!",
                "full_text": p3
            }
        ]
    }
    return res"""

new_text = text[:idx_start] + new_func + text[idx_end:]
with open('core/stories/cycles_21_to_30_masterpieces.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully replaced get_story_cycle_28 in cycles_21_to_30_masterpieces.py")
