from flask import Blueprint

api_bp = Blueprint('api', __name__)
auth_bp = Blueprint('auth', __name__)

from app.views.api import *
from app.views.auth import *
