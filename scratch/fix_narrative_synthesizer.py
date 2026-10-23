# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("core/narrative_synthesizer.py")
content = p.read_text(encoding="utf-8")

content = content.replace("from core.stories.romance_nguoctam_masterpiece import get_nguoctam_masterpiece_story", "from core.stories.romance_nguoctam_masterpiece import get_romance_nguoctam_masterpiece_story")
content = content.replace("orig = get_nguoctam_masterpiece_story(title)", "orig = get_romance_nguoctam_masterpiece_story(title)")

content = content.replace("from core.stories.romance_haomon_masterpiece import get_haomon_masterpiece_story", "from core.stories.romance_haomon_masterpiece import get_romance_haomon_masterpiece_story")
content = content.replace("orig = get_haomon_masterpiece_story(title)", "orig = get_romance_haomon_masterpiece_story(title)")

content = content.replace("from core.stories.romance_chualanh_masterpiece import get_chualanh_masterpiece_story", "from core.stories.romance_chualanh_masterpiece import get_romance_chualanh_masterpiece_story")
content = content.replace("orig = get_chualanh_masterpiece_story(title)", "orig = get_romance_chualanh_masterpiece_story(title)")

p.write_text(content, encoding="utf-8")
print("Fixed narrative_synthesizer.py imports successfully.")
