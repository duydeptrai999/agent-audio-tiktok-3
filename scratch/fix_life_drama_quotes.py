# -*- coding: utf-8 -*-
with open('core/stories/life_drama.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('!""""', '!"""')
text = text.replace('nhé!""""', 'nhé!"""')
text = text.replace('một mình!""""', 'một mình!"""')

with open('core/stories/life_drama.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Checked quotes in life_drama.py")
