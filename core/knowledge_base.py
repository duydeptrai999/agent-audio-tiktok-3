# -*- coding: utf-8 -*-
"""
core/knowledge_base.py
Cơ Sở Dữ Liệu Tri Thức Biên Kịch Chuyên Sâu (Chinese Short Story Knowledge Base Engine)
Tổng hợp, lập chỉ mục và cung cấp API truy vấn thông minh từ 100 tác phẩm đoản văn kinh điển
thuộc 10 nhóm thể loại hàng đầu (Zhihu 盐选, Douyin 短剧, Fanqie, Jinjiang, Qidian).

Mục tiêu cốt lõi:
Mỗi khi hệ thống tạo ra một kịch bản mới, Agent Biên Kịch bắt buộc phải tra cứu Cơ sở dữ liệu này
để chọn lọc case study tương đồng nhất, áp dụng 10 Định Luật Vàng, Mô hình 4 Tầng Bất đối xứng Thông tin,
6 Mẫu Hook Mở màn, Ma trận Điểm Sảng, Hệ thống 4 Tầng Phản diện và Cắt điểm rơi Cliffhanger nghẹt thở.
"""

import os
import re
import json
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path

from core.state import VideoCategory
from data.stories_study.genre1_nguoc_tam import STORIES_GENRE_1
from data.stories_study.genre2_trong_sinh import STORIES_GENRE_2
from data.stories_study.genre3_huyen_nghi import STORIES_GENRE_3
from data.stories_study.genre4_me_chong import STORIES_GENRE_4
from data.stories_study.genre5_hao_mon import STORIES_GENRE_5
from data.stories_study.genre6_kinh_di import STORIES_GENRE_6
from data.stories_study.genre7_sa_dieu import STORIES_GENRE_7
from data.stories_study.genre8_cung_dau import STORIES_GENRE_8
from data.stories_study.genre9_cuu_roi import STORIES_GENRE_9
from data.stories_study.genre10_vo_han import STORIES_GENRE_10

logger = logging.getLogger("KnowledgeBase")
root_dir = Path(__file__).resolve().parent.parent

# ==============================================================================
# 1. HỆ THỐNG 10 ĐỊNH LUẬT VÀNG BIÊN KỊCH ĐOẢN VĂN VIRAL
# ==============================================================================
GOLDEN_RULES_10 = [
    {
        "rule_id": 1,
        "name": "In Medias Res (Golden Retention Hook 5 Giây)",
        "principle": "Cấm tuyệt đối đọc lý lịch tuổi tác hoặc tả thời tiết (Zero-Biography). 15 từ đầu tiên phải ném ngay câu thoại áp chế, hiện trường rùng mình hoặc nghịch lý biến cố.",
        "formula": "Hook = [Xung đột cực độ] + [Người thân phản trắc / Biến cố sinh tử] + [Nghịch lý nhận thức]"
    },
    {
        "rule_id": 2,
        "name": "Nén Áp Suất & Giải Phóng Cảm Xúc (Suppression & Catharsis)",
        "principle": "Khoái cảm sảng văn tỷ lệ thuận với độ nén ức chế. Cứ 300 từ có một vi-xung đột làm đối phương lấn tới, nhân vật chính nén lại rồi bùng nổ khi phản diện đắc ý nhất.",
        "formula": "Tập 1 nén áp lực -> Tập 2 bế tắc đường cùng -> Tập 3 vỡ òa trừng phạt triệt để"
    },
    {
        "rule_id": 3,
        "name": "Khẩu Súng Của Chekhov (Cỏ Rắn Vệt Tro - 草蛇灰线)",
        "principle": "Mọi vật phẩm, thói quen, chi tiết xuất hiện ở Hồi 1 (chiếc bánh bao, chiếc USB, thói quen dị ứng, đồng hồ chết) đều phải trở thành chìa khóa đoạt mạng ở Hồi 3.",
        "formula": "Chi tiết vô hại Hồi 1 -> Vật chứng quyết định Hồi 3"
    },
    {
        "rule_id": 4,
        "name": "Tương Phản Nhân Vật Cực Đoan (Extreme Archetype Contrast)",
        "principle": "Đặt hai hình tượng đối lập cạnh nhau: Tổng tài lạnh lùng vs Vợ thực dụng coi hôn nhân là công việc; Mẹ chồng gia quy vs Dâu kiểm toán viên sắc sảo; Mèo quýt béo ú vs Trùm xã hội đen.",
        "formula": "Sự va chạm giữa hai thế giới quan trái ngược tạo ra xung đột và tiếng cười tự nhiên"
    },
    {
        "rule_id": 5,
        "name": "Phản Sáo Lộ & Nghịch Chuyển Kỳ Vọng (Subverting Tropes)",
        "principle": "Khi khán giả nghĩ câu chuyện đi theo lối mòn A (khóc lóc tha thứ), kịch bản lập tức rẽ sang hướng B (rút dao rạch mặt, bỏ đi làm giàu, tuyệt đối không quay đầu).",
        "formula": "Dẫn dắt theo lối mòn cũ -> Bẻ ngoặt 180 độ ở giây phút quyết định"
    },
    {
        "rule_id": 6,
        "name": "Tiết Tấu Câu Ngắn Cho Tốc Độ Đọc 1.5x (Punchy Cadence)",
        "principle": "Tốc độ đọc 1.5x (346 từ/phút) đòi hỏi câu văn 10-20 từ. Dùng nhiều dấu phẩy ',', ba chấm '...', gạch ngang ' - ' để giọng đọc AI nhấn nhá truyền cảm.",
        "formula": "Câu ngắn gãy gọn + Điểm rơi dấu câu nhịp thở"
    },
    {
        "rule_id": 7,
        "name": "Show, Don't Tell (Hành Động Hóa Trạng Thái)",
        "principle": "Tuyệt đối không tóm tắt sự kiện khô khan. Miêu tả chi tiết bàn tay siết chặt, nhịp thở dồn dập, chiếc nhẫn cưới trượt rơi vào ly rượu vang.",
        "formula": "Hành động cụ thể + Chi tiết giác quan = Cảm xúc sống động"
    },
    {
        "rule_id": 8,
        "name": "Đảo Chiều Đa Tầng (Multi-Layered Plot Twist)",
        "principle": "Twist tầng 1 (Vả mặt bề mặt) -> Twist tầng 2 (Bóc trần âm mưu ngầm) -> Twist tầng 3 (Động cơ sâu xa / Dư âm lương tâm suốt đời).",
        "formula": "3 tầng lật kèo liên hoàn tạo dư chấn tâm lý mạnh mẽ"
    },
    {
        "rule_id": 9,
        "name": "Trả Thù Bằng Sự Nghiệp & Sự Tự Do (Sober Autonomy)",
        "principle": "Phụ nữ hiện đại không tranh giành đàn ông. Họ hả dạ nhất khi nhân vật chính độc lập tài chính, sự nghiệp thăng hoa và coi kẻ phản bội như rác rưởi.",
        "formula": "Tự do tài chính + Lạnh lùng buông bỏ = Sảng khoái tối thượng"
    },
    {
        "rule_id": 10,
        "name": "Cliffhanger Điểm Rơi Nghẹt Thở Cuối Tập 1 & 2 (卡点)",
        "principle": "Không bao giờ dừng tập khi câu chuyện đã giải quyết xong; dừng lại đúng 0.5 giây trước khi bí mật động trời được phơi bày hoặc ngay khi đối phương ra đòn hiểm.",
        "formula": "Cắt đúng đỉnh cao trào chưa giải quyết để kéo người nghe sang tập tiếp theo"
    }
]

