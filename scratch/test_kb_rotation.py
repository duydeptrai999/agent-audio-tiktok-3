import sys, os
sys.path.insert(0, os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')
from core.knowledge_base import get_knowledge_base

kb = get_knowledge_base()
for i in range(4):
    c = kb.consult_before_writing(genre_hint='TRONG_SINH', topic_title=f'Series {i}')
    h = c['recommended_hook_archetype']
    u = c['recommended_character_universe']
    r = c['recommended_resolution']
    print(f"Call {i+1}: Hook={h['archetype_id']} ({h['name'][:30]}) | Univ={u['universe_id']} ({u['name'][:25]}) | Res={r['resolution_id']}")
