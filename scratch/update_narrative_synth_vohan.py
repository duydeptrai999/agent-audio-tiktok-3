with open("core/narrative_synthesizer.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

# 1. Update get_vo_han_full_narrative to import mat_the_sinh_ton_masterpiece
target_vohan = """def get_vo_han_full_narrative(custom_title: str = "", voice: str = "vi-VN-NamMinhNeural") -> Dict[str, Any]:
    from core.stories.horror_chuyentau_masterpiece import get_horror_chuyentau_masterpiece_story
    title = custom_title or "Mạt Thế Kỷ Băng Hà: Tôi Tích Trữ 100 Tỷ Vật Tư Xây Pháo Đài Ấm Áp"
    orig = get_horror_chuyentau_masterpiece_story(title)"""

new_vohan = """def get_vo_han_full_narrative(custom_title: str = "", voice: str = "vi-VN-NamMinhNeural") -> Dict[str, Any]:
    from core.stories.mat_the_sinh_ton_masterpiece import get_mat_the_sinh_ton_masterpiece_story
    title = custom_title or "Trọng Sinh Về 30 Ngày Trước Tận Thế: Boong Ke Bất Khả Xâm Phạm"
    orig = get_mat_the_sinh_ton_masterpiece_story(title)"""

assert target_vohan in text, "target_vohan not found in narrative_synthesizer.py"
text = text.replace(target_vohan, new_vohan)

# 2. Update p2 in get_thanh_xuan_full_narrative to add punchy dialogue
target_tx_p2 = """    p2 = \"\"\"Lâm Diễm lao tới giật chiếc điện thoại, nhưng bàn tay của thầy hiệu phó đã đặt lên vai cô ta từ phía sau!

Cả sân trường năm trăm học sinh bỗng chốc im phăng phắc. Tiếng loa phát thanh vang lên rành rọt từng câu từng chữ về kế hoạch tráo đổi đề thi học kỳ của nhóm học sinh ưu tú.

Từng gương mặt trong hội đồng khen thưởng dần biến sắc. Người bố quyền lực của Lâm Diễm ngồi trên hàng ghế danh dự siết chặt tách trà đến mức các đầu ngón tay trắng bệch.

Lâm Diễm run rẩy lùi lại ba bước, ánh mắt kiêu ngạo thường ngày sụp đổ hoàn toàn trước ánh nhìn phán xét của bạn bè cùng lớp.

Vật chứng thẻ nhớ Micro-SD lập tức được chuyển giao cho ban thanh tra độc lập của Sở Giáo dục để giám định kỹ thuật số.\"\"\""""

new_tx_p2 = """    p2 = \"\"\"Lâm Diễm lao tới giật chiếc điện thoại, nhưng bàn tay của thầy hiệu phó đã đặt lên vai cô ta từ phía sau:
'Lâm Diễm! Trật tự ngay!'.

Cả sân trường năm trăm học sinh bỗng chốc im phăng phắc. Tiếng loa phát thanh vang lên rành rọt từng câu từng chữ về kế hoạch tráo đổi đề thi học kỳ của nhóm học sinh ưu tú.

Từng gương mặt trong hội đồng khen thưởng dần biến sắc. Người bố quyền lực của Lâm Diễm ngồi trên hàng ghế danh dự siết chặt tách trà đến mức các đầu ngón tay trắng bệch.

Lâm Diễm run rẩy lùi lại ba bước, đôi môi lắp bắp: 'Thầy ơi... Bạn ấy vu khống em!'.

Tôi bước lên bục danh dự, ngắt nhịp rành rọt: 'Vu khống sao? Đoạn băng này... Ghi rõ giọng của cậu!'.

Vật chứng thẻ nhớ Micro-SD lập tức được chuyển giao cho ban thanh tra độc lập của Sở Giáo dục để giám định kỹ thuật số.\"\"\""""

assert target_tx_p2 in text, "target_tx_p2 not found in narrative_synthesizer.py"
text = text.replace(target_tx_p2, new_tx_p2)

with open("core/narrative_synthesizer.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully updated get_vo_han_full_narrative and get_thanh_xuan_full_narrative!")
