from pathlib import Path

p = Path("config/settings.py")
content = p.read_text(encoding="utf-8")
content = content.replace("DUCKING_THRESHOLD = 0.12", "DUCKING_THRESHOLD = 0.079")
content = content.replace("DUCKING_RATIO = 2.0", "DUCKING_RATIO = 4.0")
content = content.replace("DUCKING_KNEE = 2.0", "DUCKING_KNEE = 2.5")
p.write_text(content, encoding="utf-8")
print("HARMONIZED DUCKING SETTINGS")
