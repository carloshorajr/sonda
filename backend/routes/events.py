from flask import Blueprint, render_template, request

events_bp = Blueprint("events", __name__)


@events_bp.route("/events")
def events():

    return render_template(
        "events.html",
        page_title="Eventos",
        page_subtitle="Registro de ocorrências",
        current_page=request.path
    )