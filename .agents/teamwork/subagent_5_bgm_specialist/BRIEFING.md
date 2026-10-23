# BRIEFING — 2026-10-17T00:38:00Z

## Mission
Audit BGM files, music selection logic, sidechain ducking implementation, curate high-emotion BGM catalog, specify mixing parameters, and design 10-minute soundscape blueprint for TikTok audio drama.

## 🔒 My Identity
- Archetype: explorer
- Roles: BGM & Emotional Soundscape Specialist, Investigator, Synthesizer
- Working directory: c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_5_bgm_specialist
- Original parent: 8d020f67-ebca-4169-bf79-d09f28b5c1dd
- Milestone: BGM & Emotional Soundscape Audit and Blueprint

## 🔒 Key Constraints
- Read-only investigation — do NOT implement
- Audit existing BGM files, music selection logic, and sidechain ducking in codebase
- Curate at least 5 high-emotion viral instrumental BGM tracks
- Specify exact sidechain ducking & mixing parameters
- Provide 10-minute soundscape blueprint mapping musical intensity
- Write report.md and handoff.md in working directory
- Notify parent via send_message

## Current Parent
- Conversation ID: 8d020f67-ebca-4169-bf79-d09f28b5c1dd
- Updated: not yet

## Investigation State
- **Explored paths**:
  - `assets/bgm/`, `assets/bgm_quarantine/` (80 mp3s audited, sizes & durations probed)
  - `core/bgm_manager.py` (blacklist, safe presets, fallback logic)
  - `core/audio_engine.py` (sidechaincompress, vocal chain filter, TTS chunking)
  - `core/ffmpeg_utils.py` (render_playable_video, stream_loop, audio filter chains)
  - `config/settings.py` (BGM_VOLUME, VOICE_VOLUME, TARGET_LUFS)
  - `data/tiktok_studio_metrics.json`, `data/published_audio_registry.json`
  - Subagent 3 report & Subagent 4 progress
- **Key findings**:
  1. Deterministic preset lookup bug in `core/bgm_manager.py` causes all drama/romance scripts to default to `chill/chill_instrumental.mp3`.
  2. Single 3-minute BGM tracks are looped 3.3 times over 10 minutes with abrupt hard seams and zero emotional modulation.
  3. Sidechain ducking filter (`threshold=0.045:ratio=7:attack=15:release=280`) causes severe acoustic pumping against 346 wpm TTS, generating fatigue for listeners.
  4. Music is completely disconnected from the 80% female 18-34 demographic expectations (lack of *Nỗi nhớ tựa ngân hà*, melancholic piano, epic cathartic strings).
- **Unexplored areas**: None, all mission requirements covered.

## Key Decisions Made
- Designed a 3-track evolving narrative arc to replace monolithic single-track looping.
- Calibrated optimal sidechain ducking parameters: threshold=-22dBFS, ratio=4:1, attack=25ms, release=750ms, vocal pocket scoop 1-3.5kHz.
- Curated 6 viral instrumental track archetypes with complete acoustic specifications.
- Drafted 10-minute soundscape blueprint synchronized with 7 dramatic storytelling beats.

## Artifact Index
- DISPATCH.md — Initial task dispatch
- BRIEFING.md — Persistent working memory
- progress.md — Liveness heartbeat and step tracking
- report.md — Comprehensive technical report (to be written)
- handoff.md — 5-component handoff report (to be written)
