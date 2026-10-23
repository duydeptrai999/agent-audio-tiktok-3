import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.daily_story_factory import SLOT_STORY_LOADERS
from core.stories.script_quality_gate import validate_story_series

for slot, loader in SLOT_STORY_LOADERS.items():
    story = loader()
    validated = validate_story_series(story)
    title = validated.get("title", "")
    passed = validated.get("quality_audit_passed", False)
    distinct = validated.get("distinctiveness_passed", False)
    print(f"Slot {slot:02d}: {title[:35]} | Quality Passed: {passed} | Distinct: {distinct}")
