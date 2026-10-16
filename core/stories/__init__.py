# -*- coding: utf-8 -*-
"""
core/stories package
Kho tàng kịch bản truyện audio 30 phút chia 3 tập (chuẩn 10+ phút / tập, >= 1,500 từ / tập).
Đa dạng thể loại:
- Tâm linh / Kinh dị (horror.py)
- Trinh thám / Đấu trí (detective.py)
- Ngôn tình / Hào môn (romance.py)
- Đời sống / Gia đình / Drama (life_drama.py)
- Doraemon / Viễn tưởng / Kỳ bí (doraemon.py)
"""

from core.stories.horror import get_30min_horror_story
from core.stories.detective import get_30min_detective_story
from core.stories.romance import get_30min_romance_story
from core.stories.life_drama import get_30min_life_drama_story
from core.stories.doraemon import get_30min_doraemon_mystery_story

__all__ = [
    "get_30min_horror_story",
    "get_30min_detective_story",
    "get_30min_romance_story",
    "get_30min_life_drama_story",
    "get_30min_doraemon_mystery_story",
]
