# -*- coding: utf-8 -*-
from pathlib import Path

# 1. Sửa romance_chualanh_masterpiece.py
f_cl = Path("core/stories/romance_chualanh_masterpiece.py")
txt_cl = f_cl.read_text(encoding="utf-8")

old_cl_hook = """    part1_full = \"\"\"'Nếu cô bước qua cánh cửa này, bóng tối trong căn phòng này sẽ nuốt chửng cả cuộc đời cô!' - Tiếng gầm thét giận dữ của chàng họa sĩ thiên tài Giang Duật Hành xé toạc màn đêm tĩnh mịch bên hồ sương mù!

Hộp màu nước kim loại bị ném mạnh va vào bậc thềm đá hoa cương, vỡ tung làm những vệt màu đen kịt bắn tung tóe lên tà váy trắng tinh khôi của nữ bác sĩ tâm lý An Hạ."""

new_cl_hook = """    part1_full = \"\"\"Hộp màu nước kim loại bị hất tung từ cánh cửa gỗ sồi đen, văng mạnh vào bậc thềm đá hoa cương làm những vệt màu đen kịt bắn tung tóe lên vạt áo bác sĩ tâm lý An Hạ!

Cánh cửa gỗ sồi nặng nề sập mạnh một tiếng RẦM, khóa chặt chàng họa sĩ ba mươi tuổi vào bóng tối u uất suốt ba năm qua."""

if old_cl_hook in txt_cl:
    txt_cl = txt_cl.replace(old_cl_hook, new_cl_hook)
    f_cl.write_text(txt_cl, encoding="utf-8")
    print("Fixed romance_chualanh_masterpiece.py hook successfully!")
else:
    print("Could not find old_cl_hook in romance_chualanh_masterpiece.py")

# 2. Bổ sung hàm get_thanh_xuan_full_narrative vào core/narrative_synthesizer.py
f_syn = Path("core/narrative_synthesizer.py")
txt_syn = f_syn.read_text(encoding="utf-8")

