from backend.services.event_service import EventService


class EventsController:

    @staticmethod
    def get_page_data():

        events = EventService.list()

        events.sort(
            key=lambda e: e.timestamp,
            reverse=True
        )

        return {
            "page_title": "Eventos",
            "page_subtitle": "Registro de ocorrências",
            "events": events
        }