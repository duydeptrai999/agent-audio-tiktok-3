import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
file_path = ROOT_DIR / "core" / "stories" / "cycles_21_to_30_masterpieces.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define new code for Cycle 27, 28, 29
cycle_27_code = '''# ==============================================================================
# VÒNG 27: GIÀN KHOAN DẦU KHÍ BIỂN SÂU (Universe 22 - Võ Trọng, Nam Khánh)
# ==============================================================================
def get_story_cycle_27(title: str = "") -> Dict[str, Any]:
    t = title or "Áp Suất Giếng Dầu Tăng Đột Biến Ở Tầng Đáy: Giàn Trưởng Võ Trọng Khóa Cụm Van Ngăn Phun Trào Biển Sâu"

    p1 = """Cắc! Chốt an toàn van ngăn phun trào dưới đáy biển ba nghìn mét nhảy bật, kim đo áp suất giếng dầu vọt lên mười lăm nghìn PSI giữa lúc tâm bão cấp mười lăm đổ bộ.

Sàn giàn khoan Vạn Tượng rung bần bật trong tiếng sóng gầm xé toạc màn đêm buốt giá.
Kỹ sư khoan Nam Khánh túm chặt lan can thép, hét lớn qua tiếng gió rít buốt óc:
'Giàn trưởng Trọng... Giám sát Chu Bách đã tắt hệ thống cảnh báo khí mê-tan tầng đáy rồi!'.

Tôi không chần chừ. Tôi khoác vội áo phao phản quang, lao thẳng về phía cụm van thủy lực khẩn cấp:
'Chu Bách... Anh định chôn sống một trăm hai mươi công nhân trên giàn khoan này sao?'.

Giám sát Chu Bách đứng chắn trước tủ điều khiển trung tâm, tay cầm chiếc cờ lê nặng hai cân gằn giọng:
'Lô dầu này trị giá ba trăm tỷ... Cấm dừng mũi khoan!'.

Tôi bước tới giật phăng cần gạt thủy lực màu đỏ:
'Mạng sống con người là vô giá... Ba trăm tỷ của anh không mua nổi lương tâm thợ mỏ đâu!'."""

    p2 = """Chu Bách vung cờ lê lao tới toan đập vỡ màn hình cảm biến áp suất đáy biển.
Nam Khánh kịp thời lao người ôm chặt lấy hắn, quật ngã xuống sàn thép trơn trượt.

Tôi khóa chặt van xả áp suất khí, kích hoạt hệ thống xi-lanh thủy lực khẩn cấp nặng hai trăm tấn.
Tiếng còi báo động áp suất cao vang rền khắp các khoang ngủ công nhân:
'Tất cả đội thợ sơ tán về phía mũi giàn, kích hoạt bè cứu sinh!'.

Chu Bách gào thét tuyệt vọng dưới sàn cabin điều khiển:
'Dừng lại đi Võ Trọng... Mũi khoan gãy thì tập đoàn sẽ kiện cậu phá hoại tài sản!'.

Tôi nhìn kim đồng hồ đo áp suất đang hạ dần về vùng an toàn màu xanh lá:
'Hộp đen giàn khoan ghi lại toàn bộ thao tác gian lận của anh rồi!'."""

    p3 = """Cụm van ngăn phun trào nặng hai trăm tấn dưới đáy biển sập chốt an toàn, dập tắt nguy cơ nổ giếng dầu thảm khốc.
Cơn bão biển quét qua, mặt biển dần phẳng lặng dưới ánh bình minh rạng rỡ của vịnh dầu khí.

Chu Bách bị còng tay vào thanh giằng phòng kiểm soát, giao cho tàu cảnh sát biển tiếp quản.
Đoàn thanh tra an toàn hàng hải tuyên bố khen thưởng đặc biệt cho lòng dũng cảm của tổ thợ khoan giàn Vạn Tượng.

Nam Khánh đưa cho tôi chiếc mũ bảo hộ sạch bụi dầu, mỉm cười rạng rỡ:
'Giàn trưởng Trọng... Chúng ta đã bảo vệ trọn vẹn sự an toàn cho giàn khoan này!'.

Tôi ngắm nhìn ngọn đuốc khí rực sáng trên đỉnh tháp khoan giữa đại dương bao la:
'Lửa biển sâu vẫn sáng... Lương tri của người thợ mỏ vĩnh viễn không bao giờ lụi tàn!'."""

    res = {
        "title": t,
        "genre": "HANH_DONG",
        "voice": "vi-VN-NamMinhNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": "Tập 1: Áp Suất Giếng Dầu Mười Lăm Nghìn PSI",
                "hook": "Cắc! Chốt an toàn van ngăn phun trào dưới đáy biển ba nghìn mét nhảy bật, kim đo áp suất giếng dầu vọt lên mười lăm nghìn PSI giữa lúc tâm bão cấp mười lăm đổ bộ.",
                "body": p1,
                "cliffhanger": "Giàn trưởng Võ Trọng giật phăng cần gạt thủy lực màu đỏ... Đối đầu nghẹt thở giữa tâm bão biển!",
                "call_to_action": "Bấm theo dõi đón xem Tập 2: Màn khóa van thủy lực hai trăm tấn dưới đáy biển sâu!",
                "full_text": p1
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": "Tập 2: Khóa Cụm Van Thủy Lực Hai Trăm Tấn",
                "hook": "Chu Bách vung cờ lê lao tới toan đập vỡ màn hình cảm biến áp suất đáy biển.",
                "body": p2,
                "cliffhanger": "Kim đồng hồ áp suất hạ dần về vùng an toàn... Hộp đen giàn khoan khóa chặt chứng cứ!",
                "call_to_action": "Bấm theo dõi đón xem Tập 3: Đại thắng của lòng dũng cảm giữa đại dương!",
                "full_text": p2
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3",
                "title": "Tập 3: Bình Minh Rạng Rỡ Trên Giàn Khoan Biển Sâu",
                "hook": "Cụm van ngăn phun trào nặng hai trăm tấn dưới đáy biển sập chốt an toàn, dập tắt nguy cơ nổ giếng dầu.",
                "body": p3,
                "cliffhanger": "Lửa biển sâu vẫn sáng, lương tri của người thợ mỏ không bao giờ lụi tàn!",
                "call_to_action": "Thả tim nếu bạn khâm phục tinh thần quả cảm của những người thợ giàn khoan biển sâu!",
                "full_text": p3
            }
        ]
    }
    return validate_story_series(res)'''

