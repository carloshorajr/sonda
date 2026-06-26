from flask import Blueprint, render_template, request, redirect

from backend.controllers.settings_controller import SettingsController

settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings", methods=["GET", "POST"])
def settings():

    if request.method == "POST":
        SettingsController.save(request.form)
        return redirect("/settings")

    return render_template(
        "settings.html",
        current_page=request.path,
        **SettingsController.get_page_data()
    )