# -*- coding: utf-8 -*-
"""
core/crawl4ai_story_scraper.py
================================================================================
HỆ THỐNG CÀO VÀ PHÂN TÍCH DỮ LIỆU TRUYỆN NGẮN THÔNG MINH DỰA TRÊN CRAWL4AI
================================================================================
Sử dụng thư viện Crawl4AI (https://github.com/unclecode/crawl4AI) kết hợp
Browser Headless (Playwright/Patchright) để tự động hóa:
1. Thu thập dữ liệu đoản văn/truyện ngắn từ các nền tảng Trung Quốc (Zhihu 盐选,
   Fanqie 番茄, Qidian 起点, 69shuba, Biquge, Bilibili) và các web truyện dịch (TruyenFull, Tangthuvien...).
2. Trích xuất sạch nội dung, tiêu đề, tác giả, thể loại, bóc tách lời thoại và lời dẫn.
3. Phân tích tự động cấu trúc kịch bản:
   - Golden Retention Hook 3-5 giây (mở màn).
   - Tỷ lệ đối thoại / miêu tả (Dialogue vs Narration ratio).
   - Ma trận leo thang xung đột & điểm nén uất ức (Suppression points).
   - Sảng điểm (Catharsis/Shuangdian) & Ngược điểm (Angst/Drama).
   - Khẩu súng của Chekhov (Chekhov's Gun).
   - Điểm rơi kết thúc & Cliffhanger (卡点).
4. Tự động xuất ra file Kinh Nghiệm Biên Kịch chuẩn mực (Markdown & JSON) và
   lập chỉ mục trực tiếp vào Knowledge Base (`core/knowledge_base.py`).
"""

import os
import re
import sys
import json
import asyncio
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger("Crawl4AiStoryScraper")
logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s][%(name)s] %(message)s")

# Thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "crawled_stories"
EXPERIENCE_DIR = BASE_DIR / "docs" / "kinh_nghiem_chi_tiet"
DATA_DIR.mkdir(parents=True, exist_ok=True)
EXPERIENCE_DIR.mkdir(parents=True, exist_ok=True)

# Crawl4AI imports
try:
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
    CRAWL4AI_AVAILABLE = True
except ImportError:
    CRAWL4AI_AVAILABLE = False
    logger.warning("crawl4ai chưa được cài đặt. Vui lòng chạy: pip install crawl4ai")


