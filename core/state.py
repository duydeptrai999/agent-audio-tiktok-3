from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, model_validator


class VideoCategory(str, Enum):
    HIGH_IQ = "HIGH_IQ"          # Kịch bản có não, logic, kích thích tranh luận
    SLEEP_CHILL = "SLEEP_CHILL"  # Kịch bản mất não, ru ngủ, kể chuyện êm đềm


class ReviewStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REVISE = "REVISE"


class QAStatus(str, Enum):
    PENDING = "PENDING"
    PASSED = "PASSED"
    FAILED = "FAILED"


class PublishStatus(str, Enum):
    DRAFT = "DRAFT"
    SCHEDULED = "SCHEDULED"
    PUBLISHED = "PUBLISHED"
    FAILED = "FAILED"


class ScriptPart(BaseModel):
    """Mô hình dữ liệu cho từng tập/phần trong chuỗi video nhiều phần (Multi-part series)."""
    part_number: int = Field(default=1, description="Số thứ tự phần (1, 2, ...)")
    total_parts: int = Field(default=1, description="Tổng số phần trong chuỗi")
    badge_label: str = Field(default="", description="Nhãn hiển thị trên video: [PHẦN 1], [PHẦN 2 / KẾT]")
    title: str = Field(default="", description="Tiêu đề của phần này")
    hook: str = Field(default="", description="Hook 3s mở đầu hoặc 3s Recap tóm tắt cho các phần sau")
    body: str = Field(default="", description="Nội dung chính của phần này")
    cliffhanger: str = Field(default="", description="Cú ngắt lửng kịch tính ở cuối để kéo sang phần sau")
    call_to_action: str = Field(default="", description="Lời kêu gọi theo dõi đón xem phần tiếp theo")
    full_text: str = Field(default="", description="Toàn bộ văn bản liền mạch để lồng tiếng")
    target_duration_seconds: int = Field(default=50, description="Thời lượng mục tiêu")
    audio_path: Optional[str] = None
    srt_path: Optional[str] = None
    final_video_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    footage_slice_path: Optional[str] = None
    qa_status: QAStatus = QAStatus.PENDING
    publish_status: PublishStatus = PublishStatus.DRAFT
    schedule_time: Optional[str] = None
    caption: str = Field(default="", description="Caption SEO riêng cho phần này")


class ScriptSchema(BaseModel):
    title: str = ""
    hook: str = ""
    body: str = ""
    call_to_action: str = ""
    full_text: str = ""
    target_duration_seconds: int = 50
    review_status: ReviewStatus = ReviewStatus.PENDING
    review_score: float = 0.0
    review_notes: str = ""
    review_rubric: Dict[str, float] = Field(default_factory=dict)
    review_strengths: List[str] = Field(default_factory=list)
    review_weaknesses: List[str] = Field(default_factory=list)
    review_guidance: str = ""
    retry_count: int = 0
    is_multipart: bool = False
    parts: List[ScriptPart] = Field(default_factory=list)



class AssetPaths(BaseModel):
    audio_path: Optional[str] = None
    srt_path: Optional[str] = None
    raw_footage_path: Optional[str] = None
    cleaned_footage_path: Optional[str] = None
    bgm_path: Optional[str] = None
    thumbnail_path: Optional[str] = None


class TrendTopic(BaseModel):
    """Mô hình dữ liệu lưu trữ thông tin chủ đề xu hướng được khai thác và chấm điểm."""
    topic_id: str = Field(default="", description="ID định danh chủ đề")
    title: str = Field(default="", description="Tiêu đề chủ đề hoặc câu chuyện xu hướng")
    source: str = Field(default="", description="Nguồn khai thác: tiktok, douyin, reddit, threads, quora, life_stories, cache")
    viral_score: float = Field(default=0.0, description="Điểm tiềm năng viral chuẩn hóa trong thang [0.0, 100.0]")
    metrics: Dict[str, Any] = Field(
        default_factory=dict, 
        description="Chỉ số định lượng: views, comments, shares, growth_velocity, engagement_rate, etc."
    )
    summary: str = Field(default="", description="Tóm tắt nội dung 2-3 câu cốt lõi")
    recommended_hook: str = Field(default="", description="Gợi ý câu hook 3 giây đầu để phá vỡ định kiến hoặc thu hút")
    keywords: List[str] = Field(default_factory=list, description="Từ khóa hoặc hashtag liên quan")
    category_match: Optional[str] = Field(default=None, description="Thể loại phù hợp: HIGH_IQ hoặc SLEEP_CHILL")
    category_affinity: Optional[Any] = Field(default=None, description="Thể loại ưu tiên")
    key_facts: List[str] = Field(default_factory=list, description="Các sự kiện chính")
    source_url: Optional[str] = Field(default=None, description="Đường dẫn nguồn")
    raw_payload: Dict[str, Any] = Field(default_factory=dict, description="Dữ liệu gốc từ nguồn khai thác")
    raw_metrics: Dict[str, Any] = Field(default_factory=dict, description="Chỉ số định lượng thô (alias cho metrics)")
    is_fallback: bool = Field(default=False, description="Đánh dấu dữ liệu từ cache dự phòng")

    @model_validator(mode="after")
    def sync_metrics_fields(self):
        """Đồng bộ tự động giữa metrics và raw_metrics."""
        if not self.metrics and self.raw_metrics:
            self.metrics = self.raw_metrics
        elif not self.raw_metrics and self.metrics:
            self.raw_metrics = self.metrics
        return self


class VideoState(BaseModel):
    video_id: str
    category: VideoCategory = VideoCategory.HIGH_IQ
    topic: TrendTopic = Field(default_factory=TrendTopic, description="Chủ đề xu hướng hoàn chỉnh")
    topic_title: str = Field(default="", description="Tiêu đề chủ đề (tương thích ngược)")
    topic_summary: str = Field(default="", description="Tóm tắt chủ đề (tương thích ngược)")
    script: ScriptSchema = Field(default_factory=ScriptSchema)
    assets: AssetPaths = Field(default_factory=AssetPaths)
    final_video_path: Optional[str] = None
    qa_status: QAStatus = QAStatus.PENDING
    qa_notes: str = ""
    publish_status: PublishStatus = PublishStatus.DRAFT
    schedule_time: Optional[str] = None
    caption: str = ""
    hashtags: List[str] = Field(default_factory=list)
    tiktok_url: Optional[str] = None

    @model_validator(mode="after")
    def sync_topic_attributes(self):
        """Đồng bộ tự động 2 chiều giữa topic object và các trường legacy topic_title / topic_summary."""
        # 1. Đồng bộ tiêu đề
        if self.topic.title and not self.topic_title:
            self.topic_title = self.topic.title
        elif self.topic_title and not self.topic.title:
            self.topic.title = self.topic_title

        # 2. Đồng bộ tóm tắt
        if self.topic.summary and not self.topic_summary:
            self.topic_summary = self.topic.summary
        elif self.topic_summary and not self.topic.summary:
            self.topic.summary = self.topic_summary

        return self

    def set_topic(self, topic: TrendTopic) -> None:
        """Helper chuyên dụng để gán chủ đề mới và tự động cập nhật topic_title, topic_summary."""
        self.topic = topic
        self.topic_title = topic.title
        self.topic_summary = topic.summary

    @property
    def is_multipart(self) -> bool:
        return self.script.is_multipart

    @property
    def parts(self) -> List[ScriptPart]:
        return self.script.parts

