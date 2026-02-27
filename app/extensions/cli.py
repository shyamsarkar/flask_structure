from flask.cli import AppGroup
from app.extensions.db import db

custom_cli = AppGroup("custom")

@custom_cli.command("reset-db")
def reset_db():
    db.drop_all()
    db.create_all()
    print("Database reset complete")