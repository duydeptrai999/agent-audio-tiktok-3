# Original User Request

## 2026-10-17T00:31:01Z

chia tầm 10 sub agent ra để phân tích kĩ cho tôi

Use a specialized multi-agent team divided into 10 sub-agents to conduct an exhaustive, multi-dimensional analysis and optimization blueprint for the TikTok Audio Drama system (10-minute videos). The goal is to resolve the core dilemma: videos are ~10 minutes long, but total watch time is under 10 minutes (average watch time is only 4-7s/view, completion rate is near zero), despite garnering 7.7K views across 240 posts with an 80% female audience (ages 18-34). 

Working directory: c:\Users\duydo\OneDrive\Tài liệu\idk
Integrity mode: development

## Team Architecture (10 Sub-Agents Phân Nhiệm Chuyên Sâu)

1. **Sub-Agent 1 (Data & Video Performance Auditor)**:
   - Thu thập và phân tích chi tiết dữ liệu 7 video đăng gần nhất trong tuần từ `data/tiktok_studio_metrics.json` (views, likes, comments, shares, estimated watch time).
   - Đo lường mức độ suy hao (Drop-off Rate) giữa các tập Part 1 → Part 2 → Part 3 của từng bộ (Mạt Thế Kỷ Băng Hà, Nàng Dâu Thức Tỉnh, Khi Cả Nhà Hào Môn...).

2. **Sub-Agent 2 (Retention Curve & Drop-Off Diagnostician)**:
   - Mổ xẻ nguyên nhân tỷ lệ giữ chân chạm đáy: Tại sao clip 10 phút mà tổng thời gian phát không nổi 10 phút (trung bình chỉ 4-7s mỗi lượt xem).
   - Phân tích hiện tượng "tử huyệt 3 giây đầu" (Hook failure) trên luồng Đề xuất (FYP 93%).

3. **Sub-Agent 3 (Audience Alignment & Demographics Specialist)**:
   - Phân tích sự chuyển dịch tệp người xem thực tế 7 ngày qua: **80% Nữ giới, 91.4% từ 18-34 tuổi** (trong khi follower cũ là 59% Nam).
   - Đối chiếu thói quen tiêu thụ nội dung drama/showbiz (người xem thường xem kênh VTV Giải Trí, phim truyền hình, showbiz) với gu kịch bản hiện tại.

4. **Sub-Agent 4 (Voice Acting & TTS Audio Engineer)**:
   - Kiểm toán giọng đọc AI hiện tại (`NamMinh`/`HoaiMy` tốc độ 346 từ/phút, `atempo=1.5`).
   - Đánh giá cảm xúc, độ chân thật, độ mệt tai khi nghe suốt 10 phút; nghiên cứu mở rộng thư viện giọng đọc biểu cảm cao (đa giọng đối thoại, chuyển tone theo tâm trạng nhân vật).

5. **Sub-Agent 5 (BGM & Emotional Soundscape Specialist)**:
   - Đánh giá kho nhạc nền hiện tại và cơ chế sidechain ducking.
   - Tuyển chọn và xây dựng danh mục BGM không lời xúc động, da diết chuẩn trend audio drama (ví dụ: phong cách *Nỗi nhớ tựa ngân hà*, nhạc piano/dương cầm trầm buồn, nhạc đấu trí hồi hộp), ghép chuẩn xác theo diễn biến từng phân đoạn kịch bản.

6. **Sub-Agent 6 (Visual Dynamics & Footage Curator)**:
   - Khắc phục sự nhàm chán thị giác của video phong cảnh lặp lại suốt 10 phút khiến người xem quẹt bỏ.
   - Thiết kế chiến lược footage cuốn hút: video làm đồ thủ công truyền thống tinh xảo, lát cắt ASMR, phong cảnh động 4K có chiều sâu, visual pacing đổi cảnh mỗi 5-8 giây để giữ mắt người xem.

7. **Sub-Agent 7 (Subtitle & Screen Layout Designer)**:
   - Tối ưu lại vị trí phụ đề: Đưa phụ đề xuống sát đáy video hoặc chuyển hướng sang tận dụng phụ đề tự động (Auto-caption) của TikTok Studio, giải phóng không gian trung tâm màn hình cho người xem tập trung chiêm ngưỡng video background đẹp.

8. **Sub-Agent 8 (Narrative Pacing & Scriptwriting Master)**:
   - Nâng cấp kịch bản truyện dài 10 phút: Thiết kế lại Hook 3 giây đầu gây sốc cực độ (xung đột gia đình gay gắt, tiếng bạt tai, câu nói lật mở bí mật), tạo cao trào dồn dập mỗi 45 giây, xóa bỏ các đoạn văn mô tả lê thê.

