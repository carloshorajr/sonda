from flask import Blueprint, render_template, request

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        page_title="Dashboard",
        page_subtitle="Visão geral da Sonda",
        current_page=request.path
    )