# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/llm_client.py")
text = fpath.read_text(encoding="utf-8")

old_part = """    if "Trend Hunter" in system_prompt or "Săn Xu Hướng" in system_prompt:
        if any(k in prompt for k in ["SLEEP_CHILL", "NGON_TINH", "ROMANCE", "TAM_SU"]):
            return json.dumps({
                "topic_name": "Cưới Em Trước Cưng Chiều Em Sau: Bản Hợp Đồng Hôn Nhân 100 Tỷ",
                "summary": "Cô gái nghèo bị ép gả thay em gái cho vị tổng tài tàn tật lạnh lùng, nào ngờ sau đêm tân hôn lại được anh cưng chiều như bảo bối.",
                "key_facts": ["Hợp đồng hôn nhân giả 1 năm", "Tổng tài giả tàn tật để bắt kẻ phản bội", "Màn bảo vệ vợ trước giới hào môn"],
                "recommended_hook": "'Ký vào đây! Tôi cho cô 100 tỷ và sự tự do, cô chỉ là kẻ gả thay hèn kém thôi!' - Vị tổng tài tàn tật ném mạnh hợp đồng xuống bàn..."
            }, ensure_ascii=False)
        elif any(k in prompt.lower() for k in ["doraemon", "thời gian", "bảo bối", "cánh cửa"]):
            return json.dumps({
                "topic_name": "Kỳ Án Cỗ Máy Thời Gian: Lời Cảnh Báo Lúc Nửa Đêm Của 20 Năm Sau",
                "summary": "Khám phá ngăn bàn học của người ông phát minh, chiếc điện thoại cổ không dây bỗng reo vang với lời cảnh báo đẫm máu từ 20 năm sau.",
                "key_facts": ["Cỗ Máy Thời Gian trong ngăn bàn học", "Cánh Cửa Thần Kỳ dẫn vào phòng thí nghiệm lượng tử", "Màn đấu trí lột mặt kẻ mạo danh"],
                "recommended_hook": "'Nếu bước qua Cánh Cửa Thần Kỳ vào đúng 12 giờ đêm nay, bạn sẽ chứng kiến một vụ án mạng mà nạn nhân chính là bản thân mình 20 năm sau!'..."
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "topic_name": "Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Bí Ẩn Lúc Nửa Đêm Của Người Đã Mất",
                "summary": "Năm năm sau khi qua đời trong vụ tai nạn thảm khốc, chiếc điện thoại bàn đã cắt dây bỗng reo lên đúng 2 giờ sáng hé lộ bí mật kinh hoàng.",
                "key_facts": ["Chiếc điện thoại bàn bị cắt dây 5 năm trước", "Bức di thư đẫm máu giấu dưới gạch men căn phòng số 13", "Kẻ chủ mưu thực sự lại là người đồng đội thân cận nhất"],
                "recommended_hook": "'Sự thật chỉ có một, và hung thủ đang giấu mình sau một vỏ bọc không ai ngờ tới!' - Đúng 2 giờ sáng, chiếc điện thoại cắt dây 5 năm bỗng rung chuông..."
            }, ensure_ascii=False)"""

new_part = """    if "Trend Hunter" in system_prompt or "Săn Xu Hướng" in system_prompt:
        if any(k in prompt for k in ["SLEEP_CHILL", "NGON_TINH", "ROMANCE", "TAM_SU"]):
            return json.dumps({
                "topic_name": "Chiếc Khăn Voan Dưới Mép Hợp Đồng Hôn Nhân 100 Tỷ",
                "summary": "Mũi bút máy vừa chạm vào điều khoản phân chia tài sản, vết son lạ trên cổ tay áo của vị tổng tài tàn tật đã tố cáo ván cờ giăng bẫy ba năm.",
                "key_facts": ["Bản hợp đồng hôn nhân dính vết nước trà", "Chiếc xe lăn hợp kim giấu camera ghi hình 24/7", "Đòn phản công thu hồi 35% cổ phần"],
                "recommended_hook_3s": "Mũi bút máy vừa chạm vào bản hợp đồng một trăm tỷ, vết son đỏ mận trên cổ tay áo anh ta đã tố cáo tất cả."
            }, ensure_ascii=False)
        elif any(k in prompt.lower() for k in ["doraemon", "thời gian", "bảo bối", "cánh cửa"]):
            return json.dumps({
                "topic_name": "Mẩu Giấy Cháy Xém Trong Ngăn Bàn: Lời Cảnh Báo Lúc 2 Giờ Sáng",
                "summary": "Ngăn bàn học cũ bật mở với tiếng lách cách kim loại, mẩu giấy cháy xém để lại lời cảnh báo đẫm máu về vụ án mạng xảy ra sau đúng 48 giờ.",
                "key_facts": ["Mẩu giấy than cháy xém mép", "Chiếc đồng hồ con lắc ngược dòng thời gian", "Vết sẹo chữ X trên cánh tay hung thủ"],
                "recommended_hook_3s": "Mẩu giấy than cháy xém vừa rơi khỏi ngăn bàn học, dòng chữ đỏ tươi đã hiện lên dòng số đếm ngược bốn mươi tám giờ."
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "topic_name": "Bức Di Thư Dưới Gạch Men Căn Phòng Số 13",
                "summary": "Mũi dao cậy nắp viên gạch men phòng tắm bật mở, bức di thư viết bằng máu hé lộ bí mật về vụ án mạng năm năm trước của người bạn thân.",
                "key_facts": ["Viên gạch men số 13 bị lung lay", "Chiếc cúc áo đồng phục dính mẫu máu khô", "Hồ sơ thế chấp tài sản giả mạo"],
                "recommended_hook_3s": "Mũi dao vừa cậy bật góc viên gạch men số mười ba, bức di thư dính máu khô đã rơi tuột xuống lòng bàn tay tôi."
            }, ensure_ascii=False)"""

if old_part in text:
    text = text.replace(old_part, new_part)
    fpath.write_text(text, encoding="utf-8")
    print("Updated core/llm_client.py successfully!")
else:
    # Try normalizing line endings
    norm_text = text.replace("\r\n", "\n")
    norm_old = old_part.replace("\r\n", "\n")
    if norm_old in norm_text:
        norm_text = norm_text.replace(norm_old, new_part.replace("\r\n", "\n"))
        fpath.write_text(norm_text, encoding="utf-8")
        print("Updated core/llm_client.py with normalized line endings!")
    else:
        print("Could not find old_part in core/llm_client.py")
