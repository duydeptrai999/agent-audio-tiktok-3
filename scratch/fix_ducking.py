from pathlib import Path

p = Path("config/settings.py")
content = p.read_text(encoding="utf-8")
content = content.replace("DUCKING_RELEASE_MS = 350", "DUCKING_RELEASE_MS = 750")
p.write_text(content, encoding="utf-8")
print("FIXED DUCKING_RELEASE_MS")
