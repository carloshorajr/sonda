import json
from pathlib import Path
from dataclasses import asdict
from datetime import datetime

from backend.models.event import Event


class EventRepository:

    EVENTS_FILE = Path("data/events.json")

    @classmethod
    def load(cls):

        if not cls.EVENTS_FILE.exists():
            return []

        with open(cls.EVENTS_FILE, "r", encoding="utf-8") as f:

            data = json.load(f)

        events = []

        for item in data:

            events.append(
                Event(
                    timestamp=datetime.fromisoformat(item["timestamp"]),
                    level=item["level"],
                    source=item["source"],
                    message=item["message"]
                )
            )

        return events
    
    @classmethod
    def add(cls, event: Event):

        events = cls.load()

        events.append(event)

        serialized = []

        for e in events:

            serialized.append({
                "timestamp": e.timestamp.isoformat(),
                "level": e.level,
                "source": e.source,
                "message": e.message
            })

        with open(cls.EVENTS_FILE, "w", encoding="utf-8") as f:

            json.dump(
                serialized,
                f,
                indent=4,
                ensure_ascii=False
            )