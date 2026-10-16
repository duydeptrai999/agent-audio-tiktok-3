import json
from pathlib import Path
from typing import Dict, Any, List
from config.settings import DATABASE_DIR

MEMORY_FILE = DATABASE_DIR / "agent_memory.json"

class AgentMemoryManager:
    """Quản lý bộ nhớ phản hồi bền vững riêng biệt cho từng Agent."""

    @staticmethod
    def _init_memory() -> Dict[str, Any]:
        return {
            "version": "1.0",
            "agents": {
                "trend_hunter": [],
                "scriptwriter": [],
                "reviewer": [],
                "voiceover": [],
                "footage": [],
                "music": [],
                "director": [],
                "qa_lead": [],
                "publisher": []
            },
            "history": []
        }

    @classmethod
    def load_memory(cls) -> Dict[str, Any]:
        if not MEMORY_FILE.exists():
            data = cls._init_memory()
            cls.save_memory(data)
            return data
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return cls._init_memory()

    @classmethod
    def save_memory(cls, data: Dict[str, Any]) -> None:
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def get_agent_feedback(cls, agent_name: str) -> List[str]:
        memory = cls.load_memory()
        return memory.get("agents", {}).get(agent_name, [])

    @classmethod
    def record_feedback(cls, agent_name: str, feedback_text: str, metric_context: str = "") -> None:
        memory = cls.load_memory()
        if agent_name not in memory["agents"]:
            memory["agents"][agent_name] = []
        
        entry = {
            "feedback": feedback_text,
            "context": metric_context
        }
        memory["agents"][agent_name].append(entry)
        memory["history"].append({
            "target_agent": agent_name,
            "feedback": feedback_text,
            "context": metric_context
        })
        # Giữ tối đa 5 chỉ thị gần nhất cho mỗi agent
        memory["agents"][agent_name] = memory["agents"][agent_name][-5:]
        cls.save_memory(memory)
