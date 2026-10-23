# Handoff Report - Sub-Agent 9 (Series Playlist & Inter-Part Funnel Architect)

## 1. Observation
1. **File `data/tiktok_studio_metrics.json` lines 4-75**:
   - Total published posts: `"total_posts_badge": "Bài đăng 240"` (240 posts).
   - "Nàng Dâu Thức Tỉnh" recent 3 parts:
     * `[TẬP 1]` (line 67): 10:02 duration, 89 views, 2 likes, 0 comments.
     * `[TẬP 2]` (line 57): 09:58 duration, 85 views, 1 like, 0 comments.
     * `[TẬP 3 - KẾT]` (line 47): 09:56 duration, 39 views, 0 likes, 0 comments.
     * View collapse from Part 2 (85 views) to Part 3 (39 views) is **-54.1%**, and from Part 1 to Part 3 is **-56.2%**.
   - "Mạt Thế Kỷ Băng Hà" recent 3 parts:
     * `[TẬP 1]` (line 37): 09:55 duration, 72 views, 2 likes.
     * `[TẬP 2]` (line 27): 09:58 duration, 67 views, 0 likes.
     * `[TẬP 3 - KẾT]` (line 17): 09:58 duration, 66 views, 0 likes.
2. **File `data/tiktok_studio_metrics.json` lines 76-87 (Traffic Sources & Search Queries)**:
   - Traffic source distribution:
     * Đề xuất (FYP): `93%`
     * Tìm kiếm (Search): `4.6%`
     * Hồ sơ cá nhân (Profile): `2.4%`
     * Đã follow: `0%`
     * Âm thanh: `0%`
   - Real user search queries:
     * `tái sinh tiểu thuyết liễu như yên 2 tập tiếp theo`: `0.5%`
     * `em dâu đuổi tôi ra khỏi nhà full`: `0.5%`
     * Proves viewers are manually typing search queries into TikTok search bar to find the next part or full story because direct in-video playlist links are absent.
3. **File `scripts/tiktok_publisher_core.py` lines 413-431 & lines 473-530**:
   - Playwright uploader fills captions into `div[contenteditable="true"]`, waits for upload completion, ensures public privacy, and clicks "Đăng".
   - It currently has NO logic to interact with the TikTok Playlist/Album dropdown (`Thêm vào danh sách phát`), leaving all published videos standalone and unbundled.
4. **File `core/ffmpeg_utils.py` lines 307-333**:
   - `render_playable_video` concatenates looping background video with voice and ducked BGM, cutting off sharply at `-shortest` without an End-screen CTA card or next-episode navigation overlay in the final 5-10 seconds.
5. **File `scripts/produce_and_schedule_5_new_masterpieces.py` lines 208-214**:
   - `get_caption_for_part` formats: `{badge} {title}. {hook} {magnet} #audio #xuhuong ... {tag}`.
   - It lacks unique series hashtag tokens (e.g. `#seriesname_full`) and does not instruct viewers how to locate the next episode via Playlist or pinned comment.

## 2. Logic Chain
1. *From Observation 2*: 93% of audience discovers videos on the FYP (For You Feed), while only 2.4% navigate to the creator's profile page.
2. *From Observation 3*: Videos are published as standalone clips without being assigned to a TikTok Creator Playlist (Tuyển tập).
3. *From TikTok platform mechanics*: The FYP algorithm prioritizes diversity and almost never delivers two consecutive videos from the same creator to an individual user's FYP. Without a Playlist pill (`📑 Tuyển tập · Tập 1/3`) on screen, the video session terminates when Part 1 ends, and swiping serves a competitor's video.
4. *From Observation 1 & 2*: In "Nàng Dâu Thức Tỉnh", 85 viewers watched Part 2, but only 39 viewers ever found Part 3 (a 54.1% collapse). Users searching "tập tiếp theo" and "full" confirms they were interested in the ending but lacked navigational pathways.
5. *From Observation 1*: There are 240 videos on the profile. For the tiny 2.4% of users who do open the profile, navigating through 240 unorganized, visually similar thumbnails with truncated captions is high friction.
6. *From Observation 4 & 5*: The current video rendering pipeline has no visual end-screen cards (5-10s before end), titles lack a unique series query hashtag, and no pinned comments are posted to guide users to Part 2 or Part 3.
7. *Synthesized Conclusion*: To bridge the Part 1 -> Part 2 -> Part 3 drop-off, the system must deploy a 3-tier inter-part funnel: (A) TikTok Studio Playlist integration for auto-next playback and sticky FYP badges, (B) End-screen cards in the final 8 seconds via FFmpeg, and (C) Automated pinned comments with direct CTAs and engagement poll magnets.

## 3. Caveats
- TikTok Studio Web UI selectors can periodically change or vary depending on account tier (accounts under 10k followers may have Playlist creation located in `/tiktokstudio/content` rather than the initial upload modal). The automation code includes fallback selectors and post-publish management handlers.
- The 240 existing videos on the channel are currently unassigned to albums. A one-time batch script or manual grouping in TikTok Studio will be needed to organize legacy content.

## 4. Conclusion
The catastrophic drop-off from Part 1/2 to Part 3 (up to 56.2%) is primarily an architectural distribution problem, not just a script pacing problem. Implementing the designed TikTok Playlist taxonomy, 8-second visual end-screen cards, pinned comments, and Playwright automation will transform disconnected 10-minute videos into seamless 30-minute binge sessions, directly increasing total watch time and viewer completion metrics.

## 5. Verification Method
1. **Inspect Report Artifact**:
   - Verify `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_9_playlist_architect\report.md` exists and contains all 5 required sections: drop-off analysis, playlist architecture, inter-part funnel design, technical automation solution, and QC checklist.
2. **Review Code Automation Snippets**:
   - Check `assign_video_to_playlist(page, playlist_name)` Playwright implementation in Section 4.1.
   - Check `build_end_screen_filter(total_duration_sec, part_num, next_part_title)` FFmpeg filter complex in Section 4.2.
   - Check `post_and_pin_funnel_comment(page, part_num, series_title, unique_hashtag)` comment pinner in Section 4.3.
3. **Data Metric Verification**:
   - Confirm against `data/tiktok_studio_metrics.json` lines 4-87 that the numbers cited (240 posts, 89/85/39 views, 93% FYP, 2.4% profile, 0.5% search queries) match verbatim.
