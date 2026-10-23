# HANDOFF REPORT — Sub-Agent 4 (Voice Acting & TTS Audio Engineer)

**Status**: Hard Handoff (Task Complete)  
**Target Path**: `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_4_tts_engineer\report.md`  
**Date**: 2026-10-17T00:39:00Z  

---

## 1. Observation

1. **Hardcoded Monotone Speed and Stacking**:
   - In `core/audio_engine.py`:
     - Lines 8-10: `"Tầng 1: Edge-TTS Native Neural Rate (+18% đến +20%)... Tầng 2: FFmpeg Gentle Time-Stretch (atempo=1.25x) đạt đúng định mức 1.50x (346 từ/phút theo chuẩn GEMINI.md)."`
     - Lines 124-129:
       ```python
       is_male = "NamMinh" in voice
       native_rate = "+18%" if is_male else "+20%"
       native_pitch = "-2Hz" if is_male else "+1Hz"
       native_factor = 1.18 if is_male else 1.20
       atempo_factor = round(target_speed / native_factor, 2)
       ```
     - Line 169: `"-filter:a", f"atempo={atempo_factor}"`
   - In `scripts/produce_series.py` (lines 82-83, 117-124):
     - `rate_val = "+18%" if "NamMinh" in voice else "+20%"`
     - `pitch_val = "-2Hz" if "NamMinh" in voice else "+1Hz"`
     - `"-filter:a", "atempo=1.25"`
   - In `docs/SO_TAY_BIEN_KICH_TRIEU_VIEW_DOUYIN_ZHIHU.md` (lines 88-92):
     - `"Tốc độ đọc 1.5x (atempo=1.5): 346 từ / phút."`
     - `"Đồng nhất giọng đọc Neural Speech (Zero Voice Mixing): Giọng Nam (vi-VN-NamMinhNeural)... Giọng Nữ (vi-VN-HoaiMyNeural)..."`

2. **Destructive Sanitization of Expressive Syntax**:
   - In `core/audio_engine.py` (lines 58-69):
     ```python
     clean_text = (
         text.replace("'", " ")
         .replace('"', ' ')
         .replace("‘", " ")
         .replace("’", " ")
         .replace("“", " ")
         .replace("”", " ")
         .replace("–", "-")
         .replace("—", "-")
         .replace("...", ", ")
         .strip()
     )
     ```
   - All quotation marks (signaling spoken dialogue) are stripped. All ellipses `...` (signaling suspenseful silence or sorrowful hesitations) are replaced with commas `, `.

3. **Performance Metrics Correlation**:
   - In `data/tiktok_studio_metrics.json`:
     - Lines 77-85: 7,700 views, 93% from FYP recommendation (`Đề xuất 93%`), 80% Female viewers, 91.4% aged 18-34.
     - Lines 4-74: Video lengths are ~9m55s to 10m02s, yet average watch time across views is only 4 - 7 seconds, with 0 comments and near-zero engagement.

4. **Edge-TTS Capability Verification**:
   - Python command execution outputting Edge-TTS Vietnamese voices confirmed:
     `vi-VN-HoaiMyNeural` (Female) and `vi-VN-NamMinhNeural` (Male).
   - Python test script successfully generated distinct character dialogue segments using pitch modulation (`-2Hz`, `+8Hz`, `+2Hz`) and rate modulation (`+5%`, `+15%`, `+10%`).

---

## 2. Logic Chain

1. **Observation 1 & 3**: On TikTok FYP (93% cold traffic), users evaluate a video within the first 1.5 - 3.0 seconds. At 346 words per minute, speech is fired at ~5.76 words/second (6.5 - 7 syllables/second).
2. **Observation 1 & 2**: Vietnamese relies on 6 lexical tones and vowel duration for word identification. Compressing speech by 1.50x without breathing cues or pitch variance strips tone contours and coarticulation clarity, triggering instant Sensory Processing Overload in the listener.
3. **Observation 2 & 1**: Enforcing "Zero Voice Mixing" forces the narrator, crying child, screaming mother-in-law, and arrogant husband to be rendered by a single neural voice at a static pitch (`-2Hz` or `+1Hz`). Dialogue quotes and dramatic trailing pauses (`...`) are erased.
4. **Observation 3**: The 80% female audience (ages 18-34) expects the dramatic emotional resonance found in top Vietnamese TV dramas and audiobooks (e.g. VTV Giải Trí, Kênh Showbiz), but receives a monotone machine-gun monologue. They experience severe cognitive dissonance and auditory burnout, swiping away within 4 - 7 seconds.
5. **Conclusion**: Therefore, replacing the static 346 wpm single-voice model with a Multi-Voice Drama Ensemble and a Non-linear Pacing Curve (210 - 250 wpm with dramatic pauses) is the prerequisite to lifting average watch time from 4-7s to multi-minute retention.

---

## 3. Caveats

- **Network Constraints**: Microsoft Edge-TTS relies on cloud websocket endpoints. While currently free and uncapped, heavy batch production (e.g., hundreds of segments simultaneously) requires local semaphore gating (concurrency 4-6) to prevent socket timeouts.
- **SSML Tag Support**: Direct XML SSML wrapping in `edge_tts.Communicate` is escaped by default; multi-voice synthesis must be achieved either by segment-level Communicate configuration (pitch/rate per segment) or using Azure Speech SDK / native SSML wrappers.
- **Third-party APIs**: Commercial APIs like FPT.AI or ElevenLabs introduce per-character API costs; thus, they are recommended selectively for the 5-second Hook rather than the full 10-minute bulk text.

---

## 4. Conclusion

1. The current AI voice setup is flawed in three specific areas: extreme speed (346 wpm), single-voice monotony ("Zero Voice Mixing"), and text flattening (stripping quotes and ellipses).
2. The recommended upgraded architecture implements:
   - Dynamic non-linear pacing: 220 wpm for Hook (0-5s), 240 wpm for general storytelling, 180-200 wpm for suspense/silence, 280 wpm for climaxes.
   - 5-profile character acting matrix utilizing pitch, rate, and FFmpeg filter adjustments (`VILLAIN_MOTHER_IN_LAW`, `FEMALE_LEAD_SOB`, `MALE_CEO_ARROGANT`, `PATRIARCH_FATHER`, `NARRATOR`).
   - Detailed blueprint provided in `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_4_tts_engineer\report.md`.

---

## 5. Verification Method

1. **Verify Source Code Flaws**:
   - Run: `python -c "from core.audio_engine import split_into_tts_chunks; print(split_into_tts_chunks('\"Trời ơi...\" - cô khóc nấc.'))"`
   - Confirm that quotes and ellipses are replaced by spaces and commas.
2. **Verify Multi-Voice Pitch/Rate Feasibility**:
   - Run:
     ```bash
     python -c "import edge_tts, asyncio; asyncio.run(edge_tts.Communicate('Chào bạn', voice='vi-VN-HoaiMyNeural', pitch='+8Hz', rate='+10%').save('test.mp3'))"
     ```
   - Inspect output audio `test.mp3` to confirm altered pitch and tone.
3. **Verify Report Existence & Completeness**:
   - Inspect `c:\Users\duydo\OneDrive\Tài liệu\idk\.agents\teamwork\subagent_4_tts_engineer\report.md`.
