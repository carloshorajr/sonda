from backend.services.event_service import EventService

class EventsController:

    @staticmethod
    def get_page_data(filters):

        events = EventService.list()

        level = filters.get("level")

        if level:
            events = [
                event
                for event in events
                if event.level == level
            ]

        events.sort(
            key=lambda e: e.timestamp,
            reverse=True
        )

        return {
            "page_title": "Eventos",
            "page_subtitle": "Registro de ocorrências",
            "events": events,
            "filters": filters
        }