import asyncio
import sys
import edge_tts

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

async def test():
    c = edge_tts.Communicate("Cô nghĩ mình là ai mà dám đòi chia đôi tài sản của Lục Thị? Trong mắt tôi, cô chỉ là con rối.", "vi-VN-NamMinhNeural")
    sentence_boundaries = []
    async for chunk in c.stream():
        if chunk["type"] == "SentenceBoundary":
            sentence_boundaries.append(chunk)
            
    print(f"Total SentenceBoundary events: {len(sentence_boundaries)}")
    for sb in sentence_boundaries:
        print(f"Sentence: offset={sb['offset']} ({sb['offset']/10000000:.2f}s), duration={sb['duration']} ({sb['duration']/10000000:.2f}s), text='{sb['text']}'")

if __name__ == "__main__":
    asyncio.run(test())
