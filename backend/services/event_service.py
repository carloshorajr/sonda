from backend.utils.datetime_utils import now

from backend.models.event import Event
from backend.repositories.event_repository import EventRepository

from datetime import timedelta

class EventService:

    @staticmethod
    def info(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="INFO",
                source=source,
                message=message
            )
        )
    
    @staticmethod
    def warning(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="WARNING",
                source=source,
                message=message
            )
        )


    @staticmethod
    def error(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="ERROR",
                source=source,
                message=message
            )
        )
    
    @staticmethod
    def list(filters=None):

        events = EventRepository.load()

        if filters is None:
            return events

        period = filters.get("period")

        if period == "today":

            limite = now().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        elif period == "24h":

            limite = now() - timedelta(hours=24)

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        elif period == "7d":

            limite = now() - timedelta(days=7)

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        return events
    
    @staticmethod
    def sources():

        events = EventRepository.load()

        return sorted(
            {
                event.source
                for event in events
            }
        )