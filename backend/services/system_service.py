import psutil
import socket
from datetime import datetime

class SystemService:

    @staticmethod
    def get_system_info():

        uptime_seconds = int(
            psutil.boot_time()
        )

        with open("/etc/host_hostname", "r") as f:
            hostname = f.read().strip()

        return {

            "hostname": hostname,

            "cpu_percent": psutil.cpu_percent(),

            "memory_percent":
                round(
                    psutil.virtual_memory().percent,
                    1
                ),

            "disk_percent":
                round(
                    psutil.disk_usage("/").percent,
                    1
                ),

            "boot_time": uptime_seconds
        }

    @staticmethod
    def get_uptime():

        boot = datetime.fromtimestamp(
            psutil.boot_time()
        )

        delta = datetime.now() - boot

        days = delta.days

        hours = delta.seconds // 3600

        minutes = (
            delta.seconds % 3600
        ) // 60

        return f"{days} Dias {hours} Horas {minutes} Minutos"
    
    @staticmethod
    def get_ip():

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect(("8.8.8.8", 80))

            ip = s.getsockname()[0]

            s.close()

            return ip

        except Exception:

            return "Não disponível"
    
    @staticmethod
    def get_disk_usage():

        return round(
            psutil.disk_usage("/").percent,
            1
        )