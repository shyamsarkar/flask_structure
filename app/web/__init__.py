from flask import Blueprint
from flask_login import login_required

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
@login_required
def index():
    return "Welcome!"


from app.web.auth import (
    auth_bp,  # noqa: E402
    routes,  # noqa: E402, F401
)

web_bp.register_blueprint(auth_bp)
