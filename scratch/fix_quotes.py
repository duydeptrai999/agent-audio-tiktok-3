# -*- coding: utf-8 -*-
with open('core/stories/life_mother_in_law.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace 4 double quotes with 3 double quotes
text = text.replace('!""""', '!"""')
with open('core/stories/life_mother_in_law.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed quadruple quotes successfully!")
