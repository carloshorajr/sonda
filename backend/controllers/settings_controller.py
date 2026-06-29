from backend.repositories.settings_repository import SettingsRepository

from backend.services.event_service import EventService
from backend.services.system_service import SystemService

class SettingsController:

    @staticmethod
    def get_page_data():

        settings = SettingsRepository.load()
        
        system = SystemService.get_system_info()

        return {
            "page_title": "Configurações",
            "page_subtitle": "Gerenciamento da Sonda",
            "settings": settings,
            "hostname": system["hostname"]
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