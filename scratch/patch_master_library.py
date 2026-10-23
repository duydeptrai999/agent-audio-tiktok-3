from pathlib import Path

p = Path("core/narrative_master_library.py")
content = p.read_text(encoding="utf-8")

content = content.replace("Đồ tiện tì ăn cắp!", "Kẻ trơ trẽn!")
content = content.replace("Nhược Dao quỳ sụp dưới sàn đá cẩm thạch lạnh buốt, nước mắt lã chã rơi đẫm mu bàn tay: 'Mẹ ơi... con thề có trời đất chứng giám, con không hề bước chân vào phòng mẹ chiều nay! Xin mẹ hãy kiểm tra camera hành lang!'.",
                          "Nhược Dao đứng thẳng người, ngón tay bấu chặt mép bàn: 'Mẹ vu oan cho con? Camera hành lang bật 24/7, mẹ dám trích xuất đối chất ngay bây giờ không?'.")
content = content.replace("cơn ác mộng kinh hoàng nhất", "đòn trừng phạt sòng phẳng nhất")
content = content.replace("tiện nhân", "kẻ phản bội")

p.write_text(content, encoding="utf-8")
print("CLEANED NARRATIVE MASTER LIBRARY!")
