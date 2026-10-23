# -*- coding: utf-8 -*-
"""
scratch/upgrade_knowledge_base.py
Nâng cấp toàn diện core/knowledge_base.py:
1. Indexing & Matching đa chiều trên toàn bộ 100 tác phẩm kinh điển.
2. Trích xuất đầy đủ 8 trường cốt lõi: Đạo cụ hữu hình, Nhịp điệu 3 hồi, Cú twist, Điểm sảng, Takeaways.
3. Hỗ trợ các API tra cứu chuyên sâu: get_story_by_id, get_stories_by_genre, search_stories_by_keyword.
4. Định dạng Prompt chỉ thị toàn diện (Writer's Directive Bible).
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB_PATH = ROOT / "core" / "knowledge_base.py"

content = KB_PATH.read_text(encoding="utf-8")

# 1. Thay đổi logic trong query_masterclass: scoring và brief_cases
old_search_scoring = """        # 2. Chấm điểm tương đồng cho các tác phẩm trong các nhóm ưu tiên
        scored_stories = []
        for s in self._all_stories:
            score = 0
            if s["genre_key"] in target_genre_keys:
                score += 10
            
            # Khớp từ khóa cụ thể trong tên và premise
            search_blob = f"{s['title_vn']} {s['premise']} {s['genre']}".lower()
            tokens = [t for t in re.split(r"\\W+", text_corpus) if len(t) >= 2]
            for token in tokens:
                if token in search_blob:
                    score += 2

            scored_stories.append((score, s))

        # Sắp xếp giảm dần theo điểm
        scored_stories.sort(key=lambda x: x[0], reverse=True)
        top_cases = [item[1] for item in scored_stories[:top_k]]

        # 3. Tạo bản tóm tắt chỉ dẫn biên kịch (Scriptwriting Guidance Brief)
        brief_cases = []
        for c in top_cases:
            brief_cases.append({
                "id": c["id"],
                "title": f"《{c['title_vn']}》({c['title_cn']})",
                "author": c["author_platform"],
                "genre": c["genre"],
                "premise": c["premise"],
                "character_setup": c["characters"],
                "sample_hook_5s": c["golden_hook"],
                "plot_twist_essence": c["plot_twist"],
                "key_takeaways": c["core_lessons"]
            })"""

new_search_scoring = """        # 2. Chấm điểm tương đồng đa chiều cho các tác phẩm
        scored_stories = []
        for s in self._all_stories:
            score = 0
            if s.get("genre_key") in target_genre_keys:
                score += 15

            # Khớp từ khóa cụ thể trong nhiều trường giàu thông tin
            search_blob = f"{s.get('title_vi', '')} {s.get('title_vn', '')} {s.get('title_cn', '')} {s.get('premise', '')} {s.get('genre', '')} {s.get('category', '')} {s.get('plot_twist', '')} {str(s.get('characters', ''))} {str(s.get('mastery_takeaways', ''))}".lower()
            tokens = [t for t in re.split(r"\\W+", text_corpus) if len(t) >= 2]
            for token in tokens:
                if token in search_blob:
                    score += 3

            scored_stories.append((score, s))

        # Sắp xếp giảm dần theo điểm
        scored_stories.sort(key=lambda x: x[0], reverse=True)
        top_cases = [item[1] for item in scored_stories[:top_k]]

        # 3. Tạo bản tóm tắt chỉ dẫn biên kịch chuyên sâu (Scriptwriting Guidance Brief)
        brief_cases = []
        for c in top_cases:
            # Chuẩn hóa danh sách bài học cốt lõi
            takeaways = c.get("mastery_takeaways") or c.get("core_lessons") or []
            if isinstance(takeaways, list):
                takeaways_str = "\\n".join(f" - {t}" for t in takeaways)
            else:
                takeaways_str = str(takeaways)

            # Chuẩn hóa nhịp điệu 3 hồi
            act_struct = c.get("act_structure") or c.get("three_acts_pacing") or {}
            if isinstance(act_struct, dict):
                act_str = f"Hồi 1: {act_struct.get('act_1', '')}\\nHồi 2: {act_struct.get('act_2', '')}\\nHồi 3: {act_struct.get('act_3', '')}"
            elif isinstance(act_struct, str):
                act_str = act_struct
            else:
                act_str = str(c.get("acts_and_pacing", ""))

            # Chuẩn hóa thiết kế nhân vật
            chars = c.get("characters") or c.get("character_design") or ""
            if isinstance(chars, list):
                chars_str = "\\n".join(f" * {ch}" for ch in chars)
            else:
                chars_str = str(chars)

            # Trích xuất đạo cụ hữu hình / mỏ neo giác quan
            tangible_props = c.get("tangible_props") or []
            if not tangible_props and isinstance(chars, list):
                props_found = []
                for ch in chars:
                    if "Mỏ neo:" in ch:
                        props_found.append(ch.split("Mỏ neo:")[1].strip())
                tangible_props = props_found

            brief_cases.append({
                "id": c.get("id"),
                "title": f"《{c.get('title_vi', c.get('title_vn', ''))}》({c.get('title_cn', '')})",
                "title_vi": c.get("title_vi", c.get("title_vn", "")),
                "title_cn": c.get("title_cn", ""),
                "author": c.get("author_platform") or f"{c.get('author', '')} - {c.get('platform', '')}",
                "genre": c.get("genre") or c.get("category", ""),
                "premise": c.get("premise", ""),
                "character_setup": chars_str,
                "tangible_props": tangible_props,
                "three_acts_pacing": act_str,
                "act_structure": act_struct,
                "sample_hook_3s": c.get("hook_3s") or c.get("golden_hook", ""),
                "sample_hook_5s": c.get("hook_3s") or c.get("golden_hook", ""),
                "plot_twist_essence": c.get("climax_twist") or c.get("plot_twist", ""),
                "shuangdian_formula": c.get("shuangdian_formula", ""),
                "key_takeaways": takeaways_str,
                "raw_takeaways": takeaways
            })"""

if old_search_scoring in content:
    content = content.replace(old_search_scoring, new_search_scoring)
    print("-> Da thay the search scoring & brief_cases thanh cong!")
else:
    print("-> WARN: Khong tim thay old_search_scoring exact match, thu chuan hoa CRLF/LF...")
    content_norm = content.replace("\r\n", "\n")
    old_norm = old_search_scoring.replace("\r\n", "\n")
    new_norm = new_search_scoring.replace("\r\n", "\n")
    if old_norm in content_norm:
        content = content_norm.replace(old_norm, new_norm)
        print("-> Da thay the search scoring & brief_cases qua ban chuan hoa LF!")
    else:
        print("-> ERROR: Khong tim thay doan code scoring can sua!")
        sys.exit(1)

# 2. Thay đổi format_brief_for_prompt
old_format = """        for idx, c in enumerate(brief.get("relevant_cases", []), 1):
            lines.append(f"\\n--- CASE STUDY THAM CHIẾU #{idx}: {c['title']} ---")
            lines.append(f" * Nguồn & Tác giả: {c['author']} | Thể loại: {c['genre']}")
            lines.append(f" * Tiền đề nghịch lý: {c['premise']}")
            lines.append(f" * Tạo hình nhân vật mẫu:\\n{c['character_setup']}")
            lines.append(f" * Hook mở màn 5s mẫu: {c['sample_hook_5s']}")
            lines.append(f" * Màn bẻ lái Plot Twist mẫu: {c['plot_twist_essence']}")
            lines.append(f" * Tinh hoa cần áp dụng:\\n{c['key_takeaways']}")"""

new_format = """        for idx, c in enumerate(brief.get("relevant_cases", []), 1):
            lines.append(f"\\n--- CASE STUDY THAM CHIẾU #{idx}: {c['title']} ---")
            lines.append(f" * Nguồn & Tác giả: {c['author']} | Thể loại: {c['genre']}")
            lines.append(f" * Tiền đề nghịch lý: {c['premise']}")
            if c.get("tangible_props"):
                props_display = ", ".join(c["tangible_props"]) if isinstance(c["tangible_props"], list) else str(c["tangible_props"])
                lines.append(f" * Đạo cụ / Vật chứng hữu hình: {props_display}")
            lines.append(f" * Tạo hình nhân vật mẫu:\\n{c['character_setup']}")
            lines.append(f" * Hook mở màn 3s mẫu: {c.get('sample_hook_3s', c.get('sample_hook_5s', ''))}")
            if c.get("three_acts_pacing"):
                lines.append(f" * Nhịp điệu 3 hồi tham chiếu:\\n{c['three_acts_pacing']}")
            lines.append(f" * Màn bẻ lái Plot Twist mẫu: {c['plot_twist_essence']}")
            if c.get("shuangdian_formula"):
                lines.append(f" * Công thức Điểm Sảng: {c['shuangdian_formula']}")
            lines.append(f" * Tinh hoa cần áp dụng:\\n{c['key_takeaways']}")"""

content_norm = content.replace("\r\n", "\n")
old_format_norm = old_format.replace("\r\n", "\n")
new_format_norm = new_format.replace("\r\n", "\n")

if old_format_norm in content_norm:
    content_norm = content_norm.replace(old_format_norm, new_format_norm)
    print("-> Da thay the format_brief_for_prompt thanh cong!")
else:
    print("-> ERROR: Khong tim thay old_format can sua!")
    sys.exit(1)

# 3. Bo sung cac ham tra cuu vao class ChineseStoryKnowledgeBase
helper_methods = """
    def get_story_by_id(self, story_id: Any) -> Optional[Dict[str, Any]]:
        \"\"\"Tra cứu chi tiết 1 tác phẩm theo ID (ví dụ '001', 1, 1001).\"\"\"
        s_id = str(story_id).zfill(3) if str(story_id).isdigit() and len(str(story_id)) <= 3 else str(story_id)
        for s in self._all_stories:
            if str(s.get("id")) == str(story_id) or str(s.get("id")) == s_id:
                return s
        return None

    def get_stories_by_genre(self, genre_key: str) -> List[Dict[str, Any]]:
        \"\"\"Lấy danh sách toàn bộ tác phẩm thuộc một nhóm thể loại.\"\"\"
        g = genre_key.upper().strip()
        return self._genre_map.get(g, [])

    def search_stories_by_keyword(self, keyword: str, top_k: int = 5) -> List[Dict[str, Any]]:
        \"\"\"Tìm kiếm tác phẩm theo từ khóa bất kỳ trên toàn bộ kho tàng tri thức.\"\"\"
        kw = keyword.lower().strip()
        matches = []
        for s in self._all_stories:
            blob = f"{s.get('title_vi', '')} {s.get('title_vn', '')} {s.get('title_cn', '')} {s.get('premise', '')} {s.get('genre', '')} {str(s.get('characters', ''))} {str(s.get('tangible_props', ''))}".lower()
            if kw in blob:
                matches.append(s)
        return matches[:top_k]

    def get_benchmark_case(self, topic_title: str, genre_hint: str = "") -> Dict[str, Any]:
        \"\"\"Lấy nhanh case study hình mẫu xuất sắc nhất cho một đề tài.\"\"\"
        brief = self.query_masterclass(topic_title=topic_title, genre_hint=genre_hint, top_k=1)
        cases = brief.get("relevant_cases", [])
        return cases[0] if cases else {}
"""

class_end_marker = "    def format_brief_for_prompt"
if class_end_marker in content_norm:
    content_norm = content_norm.replace(class_end_marker, helper_methods + "\n    def format_brief_for_prompt")
    print("-> Da bo sung cac ham tra cuu helper vao class ChineseStoryKnowledgeBase!")
else:
    print("-> ERROR: Khong tim thay marker format_brief_for_prompt!")
    sys.exit(1)

KB_PATH.write_text(content_norm, encoding="utf-8")
print(" Hoan tat nang cap core/knowledge_base.py!")
