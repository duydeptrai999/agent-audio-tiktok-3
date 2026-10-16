"""
core/viral_scorer.py
Authoritative Algorithmic Viral Scoring Engine for Milestone 1.
Computes mathematical virality potential across:
- Growth Velocity (S_v): Logarithmic order-of-magnitude scaling normalized to 50k views/h
- Engagement Rate (S_er): Weighted comments (2x) and shares (3x) with 1,000 view floor
- Hook Curiosity (S_hook): Shock, paradox, question pattern detection with brevity modifier and cliche penalty
- Penalty Multiplier (M_pen): Policy and anti-spam multiplier in [0.0, 1.0]
Clamped strictly to [0.0, 100.0] with zero uncaught exceptions.
"""

from typing import Dict, Any, List, Optional, Union
import math
import re
import unicodedata


# ==========================================
# Compiled Pattern Groups
# ==========================================

SHOCK_PATTERNS = [
    # Vietnamese
    r"sự thật (?:kinh hoàng|điên rồ|rùng rợn|trần trụi|đen tối|ít ai biết|chấn động|quá kinh hoàng)",
    r"bí mật (?:kinh hoàng|động trời|tối mật|bị che giấu|chết người)",
    r"nguy hiểm nhất",
    r"bị lừa(?: dối)?",
    r"(?:gây )?sốc",
    r"kinh ngạc",
    r"không thể ngờ",
    r"cấm kỵ",
    r"lật tẩy|bóc trần",
    r"sai lầm (?:chết người|tai hại|nghiêm trọng)",
    r"hoàn toàn sai",
    r"sự thật là",
    r"chưa từng có",
    r"đe dọa tính mạng",
    r"bị cấm",
    r"bí ẩn",

    # English
    r"shocking (?:truth|fact|reality|discovery)",
    r"nobody knows|nobody told you",
    r"insane secret",
    r"you(?:'ve| have) been lied to",
    r"disturbing (?:fact|truth)",
    r"mind-blowing",
    r"exposed",
    r"terrifying truth",
    r"deadly mistake",
    r"dark secret",
    r"completely wrong",
    r"unbelievable",
    r"hidden truth",
    r"forbidden",
]

PARADOX_PATTERNS = [
    # Vietnamese
    r"nghịch lý(?: fermi| thời gian| kẻ nói dối| ông nội| du hành thời gian)?",
    r"càng\s+[^,.!?]+\s+càng",
    r"tại sao càng",
    r"vô lý nhưng(?: lại)?",
    r"tưởng là\s+.*\s+nhưng",
    r"trớ trêu|ngược đời",
    r"không thể tin nổi",
    r"ngược lại với",
    r"mâu thuẫn",
    r"sự thật trớ trêu",
    r"ngược ngạo",

    # English
    r"paradox(?:ical)?",
    r"the more\s+\w+,\s+the (?:less|more)",
    r"counter-intuitive",
    r"irony|ironic",
    r"seems impossible but",
    r"opposite of what you think",
    r"makes no sense",
    r"contradiction",
    r"fermi paradox",
    r"bizarre twist",
]

QUESTION_PATTERNS = [
    # Vietnamese
    r"tại sao",
    r"điều gì (?:sẽ )?xảy ra nếu",
    r"liệu có phải",
    r"vì sao",
    r"ai là người",
    r"bí ẩn gì đằng sau",
    r"có thật không",
    r"làm thế nào mà",
    r"bạn có dám",
    r"điều gì khiến",
    r"chuyện gì đã xảy ra",
    r"\?\s*$",

    # English
    r"why (?:does|do|is|are|did)",
    r"what (?:really )?happens if",
    r"is it (?:really )?possible",
    r"how did",
    r"what if",
    r"have you ever wondered",
    r"who really",
    r"the real reason why",
    r"\?\s*$",
]

CLICHE_PATTERNS = [
    # Vietnamese (Forbidden openers)
    r"^bạn có biết",
    r"^hôm nay mình sẽ kể",
    r"^chào các bạn",
    r"^hôm nay chúng ta sẽ",
    r"^mọi người ơi",
    r"^video này sẽ",

    # English
    r"^did you know",
    r"^today i will tell you",
    r"^hello guys",
    r"^welcome back to",
    r"^in this video",
    r"^subscribe to",
]

# Prohibited Tier 1 Blacklist Keywords (Zero score)
BANNED_KEYWORDS = [
    "kubet",
    "bet88",
    "baccarat",
    "tài xỉu",
    "nhà cái",
    "casino",
    "lô đề",
    "soi cầu",
    "cờ bạc",
    "kiếm tiền không cần vốn",
    "cam kết lợi nhuận 100%",
    "lừa đảo đa cấp",
    "lừa đảo",
]

