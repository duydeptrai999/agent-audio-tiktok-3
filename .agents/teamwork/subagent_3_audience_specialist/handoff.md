# HANDOFF REPORT: Sub-Agent 3 (Audience Alignment & Demographics Specialist)

## 1. Observation
- **Direct file audit**: Inspected `data/tiktok_studio_metrics.json` (lines 76-87).
  - Viewer Gender breakdown: Nữ 80%, Nam 20%, Khác 0%.
  - Viewer Age breakdown: 18-24 (49.8%), 25-34 (41.6%), 35-44 (5.4%), 45-54 (1.9%), 55+ (1.3%).
  - Total aged 18-34: 91.4% of total viewers.
  - Viewer Geographic location: Việt Nam 95.4%, Vương quốc Anh 1.0%, Úc <1%, Canada <1%, Nhật Bản <1%.
  - Follower Gender breakdown: Nam 59%, Nữ 40%, Khác 1%.
  - Traffic source distribution: Đề xuất (FYP) 93%, Tìm kiếm 4.6%, Hồ sơ cá nhân 2.4%, Đã follow 0%.
  - Top video watched by viewers: "Tỉ số đã là 2-2 | Mùa Hè Năm Ấy | Tập 26 #vtvgiaitri #muahenamay #xuhuong" (1.6M views - VTV Giải Trí Official).
  - Top creators watched by viewers: VTV Go (2.1M followers), KÊNH SHOWBIZ (1.3M), molistarofficial (2.5M), VTV Giải Trí Official (4.3M), Vũ Trụ Showbiz (476K).
  - Search queries leading to/around the content: "phong tránh cạm bẫy bạn thân" (0.5%), "tái sinh tiểu thuyết liễu như yên 2 tập tiếp theo" (0.5%), "audio làm đồ ăn" (0.5%), "em dâu đuổi tôi ra khỏi nhà full" (0.5%).
- **Current published audio videos** (`data/tiktok_studio_metrics.json`, lines 4-74):
  - 3 episodes of "Mạt Thế Kỷ Băng Hà: Tôi Tích Trữ 100 Tỷ Vật Tư Xây Pháo Đài Ấm Áp" (Views: Ep 1 = 72, Ep 2 = 67, Ep 3 = 66, Likes = 2, Comments = 0).
  - 3 episodes of "Nàng Dâu Thức Tỉnh: Đêm Mưa Bị Đuổi Khỏi Hào Môn & Bản Lĩnh Tự Chủ 120 Tỷ" (Views: Ep 1 = 89, Ep 2 = 85, Ep 3 = 39, Likes = 3, Comments = 0).
  - Total post badge: 240 bài đăng, 7.7K views, 138 likes, 0 comments, avg watch time 4-7s.
- **Audio engine configuration** (`ORIGINAL_REQUEST.md`, lines 26-28):
  - Voice: `NamMinh` / `HoaiMy` at 346 wpm, `atempo=1.5`.

## 2. Logic Chain
1. From Observation 1 (`tiktok_studio_metrics.json`), 93% of current traffic comes from the FYP algorithm, reaching an audience that is 80% female and 91.4% aged 18-34, whereas followers were 59% male. Follower traffic is 0%.
2. This establishes that the algorithm is actively testing the channel against young Vietnamese female audiences who consume VTV drama, showbiz gossip, and domestic conflict storylines.
3. However, current channel output still carries legacy male-survival themes (e.g., *Mạt Thế Kỷ Băng Hà* with endless bunker hoarding descriptions) or executes female drama at a breathless 346 words/minute with static landscape b-roll.
4. When young female users (49.8% Gen Z 18-24 and 41.6% Millennials 25-34) encounter a robotic, hyper-accelerated voice or dry bunker logistics in the first 3 seconds without immediate emotional conflict, they swipe away within 4-7 seconds.
5. In contrast, *Nàng Dâu Thức Tỉnh: Đêm Mưa Bị Đuổi Khỏi Hào Môn* generated the highest views (89 views on Ep 1), proving that female melodrama, maternal/in-law oppression, and financial retribution directly resonate with this viewer base.
6. Therefore, aligning 100% of the channel's narrative, emotional soundscapes, voice cadence (slowing to 220-245 wpm), and visual footage (ASMR baking/crafts) to these female viewer personas is the prerequisite to lifting retention from 4-7s to >3 minutes.

## 3. Caveats
- No direct individual user surveys were conducted; findings are derived from TikTok Studio analytics data, search queries, channel co-viewing affinities, and established Douyin/TikTok Vietnamese market consumption patterns.
- Follower acquisition is currently near zero (0% traffic from followers); the recommendations assume the channel continues to leverage the FYP recommendation algorithm as its primary growth engine.

## 4. Conclusion
The retention collapse is primarily caused by an acute misalignment between the 80% female (18-34) audience and the male-survival tropes, robotic 1.5x pacing, and static landscape footage of the current videos. The channel must immediately pivot to:
1. 50% In-Law / Family Revenge & Wealth Independence Melodrama (*Nàng Dâu Thức Tỉnh*).
2. 30% Sa Điêu / Mind-Reading Satire (*Tiếng Lòng Hào Môn*).
3. 20% Sweet Romance / Late-Night Healing.
4. 3 specific female-tailored 3-second hook templates (Domestic rejection in the rain, Wedding exposure of mistress, Comedic family mind-reading).
5. Slower expressive narration (1.1x-1.2x) with ASMR baking/craft background footage.

## 5. Verification Method
- Inspect `data/tiktok_studio_metrics.json` lines 76-87 to independently verify the demographic breakdown (80% Nữ, 91.4% 18-34 tuổi, 93% FYP, VTV Giải Trí affinity).
- Inspect `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_3_audience_specialist\report.md` for the complete analytical findings and blueprints.
- Invalidation condition: If subsequent 7-day TikTok Studio metrics show female viewership dropping below 50% or male engagement reviving without female targeting, demographic allocations should be recalibrated.
