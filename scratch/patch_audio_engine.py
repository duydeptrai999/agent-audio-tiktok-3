from pathlib import Path

p = Path("core/audio_engine.py")
content = p.read_text(encoding="utf-8")

target = """    if target_speed is None:
        try:
            from config.settings import VOICE_SPEED_MULTIPLIER
            target_speed = float(VOICE_SPEED_MULTIPLIER)
        except Exception:
            target_speed = 1.15"""

replacement = """    if target_speed is None:
        try:
            from config.settings import VOICE_SPEED_MULTIPLIER
            target_speed = float(VOICE_SPEED_MULTIPLIER)
        except Exception:
            target_speed = 1.15

    # BẮT BUỘC: Đọc kinh nghiệm từ GEMINI.md & 5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md trước khi làm audio
    try:
        from core.stories.script_quality_gate import require_preflight_experience, audit_and_optimize_part_text
        require_preflight_experience()
        text, _ = audit_and_optimize_part_text(text, title="PreAudioTTS", part_num=1)
    except Exception as e:
        logger.warning(f"Lỗi kiểm tra preflight experience: {e}")"""

# Normalize \r\n to \n for replacement
norm_content = content.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_replacement = replacement.replace("\r\n", "\n")

if norm_target in norm_content:
    updated = norm_content.replace(norm_target, norm_replacement, 1)
    p.write_text(updated, encoding="utf-8")
    print("PATCH SUCCESSFUL")
else:
    print("TARGET NOT FOUND IN NORM CONTENT")
