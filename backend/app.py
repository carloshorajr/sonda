from flask import Flask, render_template, request
from backend.services.system_service import SystemService

app = Flask(
    __name__,
    template_folder="../frontend/templates"
)

@app.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        page_title="Dashboard",
        page_subtitle="Visão geral da Sonda",
        current_page=request.path
    )

@app.route("/settings")
def settings():

    return render_template(
        "settings.html",
        page_title="Configurações",
        page_subtitle="Gerenciamento da Sonda",
        current_page=request.path
    )

@app.route("/metrics")
def metrics():

    return render_template(
        "metrics.html",
        page_title="Métricas",
        page_subtitle="Indicadores coletados",
        current_page=request.path
    )

@app.route("/events")
def events():

    return render_template(
        "events.html",
        page_title="Eventos",
        page_subtitle="Registro de ocorrências",
        current_page=request.path
    )

@app.route("/system")
def system():

    info = SystemService.get_system_info()

    return render_template(
        "system.html",

        page_title="Sistema",
        page_subtitle="Informações da Sonda",
        current_page=request.path,

        hostname=info["hostname"],

        cpu=info["cpu_percent"],

        memory=info["memory_percent"],

        disk=info["disk_percent"],

        ip=SystemService.get_ip(),

        uptime=SystemService.get_uptime()
    )