# ==============================================================================
# 2. MÔ HÌNH 4 TẦNG BẤT ĐỐI XỨNG THÔNG TIN (INFORMATION ASYMMETRY ECONOMICS)
# ==============================================================================
INFORMATION_ASYMMETRY_MODEL = {
    "layers": {
        "fact_layer": "Sự thật khách quan: Biến cố thực tế diễn ra trong cốt truyện.",
        "narrator_layer": "Lời người kể chuyện: Có thể là Unreliable Narrator đánh lừa độc giả.",
        "character_layer": "Góc nhìn nhân vật: Tầm nhìn hạn chế của từng nhân vật trong bối cảnh.",
        "audience_layer": "Góc nhìn khán giả: Nhận thức được định hình qua dữ kiện nhận được."
    },
    "dynamics": {
        "audience_gt_character": "Khán giả biết > Nhân vật biết -> Tạo cảm giác Lo âu & Nghẹt thở ('Đừng mở cánh cửa đó!').",
        "character_gt_audience": "Nhân vật biết > Khán giả biết -> Tạo cảm giác Tò mò & Động cơ bí ẩn ('Tại sao lại quỳ trước người giao hàng?').",
        "narrator_gt_audience": "Người kể chuyện lừa Khán giả -> Tạo cảm giác Kinh ngạc cực độ (Mind-blowing Twist)."
    }
}

