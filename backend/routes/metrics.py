from flask import Blueprint, render_template, request

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.route("/metrics")
def metrics():

    return render_template(
        "metrics.html",
        page_title="Métricas",
        page_subtitle="Indicadores coletados",
        current_page=request.path
    )