import re
from typing import List, Tuple, Optional, Dict, Any
from core.state import ScriptPart, VideoCategory

def split_into_series(
    title: str,
    hook: str,
    body: str,
    cta: str,
    full_text: str,
    category: VideoCategory = VideoCategory.HIGH_IQ,
    structured_parts: Optional[List[Dict[str, Any]]] = None,
    target_parts_count: int = 3
) -> Tuple[bool, List[ScriptPart]]:
    """
    Động cơ Phân Đoạn Bộ Truyện Audio 3 Hồi Chuẩn TikTok (30 Phút Chia 3 Tập X 10 Phút).
    - Tập 1 (~10 phút): Mở đầu biến cố bí ẩn & Cliffhanger nghẹt thở.
    - Tập 2 (~10 phút): 15s Recap & Bước ngoặt cao trào tột độ & Cliffhanger 2.
    - Tập 3 (~10 phút): 15s Recap & Tháo gỡ nút thắt đại kết cục & Câu hỏi phân cực.
    """
    # 1. Trường hợp có sẵn danh sách 3 phần có cấu trúc từ LLM Biên Kịch
    if structured_parts and len(structured_parts) >= 2:
        parts: List[ScriptPart] = []
        total_p = len(structured_parts)
        for idx, p_data in enumerate(structured_parts, start=1):
            is_last = (idx == total_p)
            badge = f"PHẦN {idx} / KẾT" if is_last else f"PHẦN {idx}"
            raw_title = p_data.get("title") or f"{title} (Tập {idx})"
            # Xóa sạch mọi chuỗi thời gian nếu có trong title
            p_title = re.sub(r'\(?\d+\s*phút\)?', '', raw_title, flags=re.IGNORECASE).strip()
            p_hook = p_data.get("hook") or ""
            p_body = p_data.get("body", "")
            p_cliff = p_data.get("cliffhanger", "")
            p_cta = p_data.get("call_to_action") or (cta if is_last else "")

            # Văn bản lồng tiếng: Thuần túy là lời kể chuyện, không bao gồm 'Ở tập 1', 'Ở tập 2', hay CTA kêu gọi
            raw_full = p_data.get("full_text") or (f"{p_body}\n\n{p_cliff}" if p_cliff else p_body).strip()
            clean_full = re.sub(r'^\s*ở\s+(?:tập|phần)\s+\d+[^,.\n]*[,.\n]+\s*', '', raw_full, flags=re.IGNORECASE).strip()
            clean_full = re.sub(r'\s*đón\s+xem\s+tập\s+\d+[^.\n]*[.!]*', '', clean_full, flags=re.IGNORECASE).strip()
            clean_full = re.sub(r'\s*bấm\s+theo\s+dõi[^.\n]*[.!]*', '', clean_full, flags=re.IGNORECASE).strip()

            parts.append(ScriptPart(
                part_number=idx,
                total_parts=total_p,
                badge_label=badge,
                title=p_title,
                hook=p_hook,
                body=p_body,
                cliffhanger=p_cliff,
                call_to_action=p_cta,
                full_text=clean_full,
                target_duration_seconds=600  # Thời lượng audio chuẩn
            ))
        return True, parts

    # 2. Trường hợp văn bản liền mạch -> Tự động cắt thành 3 phần cân đối
    sentences = [s.strip() for s in re.split(r'(?<=[.!?…])\s+', body.strip()) if s.strip()]
    if len(sentences) < 3:
        # Nếu quá ít câu, chia đều theo từ
        words = full_text.split()
        third = max(1, len(words) // 3)
        chunk1 = " ".join(words[:third])
        chunk2 = " ".join(words[third:2*third])
        chunk3 = " ".join(words[2*third:])
    else:
        third_idx = max(1, len(sentences) // 3)
        chunk1 = " ".join(sentences[:third_idx])
        chunk2 = " ".join(sentences[third_idx:2*third_idx])
        chunk3 = " ".join(sentences[2*third_idx:])

    # Xây dựng câu kết truyện tự nhiên cho từng hồi (thuần kể chuyện, không thông báo ngoài lề)
    if category == VideoCategory.SLEEP_CHILL:
        cliff_p1 = "Không gian tĩnh mịch của đêm tối dường như đang lắng lại, mang theo những rung động đầu tiên của hai tâm hồn đang dần xích lại gần nhau."
        cliff_p2 = "Trong màn đêm dịu êm, những hoài nghi ban đầu dần tan biến, nhường chỗ cho sự thấu hiểu và gắn kết chân thành."
        cta_p1 = "Bấm follow để không bỏ lỡ Tập 2 vào đêm nay."
        cta_p2 = "Đón xem Tập 3 trên kênh nhé."
        cta_p3 = cta or "Chúc bạn có một giấc ngủ an lành và những giấc mơ ngọt ngào."
    else:
        cliff_p1 = "Trong bóng tối mịt mùng, tiếng bước chân lạ vẫn vang lên đều đặn, báo hiệu một sự thật kinh hoàng chuẩn bị được hé lộ."
        cliff_p2 = "Mọi chứng cứ tưởng như đã rõ ràng bỗng chốc đảo lộn hoàn toàn, đẩy sự việc vào một bước ngoặt nguy hiểm không thể lường trước."
        cta_p1 = "Bấm follow ngay để đón xem Tập 2 phát sóng tối nay!"
        cta_p2 = "Đón xem Tập 3 - Đại Kết Cục phát sóng tối nay trên kênh!"
        cta_p3 = cta or "Theo bạn, cái kết này có thực sự công bằng? Để lại bình luận bên dưới nhé!"

    recap_p2 = "Nối tiếp diễn biến căng thẳng của phần trước..." if category != VideoCategory.SLEEP_CHILL else "Tiếp nối câu chuyện đêm muộn dịu êm..."
    recap_p3 = "Nối tiếp đại kết cục nghẹt thở..." if category != VideoCategory.SLEEP_CHILL else "Khép lại những lắng đọng tâm hồn..."

    full_p1 = f"{chunk1} {cliff_p1}".strip()
    full_p2 = f"{chunk2} {cliff_p2}".strip()
    full_p3 = chunk3.strip()

    clean_base_title = re.sub(r'\(?\d+\s*phút\)?', '', title, flags=re.IGNORECASE).strip()

    part1 = ScriptPart(
        part_number=1,
        total_parts=3,
        badge_label="PHẦN 1",
        title=f"{clean_base_title} (Tập 1)",
        hook=hook,
        body=chunk1,
        cliffhanger=cliff_p1,
        call_to_action=cta_p1,
        full_text=full_p1,
        target_duration_seconds=600
    )

    part2 = ScriptPart(
        part_number=2,
        total_parts=3,
        badge_label="PHẦN 2",
        title=f"{clean_base_title} (Tập 2)",
        hook=recap_p2,
        body=chunk2,
        cliffhanger=cliff_p2,
        call_to_action=cta_p2,
        full_text=full_p2,
        target_duration_seconds=600
    )

    part3 = ScriptPart(
        part_number=3,
        total_parts=3,
        badge_label="PHẦN 3 / KẾT",
        title=f"{clean_base_title} (Tập 3 - Đại Kết Cục)",
        hook=recap_p3,
        body=chunk3,
        cliffhanger="",
        call_to_action=cta_p3,
        full_text=full_p3,
        target_duration_seconds=600
    )

    return True, [part1, part2, part3]