# ==============================================================================
# 3. MA TRẬN 10 TRƯỜNG PHÁI MỞ ĐẦU ĐỘC BẢN (DIVERSE HOOK ARCHETYPES 10)
# ==============================================================================
# Khắc phục triệt để lỗi "na ná nhau" giữa các audio. Mỗi archetype sở hữu giác quan neo đậu,
# nghịch lý vật lý và chiến thuật kép (Thoáng qua 12-20 từ vs Chi tiết cận cảnh 25-45 từ) riêng biệt.
DIVERSE_HOOK_ARCHETYPES_10 = [
    {
        "archetype_id": 1,
        "name": "Vật chứng pháp y & Kẽ hở thời gian (Forensic Timeline Hook)",
        "type": "Vật chứng pháp y & Kẽ hở thời gian",
        "sensory_anchor": "Mũi kim đồng hồ chết, vết cào dưới móng tay gãy, sợi len vướng khuy áo",
        "desc": "Neo vào vật chứng cơ học ở hiện trường chết chóc, chỉ ra nghịch lý thời gian và mối quan hệ thân nhân bí mật.",
        "example": "'Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, ngay dưới đáy móng tay gãy vụn của cô ấy là sợi len màu xanh cổ vịt - chiếc áo duy nhất tôi mặc trong ngày cưới.'",
        "strategy_a_flash": "Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, ngay dưới đáy móng tay gãy vụn của cô ấy là sợi len màu xanh cổ vịt - chiếc áo duy nhất tôi mặc trong ngày cưới.",
        "strategy_b_detailed": "Mảnh kính vỡ từ mặt đồng hồ Rolex rơi xuống sàn gạch men, phản chiếu kim giây chết cứng ở hai giờ mười bốn phút. Vị điều tra viên trưởng không nhìn thi thể, ông cúi xuống gắp từ kẽ móng tay cháy đen của nạn nhân một mẩu vải len màu xanh cổ vịt. Đó là chiếc áo dệt kim độc bản mẹ chồng vừa tặng tôi vào tiệc đính hôn tối qua.",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM", "NGUOC_TAM"]
    },
    {
        "archetype_id": 2,
        "name": "Âm thanh cơ khí đe dọa cận kề (Mechanical Acoustic Hook)",
        "type": "Âm thanh cơ khí đe dọa cận kề",
        "sensory_anchor": "Tiếng chốt thép ba lớp sập cạch, van xả khí áp lực cao, bọc chăn để lộ đầu búp bê cao su hỏng mắt",
        "desc": "Khoảng cách vật lý tính bằng milimét giữa sinh tử và sự xâm nhập, âm thanh va chạm cơ khí đanh thép.",
        "example": "'Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang.'",
        "strategy_a_flash": "Tiếng còi báo động boong ke vừa hú lên đợt thứ ba, van xả khí cay tự động đã khóa chặt chốt cơ học cuối cùng ngay trước mũi giày ả em họ.",
        "strategy_b_detailed": "Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang: 'Chị Lam ơi! Thằng bé sốt bốn mươi độ rồi, cho em xin mẩu nến và gói mì tôm thôi!'. Tôi không mở cửa. Tôi tựa lưng vào vách thép dày mười lăm phân, ngón tay đặt sẵn trên van xả khí cay áp suất cao. Qua lỗ quan sát hồng ngoại, chiếc bọc chăn bông trên tay ả khẽ xốc xếch, để lộ một góc đầu búp bê cao su hỏng một mắt.",
        "best_for": ["VO_HAN", "MAT_THE", "KINH_DI"]
    },
    {
        "archetype_id": 3,
        "name": "Nghịch lý tương phản trào phúng & Tiếng lòng (Satirical Subtext Hook)",
        "type": "Nghịch lý tương phản trào phúng & Tiếng lòng",
        "sensory_anchor": "Ngòi bút nạm kim cương cách chữ ký một milimét, cà vạt màu cánh sen chấm bi, tiếng lòng bóc phốt sắc lẹm",
        "desc": "Phá tan sự trang nghiêm của giới thượng lưu bằng sự thật trần trụi, hài hước và bóc mẽ âm mưu ngầm.",
        "example": "'Chiếc bút máy nạm kim cương của Lục Cảnh Hoài chỉ còn cách dòng chữ ký bản hợp đồng năm trăm tỷ đúng một milimét, thì một giọng nữ lanh lảnh bỗng dội thẳng vào màng nhĩ anh: Dừng bút lại đồ ngốc!'",
        "strategy_a_flash": "Ngòi bút năm trăm tỷ vừa chạm mặt giấy, tiếng lòng của tôi đã lanh lảnh dội vào tai sếp: 'Ký đi đồ ngốc, ký xong là nhảy lầu tập thể!'.",
        "strategy_b_detailed": "Chiếc bút máy nạm kim cương của Lục Cảnh Hoài chỉ còn cách dòng chữ ký bản hợp đồng năm trăm tỷ đúng một milimét, thì một giọng nữ lanh lảnh bỗng dội thẳng vào màng nhĩ anh: 'Dừng bút lại đồ ngốc! Bản hợp đồng này ký xuống là mất trắng năm trăm tỷ, chưa kể chiếc cà vạt hoa hòe màu cánh sen chấm bi của sếp nhìn y hệt con công đang xòe đuôi!'. Bàn tay đang cầm bút của vị tổng tài khựng lại giữa không trung.",
        "best_for": ["SA_DIEU", "HAI_HUOC", "HAO_MON"]
    },
    {
        "archetype_id": 4,
        "name": "Bạo lực lạnh & Cắt dòng tiền (Cold Violence Financial Hook)",
        "type": "Bạo lực lạnh & Cắt dòng tiền",
        "sensory_anchor": "Chiếc thìa mạ vàng chạm đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng, máy ghi âm mini",
        "desc": "Mẹ chồng - nàng dâu hoặc gia đấu gia tộc: nụ cười điềm đạm ngụy trang âm mưu đoạt tài sản, đáp trả bằng bẫy sao kê.",
        "example": "'Mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng vừa lộ ra dưới đáy bát yến sáu mươi triệu, ngón trỏ của tôi đã bấm nút phát loa ngoài chiếc điện thoại bàn.'",
        "strategy_a_flash": "Mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng vừa lộ ra dưới đáy bát yến sáu mươi triệu, ngón trỏ của tôi đã bấm nút phát loa ngoài chiếc điện thoại bàn.",
        "strategy_b_detailed": "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi. Bà Mai ngồi đối diện, chiếc vòng ngọc phỉ thúy trên cổ tay bà khẽ va vào thành bàn kính: Cạch! Tôi không cầm thìa. Tôi đẩy nhẹ chiếc máy ghi âm siêu nhỏ trong lòng bàn tay ra giữa bàn trà: 'Mẹ chu đáo quá. Nhưng mẹ có muốn nghe thử đoạn ghi âm mẹ chỉ đạo nhân viên bảo hiểm đổi người thụ hưởng hợp đồng hai trăm tỷ sang tên mẹ không?'.",
        "best_for": ["ME_CHONG", "GIA_DAU", "NGUOC_TAM"]
    },
    {
        "archetype_id": 5,
        "name": "Hành động quy tắc hiện trường (In-Action Rule Survival Hook)",
        "type": "Hành động quy tắc hiện trường",
        "sensory_anchor": "Khán phòng ba trăm chỗ niêm phong, bóng áo mưa đen sũng nước ngồi ghế số bốn, ánh đèn chiếu phim",
        "desc": "Dị thường thị giác phá vỡ trật tự không gian quen thuộc, nhân vật phản xạ lập tức theo quy tắc sinh tồn ngầm.",
        "example": "'Luồng sáng trắng từ buồng máy chiếu vừa rọi qua khe kính xuống khán phòng ba trăm chỗ, hàng ghế số bốn vốn niêm phong bỗng có người áo mưa đen ngồi bất động dù ngoài trời nắng ráo suốt ba tuần.'",
        "strategy_a_flash": "Tấm vé rạp phim rách mép vừa rơi xuống chân, bóng áo mưa đen sũng nước ở hàng ghế số bốn đã từ từ quay đầu một trăm tám mươi độ.",
        "strategy_b_detailed": "Luồng sáng trắng từ buồng máy chiếu vừa rọi qua khe kính xuống khán phòng ba trăm chỗ, hàng ghế số bốn vốn niêm phong bỗng có người áo mưa đen ngồi bất động dù ngoài trời nắng ráo suốt ba tuần. Tôi cúi gầm mặt, ngón tay bấu chặt vào cuộn băng dính phản quang trong túi áo khoác, tuyệt đối không chớp mắt nhìn vào chiếc gáy ướt sũng đang xoay ngược lại phía tôi.",
        "best_for": ["KINH_DI", "QUAI_DAM", "HUYEN_NGHI"]
    },
    {
        "archetype_id": 6,
        "name": "Đấu giá bất đối xứng thông tin (Information Asymmetry Auction Hook)",
        "type": "Đấu giá bất đối xứng thông tin",
        "sensory_anchor": "Búa gỗ gõ cắc một trăm tỷ, bút laser rọi bản đồ quy hoạch ngầm, ly rượu vang vỡ tan",
        "desc": "Kẻ thù tự đắc tưởng mình thắng đậm dự án thế kỷ, thực chất đang mua phải bãi rác hóa chất nợ ngập đầu.",
        "example": "'Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm.'",
        "strategy_a_flash": "Tiếng búa gõ cắc một trăm hai mươi tỷ cho bãi rác hóa chất vừa dứt, tôi thong thả buông biển đấu giá xuống mặt bàn bọc nhung đỏ.",
        "strategy_b_detailed": "Khoảnh khắc chiếc búa gỗ của đấu giá viên vừa giơ lên, ngón tay tôi đã khẽ bấm nhẹ chiếc bút laser kiểm tra bản đồ quy hoạch ngầm. Bạch Ngưng Băng ngồi ở hàng ghế VIP đối diện nở nụ cười đắc thắng, giơ cao biển đấu giá một trăm tỷ cho mảnh đất hoang phía nam thành phố. Ả ta không hề biết rằng, dưới lớp cát sâu mười mét của khu đất đó là bãi rác thải hóa chất công nghiệp bị chôn lấp trái phép từ hai mươi năm trước.",
        "best_for": ["TRONG_SINH", "VA_MAT", "HAO_MON"]
    },
    {
        "archetype_id": 7,
        "name": "Dược lý thâm cung & Ngự y cơ mật (Palace Toxicology Hook)",
        "type": "Dược lý thâm cung & Ngự y cơ mật",
        "sensory_anchor": "Trâm bạc nhúng chén hoa cúc sủi bọt xám tro, hương long diên ngạt mũi, tay áo thêu chỉ vàng",
        "desc": "Sự tàn khốc chốn hậu cung được ngụy trang bằng phép tắc và nụ cười hòa nhã của bậc mẫu nghi.",
        "example": "'Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng.'",
        "strategy_a_flash": "Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng.",
        "strategy_b_detailed": "Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng. Thục phi vẫn mỉm cười dịu dàng nâng tách trà lên môi tôi: 'Uống đi con dâu, trà nguội mất ngon'. Dưới ống tay áo thêu chim phượng bằng chỉ vàng lấp lánh, ngón tay đeo móng bạc của bà ta đang khẽ gõ nhịp xuống thành ghế đàn hương, từng nhịp từng nhịp như hồi chuông đòi mạng.",
        "best_for": ["CUNG_DAU", "TRACH_DAU", "NGUOC_TAM"]
    },
    {
        "archetype_id": 8,
        "name": "Âm thanh rợn gáy kinh dị đô thị (Acoustic Urban Horror Hook)",
        "type": "Âm thanh rợn gáy kinh dị đô thị",
        "sensory_anchor": "Tiếng cào móng tay khô khốc dưới dát giường gỗ ép, giọt nước bùn ao rỉ trán, căn hộ tầng bảy không cửa sổ",
        "desc": "Ám ảnh không gian kín và vật lý phi lý trí tại các tòa chung cư cũ hoặc phòng trọ sinh viên.",
        "example": "'Tiếng cào móng tay khô khốc dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh nhỏ thẳng vào giữa trán tôi, mang theo mùi bùn ao tanh tưởi.'",
        "strategy_a_flash": "Tiếng cào móng tay dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh mang mùi bùn ao nhỏ thẳng vào giữa trán tôi.",
        "strategy_b_detailed": "Tiếng cào móng tay khô khốc dưới dát giường gỗ ép vừa dừng bặt, một giọt nước lạnh tanh nhỏ thẳng vào giữa trán tôi, mang theo mùi bùn ao tanh tưởi giữa căn hộ tầng bảy không có cửa sổ. Tôi nín thở, ngón tay bấu chặt vào thanh sắt lan can giường tầng, cố ngăn chiếc răng hàm va vào nhau cầm cập khi nhìn thấy năm ngón tay tím tái đang từ từ luồn qua kẽ ván gỗ.",
        "best_for": ["KINH_DI", "QUAI_DAM", "VO_HAN"]
    },
    {
        "archetype_id": 9,
        "name": "Vật chứng số & Bẻ gãy cơ học học đường (Academic Whistleblower Hook)",
        "type": "Vật chứng số & Bẻ gãy cơ học học đường",
        "sensory_anchor": "Vỏ bút dạ quang vàng gãy làm đôi, thẻ nhớ micro SD 32GB rơi xuống bàn, màn hình in đề thi",
        "desc": "Xung đột trí tuệ học đường khốc liệt: bóc trần đường dây gian lận bằng dữ liệu số và chứng cứ vật lý.",
        "example": "'Vỏ bút dạ quang vừa bẻ gãy rơi chiếc thẻ nhớ ba mươi hai gigabyte chứa camera quay lén phòng in đề thi, tiếng chuông báo giờ thi học bổng đã vang lên.'",
        "strategy_a_flash": "Vỏ bút dạ quang vừa bẻ gãy rơi chiếc thẻ nhớ ba mươi hai gigabyte chứa camera quay lén phòng in đề thi, tiếng chuông báo giờ thi học bổng đã vang lên.",
        "strategy_b_detailed": "Rắc! Thân bút dạ quang màu vàng chanh gãy làm đôi dưới lực bấm của tôi, làm rơi ra chiếc thẻ nhớ micro SD ba mươi hai gigabyte chứa toàn bộ video quay lén phòng in đề thi quốc gia. Thủ khoa khối tự nhiên ngồi bàn trên quay ngoắt lại, cây bút chì kim hai bê trên tay hắn gãy vụn khi nhìn thấy chiếc đầu đọc thẻ nhớ đang cắm thẳng vào cổng USB chiếc máy tính giám thị.",
        "best_for": ["CUU_ROI", "THANH_XUAN", "TRINH_THAM"]
    },
    {
        "archetype_id": 10,
        "name": "Tử huyệt kiểm toán & Niêm phong con dấu (Corporate Forensic Seal Hook)",
        "type": "Tử huyệt kiểm toán & Niêm phong con dấu",
        "sensory_anchor": "Mũi kéo inox bấm đứt chỉ sáp đỏ niêm phong, tập hồ sơ ba mươi tỷ, còi xe thanh tra thuế rú dưới sảnh",
        "desc": "Thương trường khốc liệt: đòn kết liễu vào phút chót bằng niêm phong kiểm toán độc lập và cơ quan chức năng.",
        "example": "'Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong trên tập hồ sơ ba mươi tỷ, tiếng còi xe thanh tra thuế đã rú lên dưới sảnh.'",
        "strategy_a_flash": "Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong trên tập hồ sơ ba mươi tỷ, tiếng còi xe thanh tra thuế đã rú lên dưới sảnh.",
        "strategy_b_detailed": "Tách! Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong sáp đỏ trên tập hồ sơ chuyển giá ba mươi tỷ, tiếng còi xe thanh tra thuế và cảnh sát kinh tế đã rú lên inh ỏi dưới sảnh chính tòa nhà sáu mươi tầng. Vị tổng giám đốc vừa giơ ly rượu mừng bỗng khựng lại, giọt vang đỏ sóng sánh sánh tràn qua mép ly, nhỏ từng giọt đặc quánh xuống chiếc cà vạt lụa Hermes đắt giá của ông ta.",
        "best_for": ["HAO_MON", "VA_MAT", "TRONG_SINH"]
    }
]

