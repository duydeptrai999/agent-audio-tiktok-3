from pathlib import Path

p = Path("core/prompts.py")
content = p.read_text(encoding="utf-8")

# Add Master Codex to BOSS_PROMPT and SCRIPTWRITER_PROMPTS
codex_section = """
QUY CHUẨN ĐỈNH CAO BẮT BUỘC (MASTER CODEX SAU 5 VÒNG THỰC NGHIỆM AGENT AUDIT):
- NGUYÊN TẮC VẬT CHẤT HỮU HÌNH: Mọi xung đột phải neo vào đạo cụ vật lý có thật (Bản di chúc, tách trà sen nóng, bật lửa Zippo, hóa đơn, kẹp inox, băng ghi âm, còi kim loại).
- HOOK 3S ĐỜI THỰC: 15 từ đầu tiên phải có Dị Thường Thị Giác hoặc Nghịch Lý Hành Động. CẤM tả thời tiết, CẤM tóm tắt tiểu sử (Zero-Summary), CẤM mở đầu YouTube ('Nếu bạn vô tình...').
- ĐỐI THOẠI NHÁT GỪNG CÓ DAO GĂM (SUBTEXT): Thoại ngắn 5-12 từ, mang tính gài bẫy. Kẻ thù không được nhận tội ngay mà phải dùng logic/bẫy phản kháng cho tới khi sụp đổ phòng tuyến tâm lý rồi tự lỡ lời thú tội.
- MICRO-PACING 25S & MICRO-MOVEMENT: Cứ mỗi 60-75 từ phải thả 1 biến số vật lý / bước ngoặt mới. Cứ sau 2 câu thoại phải có 1 chuyển động cơ thể (xoay cổ tay, hất tách trà, lùi một bước, rút điện thoại).
- ACTION-APEX CLIFFHANGER: Cắt tập đúng đỉnh điểm hành động sinh tử hoặc đối mặt hiểm nguy, KHÔNG cắt lúc nhân vật suy nghĩ nội tâm.
- ÂM HỌC EDGE-TTS: Câu ngắn 8-16 từ (tối đa 20 từ), chốt câu bằng thanh trắc đanh thép.
- ZERO MECHANICAL PADDING: TUYỆT ĐỐI CẤM độn chữ cơ học hoặc lặp lại đoạn văn để kéo dài thời gian."""

if "MASTER CODEX SAU 5 VÒNG THỰC NGHIỆM AGENT AUDIT" not in content:
    content = content.replace("QUY TẮC CỐT TỬ NÂNG TẦM KỊCH BẢN:", f"QUY TẮC CỐT TỬ NÂNG TẦM KỊCH BẢN:\n{codex_section}")
    content = content.replace("QUY TẮC CỐT TỬ NÂNG TẦM KỊCH BẢN ĐỘC LẠ:", f"QUY TẮC CỐT TỬ NÂNG TẦM KỊCH BẢN ĐỘC LẠ:\n{codex_section}")
    p.write_text(content, encoding="utf-8")
    print("UPGRADED CORE/PROMPTS.PY WITH MASTER CODEX!")
else:
    print("ALREADY PRESENT")
