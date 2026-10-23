import os
import json
import re
from typing import Dict, Any

def clean_json_response(raw_text: str) -> Dict[str, Any]:
    """Làm sạch markdown code fences và trích xuất JSON hợp lệ"""
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    try:
        return json.loads(text)
    except Exception:
        # Tìm khối {} đầu tiên nếu có text xung quanh
        json_match = re.search(r"\{[\s\S]*\}", text)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except Exception:
                pass
        return {"raw_output": text}

def call_llm(prompt: str, system_prompt: str = "") -> str:
    """
    Gọi LLM qua Google Gemini API hoặc OpenAI API.
    Nếu chưa có API Key, tự động sinh dữ liệu mẫu để kiểm thử pipeline mượt mà.
    """
    gemini_key = os.getenv("GEMINI_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if gemini_key:
        try:
            from google import genai
            client = genai.Client(api_key=gemini_key)
            full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
            candidates = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-pro"]
            for m in candidates:
                try:
                    response = client.models.generate_content(
                        model=m,
                        contents=full_prompt,
                    )
                    if response and response.text:
                        return response.text
                except Exception:
                    continue
            raise RuntimeError("All Gemini model candidates failed.")
        except Exception as e:
            print(f"[Warning] Gemini API call failed: {e}. Fallback to simulated response.")

    elif openai_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            for m in ["gpt-4o-mini", "gpt-4o"]:
                try:
                    response = client.chat.completions.create(
                        model=m,
                        messages=messages
                    )
                    if response and response.choices:
                        return response.choices[0].message.content
                except Exception:
                    continue
            raise RuntimeError("All OpenAI model candidates failed.")
        except Exception as e:
            print(f"[Warning] OpenAI API call failed: {e}. Fallback to simulated response.")

    # Chế độ Fallback / Demo khi người dùng chưa cấu hình API Key:
    return _generate_simulated_response(prompt, system_prompt)

def _generate_simulated_response(prompt: str, system_prompt: str) -> str:
    """Tự động sinh phản hồi giả lập chuẩn JSON để test hệ thống ngay lập tức"""
    if "Trend Hunter" in system_prompt or "Săn Xu Hướng" in system_prompt:
        if any(k in prompt for k in ["SLEEP_CHILL", "NGON_TINH", "ROMANCE", "TAM_SU"]):
            return json.dumps({
                "topic_name": "Chiếc Khăn Voan Dưới Mép Hợp Đồng Hôn Nhân 100 Tỷ",
                "summary": "Mũi bút máy vừa chạm vào điều khoản phân chia tài sản, vết son lạ trên cổ tay áo của vị tổng tài tàn tật đã tố cáo ván cờ giăng bẫy ba năm.",
                "key_facts": ["Bản hợp đồng hôn nhân dính vết nước trà", "Chiếc xe lăn hợp kim giấu camera ghi hình 24/7", "Đòn phản công thu hồi 35% cổ phần"],
                "recommended_hook_3s": "Mũi bút máy vừa chạm vào bản hợp đồng một trăm tỷ, vết son đỏ mận trên cổ tay áo anh ta đã tố cáo tất cả."
            }, ensure_ascii=False)
        elif any(k in prompt.lower() for k in ["doraemon", "thời gian", "bảo bối", "cánh cửa"]):
            return json.dumps({
                "topic_name": "Mẩu Giấy Cháy Xém Trong Ngăn Bàn: Lời Cảnh Báo Lúc 2 Giờ Sáng",
                "summary": "Ngăn bàn học cũ bật mở với tiếng lách cách kim loại, mẩu giấy cháy xém để lại lời cảnh báo đẫm máu về vụ án mạng xảy ra sau đúng 48 giờ.",
                "key_facts": ["Mẩu giấy than cháy xém mép", "Chiếc đồng hồ con lắc ngược dòng thời gian", "Vết sẹo chữ X trên cánh tay hung thủ"],
                "recommended_hook_3s": "Mẩu giấy than cháy xém vừa rơi khỏi ngăn bàn học, dòng chữ đỏ tươi đã hiện lên dòng số đếm ngược bốn mươi tám giờ."
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "topic_name": "Bức Di Thư Dưới Gạch Men Căn Phòng Số 13",
                "summary": "Mũi dao cậy nắp viên gạch men phòng tắm bật mở, bức di thư viết bằng máu hé lộ bí mật về vụ án mạng năm năm trước của người bạn thân.",
                "key_facts": ["Viên gạch men số 13 bị lung lay", "Chiếc cúc áo đồng phục dính mẫu máu khô", "Hồ sơ thế chấp tài sản giả mạo"],
                "recommended_hook_3s": "Mũi dao vừa cậy bật góc viên gạch men số mười ba, bức di thư dính máu khô đã rơi tuột xuống lòng bàn tay tôi."
            }, ensure_ascii=False)

    elif "Biên Kịch" in system_prompt:
        topic_match = re.search(r"Chủ đề:\s*([^\n]+)", prompt)
        story_topic = topic_match.group(1).strip() if topic_match else ""

        from core.story_vault import get_detective_masterpiece_story, get_family_drama_masterpiece_story
        prompt_low = (prompt + " " + story_topic).lower()
        if any(k in prompt_low for k in ["sleep_chill", "ru ngủ", "mất não", "gia đấu", "hào môn", "nữ chủ", "biệt thự", "50 tỷ", "mẹ con", "ly hôn", "mẹ chồng", "đời sống", "drama"]):
            story_data = get_family_drama_masterpiece_story(title=story_topic)
        else:
            story_data = get_detective_masterpiece_story(title=story_topic)
        return json.dumps(story_data, ensure_ascii=False)

    elif any(k in system_prompt for k in ["Biên Tập Viên", "Script Reviewer", "Tổng Biên Tập", "Thẩm Định Kịch Bản"]):
        return json.dumps({
            "status": "APPROVED",
            "score": 9.3,
            "rubric": {
                "hook_retention_score": 9.5,
                "depth_and_length_score": 9.2,
                "pacing_and_dialogue_score": 9.4,
                "continuity_and_flow_score": 9.5,
                "cliffhanger_climax_score": 9.1
            },
            "strengths": [
                "Hook 5s đầu bốc thẳng xung đột nghẹt thở, không lan man lý lịch hay thời tiết.",
                "Ngắt nhịp câu văn với dấu ba chấm, dấu gạch ngang và dấu than rất đắt giá cho giọng đọc AI lồng tiếng truyền cảm.",
                "Cấu trúc 3 tập liền mạch, kết cấu Show Don't Tell tinh tế và cao trào lật kèo thỏa mãn."
            ],
            "weaknesses": [],
            "specific_revision_guidance": "Kịch bản đã đạt chất lượng xuất xưởng tiêu chuẩn điện ảnh audio.",
            "notes": "Kịch bản xuất sắc đạt chuẩn điện ảnh audio. Giữ chân người nghe từ giây đầu đến phút cuối."
        }, ensure_ascii=False)

    elif "Phát Hành" in system_prompt or "Publisher" in system_prompt:
        prompt_low = prompt.lower()
        if any(k in prompt_low for k in ["kinh_di", "tam_linh", "kinh dị", "tâm linh", "mộ cổ", "huyết ấn", "quỷ", "ma"]):
            return json.dumps({
                "caption": "Bí mật ngôi mộ cổ và lời nguyền huyết ấn 500 năm 🕯️ #truyenaudio #kinhdi #tamlinh #moco #chuyendatrenbantho #xuhuong",
                "hashtags": ["#truyenaudio", "#kinhdi", "#tamlinh", "#moco", "#xuhuong"],
                "schedule_time": "23:00"
            }, ensure_ascii=False)
        elif any(k in prompt_low for k in ["doi_song", "drama", "gia_dinh", "đời sống", "gia đình", "di chúc", "nền bếp"]):
            return json.dumps({
                "caption": "Cuộc chiến di chúc dưới nền bếp: Sự thật đau lòng sau 20 năm ⚡ #truyenaudio #doisong #drama #giadinh #dichuc #xuhuong",
                "hashtags": ["#truyenaudio", "#doisong", "#drama", "#giadinh", "#xuhuong"],
                "schedule_time": "19:30"
            }, ensure_ascii=False)
        elif any(k in prompt_low for k in ["sleep_chill", "ngôn tình", "tình cảm", "hào môn", "tổng tài", "hôn nhân"]):
            return json.dumps({
                "caption": "Bản hợp đồng hôn nhân 100 tỷ và đêm tân hôn định mệnh 🌹 #truyenaudio #ngontinh #cuoituocyeusau #tongtai #tamlytinhcam #xuhuong",
                "hashtags": ["#truyenaudio", "#ngontinh", "#cuoituocyeusau", "#tongtai", "#xuhuong"],
                "schedule_time": "20:00"
            }, ensure_ascii=False)
        elif any(k in prompt_low for k in ["doraemon", "thời gian", "cánh cửa", "bảo bối"]):
            return json.dumps({
                "caption": "Kỳ án Cỗ Máy Thời Gian: Lời cảnh báo lúc nửa đêm của 20 năm sau ⏳ #truyenaudio #doraemon #trinhtham #kyan #khoahoc #xuhuong",
                "hashtags": ["#truyenaudio", "#doraemon", "#trinhtham", "#kyan", "#xuhuong"],
                "schedule_time": "21:00"
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "caption": "Kỳ án căn phòng số 13: Sự thật chỉ có một 🔍 #truyenaudio #conan #sherlockholmes #trinhtham #kyan #dautri #toipham #xuhuong",
                "hashtags": ["#truyenaudio", "#conan", "#trinhtham", "#kyan", "#dautri", "#xuhuong"],
                "schedule_time": "21:00"
            }, ensure_ascii=False)

    elif "Nghiên Cứu Thuật Toán" in system_prompt or "Chuyên gia Tối ưu" in prompt or "phân tích công thức viral" in prompt:
        topic_match = re.search(r"Tiêu đề:\s*([^\n]+)", prompt)
        topic_title = topic_match.group(1).strip() if topic_match else "Chuyện lạ có thật"
        # Làm sạch tiền tố như "Xu hướng TikTok:" nếu có
        topic_clean = re.sub(r'^(Xu hướng TikTok|Bí ẩn|Kỳ án|Truyện Đêm):\s*', '', topic_title, flags=re.IGNORECASE).strip()
        
        is_sleep = any(k in prompt.lower() or k in topic_clean.lower() for k in ["sleep", "ru ngủ", "mưa", "đêm", "chữa lành", "ngân hà", "hokkaido", "fansipan", "tĩnh lặng", "cabin"])
        
        if is_sleep:
            return json.dumps({
                "hook_formula": "Sensory Decompression",
                "hook_template": f"'Buông bỏ mọi muộn phiền, đêm nay câu chuyện về {topic_clean} sẽ vỗ về tâm hồn bạn'...",
                "viral_title_template": f"Truyện Đêm: {topic_clean} - Thả Lỏng Tâm Trí Và Ngủ Ngon",
                "comment_trigger": "Bạn đang nghe câu chuyện này ở đâu? Hãy để lại lời chúc ngủ ngon cho người lướt qua nhé.",
                "suggested_broll": "nature",
                "why_it_works": "Xoa dịu sóng não Alpha, phối hợp tiếng mưa rơi và piano 432Hz ru ngủ tuyệt đối."
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "hook_formula": "Climax First",
                "hook_template": f"'Sự thật chỉ có một, và mọi nghi vấn đều hướng về {topic_clean}!' - Bí mật kinh hoàng hé lộ...",
                "viral_title_template": f"Kỳ Án: Bí Mật Đằng Sau {topic_clean}",
                "comment_trigger": f"Nếu ở trong hoàn cảnh của nhân vật chính trong chuyện '{topic_clean}', bạn sẽ lựa chọn như thế nào?",
                "suggested_broll": "baking",
                "why_it_works": "Bốc cao trào lên 3s đầu, kết hợp video làm bánh ASMR giữ mắt người xem để tai nghe trọn vẹn 3 tập truyện."
            }, ensure_ascii=False)

    return "{}"