# Alias tương thích ngược cho các module cũ
OPENING_HOOK_TEMPLATES_6 = DIVERSE_HOOK_ARCHETYPES_10[:6]

# ==============================================================================
# 3B. MA TRẬN 10 VŨ TRỤ NHÂN VẬT ĐỘC BẢN (10 CHARACTER UNIVERSES)
# ==============================================================================
# Đảm bảo các audio liên tiếp không bị lặp tên nhân vật hay bối cảnh nghề nghiệp
CHARACTER_UNIVERSES_10 = [
    {
        "universe_id": 1,
        "name": "Kiểm Toán Điều Tra & Thị Trường Vốn (Forensic Finance)",
        "domain": "Kiểm toán, ngân hàng đầu tư, chứng khoán",
        "protagonist_names": ["Thẩm Tri Ý", "Phó Trầm Uyên", "Cố Hàn Châu"],
        "antagonist_names": ["Hoàng Minh Triết", "Bà Mai", "Lục Vĩ Khang"],
        "supporting_names": ["Trưởng ban thanh tra Tề", "Luật sư Trần Bách"],
        "conflict_axis": "Chuyển giá xuyên biên giới & Thao túng phát hành trái phiếu",
        "best_for": ["HAO_MON", "ME_CHONG", "TRONG_SINH"]
    },
    {
        "universe_id": 2,
        "name": "Vi Phẫu Thần Kinh & Cấp Cứu Y Khoa (Neuro-Surgical Unit)",
        "domain": "Bệnh viện tuyến cuối, ghép tạng, tế bào gốc",
        "protagonist_names": ["Bác sĩ Lương Thế Vinh", "Bác sĩ Nhã Uyên"],
        "antagonist_names": ["Viện phó Chu Bá Khiêm", "Bác sĩ trưởng Doãn Hạo"],
        "supporting_names": ["Điều dưỡng trưởng Mỹ Linh", "Bệnh nhân lão tướng Phan"],
        "conflict_axis": "Đánh cắp bằng sáng chế mổ vi phẫu & Giả mạo chữ ký hồ sơ hiến tạng",
        "best_for": ["HUYEN_NGHI", "CUU_ROI", "NGUOC_TAM"]
    },
    {
        "universe_id": 3,
        "name": "Boong Ke Kỷ Băng Hà & Kỹ Thuật Sinh Tồn (Arctic Survival)",
        "domain": "Hầm ngầm công nghệ cao, cực hàn mạt thế",
        "protagonist_names": ["Kỹ sư cơ điện Trần Minh", "Nhà nông học Lê Na"],
        "antagonist_names": ["Đội trưởng tuần tra Tiêu Trạch", "Ả em họ Diệp Nhi"],
        "supporting_names": ["Bác sĩ già Nhậm", "Robot giám sát Alpha"],
        "conflict_axis": "Chiếm đoạt nguồn tuần hoàn nhiệt & Phá hoại chốt xả khí độc cách ly",
        "best_for": ["VO_HAN", "MAT_THE", "KINH_DI"]
    },
    {
        "universe_id": 4,
        "name": "Đội Tuyển Olympic Khoa Học Học Đường (Elite Academy)",
        "domain": "Trường nội trú trọng điểm, kỳ thi quốc gia",
        "protagonist_names": ["Nữ sinh nội trú Hạ Vy", "Thiên tài toán học Khang Duy"],
        "antagonist_names": ["Hội trưởng hội học sinh Trịnh Phong", "Tôn phu nhân"],
        "supporting_names": ["Thầy phụ trách in đề Trịnh Hưng", "Giám thị Đỗ"],
        "conflict_axis": "Đường dây tuồn đề thi quốc gia & Tống tiền bằng clip camera giấu kín",
        "best_for": ["CUU_ROI", "THANH_XUAN", "TRINH_THAM"]
    },
    {
        "universe_id": 5,
        "name": "Phục Chế Cổ Vật & Giám Định Ngọc (Heritage Restoration)",
        "domain": "Viện bảo tàng quốc gia, đấu giá cổ vật",
        "protagonist_names": ["Nhà phục chế Nguyễn Hoài Nam", "Nghệ nhân tranh lụa Lâm Diệp"],
        "antagonist_names": ["Trùm buôn đồ giả cổ Tống Khắc Lương", "Đấu giá viên Triệu Phàm"],
        "supporting_names": ["Giáo sư khảo cổ Trần Quốc Bảo", "Lão thợ kim hoàn họ Bùi"],
        "conflict_axis": "Tráo đổi ngọc tỉ truyền quốc bằng đá bột ép polymer phát quang",
        "best_for": ["HUYEN_NGHI", "VA_MAT", "TRONG_SINH"]
    },
    {
        "universe_id": 6,
        "name": "Tàu Hàng Container Viễn Dương (Deep Ocean Cargo)",
        "domain": "Hải trình quốc tế, siêu bão biển sâu",
        "protagonist_names": ["Hoa tiêu trưởng Vũ Đình", "Máy trưởng Quốc Huy"],
        "antagonist_names": ["Thuyền trưởng Đỗ Hồng Long", "Thủy thủ trưởng Sầm Hào"],
        "supporting_names": ["Thủy thủ trẻ Hải Đăng", "Bác sĩ tàu viễn dương"],
        "conflict_axis": "Vận chuyển công-ten-nơ rác phóng xạ trái phép qua vùng biển bão cấp 12",
        "best_for": ["VO_HAN", "HUYEN_NGHI", "KINH_DI"]
    },
    {
        "universe_id": 7,
        "name": "Thái Y Viện & Dược Điển Cung Đình (Imperial Pharmacy)",
        "domain": "Hoàng cung, ngự dược phòng, Đông cung",
        "protagonist_names": ["Nữ ngự y Diệp Uyển Thanh", "Tướng quân Tiêu Khải"],
        "antagonist_names": ["Thục phi Nhan Ngọc Dao", "Thái y viện trưởng Cố Đức Thuận"],
        "supporting_names": ["Cung nữ thân tín Như Ngọc", "Thái tử Tiêu Cảnh Hoan"],
        "conflict_axis": "Dùng độc hoa cà độc dược tẩm vào bánh hoa cúc hãm hại hoàng tự",
        "best_for": ["CUNG_DAU", "TRACH_DAU", "NGUOC_TAM"]
    },
    {
        "universe_id": 8,
        "name": "Khách Sạn Năm Sao & Ẩm Thực Michelin (Luxury Hospitality)",
        "domain": "Đại tiệc ngoại giao, bếp trưởng quốc tế",
        "protagonist_names": ["Giám đốc vận hành Đoàn Bảo Ngọc", "Bếp trưởng Henry Vũ"],
        "antagonist_names": ["Chủ tịch tập đoàn ẩm thực Doãn Thế Hào", "Thanh tra ẩm thực Pierre Đỗ"],
        "supporting_names": ["Phụ bếp trung thành Tiểu Lâm", "Nhà phê bình tự do Mai Phương"],
        "conflict_axis": "Cố tình pha chất gây sốc phản vệ vào món tráng miệng yến tiệc quốc tế",
        "best_for": ["HAO_MON", "SA_DIEU", "VA_MAT"]
    },
    {
        "universe_id": 9,
        "name": "An Ninh Dữ Liệu Số & Mạng Đám Mây (Cyber Forensics)",
        "domain": "Trung tâm an ninh mạng tài chính",
        "protagonist_names": ["Chuyên gia dấu vết số Đặng Quốc Phong", "Nữ hacker mũ trắng Minh Khuê"],
        "antagonist_names": ["Giám đốc công nghệ Tạ Quang", "Hacker chợ đen Bóng Đêm"],
        "supporting_names": ["Trưởng phòng máy chủ Bác Ba", "Cán bộ Cục An ninh mạng"],
        "conflict_axis": "Cài mã độc đào coin và đánh cắp mã OTP của ba triệu người dùng ví điện tử",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM", "VA_MAT"]
    },
    {
        "universe_id": 10,
        "name": "Lưu Trữ Điện Ảnh & Buồng Chiếu Phim Cũ (Cinema Archive)",
        "domain": "Rạp chiếu bóng cổ, bảo tàng phim nhựa",
        "protagonist_names": ["Kỹ thuật viên buồng chiếu Trần Hạo", "Biên kịch độc lập Băng Châu"],
        "antagonist_names": ["Nhà đầu tư giải tỏa Chu Văn Hùng", "Bảo vệ ca đêm Quách Tử"],
        "supporting_names": ["Nghệ nhân lồng tiếng Hoàng Lâm", "Cô bé bán vé dạo"],
        "conflict_axis": "Cuộn phim nhựa 35mm quay lại hiện trường vụ án mạng phòng kín 25 năm trước",
        "best_for": ["KINH_DI", "QUAI_DAM", "HUYEN_NGHI"]
    }
]

