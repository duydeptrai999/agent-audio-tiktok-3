import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/viral_full_100_cases.json', 'r', encoding='utf-8') as f:
    cases = json.load(f)

print(f"Total: {len(cases)} items")

# Group by genre/theme based on keywords
themes = {
    "Vả Mặt / Báo Thù / Trà Xanh": [],
    "Mẹ Chồng Nàng Dâu / Gia Đấu": [],
    "Trọng Sinh / Tái Sinh / Hoán Đổi": [],
    "Thật Giả Thiên Kim / Hào Môn": [],
    "Kỳ Án / Trinh Thám / Tâm Lý Tội Phạm": [],
    "Kinh Dị / Quái Đàm / Ma Mị": [],
    "Thanh Xuân / Vườn Trường / Hài Hước (Sa điêu)": [],
    "Khác": []
}

for c in cases:
    t = c.get('title', '')
    desc = c.get('description', '')
    full = (t + " " + desc).lower()
    
    if any(k in full for k in ["trà xanh", "vả mặt", "báo thù", "trừng trị", "hối hận", "hạ bệ"]):
        themes["Vả Mặt / Báo Thù / Trà Xanh"].append(c)
    elif any(k in full for k in ["mẹ chồng", "nàng dâu", "nhà chồng", "hầu phủ", "chồng", "ly hôn"]):
        themes["Mẹ Chồng Nàng Dâu / Gia Đấu"].append(c)
    elif any(k in full for k in ["trọng sinh", "tái sinh", "trùng sinh", "sống lại", "xuyên"]):
        themes["Trọng Sinh / Tái Sinh / Hoán Đổi"].append(c)
    elif any(k in full for k in ["thiên kim", "hào môn", "tổng tài", "thái tử", "phú bà"]):
        themes["Thật Giả Thiên Kim / Hào Môn"].append(c)
    elif any(k in full for k in ["trinh thám", "kỳ án", "pháp y", "tội phạm", "phân xác", "vụ án"]):
        themes["Kỳ Án / Trinh Thám / Tâm Lý Tội Phạm"].append(c)
    elif any(k in full for k in ["kinh dị", "quái đản", "lễ tang", "mùi xác", "ma", "quỷ"]):
        themes["Kinh Dị / Quái Đàm / Ma Mị"].append(c)
    elif any(k in full for k in ["học bá", "sa điêu", "tiếng lòng", "hài", "thanh xuân", "bạn thân"]):
        themes["Thanh Xuân / Vườn Trường / Hài Hước (Sa điêu)"].append(c)
    else:
        themes["Khác"].append(c)

for theme, items in themes.items():
    print(f"\n=== {theme.upper()} ({len(items)} videos) ===")
    for item in items[:6]:
        print(f" - {item.get('title')}")
