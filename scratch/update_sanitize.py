# -*- coding: utf-8 -*-
with open('core/audio_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        "chửi rủa": "mắng mỏ",
        "Chửi rủa": "Mắng mỏ",
    }"""

replacement = """        "chửi rủa": "mắng mỏ",
        "Chửi rủa": "Mắng mỏ",
        "trả thù": "đáp trả",
        "Trả thù": "Đáp trả",
        "bẩn thỉu": "xấu xa",
        "Bẩn thỉu": "Xấu xa",
        "thiêu đốt da thịt": "lạnh buốt tâm can",
        "Thiêu đốt da thịt": "Lạnh buốt tâm can",
        "thiêu đốt": "áp đảo",
        "Thiêu đốt": "Áp đảo",
        "giết người": "hại người",
        "Giết người": "Hại người",
        "chết chóc": "tang thương",
        "Chết chóc": "Tang thương",
    }"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/audio_engine.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated sanitize_tts_text in core/audio_engine.py!")
else:
    print("TARGET NOT FOUND in core/audio_engine.py")
