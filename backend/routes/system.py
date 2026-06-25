from flask import Blueprint, render_template, request

from backend.services.system_service import SystemService
from backend.services.network_service import NetworkService

system_bp = Blueprint("system", __name__)


@system_bp.route("/system")
def system():

    info = SystemService.get_system_info()
    disk = SystemService.get_disk_usage()

    return render_template(
        "system.html",

        page_title="Sistema",
        page_subtitle="Informações da Sonda",
        current_page=request.path,

        hostname=info["hostname"],
        cpu=info["cpu_percent"],
        memory=info["memory_percent"],

        disk=disk,

        interfaces=NetworkService.get_network_interfaces(),

        uptime=SystemService.get_uptime()
    )