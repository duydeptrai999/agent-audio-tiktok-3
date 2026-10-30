import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story
from core.stories.script_quality_gate import validate_story_series

story = get_man_tra_thu_masterpiece_story()
print("Validating story series with script_quality_gate...")
try:
    validated = validate_story_series(story)
    print("SUCCESS! Script passed quality gate with flying colors!")
    print(f"Title: {validated['title']}")
    print(f"Parts count: {len(validated['parts'])}")
    for p in validated['parts']:
        print(f"  Part {p['part_number']}: {len(p['full_text'].split())} words")
except Exception as e:
    print(f"FAILED with error: {e}")
