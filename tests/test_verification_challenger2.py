import ast
import os
import re
import subprocess
import sys
import imageio_ffmpeg

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath("."))

def test_document_verification():
    doc_path = "docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md"
    assert os.path.exists(doc_path), f"File {doc_path} not found!"
    
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print("=== TEST 1: HOOK WORD COUNT AND DURATION ===")
    t1_pattern = r'Template 1.*?>\s*\*"([^"]+)"\*'
    t2_pattern = r'Template 2.*?>\s*\*"([^"]+)"\*'
    t3_pattern = r'Template 3.*?>\s*\*"([^"]+)"\*'
    
    m1 = re.search(t1_pattern, content, re.DOTALL)
    m2 = re.search(t2_pattern, content, re.DOTALL)
    m3 = re.search(t3_pattern, content, re.DOTALL)
    
    assert m1 and m2 and m3, "Could not find all 3 Hook templates in document!"
    t1_text = m1.group(1).strip()
    t2_text = m2.group(1).strip()
    t3_text = m3.group(1).strip()
    
    print(f"Template 1: '{t1_text}' ({len(t1_text.split())} words/syllables)")
    print(f"Template 2: '{t2_text}' ({len(t2_text.split())} words/syllables)")
    print(f"Template 3: '{t3_text}' ({len(t3_text.split())} words/syllables)")
    
    assert t1_text == "Đêm tân hôn, tôi chết lặng thấy bạn thân trốn trong tủ quần áo!", f"Unexpected T1 text: {t1_text}"
    assert t2_text == "Mẹ chồng hắt canh nóng, bắt tôi ly hôn rồi cút khỏi nhà!", f"Unexpected T2 text: {t2_text}"
    assert t3_text == "Mẹ chồng ném mười tỷ ép tôi rời xa con trai bà ngay lập tức!", f"Unexpected T3 text: {t3_text}"
    print("  -> PASSED: All 3 Hook templates match the compacted, high-impact phrasing!")
    
    print("\n=== TEST 2: PROHIBITED TERM 'khỏa thân' SANITIZATION ===")
    assert "cô bạn thân đang khỏa thân trốn bên trong" not in content, "Found old prohibited hook phrase!"
    # Check that 'khỏa thân' is not used inside any script dialog
    script_lines = [line for line in content.splitlines() if line.strip().startswith(">")]
    for sl in script_lines:
        assert "khỏa thân" not in sl.lower() and "lõa thể" not in sl.lower(), f"Sensitive word found in dialogue: {sl}"
    print("  -> PASSED: No sensitive terms found in script dialogues!")
    
    print("\n=== TEST 3: FFMPEG END-SCREEN CARD FONT PATH ===")
    from core.ffmpeg_utils import get_vietnamese_font_path
    font_path = get_vietnamese_font_path()
    print(f"Dynamic font returned: '{font_path}'")
    assert font_path is not None and len(font_path) > 0, "Font path should not be empty"
    assert "from core.ffmpeg_utils import get_vietnamese_font_path" in content, "Missing import in doc"
    assert "font = get_vietnamese_font_path() or \"arial\"" in content, "Missing dynamic font assignment in doc"
    print("  -> PASSED: FFmpeg filter uses dynamic get_vietnamese_font_path()!")
    
    print("\n=== TEST 4: PLAYWRIGHT 2.5K FOLLOWER SAFEGUARD & BILINGUAL SELECTOR ===")
    assert "2.5K follower" in content, "Missing 2.5K follower analysis"
    assert "div[role=\"combobox\"]:has-text(\"danh sách phát\")," in content or "div[role=\"combobox\"]:has-text(\"Playlist\")" in content
    assert "Series" in content
    assert "wait_for(state=\"visible\"" in content
    print("  -> PASSED: Playwright automation includes 2.5K follower safeguard, fallback and bilingual selectors!")

    print("\n=== ALL TESTS PASSED SUCCESSFULLY! ===")

if __name__ == "__main__":
    test_document_verification()
