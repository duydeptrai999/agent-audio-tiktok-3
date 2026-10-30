import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for l in [36, 271, 548]:
    data = json.loads(lines[l])
    print(f"=== Line {l} ===")
    print(str(data.get("content"))[:400])