9. **Sub-Agent 9 (Series Playlist & Inter-Part Funnel Architect)**:
   - Thiết kế giải pháp gom 3 part của 1 bộ truyện vào **Tuyển tập / Danh sách phát (TikTok Series/Playlists)** ngay trong TikTok Studio để người xem từ FYP bấm là xem liền mạch Part 1, 2, 3.
   - Thêm nút điều hướng (End-screen card & Pinned comment) chuyển tập tự động.

10. **Sub-Agent 10 (Master Growth & Execution Strategist)**:
    - Tổng hợp kết quả từ 9 sub-agents, biên soạn bản kế hoạch hành động chi tiết (`docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md`) với roadmap nâng cấp hệ thống code và quy trình sản xuất video 10 phút triệu view.

## Requirements

### R1. Kiểm toán Số liệu Video & Đối soát Tuyển tập
Bóc tách toàn bộ chỉ số thực tế từ `data/tiktok_studio_metrics.json` và lịch sử xuất bản `data/published_audio_registry.json`. Xác định rõ tỷ lệ rớt view giữa Part 1, Part 2, Part 3 của từng bộ truyện.

### R2. Định danh 5 Tử Huyệt Khiến Tỷ Lệ Giữ Chân Thấp Kỷ Lục
Chỉ rõ các sai lầm trong việc dựng video 10 phút phân phối trên FYP (93% traffic):
1. Tử huyệt 3 giây đầu (Hook mở màn thiếu xung đột thị giác và thính giác).
2. Giọng đọc đơn điệu, thiếu ngữ điệu biểu cảm kịch tính.
3. Nhạc nền lệch tone cảm xúc, chưa tạo được rung động như các trend nhạc không lời viral.
4. Video background trôi chậm, lặp lại gây chán ngán cho người dùng lướt nhanh.
5. Sự thiếu hụt Playlist/Tuyển tập khiến người dùng gặp Part 2/3 không tìm thấy Part 1.

### R3. Thiết kế Cấu trúc Kịch bản & Âm thanh Cho Video 10 Phút Giữ Chân Cao
- Giữ nguyên thời lượng 10 phút nhưng tái cấu trúc nhịp điệu: Hook (0-5s) → Giới thiệu biến cố chấn động (5-30s) → Đấu trí/Cao trào 1 (1-3 phút) → Xung đột bước ngoặt (4-7 phút) → Đại cao trào & Cliffhanger (8-10 phút).
- Thư viện nhạc nền BGM cảm xúc cao (phong cách *Nỗi nhớ tựa ngân hà*, piano cổ phong, v.v.).

### R4. Tối ưu Giao diện Thị giác & Phụ đề Đáy Màn hình
- Đổi layout phụ đề xuống sát đáy (vùng an toàn tương tác TikTok) hoặc cơ chế kích hoạt subtitle tự động của TikTok Studio.
- Đề xuất nguồn footage thủ công mỹ nghệ / cảnh quay sinh động giữ mắt người nhìn.

### R5. Quy trình Đóng gói Tuyển tập 3 Part (TikTok Playlist Automation)
Đưa ra giải pháp kỹ thuật tích hợp vào script tự động đăng để tự động thêm video vào Danh sách phát / Tuyển tập theo từng bộ truyện.

## Acceptance Criteria

### Báo cáo & Cẩm nang Tối ưu Triệu View
- [ ] Báo cáo phân tích có bảng kiểm toán số liệu từng video và từng part của các bộ truyện đã đăng trong tuần qua.
- [ ] Xác định nguyên nhân khách quan và định lượng của hiện tượng watch time trung bình 4-7 giây trên video 10 phút.
- [ ] Đề xuất danh sách ít nhất 5 bản nhạc nền BGM cảm xúc cao (kiểu *Nỗi nhớ tựa ngân hà*, piano trầm lắng, cổ phong xúc động) kèm thông số mix ducking phù hợp.
- [ ] Đưa ra ít nhất 3 template mở màn kịch bản Hook 3s giật gân dành riêng cho tệp 80% Nữ giới (18-34 tuổi).
- [ ] Cung cấp giải pháp kỹ thuật cấu hình phụ đề đáy màn hình và đưa 3 part vào cùng một Album/Tuyển tập trên TikTok Studio.
- [ ] Báo cáo toàn diện hoàn chỉnh được lưu tại `docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md`.


## 2026-10-23T00:33:59Z