# ==============================================================================
# 3C. MA TRẬN 10 CƠ CHẾ KẾT THÚC & LẬT KÈO ĐỘC BẢN (10 DIVERSE RESOLUTIONS)
# ==============================================================================
# Chấm dứt triệt để việc truyện nào cũng kết thúc bằng "công an ập vào" hoặc "thanh tra thuế"
DIVERSE_RESOLUTIONS_10 = [
    {
        "resolution_id": 1,
        "name": "Cháy tài khoản ký quỹ đòn bẩy (Margin Call Liquidation)",
        "mechanism": "Phản diện dốc toàn lực đầu cơ khống, nhân vật chính tháo gỡ đòn bẩy khiến đối phương phá sản tức thì sau 30 giây công bố số liệu.",
        "best_for": ["HAO_MON", "VA_MAT"]
    },
    {
        "resolution_id": 2,
        "name": "Đảo ngược quy tắc sinh tồn (Rule Inversion Trap)",
        "mechanism": "Kích hoạt điều khoản ngầm số 0 trong quy tắc, biến chính kẻ đi săn thành con mồi chịu hình phạt trong không gian kín.",
        "best_for": ["KINH_DI", "QUAI_DAM", "VO_HAN"]
    },
    {
        "resolution_id": 3,
        "name": "Phát trực tiếp dữ liệu ẩn lên màn hình quảng trường (Digital Forensic Stream)",
        "mechanism": "Dữ liệu camera ngầm và ghi âm giao dịch bẩn được truyền phát tự động lên màn hình LED giữa tiệc mừng, không thể cắt sóng.",
        "best_for": ["ME_CHONG", "TRONG_SINH"]
    },
    {
        "resolution_id": 4,
        "name": "Giám định chuỗi gien và vết sáp niêm phong cổ (Forensic Pathology Match)",
        "mechanism": "Vết mực niêm phong và ADN trên di vật lịch sử chỉ ra kẻ giả mạo huyết thống ngay trước hội đồng gia tộc.",
        "best_for": ["HUYEN_NGHI", "TRINH_THAM"]
    },
    {
        "resolution_id": 5,
        "name": "Kích hoạt thư tín thác công chứng 15 năm trước (Time Capsule Will)",
        "mechanism": "Bản di chúc gửi tại ngân hàng Thụy Sĩ có hiệu lực tự động khi phát sinh giao dịch bất thường, vô hiệu hóa toàn bộ quyền sở hữu giả mạo.",
        "best_for": ["NGUOC_TAM", "CUU_ROI"]
    },
    {
        "resolution_id": 6,
        "name": "Phản ứng đổi màu của giấy quỳ thử độc (Chemical Toxic Indicator)",
        "mechanism": "Giọt nước canh nhỏ lên vạt áo thêu ngự ban chuyển sang màu tím than, làm bại lộ thuốc độc ngay trước mặt sứ thần các nước.",
        "best_for": ["CUNG_DAU", "TRACH_DAU"]
    },
    {
        "resolution_id": 7,
        "name": "Trích xuất nhật ký truy cập máy chủ 2h sáng (Server Audit Log Extraction)",
        "mechanism": "Địa chỉ MAC máy tính cá nhân và dấu vân tay trên máy photocopy in đề thi bóc trần thủ phạm gian lận trước hội đồng tuyển sinh.",
        "best_for": ["THANH_XUAN", "CUU_ROI"]
    },
    {
        "resolution_id": 8,
        "name": "Đóng sập cửa áp suất cơ học cách ly (Pressure Isolation Containment)",
        "mechanism": "Khóa van điều áp cô lập kẻ phản trắc ở khoang ngoài khi bão tuyết ập tới, bảo toàn toàn bộ hệ thống dự trữ cho người vô tội.",
        "best_for": ["MAT_THE", "VO_HAN"]
    },
    {
        "resolution_id": 9,
        "name": "Phán quyết hủy giao dịch do lừa dối (Civil Fraud Void Judgment)",
        "mechanism": "Tòa án tuyên bố hợp đồng tặng cho tài sản vô hiệu từ thời điểm xác lập do có hành vi gian dối, thu hồi từng xu tiền bất chính.",
        "best_for": ["GIA_DAU", "ME_CHONG"]
    },
    {
        "resolution_id": 10,
        "name": "Tự thú vì hiểu lầm tiếng lòng là thần dụ (Satirical Psychological Collapse)",
        "mechanism": "Phản diện tưởng bí mật sát hại của mình đã bị thần linh soi xét qua tiếng lòng của nhân vật chính, tự khai ra toàn bộ đồng bọn trước hội trường.",
        "best_for": ["SA_DIEU", "HAI_HUOC"]
    }
]

# ==============================================================================
# 4. MA TRẬN 5 LOẠI ĐIỂM SẢNG (SATISFACTION MATRIX)
# ==============================================================================
SATISFACTION_MATRIX_5 = {
    "identity_crushing": {
        "name": "Nghiền ép thân phận",
        "formula": "Bị sỉ nhục -> Nhẫn nhịn -> Lộ thân phận thật -> Toàn trường quỳ gối xin tha",
        "weight": 0.35
    },
    "face_slapping_revenge": {
        "name": "Vả mặt báo thù",
        "formula": "Phản diện đắc chí -> Bẫy sập -> Chứng cứ công khai đanh thép -> Phản diện thân bại danh liệt",
        "weight": 0.40
    },
    "counterattack_turnaround": {
        "name": "Nghịch tập lật kèo",
        "formula": "Rơi vào tuyệt cảnh -> Kích hoạt bài tẩy / Trí tuệ chiến thuật -> Lật ngược thế cờ",
        "weight": 0.15
    },
    "emotional_explosion": {
        "name": "Cảm xúc bùng nổ / Thiên vị độc sủng",
        "formula": "Bị cô lập -> Người quyền lực nhất đứng ra che chở vô điều kiện -> Hóa giải hiểu lầm",
        "weight": 0.10
    },
    "mystery_unveiling": {
        "name": "Giải mã chân tướng kinh hoàng",
        "formula": "Manh mối Chekhov -> Suy luận sắc bén -> Bóc trần kẻ thủ ác ngụy trang thánh thiện",
        "weight": 0.20
    }
}

