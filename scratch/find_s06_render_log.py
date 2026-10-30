import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for idx, line in enumerate(lines):
    if "s06_slot_06_haomon_part1_final.mp4" in line:
        data = json.loads(line)
        print(f"Line {idx} Step {data.get('step_index')}: {data.get('type')}")
        if data.get("tool_calls"):
            print("  tool_calls:", data.get("tool_calls"))
        if data.get("content"):
            print("  content:", str(data.get("content"))[:300])
