# -*- coding: utf-8 -*-
with open('core/stories/sa_dieu_tieng_long_masterpiece.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('!""""', '!"""')
text = text.replace('bật!""""', 'bật!"""')
text = text.replace('biểu!""""', 'biểu!"""')
text = text.replace('tôi!""""', 'tôi!"""')

with open('core/stories/sa_dieu_tieng_long_masterpiece.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed quotes in sa_dieu_tieng_long_masterpiece.py!")
