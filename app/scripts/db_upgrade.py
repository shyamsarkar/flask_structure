from flask_migrate import upgrade
from app.extensions import db
from app import create_app

with create_app().app_context():
    upgrade()

print("Database upgraded successfully!")
