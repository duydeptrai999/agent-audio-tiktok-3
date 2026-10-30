# -*- coding: utf-8 -*-
with open("core/background_manager.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

helper_method = """    def _collect_all_candidate_pool_files(self, genre: str = "") -> List[Path]:
        \"\"\"Thu thập danh sách video nền 16:9 từ POOL_DIR (youtube_pool) và raw_downloaded, lọc theo tâm lý thể loại.\"\"\"
        pool_files = [
            f for f in POOL_DIR.glob("*.mp4")
            if f.is_file() and f.stat().st_size > 1000000
        ]
        raw_dir = ROOT_DIR / "assets" / "footage" / "raw_downloaded"
        if raw_dir.exists():
            for rf in raw_dir.glob("*.mp4"):
                if rf.is_file() and rf.stat().st_size > 15000000:
                    pool_files.append(rf)

        g_low = (genre or "").lower()
        is_dark_genre = any(k in g_low for k in ["kinh dị", "kinh_di", "quái đàm", "quai_dam", "trinh thám", "trinh_tham", "mạt thế", "mat_the"])
        if not is_dark_genre and len(pool_files) > 1:
            filtered = [f for f in pool_files if "tool_restoration" not in f.name.lower()]
            if filtered:
                pool_files = filtered

        return pool_files
"""

# Insert _collect_all_candidate_pool_files before register_source_video
old_reg = "    def register_source_video("
assert old_reg in t_norm, "old_reg not found"
t_norm = t_norm.replace(old_reg, helper_method + "\n" + old_reg)

# Update rotate_pool_video signature and implementation
old_rot = """    def rotate_pool_video(self) -> Optional[Path]:"""
new_rot = """    def rotate_pool_video(self, genre: str = "") -> Optional[Path]:"""
t_norm = t_norm.replace(old_rot, new_rot)

old_pool_scan = """        # Quét kiểm tra tất cả video có sẵn trong POOL_DIR (> 1MB)
        pool_files = [
            f for f in POOL_DIR.glob("*.mp4")
            if f.is_file() and f.stat().st_size > 1000000
        ]"""
new_pool_scan = """        pool_files = self._collect_all_candidate_pool_files(genre=genre)"""
t_norm = t_norm.replace(old_pool_scan, new_pool_scan)

# Update get_or_download_active_video signature and call
old_god = """    def get_or_download_active_video(self, preferred_url: Optional[str] = None) -> Optional[Path]:"""
new_god = """    def get_or_download_active_video(self, preferred_url: Optional[str] = None, genre: str = "") -> Optional[Path]:"""
t_norm = t_norm.replace(old_god, new_god)
t_norm = t_norm.replace("rotated = self.rotate_pool_video()", "rotated = self.rotate_pool_video(genre=genre)")

old_god_scan = """        # 3. Quét kiểm tra video đã có sẵn trong POOL_DIR
        pool_files = sorted(
            [f for f in POOL_DIR.glob("*.mp4") if f.stat().st_size > 1000000],
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )"""
new_god_scan = """        # 3. Quét kiểm tra video đã có sẵn trong POOL_DIR và raw_downloaded (16:9)
        pool_files = sorted(
            self._collect_all_candidate_pool_files(genre=genre),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )"""
t_norm = t_norm.replace(old_god_scan, new_god_scan)

# Update get_distinct_slice_for_part signature and source_path call
old_gds = """    def get_distinct_slice_for_part(
        self,
        series_id: str,
        part_number: int,
        duration_seconds: float,
        preferred_url: Optional[str] = None,
        total_parts: int = 3
    ) -> Path:"""
new_gds = """    def get_distinct_slice_for_part(
        self,
        series_id: str,
        part_number: int,
        duration_seconds: float,
        preferred_url: Optional[str] = None,
        total_parts: int = 3,
        genre: str = ""
    ) -> Path:"""
t_norm = t_norm.replace(old_gds, new_gds)
t_norm = t_norm.replace(
    "source_path = self.get_or_download_active_video(preferred_url=preferred_url)",
    "source_path = self.get_or_download_active_video(preferred_url=preferred_url, genre=genre)"
)

final = t_norm.replace("\n", "\r\n")
with open("core/background_manager.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated core/background_manager.py with genre filtering!")
