# -*- coding: utf-8 -*-
from pathlib import Path

sg_file = Path("core/script_generator.py")
content = sg_file.read_text(encoding="utf-8")

old_block = """        relevant_cases = consult_data.get("relevant_cases", [])
        hook_template = consult_data.get("recommended_hook_template", OPENING_HOOK_TEMPLATES_6[0])

        blueprint = {
            "title": title,
            "genre_key": genre_key,
            "premise": premise,
            "consultation_token": consult_data.get("consultation_token", ""),
            "benchmark_cases": [c["title"] for c in relevant_cases],
            "hook_strategy": hook_template["type"],
            "chekhov_guns": [
                "Vật chứng 1: Chiếc USB chứa dữ liệu ẩn hoặc bản khế ước chuyển nhượng ngầm",
                "Vật chứng 2: Thói quen dị ứng hoặc camera hành trình giấu kín"
            ],"""

new_block = """        relevant_cases = consult_data.get("relevant_cases", [])
        hook_template = consult_data.get("recommended_hook_template", OPENING_HOOK_TEMPLATES_6[0])

        chekhov_props = []
        for case in relevant_cases:
            props = case.get("tangible_props", [])
            for p in props:
                if p not in chekhov_props:
                    chekhov_props.append(p)
        if not chekhov_props:
            chekhov_props = [
                "Vật chứng 1: Chiếc USB chứa dữ liệu ẩn hoặc bản khế ước chuyển nhượng ngầm",
                "Vật chứng 2: Thói quen dị ứng hoặc camera hành trình giấu kín"
            ]

        benchmark_act_pacing = {}
        if relevant_cases:
            benchmark_act_pacing = relevant_cases[0].get("three_acts_pacing", {})

        blueprint = {
            "title": title,
            "genre_key": genre_key,
            "premise": premise,
            "consultation_token": consult_data.get("consultation_token", ""),
            "benchmark_cases": [c["title"] for c in relevant_cases],
            "benchmark_act_pacing": benchmark_act_pacing,
            "hook_strategy": hook_template["type"],
            "chekhov_guns": chekhov_props,"""

# Normalize line endings for replacement
norm_content = content.replace("\r\n", "\n")
norm_old = old_block.replace("\r\n", "\n")
norm_new = new_block.replace("\r\n", "\n")

if norm_old in norm_content:
    norm_content = norm_content.replace(norm_old, norm_new)
    sg_file.write_text(norm_content, encoding="utf-8")
    print("Successfully upgraded core/script_generator.py with dynamic Chekhov props and benchmark pacing!")
else:
    print("Warning: old_block not found in core/script_generator.py")
