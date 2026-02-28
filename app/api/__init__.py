from flask import Blueprint

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

from app.api.auth import views  # noqa: E402, F401
