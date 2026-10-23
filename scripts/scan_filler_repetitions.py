# -*- coding: utf-8 -*-
import sys
import glob

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

keywords = [
    "Thẩm Băng Tuyết",
    "Ánh đèn chùm pha lê rọi xuống",
    "Gió đêm từ dòng sông Nam Giang",
    "Tôi đã dùng năm năm thanh xuân ngồi tù",
    "Hạnh phúc đích thực không phải là sự trả thù"
]

for f in sorted(glob.glob("core/stories/*.py")):
    try:
        txt = open(f, encoding='utf-8').read()
        matches = []
        for kw in keywords:
            cnt = txt.count(kw)
            if cnt > 1:
                matches.append(f"{kw}: {cnt} lần")
        if matches:
            print(f"{f}:")
            for m in matches:
                print(f"   -> {m}")
    except Exception as e:
        print(f"Error {f}: {e}")
