# -*- coding: utf-8 -*-
with open("core/knowledge_base.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

target = """        # 4. CHỐNG ĐỒNG HÓA & LỰA CHỌN ĐỘC BẢN (ANTI-HOMOGENIZATION ENGINE):
        # A. Chọn Hook Archetype (Ưu tiên thể loại, loại trừ các ID đã dùng gần đây)
        exclude_archetypes = exclude_archetype_ids or []
        compatible_hooks = [h for h in DIVERSE_HOOK_ARCHETYPES_10 if any(gk in h["best_for"] for gk in target_genre_keys)]
        if not compatible_hooks:
            compatible_hooks = DIVERSE_HOOK_ARCHETYPES_10

        fresh_hooks = [h for h in compatible_hooks if h["archetype_id"] not in exclude_archetypes]
        matched_hook_archetype = fresh_hooks[0] if fresh_hooks else compatible_hooks[0]

        # B. Chọn Vũ Trụ Nhân Vật (10 Character Universes, loại trừ ID đã dùng gần đây)
        exclude_universes = exclude_universe_ids or []
        compatible_universes = [u for u in CHARACTER_UNIVERSES_10 if any(gk in u.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_universes:
            compatible_universes = CHARACTER_UNIVERSES_10
        fresh_universes = [u for u in compatible_universes if u["universe_id"] not in exclude_universes]
        matched_universe = fresh_universes[0] if fresh_universes else compatible_universes[0]

        # C. Chọn Cơ Chế Lật Kèo Độc Bản (10 Diverse Resolutions)
        exclude_res = exclude_resolution_ids or []
        compatible_res = [r for r in DIVERSE_RESOLUTIONS_10 if any(gk in r.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_res:
            compatible_res = DIVERSE_RESOLUTIONS_10
        fresh_res = [r for r in compatible_res if r["resolution_id"] not in exclude_res]
        matched_resolution = fresh_res[0] if fresh_res else compatible_res[0]"""

replacement = """        # 4. CHỐNG ĐỒNG HÓA & LỰA CHỌN ĐỘC BẢN (ANTI-HOMOGENIZATION ENGINE):
        def _pick_least_recently_used(candidates: List[Dict[str, Any]], recent_ids: List[int], id_key: str) -> Dict[str, Any]:
            if not candidates:
                return {}
            def _lru_score(item: Dict[str, Any]) -> float:
                iid = item.get(id_key)
                if not recent_ids or iid not in recent_ids:
                    return float("inf")
                rev = list(reversed(recent_ids))
                return float(rev.index(iid)) if iid in rev else float("inf")
            return sorted(candidates, key=_lru_score, reverse=True)[0]

        # A. Chọn Hook Archetype (Ưu tiên thể loại, xoay vòng theo LRU)
        compatible_hooks = [h for h in DIVERSE_HOOK_ARCHETYPES_10 if any(gk in h["best_for"] for gk in target_genre_keys)]
        if not compatible_hooks:
            compatible_hooks = DIVERSE_HOOK_ARCHETYPES_10
        matched_hook_archetype = _pick_least_recently_used(compatible_hooks, exclude_archetype_ids or [], "archetype_id")

        # B. Chọn Vũ Trụ Nhân Vật (10 Character Universes, xoay vòng theo LRU)
        compatible_universes = [u for u in CHARACTER_UNIVERSES_10 if any(gk in u.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_universes:
            compatible_universes = CHARACTER_UNIVERSES_10
        matched_universe = _pick_least_recently_used(compatible_universes, exclude_universe_ids or [], "universe_id")

        # C. Chọn Cơ Chế Lật Kèo Độc Bản (10 Diverse Resolutions, xoay vòng theo LRU)
        compatible_res = [r for r in DIVERSE_RESOLUTIONS_10 if any(gk in r.get("best_for", []) for gk in target_genre_keys)]
        if not compatible_res:
            compatible_res = DIVERSE_RESOLUTIONS_10
        matched_resolution = _pick_least_recently_used(compatible_res, exclude_resolution_ids or [], "resolution_id")"""

assert target in text, "Target not found in knowledge_base.py!"
text = text.replace(target, replacement)

with open("core/knowledge_base.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully updated with LRU anti-homogenization picker!")
