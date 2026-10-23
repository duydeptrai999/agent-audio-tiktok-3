# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT_DIR = Path.cwd()
sys.path.insert(0, str(ROOT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from scripts.run_agent_scriptwriting_10_cycles import run_full_10_cycle_agent_audit
data = run_full_10_cycle_agent_audit()
print("\n" + "=" * 50)
print("CHI TIET CAC LOI CON TON TAI:")
for d in data:
    print(f"Vong {d['cycle']} ({d['genre']}): flaws={d['flaws']}")
