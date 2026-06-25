import psutil
import socket
import subprocess
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

        if days > 0:

            return f"{days}d {hours}h {minutes}min"

        return f"{hours}h {minutes}min"
    
    @staticmethod
    def get_network_interfaces():

        interfaces = []

        ignored = (
            "lo",
            "docker",
            "br-",
            "veth"
        )

        addrs = psutil.net_if_addrs()

        stats = psutil.net_if_stats()

        for name, addresses in addrs.items():

            if name.startswith(ignored):
                continue

            ip = None
            mac = None

            for addr in addresses:

                if addr.family == socket.AF_INET:

                    ip = addr.address

                elif addr.family == psutil.AF_LINK:

                    mac = addr.address

            if not ip:
                continue

            if name.startswith("eth"):
                label = "Ethernet"

            elif name.startswith("wlan"):
                label = "Wi-Fi"

            else:
                label = name

            ssid = None

            if name.startswith("wlan"):

                ssid = SystemService.get_wifi_ssid(name)

            interfaces.append({

                "name": name,

                "label": label,

                "ip": ip,

                "mac": mac,

                "ssid": ssid,

                "status": (
                    "UP"
                    if stats[name].isup
                    else "DOWN"
                )

            })

        return interfaces
    
    @staticmethod
    def get_wifi_ssid(interface):

        try:

            result = subprocess.run(

                [
                    "nmcli",
                    "-t",
                    "-f",
                    "GENERAL.CONNECTION",
                    "device",
                    "show",
                    interface
                ],

                capture_output=True,

                text=True,

                check=True

            )

            line = result.stdout.strip()

            if ":" in line:

                return line.split(":", 1)[1]

            return None

        except Exception:

            return None
    
    @staticmethod
    def get_disk_usage():

        usage = psutil.disk_usage("/")

        total = round(usage.total / (1024 ** 3), 1)

        used = round(usage.used / (1024 ** 3), 1)

        free = round(usage.free / (1024 ** 3), 1)

        return {

            "percent": round(usage.percent, 1),

            "used": used,

            "free": free,

            "total": total

        }