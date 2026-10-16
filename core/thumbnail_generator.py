# -*- coding: utf-8 -*-
"""
core/thumbnail_generator.py
Tạo Thumbnail chuẩn 16:9 (1920x1080) sắc nét, nghệ thuật cho từng Part / từng Audio:
- Trích xuất frame đại diện đẹp mắt từ video background của từng part.
- Tự động phủ gradient bảo vệ thị giác chống chìm chữ.
- Nhãn Visual Badge (TẬP 1, TẬP 2, TẬP 3 - KẾT) mạ vàng nổi bật.
- Tiêu đề câu chuyện tiếng Việt chuẩn 100% Unicode không lỗi font.
- Nhúng thumbnail vào metadata MP4 (Cover Art) hoặc xuất file ảnh riêng để tải lên.
"""

import os
import sys
import re
import time
import shutil
import subprocess
from pathlib import Path
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from core.ffmpeg_utils import get_ffmpeg_exe, get_vietnamese_font_path

def extract_video_frame(video_path: Path, output_frame_path: Path, timestamp_sec: float = 15.0) -> bool:
    """Trích xuất 1 frame chất lượng cao từ video tại thời điểm timestamp_sec."""
    ffmpeg = get_ffmpeg_exe()
    output_frame_path.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        ffmpeg, "-y",
        "-ss", str(timestamp_sec),
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "2",
        str(output_frame_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0 and output_frame_path.exists() and output_frame_path.stat().st_size > 1000:
        return True
        
    # Fallback trích xuất frame tại giây 1 nếu giây 15 vượt quá độ dài
    cmd_fallback = [
        ffmpeg, "-y",
        "-ss", "1.0",
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "2",
        str(output_frame_path)
    ]
    res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res_fb.returncode == 0 and output_frame_path.exists() and output_frame_path.stat().st_size > 1000

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    """Tự động ngắt dòng thông minh theo độ rộng pixel."""
    words = text.split()
    lines = []
    cur_line = []
    
    for word in words:
        test_line = " ".join(cur_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_w = bbox[2] - bbox[0]
        if line_w <= max_width or not cur_line:
            cur_line.append(word)
        else:
            lines.append(" ".join(cur_line))
            cur_line = [word]
            
    if cur_line:
        lines.append(" ".join(cur_line))
    return lines

def generate_part_thumbnail(
    source_video_or_image: Path,
    output_thumb_path: Path,
    story_title: str,
    part_label: str = "TẬP 1",
    genre_tag: str = "#AudioTruyện",
    subtitle_hint: str = "Audio Trọn Bộ • Tốc Độ 1.5x"
) -> Path:
    """
    Tạo thumbnail 1920x1080 hoàn chỉnh cho từng part của câu chuyện.
    """
    output_thumb_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 1. Lấy frame nền từ video hoặc ảnh
    temp_frame = output_thumb_path.parent / f"temp_{output_thumb_path.stem}.jpg"
    try:
        if source_video_or_image.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm"]:
            success = extract_video_frame(source_video_or_image, temp_frame, timestamp_sec=20.0)
            base_img_path = temp_frame if success else None
        elif source_video_or_image.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
            base_img_path = source_video_or_image
        else:
            base_img_path = None
            
        width, height = 1920, 1080
        if base_img_path and base_img_path.exists():
            base_image = Image.open(base_img_path).convert("RGBA")
            base_image = base_image.resize((width, height), Image.Resampling.LANCZOS)
        else:
            # Fallback gradient tối sang trọng
            base_image = Image.new("RGBA", (width, height), (15, 20, 35, 255))
            
        # 2. Phủ lớp gradient mờ (Vignette + Dark Overlay) để văn bản luôn nổi bần bật
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw_overlay = ImageDraw.Draw(overlay)
        
        # Gradient từ trên xuống (top bar) và từ dưới lên (bottom content)
        for y in range(height):
            if y < 220:
                alpha = int(170 * (1.0 - y / 220.0))
                draw_overlay.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))
            elif y > 450:
                alpha = int(210 * ((y - 450) / (height - 450)))
                draw_overlay.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))
                
        combined = Image.alpha_composite(base_image, overlay)
        draw = ImageDraw.Draw(combined)
        
        # 3. Nạp font chuẩn tiếng Việt
        font_candidates = [
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\tahomabd.ttf"
        ]
        font_path = "arialbd.ttf"
        for cand in font_candidates:
            if os.path.exists(cand):
                font_path = cand
                break
                
        font_badge = ImageFont.truetype(font_path, size=46)
        font_title = ImageFont.truetype(font_path, size=72)
        font_sub = ImageFont.truetype(font_path, size=38)
        font_tag = ImageFont.truetype(font_path, size=36)
        
        # 4. Vẽ Pill Badge (TẬP X / ĐẠI KẾT CỤC)
        clean_part = part_label.upper().replace("[", "").replace("]", "").strip()
        badge_text = f" {clean_part} "
        bbox_b = draw.textbbox((0, 0), badge_text, font=font_badge)
        b_w = bbox_b[2] - bbox_b[0]
        b_h = bbox_b[3] - bbox_b[1]
        
        bx0 = 80
        by0 = 70
        bx1 = bx0 + b_w + 50
        by1 = by0 + b_h + 30
        
        # Bo góc mềm mại màu vàng hoàng kim với viền nổi
        draw.rounded_rectangle([bx0, by0, bx1, by1], radius=20, fill=(255, 204, 0, 255), outline=(255, 255, 255, 255), width=3)
        draw.text((bx0 + 25, by0 + 10), badge_text, font=font_badge, fill=(15, 15, 15, 255))
        
        # 5. Vẽ Title chính (có bóng đổ drop-shadow đậm đà)
        clean_title = story_title.strip()
        lines = wrap_text(clean_title, font_title, max_width=1740, draw=draw)
        if len(lines) > 3:
            lines = lines[:3]
            lines[-1] += "..."
            
        start_y = height - 160 - (len(lines) * 90)
        for line in lines:
            # Vẽ bóng đổ 8 hướng tạo chiều sâu khối
            for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (4, 0), (-4, 0), (0, -4)]:
                draw.text((80 + dx, start_y + dy), line, font=font_title, fill=(0, 0, 0, 240))
            # Chữ chính màu trắng tinh
            draw.text((80, start_y), line, font=font_title, fill=(255, 255, 255, 255))
            start_y += 92
            
        # 6. Vẽ Footer Bar (Hashtags + Thể Loại + Hint)
        tag_text = f"{genre_tag} • {subtitle_hint}"
        draw.text((80, height - 75), tag_text, font=font_tag, fill=(255, 215, 0, 255))
        
        # Lưu file thumbnail định dạng RGB JPEG chất lượng 95
        final_rgb = combined.convert("RGB")
        final_rgb.save(str(output_thumb_path), format="JPEG", quality=95)
        print(f"  🖼️ Đã tạo xong Thumbnail 1080p: {output_thumb_path.name}")
        return output_thumb_path
    finally:
        # Dọn dẹp triệt để frame tạm trong khối finally
        if temp_frame.exists():
            try:
                temp_frame.unlink()
            except Exception:
                pass

