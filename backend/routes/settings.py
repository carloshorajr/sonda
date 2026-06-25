from flask import Blueprint, render_template, request

settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings")
def settings():

    return render_template(
        "settings.html",
        page_title="Configurações",
        page_subtitle="Gerenciamento da Sonda",
        current_page=request.path
    )