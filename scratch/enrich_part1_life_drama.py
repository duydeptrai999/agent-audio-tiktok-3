# -*- coding: utf-8 -*-
with open('core/stories/life_drama.py', 'r', encoding='utf-8') as f:
    text = f.read()

part1_extra = """
Tôi vẫn nhớ như in buổi chiều mùa thu năm ngoái, trong những giây phút tỉnh táo hiếm hoi cuối cùng của cuộc đời, bố tôi đã run rẩy nắm chặt lấy bàn tay thô ráp đầy vết chai sạn của tôi. Đôi mắt người cha già ngấn lệ, từng giọt nước mắt đục ngầu lăn dài trên gò má hốc hác. Bố thều thào nói từng tiếng đứt quãng: "Hà ơi... bố có lỗi với con nhiều lắm... Bố nuông chiều thằng Tuấn quá đà để rồi biến nó thành kẻ hư hỏng, bất hiếu... Bố chỉ thương con gái bố phải chịu khổ cả một đời thanh xuân vì ông già tàn phế này... Căn nhà này là mồ hôi nước mắt của tổ tiên để lại, bố đã tính toán chu toàn cho con rồi... Con phải mạnh mẽ lên, đừng để ai bắt nạt con nhé con gái...".

Những lời dặn dò thiêng liêng ấy của bố như khắc sâu vào tâm khảm tôi. Nó chính là điểm tựa tinh thần vững chắc nhất, là ngọn lửa sưởi ấm tâm hồn tôi qua bao đêm đông giá rét. Người cha cả đời nghiêm nghị ấy trước lúc nhắm mắt xuôi tay đã thấu suốt tất cả. Bố hiểu rõ ai mới là người thực sự có tâm có đức, và ai là kẻ chỉ biết rình rập để xâu xé mồ hôi nước mắt của người khác!
"""

target = "Họ nghĩ rằng tôi là một đứa con gái hiền lành, quen thói nhẫn nhịn cam chịu suốt mười năm qua"
text = text.replace(target, part1_extra.strip() + "\n\n" + target)

with open('core/stories/life_drama.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added extra paragraph to Part 1 of life_drama.py!")