# ==============================================================================
# 5. HỆ THỐNG 4 TẦNG PHẢN DIỆN (4-TIER VILLAIN SYSTEM)
# ==============================================================================
VILLAIN_SYSTEM_4 = [
    {"tier": 1, "role": "Pháo hôi (Cannon Fodder)", "timing": "Tập 1 (0-15%)", "purpose": "Sỉ nhục nhân vật chính để làm ngòi nổ, bị vả mặt nhanh chóng để tạo đà hưng phấn."},
    {"tier": 2, "role": "Trung phản diện (Mid-level)", "timing": "Tập 2 (15-60%)", "purpose": "Kẻ ngáng đường có thực lực, giở thủ đoạn dơ bẩn dồn nhân vật chính vào thế khó."},
    {"tier": 3, "role": "Đại phản diện (Ultimate Boss)", "timing": "Tập 3 (60-90%)", "purpose": "Trùm cuối có quyền thế khổng lồ, cuộc đấu trí sinh tử trực diện."},
    {"tier": 4, "role": "Ẩn tàng phản diện (Hidden Betrayer)", "timing": "Tập 3 (Cao trào)", "purpose": "Người thân tín nhất phản trắc, phải có ít nhất 3 phục bút từ Tập 1 để tạo cảm giác rùng mình (细思极恐)."}
]


