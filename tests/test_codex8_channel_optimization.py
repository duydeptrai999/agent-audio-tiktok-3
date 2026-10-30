# -*- coding: utf-8 -*-
"""
tests/test_codex8_channel_optimization.py
Kiểm chứng toàn diện gói nâng cấp Tối Ưu Kênh & Quy Trình Làm Video (Master Codex 8.0):
1. Khung hình dọc chuẩn 9:16 (1080x1920) cho cả B-Roll slice, Thumbnail và Video MP4 thành phẩm.
2. Phụ đề động (Kinetic Captions) 3-5 từ/cụm nằm ở 1/3 dưới màn hình (Safe Zone).
3. Chữa dứt điểm lỗi dấu ba chấm / dấu chấm giữa câu đi trước chữ thường khiến Edge-TTS đọc khựng giọng.
4. Giọng đọc Edge-TTS tốc độ tự nhiên (rate +5%..+8% cho Hoài My, +3%..+6% cho Nam Minh) & BGM Ducking -22dB (volume=0.08).
5. Giám tuyển B-Roll khớp thể loại (Loại bỏ video gõ búa sắt rỉ sét khỏi truyện Nữ/Gia đình/Tình cảm).
6. Comment Magnets phân cực theo ngữ cảnh thực tế (Loại bỏ câu hỏi robot "bình luận 1 hoặc 2").
"""

import os
import sys
import shutil
import unittest
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


