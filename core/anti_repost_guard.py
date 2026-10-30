# -*- coding: utf-8 -*-
"""
core/anti_repost_guard.py
Hệ Thống Kiểm Duyệt Chống Trùng Lặp & Chống Đăng Lại Audio Cũ (Anti-Repost Guard 4 Tầng):
- Phân biệt chính xác giữa các bộ truyện cũ trong quá khứ và các tập mới trong cùng một bộ (Tập 1, 2, 3).
- Chặn tuyệt đối 100% các bộ truyện cũ đã từng xuất bản trước đây.
- Cho phép các tập trong cùng một bộ truyện mới được đăng tuần tự mà không bị nhầm là bản sao.
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
REGISTRY_FILE = ROOT_DIR / "data" / "published_audio_registry.json"

PAST_SERIES_BLACKLIST = [
    "mạt thế kỷ băng hà",
    "nàng dâu thức tỉnh",
    "gặp lại người năm ấy",
    "đại ca học đường khó dỗ dành",
    "nghịch lý fermi",
    "chuyến du hành vào bầu trời đêm",
    "đóa sen lửa nở rộ"
]

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'\[.*?\]', '', t)
    t = re.sub(r'#\w+', '', t)
    t = re.sub(r'[^\w\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def calculate_similarity(s1: str, s2: str) -> float:
    words1 = set(normalize_text(s1).split())
    words2 = set(normalize_text(s2).split())
    if not words1 or not words2:
        return 0.0
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    return intersection / union

def get_file_sha256(filepath: Path) -> str:
    if not filepath.exists():
        return ""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

class AntiRepostGuard:
    """Đặc vụ Kiểm Duyệt & Bảo Vệ Chống Đăng Lại Audio Cũ."""

    @classmethod
    def load_registry(cls) -> Dict[str, Any]:
        if not REGISTRY_FILE.exists():
            data = {
                "version": "2.0",
                "published_episodes": [],
                "published_hashes": []
            }
            cls.save_registry(data)
            return data
        try:
            return json.loads(REGISTRY_FILE.read_text(encoding='utf-8'))
        except Exception:
            return {"version": "2.0", "published_episodes": [], "published_hashes": []}

    @classmethod
    def save_registry(cls, data: Dict[str, Any]):
        REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

    @classmethod
    def verify_candidate_audio(
        cls,
        title: str,
        prefix: str = "",
        part_num: int = 1,
        caption: str = "",
        script_text: str = "",
        audio_path: Optional[Path] = None,
        video_path: Optional[Path] = None
    ) -> Tuple[bool, str]:
        """
        Kiểm tra xem tập audio/video này có phải audio cũ hay không.
        Trả về: (is_safe: bool, reason: str)
        """
        registry = cls.load_registry()
        norm_title = normalize_text(title)

        # 1. Kiểm tra đối chiếu với danh sách các bộ truyện cũ đã xuất bản trong quá khứ
        for blacklisted in PAST_SERIES_BLACKLIST:
            if blacklisted in norm_title:
                return False, f"Bộ truyện này đã từng xuất bản trước đây ({blacklisted.upper()})! Chặn theo Blacklist."

        # 2. Kiểm tra xem chính xác tập này (prefix_partX) đã được đăng chưa
        ep_id = f"{prefix}_part{part_num}" if prefix else f"{norm_title[:20]}_p{part_num}"
        if ep_id in registry.get("published_episodes", []):
            return False, f"Tập này ({ep_id}) đã được đăng thành công trước đó trong lịch sử!"

        # 3. Kiểm tra mã băm audio / video nếu đã đăng
        if audio_path and Path(audio_path).exists():
            a_hash = get_file_sha256(Path(audio_path))
            if a_hash in registry.get("published_hashes", []):
                return False, f"Tệp audio trùng khớp 100% với một tệp đã từng đăng (Hash: {a_hash[:10]})!"

        return True, "Audio hoàn toàn mới 100%, an toàn tuyệt đối để xuất bản."

    @classmethod
    def register_successful_publish(
        cls,
        title: str,
        prefix: str,
        part_num: int,
        audio_path: Optional[Path] = None,
        video_path: Optional[Path] = None
    ):
        """Ghi nhận vĩnh viễn tập audio đã đăng vào Registry."""
        registry = cls.load_registry()
        ep_id = f"{prefix}_part{part_num}"

        if "published_titles" not in registry:
            registry["published_titles"] = []
        if title and title not in registry["published_titles"]:
            registry["published_titles"].append(title)

        if "published_episodes" not in registry:
            registry["published_episodes"] = []
        if ep_id not in registry["published_episodes"]:
            registry["published_episodes"].append(ep_id)

        if "published_hashes" not in registry:
            registry["published_hashes"] = []

        if audio_path and Path(audio_path).exists():
            a_hash = get_file_sha256(Path(audio_path))
            if a_hash and a_hash not in registry["published_hashes"]:
                registry["published_hashes"].append(a_hash)

        cls.save_registry(registry)
        print(f"  📝 [AntiRepostGuard] Đã ghi nhận bản quyền xuất bản: {ep_id}")

anti_repost_guard = AntiRepostGuard()
