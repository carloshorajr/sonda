from backend.repositories.settings_repository import SettingsRepository

from backend.services.event_service import EventService

class SettingsController:

    @staticmethod
    def get_page_data():

        settings = SettingsRepository.load()

        return {
            "page_title": "Configurações",
            "page_subtitle": "Gerenciamento da Sonda",
            "settings": settings
        }
    
    @staticmethod
    def save(form):

        settings = SettingsRepository.load()

        settings.update_from_form(form)

        SettingsRepository.save(settings)

        EventService.info(
            source="Configurações",
            message="Configurações atualizadas."
        )