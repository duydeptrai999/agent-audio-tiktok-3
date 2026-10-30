# -*- coding: utf-8 -*-
"""
core/visual_design.py
Hệ Thống Thiết Kế Chữ Dùng Chung (Packaging Design System) cho Thumbnail & Header Video.

Thay thế hoàn toàn kiểu cũ "chữ trắng trên hộp nền đen + thanh đỏ" (xấu, rẻ tiền):
- Font Be Vietnam Pro (thiết kế riêng cho tiếng Việt, dấu đẹp, không lỗi ô vuông).
- KHÔNG dùng hộp nền đặc. Độ đọc được đảm bảo bằng gradient mềm + bóng đổ mờ (soft shadow) + viền mảnh.
- Bảng màu nhấn theo thể loại (Ngôn tình hồng đào, Kinh dị đỏ máu, Trinh thám xanh lạnh, Gia đấu vàng hổ phách...).
- Tách tiêu đề "Tên Phim: Mô Tả" thành 2 tầng chữ: Tên phim to đậm + mô tả nhỏ thanh lịch.
"""

import os
import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT_DIR = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT_DIR / "assets" / "fonts"

_FONT_FILES = {
    "black": ["BeVietnamPro-Black.ttf"],
    "extrabold": ["BeVietnamPro-ExtraBold.ttf", "BeVietnamPro-Black.ttf"],
    "bold": ["BeVietnamPro-Bold.ttf", "BeVietnamPro-ExtraBold.ttf"],
    "semibold": ["BeVietnamPro-SemiBold.ttf", "BeVietnamPro-Bold.ttf"],
    "medium": ["BeVietnamPro-Medium.ttf", "BeVietnamPro-SemiBold.ttf"],
}
_SYSTEM_FALLBACK = {
    "black": [r"C:\Windows\Fonts\seguibl.ttf", r"C:\Windows\Fonts\arialbd.ttf"],
    "extrabold": [r"C:\Windows\Fonts\seguibl.ttf", r"C:\Windows\Fonts\arialbd.ttf"],
    "bold": [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"],
    "semibold": [r"C:\Windows\Fonts\seguisb.ttf", r"C:\Windows\Fonts\arialbd.ttf"],
    "medium": [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"],
}
_font_cache: Dict[Tuple[str, int], ImageFont.FreeTypeFont] = {}


def get_font(weight: str, size: int) -> ImageFont.FreeTypeFont:
    """Trả về font tiếng Việt đẹp nhất có sẵn theo độ đậm (black/extrabold/bold/semibold/medium)."""
    key = (weight, size)
    if key in _font_cache:
        return _font_cache[key]
    candidates = [str(FONT_DIR / f) for f in _FONT_FILES.get(weight, [])] + _SYSTEM_FALLBACK.get(weight, [])
    for cand in candidates:
        if os.path.exists(cand):
            try:
                font = ImageFont.truetype(cand, size=size)
                _font_cache[key] = font
                return font
            except Exception:
                continue
    font = ImageFont.load_default()
    _font_cache[key] = font
    return font


def _strip_accents(text: str) -> str:
    t = unicodedata.normalize("NFD", text or "")
    t = re.sub(r"[\u0300-\u036f]", "", t)
    return t.replace("đ", "d").replace("Đ", "D").lower()


# Bảng màu theo thể loại: accent = màu nhấn (pill, gạch chân), soft = màu chữ phụ, ink = màu chữ trên pill
GENRE_PALETTES = {
    "horror": {"accent": (226, 38, 52), "soft": (255, 196, 196), "ink": (255, 255, 255), "label": "KINH DỊ"},
    "detective": {"accent": (88, 196, 255), "soft": (200, 236, 255), "ink": (8, 20, 32), "label": "TRINH THÁM"},
    "survival": {"accent": (255, 146, 54), "soft": (255, 222, 190), "ink": (30, 14, 0), "label": "MẠT THẾ"},
    "comedy": {"accent": (196, 255, 74), "soft": (236, 255, 200), "ink": (18, 28, 0), "label": "SA ĐIÊU"},
    "palace": {"accent": (234, 188, 98), "soft": (255, 232, 190), "ink": (40, 14, 6), "label": "CUNG ĐẤU"},
    "revenge": {"accent": (255, 88, 96), "soft": (255, 210, 212), "ink": (255, 255, 255), "label": "VẢ MẶT"},
    "family": {"accent": (255, 194, 60), "soft": (255, 234, 186), "ink": (34, 20, 0), "label": "GIA ĐẤU"},
    "rich": {"accent": (240, 204, 128), "soft": (255, 238, 204), "ink": (36, 24, 4), "label": "HÀO MÔN"},
    "romance": {"accent": (255, 132, 168), "soft": (255, 218, 228), "ink": (54, 6, 24), "label": "THANH XUÂN"},
}


def classify_genre_style(genre: str) -> str:
    g = _strip_accents(genre)
    rules = [
        ("horror", ["kinh di", "quai dam", "truyen ma", "horror", "tam linh", "ma quy", "am hon"]),
        ("detective", ["trinh tham", "ky an", "huyen nghi", "detective", "phap y", "toi pham"]),
        ("survival", ["mat the", "sinh ton", "tan the", "survival"]),
        ("comedy", ["sa dieu", "hai huoc", "tieng long", "cong so", "funny", "comedy"]),
        ("palace", ["cung dau", "co phong", "hoang hau", "dich nu", "ancient", "palace"]),
        ("revenge", ["trong sinh", "va mat", "bao thu", "revenge"]),
        ("family", ["gia dau", "me chong", "ly hon", "doi song", "drama", "gia dinh", "family"]),
        ("rich", ["hao mon", "tong tai", "do thi", "rich"]),
        ("romance", ["thanh xuan", "vuon truong", "romance", "ngon tinh", "chua lanh", "tinh yeu", "healing"]),
    ]
    for style, kws in rules:
        if any(k in g for k in kws):
            return style
    return "romance"


def get_genre_palette(genre: str) -> Dict:
    return GENRE_PALETTES[classify_genre_style(genre)]


def split_title(title: str) -> Tuple[str, str]:
    """Tách 'Tên Phim: Mô tả' -> (tên phim, mô tả). Hỗ trợ dấu ':' , ' – ', ' - ', ' | '."""
    t = re.sub(r"\s+", " ", (title or "").replace("'", "’")).strip()
    for sep in [":", " – ", " — ", " | ", " - "]:
        if sep in t:
            main, sub = t.split(sep, 1)
            if len(main.strip()) >= 4 and sub.strip():
                return main.strip(), sub.strip()
    return t, ""


def clean_part_label(part_label: str, part_num: Optional[int] = None) -> str:
    lbl = (part_label or "").upper().replace("[", "").replace("]", "").strip()
    lbl = re.sub(r"\(?\d+\s*PHÚT\)?", "", lbl).strip()
    lbl = lbl.replace("PHẦN", "TẬP")
    m = re.search(r"(\d+)", lbl)
    num = part_num or (int(m.group(1)) if m else 1)
    if num >= 3 or "KẾT" in lbl:
        return "TẬP 3 · KẾT"
    return f"TẬP {num}/3"


def wrap_by_pixels(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    words = text.split()
    lines: List[str] = []
    cur: List[str] = []
    for w in words:
        test = " ".join(cur + [w])
        if not cur or draw.textlength(test, font=font) <= max_width:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    # Chống "mồ côi": dòng cuối chỉ có 1 từ ngắn -> kéo bớt 1 từ từ dòng trên xuống
    if len(lines) >= 2 and len(lines[-1].split()) == 1:
        prev = lines[-2].split()
        if len(prev) >= 3:
            candidate = prev[-1] + " " + lines[-1]
            if draw.textlength(candidate, font=font) <= max_width:
                lines[-2] = " ".join(prev[:-1])
                lines[-1] = candidate
    return lines


def fit_text_block(text: str, weight: str, max_size: int, min_size: int, max_width: int,
                   max_lines: int, draw: ImageDraw.ImageDraw) -> Tuple[ImageFont.FreeTypeFont, List[str]]:
    """Tự động giảm cỡ chữ cho đến khi khối chữ vừa max_lines dòng."""
    size = max_size
    while size >= min_size:
        font = get_font(weight, size)
        lines = wrap_by_pixels(text, font, max_width, draw)
        if len(lines) <= max_lines:
            return font, lines
        size -= 4
    font = get_font(weight, min_size)
    lines = wrap_by_pixels(text, font, max_width, draw)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(",.;:") + "…"
    return font, lines


def vertical_gradient(width: int, height: int, stops: List[Tuple[int, int]]) -> Image.Image:
    """Tạo lớp gradient đen trong suốt theo chiều dọc. stops = [(y, alpha), ...] nội suy mượt (ease)."""
    grad = Image.new("L", (1, height), 0)
    px = grad.load()
    stops = sorted(stops)
    for y in range(height):
        if y <= stops[0][0]:
            a = stops[0][1]
        elif y >= stops[-1][0]:
            a = stops[-1][1]
        else:
            for (y0, a0), (y1, a1) in zip(stops, stops[1:]):
                if y0 <= y <= y1:
                    t = (y - y0) / max(1, (y1 - y0))
                    t = t * t * (3 - 2 * t)  # smoothstep
                    a = a0 + (a1 - a0) * t
                    break
        px[0, y] = int(max(0, min(255, a)))
    alpha = grad.resize((width, height))
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    layer.putalpha(alpha)
    return layer


def draw_text_with_shadow(canvas: Image.Image, xy: Tuple[float, float], text: str, font: ImageFont.FreeTypeFont,
                          fill: Tuple[int, ...], anchor: str = "la", shadow_alpha: int = 120,
                          shadow_blur: int = 3, shadow_offset: Tuple[int, int] = (0, 2),
                          stroke: int = 2, stroke_fill: Tuple[int, ...] = (12, 16, 24, 220)) -> None:
    """Vẽ chữ sắc nét với viền vi mảnh (sharp micro-stroke) và bóng đổ nhẹ, không tạo vệt đen nhòe."""
    if shadow_alpha > 0 and shadow_blur > 0:
        shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        sx, sy = xy[0] + shadow_offset[0], xy[1] + shadow_offset[1]
        sd.text((sx, sy), text, font=font, fill=(0, 0, 0, shadow_alpha), anchor=anchor,
                stroke_width=stroke, stroke_fill=(0, 0, 0, shadow_alpha))
        shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
        canvas.alpha_composite(shadow)
    d = ImageDraw.Draw(canvas)
    d.text(xy, text, font=font, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=stroke_fill)


def draw_pill(canvas: Image.Image, x: int, y: int, text: str, font: ImageFont.FreeTypeFont,
              fill: Tuple[int, int, int], ink: Tuple[int, int, int], pad_x: int = 22, pad_y: int = 7,
              align: str = "left") -> Tuple[int, int, int, int]:
    """Vẽ nhãn bo tròn (pill) tinh tế, viền mảnh sắc nét, không bóng đen nhòe. Trả về bbox."""
    d = ImageDraw.Draw(canvas)
    bbox = d.textbbox((0, 0), text, font=font, anchor="lt")
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    w, h = tw + pad_x * 2, th + pad_y * 2
    if align == "center":
        x = int(x - w / 2)
    # Vẽ capsule hiện đại với viền trắng mờ tinh tế
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill + (245,),
                        outline=(255, 255, 255, 140), width=1)
    d.text((x + pad_x - bbox[0], y + pad_y - bbox[1]), text, font=font, fill=ink + (255,), anchor="lt")
    return (x, y, x + w, y + h)


def render_video_header_overlay(output_png: Path, title: str, part_label: str, genre: str = "",
                                width: int = 1920, height: int = 1080) -> Path:
    """
    Tạo lớp overlay PNG trong suốt cho phần đầu video:
    - TUYỆT ĐỐI KHÔNG DÙNG NỀN ĐEN MỜ (Zero Murky Scrim): Giữ video B-roll sáng trong trẻo 100%.
    - Pill Badge [TẬP X] bo tròn capsule sắc nét, màu nhấn thể loại, viền kính mờ tinh tế.
    - Tên phim: Font BeVietnamPro-Black/ExtraBold trắng sáng, đổ bóng Gaussian đa tầng mượt mà, không bóng đen nhòe.
    - Mô tả phim / tập: Font BeVietnamPro-SemiBold màu vàng champagne ánh kim sang trọng, nổi bật và thanh lịch.
    """
    output_png.parent.mkdir(parents=True, exist_ok=True)
    pal = get_genre_palette(genre or title)
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    is_horizontal = width >= height
    cx = width // 2
    dummy_d = ImageDraw.Draw(canvas)
    main, sub = split_title(title)

    y = int(height * 0.048) if is_horizontal else 140
    max_w = int(width * 0.84) if is_horizontal else int(width * 0.88)

    # 1. Pill Badge [TẬP 1], [TẬP 2], [TẬP 3 · KẾT]
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
    pld.text(
        (cx, py + pad_y + th // 2),
        ep_text,
        font=pill_font,
        fill=(255, 255, 255, 255) if (pal["accent"][0] > 100 or pal["accent"][1] < 180) else pal["ink"] + (255,),
        anchor="mm"
    )
    canvas.alpha_composite(pill_layer)

    y = py + ph + (13 if is_horizontal else 16)

    # 2. Tên Phim (Main Title)
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
        tsd.text((cx, cur_y + 3), ln, font=main_font, fill=(0, 0, 0, 160), anchor="ma")
        cur_y += line_h
    title_shadow = title_shadow.filter(ImageFilter.GaussianBlur(5))
    canvas.alpha_composite(title_shadow)

    # Text Tên Phim chính: Trắng sáng tinh khiết + viền vi mảnh 1px chống lóa
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

    # 3. Mô Tả Phim / Tập (Subtitle)
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

        # Màu chữ Subtitle: Vàng champagne sang trọng (#FEF08A / #FDE047)
        sub_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sld = ImageDraw.Draw(sub_layer)
        cur_y = y
        sub_color = (254, 240, 138) if (pal["soft"][0] > 200 and pal["soft"][1] > 200) else pal["soft"]
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

    canvas.save(str(output_png), format="PNG")
    return output_png
