from flask import Blueprint, render_template, request

from backend.controllers.settings_controller import SettingsController

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
def settings():

    return render_template(
        "settings.html",

        current_page=request.path,

        **SettingsController.get_page_data()
    )