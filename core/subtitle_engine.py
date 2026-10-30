# -*- coding: utf-8 -*-
"""
core/subtitle_engine.py
Động Cơ Tạo Phụ Đề Động Chuẩn TikTok High-CTR (Kinetic Subtitles Engine - Codex 8.0).
- Tự động phân tách kịch bản thành các cụm từ ngắn gọn (3 - 6 từ / hiển thị)
- Phân bổ mốc thời gian chính xác theo độ dài file Audio thực tế (tính đến độ trễ dấu câu)
- Xuất file SRT chuẩn UTF-8 tương thích 100% với FFmpeg libass filter
- Thiết lập định dạng dọc 9:16 (1080x1920) thẩm mỹ cao: Chữ vàng chanh / trắng tuyết, viền đen sắc nét, đặt đúng 1/3 dưới màn hình (Safe Zone)
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Optional

def split_into_subtitle_phrases(text: str, max_words: int = 5) -> List[str]:
    """
    Tách đoạn văn thành các cụm từ ngắn gọn, tự nhiên theo ngữ điệu tiếng Việt.
    Mỗi cụm từ dài từ 3 đến 5 từ (chuẩn GEMINI.md 3.2) để khóa mắt người xem trên khung hình dọc 9:16.
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
                # Cắt thành các block 4-5 từ nhịp nhàng
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
    lead_in: float = 0.15
) -> Path:
    """
    Tạo file .srt hoàn chỉnh dựa trên văn bản kịch bản và tổng thời lượng file audio thực tế.
    Phân bổ thời gian theo trọng số độ dài ký tự và độ trễ dấu câu.
    """
    output_srt_path.parent.mkdir(parents=True, exist_ok=True)
    phrases = split_into_subtitle_phrases(text, max_words=5)
    
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
        # Đảm bảo mỗi cụm từ xuất hiện vừa vặn theo tốc độ đọc
        duration_for_phrase = max(0.55, min(3.8, duration_for_phrase))
        
        start_t = current_time
        end_t = min(total_duration_seconds, start_t + duration_for_phrase - 0.03)
        if end_t <= start_t:
            end_t = start_t + 0.4
            
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
    font_size: int = 16,
    margin_v: int = 68
) -> str:
    """
    Trả về chuỗi tham số filter subtitles của FFmpeg với style High-CTR chuẩn TikTok 9:16 (1080x1920):
    - Lưu ý: libass mặc định PlayResY=288 cho file .srt, nên FontSize=16 (~106px thật) và MarginV=68 (~450px cách đáy)
      đặt phụ đề nằm gọn gàng ở đúng vùng 1/3 dưới màn hình (Safe Zone), không chạm vào icon phải hay caption dưới.
    """
    escaped_srt = str(srt_path.resolve()).replace("\\", "/").replace(":", "\\:")
    
    primary_color = "&H0000FFFF" if color_scheme == "yellow" else "&H00FFFFFF"
    # Đảm bảo nếu truyền nhầm giá trị pixel lớn (>120) thì tự động quy đổi về thang PlayResY=288
    safe_font_size = font_size if font_size <= 22 else 16
    safe_margin_v = margin_v if margin_v <= 110 else 68
    
    style = (
        f"FontName=Arial,"
        f"FontSize={safe_font_size},"
        f"Bold=1,"
        f"PrimaryColour={primary_color},"
        f"SecondaryColour=&H00000000,"
        f"OutlineColour=&H00000000,"
        f"BackColour=&H80000000,"
        f"BorderStyle=1,"
        f"Outline=2,"
        f"Shadow=1,"
        f"Alignment=2,"
        f"MarginL=24,"
        f"MarginR=38,"
        f"MarginV={safe_margin_v}"
    )
    return f"subtitles='{escaped_srt}':force_style='{style}'"
