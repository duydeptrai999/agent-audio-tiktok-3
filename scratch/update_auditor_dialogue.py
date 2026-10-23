with open("scripts/run_agent_scriptwriting_10_cycles.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

target = """        # Check dialogue length
        long_quotes = [q for q in quote_matches if len(q.split()) > 22]
        if long_quotes:
            flaws.append(f"DIALOGUE_EXPOSITION: Có {len(long_quotes)} câu thoại quá dài (> 22 từ), mang tính diễn kịch/thuyết giảng.")
        else:
            strengths.append(f"DIALOGUE_PUNCHY: Có {dialogue_count} câu thoại gãy gọn, giàu tính khiêu khích.")"""

replacement = """        # Check dialogue length & subtext punchiness (Mỗi vế thoại không quá 16 từ)
        long_sentences = [s.strip() for q in quote_matches for s in re.split(r'[.!?…]+', q) if len(s.strip().split()) > 16]
        if long_sentences:
            flaws.append(f"DIALOGUE_EXPOSITION: Có {len(long_sentences)} vế thoại quá dài (> 16 từ), mang tính diễn kịch/thuyết giảng.")
        else:
            strengths.append(f"DIALOGUE_PUNCHY: Có {dialogue_count} câu thoại gãy gọn đanh thép, ngắt nhịp dao găm dưới 12-16 từ.")"""

assert target in text, "Target not found in run_agent_scriptwriting_10_cycles.py"
text = text.replace(target, replacement)

with open("scripts/run_agent_scriptwriting_10_cycles.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Updated dialogue check in run_agent_scriptwriting_10_cycles.py!")
