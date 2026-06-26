from backend.repositories.settings_repository import SettingsRepository

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

        settings.nome = form["nome"]
        settings.cliente = form["cliente"]
        settings.local = form["local"]
        settings.descricao = form["descricao"]
        settings.uuid = form["uuid"]

        settings.heartbeat = int(form["heartbeat"])
        settings.coleta = int(form["coleta"])

        SettingsRepository.save(settings)