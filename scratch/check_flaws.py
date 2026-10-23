import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.run_agent_scriptwriting_10_cycles import run_full_10_cycle_agent_audit

data = run_full_10_cycle_agent_audit()
print("\n" + "="*80)
print("CHI TIẾT LỖI TỪNG VÒNG:")
print("="*80)
for d in data:
    print(f"Vòng {d['cycle']} ({d['genre']}) - Điểm: {d['score']}/10:")
    for f in d['flaws']:
        print(f"  - {f}")
