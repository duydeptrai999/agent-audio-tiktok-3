import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

for name in ["VID_20261027_s06_slot_06_haomon.json", "VID_20261027_s07_slot_07_giadau.json"]:
    p = Path("data/generated_scripts") / name
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        print("File:", name)
        print("  title:", d.get("title"))
        print("  genre:", d.get("genre"))
        print("  voice:", d.get("voice"))
        print("  bgm_genre:", d.get("bgm_genre"))
        print("  parts count:", len(d.get("parts", [])))
        for pt in d.get("parts", []):
            print(f"    Part {pt.get('part_number')}: {pt.get('badge_label')} - len words: {len(pt.get('text', '').split())}")
