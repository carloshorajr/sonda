from dataclasses import dataclass

@dataclass
class Settings:

    nome: str

    cliente: str

    local: str

    descricao: str

    uuid: str

    heartbeat: int

    coleta: int

    timezone: str

    idioma: str

    log_level: str