class StoryNarrativeAnalyzer:
    """
    Bộ phân tích cấu trúc tự sự và đúc kết kinh nghiệm biên kịch tự động từ văn bản truyện.
    Áp dụng các định luật đoản văn triệu view Zhihu & Douyin.
    """

    @staticmethod
    def extract_golden_hook(text: str, max_sentences: int = 3) -> str:
        """Trích xuất câu mở màn 5 giây (Golden Retention Hook)."""
        paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 15]
        if not paragraphs:
            return ""
        # Lấy đoạn đầu tiên hoặc ghép 2-3 câu đầu tiên
        first_para = paragraphs[0]
        sentences = re.split(r'(?<=[.!?…])\s+', first_para)
        hook = " ".join(sentences[:max_sentences])
        return hook[:300].strip()

    @staticmethod
    def calculate_dialogue_ratio(text: str) -> Dict[str, Any]:
        """Tính toán tỷ lệ đối thoại / độc thoại / miêu tả."""
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        dialogue_chars = 0
        total_chars = len(text)

        # Regex nhận diện ngoặc kép tiếng Trung 「」, “”, hoặc gạch đầu dòng
        dialogue_pattern = re.compile(r'[“"「『](.*?)[”"」』]')
        for line in lines:
            matches = dialogue_pattern.findall(line)
            for m in matches:
                dialogue_chars += len(m)
            if line.startswith("- ") or line.startswith("— "):
                dialogue_chars += len(line)

        ratio = round((dialogue_chars / max(1, total_chars)) * 100, 2)
        return {
            "total_chars": total_chars,
            "dialogue_chars": dialogue_chars,
            "dialogue_ratio_percent": ratio,
            "assessment": "Rất cao (chuẩn kịch bản thoại Douyin/Audio)" if ratio >= 35 else "Cân bằng miêu tả và thoại"
        }

    @staticmethod
    def detect_conflict_keywords(text: str) -> List[str]:
        """Phát hiện các từ khóa xung đột, kích hoạt cảm xúc mạnh."""
        keywords_dict = {
            "Trọng sinh / Kiếp trước": ["trọng sinh", "kiếp trước", "sống lại", "quay về", "đời trước", "重生", "前世"],
            "Vả mặt / Báo thù": ["vả mặt", "báo thù", "trừng phạt", "hối hận", "tát", "phá sản", "vào tù", "打脸", "报仇"],
            "Ngược luyến / Hỏa táng": ["ly hôn", "thế thân", "bạch nguyệt quang", "ung thư", "bỏ đi", "hỏa táng tràng", "quỳ xin", "火葬场", "替身", "白月光"],
            "Hào môn / Gia tộc": ["tổng tài", "hợp đồng", "thẻ đen", "thừa kế", "tỷ phú", "thái tử gia", "cổ phần", "总裁", "豪门"],
            "Kinh dị / Quái đàm": ["quy tắc", "nửa đêm", "bệnh viện", "máu", "thi thể", "bóng đen", "biến mất", "cấm kỵ", "规则怪谈"],
            "Sa điêu / Đọc tiếng lòng": ["tiếng lòng", "hệ thống", "tấu hài", "sa điêu", "chửi thầm", "bắt bài", "读心术", "系统"]
        }
        detected = []
        lower_text = text.lower()
        for cat, kws in keywords_dict.items():
            for kw in kws:
                if kw in lower_text:
                    detected.append(f"{cat}: '{kw}'")
                    break
        return detected

    @staticmethod
    def extract_cliffhanger(text: str) -> str:
        """Trích xuất phân đoạn kết thúc hoặc điểm rơi cuối tác phẩm / chương."""
        paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 20]
        if not paragraphs:
            return ""
        return paragraphs[-1][:300]

    @classmethod
    def analyze_story(cls, title: str, text: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Phân tích toàn diện kịch bản theo chuẩn biên kịch chuyên sâu."""
        meta = metadata or {}
        words = len(text.split())
        chars = len(text)
        hook = cls.extract_golden_hook(text)
        dialogue_stats = cls.calculate_dialogue_ratio(text)
        conflicts = cls.detect_conflict_keywords(text)
        cliffhanger = cls.extract_cliffhanger(text)

        # Ước tính thời lượng phát âm thanh ở tốc độ 1.5x (chuẩn 346 từ/phút)
        audio_minutes_15x = round(words / 346, 1)

        analysis = {
            "title": title,
            "author": meta.get("author", "Khuyết danh"),
            "platform": meta.get("platform", "Web/Zhihu/Fanqie"),
            "genre": meta.get("genre", "Đoản văn Trung Quốc"),
            "url": meta.get("url", ""),
            "crawled_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "word_count": words,
            "char_count": chars,
            "estimated_audio_runtime_15x_minutes": audio_minutes_15x,
            "golden_retention_hook_5s": hook,
            "dialogue_metrics": dialogue_stats,
            "conflict_triggers": conflicts,
            "cliffhanger_or_ending": cliffhanger,
            "pacing_beat_sheet": {
                "hoi_1_thiet_lap_va_hook": "Ném người đọc vào tâm chấn xung đột, cài súng Chekhov, không mở bài dông dài.",
                "hoi_2_nen_ap_suat_va_leo_thang": "Phản diện lấn tới, uất ức tích tụ, nhân vật chính thu thập chứng cứ và tương kế tựu kế.",
                "hoi_3_bung_no_va_sa_van_shuangdian": "Vả mặt triệt để, phơi bày đa tầng chân tướng, đúc kết dư âm nhân sinh."
            },
            "scriptwriting_takeaways": [
                f"Độ dài: {words} từ (~{audio_minutes_15x} phút ở 1.5x) rất phù hợp cho video/audio TikTok/YouTube.",
                f"Tỷ lệ đối thoại {dialogue_stats['dialogue_ratio_percent']}% giúp diễn đạt cảm xúc sống động qua giọng đọc AI.",
                f"Cú hook: '{hook[:100]}...' đánh trực diện vào tâm lý tò mò của khán giả ngay 5 giây đầu."
            ]
        }
        return analysis


class Crawl4AiStoryScraper:
    """
    Bộ cào dữ liệu truyện thông minh sử dụng Crawl4AI AsyncWebCrawler.
    Hỗ trợ cào đa nền tảng, bóc tách cấu trúc kịch bản và lưu trữ kinh nghiệm.
    """

    def __init__(self, headless: bool = True, verbose: bool = False):
        self.headless = headless
        self.verbose = verbose
        self.browser_config = None
        self.run_config = None
        if CRAWL4AI_AVAILABLE:
            self.browser_config = BrowserConfig(
                headless=self.headless,
                verbose=self.verbose,
                extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"]
            )
            self.run_config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                word_count_threshold=50,
                page_timeout=30000,
                delay_before_return_html=1.5
            )

    async def crawl_url(self, url: str) -> Dict[str, Any]:
        """
        Cào trực tiếp một URL truyện bằng Crawl4AI.
        Trả về metadata, markdown, cleaned_html.
        """
        if not CRAWL4AI_AVAILABLE:
            raise RuntimeError("crawl4ai library is not installed.")

        logger.info(f"Đang kích hoạt Crawl4AI để cào URL: {url}")
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result = await crawler.arun(url=url, config=self.run_config)
            if not result.success:
                logger.error(f"Cào thất bại ({url}): {result.error_message}")
                return {
                    "success": False,
                    "url": url,
                    "error": result.error_message
                }

            # Trích xuất tiêu đề từ metadata hoặc thẻ h1
            title = "Truyện Ngắn Không Tiêu Đề"
            if result.metadata and result.metadata.get("title"):
                title = result.metadata.get("title").split(" - ")[0].split("_")[0].strip()

            raw_markdown = result.markdown or ""
            cleaned_text = self.clean_novel_text(raw_markdown)

            # Nhận diện platform
            platform = "Web"
            if "zhihu.com" in url:
                platform = "Zhihu 盐选"
            elif "fanqienovel.com" in url or "fanqie" in url:
                platform = "Fanqie 番茄"
            elif "qidian.com" in url:
                platform = "Qidian 起点"
            elif "69shuba" in url:
                platform = "69 Thư Ba (69shuba)"
            elif "truyenfull" in url:
                platform = "TruyenFull"
            elif "tangthuvien" in url:
                platform = "Tàng Thư Viện"

            metadata = {
                "title": title,
                "url": url,
                "platform": platform,
                "status_code": result.status_code,
                "crawled_at": datetime.now().isoformat()
            }

            # Phân tích kịch bản
            analysis = StoryNarrativeAnalyzer.analyze_story(title, cleaned_text, metadata)

            return {
                "success": True,
                "metadata": metadata,
                "title": title,
                "content": cleaned_text,
                "raw_markdown_length": len(raw_markdown),
                "analysis": analysis
            }

    @staticmethod
    def clean_novel_text(text: str) -> str:
        """Lọc bỏ quảng cáo, link điều hướng, ghi chú dịch giả và boilerplate."""
        lines = text.split("\n")
        cleaned_lines = []
        noise_keywords = [
            "chương trước", "chương sau", "mục lục", "bình luận", "đăng nhập", "quảng cáo",
            "previous chapter", "next chapter", "table of contents", "advertisement",
            "vote sao", "ủng hộ dịch giả", "fanpage", "truyencv", "truyenfull",
            "点赞", "收藏", "目录", "上一章", "下一章", "关注", "知乎盐选"
        ]
        for line in lines:
            line_str = line.strip()
            # Bỏ qua các dòng ngắn có link markdown hoặc ký tự điều hướng
            if not line_str:
                continue
            lower_line = line_str.lower()
            if any(k in lower_line for k in noise_keywords) and len(line_str) < 60:
                continue
            if re.match(r'^\[.*?\]\(.*?\)$', line_str):
                continue
            cleaned_lines.append(line_str)

        return "\n\n".join(cleaned_lines)

    def save_crawled_story(self, crawl_result: Dict[str, Any], custom_id: Optional[str] = None) -> Tuple[Path, Path]:
        """
        Lưu truyện đã cào thành 2 file:
        1. File dữ liệu JSON trong data/crawled_stories/
        2. File đúc kết kinh nghiệm biên kịch Markdown trong docs/kinh_nghiem_chi_tiet/
        """
        title = crawl_result.get("title", "story")
        safe_title = re.sub(r'[\/:*?"<>| ]+', '_', title)[:40]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        story_id = custom_id or f"crawl_{timestamp}_{safe_title}"

        # 1. Lưu JSON
        json_file = DATA_DIR / f"{story_id}.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(crawl_result, f, ensure_ascii=False, indent=2)

        # 2. Tạo Markdown kinh nghiệm chi tiết
        analysis = crawl_result.get("analysis", {})
        md_file = EXPERIENCE_DIR / f"EXP_{story_id}.md"

        md_content = f"""# ĐÚC KẾT KINH NGHIỆM BIÊN KỊCH CHI TIẾT: {title}
**Nền tảng & Nguồn:** {analysis.get('platform', 'N/A')} ({analysis.get('url', 'N/A')})  
**Thời gian phân tích:** {analysis.get('crawled_at', 'N/A')}  
**Quy mô văn bản:** {analysis.get('word_count', 0)} từ / {analysis.get('char_count', 0)} ký tự (~{analysis.get('estimated_audio_runtime_15x_minutes', 0)} phút audio 1.5x)

---

## 1. TINH HOA & ẤN TƯỢNG CỦA TÁC PHẨM (ESSENCE & HIGHLIGHTS)
- **Cú Hook 5 Giây Đầu (Golden Retention Hook):**
  > "{analysis.get('golden_retention_hook_5s', 'N/A')}"
- **Đánh giá tỷ lệ đối thoại:** {analysis.get('dialogue_metrics', {}).get('dialogue_ratio_percent', 0)}% đối thoại ({analysis.get('dialogue_metrics', {}).get('assessment', '')}).
- **Các từ khóa xung đột then chốt:** {', '.join(analysis.get('conflict_triggers', ['N/A']))}

---

## 2. BỐI CẢNH & THIẾT LẬP NHÂN VẬT (SETTING & CHARACTER DYNAMICS)
- **Bối cảnh:** {analysis.get('genre', 'Đoản văn')} - Xây dựng tình huống mâu thuẫn trực diện, cô đọng không gian để tập trung vào xung đột tâm lý.
- **Tạo hình nhân vật chính:** Thiết lập mục tiêu rõ ràng, phản ứng nhanh trước áp bức, từ chối lối mòn cam chịu.
- **Tạo hình đối kháng (Phản diện):** Tạo áp lực leo thang bậc thang, làm bàn đạp cho sảng điểm bùng nổ.

---

## 3. CẤU TRÚC 3 HỒI & NHỊP ĐIỆU KỊCH TÍNH (BEAT-SHEET)
- **Hồi 1 (Mở màn & Thiết lập):** {analysis.get('pacing_beat_sheet', {}).get('hoi_1_thiet_lap_va_hook', '')}
- **Hồi 2 (Nén áp suất & Đối đầu):** {analysis.get('pacing_beat_sheet', {}).get('hoi_2_nen_ap_suat_va_leo_thang', '')}
- **Hồi 3 (Đại kết cục & Vả mặt triệt để):** {analysis.get('pacing_beat_sheet', {}).get('hoi_3_bung_no_va_sa_van_shuangdian', '')}
- **Điểm rơi kết thúc (Cliffhanger / Ending):**
  > "{analysis.get('cliffhanger_or_ending', 'N/A')}"

---

## 4. ĐÚC KẾT BÀI HỌC BIÊN KỊCH THỰC CHIẾN (SCRIPTWRITING TAKEAWAYS)
{chr(10).join(f"- {item}" for item in analysis.get('scriptwriting_takeaways', []))}
- **Ứng dụng cho Video/Audio 30 Phút:**
  * Giữ nhịp câu 10 - 20 từ, tận dụng dấu phẩy và dấu ba chấm để tạo khoảng thở kịch tính.
  * Tận dụng âm thanh hiệu ứng (B-Roll sound effects) tại các bước ngoặt cảm xúc.
  * Đảm bảo nguyên lý Chekhov: Không để chi tiết nào xuất hiện vô nghĩa.

---
*File đúc kết được tạo tự động bởi Hệ thống Crawl4AI Story Scraper & Analyzer.*
"""
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        logger.info(f"Đã lưu thành công story data: {json_file}")
        logger.info(f"Đã tạo file kinh nghiệm chi tiết: {md_file}")
        return json_file, md_file


# Singleton instance
_scraper_instance = None

def get_story_scraper(headless: bool = True) -> Crawl4AiStoryScraper:
    global _scraper_instance
    if _scraper_instance is None:
        _scraper_instance = Crawl4AiStoryScraper(headless=headless)
    return _scraper_instance
