from flask import Blueprint
from flask_jwt_extended import JWTManager
from project.extensions import db, jwt


auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

jwt_manager = JWTManager()


@jwt_manager.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt_manager.user_loader_callback_loader
def user_loader_callback(identity):
    from project.auth.models import User
    return User.query.get(identity)


def init_app(app):
    from project.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    jwt_manager.init_app(app)
