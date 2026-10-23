import sys
from pathlib import Path

# Add project root to path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_11_to_20_masterpieces import (
    get_story_cycle_11, get_story_cycle_12, get_story_cycle_13, get_story_cycle_14, get_story_cycle_15,
    get_story_cycle_16, get_story_cycle_17, get_story_cycle_18, get_story_cycle_19, get_story_cycle_20
)
from core.stories.cycles_21_to_30_masterpieces import (
    get_story_cycle_21, get_story_cycle_22, get_story_cycle_23, get_story_cycle_24, get_story_cycle_25,
    get_story_cycle_26, get_story_cycle_27, get_story_cycle_28, get_story_cycle_29, get_story_cycle_30
)
from core.stories.cycles_31_to_40_masterpieces import (
    get_story_cycle_31, get_story_cycle_32, get_story_cycle_33, get_story_cycle_34, get_story_cycle_35,
    get_story_cycle_36, get_story_cycle_37, get_story_cycle_38, get_story_cycle_39, get_story_cycle_40
)
from core.stories.cycles_41_to_50_masterpieces import (
    get_story_cycle_41, get_story_cycle_42, get_story_cycle_43, get_story_cycle_44, get_story_cycle_45,
    get_story_cycle_46, get_story_cycle_47, get_story_cycle_48, get_story_cycle_49, get_story_cycle_50
)
from core.stories.script_quality_gate import (
    calculate_title_similarity,
    calculate_hook_similarity,
    calculate_jaccard_similarity,
    detect_resolution_mechanism,
    detect_opening_syntax_archetype,
    extract_hook_snippet,
    extract_story_full_text
)

stories = []
for i in range(11, 21):
    fn = globals()[f"get_story_cycle_{i}"]
    stories.append((i, fn()))
for i in range(21, 31):
    fn = globals()[f"get_story_cycle_{i}"]
    stories.append((i, fn()))
for i in range(31, 41):
    fn = globals()[f"get_story_cycle_{i}"]
    stories.append((i, fn()))
for i in range(41, 51):
    fn = globals()[f"get_story_cycle_{i}"]
    stories.append((i, fn()))

print(f"Loaded {len(stories)} stories (Cycles 11 to 50). Total pairs: {len(stories)*(len(stories)-1)//2}")

# Check duplicates and clashes
title_clashes = []
hook_clashes = []
jaccard_clashes = []
resolutions = {}
hooks = {}

for num, s in stories:
    title = s.get("title", "")
    hook = extract_hook_snippet(s)
    full_text = extract_story_full_text(s)
    arch = detect_opening_syntax_archetype(hook)
    res = detect_resolution_mechanism(full_text)
    resolutions[num] = res
    hooks[num] = (hook, arch)

for i in range(len(stories)):
    num1, s1 = stories[i]
    t1 = s1.get("title", "")
    h1 = extract_hook_snippet(s1)
    txt1 = extract_story_full_text(s1)
    
    for j in range(i + 1, len(stories)):
        num2, s2 = stories[j]
        t2 = s2.get("title", "")
        h2 = extract_hook_snippet(s2)
        txt2 = extract_story_full_text(s2)
        
        # 1. Title Similarity
        sim_title = calculate_title_similarity(t1, t2)
        if sim_title >= 0.35:
            title_clashes.append((num1, num2, sim_title, t1, t2))
            
        # 2. Hook Overlap
        sim_hook = calculate_hook_similarity(h1, h2)
        if sim_hook >= 0.30:
            hook_clashes.append((num1, num2, sim_hook, h1, h2))
            
        # 3. Jaccard Text Similarity
        sim_jac = calculate_jaccard_similarity(txt1, txt2)
        if sim_jac >= 0.25:
            jaccard_clashes.append((num1, num2, sim_jac))

print("\n=== SCAN RESULTS ===")
print(f"Title Clashes (>= 0.35): {len(title_clashes)}")
for c in title_clashes:
    print(f"  Cycle {c[0]} vs {c[1]}: {c[2]:.1%} | '{c[3]}' vs '{c[4]}'")

print(f"\nHook Clashes (>= 0.30): {len(hook_clashes)}")
for c in hook_clashes:
    print(f"  Cycle {c[0]} vs {c[1]}: {c[2]:.1%}\n    H1: {c[3]}\n    H2: {c[4]}")

print(f"\nJaccard Clashes (>= 0.25): {len(jaccard_clashes)}")
for c in jaccard_clashes:
    print(f"  Cycle {c[0]} vs {c[1]}: {c[2]:.1%}")

print(f"\nUnique Resolutions Detected: {len(set(resolutions.values()))}")
from collections import Counter
print("Resolution breakdown:", Counter(resolutions.values()))
