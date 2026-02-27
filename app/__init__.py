from flask import Flask

from app.extensions.cache import cache
from app.extensions.celery import init_celery
from app.extensions.db import db
from app.extensions.limiter import limiter
from app.extensions.login_manager import login_manager
from app.extensions.mail import mail
from app.extensions.migrate import migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    mail.init_app(app)
    init_celery(app)

    # Blueprints
    from app.web import web_bp

    app.register_blueprint(web_bp)

    from app.api import api_bp

    app.register_blueprint(api_bp)

    return app
