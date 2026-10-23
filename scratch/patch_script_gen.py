from pathlib import Path

p = Path("core/script_generator.py")
content = p.read_text(encoding="utf-8")

old = """        from core.narrative_synthesizer import get_masterpiece_narrative
        return get_masterpiece_narrative(
            genre_key=genre_key,
            custom_title=title,
            voice=voice,
            consult_data=consult_data
        )"""

new = """        from core.narrative_synthesizer import get_masterpiece_narrative
        from core.stories.script_quality_gate import validate_story_series
        raw_story = get_masterpiece_narrative(
            genre_key=genre_key,
            custom_title=title,
            voice=voice,
            consult_data=consult_data
        )
        return validate_story_series(raw_story)"""

norm_content = content.replace("\r\n", "\n")
norm_old = old.replace("\r\n", "\n")
norm_new = new.replace("\r\n", "\n")

if norm_old in norm_content:
    updated = norm_content.replace(norm_old, norm_new, 1)
    p.write_text(updated, encoding="utf-8")
    print("PATCHED SCRIPT GENERATOR WITH VALIDATE_STORY_SERIES!")
else:
    print("OLD NOT FOUND IN SCRIPT GENERATOR")
