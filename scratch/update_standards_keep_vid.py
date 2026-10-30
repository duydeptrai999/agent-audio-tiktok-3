# -*- coding: utf-8 -*-
with open(".agents/rules/scriptwriting_standards.md", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_sec2_top = """> 🚨 **TRIỆT TIÊU VĨNH VIỄN BỆNH "CHỮ TRÊN NỀN BÓNG ĐEN XẤU NHƯ CỨT" & "THUMBNAIL BỊ KÉO DÃN MÉO HÌNH"**:
> - Khán giả lướt TikTok nhìn video trong 0.5 giây đầu tiên. Video phải trong trẻo, sang trọng, sáng rõ từng chi tiết B-roll.
> - TUYỆT ĐỐI KHÔNG làm thumbnail ảnh tĩnh rời tải lên vì TikTok Studio sẽ kéo dãn méo hình! TikTok lấy trực tiếp frame gốc chuẩn dọc 1080x1920 (setsar=1) từ video MP4 đã khắc sẵn Header Text Title và Mô Tả sắc nét."""

new_sec2_top = """> 🚨 **ĐẠI QUY TẮC SỐNG CÒN: GIỮ NGUYÊN KHUNG HÌNH GỐC CỦA VIDEO (ZERO CROP / ZERO STRETCH / ZERO FIT)**:
> - **TUYỆT ĐỐI GIỮ NGUYÊN VIDEO GỐC**: CẤM 100% các hành vi kéo dãn video, CẤM crop xén mất góc, CẤM cưỡng bức scale ép fit (như scale=1080:1920) làm biến dạng hay méo mó khung hình!
> - Khung hình video gốc như thế nào (16:9 ngang, 9:16 dọc, 4:3, 1:1) thì **GIỮ NGUYÊN BẢN 100%**, chỉ lồng thêm giọng đọc AI và BGM ducking.
> - **KHÔNG làm thumbnail ảnh tĩnh rời**: Để tránh bị TikTok Studio kéo dãn méo hình khi upload cover, TikTok tự động lấy trực tiếp frame nguyên bản từ video MP4 đã có Header Title và Mô Tả thanh lịch."""

assert old_sec2_top in t_norm, "old_sec2_top not found in scriptwriting_standards.md"
t_norm = t_norm.replace(old_sec2_top, new_sec2_top)

with open(".agents/rules/scriptwriting_standards.md", "w", encoding="utf-8", newline="\n") as f:
    f.write(t_norm)

print("Updated scriptwriting_standards.md successfully!")
