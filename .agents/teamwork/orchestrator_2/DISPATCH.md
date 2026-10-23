# Dispatch Log

## 2026-10-23T00:36:00Z
From: Sentinel (eed75459-c1cd-49d0-a615-bfce69309004)
Message:
You are the Project Orchestrator for the TikTok Studio Deep Analytics & Weekly Content Audit project.

Working directory: c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\orchestrator_2\
Project root: c:\Users\duydo\OneDrive\Tài liệu\idk
User request file: c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\ORIGINAL_REQUEST.md

Your mission:
Orchestrate a large team of ~10 subagents ("chia tầm 10 sub agent ra để phân tích kĩ cho tôi") to conduct an exhaustive, forensic analytics and content audit of the TikTok channel via TikTok Studio and local project records.

Key Requirements:
1. R1. Live TikTok Studio Deep Extraction (Overview, Audience & Per-Video Sub-Pages):
   - Connect to TikTok Studio via authenticated Cốc Cốc browser profile (single-instance file locking).
   - Collect live data for the current week (past 7 days): Overall Channel Analytics, Viewer & Follower Analytics, and Individual Video Deep Analytics (clicking into each video's dedicated analytics sub-page for Duration, Publish time, Views, Likes, Comments, Shares, Saves, Total Play Time, Average Watch Time, Full Video Watched %, Key retention drop-off timestamps, Traffic sources).
   - Save live raw extracted data to `data/tiktok_studio_weekly_deep_audit.json` and verification screenshots to `data/`.

2. R2. Parallel 10-Subagent Granular Audit:
   - Partition analytical workload across ~10 specialized subagents.
   - Individual Video Diagnosis: Exact math (Views × Avg Watch Time = Total Play Time), why ~10-minute video gets < 10 mins total play time, early swipe-away (1-5s), near-zero completion rate.
   - Audio Series & Part-by-Part Funnel (Part 1 -> Part 2 -> Part 3): Group all videos posted this week into Audio Series, analyze every part individually and comparatively against actual script text, 3s hook, pacing, word count, voice/BGM mix, title/caption in workspace.
   - Audience & Algorithm Fit Analysis.

3. R3. Read-Only Production Constraint & Comprehensive Master Report:
   - Do NOT modify any existing production scripts, autopilot schedulers, or core codebase modules in `core/` or publisher scripts.
   - Deliver comprehensive Vietnamese master report to `docs/BAO_CAO_PHAN_TICH_TIKTOK_STUDIO_CHI_TIET_TUAN_NAY.md` meeting all acceptance criteria.

Maintain your `plan.md`, `progress.md`, and `BRIEFING.md` in your working directory `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\orchestrator_2\`.
Report back via send_message when the project is completed so victory verification can proceed.
