import json
from pathlib import Path
from dataclasses import asdict

from backend.models.settings import Settings

class SettingsRepository:

    SETTINGS_FILE = Path("data/settings.json")

    @classmethod
    def load(cls):

        if not cls.SETTINGS_FILE.exists():
            return {}

        with open(cls.SETTINGS_FILE, "r", encoding="utf-8") as f:

            data = json.load(f)

            return Settings(**data)

    @classmethod
    def save(cls, settings: Settings):

        with open(cls.SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(
                asdict(settings),
                f,
                indent=4,
                ensure_ascii=False
            )