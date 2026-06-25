from flask import Flask

from backend.routes.dashboard import dashboard_bp
from backend.routes.settings import settings_bp
from backend.routes.metrics import metrics_bp
from backend.routes.events import events_bp
from backend.routes.system import system_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates"
)

app.register_blueprint(dashboard_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(metrics_bp)
app.register_blueprint(events_bp)
app.register_blueprint(system_bp)