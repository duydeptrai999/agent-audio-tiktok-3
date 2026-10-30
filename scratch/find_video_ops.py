import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

p = Path(r"C:\Users\duydo\.gemini\antigravity\brain\66659ed1-4141-45bb-b836-ecf4111cc543\.system_generated\logs\transcript.jsonl")
lines = p.read_text(encoding="utf-8").splitlines()
for idx in range(500, 780):
    data = json.loads(lines[idx])
    tc = data.get("tool_calls")
    if tc:
        for t in tc:
            args = str(t.get("args"))
            if any(k in args for k in ["render", "output", ".mp4", "autopilot", "slot"]):
                print(f"Line {idx} Step {data.get('step_index')}: {t.get('name')}({args[:150]})")
