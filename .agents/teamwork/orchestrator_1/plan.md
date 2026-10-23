# Plan: TikTok Audio Drama Retention Analysis & 10-Agent Optimization Blueprint

## Objective
Execute the multi-agent analysis and optimization blueprint across 10 specialized sub-agent tracks per `ORIGINAL_REQUEST.md` to produce `docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md` meeting all Requirements (R1-R5) and Acceptance Criteria.

## Tracks and Sub-Agent Responsibilities

### Track 1: Sub-Agent 1 (Data & Video Performance Auditor)
- Investigate `data/tiktok_studio_metrics.json` and `data/published_audio_registry.json`.
- Extract metrics for the 7 recent videos in the past week: views, likes, comments, shares, estimated watch time.
- Calculate drop-off rates across Part 1 -> Part 2 -> Part 3 for each series (Mạt Thế Kỷ Băng Hà, Nàng Dâu Thức Tỉnh, Khi Cả Nhà Hào Môn...).
- Output: `.agents/teamwork/subagent_1/report.md`

### Track 2: Sub-Agent 2 (Retention Curve & Drop-Off Diagnostician)
- Analyze root causes of abysmal retention: 10-min clips with total watch time < 10 min (avg 4-7s/view, near-zero completion rate).
- Analyze the "fatal 3-second hook failure" on FYP (93% traffic).
- Output: `.agents/teamwork/subagent_2/report.md`

### Track 3: Sub-Agent 3 (Audience Alignment & Demographics Specialist)
- Analyze the demographic shift in the past 7 days: 80% Female, 91.4% 18-34 years old (contrasting previous 59% male followers).
- Cross-reference drama/showbiz consumption habits (VTV Giải Trí, TV drama, showbiz gossip) with current audio drama scripts.
- Output: `.agents/teamwork/subagent_3/report.md`

### Track 4: Sub-Agent 4 (Voice Acting & TTS Audio Engineer)
- Audit current AI voice setup: `NamMinh` / `HoaiMy` at 346 wpm (`atempo=1.5`).
- Evaluate emotion, naturalness, auditory fatigue over 10 minutes.
- Research expressive voice expansion, multi-voice dialog, emotional tone switching.
- Output: `.agents/teamwork/subagent_4/report.md`

### Track 5: Sub-Agent 5 (BGM & Emotional Soundscape Specialist)
- Audit current BGM library and sidechain ducking mechanics.
- Curate emotional BGM catalog (style like *Nỗi nhớ tựa ngân hà*, melancholic piano, suspenseful tension).
- Map BGM transitions accurately to narrative beats.
- Output: `.agents/teamwork/subagent_5/report.md`

### Track 6: Sub-Agent 6 (Visual Dynamics & Footage Curator)
- Solve visual boredom of static landscape loops over 10 minutes.
- Curate footage strategy: traditional artisanal craft, ASMR slices, dynamic 4K scenery with depth.
- Visual pacing: scene cut every 5-8 seconds to maintain visual focus.
- Output: `.agents/teamwork/subagent_6/report.md`

### Track 7: Sub-Agent 7 (Subtitle & Screen Layout Designer)
- Optimize subtitle layout: move subtitles to bottom safe zone or utilize TikTok Studio auto-captions.
- Clear center screen area for background appreciation.
- Output: `.agents/teamwork/subagent_7/report.md`

### Track 8: Sub-Agent 8 (Narrative Pacing & Scriptwriting Master)
- Restructure 10-minute scripts: 3-second shocking hook, dramatic beats every 45 seconds, remove verbose exposition.
- Provide 3 shocking hook templates tailored to 80% female (18-34) audience.
- Output: `.agents/teamwork/subagent_8/report.md`

### Track 9: Sub-Agent 9 (Series Playlist & Inter-Part Funnel Architect)
- Design TikTok Series/Playlist organization in TikTok Studio for 3-part series.
- Design navigation: end-screen cards, pinned comments, playlist auto-chaining.
- Technical solution for automated publishing scripts to assign videos to albums/playlists.
- Output: `.agents/teamwork/subagent_9/report.md`

### Track 10: Sub-Agent 10 (Master Growth & Execution Strategist - Worker)
- Synthesize all findings from Sub-Agents 1-9 into `docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md`.
- Ensure all R1-R5 and Acceptance Criteria are comprehensively satisfied.
- Provide concrete roadmap for code upgrades and production pipelines.

### Verification Gate: Reviewers & Auditor
- 2 Reviewers independently review the master deliverable against R1-R5 and acceptance criteria.
- 1 Forensic Auditor verifies integrity and authenticity.
- 1 Challenger tests feasibility and consistency.
