from flask import Blueprint, render_template, request

from backend.controllers.events_controller import EventsController

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def events():

    return render_template(
        "events.html",
        current_page=request.path,
        **EventsController.get_page_data(request.args)
    )