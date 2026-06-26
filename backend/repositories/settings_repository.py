import json
from pathlib import Path


class SettingsRepository:

    SETTINGS_FILE = Path("data/settings.json")


    @classmethod
    def load(cls):

        if not cls.SETTINGS_FILE.exists():
            return {}

        with open(cls.SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)


    @classmethod
    def save(cls, data):

        with open(cls.SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )