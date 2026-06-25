from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:

    timestamp: datetime

    level: str

    title: str

    message: str