# -*- coding: utf-8 -*-
with open('core/stories/life_divorce.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any quadruple quotes or unbalanced quote patterns
text = text.replace('!""""', '!"""')
text = text.replace('!""\'""', '!"""')
text = text.replace('còn!""""', 'còn!"""')
text = text.replace('lập tức!"\'""', 'lập tức!"""')

with open('core/stories/life_divorce.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed life_divorce.py quotes!")
