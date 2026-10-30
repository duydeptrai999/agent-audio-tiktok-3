# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, '.')
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from core.visual_design import get_font, get_genre_palette, split_title, clean_part_label, wrap_by_pixels

def render_aesthetic_header(
    canvas_size: tuple[int, int],
    title: str,
    part_label: str,
    genre: str = ""
) -> Image.Image:
    """
    Tạo Header Overlay cao cấp điện ảnh, TUYỆT ĐỐI KHÔNG DÙNG NỀN ĐEN MỜ (Zero Murky Scrim):
    1. Video nền B-roll giữ nguyên 100% độ sáng, trong trẻo, tự nhiên.
    2. Pill Badge [TẬP X] bo tròn capsule sắc nét, màu nhấn rực rỡ, chữ trắng tinh khôi, viền kính mờ tinh tế.
    3. Tên Phim (Main Title): Font BeVietnamPro-Black/ExtraBold trắng sáng, đổ bóng Gaussian đa tầng mượt mà, không gai nét.
    4. Mô Tả Phim (Subtitle): Font BeVietnamPro-SemiBold màu vàng ánh kim hoặc pastel dạ quang sang trọng, thanh thoát.
    """
    width, height = canvas_size
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pal = get_genre_palette(genre or title)
    is_horizontal = width >= height
    cx = width // 2
    
    # TUYỆT ĐỐI KHÔNG ÁP DỤNG SCRIM / KHÔNG DÙNG DẢI MÀU ĐEN MỜ!
    dummy_d = ImageDraw.Draw(canvas)
    main, sub = split_title(title)
    
    # Vị trí y đỉnh
    y = int(height * 0.048) if is_horizontal else 140
    max_w = int(width * 0.84) if is_horizontal else int(width * 0.88)
    
    # -------------------------------------------------------------
    # 1. Pill Badge [TẬP 1] / [TẬP 3 · KẾT]
    # -------------------------------------------------------------
    ep_text = clean_part_label(part_label)
    pill_font = get_font("bold", 22 if is_horizontal else 25)
    p_bbox = dummy_d.textbbox((0, 0), ep_text, font=pill_font, anchor="lt")
    tw, th = p_bbox[2] - p_bbox[0], p_bbox[3] - p_bbox[1]
    pad_x, pad_y = (20, 6) if is_horizontal else (24, 8)
    pw, ph = tw + pad_x * 2, th + pad_y * 2
    px = cx - pw // 2
    py = y
    
    # Soft ambient shadow cho Pill Badge
    pill_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    psd = ImageDraw.Draw(pill_shadow)
    psd.rounded_rectangle([px, py + 2, px + pw, py + ph + 2], radius=ph // 2, fill=(0, 0, 0, 100))
    pill_shadow = pill_shadow.filter(ImageFilter.GaussianBlur(3))
    canvas.alpha_composite(pill_shadow)
    
    # Capsule Pill
    pill_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pld = ImageDraw.Draw(pill_layer)
    pld.rounded_rectangle(
        [px, py, px + pw, py + ph],
        radius=ph // 2,
        fill=pal["accent"] + (240,),
        outline=(255, 255, 255, 175),
        width=1
    )
    # Chữ trên Pill luôn là màu tương phản cao (trắng hoặc ink)
    pld.text(
        (cx, py + pad_y + th // 2),
        ep_text,
        font=pill_font,
        fill=(255, 255, 255, 255) if pal["accent"][0] > 100 or pal["accent"][1] < 180 else pal["ink"] + (255,),
        anchor="mm"
    )
    canvas.alpha_composite(pill_layer)
    
    y = py + ph + (13 if is_horizontal else 16)
    
    # -------------------------------------------------------------
    # 2. Tên Phim (Main Title)
    # -------------------------------------------------------------
    main_font = get_font("black", 42 if is_horizontal else 48)
    main_lines = wrap_by_pixels(main, main_font, max_w, dummy_d)
    if len(main_lines) > 2:
        main_font = get_font("black", 36 if is_horizontal else 42)
        main_lines = wrap_by_pixels(main, main_font, max_w, dummy_d)
    if len(main_lines) > 2:
        main_lines = main_lines[:2]
        main_lines[-1] = main_lines[-1].rstrip(",.;:") + "…"
        
    line_h = int(main_font.size * 1.22)
    
    # Gaussian Drop Shadow đa tầng cho Tên Phim
    title_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    tsd = ImageDraw.Draw(title_shadow)
    cur_y = y
    for ln in main_lines:
        # Tầng bóng mờ dịu
        tsd.text((cx, cur_y + 3), ln, font=main_font, fill=(0, 0, 0, 160), anchor="ma")
        cur_y += line_h
    title_shadow = title_shadow.filter(ImageFilter.GaussianBlur(5))
    canvas.alpha_composite(title_shadow)
    
    # Text Tên Phim: Trắng tinh thể sáng rực rỡ + viền vi mảnh 1px chống lóa trên nền trắng
    title_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    tld = ImageDraw.Draw(title_layer)
    cur_y = y
    for ln in main_lines:
        tld.text(
            (cx, cur_y),
            ln,
            font=main_font,
            fill=(255, 255, 255, 255),
            anchor="ma",
            stroke_width=1,
            stroke_fill=(15, 23, 42, 140)
        )
        cur_y += line_h
    canvas.alpha_composite(title_layer)
    y = cur_y
    
    # -------------------------------------------------------------
    # 3. Mô Tả Phim / Tập (Subtitle)
    # -------------------------------------------------------------
    if sub:
        y += (7 if is_horizontal else 9)
        sub_font = get_font("semibold", 27 if is_horizontal else 30)
        sub_lines = wrap_by_pixels(sub, sub_font, max_w, dummy_d)
        if len(sub_lines) > 2:
            sub_lines = sub_lines[:2]
            sub_lines[-1] = sub_lines[-1].rstrip(",.;:") + "…"
        sub_h = int(sub_font.size * 1.24)
        
        # Gaussian Drop Shadow cho Subtitle
        sub_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        ssd = ImageDraw.Draw(sub_shadow)
        cur_y = y
        for sln in sub_lines:
            ssd.text((cx, cur_y + 2), sln, font=sub_font, fill=(0, 0, 0, 150), anchor="ma")
            cur_y += sub_h
        sub_shadow = sub_shadow.filter(ImageFilter.GaussianBlur(4))
        canvas.alpha_composite(sub_shadow)
        
        # Màu chữ Subtitle: Vàng Champagne / Ánh Kim / Soft Pastel nổi bật
        sub_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sld = ImageDraw.Draw(sub_layer)
        cur_y = y
        # Màu vàng ánh kim champagne sang trọng (#FDE047 / #FEF08A) hoặc pastel thể loại
        sub_color = (254, 240, 138) if pal["soft"][0] > 200 and pal["soft"][1] > 200 else pal["soft"]
        for sln in sub_lines:
            sld.text(
                (cx, cur_y),
                sln,
                font=sub_font,
                fill=sub_color + (255,),
                anchor="ma",
                stroke_width=1,
                stroke_fill=(15, 23, 42, 130)
            )
            cur_y += sub_h
        canvas.alpha_composite(sub_layer)
        
    return canvas
