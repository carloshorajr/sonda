from datetime import datetime

from backend.models.event import Event
from backend.repositories.event_repository import EventRepository


class EventService:

    @staticmethod
    def info(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=datetime.now(),
                level="INFO",
                source=source,
                message=message
            )
        )
    
    @staticmethod
    def warning(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=datetime.now(),
                level="WARNING",
                source=source,
                message=message
            )
        )


    @staticmethod
    def error(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=datetime.now(),
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