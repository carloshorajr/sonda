from backend.utils.datetime_utils import now

from backend.models.event import Event
from backend.repositories.event_repository import EventRepository


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
    def list():

        events = EventRepository.load()

        print("EVENTOS:", len(events))

        return events