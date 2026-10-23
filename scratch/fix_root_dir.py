from pathlib import Path

p = Path("core/stories/script_quality_gate.py")
content = p.read_text(encoding="utf-8")

old = 'ROOT_DIR = Path(__file__).resolve().parent.parent.parent'
new = '''ROOT_DIR = Path(__file__).parent.parent.parent
if not (ROOT_DIR / "GEMINI.md").exists():
    ROOT_DIR = Path.cwd()'''

content = content.replace(old, new)
p.write_text(content, encoding="utf-8")
print("FIXED ROOT_DIR")