def attach_thumbnail_to_mp4(video_path: Path, thumbnail_path: Path, output_path: Optional[Path] = None) -> Path:
    """
    Nhúng thumbnail vào metadata MP4 (Cover Art) để hiển thị trên trình phát và hệ thống.
    Được bảo vệ bằng cơ chế retry backoff khi gặp khóa file trên Windows (WinError 32)
    và luôn dọn sạch file tạm trong khối finally.
    """
    ffmpeg = get_ffmpeg_exe()
    target_out = output_path or (video_path.parent / f"{video_path.stem}_with_thumb.mp4")
    
    cmd = [
        ffmpeg, "-y",
        "-i", str(video_path),
        "-i", str(thumbnail_path),
        "-map", "0",
        "-map", "1",
        "-c", "copy",
        "-disposition:v:1", "attached_pic",
        str(target_out)
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and target_out.exists() and target_out.stat().st_size > 100000:
            if output_path is None:
                # Ghi đè lại file gốc an toàn với retry exponential backoff chống WinError 32
                max_retries = 5
                delay = 0.5
                replaced = False
                for attempt in range(max_retries):
                    try:
                        target_out.replace(video_path)
                        replaced = True
                        break
                    except (PermissionError, OSError) as e:
                        time.sleep(delay)
                        delay *= 1.5
                if not replaced:
                    try:
                        shutil.copyfile(str(target_out), str(video_path))
                        target_out.unlink(missing_ok=True)
                        replaced = True
                    except Exception as e_copy:
                        print(f"⚠️ [ThumbnailGenerator] Lỗi sao chép fallback thay thế video: {e_copy}")
                return video_path
            return target_out
        return video_path
    finally:
        # Dọn dẹp tệp tạm _with_thumb.mp4 nếu output_path là None và tệp tạm vẫn còn tồn tại
        if output_path is None and target_out.exists() and target_out != video_path:
            try:
                target_out.unlink(missing_ok=True)
            except Exception:
                pass
