import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for idx, line in enumerate(lines):
    if idx < 550 and any(k in line for k in ["s06", "slot_06"]):
        data = json.loads(line)
        print(f"Line {idx} Step {data.get('step_index')}: {data.get('type')}")
        if data.get("tool_calls"):
            print("  tool_calls:", [t.get("name") for t in data.get("tool_calls")])
            for t in data.get("tool_calls"):
                print("    ", str(t.get("args"))[:200])
