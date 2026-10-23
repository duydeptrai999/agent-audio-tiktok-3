from pathlib import Path

p = Path("scripts/run_agent_scriptwriting_5_cycles.py")
content = p.read_text(encoding="utf-8")
content = content.replace("ROOT_DIR = Path(__file__).resolve().parent.parent", """ROOT_DIR = Path(__file__).parent.parent
if not (ROOT_DIR / "GEMINI.md").exists():
    ROOT_DIR = Path.cwd()""")
p.write_text(content, encoding="utf-8")
print("FIXED ROOT_DIR IN SCRIPT AUDITOR")