thanh_xuan_func = '''
def get_thanh_xuan_full_narrative(custom_title: str = "", voice: str = "vi-VN-HoaiMyNeural") -> Dict[str, Any]:
    title = custom_title or "Chiếc Thẻ Nhớ Trong Hộp Bút Màu Hồng: Vạch Mặt Hội Trưởng Học Sinh"
    
    p1 = """Cốc trà sữa trân châu vừa đổ trọn xuống vạt váy đồng phục trắng của tôi, bàn tay của hội trưởng học sinh Lâm Diễm đã vội vã giơ chiếc khăn ướt lên lau với vẻ mặt xót xa:
'Hạ Vy à, cậu lại bất cẩn thế rồi. Mau vào nhà vệ sinh thay váy đi, kẻo thầy giám thị nhìn thấy lại trừ điểm thi đua của lớp'.

Cả lớp nhìn tôi bằng ánh mắt chế giễu ngầm. Bố của Lâm Diễm là Chủ tịch Hội đồng Quản trị trường liên cấp này. Mọi người đều nghĩ tôi chỉ là đứa con gái nhà nghèo cam chịu, một kẻ nhận học bổng không dám mở miệng thanh minh.

Tôi không nhận chiếc khăn ướt. Tôi cúi người nhặt chiếc bút dạ quang màu hồng của cô ta rơi trên bục giảng.

Ngón tay tôi vặn nhẹ chuôi bút, rút ra một chiếc thẻ nhớ siêu nhỏ dính dưới ruột mực.

Tôi ngước mắt nhìn thẳng vào nụ cười giả tạo của cô ta:
'Lâm Diễm, thẻ nhớ này rơi ra từ bút của cậu chiều thứ sáu. Trong này... ghi lại cảnh cậu cùng nhóm bạn lẻn vào phòng hội đồng tráo đổi đề thi học kỳ'.

Nụ cười trên môi cô ta cứng đờ lại. Đôi mắt ả lóe lên một tia hoảng loạn:
'Cậu... đưa đây ngay!'.

Tôi lùi lại một bước, giơ chiếc điện thoại đã kết nối Bluetooth với hệ thống loa phát thanh giờ chào cờ toàn trường:
'Năm trăm học sinh bên dưới đang tập hợp rồi. Cậu có muốn cả trường cùng nghe đoạn ghi âm cậu bàn bạc việc hãm hại bạn học không?'."""

    p2 = """Lâm Diễm lao tới giật chiếc điện thoại, nhưng bàn tay của thầy hiệu phó đã đặt lên vai cô ta từ phía sau!

Cả sân trường năm trăm học sinh bỗng chốc im phăng phắc. Tiếng loa phát thanh vang lên rành rọt từng câu từng chữ về kế hoạch tráo đổi đề thi học kỳ của nhóm học sinh ưu tú.

Từng gương mặt trong hội đồng khen thưởng dần biến sắc. Người bố quyền lực của Lâm Diễm ngồi trên hàng ghế danh dự siết chặt tách trà đến mức các đầu ngón tay trắng bệch.

Lâm Diễm run rẩy lùi lại ba bước, ánh mắt kiêu ngạo thường ngày sụp đổ hoàn toàn trước ánh nhìn phán xét của bạn bè cùng lớp.

Vật chứng thẻ nhớ Micro-SD lập tức được chuyển giao cho ban thanh tra độc lập của Sở Giáo dục để giám định kỹ thuật số."""

    p3 = """Quyết định đình chỉ học tập một năm và tước toàn bộ danh hiệu thi đua của Lâm Diễm được dán công khai tại bảng tin trung tâm trường học.

Gia đình cô ta tìm mọi cách bưng bít thông tin, nhưng trước làn sóng phẫn nộ của phụ huynh và sự vào cuộc của cơ quan quản lý, trật tự công bằng đã được lập lại.

Tôi bước ra khỏi cổng trường trong ánh nắng ban mai rực rỡ của mùa hè. Chiếc thẻ nhớ đã hoàn thành sứ mệnh của nó, trả lại sự trong sạch cho bài thi thử và danh dự của tôi.

Công lý không phải là thứ để cầu xin hay ban phát. Công lý phải được bảo vệ bằng chính sự can đảm, bằng chứng cứ đanh thép và bản lĩnh tự chủ của mỗi con người!"""

    return {
        "title": title,
        "hook": "Cốc trà sữa trân châu vừa đổ trọn xuống vạt váy đồng phục trắng của tôi, bàn tay của hội trưởng học sinh Lâm Diễm đã vội vã giơ chiếc khăn ướt lên lau với vẻ mặt xót xa.",
        "genre": "THANH_XUAN",
        "voice": voice,
        "parts": [
            {
                "part_number": 1,
                "badge_label": "PHẦN 1",
                "title": "Tập 1: Chiếc Thẻ Nhớ Trong Bút Dạ Quang",
                "hook": "Cốc trà sữa trân châu vừa đổ trọn xuống vạt váy đồng phục trắng của tôi, bàn tay của hội trưởng học sinh Lâm Diễm đã vội vã giơ chiếc khăn ướt lên lau với vẻ mặt xót xa.",
                "body": p1,
                "cliffhanger": "Tôi giơ chiếc điện thoại kết nối Bluetooth với hệ thống loa phát thanh toàn trường: 'Năm trăm học sinh đang tập hợp... Cậu có muốn cả trường cùng nghe đoạn ghi âm này không?'...",
                "call_to_action": "Bình luận 1 nếu bạn ủng hộ việc vạch mặt bắt nạt học đường bằng công nghệ!",
                "full_text": p1
            },
            {
                "part_number": 2,
                "badge_label": "PHẦN 2",
                "title": "Tập 2: Phát Loa Toàn Trường Giờ Chào Cờ",
                "hook": "Tiếng loa phát thanh vang lên rành rọt từng câu từng chữ về kế hoạch tráo đổi đề thi học kỳ của nhóm học sinh ưu tú.",
                "body": p2,
                "cliffhanger": "Vật chứng thẻ nhớ Micro-SD lập tức được chuyển giao cho ban thanh tra độc lập của Sở Giáo dục để giám định kỹ thuật số.",
                "call_to_action": "Bạn nghĩ hội đồng trường có dám kỷ luật con gái của Chủ tịch không? Bình luận 1 là có, 2 là không!",
                "full_text": p2
            },
            {
                "part_number": 3,
                "badge_label": "PHẦN 3 / KẾT",
                "title": "Tập 3: Đại Kết Cục Công Lý Học Đường",
                "hook": "Quyết định đình chỉ học tập một năm và tước toàn bộ danh hiệu thi đua của Lâm Diễm được dán công khai tại bảng tin trung tâm.",
                "body": p3,
                "cliffhanger": "",
                "call_to_action": "Bạn đã từng chứng kiến cảnh bắt nạt học đường nào chưa? Chia sẻ câu chuyện của bạn dưới phần bình luận nhé!",
                "full_text": p3
            }
        ]
    }
'''

if "def get_thanh_xuan_full_narrative" not in txt_syn:
    # Chèn trước get_masterpiece_narrative
    target = "def get_masterpiece_narrative("
    txt_syn = txt_syn.replace(target, thanh_xuan_func + "\n\n" + target)

# Cập nhật dispatcher trong get_masterpiece_narrative
old_dispatch = '''    elif "CUNG_DAU" in g or "TRACH_DAU" in g or "NU_QUYEN" in g:
        return get_cung_dau_full_narrative(custom_title, chosen_voice)
    elif "CUU_ROI" in g or "CHUA_LANH" in g or "THANH_XUAN" in g:
        return get_cuu_roi_full_narrative(custom_title, chosen_voice)'''

new_dispatch = '''    elif "CUNG_DAU" in g or "TRACH_DAU" in g or "NU_QUYEN" in g:
        return get_cung_dau_full_narrative(custom_title, chosen_voice)
    elif "THANH_XUAN" in g or "HOC_DUONG" in g:
        return get_thanh_xuan_full_narrative(custom_title, chosen_voice)
    elif "CUU_ROI" in g or "CHUA_LANH" in g:
        return get_cuu_roi_full_narrative(custom_title, chosen_voice)'''

if old_dispatch in txt_syn:
    txt_syn = txt_syn.replace(old_dispatch, new_dispatch)
    print("Updated dispatcher for THANH_XUAN in core/narrative_synthesizer.py!")

f_syn.write_text(txt_syn, encoding="utf-8")
print("Updated core/narrative_synthesizer.py with get_thanh_xuan_full_narrative!")