cycle_28_code = '''# ==============================================================================
# VÒNG 28: KIẾN TRÚC ÂM HỌC NHÀ HÁT (Universe 23 - Thẩm Khải Minh, Uyển My)
# ==============================================================================
def get_story_cycle_28(title: str = "") -> Dict[str, Any]:
    t = title or "Tấm Gỗ Tiêu Âm Phong Cầm Bị Đục Lỗ Ngầm: Mũi Dò Tần Số Sóng Âm Vạch Trần Kẻ Phá Hoại Đêm Diễn"

    p1 = """'Cậu dám mang máy đo âm học quét sàn sân khấu sao?' - Nhạc trưởng Lâm Hạo giấu vội chiếc máy phát hạ âm mini vào túi áo vest trước giờ biểu diễn mở màn.

Hội trường nhà hát giao hưởng ba nghìn chỗ ngồi đang dần kín khán giả quốc tế.
Nghệ sĩ cello Uyển My ngồi ở cánh gà, hai tay run rẩy, lồng ngực đập dồn dập vì tức ngực khó thở.

Tôi cầm máy phân tích phổ âm thanh FFT, rọi đầu dò vào vách gỗ sồi tiêu âm phía sau đàn phong cầm:
'Thưa nhạc trưởng... Tần số mười tám héc này không phải do dàn nhạc tạo ra!'.

Lâm Hạo biến sắc, bước tới chắn ngang ống kính máy đo phổ âm:
'Đừng có vẽ chuyện kiếm cớ... Uyển My không biểu diễn được thì để học trò của tôi thế chỗ!'.

Tôi bấm nút phát loa kiểm âm định hướng, âm thanh cộng hưởng rung giật khiến mặt sàn gỗ rền vang:
'Hạ âm mười tám héc làm giãn nhịp tim nghệ sĩ... Anh gài bẫy hạ bệ My để chiếm vị trí độc tấu sao?'."""

    p2 = """Lâm Hạo toan giật lấy thiết bị đo âm thanh trên tay tôi nhưng trượt chân ngã vào hàng ghế gỗ.
Tôi dùng tua-vít chuyên dụng cạy tấm ốp gỗ tiêu âm số chín trên sân khấu vòm.

Một thiết bị phát sóng hạ âm cỡ ngón tay dán keo silicon lộ ra trước sự chứng kiến của ban giám đốc.
Uyển My hít sâu một hơi thở nhẹ nhõm, nhịp tim dần đập ổn định trở lại:
'Thầy Hạo... Em đã kính trọng thầy suốt mười năm qua, tại sao thầy lại dùng thủ đoạn bẩn thỉu này?'.

Lâm Hạo lúng túng biện minh trong hoảng loạn:
'Tôi... Tôi chỉ muốn thử thách tâm lý nghệ sĩ solist thôi mà!'.

Tôi bật màn hình điện thoại kết nối trực tiếp với máy chủ âm thanh trung tâm:
'Địa chỉ Bluetooth của máy phát hạ âm này vừa khớp với điện thoại của anh!'."""

    p3 = """Hội đồng nghệ thuật quốc tế quyết định đình chỉ vĩnh viễn tư cách chỉ huy của Lâm Hạo ngay trước buổi diễn.
Tấm ốp tiêu âm được hiệu chỉnh lại góc phản xạ âm học chuẩn xác nhất.

Uyển My bước lên bục sân khấu dưới ánh đèn spotlight lung linh, tiếng đàn cello vang lên thánh thót xao xuyến triệu con tim.
Khán phòng ba nghìn khán giả đứng dậy vỗ tay vang dội suốt năm phút chào đón màn trình diễn đỉnh cao.

Tôi đứng ở phòng điều khiển âm học trung tâm, mỉm cười nhìn người bạn đồng hành tỏa sáng kiêu hãnh:
'Âm thanh chân chính xuất phát từ trái tim... Thủ đoạn đen tối không bao giờ dập tắt được nghệ thuật!'.

Tiếng đàn dương cầm hòa quyện trong không gian tuyệt mỹ, đánh dấu cột mốc huy hoàng của nhà hát opera."""

    res = {
        "title": t,
        "genre": "THANH_XUAN",
        "voice": "vi-VN-HoaiMyNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": "Tập 1: Mũi Dò Tần Số Sóng Âm Mười Tám Héc",
                "hook": "'Cậu dám mang máy đo âm học quét sàn sân khấu sao?' - Nhạc trưởng Lâm Hạo giấu vội chiếc máy phát hạ âm mini vào túi áo vest trước giờ biểu diễn mở màn.",
                "body": p1,
                "cliffhanger": "Khải Minh bật loa kiểm âm định hướng... Âm mưu hạ bệ nghệ sĩ độc tấu bị vạch trần!",
                "call_to_action": "Bấm theo dõi đón xem Tập 2: Màn bóc trần thiết bị phát hạ âm giấu sau vách gỗ sồi!",
                "full_text": p1
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": "Tập 2: Thiết Bị Hạ Âm Sau Tấm Ốp Gỗ Tiêu Âm",
                "hook": "Lâm Hạo toan giật lấy thiết bị đo âm thanh trên tay tôi nhưng trượt chân ngã vào hàng ghế gỗ.",
                "body": p2,
                "cliffhanger": "Địa chỉ Bluetooth trùng khớp với máy chủ trung tâm... Nhạc trưởng hoảng loạn câm nín!",
                "call_to_action": "Bấm theo dõi đón xem Tập 3: Tiếng đàn cello thăng hoa rực rỡ trên sân khấu quốc tế!",
                "full_text": p2
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3",
                "title": "Tập 3: Tiếng Vỗ Tay Vang Dội Khán Phòng Ba Nghìn Người",
                "hook": "Hội đồng nghệ thuật quốc tế quyết định đình chỉ vĩnh viễn tư cách chỉ huy của Lâm Hạo.",
                "body": p3,
                "cliffhanger": "Âm thanh chân chính xuất phát từ trái tim, thủ đoạn đen tối không dập tắt được nghệ thuật!",
                "call_to_action": "Thả tim nếu bạn tin rằng tài năng chân chính luôn luôn tỏa sáng kiêu hãnh!",
                "full_text": p3
            }
        ]
    }
    return validate_story_series(res)'''