# Sensitive Engagement Bait (50% penalty)
SENSITIVE_PATTERNS = [
    r"share ngay nếu không muốn xui xẻo",
    r"bấm tim để nhận lộc",
    r"tag 3 người bạn ngay",
    r"chia sẻ ngay để nhận tiền",
]


class ViralScorer:
    """
    Deterministic mathematical Viral Scoring Engine for Milestone 1.
    Calculates composite virality potential across Growth Velocity (S_v),
    Engagement Rate (S_er), Hook Curiosity (S_hook), and Penalty Multipliers (M_pen).
    """

    TARGET_VELOCITY_VPH: float = 50000.0
    BENCHMARK_ER: float = 0.08
    VIEW_DENOM_FLOOR: float = 1000.0
    MIN_AGE_HOURS: float = 0.5
    DEFAULT_AGE_HOURS: float = 24.0

    WEIGHT_VELOCITY: float = 0.35
    WEIGHT_ENGAGEMENT: float = 0.40
    WEIGHT_HOOK: float = 0.25

    def __init__(self):
        self._compiled_shock = [re.compile(p, re.IGNORECASE) for p in SHOCK_PATTERNS]
        self._compiled_paradox = [re.compile(p, re.IGNORECASE) for p in PARADOX_PATTERNS]
        self._compiled_question = [re.compile(p, re.IGNORECASE) for p in QUESTION_PATTERNS]
        self._compiled_cliche = [re.compile(p, re.IGNORECASE) for p in CLICHE_PATTERNS]
        self._compiled_sensitive = [re.compile(p, re.IGNORECASE) for p in SENSITIVE_PATTERNS]
        self._log_target_v = math.log10(self.TARGET_VELOCITY_VPH + 1.0)

    def _sanitize_str(self, val: Any) -> str:
        """Safely converts any input into an NFC-normalized stripped string."""
        if val is None:
            return ""
        if isinstance(val, str):
            return unicodedata.normalize("NFC", val).strip()
        return unicodedata.normalize("NFC", str(val)).strip()

    def _sanitize_float(self, val: Any, default: float = 0.0) -> float:
        """Sanitizes non-numeric or special float values."""
        if val is None:
            return default
        try:
            f = float(val)
            if math.isnan(f):
                return default
            if math.isinf(f):
                return 1e12 if f > 0 else 0.0
            return f
        except OverflowError:
            if isinstance(val, (int, float)):
                return 1e12 if val > 0 else 0.0
            val_str = str(val).strip()
            return 0.0 if val_str.startswith("-") else 1e12
        except (ValueError, TypeError):
            return default

    def calculate_velocity_score(
        self,
        views: Union[int, float],
        age_hours: Optional[Union[int, float]] = 24.0
    ) -> float:
        """
        Computes S_v in [0.0, 100.0] via logarithmic scaling:
        S_v = 100.0 * (log10(V + 1.0) / log10(V_target + 1.0))
        where V = views / t_eff, with t_eff = max(0.5, age_hours).
        """
        sanitized_views = max(0.0, self._sanitize_float(views, 0.0))
        if sanitized_views <= 0.0:
            return 0.0

        if age_hours is None:
            raw_age = self.DEFAULT_AGE_HOURS
        else:
            raw_age = self._sanitize_float(age_hours, self.DEFAULT_AGE_HOURS)

        t_eff = max(self.MIN_AGE_HOURS, raw_age)
        velocity = sanitized_views / t_eff

        if velocity <= 0.0:
            return 0.0

        log_v = math.log10(velocity + 1.0)
        s_v = 100.0 * (log_v / self._log_target_v)
        return max(0.0, min(100.0, s_v))

    def calculate_engagement_score(
        self,
        comments: Union[int, float],
        shares: Union[int, float],
        views: Union[int, float]
    ) -> float:
        """
        Computes S_er in [0.0, 100.0] with volume damping floor:
        E_w = 2.0 * comments + 3.0 * shares
        V_denom = max(1000, views)
        ER = E_w / V_denom
        S_er = min(100.0, max(0.0, 100.0 * (ER / ER_target)))
        """
        sanitized_comments = max(0.0, self._sanitize_float(comments, 0.0))
        sanitized_shares = max(0.0, self._sanitize_float(shares, 0.0))
        sanitized_views = max(0.0, self._sanitize_float(views, 0.0))

        e_w = 2.0 * sanitized_comments + 3.0 * sanitized_shares
        if e_w <= 0.0:
            return 0.0

        v_denom = max(self.VIEW_DENOM_FLOOR, sanitized_views)
        er = e_w / v_denom

        s_er = 100.0 * (er / self.BENCHMARK_ER)
        return max(0.0, min(100.0, s_er))

    def calculate_hook_score(self, text: Any) -> Dict[str, Any]:
        """
        Computes S_hook in [0.0, 100.0] analyzing shock, paradox, questions,
        and penalizing forbidden clichés. Returns score and matched pattern tags.
        """
        cleaned = self._sanitize_str(text)
        if not cleaned:
            return {"score": 0.0, "c_shock": 0, "c_paradox": 0, "c_question": 0, "c_brevity": 0, "p_cliche": 0}

        # Truncate to first 500 characters to prevent ReDoS
        eval_text = cleaned[:500]
        words = eval_text.split()
        word_count = len(words)

        # 1. Cliché check (at start)
        p_cliche = 0
        for pat in self._compiled_cliche:
            if pat.search(eval_text):
                p_cliche = 30
                break

        # 2. Shock patterns
        shock_matches = sum(1 for pat in self._compiled_shock if pat.search(eval_text))
        if shock_matches >= 2:
            c_shock = 35
        elif shock_matches == 1:
            c_shock = 25
        else:
            c_shock = 0

        # 3. Paradox patterns
        paradox_matches = sum(1 for pat in self._compiled_paradox if pat.search(eval_text))
        if paradox_matches >= 2:
            c_paradox = 35
        elif paradox_matches == 1:
            c_paradox = 25
        else:
            c_paradox = 0

        # 4. Question / curiosity
        has_question = any(pat.search(eval_text) for pat in self._compiled_question)
        c_question = 25 if has_question else 0

        # 5. Brevity modifier
        if 5 <= word_count <= 16:
            c_brevity = 10
        elif 1 <= word_count <= 4 or 17 <= word_count <= 28:
            c_brevity = 0
        elif word_count > 28:
            c_brevity = -10
        else:
            c_brevity = 0

        # Only award brevity if at least one curiosity pattern matched or word count is normal
        raw_score = c_shock + c_paradox + c_question + c_brevity - p_cliche
        final_hook = max(0.0, min(100.0, float(raw_score)))

        return {
            "score": final_hook,
            "c_shock": c_shock,
            "c_paradox": c_paradox,
            "c_question": c_question,
            "c_brevity": c_brevity,
            "p_cliche": p_cliche,
            "shock_matches": shock_matches,
            "paradox_matches": paradox_matches,
            "has_question": has_question,
            "word_count": word_count,
        }

    def calculate_penalty_multiplier(
        self,
        text: Any = "",
        is_sensitive: bool = False,
        is_banned: bool = False
    ) -> Dict[str, Any]:
        """
        Computes M_pen in [0.0, 1.0] analyzing safety and spam triggers.
        """
        if is_banned:
            return {"multiplier": 0.0, "reason": "is_banned_flag"}

        raw_str = self._sanitize_str(text)
        if not raw_str:
            return {"multiplier": 0.5 if is_sensitive else 1.0, "reason": "clean"}

        eval_text = raw_str.lower()

        # Tier 1: Hard violation check
        for kw in BANNED_KEYWORDS:
            kw_norm = unicodedata.normalize("NFC", kw).lower()
            if kw_norm in eval_text:
                return {"multiplier": 0.0, "reason": f"banned_keyword:{kw}"}

        multiplier = 1.0

        # Tier 2: Sensitive check
        if is_sensitive:
            multiplier *= 0.5
        else:
            for pat in self._compiled_sensitive:
                if pat.search(eval_text):
                    multiplier *= 0.5
                    break

        # Tier 3: Formatting Spam
        # Excessive punctuation (4 or more consecutive punctuation marks)
        if re.search(r"[!?.,]{4,}", raw_str):
            multiplier *= 0.7

        # Excessive ALL CAPS (> 60% caps in string > 20 chars)
        letters = [c for c in raw_str if c.isalpha()]
        if len(raw_str) > 20 and len(letters) >= 10:
            caps_count = sum(1 for c in letters if c.isupper())
            if caps_count / len(letters) > 0.60:
                multiplier *= 0.7

        # Hashtag stuffing (> 8 hashtags)
        hashtags = re.findall(r"#\w+", raw_str)
        if len(hashtags) > 8:
            multiplier *= 0.7

        multiplier = max(0.0, min(1.0, multiplier))
        return {"multiplier": multiplier, "reason": "evaluated"}

    def score(
        self,
        views: Any = 0,
        comments: Any = 0,
        shares: Any = 0,
        age_hours: Any = 24.0,
        hook_text: Any = "",
        title: Any = "",
        is_sensitive: bool = False,
        is_banned: bool = False
    ) -> Dict[str, Any]:
        """
        Master calculation returning final ViralScore and full component breakdown.
        """
        s_v = self.calculate_velocity_score(views, age_hours)
        s_er = self.calculate_engagement_score(comments, shares, views)

        # Hook text evaluates hook_text if present, else title
        hook_str = self._sanitize_str(hook_text)
        title_str = self._sanitize_str(title)
        eval_hook_str = hook_str or title_str
        hook_res = self.calculate_hook_score(eval_hook_str)
        s_hook = hook_res["score"]

        # Penalty checks combined text
        full_text = f"{title_str} {hook_str}".strip()
        pen_res = self.calculate_penalty_multiplier(full_text, is_sensitive, is_banned)
        m_pen = pen_res["multiplier"]

        composite = (
            self.WEIGHT_VELOCITY * s_v
            + self.WEIGHT_ENGAGEMENT * s_er
            + self.WEIGHT_HOOK * s_hook
        ) * m_pen

        final_score = round(max(0.0, min(100.0, composite)), 2)

        return {
            "viral_score": final_score,
            "s_velocity": round(s_v, 2),
            "s_engagement": round(s_er, 2),
            "s_hook": round(s_hook, 2),
            "m_penalty": round(m_pen, 2),
            "hook_details": hook_res,
            "penalty_details": pen_res,
        }

    def calculate_score(self, topic: Any) -> float:
        """
        Convenience adapter for TrendTopic or dict objects.
        Returns float in [0.0, 100.0].
        """
        if topic is None:
            return 0.0

        views = 0
        comments = 0
        shares = 0
        age_hours = 24.0
        title = ""
        hook_text = ""
        is_sensitive = False
        is_banned = False

        if isinstance(topic, dict):
            title = self._sanitize_str(topic.get("title", ""))
            hook_text = self._sanitize_str(topic.get("recommended_hook", topic.get("hook", "")))
            metrics = topic.get("metrics", {})
            if isinstance(metrics, dict):
                views = metrics.get("views", 0)
                comments = metrics.get("comments", 0)
                shares = metrics.get("shares", 0)
                age_hours = metrics.get("age_hours", metrics.get("hours", 24.0))
            else:
                views = topic.get("views", 0)
                comments = topic.get("comments", 0)
                shares = topic.get("shares", 0)
                age_hours = topic.get("age_hours", topic.get("hours", 24.0))
            is_sensitive = bool(topic.get("is_sensitive", False))
            is_banned = bool(topic.get("is_banned", False))
        else:
            # Assume TrendTopic or similar object
            title = self._sanitize_str(getattr(topic, "title", ""))
            hook_text = self._sanitize_str(getattr(topic, "recommended_hook", ""))
            metrics = getattr(topic, "metrics", {})
            if isinstance(metrics, dict) and metrics:
                views = metrics.get("views", 0)
                comments = metrics.get("comments", 0)
                shares = metrics.get("shares", 0)
                age_hours = metrics.get("age_hours", metrics.get("hours", metrics.get("delta_time_hours", 24.0)))
            elif hasattr(topic, "raw_metrics") and getattr(topic, "raw_metrics"):
                rm = getattr(topic, "raw_metrics")
                if isinstance(rm, dict):
                    views = rm.get("views", 0)
                    comments = rm.get("comments", 0)
                    shares = rm.get("shares", 0)
                    age_hours = rm.get("age_hours", rm.get("hours", rm.get("delta_time_hours", 24.0)))
                else:
                    views = getattr(rm, "views", 0)
                    comments = getattr(rm, "comments", 0)
                    shares = getattr(rm, "shares", 0)
                    age_hours = getattr(rm, "delta_time_hours", getattr(rm, "age_hours", 24.0))
            elif isinstance(metrics, dict):
                views = metrics.get("views", 0)
                comments = metrics.get("comments", 0)
                shares = metrics.get("shares", 0)
                age_hours = metrics.get("age_hours", metrics.get("hours", 24.0))

            is_sensitive = bool(getattr(topic, "is_sensitive", False))
            is_banned = bool(getattr(topic, "is_banned", False))

        res = self.score(
            views=views,
            comments=comments,
            shares=shares,
            age_hours=age_hours,
            hook_text=hook_text,
            title=title,
            is_sensitive=is_sensitive,
            is_banned=is_banned,
        )
        return float(res["viral_score"])

    def score_topic(self, topic: Any) -> float:
        """Alias for calculate_score."""
        return self.calculate_score(topic)


def compute_viral_score(
    views: Any = 0,
    comments: Any = 0,
    shares: Any = 0,
    age_hours: Any = 24.0,
    hook_text: Any = "",
    title: Any = "",
    is_sensitive: bool = False,
    is_banned: bool = False
) -> float:
    """Returns rounded composite viral score in [0.0, 100.0]."""
    scorer = ViralScorer()
    res = scorer.score(
        views=views,
        comments=comments,
        shares=shares,
        age_hours=age_hours,
        hook_text=hook_text,
        title=title,
        is_sensitive=is_sensitive,
        is_banned=is_banned,
    )
    return res["viral_score"]
