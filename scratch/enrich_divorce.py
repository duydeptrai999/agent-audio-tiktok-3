# -*- coding: utf-8 -*-
with open('core/stories/life_divorce.py', 'r', encoding='utf-8') as f:
    text = f.read()

part3_addition = """
Sau khi ký xong biên bản bàn giao, Hoàng Vĩnh Kỳ vẫn ngồi thẫn thờ như một pho tượng đá giữa căn phòng làm việc từng là niềm tự hào của gã. 

Đúng lúc đó, tiếng chuông điện thoại của gã lại một lần nữa reo vang inh ỏi. Lần này là số của ông Lâm – đối tác cung cấp gỗ lớn nhất của công ty suốt ba năm qua:

"Alo Kỳ hả? Tôi vừa nghe tin bên Cục Thuế phong tỏa tài khoản công ty cậu để thanh tra sáu hóa đơn khống phải không? Hợp đồng cung ứng vật tư đợt tới trị giá năm tỷ của bên tôi xin phép tạm dừng lại nhé. Làm ăn kiểu chụp giật, trốn thuế như cậu thì tôi không dám hợp tác nữa đâu. Chiều nay tôi sẽ cho nhân viên qua thu hồi toàn bộ số gỗ đã ký gửi!"

Hoàng Vĩnh Kỳ chưa kịp ú ớ thanh minh lấy một câu thì đầu dây bên kia đã dập máy một cái 'cụp'. 

Tiếp theo đó, điện thoại của gã liên tục rung lên bần bật bởi hàng chục tin nhắn từ các nhà thầu thi công, nhân viên kinh doanh xin nghỉ việc và chủ nợ đòi tiền thuê mặt bằng. 

Bấy giờ, gã mới thực sự thấm thía cái giá phải trả cho thói phông bạt, trơ tráo và phản bội. Khi người ta đứng trên đỉnh cao danh vọng, người ta thường ngộ nhận rằng hào quang đó là do một mình mình tạo ra, mà quên mất rằng nền móng vững chắc nhất chính là sự hy sinh thầm lặng của người phụ nữ bên cạnh. Một khi đã tự tay phá vỡ nền móng ấy, thì tòa lâu đài cát nguy nga đến mấy cũng sẽ sụp đổ tan tành chỉ sau một cơn sóng nhỏ!

Tôi bước xuống khu vực sảnh văn phòng công ty. Toàn bộ hai mươi nhân viên thiết kế và kỹ thuật đang tập trung đông đủ, ai nấy đều mang vẻ mặt lo âu trước những biến động vừa xảy ra.

Tôi đứng trước mặt mọi người, cất giọng ấm áp nhưng vô cùng kiên định:

"Chào toàn thể các bạn. Kể từ giờ phút này, tôi – Lê Thục Quyên – sẽ chính thức tiếp quản vị trí Giám đốc điều hành công ty. Toàn bộ các sai phạm tài chính cá nhân của ông Hoàng Vĩnh Kỳ sẽ được tách bạch hoàn toàn khỏi hoạt động chung của doanh nghiệp. Tôi cam kết với các bạn: Tiền lương, tiền thưởng và các dự án thiết kế đang thi công của chúng ta sẽ được bảo đảm thanh toán một trăm phần trăm, không thiếu một đồng và không chậm một ngày! Những ai đồng hành cùng công ty trong giai đoạn tái cấu trúc này sẽ được hưởng chính sách đãi ngộ xứng đáng nhất!"

Tiếng vỗ tay vang dội khắp văn phòng xua tan đi bầu không khí u ám bấy lâu nay. Từng ánh mắt của những người đồng nghiệp cũ nhìn tôi bằng sự kính trọng và tin tưởng tuyệt đối. Họ biết rõ ai mới là người thực sự có tâm và có tầm để dẫn dắt công ty này đi qua giông bão.
"""

target = "Nói xong, tôi dứt khoát quay lưng bước ra khỏi căn phòng."
replacement = part3_addition.strip() + "\n\n" + target
text = text.replace(target, replacement, 1)

with open('core/stories/life_divorce.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Enriched Part 3 in life_divorce.py successfully!")
