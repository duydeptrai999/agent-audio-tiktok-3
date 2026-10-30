# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, '.')
from PIL import Image, ImageDraw, ImageFilter
from core.visual_design import get_font, get_genre_palette, split_title, clean_part_label, wrap_by_pixels

def create_modern_header_overlay(
    width: int,
    height: int,
    title: str,
    part_label: str,
    genre: str = "",
    use_scrim: bool = False
) -> Image.Image:
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pal = get_genre_palette(genre or title)
    is_horizontal = width >= height
    cx = width // 2
    
    # 0. KHÔNG DÙNG NỀN ĐEN MỜ (ZERO MURKY SCRIM)
    if use_scrim:
        from core.visual_design import vertical_gradient
        scrim_end = int(height * 0.28) if is_horizontal else 360
        canvas.alpha_composite(vertical_gradient(width, height, [(0, 40), (scrim_end, 0)]))
        
    main, sub = split_title(title)
    
    # Tính toán layout
    y = int(height * 0.05) if is_horizontal else 140
    max_w = int(width * 0.85) if is_horizontal else int(width * 0.88)
    
    # 1. Pill Badge [TẬP 1] - Capsule hiện đại với soft shadow
    ep_text = clean_part_label(part_label)
    pill_font = get_font("bold", 22 if is_horizontal else 25)
    
    # Đo kích thước pill
    dummy_d = ImageDraw.Draw(canvas)
    p_bbox = dummy_d.textbbox((0, 0), ep_text, font=pill_font, anchor="lt")
    tw, th = p_bbox[2] - p_bbox[0], p_bbox[3] - p_bbox[1]
    pad_x, pad_y = (20, 6) if is_horizontal else (24, 8)
    pw, ph = tw + pad_x * 2, th + pad_y * 2
    px = cx - pw // 2
    py = y
    
    # Vẽ soft shadow cho pill
    pill_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    psd = ImageDraw.Draw(pill_shadow)
    psd.rounded_rectangle([px, py + 3, px + pw, py + ph + 3], radius=ph // 2, fill=(0, 0, 0, 90))
    pill_shadow = pill_shadow.filter(ImageFilter.GaussianBlur(4))
    canvas.alpha_composite(pill_shadow)
    
    # Vẽ capsule pill
    pill_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pld = ImageDraw.Draw(pill_layer)
    pld.rounded_rectangle(
        [px, py, px + pw, py + ph],
        radius=ph // 2,
        fill=pal["accent"] + (235,),
        outline=(255, 255, 255, 160),
        width=1
    )
    pld.text(
        (cx, py + pad_y + th // 2),
        ep_text,
        font=pill_font,
        fill=pal["ink"] + (255,),
        anchor="mm"
    )
    canvas.alpha_composite(pill_layer)
    
    y = py + ph + (14 if is_horizontal else 16)
    
    # 2. Main Title (Tên Phim)
    main_font = get_font("extrabold", 42 if is_horizontal else 48)
    main_lines = wrap_by_pixels(main, main_font, max_w, dummy_d)
    if len(main_lines) > 2:
        main_font = get_font("extrabold", 36 if is_horizontal else 42)
        main_lines = wrap_by_pixels(main, main_font, max_w, dummy_d)
    if len(main_lines) > 2:
        main_lines = main_lines[:2]
        main_lines[-1] = main_lines[-1].rstrip(",.;:") + "…"
        
    line_h = int(main_font.size * 1.22)
    
    # Tạo shadow layer riêng biệt với Gaussian Blur đa tầng (Dual-Pass Feathered Shadow)
    title_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    tsd = ImageDraw.Draw(title_shadow)
    cur_y = y
    for ln in main_lines:
        # Layer 1: Ambient soft shadow
        tsd.text((cx, cur_y + 3), ln, font=main_font, fill=(0, 0, 0, 160), anchor="ma")
        cur_y += line_h
    title_shadow = title_shadow.filter(ImageFilter.GaussianBlur(5))
    canvas.alpha_composite(title_shadow)
    
    # Text Title chính: Trắng tinh khiết + viền vi mảnh 1px chống lóa
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
            stroke_fill=(0, 0, 0, 160)
        )
        cur_y += line_h
    canvas.alpha_composite(title_layer)
    y = cur_y
    
    # 3. Subtitle (Mô Tả Phim / Tập)
    if sub:
        y += (6 if is_horizontal else 8)
        sub_font = get_font("semibold", 26 if is_horizontal else 30)
        sub_lines = wrap_by_pixels(sub, sub_font, max_w, dummy_d)
        if len(sub_lines) > 2:
            sub_lines = sub_lines[:2]
            sub_lines[-1] = sub_lines[-1].rstrip(",.;:") + "…"
        sub_h = int(sub_font.size * 1.25)
        
        # Subtitle shadow
        sub_shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        ssd = ImageDraw.Draw(sub_shadow)
        cur_y = y
        for sln in sub_lines:
            ssd.text((cx, cur_y + 2), sln, font=sub_font, fill=(0, 0, 0, 150), anchor="ma")
            cur_y += sub_h
        sub_shadow = sub_shadow.filter(ImageFilter.GaussianBlur(3))
        canvas.alpha_composite(sub_shadow)
        
        # Subtitle text: Màu pastel phát sáng nhẹ theo thể loại
        sub_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sld = ImageDraw.Draw(sub_layer)
        cur_y = y
        for sln in sub_lines:
            sld.text(
                (cx, cur_y),
                sln,
                font=sub_font,
                fill=pal["soft"] + (255,),
                anchor="ma",
                stroke_width=1,
                stroke_fill=(0, 0, 0, 140)
            )
            cur_y += sub_h
        canvas.alpha_composite(sub_layer)
        
    return canvas

print("create_modern_header_overlay function ready!")
