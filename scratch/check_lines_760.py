import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for idx in range(760, 785):
    if idx < len(lines):
        data = json.loads(lines[idx])
        tc = data.get("tool_calls")
        if tc:
            for t in tc:
                print(f"Line {idx}: {t.get('name')}: {str(t.get('args'))[:200]}")
        if data.get("content"):
            print(f"Line {idx} content: {str(data.get('content'))[:300]}")
