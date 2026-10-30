# -*- coding: utf-8 -*-
with open("core/cinema_30min_splitter.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("ROOT_DIR = Path(__file__).resolve().parent.parent", "ROOT_DIR = Path.cwd()")

with open("core/cinema_30min_splitter.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated ROOT_DIR to Path.cwd() in cinema_30min_splitter.py")
