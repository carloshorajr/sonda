from datetime import datetime
from zoneinfo import ZoneInfo

from backend.repositories.settings_repository import SettingsRepository

def now():

    settings = SettingsRepository.load()

    return datetime.now(
        ZoneInfo(settings.timezone)
    )

def parse_datetime(value: str):

    dt = datetime.fromisoformat(value)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=get_timezone())

    return dt