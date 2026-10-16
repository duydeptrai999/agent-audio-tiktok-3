# -*- coding: utf-8 -*-
"""
scripts/crawl_stories_crawl4ai.py
================================================================================
CÔNG CỤ CÀO VÀ ĐÚC KẾT KINH NGHIỆM TRUYỆN NGẮN VỚI CRAWL4AI
================================================================================
Hướng dẫn sử dụng:
1. Cào trực tiếp 1 truyện từ URL:
   python scripts/crawl_stories_crawl4ai.py --url "https://..."

2. Chạy thử nghiệm cào mẫu và phân tích đúc kết kinh nghiệm:
   python scripts/crawl_stories_crawl4ai.py --demo

3. Cào danh sách truyện từ file txt:
   python scripts/crawl_stories_crawl4ai.py --file danh_sach_url.txt

4. Quét toàn bộ truyện đã cào và xuất báo cáo tổng hợp kinh nghiệm:
   python scripts/crawl_stories_crawl4ai.py --summarize
"""

import os
import sys
import argparse
import asyncio
import logging
from pathlib import Path

# Thêm thư mục gốc vào PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Đảm bảo UTF-8 trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from core.crawl4ai_story_scraper import Crawl4AiStoryScraper, get_story_scraper, StoryNarrativeAnalyzer

logger = logging.getLogger("CrawlStoriesCLI")
logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s] %(message)s")


DEMO_SAMPLE_STORY = """
Lâm Viễn ném bản thỏa thuận ly hôn sang trước mặt tôi, ngón tay gõ nhẹ lên mặt bàn đá cẩm thạch lạnh ngắt:
"An Nhiên, cô nên ra ngoài đi làm để biết kiếm tiền khó thế nào, đừng quanh quẩn ở nhà làm phiền tôi nữa. Ký đi, căn nhà này và chiếc xe tôi để lại cho cô."

Tôi cúi đầu nhìn dòng chữ in đậm đen tuyền trên giấy trắng. Cơn đau thắt nơi lồng ngực lại dội lên, nhưng bàn tay tôi giấu dưới bàn ăn vẫn siết chặt, không run rẩy dù chỉ một milimet. 

"Được, tôi ký." Giọng tôi bình thản đến mức chính Lâm Viễn cũng phải ngẩng đầu lên, ánh mắt đầy vẻ ngờ vực.

Năm năm trước, ngày Lâm Viễn phá sản nợ nần chồng chất, tôi đã bán toàn bộ số trang sức của mẹ để lại, cùng anh ăn những gói mì tôm năm nghìn trong căn phòng trọ dột nát. Tôi thức trắng hàng trăm đêm cùng anh sửa từng trang hồ sơ thầu, giặt từng chiếc áo sơ mi dính đầy vết cà phê.

Đến khi công ty anh lên sàn chứng khoán, giá trị vốn hóa chạm mốc hàng nghìn tỷ, người đứng cạnh anh trên bục vinh quang lại là cô trợ lý mới tốt nghiệp đại học, với đôi mắt to tròn ngây thơ và câu nói: "Em không cần tiền của anh, em chỉ muốn cùng anh ngắm hoàng hôn".

Tôi rút bút ký tên mình vào góc phải bản thỏa thuận. Không đòi hỏi thêm một đồng, cũng không chất vấn nửa lời.

Lâm Viễn cười nhạt, ánh mắt hiện lên vẻ khinh miệt:
"Biết điều vậy là tốt. Tôi ghét nhất phụ nữ bám riết không buông."

Anh đâu biết, trong chiếc túi xách cũ kỹ đặt bên cạnh chiếc va li của tôi, là tờ kết quả xét nghiệm ung thư xương giai đoạn cuối của Bệnh viện Ung bướu Trung ương. Bác sĩ bảo, thời gian của tôi chỉ còn chưa đầy ba tháng.

Tôi rời khỏi căn biệt thự lúc 3 giờ chiều, không mang theo bất cứ thứ gì ngoài ba bộ quần áo giản dị và cuốn sổ tay ghi lại toàn bộ danh mục thuốc dị ứng, số đo trang phục và lịch ăn kiêng của Lâm Viễn. Tôi đặt cuốn sổ ngay ngắn trên bàn trà, bên cạnh là chiếc nhẫn cưới bằng bạc năm xưa chúng tôi mua với giá ba trăm nghìn.

Một tháng sau khi tôi biến mất, Lâm Viễn đưa người yêu mới về sống trong căn biệt thự. Nhưng chuỗi ngày êm ấm mà anh ta tưởng tượng chưa từng xuất hiện.

Chiếc áo sơ mi đắt tiền bị người giúp việc ủi cháy xém. Đồ ăn ngoài dầu mỡ khiến dạ dày anh ta đau quằn quại giữa đêm khuya. Khi mở tủ thuốc tìm lọ thuốc dạ dày, anh ta chỉ thấy khoảng trống lạnh lẽo cùng một mẩu giấy ghi chú viết tay bằng nét chữ quen thuộc: "Thuốc dạ dày uống sau ăn 30 phút, tuyệt đối không được uống cùng rượu vang."

Lâm Viễn sững sờ. Anh ta bắt đầu lùng sục căn phòng, mở từng ngăn kéo, và vô tình chạm vào chiếc ngăn kéo khóa kín dưới đáy bàn trang điểm.

Bên trong là hóa đơn những lần tôi xạ trị đơn độc trong bóng tối, cùng cuốn nhật ký 100 trang tôi viết cho anh mỗi ngày:
"Hôm nay Lâm Viễn về muộn, trên cổ áo có mùi nước hoa hoa nhài. Mình biết anh ấy đã rung động rồi. Nhưng mình không giận, chỉ mong người con gái ấy sẽ thay mình nhắc anh uống thuốc mỗi khi trời trở lạnh."

Dòng chữ cuối cùng bị nhòe đi bởi vệt nước mắt đã khô cứng.

Chiếc điện thoại trên tay Lâm Viễn rơi xuống sàn vỡ toang. Anh ta phát điên, lao xe như một kẻ mất trí đến tất cả các bệnh viện trong thành phố, quỳ gối trước cổng viện gào khóc trong cơn mưa bão tuyết mù trời:
"An Nhiên, em ở đâu? Anh không cần công ty nữa, anh không cần danh vọng nữa, em về với anh được không?!"

Nhưng thành phố rộng lớn hàng chục triệu dân, không ai trả lời anh ta nữa. 

Dưới chân một ngọn đồi nhỏ ở ngoại ô, có một nấm mồ xanh cỏ mới đắp, trên bia đá chỉ khắc vỏn vẹn một dòng chữ:
"An Nhiên - Người đã từng yêu hết lòng, và ra đi thanh thản."
"""


async def run_demo():
    """Chạy thử nghiệm cào và phân tích cấu trúc kịch bản mẫu."""
    logger.info("=== BẮT ĐẦU CHẠY THỬ NGHIỆM CRAWL4AI NARRATIVE ANALYZER ===")
    
    # 1. Khởi tạo scraper
    scraper = get_story_scraper(headless=True)
    
    # 2. Phân tích văn bản đoản văn mẫu
    title = "An Nhiên và Lâm Viễn - Ngược Luyến Hỏa Táng Tràng"
    metadata = {
        "title": title,
        "author": "Cửu Cửu (Zhihu)",
        "platform": "Zhihu 盐选 / Douyin Đoản Văn",
        "genre": "Ngược Luyến Tàn Tâm & Hỏa Táng Tràng",
        "url": "https://www.zhihu.com/demo/an-nhien-lam-vien"
    }
    
    cleaned_text = scraper.clean_novel_text(DEMO_SAMPLE_STORY)
    analysis = StoryNarrativeAnalyzer.analyze_story(title, cleaned_text, metadata)
    
    crawl_result = {
        "success": True,
        "metadata": metadata,
        "title": title,
        "content": cleaned_text,
        "raw_markdown_length": len(cleaned_text),
        "analysis": analysis
    }
    
    # 3. Lưu dữ liệu và xuất file kinh nghiệm chi tiết
    json_path, md_path = scraper.save_crawled_story(crawl_result, custom_id="demo_an_nhien_lam_vien")
    
    print("\n" + "="*80)
    print("✅ ĐÃ HOÀN TẤT THỬ NGHIỆM CRAWL4AI VÀ PHÂN TÍCH KỊCH BẢN!")
    print(f"📁 File Dữ Liệu JSON: {json_path}")
    print(f"📖 File Kinh Nghiệm Biên Kịch Chi Tiết: {md_path}")
    print("="*80)
    print(f"📌 Tiêu Đề: {title}")
    print(f"⏱ Quy mô: {analysis['word_count']} từ (~{analysis['estimated_audio_runtime_15x_minutes']} phút audio ở tốc độ 1.5x)")
    print(f"🎯 Golden Hook (5s): \"{analysis['golden_retention_hook_5s'][:120]}...\"")
    print(f"💬 Tỷ lệ thoại: {analysis['dialogue_metrics']['dialogue_ratio_percent']}% ({analysis['dialogue_metrics']['assessment']})")
    print(f"🔥 Kích hoạt cảm xúc: {', '.join(analysis['conflict_triggers'])}")
    print("="*80 + "\n")


async def crawl_single_url(url: str):
    """Cào một URL cụ thể và phân tích đúc kết kinh nghiệm."""
    scraper = get_story_scraper(headless=True)
    logger.info(f"Bắt đầu cào URL: {url}")
    result = await scraper.crawl_url(url)
    if not result.get("success"):
        logger.error(f"Cào thất bại: {result.get('error')}")
        return
    
    json_path, md_path = scraper.save_crawled_story(result)
    logger.info(f"Cào và phân tích thành công!")
    logger.info(f"JSON: {json_path}")
    logger.info(f"Markdown Kinh Nghiệm: {md_path}")


def main():
    parser = argparse.ArgumentParser(description="Crawl4AI Story Scraper and Narrative Learning Engine")
    parser.add_argument("--url", type=str, help="URL truyện ngắn cần cào")
    parser.add_argument("--demo", action="store_true", help="Chạy thử nghiệm cào và phân tích mẫu")
    parser.add_argument("--file", type=str, help="File txt chứa danh sách URL cần cào hàng loạt")
    
    args = parser.parse_args()
    
    if args.demo:
        asyncio.run(run_demo())
    elif args.url:
        asyncio.run(crawl_single_url(args.url))
    elif args.file:
        url_file = Path(args.file)
        if not url_file.exists():
            print(f"Lỗi: Không tìm thấy file {url_file}")
            return
        with open(url_file, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"Tìm thấy {len(urls)} URLs cần cào...")
        for u in urls:
            asyncio.run(crawl_single_url(u))
    else:
        # Mặc định chạy demo nếu không truyền cờ
        asyncio.run(run_demo())


if __name__ == "__main__":
    main()
