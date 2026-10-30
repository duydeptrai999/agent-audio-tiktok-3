# -*- coding: utf-8 -*-
with open("core/background_manager.py", "r", encoding="utf-8") as f:
    text = f.read()

t_norm = text.replace("\r\n", "\n")

old_slice_fn = '''def extract_video_slice(
    source_path: Path,
    slice_path: Path,
    start_sec: float,
    duration_seconds: float,
    force_vertical_9_16: bool = True
) -> Path:
    """
    Trích xuất phân đoạn B-roll siêu tốc với libx264 ultrafast re-encode:
    - Tự động Center-Crop & Scale về chuẩn dọc 1080x1920 (9:16) nếu force_vertical_9_16=True.
    - Cưỡng bức khung hình 0 (Frame 0) luôn là IDR Keyframe ở PTS=0 (iskey=1, type=I).
    - Triệt tiêu 100% lỗi màn hình đen hoặc viền đen 16:9 trên điện thoại TikTok.
    """
    ffmpeg = get_ffmpeg_exe()
    slice_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg, "-y",
        "-ss", str(start_sec),
        "-i", str(source_path),
        "-t", str(duration_seconds),
    ]
    if force_vertical_9_16:
        # Tự động cắt vùng 9:16 và loại bỏ 22% đáy của video ngang (nơi hay có phụ đề Hàn/Trung/Anh gốc)
        vf_crop_916 = (
            "crop='if(gt(iw,ih),ih*0.78*9/16,min(iw,ih*9/16))':"
            "'if(gt(iw,ih),ih*0.78,min(ih,iw*16/9))':"
            "'(iw-if(gt(iw,ih),ih*0.78*9/16,min(iw,ih*9/16)))/2':"
            "'if(gt(iw,ih),ih*0.04,(ih-min(ih,iw*16/9))/2)',"
            "scale=1080:1920,setsar=1"
        )
        cmd.extend(["-vf", vf_crop_916])

    cmd.extend([
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-force_key_frames", "expr:gte(t,0)",
        "-avoid_negative_ts", "make_zero",
        "-an",
        str(slice_path)
    ])
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=600)
    except subprocess.TimeoutExpired:
        print(f"[BackgroundManager Error] Timeout 600s khi cắt video slice {slice_path.name}")
        raise
    return slice_path'''

new_slice_fn = '''def extract_video_slice(
    source_path: Path,
    slice_path: Path,
    start_sec: float,
    duration_seconds: float,
    force_vertical_9_16: bool = False
) -> Path:
    """
    Trích xuất phân đoạn B-roll siêu tốc:
    - GIỮ NGUYÊN 100% KHUNG HÌNH VÀ TỶ LỆ GỐC CỦA VIDEO (Zero Crop / Zero Stretch / Zero Fit).
    - Tuyệt đối KHÔNG tự ý kéo dãn, crop xén hay ép fit khung hình làm méo video.
    - Cưỡng bức khung hình 0 (Frame 0) luôn là IDR Keyframe ở PTS=0 (iskey=1, type=I).
    """
    ffmpeg = get_ffmpeg_exe()
    slice_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg, "-y",
        "-ss", str(start_sec),
        "-i", str(source_path),
        "-t", str(duration_seconds),
    ]
    if force_vertical_9_16:
        # Chỉ khi được cấu hình bắt buộc mới can thiệp khung hình
        vf_crop_916 = (
            "crop='min(iw,ih*9/16)':'min(ih,iw*16/9)':'(iw-min(iw,ih*9/16))/2':'(ih-min(ih,iw*16/9))/2',"
            "scale=1080:1920,setsar=1"
        )
        cmd.extend(["-vf", vf_crop_916])

    cmd.extend([
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-force_key_frames", "expr:gte(t,0)",
        "-avoid_negative_ts", "make_zero",
        "-an",
        str(slice_path)
    ])
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=600)
    except subprocess.TimeoutExpired:
        print(f"[BackgroundManager Error] Timeout 600s khi cắt video slice {slice_path.name}")
        raise
    return slice_path'''

old_extract_slice = '''    def extract_video_slice(
        self,
        source_path: Path,
        slice_path: Path,
        start_sec: float,
        duration_seconds: float
    ) -> Path:
        """Cắt video slice chuẩn dọc 9:16 (1080x1920) với IDR keyframe ở PTS=0."""
        return extract_video_slice(source_path, slice_path, start_sec, duration_seconds, force_vertical_9_16=True)'''

new_extract_slice = '''    def extract_video_slice(
        self,
        source_path: Path,
        slice_path: Path,
        start_sec: float,
        duration_seconds: float
    ) -> Path:
        """Cắt video slice giữ nguyên khung hình gốc (Zero Crop / Zero Stretch / Zero Fit)."""
        return extract_video_slice(source_path, slice_path, start_sec, duration_seconds, force_vertical_9_16=False)'''

old_probe_check = '''        if slice_path.exists() and slice_path.stat().st_size > 500000:
            probe_sl = probe_media_file(slice_path)
            if probe_sl.get("height", 0) > probe_sl.get("width", 0):
                print(f"🎬 [BackgroundManager] Sử dụng phân đoạn dọc 9:16 có sẵn: {slice_name}")
                return slice_path
            else:
                print(f"🔄 [BackgroundManager] Phân đoạn cũ {slice_name} đang ở khung ngang, tự động chuyển đổi sang dọc 9:16 (1080x1920)...")'''

new_probe_check = '''        if slice_path.exists() and slice_path.stat().st_size > 500000:
            print(f"🎬 [BackgroundManager] Sử dụng phân đoạn video có sẵn: {slice_name}")
            return slice_path'''

assert old_slice_fn in t_norm, "old_slice_fn not found"
assert old_extract_slice in t_norm, "old_extract_slice not found"
assert old_probe_check in t_norm, "old_probe_check not found"

t_norm = t_norm.replace(old_slice_fn, new_slice_fn)
t_norm = t_norm.replace(old_extract_slice, new_extract_slice)
t_norm = t_norm.replace(old_probe_check, new_probe_check)

final = t_norm.replace("\n", "\r\n")

with open("core/background_manager.py", "w", encoding="utf-8") as f:
    f.write(final)

print("Updated core/background_manager.py successfully!")
