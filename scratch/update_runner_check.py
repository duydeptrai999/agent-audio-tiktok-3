# -*- coding: utf-8 -*-
import sys
from pathlib import Path

# Update scripts/run_agent_scriptwriting_cycles_41_to_50.py dialogue check
runner_file = Path("scripts/run_agent_scriptwriting_cycles_41_to_50.py")
runner_text = runner_file.read_text(encoding="utf-8")

old_check = """        long_quotes = [q for q in quote_matches if len(q.split()) > 18]
        if long_quotes:
            flaws.append(f"THOAI_DAI_DONG: Có {len(long_quotes)} câu thoại quá 18 từ, thiếu nhịp dao găm: '{long_quotes[0][:40]}...'")
        else:
            strengths.append(f"THOAI_DAO_GAM: Sở hữu {dialogue_count} câu thoại sắc gọn dưới 16 từ, mang tính công kích và gài bẫy cao.")"""

new_check = """        long_quotes = [s.strip() for q in quote_matches for s in re.split(r'[.!?…\\n]+', q) if len(s.strip().split()) > 16]
        if long_quotes:
            flaws.append(f"THOAI_DAI_DONG: Có {len(long_quotes)} vế thoại quá 16 từ, thiếu nhịp dao găm: '{long_quotes[0][:40]}...'")
        else:
            strengths.append(f"THOAI_DAO_GAM: Sở hữu {dialogue_count} nhịp thoại sắc gọn dưới 14-16 từ, mang tính công kích và gài bẫy cao.")"""

if old_check in runner_text:
    runner_text = runner_text.replace(old_check, new_check)
    runner_file.write_text(runner_text, encoding="utf-8")
    print("Updated dialogue clause check in scripts/run_agent_scriptwriting_cycles_41_to_50.py")
else:
    print("Warning: old_check not found in runner")
