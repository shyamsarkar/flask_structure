from flask import Flask
import os
from app import models
from app import scripts
from app.routes import api_bp
from app.extensions import db, migrate, admin, babel, custom_cli
# from flask_jwt_extended import JWTManager
# from flask_mail import Mail
# from celery import Celery
# from app.auth.views import auth
from dotenv import load_dotenv


# from app.extensions import mail, celery, jwt, login_manager
# from app.auth.views import auth




def create_app(config_object='config.DevelopmentConfig'):
    # Load .env
    dotenv_path = os.path.abspath(os.path.join(__file__,  "..", "..", '.env'))
    if not os.path.exists(dotenv_path):
        quit("=====================.env file missing=====================")
    load_dotenv(dotenv_path)
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    # app.config.from_pyfile('config.py', silent=True)
    migrate.init_app(app, db)
    admin.init_app(app)
    babel.init_app(app)


    """ Initialize All Apps """
    db.init_app(app)
    # mail.init_app(app)
    # celery.init_app(app)
    # login_manager.init_app(app)
    # api.init_app(app)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    """ Register All Routes """
    app.register_blueprint(api_bp)

    app.cli.add_command(custom_cli)

    # jwt = JWTManager(app)

    return app