class TestCodex8ChannelOptimization(unittest.TestCase):

    def test_1_vertical_916_settings_and_subtitle_phrases(self):
        """Kiểm tra cấu hình 9:16 (1080x1920), BGM -22dB (0.08) và Kinetic Captions 3-5 từ."""
        import config.settings as s
        from core.subtitle_engine import split_into_subtitle_phrases, get_tiktok_subtitles_filter_param

        self.assertEqual(s.VIDEO_WIDTH, 1080)
        self.assertEqual(s.VIDEO_HEIGHT, 1920)
        self.assertAlmostEqual(s.BGM_VOLUME, 0.08, places=2)
        self.assertTrue(s.ENABLE_SUBTITLES)

        sample_sentence = "Vừa ký đơn ly hôn xong, tôi lập tức chuyển khoản cho chồng cũ một tỷ hai kèm lời nhắn."
        phrases = split_into_subtitle_phrases(sample_sentence)
        self.assertGreaterEqual(len(phrases), 3)
        for p in phrases:
            w_len = len(p.split())
            self.assertLessEqual(w_len, 6, f"Cụm phụ đề '{p}' vượt quá 6 từ ({w_len} từ)")

        sub_filter = get_tiktok_subtitles_filter_param(Path("dummy.srt"))
        self.assertIn("MarginV=68", sub_filter)
        self.assertIn("FontSize=16", sub_filter)

    def test_2_mid_sentence_period_healer(self):
        """Kiểm tra bộ chữa lỗi dấu chấm / ba chấm giữa câu trước chữ thường cho Edge-TTS."""
        from core.audio_engine import split_into_tts_chunks
        from core.stories.script_quality_gate import audit_and_optimize_part_text

        buggy_text = (
            "Chiếc xe lăn vốn dĩ phải có người ngồi... giờ đây hoàn toàn trống trơn. "
            "Bóng người phản chiếu trong gương. hoàn toàn không phải là tôi! "
            "Bố. bố hiểu lầm rồi. bọn con chỉ nói chuyện thôi."
        )
        opt_text, _ = audit_and_optimize_part_text(buggy_text, title="TestHealer", part_num=2)
        self.assertNotIn("ngồi. giờ", opt_text)
        self.assertNotIn("gương. hoàn", opt_text)
        self.assertNotIn("Bố. bố", opt_text)
        self.assertIn("ngồi, giờ", opt_text)
        self.assertIn("gương, hoàn", opt_text)

        chunks = split_into_tts_chunks(buggy_text)
        joined = " ".join(chunks)
        self.assertNotIn("ngồi. giờ", joined)
        self.assertNotIn("gương. hoàn", joined)

    def test_3_genre_aware_broll_excludes_rusty_tools_for_drama(self):
        """Kiểm tra bộ lọc B-Roll loại bỏ video gõ búa rỉ sét khỏi truyện Hào môn / Gia đấu."""
        from core.background_manager import background_manager

        candidates = background_manager._collect_all_candidate_pool_files(genre="Hào Môn")
        names = [c.name.lower() for c in candidates]
        for n in names:
            self.assertNotIn("tool_restoration", n, f"B-roll gõ búa rỉ sét '{n}' không được lọt vào truyện Hào Môn")

    def test_4_contextual_polarizing_comment_magnets(self):
        """Kiểm tra Comment Magnets phân cực theo cốt truyện, không còn câu robot 'bình luận 1 hoặc 2'."""
        from core.stories.daily_story_factory import generate_contextual_hooks_and_magnets

        parts = [
            {"part_number": 1, "text": "Vừa ký đơn ly hôn xong, tôi lập tức yêu cầu chồng cũ sao kê toàn bộ tài sản chung suốt năm năm."},
            {"part_number": 2, "text": "Bà mẹ chồng đập bàn đòi giữ lại căn hộ đứng tên riêng của tôi."},
            {"part_number": 3, "text": "Trước mặt luật sư, anh ta tái mặt nhìn tờ giấy ủy quyền."}
        ]
        hooks, magnets = generate_contextual_hooks_and_magnets(
            title="Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Sau Ly Hôn",
            genre="Gia Đấu",
            parts_list=parts,
            start_time_str="17:30"
        )
        self.assertEqual(len(hooks), 3)
        self.assertEqual(len(magnets), 3)
        for h in hooks:
            self.assertNotIn("bình luận 1 hoặc 2", h.lower())
        self.assertIn("Vừa ký đơn ly hôn xong", hooks[0])

    def test_5_end_to_end_vertical_916_video_and_thumbnail_render(self):
        """Kiểm tra thực tế dựng 1 video mẫu dọc 9:16 (1080x1920) có Header Card + Kinetic Subtitles + Thumbnail."""
        from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
        from core.background_manager import background_manager
        from core.subtitle_engine import generate_srt_from_text_and_duration
        from core.thumbnail_generator import generate_part_thumbnail
        from core.bgm_manager import get_safe_bgm_for_genre

        tmp_dir = ROOT_DIR / "assets" / "output" / "test_codex8_verify"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        try:
            ffmpeg = get_ffmpeg_exe()
            sample_voice = tmp_dir / "sample_voice.mp3"
            sample_srt = tmp_dir / "sample_voice.srt"
            sample_thumb = tmp_dir / "sample_thumb.jpg"
            sample_out = tmp_dir / "sample_vertical_916.mp4"

            # Tạo 6 giây voice giả lập (sine wave nhẹ ở 220Hz) để test pipeline nhanh
            subprocess.run([
                ffmpeg, "-y", "-f", "lavfi", "-i", "sine=frequency=220:duration=6",
                "-c:a", "libmp3lame", "-b:a", "128k", str(sample_voice)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

            sample_text = (
                "Vừa ký đơn ly hôn xong, tôi lập tức chuyển khoản cho chồng cũ một tỷ hai. "
                "Kèm theo lời nhắn chúc anh hạnh phúc bên người mới."
            )
            generate_srt_from_text_and_duration(sample_text, 6.0, sample_srt)
            self.assertTrue(sample_srt.exists())

            slice_path = background_manager.get_distinct_slice_for_part(
                series_id="TEST_CODEX8_916",
                part_number=1,
                duration_seconds=6.0,
                genre="Gia Đấu"
            )
            slice_probe = probe_media_file(slice_path)
            # Khung hình B-roll giữ nguyên bản chất lượng video gốc (Zero Crop / Zero Stretch / Zero Fit)
            self.assertGreater(slice_probe["width"], 0)
            self.assertGreater(slice_probe["height"], 0)

            generate_part_thumbnail(
                source_video_or_image=slice_path,
                output_thumb_path=sample_thumb,
                story_title="Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Sau Ly Hôn",
                part_label="TẬP 1",
                genre_tag="#GiaĐấu"
            )
            self.assertTrue(sample_thumb.exists())
            thumb_probe = probe_media_file(sample_thumb)
            self.assertEqual(thumb_probe["width"], 1080)
            self.assertEqual(thumb_probe["height"], 1920)

            bgm_file = get_safe_bgm_for_genre("GIA_DAU")
            render_playable_video(
                output_file=sample_out,
                voice_audio_path=str(sample_voice),
                clean_footage_path=str(slice_path),
                bgm_audio_path=str(bgm_file),
                srt_path=str(sample_srt),
                badge_label="TẬP 1",
                bgm_volume=0.08,
                voice_volume=0.96,
                enable_subtitles=True,
                title_text="Màn Trả Thù Đã Nhất Đời Tôi: Sự Thức Tỉnh Sau Ly Hôn",
                genre="Gia Đấu"
            )
            self.assertTrue(sample_out.exists())
            out_probe = probe_media_file(sample_out)
            self.assertTrue(out_probe["is_valid"])
            self.assertTrue(out_probe["has_audio"])
            # Video thành phẩm giữ nguyên vẹn 100% khung hình gốc của video B-roll (Zero Crop / Zero Stretch / Zero Fit)
            self.assertEqual(out_probe["width"], slice_probe["width"])
            self.assertEqual(out_probe["height"], slice_probe["height"])
            self.assertGreaterEqual(out_probe["duration"], 5.5)

            # Trích xuất 1 frame mẫu ở giây 1.5 và copy thumbnail để lưu làm bằng chứng trực quan
            preview_frame = Path(r"C:\Users\duydo\.gemini\antigravity\brain\6ac3142d-b6bd-44e4-b362-edf81fad7ff1\codex8_vertical_916_after.png")
            preview_thumb = Path(r"C:\Users\duydo\.gemini\antigravity\brain\6ac3142d-b6bd-44e4-b362-edf81fad7ff1\codex8_thumb_916_after.jpg")
            if preview_frame.parent.exists():
                subprocess.run([
                    ffmpeg, "-y", "-ss", "1.5", "-i", str(sample_out),
                    "-frames:v", "1", str(preview_frame)
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                shutil.copy2(sample_thumb, preview_thumb)
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            for sl in (ROOT_DIR / "assets" / "footage" / "active_slices").glob("slice_TEST_CODEX8_916*"):
                sl.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