class ChineseStoryKnowledgeBase:
    """
    Cơ sở dữ liệu tri thức biên kịch chứa 100 tác phẩm đoản văn kinh điển
    và hệ thống tra cứu thông minh hỗ trợ Agent 2 (Biên kịch).
    """

    def __init__(self):
        self._all_stories: List[Dict[str, Any]] = []
        self._genre_map: Dict[str, List[Dict[str, Any]]] = {}
        self._load_and_index()

    def _load_and_index(self) -> None:
        """Nạp toàn bộ 100 tác phẩm từ 10 modules và lập chỉ mục"""
        genre_collections = [
            ("NGUOC_TAM", STORIES_GENRE_1),
            ("TRONG_SINH", STORIES_GENRE_2),
            ("HUYEN_NGHI", STORIES_GENRE_3),
            ("ME_CHONG", STORIES_GENRE_4),
            ("HAO_MON", STORIES_GENRE_5),
            ("KINH_DI", STORIES_GENRE_6),
            ("SA_DIEU", STORIES_GENRE_7),
            ("CUNG_DAU", STORIES_GENRE_8),
            ("CUU_ROI", STORIES_GENRE_9),
            ("VO_HAN", STORIES_GENRE_10),
        ]

        self._all_stories = []
        for genre_key, stories_list in genre_collections:
            self._genre_map[genre_key] = list(stories_list)
            for s in stories_list:
                s_copy = dict(s)
                s_copy["genre_key"] = genre_key
                self._all_stories.append(s_copy)

        # Nạp động các tác phẩm cào từ Crawl4AI trong data/crawled_stories/
        crawled_dir = root_dir / "data" / "crawled_stories"
        crawled_count = 0
        if crawled_dir.exists():
            for json_path in crawled_dir.glob("*.json"):
                try:
                    with open(json_path, "r", encoding="utf-8") as f:
                        c_data = json.load(f)
                    title = c_data.get("title", json_path.stem)
                    meta = c_data.get("metadata", {})
                    analysis = c_data.get("analysis", {})
                    
                    # Tự động phân loại genre_key
                    g_key = "NGUOC_TAM"
                    text_blob = f"{title} {meta.get('genre', '')} {c_data.get('content', '')[:600]}".lower()
                    if any(w in text_blob for w in ["trọng sinh", "vả mặt", "sảng văn", "thức tỉnh"]):
                        g_key = "TRONG_SINH"
                    elif any(w in text_blob for w in ["án mạng", "trinh thám", "pháp y", "camera"]):
                        g_key = "HUYEN_NGHI"
                    elif any(w in text_blob for w in ["mẹ chồng", "nàng dâu", "ly hôn", "gia đình"]):
                        g_key = "ME_CHONG"
                    elif any(w in text_blob for w in ["tổng tài", "hào môn", "hợp đồng", "thái tử"]):
                        g_key = "HAO_MON"
                    elif any(w in text_blob for w in ["quái đàm", "kinh dị", "quy tắc", "bệnh viện đêm"]):
                        g_key = "KINH_DI"
                    elif any(w in text_blob for w in ["sa điêu", "tiếng lòng", "hài hước", "tấu hài"]):
                        g_key = "SA_DIEU"
                    elif any(w in text_blob for w in ["cung đấu", "trạch đấu", "hoàng hậu"]):
                        g_key = "CUNG_DAU"
                    elif any(w in text_blob for w in ["cứu rỗi", "chữa lành", "thanh xuân"]):
                        g_key = "CUU_ROI"
                    elif any(w in text_blob for w in ["mạt thế", "vô hạn", "tích trữ", "kỷ băng hà"]):
                        g_key = "VO_HAN"

                    c_story = {
                        "id": 1000 + len(self._all_stories),
                        "title_vn": title,
                        "title_cn": title,
                        "author_platform": f"{meta.get('platform', 'Crawl4AI')} - {meta.get('url', '')}",
                        "genre": meta.get("genre", "Đoản văn cào tự động"),
                        "premise": analysis.get("pacing_beat_sheet", {}).get("hoi_1_thiet_lap_va_hook", title),
                        "characters": f"- Nhân vật chính: Xây dựng theo mô-típ {g_key}\n- Đối kháng: Phản diện leo thang",
                        "golden_hook": analysis.get("golden_retention_hook_5s", ""),
                        "acts_and_pacing": f"Hồi 1: {analysis.get('pacing_beat_sheet', {}).get('hoi_1_thiet_lap_va_hook', '')}\nHồi 2: {analysis.get('pacing_beat_sheet', {}).get('hoi_2_nen_ap_suat_va_leo_thang', '')}\nHồi 3: {analysis.get('pacing_beat_sheet', {}).get('hoi_3_bung_no_va_sa_van_shuangdian', '')}",
                        "plot_twist": analysis.get("cliffhanger_or_ending", ""),
                        "core_lessons": "\n".join(analysis.get("scriptwriting_takeaways", ["Áp dụng từ dữ liệu Crawl4AI"])),
                        "genre_key": g_key,
                        "is_crawled": True
                    }
                    self._all_stories.append(c_story)
                    self._genre_map.setdefault(g_key, []).append(c_story)
                    crawled_count += 1
                except Exception as e:
                    logger.debug(f"Không thể nạp file crawled story {json_path}: {e}")

        logger.info(f"Đã lập chỉ mục thành công {len(self._all_stories)} tác phẩm trong Knowledge Base (bao gồm {crawled_count} truyện cào từ Crawl4AI).")

    @property
    def total_stories(self) -> int:
        return len(self._all_stories)

    def get_all_stories(self) -> List[Dict[str, Any]]:
        return self._all_stories

    def get_golden_rules(self) -> List[Dict[str, Any]]:
        return GOLDEN_RULES_10

    def query_masterclass(
        self,
        topic_title: str = "",
        topic_summary: str = "",
        category: Optional[VideoCategory] = None,
        top_k: int = 3,
        genre_hint: str = "",
        exclude_archetype_ids: Optional[List[int]] = None,
        exclude_universe_ids: Optional[List[int]] = None,
        exclude_resolution_ids: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """
        Tra cứu cơ sở dữ liệu để tìm ra các case study và bài học tương đồng nhất.
        Được gọi bắt buộc trước mỗi lần biên kịch sinh kịch bản mới.
        """
        text_corpus = f"{topic_title} {topic_summary} {genre_hint}".lower()
        
        # 1. Định hướng nhóm thể loại ưu tiên
        target_genre_keys = []
        if genre_hint:
            gh = genre_hint.upper().strip()
            for k in ["NGUOC_TAM", "TRONG_SINH", "HUYEN_NGHI", "ME_CHONG", "HAO_MON", "KINH_DI", "SA_DIEU", "CUNG_DAU", "CUU_ROI", "VO_HAN"]:
                if k in gh or gh in k:
                    if k not in target_genre_keys:
                        target_genre_keys.append(k)

        if any(w in text_corpus for w in ["nguoc", "ngược", "hỏa táng", "hoa tang", "bạch nguyệt quang", "the than", "thế thân", "bỏ lỡ", "tàn tâm", "tan tam"]):
            if "NGUOC_TAM" not in target_genre_keys: target_genre_keys.append("NGUOC_TAM")
        if any(w in text_corpus for w in ["trong_sinh", "trọng sinh", "vả mặt", "va mat", "thiên kim", "thien kim", "sống lại", "song lai", "thức tỉnh", "sảng văn"]):
            if "TRONG_SINH" not in target_genre_keys: target_genre_keys.append("TRONG_SINH")
        if any(w in text_corpus for w in ["huyen_nghi", "trinh_tham", "án mạng", "an mang", "camera", "phòng kín", "thám tử", "sát nhân", "công an", "pháp y", "manh mối", "50 mét"]):
            if "HUYEN_NGHI" not in target_genre_keys: target_genre_keys.append("HUYEN_NGHI")
        if any(w in text_corpus for w in ["me_chong", "mẹ chồng", "nàng dâu", "nang dau", "sính lễ", "nhà chồng", "ly hôn", "ngoại tình", "tiểu tam", "em trai chồng", "ma đệ ma", "cực phẩm"]):
            if "ME_CHONG" not in target_genre_keys: target_genre_keys.append("ME_CHONG")
        if any(w in text_corpus for w in ["hao_mon", "hợp đồng", "tổng tài", "tong tai", "100 tỷ", "hào môn", "gả thay", "thái tử", "giả nghèo", "cưới trước yêu sau"]):
            if "HAO_MON" not in target_genre_keys: target_genre_keys.append("HAO_MON")
        if any(w in text_corpus for w in ["kinh_di", "quai_dam", "quy tắc", "quái đàm", "kinh dị", "bệnh viện đêm", "ký túc xá", "ma-nơ-canh", "sinh tồn"]):
            if "KINH_DI" not in target_genre_keys: target_genre_keys.append("KINH_DI")
        if any(w in text_corpus for w in ["sa_dieu", "hai_huoc", "tiếng lòng", "tieng long", "đọc suy nghĩ", "mèo", "tấu hài", "sa điêu", "hài hước", "nhầm tin nhắn", "phản sáo lộ"]):
            if "SA_DIEU" not in target_genre_keys: target_genre_keys.append("SA_DIEU")
        if any(w in text_corpus for w in ["cung_dau", "trach_dau", "cung đấu", "hoàng hậu", "thám hoa", "thứ nữ", "khoa cử", "vương phi", "trạch đấu"]):
            if "CUNG_DAU" not in target_genre_keys: target_genre_keys.append("CUNG_DAU")
        if any(w in text_corpus for w in ["cuu_roi", "chua_lanh", "chữa lành", "thanh xuân", "học bá", "khiếm thính", "bức thư", "hộp thời gian", "bác trương", "cứu rỗi"]):
            if "CUU_ROI" not in target_genre_keys: target_genre_keys.append("CUU_ROI")
        if any(w in text_corpus for w in ["vo_han", "mat_the", "mạt thế", "bão tuyết", "kỷ băng hà", "tích trữ", "vô hạn lưu", "zombie", "thần chết", "axit"]):
            if "VO_HAN" not in target_genre_keys: target_genre_keys.append("VO_HAN")

        # Fallback theo Category nếu không tìm thấy từ khóa
        if not target_genre_keys:
            if category == VideoCategory.HIGH_IQ:
                target_genre_keys = ["HUYEN_NGHI", "VO_HAN", "KINH_DI"]
            else:
                target_genre_keys = ["HAO_MON", "ME_CHONG", "NGUOC_TAM", "CUU_ROI"]

        # 2. Chấm điểm tương đồng cho các tác phẩm trong các nhóm ưu tiên
        scored_stories = []
        for s in self._all_stories:
            score = 0
            if s["genre_key"] in target_genre_keys:
                score += 10
            
            # Khớp từ khóa cụ thể trong tên và premise
            search_blob = f"{s['title_vn']} {s['premise']} {s['genre']}".lower()
            tokens = [t for t in re.split(r"\W+", text_corpus) if len(t) >= 2]
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
            })

        # 4. CHỐNG ĐỒNG HÓA & LỰA CHỌN ĐỘC BẢN (ANTI-HOMOGENIZATION ENGINE):
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
        matched_resolution = _pick_least_recently_used(compatible_res, exclude_resolution_ids or [], "resolution_id")

        return {
            "status": "CONSULTED_SUCCESS",
            "total_knowledge_pool": self.total_stories,
            "target_genres": target_genre_keys,
            "relevant_cases": brief_cases,
            "golden_rules": GOLDEN_RULES_10,
            "recommended_hook_template": matched_hook_archetype,
            "recommended_hook_archetype": matched_hook_archetype,
            "recommended_character_universe": matched_universe,
            "recommended_resolution": matched_resolution,
            "diverse_hooks_catalog": DIVERSE_HOOK_ARCHETYPES_10,
            "character_universes_catalog": CHARACTER_UNIVERSES_10,
            "diverse_resolutions_catalog": DIVERSE_RESOLUTIONS_10,
            "satisfaction_matrix": SATISFACTION_MATRIX_5,
            "villain_system": VILLAIN_SYSTEM_4,
            "information_asymmetry": INFORMATION_ASYMMETRY_MODEL,
            "voice_pacing_standard": {
                "reading_speed_multiplier": 1.5,
                "words_per_minute": 346,
                "min_words_per_part": 3460,
                "target_total_words_30min": 10380,
                "sentence_length": "10-20 words per sentence",
                "punctuation_density": "High (commas, ellipses, dashes for breathing pauses)"
            }
        }

    def consult_before_writing(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:
        """
        Hàm bắt buộc gọi trước khi biên soạn bất kỳ kịch bản nào.
        Tự động tra cứu lịch sử các audio gần nhất để xoay vòng Hook Archetype, Vũ trụ nhân vật và Cơ chế lật kèo,
        triệt tiêu 100% tình trạng các audio bị na ná hay lặp lại mô-típ.
        Gắn kèm consultation_token duy nhất để làm thẻ bài thông qua Cổng Kiểm Duyệt Tri Thức.
        """
        consult_log_path = root_dir / "data" / "knowledge_consultations.jsonl"
        recent_archetypes: List[int] = []
        recent_universes: List[int] = []
        recent_resolutions: List[int] = []

        if consult_log_path.exists():
            try:
                with open(consult_log_path, "r", encoding="utf-8") as f:
                    lines = [ln.strip() for ln in f if ln.strip()]
                for line in lines[-6:]:
                    try:
                        record = json.loads(line)
                        if record.get("hook_archetype_id"):
                            recent_archetypes.append(record["hook_archetype_id"])
                        if record.get("universe_id"):
                            recent_universes.append(record["universe_id"])
                        if record.get("resolution_id"):
                            recent_resolutions.append(record["resolution_id"])
                    except Exception:
                        pass
            except Exception as e:
                logger.debug(f"Không thể đọc lịch sử consultation: {e}")

        brief = self.query_masterclass(
            topic_title=topic_title,
            topic_summary=topic_summary,
            category=category,
            top_k=top_k,
            genre_hint=genre_hint,
            exclude_archetype_ids=recent_archetypes,
            exclude_universe_ids=recent_universes,
            exclude_resolution_ids=recent_resolutions
        )

        token = f"TOKEN_KB_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.urandom(4).hex()}"
        brief["consultation_token"] = token
        brief["consulted_at"] = datetime.now().isoformat()

        # Ghi log lịch sử tra cứu (Audit Trail)
        consult_log_path.parent.mkdir(parents=True, exist_ok=True)
        hook_obj = brief.get("recommended_hook_archetype", {})
        univ_obj = brief.get("recommended_character_universe", {})
        res_obj = brief.get("recommended_resolution", {})

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "consultation_token": token,
            "query_title": topic_title,
            "target_genres": brief.get("target_genres", []),
            "matched_cases": [c["title"] for c in brief.get("relevant_cases", [])],
            "hook_archetype_id": hook_obj.get("archetype_id"),
            "hook_archetype_name": hook_obj.get("name"),
            "universe_id": univ_obj.get("universe_id"),
            "universe_name": univ_obj.get("name"),
            "resolution_id": res_obj.get("resolution_id"),
            "resolution_name": res_obj.get("name"),
            "status": "VERIFIED_BEFORE_WRITING"
        }

        try:
            with open(consult_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        except Exception as e:
            logger.warning(f"Không thể ghi log consultation: {e}")

        return brief

    def format_brief_for_prompt(self, brief: Dict[str, Any]) -> str:
        """
        Định dạng bản tóm tắt tri thức thành chuỗi văn bản nạp trực tiếp vào Prompt của LLM
        để bảo đảm LLM phải soi chiếu vào kinh nghiệm này trước khi viết.
        """
        lines = []
        lines.append("=" * 65)
        lines.append("📚 [BỘ CƠ SỞ TRI THỨC 100 KỊCH BẢN KINH ĐIỂN ĐÃ ĐƯỢC TRA CỨU]:")
        lines.append("Hệ thống đã tự động đối soát kho tàng 100 tác phẩm đoản văn triệu view và chọn lọc các Case Study tinh hoa nhất để làm hình mẫu:")
        
        for idx, c in enumerate(brief.get("relevant_cases", []), 1):
            lines.append(f"\n--- CASE STUDY THAM CHIẾU #{idx}: {c['title']} ---")
            lines.append(f" * Nguồn & Tác giả: {c['author']} | Thể loại: {c['genre']}")
            lines.append(f" * Tiền đề nghịch lý: {c['premise']}")
            lines.append(f" * Tạo hình nhân vật mẫu:\n{c['character_setup']}")
            lines.append(f" * Hook mở màn 5s mẫu: {c['sample_hook_5s']}")
            lines.append(f" * Màn bẻ lái Plot Twist mẫu: {c['plot_twist_essence']}")
            lines.append(f" * Tinh hoa cần áp dụng:\n{c['key_takeaways']}")

        hook_rec = brief.get("recommended_hook_archetype", {})
        univ_rec = brief.get("recommended_character_universe", {})
        res_rec = brief.get("recommended_resolution", {})

        if hook_rec:
            lines.append(f"\n⚡ [ARCHETYPE MỞ ĐẦU ĐỘC BẢN ĐƯỢC CHỈ ĐỊNH]: {hook_rec.get('name')}")
            lines.append(f" * Neo đậu giác quan: {hook_rec.get('sensory_anchor')}")
            lines.append(f" * Mẫu Chiến thuật A (Thoáng qua 12-20 từ): {hook_rec.get('strategy_a_flash')}")
            lines.append(f" * Mẫu Chiến thuật B (Chi tiết cận cảnh 25-45 từ): {hook_rec.get('strategy_b_detailed')}")

        if univ_rec:
            lines.append(f"\n🎭 [VŨ TRỤ NHÂN VẬT ĐỘC BẢN ĐƯỢC CHỈ ĐỊNH - CHỐNG TRÙNG LẶP]: {univ_rec.get('name')}")
            lines.append(f" * Lĩnh vực bối cảnh: {univ_rec.get('domain')}")
            lines.append(f" * Nhân vật chính đề xuất: {', '.join(univ_rec.get('protagonist_names', []))}")
            lines.append(f" * Phản diện đề xuất: {', '.join(univ_rec.get('antagonist_names', []))}")
            lines.append(f" * Trục xung đột cốt lõi: {univ_rec.get('conflict_axis')}")

        if res_rec:
            lines.append(f"\n💥 [CƠ CHẾ LẬT KÈO ĐỘC BẢN - CHỐNG CÔNG AN/THUẾ RẬP KHUÔN]: {res_rec.get('name')}")
            lines.append(f" * Cơ chế: {res_rec.get('mechanism')}")

        lines.append("\n🎯 10 ĐỊNH LUẬT VÀNG BẮT BUỘC ÁP DỤNG:")
        for r in brief.get("golden_rules", [])[:5]:
            lines.append(f" - [Định luật {r['rule_id']} - {r['name']}]: {r['principle']}")

        lines.append("\n⚡ NGHỆ THUẬT NGẮT NHỊP CHO GIỌNG ĐỌC AI TỐC ĐỘ 1.5X:")
        lines.append(" - Câu văn gãy gọn 10-20 từ. Sử dụng nhiều dấu phẩy ',', dấu ba chấm '...', gạch ngang ' - ' để tạo khoảng lặng kịch tính.")
        lines.append(" - Tổng 3 tập bắt buộc >= 10,380 từ (mỗi tập >= 3,460 từ) cho thời lượng tròn 30 phút audio.")
        lines.append("=" * 65)

        return "\n".join(lines)


# Singleton instance để tái sử dụng toàn hệ thống
_GLOBAL_KNOWLEDGE_BASE: Optional[ChineseStoryKnowledgeBase] = None

def get_knowledge_base() -> ChineseStoryKnowledgeBase:
    global _GLOBAL_KNOWLEDGE_BASE
    if _GLOBAL_KNOWLEDGE_BASE is None:
        _GLOBAL_KNOWLEDGE_BASE = ChineseStoryKnowledgeBase()
    return _GLOBAL_KNOWLEDGE_BASE

def require_knowledge_consultation(
    category: Optional[VideoCategory] = None,
    topic_title: str = "",
    topic_summary: str = "",
    top_k: int = 3,
    genre_hint: str = ""
) -> Dict[str, Any]:
    """Hàm tiện ích toàn cục bắt buộc gọi trước khi tạo bất kỳ kịch bản nào"""
    kb = get_knowledge_base()
    return kb.consult_before_writing(category=category, topic_title=topic_title, topic_summary=topic_summary, top_k=top_k, genre_hint=genre_hint)


class KnowledgeGateViolationError(Exception):
    """
    Ngoại lệ nghiêm ngặt: Ném ra khi một tiến trình biên kịch cố tình bỏ qua
    bước tra cứu Cơ sở dữ liệu 100 tác phẩm kinh điển!
    """
    pass


def verify_knowledge_gate(consult_data: Optional[Dict[str, Any]]) -> bool:
    """
    Cổng kiểm duyệt tri thức bắt buộc (Mandatory Knowledge Gate):
    Xác minh xem kịch bản đã được đối soát qua Cơ sở tri thức 100 bộ truyện kinh điển chưa.
    Nếu chưa -> Ném ngoại lệ KnowledgeGateViolationError và từ chối sinh kịch bản.
    """
    if not consult_data or not isinstance(consult_data, dict):
        raise KnowledgeGateViolationError(
            "🚨 VI PHẠM NGUYÊN TẮC BIÊN KỊCH: "
            "Bắt buộc phải tra cứu Cơ sở tri thức 100 tác phẩm đoản văn kinh điển "
            "(thông qua 'require_knowledge_consultation' hoặc 'consult_before_writing') "
            "trước khi tiến hành lập dàn ý hoặc sinh kịch bản!"
        )

    token = consult_data.get("consultation_token")
    cases = consult_data.get("relevant_cases", [])

    if not token or not cases:
        raise KnowledgeGateViolationError(
            "🚨 CƠ SỞ TRI THỨC CHƯA ĐƯỢC ĐỐI SOÁT HỢP LỆ: "
            "Dữ liệu tư vấn thiếu Thẻ bài tri thức (consultation_token) "
            "hoặc danh sách Case Study tham chiếu hợp lệ!"
        )

    logger.info(f"✅ Knowledge Gate PASSED! Thẻ bài tri thức: {token} ({len(cases)} Case Studies được bảo chứng).")
    return True

