# BRIEFING — 2026-10-17T00:38:40Z

## Mission
Audit current subtitle rendering and screen layout in the TikTok Audio Drama system, and design an optimized subtitle layout (bottom safe zone avoiding UI, or TikTok Studio auto-captions) to maximize visual aesthetic and retention.

## 🔒 My Identity
- Archetype: explorer
- Roles: Subtitle & Screen Layout Designer
- Working directory: c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_7_subtitle_designer\
- Original parent: 8d020f67-ebca-4169-bf79-d09f28b5c1dd
- Milestone: Subtitle & Screen Layout Optimization Analysis

## 🔒 Key Constraints
- Read-only investigation — do NOT implement
- Audit current subtitle rendering and screen layout in the codebase (ffmpeg/ass/srt configs)
- Design optimized subtitle layout: moving subtitles to bottom safe zone or leveraging TikTok Studio auto-captions
- Provide exact typography, font family, font size, stroke outline, contrast shadows, karaoke word-highlighting specifications, and safe zone coordinate calculations for 9:16 vertical video
- Detail code changes/configs needed in video generation scripts
- Write complete report to c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_7_subtitle_designer\report.md and notify the parent orchestrator via send_message

## Current Parent
- Conversation ID: 8d020f67-ebca-4169-bf79-d09f28b5c1dd
- Updated: not yet

## Investigation State
- **Explored paths**: `config/settings.py`, `core/subtitle_engine.py`, `core/ffmpeg_utils.py`, `core/audio_engine.py`, `core/thumbnail_generator.py`, `scripts/produce_*.py`, `scripts/auto_upload_*.py`, system fonts on Windows (`C:\Windows\Fonts`)
- **Key findings**:
  1. Current pipeline renders 16:9 Landscape (1920x1080) with MarginV=220px (Y=860px). When displayed on 9:16 TikTok, it either letterboxes or, if converted to 9:16 (1080x1920), MarginV=220px places subtitles at Y=1700px, completely occluded by TikTok's username, caption, sound disc, and navigation bar!
  2. Top visual badge at Y=45px (height 90px) collides directly with TikTok's mobile status bar and "Following / For You" tabs.
  3. Current subtitle timestamps in `core/subtitle_engine.py` are generated using character-length heuristics, causing accumulated desync over 10-minute videos.
  4. `edge_tts.SubMaker` and `edge_tts.Communicate.stream()` natively provide millisecond-accurate `WordBoundary` events, enabling true zero-drift word alignment and ASS `\k` karaoke animation without extra API cost.
  5. TikTok 9:16 UI obstruction zones mapped: Right rail (X=860-1080px), Bottom rail (Y=1450-1920px), Top rail (Y=0-220px). Subtitle "Sweet Spot" is Y=1260-1420px (MarginV=500-540px, MarginL=80px, MarginR=240px).
- **Unexplored areas**: None. All core scripts and UI specs fully mapped.

## Key Decisions Made
- Architected two complete production-ready solutions:
  - Strategy A: Bottom Safe-Zone Burnt-in Kinetic Subtitles (ASS format with `\k` word-sync, Be Vietnam Pro/Montserrat/Segoe UI Bold, MarginV=520px, MarginR=240px).
  - Strategy B: Zero-Burnt-In Screen + TikTok Studio Auto-Captions/SRT Upload (100% aesthetic visual immersion, user toggleable CC, native algorithmic SEO indexing).
- Formulated complete code diffs and configuration blueprints for `config/settings.py`, `core/subtitle_engine.py`, `core/ffmpeg_utils.py`, and upload scripts.

## Artifact Index
- report.md — Comprehensive Subtitle & Screen Layout Optimization Blueprint
- handoff.md — 5-component handoff report
- progress.md — Liveness heartbeat and progress log
- DISPATCH.md — Parent dispatch record
