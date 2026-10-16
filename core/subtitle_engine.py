# -*- coding: utf-8 -*-
"""
core/subtitle_engine.py
Động Cơ Tạo Phụ Đề Động Chuẩn TikTok High-CTR (Kinetic Subtitles Engine).
- Tự động phân tách kịch bản thành các cụm từ ngắn gọn (4 - 8 từ / hiển thị)
- Phân bổ mốc thời gian chính xác theo độ dài file Audio thực tế (tính đến độ trễ dấu câu)
- Xuất file SRT chuẩn UTF-8 tương thích 100% với FFmpeg libass filter
- Thiết lập định dạng thẩm mỹ cao: Chữ vàng tươi chanh / trắng tuyết, viền đen dày, bóng đổ nổi bật
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Optional

def split_into_subtitle_phrases(text: str, max_words: int = 7) -> List[str]:
    """
    Tách đoạn văn thành các cụm từ ngắn gọn, tự nhiên theo ngữ điệu tiếng Việt.
    Mỗi cụm từ dài từ 3 đến 7 từ để người xem lướt đọc trong 1.5 - 2.5 giây.
    """
    clean = re.sub(r'[\r\n]+', ' ', text).strip()
    # Tách trước theo dấu câu lớn (. ! ? … -)
    raw_sentences = re.split(r'(?<=[.!?…\n])\s+', clean)
    
    phrases = []
    for sent in raw_sentences:
        sent = sent.strip()
        if not sent:
            continue
        
        # Tách tiếp theo dấu phẩy hoặc liên từ nếu câu còn dài
        sub_parts = re.split(r'(?<=[,;:\-])\s+', sent)
        for part in sub_parts:
            part = part.strip()
            if not part:
                continue
            words = part.split()
            if len(words) <= max_words:
                phrases.append(part)
            else:
                # Cắt thành các block nhỏ hơn
                for i in range(0, len(words), max_words):
                    chunk = " ".join(words[i:i + max_words])
                    if chunk:
                        phrases.append(chunk)
                        
    return phrases

def format_srt_time(seconds: float) -> str:
    """Format số giây float thành chuẩn timestamp SRT: HH:MM:SS,mmm"""
    if seconds < 0:
        seconds = 0
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        secs += 1
        millis = 0
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def generate_srt_from_text_and_duration(
    text: str,
    total_duration_seconds: float,
    output_srt_path: Path,
    lead_in: float = 0.2
) -> Path:
    """
    Tạo file .srt hoàn chỉnh dựa trên văn bản kịch bản và tổng thời lượng file audio thực tế.
    Phân bổ thời gian theo trọng số độ dài ký tự và độ trễ dấu câu.
    """
    output_srt_path.parent.mkdir(parents=True, exist_ok=True)
    phrases = split_into_subtitle_phrases(text, max_words=7)
    
    if not phrases:
        phrases = ["..."]

    # Tính trọng số thời lượng của từng cụm từ
    weights = []
    for p in phrases:
        # Cơ bản: độ dài ký tự
        w = max(1.0, len(p))
        # Thêm độ trễ nếu kết thúc bằng dấu chấm, hỏi, than, ba chấm
        if p.endswith(('.', '!', '?', '…', '...')):
            w *= 1.35
        elif p.endswith((',', ';', ' -', '-')):
            w *= 1.15
        weights.append(w)
        
    total_weight = sum(weights)
    usable_duration = max(1.0, total_duration_seconds - lead_in)
    
    srt_entries = []
    current_time = lead_in

    for idx, (phrase, w) in enumerate(zip(phrases, weights), 1):
        duration_for_phrase = (w / total_weight) * usable_duration
        # Đảm bảo mỗi cụm từ xuất hiện ít nhất 0.8s và nhiều nhất 4.0s
        duration_for_phrase = max(0.8, min(4.5, duration_for_phrase))
        
        start_t = current_time
        end_t = min(total_duration_seconds, start_t + duration_for_phrase - 0.05)
        if end_t <= start_t:
            end_t = start_t + 0.5
            
        srt_entries.append(f"{idx}\n{format_srt_time(start_t)} --> {format_srt_time(end_t)}\n{phrase.strip()}\n")
        current_time += duration_for_phrase
        if current_time >= total_duration_seconds:
            break

    # Ghi file SRT UTF-8 chuẩn
    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries) + "\n")
        
    return output_srt_path

def get_tiktok_subtitles_filter_param(
    srt_path: Path,
    color_scheme: str = "yellow",
    font_size: int = 28,
    margin_v: int = 220
) -> str:
    """
    Trả về chuỗi tham số filter subtitles của FFmpeg với style High-CTR chuẩn TikTok:
    - Font chữ Arial đậm nét
    - Màu chữ vàng chanh rực rỡ (&H0000FFFF) hoặc trắng tuyết (&H00FFFFFF)
    - Viền đen đậm nét 3px (Outline=3) chống chìm trên mọi background
    - Vị trí MarginV=220px cách đáy màn hình (tránh nút caption TikTok)
    """
    escaped_srt = str(srt_path.resolve()).replace("\\", "/").replace(":", "\\:")
    
    primary_color = "&H0000FFFF" if color_scheme == "yellow" else "&H00FFFFFF"
    
    style = (
        f"FontName=Arial,"
        f"FontSize={font_size},"
        f"Bold=1,"
        f"PrimaryColour={primary_color},"
        f"SecondaryColour=&H00000000,"
        f"OutlineColour=&H00000000,"
        f"BackColour=&H80000000,"
        f"BorderStyle=1,"
        f"Outline=3,"
        f"Shadow=2,"
        f"Alignment=2,"
        f"MarginV={margin_v}"
    )
    return f"subtitles='{escaped_srt}':force_style='{style}'"
