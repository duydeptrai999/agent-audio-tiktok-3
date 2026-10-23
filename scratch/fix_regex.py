with open("core/stories/script_quality_gate.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "pattern = r" in line and "“" in line:
        new_lines.append('    pattern = r"[\'\\"\u201c]([^\'\\"\u201d\\n]+)[\'\\"\u201d]"\n')
    else:
        new_lines.append(line)

with open("core/stories/script_quality_gate.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.writelines(new_lines)

print("Fixed regex cleanly!")