cycle_29_code = '''# ==============================================================================
# VÒNG 29: THỢ LẶN HANG NGẦM TÁM MƯƠI MÉT (Universe 21 - Lê Hoàng Phong, Tuấn Anh)
# ==============================================================================
def get_story_cycle_29(title: str = "") -> Dict[str, Any]:
    t = title or "Dây Dẫn Đường Hang Ngầm Đứt Ở Độ Sâu Tám Mươi Mét: Lê Hoàng Phong Khóa Van Heliox Cứu Sống Đồng Đội"

    p1 = """Phụt! Sợi dây dẫn đường hang ngầm bằng sợi kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen mù mịt lập tức nuốt chửng ánh đèn lặn của tôi trong hốc đá karst.

Đồng hồ đo áp suất bình khí thở Heliox tụt nhanh xuống mức nguy hiểm bốn mươi bar.
Trợ lý lặn Tuấn Anh hoảng loạn thở dồn dập, kéo giật van thở dự phòng bên hông tôi qua ống dẫn cao su.

Tôi giữ chặt tay cậu ấy, gõ nhịp đèn hiệu ba lần vào mặt kính lặn ra hiệu bình tĩnh:
'Không thở dốc... Giữ nhịp tim dưới một trăm, bám sát vách đá vôi!'.

Qua mặt nạ lặn toàn phần, tôi nhìn thấy bóng dáng Trưởng đoàn Trịnh Bá đang bơi nhanh về phía cửa hang thoát hiểm.
Trên tay hắn là chiếc kìm cắt cáp chuyên dụng dính sợi chỉ kevlar màu vàng chanh.
Hắn đã cố tình cắt đứt dây tiêu ngầm để độc chiếm bản đồ túi quặng titan dưới đáy vực ngập nước!"""

    p2 = """Nước hang ngầm cuộn xoáy đục ngầu, tầm nhìn giảm xuống dưới nửa mét buốt giá.
Tuấn Anh kiệt sức ngã quỵ vào vách đá ngầm, bình khí của cậu ấy rít lên tiếng còi báo động cạn khí.

Tôi tháo van xả khí phụ của bình Heliox ba trăm bar, chia đôi đầu thở khẩn cấp cho Tuấn Anh:
'Hít thở chậm theo tôi... Chúng ta lặn theo vệt phấn huỳnh quang tôi đã rạch trên đá!'.

Tôi bật đèn lặn tia cực tím quét dọc theo góc đá vôi karst sần sùi.
Những vệt sáng màu lục bảo hiện lên dẫn lối qua khe hẹp hiểm trở sâu hun hút.

Trịnh Bá quay lại nhìn thấy hai chùm sáng xanh rực rỡ bám sát sau lưng, khuôn mặt sau kính lặn lộ rõ vẻ kinh hoàng."""

    p3 = """Hai chúng tôi vượt qua cửa hang hẹp trồi lên mặt nước hồ ngầm an toàn trong tiếng reo hò của đội hậu cần.
Lực lượng kiểm định địa chất lập tức phong tỏa ca-nô khảo sát của Trịnh Bá.

Chiếc kìm cắt cáp dính sợi kevlar và bản ghi nhớ ăn cắp tọa độ túi quặng bị thu giữ làm vật chứng pháp lý.
Trịnh Bá bị tước thẻ lặn chuyên nghiệp vĩnh viễn và khởi tố về hành vi cố ý giết người.

Tuấn Anh tháo bình khí thở, bắt chặt tay tôi trong làn nước trong vắt của buổi sớm mai:
'Đội trưởng Phong... Nếu không có bản lĩnh thép của anh, tôi đã vĩnh viễn nằm lại đáy vực sâu!'.

Tôi nhìn mặt hồ ngọc bích bình yên dưới chân vách núi đá vôi hùng vĩ:
'Đáy vực sâu dù tối tăm... Ánh sáng của tình đồng đội và sự quả cảm sẽ luôn dẫn lối trở về!'."""

    res = {
        "title": t,
        "genre": "SINH_TON",
        "voice": "vi-VN-NamMinhNeural",
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": "Tập 1: Dây Dẫn Đường Kevlar Đứt Ở Độ Sâu Tám Mươi Mét",
                "hook": "Phụt! Sợi dây dẫn đường hang ngầm bằng sợi kevlar đứt toác ở độ sâu tám mươi mét, luồng bùn đen mù mịt lập tức nuốt chửng ánh đèn lặn của tôi trong hốc đá karst.",
                "body": p1,
                "cliffhanger": "Trưởng đoàn Trịnh Bá bơi trốn với chiếc kìm cắt cáp dính sợi kevlar... Bình khí chỉ còn bốn mươi bar!",
                "call_to_action": "Bấm theo dõi đón xem Tập 2: Màn cứu hộ bằng bình Heliox ba trăm bar và vệt sáng huỳnh quang!",
                "full_text": p1
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": "Tập 2: Vệt Phấn Huỳnh Quang Dưới Đáy Hang Karst",
                "hook": "Nước hang ngầm cuộn xoáy đục ngầu, tầm nhìn giảm xuống dưới nửa mét buốt giá.",
                "body": p2,
                "cliffhanger": "Hai chùm sáng xanh lục bảo rọi thẳng sau lưng kẻ phản bội... Trịnh Bá kinh hoàng chết lặng!",
                "call_to_action": "Bấm theo dõi đón xem Tập 3: Cuộc trồi lên mặt hồ an toàn và bản án đích đáng!",
                "full_text": p2
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3",
                "title": "Tập 3: Ánh Sáng Bình Yên Trên Mặt Hồ Ngọc Bích",
                "hook": "Hai chúng tôi vượt qua cửa hang hẹp trồi lên mặt nước hồ ngầm an toàn trong tiếng reo hò của đội hậu cần.",
                "body": p3,
                "cliffhanger": "Đáy vực sâu dù tối tăm, tình đồng đội và lòng quả cảm sẽ luôn dẫn lối trở về!",
                "call_to_action": "Thả tim nếu bạn ngưỡng mộ tinh thần bất khuất của những người thợ lặn hang ngầm thám hiểm!",
                "full_text": p3
            }
        ]
    }
    return validate_story_series(res)'''

import re

# Use regex to find where get_story_cycle_27 starts and where get_story_cycle_30 starts
pattern = r"(#\s*={5,}\s*\n#\s*VÒNG 27.*?\n)(def get_story_cycle_30)"
match = re.search(pattern, content, re.DOTALL)
if not match:
    print("Could not match pattern for Cycle 27-29!")
    sys.exit(1)

new_block = cycle_27_code + "\n\n" + cycle_28_code + "\n\n" + cycle_29_code + "\n\n# ==============================================================================\n# VÒNG 30: HÀO MÔN & THƯƠNG CHIẾN\n# ==============================================================================\n"
start_idx = match.start(1)
end_idx = match.start(2)

new_content = content[:start_idx] + new_block + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully replaced Cycle 27, 28, 29 in cycles_21_to_30_masterpieces.py!")
