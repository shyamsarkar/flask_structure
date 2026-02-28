from flask import Blueprint

api_auth_bp = Blueprint("api_auth", __name__, url_prefix="/auth")

from app.api.auth import views  # noqa: E402, F401
