# -*- coding: utf-8 -*-
with open('core/stories/sa_dieu_tieng_long_masterpiece.py', 'r', encoding='utf-8') as f:
    text = f.read()

part2_extra = """
Lúc hai người cùng bước vào thang máy riêng để xuống tầng hầm lấy xe, bầu không khí bỗng nhiên trở nên im ắng lạ thường. 

Tôi đứng nép sát vào góc thang máy, mắt nhìn chăm chú vào những con số tầng đang nhảy lùi dần từ tầng sáu mươi xuống. Trong đầu tôi lúc này như một cái đài phát thanh bị nhiễu sóng, nhảy số liên tục không ngừng:

"Ủa sao thang máy đi chậm vậy trời? Đứng cạnh sếp áp lực ghê á, người gì đâu mà cao mét tám lăm, mùi nước hoa gỗ trầm hương thơm xỉu lên xỉu xuống. Mỗi tội mặt lúc nào cũng lạnh như băng, cứ như ai giật nợ tám tỷ không bằng. Cơ mà hồi nãy lúc sếp đưa khăn tay cho mình, ngón tay sếp chạm nhẹ vào tay mình một cái, ấm ghê ta... Ê bậy bạ nha Cẩm Chi! Mày chỉ là con bé thực tập thử việc quèn thôi, đừng có mà mơ mộng hão huyền trèo cao ngã đau nha con gái! Mục tiêu tối thượng của mày là kiếm đủ tiền mua một căn chung cư nhỏ và nuôi hai con mèo mướp, nhớ chưa!"

Tôi vừa tự nhắc nhở bản thân xong, thì bất ngờ thấy sếp Lục đứng bên cạnh khẽ hắng giọng một tiếng. Anh ấy đưa tay lên che miệng, bờ vai khẽ rung lên như đang cố nhịn cười. 

Rồi trước ánh mắt ngơ ngác của tôi, sếp bất ngờ thò tay vào túi áo khoác, lấy ra một chiếc hộp giấy nhỏ xinh xắn còn bốc khói nghi ngút, đưa thẳng về phía tôi:

"Cầm lấy đi. Bánh trứng nướng phô mai mới ra lò ở tiệm bánh đối diện. Ăn tạm lót dạ đi, rồi lát nữa đi ăn cơm sườn sau."

Mắt tôi sáng rực lên như vớ được vàng, vội vàng đón lấy chiếc hộp: "Ôi em cảm ơn Tổng giám đốc nhiều lắm ạ! Sếp đúng là vị cứu tinh của dạ dày em!"

Sếp Lục khẽ mỉm cười, ánh mắt nhìn tôi dịu dàng đến mức làm tim tôi đập thình thịch: "Ăn đi, đừng có vừa ăn vừa nói xấu tôi trong bụng nữa là được."

Câu nói đó làm tôi suýt chút nữa nghẹn miếng bánh trứng trong cổ họng! May mà cửa thang máy vừa lúc mở 'ting' một tiếng cứu nguy, tôi mới vội vàng xách túi chạy tót ra ngoài.
"""

target = 'Tôi vừa thầm nghĩ đến chữ "bật lửa Zippo mạ vàng", thì sếp Lục phía trước bỗng nhiên đứng phắt dậy!'
replacement = part2_extra.strip() + "\n\n" + target

text = text.replace(target, replacement, 1)

with open('core/stories/sa_dieu_tieng_long_masterpiece.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Part 2 enriched successfully!")
