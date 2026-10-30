import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for idx, line in enumerate(lines):
    data = json.loads(line)
    if data.get("type") == "USER_INPUT":
        c = str(data.get("content"))[:120].replace("\n", " ")
        print(f"Line {idx} Step {data.get('step_index')}: USER: {c}")
