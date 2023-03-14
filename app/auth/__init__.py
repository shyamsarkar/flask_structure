from flask import Blueprint
from flask_login import LoginManager
from project.extensions import db, login_manager
from project.auth.views import AuthView

auth = Blueprint('auth', __name__, url_prefix='/auth')

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

auth_view = AuthView.as_view('auth')

auth.add_url_rule('/login', methods=['GET', 'POST'], view_func=auth_view)
auth.add_url_rule('/register', methods=['GET', 'POST'], view_func=auth_view)
