# -*- coding: utf-8 -*-
with open('core/stories/school_romance_vungtrom_masterpiece.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace p1_fill = " with p1_fill = \"\"\"
text = text.replace('p1_fill = "Trong những', 'p1_fill = """Trong những')
text = text.replace('chưa một lần dám cất lên thành lời."', 'chưa một lần dám cất lên thành lời."""')

with open('core/stories/school_romance_vungtrom_masterpiece.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed p1_fill triple quotes!")
