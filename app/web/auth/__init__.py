from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

from app.web.auth import views  # noqa: E402, F401
