# -*- coding: utf-8 -*-
"""
core/thumbnail_generator.py
Tạo Thumbnail chuẩn dọc TikTok 9:16 (1080x1920) sắc nét, hiện đại cho từng Tập / từng Audio:
- Trích xuất frame đại diện đẹp mắt từ video background của từng tập và center-crop về 1080x1920.
- Phủ lớp gradient điện ảnh mềm mại (KHÔNG dùng hộp nền đen thô kệch).
- Phân tầng thị giác rõ ràng bằng font Be Vietnam Pro:
  1. Nhãn Tập (Pill Badge: TẬP 1/3, TẬP 2/3, TẬP 3 · KẾT) + Nhãn Thể Loại phối màu theo cảm xúc.
  2. Tên Phim (Main Title) cỡ lớn, chữ đậm sắc nét có bóng đổ mờ (soft Gaussian shadow).
  3. Mô Tả Phim / Tập (Subtitle) tách riêng bên dưới thanh lịch, dễ đọc ngay trên lưới hồ sơ 3:4 của TikTok.
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
from typing import Optional
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from core.ffmpeg_utils import get_ffmpeg_exe
from core.visual_design import (
    clean_part_label,
    draw_pill,
    draw_text_with_shadow,
    fit_text_block,
    get_font,
    get_genre_palette,
    split_title,
    vertical_gradient,
    wrap_by_pixels,
)


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
    return wrap_by_pixels(text, font, max_width, draw)


def generate_part_thumbnail(
    source_video_or_image: Path,
    output_thumb_path: Path,
    story_title: str,
    part_label: str = "TẬP 1",
    genre_tag: str = "#AudioTruyện",
    subtitle_hint: str = "Audio Đời Thực • Cắm Tai Nghe"
) -> Path:
    """
    Tạo thumbnail chuẩn dọc 1080x1920 (9:16) tối ưu hóa hiển thị trên lưới Profile TikTok (vùng 3:4 trung tâm).
    Không dùng nền hộp đen cứng; dùng gradient mềm + font Be Vietnam Pro phân tách Tên Phim và Mô Tả.
    """
    output_thumb_path.parent.mkdir(parents=True, exist_ok=True)
    temp_frame = output_thumb_path.parent / f"temp_{output_thumb_path.stem}.jpg"

    try:
        source_path = Path(source_video_or_image) if source_video_or_image else None
        if source_path and source_path.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm"]:
            success = extract_video_frame(source_path, temp_frame, timestamp_sec=18.0)
            base_img_path = temp_frame if success else None
        elif source_path and source_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
            base_img_path = source_path
        else:
            base_img_path = None

        width, height = 1080, 1920
        if base_img_path and base_img_path.exists():
            base_image = Image.open(base_img_path).convert("RGB")
            base_image = ImageOps.fit(base_image, (width, height), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
            base_image = ImageEnhance.Color(base_image).enhance(1.08)
            base_image = ImageEnhance.Contrast(base_image).enhance(1.05)
            base_image = base_image.convert("RGBA")
        else:
            base_image = Image.new("RGBA", (width, height), (20, 24, 38, 255))

        pal = get_genre_palette(f"{genre_tag} {story_title}")

        # Scrim điện ảnh siêu nhẹ, giữ độ sáng và vẻ đẹp của video nền ASMR, không tạo bóng đen sẫm
        grad_layer = vertical_gradient(
            width,
            height,
            [
                (0, 30),
                (600, 15),
                (900, 45),
                (1200, 80),
                (1600, 100),
                (1920, 100),
            ],
        )
        combined = Image.alpha_composite(base_image, grad_layer)
        draw = ImageDraw.Draw(combined)

        main_title, sub_title = split_title(story_title)
        clean_ep = clean_part_label(part_label)

        # Tính toán kích thước khối Tên Phim (Main Title) & Mô Tả (Subtitle)
        left_x = 80
        max_text_w = width - left_x * 2 - 16
        main_font, main_lines = fit_text_block(main_title, "black", 76, 54, max_text_w, 3, draw)
        main_line_h = int(main_font.size * 1.30)
        main_block_h = len(main_lines) * main_line_h

        sub_lines = []
        sub_font = get_font("semibold", 42)
        sub_line_h = 54
        if sub_title:
            sub_font, sub_lines = fit_text_block(sub_title, "semibold", 44, 34, max_text_w, 3, draw)
            sub_line_h = int(sub_font.size * 1.28)
        sub_block_h = len(sub_lines) * sub_line_h + (22 if sub_lines else 0)

        # Đặt toàn bộ cụm chữ trong vùng trung tâm lưới 3:4 của TikTok (y = 820 .. 1480)
        total_content_h = main_block_h + sub_block_h
        start_y = max(860, 1390 - total_content_h)

        # 1. Vẽ Pill Badge (TẬP 1/3) + Nhãn thể loại phía trên Tên Phim
        badge_font = get_font("black", 36)
        pill_box = draw_pill(
            combined,
            left_x,
            start_y - 86,
            clean_ep,
            badge_font,
            pal["accent"],
            pal["ink"],
            pad_x=28,
            pad_y=12,
            align="left",
        )
        genre_label_font = get_font("bold", 30)
        genre_chip_text = f"•  {pal['label']} AUDIO"
        draw_text_with_shadow(
            combined,
            (pill_box[2] + 20, pill_box[1] + 14),
            genre_chip_text,
            genre_label_font,
            pal["soft"] + (255,),
            anchor="la",
            shadow_alpha=180,
            shadow_blur=6,
        )

        # 2. Thanh nhấn dọc (Accent Vertical Bar) bên trái khối tiêu đề
        bar_top = start_y + 8
        bar_bottom = start_y + total_content_h - 10
        draw = ImageDraw.Draw(combined)
        draw.rounded_rectangle(
            [left_x - 24, bar_top, left_x - 12, bar_bottom],
            radius=6,
            fill=pal["accent"] + (255,),
        )

        # 3. Vẽ Tên Phim (Main Title) sắc nét với bóng đổ mềm
        cur_y = start_y
        for idx_l, line in enumerate(main_lines):
            line_color = (255, 255, 255, 255) if idx_l == 0 else (248, 248, 252, 255)
            draw_text_with_shadow(
                combined,
                (left_x, cur_y),
                line,
                main_font,
                line_color,
                anchor="la",
                shadow_alpha=120,
                shadow_blur=4,
                shadow_offset=(0, 2),
                stroke=2,
                stroke_fill=(12, 16, 24, 230),
            )
            cur_y += main_line_h

        # 4. Vẽ Mô Tả Phim / Tập (Subtitle) màu nhấn dịu mắt
        if sub_lines:
            cur_y += 18
            for line in sub_lines:
                draw_text_with_shadow(
                    combined,
                    (left_x, cur_y),
                    line,
                    sub_font,
                    pal["soft"] + (255,),
                    anchor="la",
                    shadow_alpha=110,
                    shadow_blur=3,
                    shadow_offset=(0, 2),
                    stroke=2,
                    stroke_fill=(12, 16, 24, 210),
                )
                cur_y += sub_line_h

        # 5. Dòng chân trang tinh tế trong Safe Zone
        footer_y = min(1510, max(1445, cur_y + 32))
        footer_font = get_font("medium", 28)
        clean_tag = genre_tag.replace("_", "").strip() if genre_tag else "#AudioTruyện"
        footer_text = f"{subtitle_hint}  •  {clean_tag}"
        draw_text_with_shadow(
            combined,
            (left_x, footer_y),
            footer_text,
            footer_font,
            (220, 224, 235, 235),
            anchor="la",
            shadow_alpha=180,
            shadow_blur=6,
        )

        final_rgb = combined.convert("RGB")
        final_rgb.save(str(output_thumb_path), format="JPEG", quality=95)
        print(f"  🖼️ Đã tạo xong Thumbnail dọc 9:16 (1080x1920): {output_thumb_path.name}")
        return output_thumb_path
    finally:
        if temp_frame.exists():
            try:
                temp_frame.unlink()
            except Exception:
                pass


def attach_thumbnail_to_mp4(video_path: Path, thumbnail_path: Path, output_path: Optional[Path] = None) -> Path:
    """
    Nhúng thumbnail vào metadata MP4 (Cover Art) nếu được yêu cầu riêng.
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
                max_retries = 5
                delay = 0.5
                replaced = False
                for _ in range(max_retries):
                    try:
                        target_out.replace(video_path)
                        replaced = True
                        break
                    except (PermissionError, OSError):
                        time.sleep(delay)
                        delay *= 1.5
                if not replaced:
                    try:
                        shutil.copyfile(str(target_out), str(video_path))
                        target_out.unlink(missing_ok=True)
                    except Exception as e_copy:
                        print(f"⚠️ [ThumbnailGenerator] Lỗi sao chép fallback thay thế video: {e_copy}")
                return video_path
            return target_out
        return video_path
    finally:
        if output_path is None and target_out.exists() and target_out != video_path:
            try:
                target_out.unlink(missing_ok=True)
            except Exception:
                pass
