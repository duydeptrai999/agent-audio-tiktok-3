# -*- coding: utf-8 -*-
with open("core/background_manager.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace any multi-\r
t_clean = text.replace("\r\r\n", "\n").replace("\r\n", "\n")

# Ensure typing imports
if "from typing import" in t_clean:
    import re
    t_clean = re.sub(r'from typing import [^\n]+', 'from typing import List, Dict, Any, Optional', t_clean)
else:
    t_clean = "from typing import List, Dict, Any, Optional\n" + t_clean

with open("core/background_manager.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(t_clean)

print("Cleaned core/background_manager.py line endings and typing imports!")
