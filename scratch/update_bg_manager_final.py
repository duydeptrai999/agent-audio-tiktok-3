# -*- coding: utf-8 -*-
with open("core/background_manager.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
for line in lines:
    # 1. Imports
    if line.startswith("import json"):
        out.append(line)
        out.append("from typing import List, Dict, Any, Optional\n")
    # 2. Add _collect_all_candidate_pool_files right before register_source_video
    elif line.strip().startswith("def register_source_video("):
        helper = [
            "    def _collect_all_candidate_pool_files(self, genre: str = '') -> List[Path]:\n",
            "        \"\"\"Thu thập danh sách video nền 16:9 từ POOL_DIR (youtube_pool) và raw_downloaded.\"\"\"\n",
            "        pool_files = [\n",
            "            f for f in POOL_DIR.glob('*.mp4')\n",
            "            if f.is_file() and f.stat().st_size > 1000000\n",
            "        ]\n",
            "        raw_dir = ROOT_DIR / 'assets' / 'footage' / 'raw_downloaded'\n",
            "        if raw_dir.exists():\n",
            "            for rf in raw_dir.glob('*.mp4'):\n",
            "                if rf.is_file() and rf.stat().st_size > 15000000:\n",
            "                    pool_files.append(rf)\n",
            "\n",
            "        g_low = (genre or '').lower()\n",
            "        is_dark_genre = any(k in g_low for k in ['kinh dị', 'kinh_di', 'quái đàm', 'quai_dam', 'trinh thám', 'trinh_tham', 'mạt thế', 'mat_the'])\n",
            "        if not is_dark_genre and len(pool_files) > 1:\n",
            "            filtered = [f for f in pool_files if 'tool_restoration' not in f.name.lower()]\n",
            "            if filtered:\n",
            "                pool_files = filtered\n",
            "        return pool_files\n",
            "\n"
        ]
        out.extend(helper)
        out.append(line)
    # 3. rotate_pool_video signature
    elif line.strip() == "def rotate_pool_video(self) -> Optional[Path]:":
        out.append("    def rotate_pool_video(self, genre: str = \"\") -> Optional[Path]:\n")
    elif "pool_files = [" in line and len(out) > 0 and "rotate_pool_video" in "".join(out[-20:]):
        # We replace the pool_files scan in rotate_pool_video
        out.append("        pool_files = self._collect_all_candidate_pool_files(genre=genre)\n")
    elif "f for f in POOL_DIR.glob(\"*.mp4\")" in line and "rotate_pool_video" in "".join(out[-20:]):
        pass  # skip
    elif "if f.is_file() and f.stat().st_size > 1000000" in line and "rotate_pool_video" in "".join(out[-20:]):
        pass  # skip
    elif line.strip() == "]" and "rotate_pool_video" in "".join(out[-20:]) and "self._collect_all_candidate_pool_files" in "".join(out[-5:]):
        pass  # skip
    # 4. get_or_download_active_video signature
    elif line.strip() == "def get_or_download_active_video(self, preferred_url: Optional[str] = None) -> Optional[Path]:":
        out.append("    def get_or_download_active_video(self, preferred_url: Optional[str] = None, genre: str = \"\") -> Optional[Path]:\n")
    elif "rotated = self.rotate_pool_video()" in line:
        out.append("                    rotated = self.rotate_pool_video(genre=genre)\n")
    # 5. get_distinct_slice_for_part signature
    elif "def get_distinct_slice_for_part(" in line:
        out.append(line)
    elif "total_parts: int = 3" in line and "get_distinct_slice_for_part" in "".join(out[-10:]):
        out.append("        total_parts: int = 3,\n")
        out.append("        genre: str = \"\"\n")
    elif "source_path = self.get_or_download_active_video(preferred_url=preferred_url)" in line:
        out.append("        source_path = self.get_or_download_active_video(preferred_url=preferred_url, genre=genre)\n")
    # 6. slice check
    elif "if slice_path.exists() and slice_path.stat().st_size > 500000:" in line:
        out.append(line)
        out.append("            probe_sl = probe_media_file(slice_path)\n")
        out.append("            if probe_sl.get('height', 0) > probe_sl.get('width', 0):\n")
        out.append("                print(f'⚠️ [BackgroundManager] Slice {slice_name} bị dọc (9:16), tự động xóa để cắt lại 16:9...')\n")
        out.append("                slice_path.unlink(missing_ok=True)\n")
        out.append("            else:\n")
    elif "print(f\"🎬 [BackgroundManager] Sử dụng phân đoạn có sẵn: {slice_name}\")" in line:
        out.append("                print(f\"🎬 [BackgroundManager] Sử dụng phân đoạn có sẵn (16:9): {slice_name}\")\n")
    elif "return slice_path" in line and "Sử dụng phân đoạn có sẵn" in "".join(out[-2:]):
        out.append("                return slice_path\n")
    else:
        out.append(line)

with open("core/background_manager.py", "w", encoding="utf-8") as f:
    f.writelines(out)

print("Updated core/background_manager.py cleanly!")