Use a large team of ~10 subagents ("chia tầm 10 sub agent ra để phân tích kĩ cho tôi") to conduct an exhaustive, forensic analytics and content audit of the TikTok channel via TikTok Studio and local project records. Extract live metrics for all videos posted this week (including clicking into each video's detailed analytics page for Total Play Time, Average Watch Time, Full Video Completion Rate, and Retention Drop-off), analyze overall channel & audience demographics, and perform a deep series-by-series and part-by-part diagnosis of why ~10-minute video parts achieve less than 10 minutes of total play time and near-zero completion rates — without modifying existing production code.

Working directory: c:\Users\duydo\OneDrive\Tài liệu\idk
Integrity mode: development

## Requirements

### R1. Live TikTok Studio Deep Extraction (Overview, Audience & Per-Video Sub-Pages)
Connect to TikTok Studio via the authenticated Cốc Cốc browser profile (using single-instance file locking so browser sessions do not collide) and collect live data for the current week (past 7 days):
- **Overall Channel Analytics (Tổng quan & Nội dung)**: Video views, profile views, likes, comments, shares, traffic source percentages, and top search queries.
- **Viewer & Follower Analytics (Người xem & Follower)**: Total viewers, new viewers, gender/age/geographic breakdown, active hours, and overlapping creators/videos watched by the audience.
- **Individual Video Deep Analytics (Phân tích từng video)**: For every video published this week, navigate into its dedicated analytics view to extract video duration, publish time, views, likes, comments, shares, saves, Total Play Time (Tổng thời gian phát), Average Watch Time (Thời gian xem trung bình), Full Video Watched % (Tỉ lệ xem hết video), key retention drop-off timestamps, and per-video traffic sources.

### R2. Parallel 10-Subagent Granular Audit (Every Video, Every Audio Series & Every Part)
Partition the analytical workload across ~10 specialized subagents to audit:
- **Individual Video Diagnosis**: Explain mathematically and behaviorally for each video why a ~10-minute video accumulates `< 10 minutes` of Total Play Time (e.g., `Views × Average Watch Time`, early swipe-away within the first 1–5 seconds) and why the completion rate is critically low.
- **Audio Series & Part-by-Part Funnel (Part 1 → Part 2 → Part 3)**: Group all videos posted this week into their respective Audio Series (Bộ Audio) and analyze each part (Part 1, Part 2, Part 3) individually and comparatively, cross-referencing TikTok Studio retention data against the actual script text, 3-second hook, pacing, word count, voice/BGM mix, and title/caption stored in the workspace.
- **Audience & Algorithm Fit Analysis**: Evaluate how the channel's current viewer demographics (age, gender, watch behavior, competing entertainment channels) and TikTok recommendation dynamics interact with 10-minute multi-part audio videos.

### R3. Read-Only Production Constraint & Comprehensive Master Report
Do not modify any existing production scripts, autopilot schedulers, or core codebase modules. Produce a complete, structured Vietnamese analytical report saved to `docs/BAO_CAO_PHAN_TICH_TIKTOK_STUDIO_CHI_TIET_TUAN_NAY.md` (backed by raw extracted JSON data in `data/tiktok_studio_weekly_deep_audit.json`), covering:
1. Executive Overview & Channel Health (Tổng quan kênh & Luồng đề xuất).
2. Deep Viewer & Follower Persona Analysis (Phân tích chuyên sâu Người xem & Follower).
3. Root-Cause Diagnosis of the "< 10 Minutes Total Play Time on a 10-Minute Video" & Low Completion Rate Phenomenon.
4. Series-by-Series & Part-by-Part Forensic Breakdown (Phân tích chi tiết từng bộ Audio và từng Part 1, 2, 3 đã đăng trong tuần).
5. Video-by-Video Full Metrics Table & Retention Diagnosis for every video posted this week.
6. Concrete, Actionable Optimization Blueprint (cấu trúc độ dài mỗi part, hook 3 giây đầu, nhịp cắt tập, khung giờ đăng, và tệp khán giả mục tiêu).

## Acceptance Criteria

### Live Data Extraction & Verification
- [ ] `data/tiktok_studio_weekly_deep_audit.json` exists, is valid JSON, and contains live-extracted data from TikTok Studio for the current week, including Overview metrics, Viewer/Follower demographics, and per-video detailed metrics (Views, Total Play Time, Average Watch Time, Full Video Completion Rate, Likes, Comments, Shares, Duration, Publish Date).
- [ ] Screenshots proving live extraction from TikTok Studio Content, Overview, Viewers, Followers, and sample per-video Analytics pages are saved in `data/`.

### Completeness of Granular Analysis
- [ ] `docs/BAO_CAO_PHAN_TICH_TIKTOK_STUDIO_CHI_TIET_TUAN_NAY.md` is written in detailed Vietnamese and explicitly analyzes **every single video** published this week, **every Audio Series (Bộ Audio)**, and **every Part (Part 1, Part 2, Part 3)** within each series without omitting or lumping videos together.
- [ ] For every 10-minute video part with `< 10 minutes` total play time, the report provides the exact calculation (`Views × Avg Watch Time = Total Play Time`), the exact drop-off timestamp/window, and a direct critique of the corresponding script opening/pacing in the workspace.
- [ ] `git status` / workspace check confirms no existing production modules in `core/` or existing publisher scripts were modified or broken.
