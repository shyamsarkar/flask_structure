from flask_migrate import Migrate, upgrade
from app.extensions import db
# from app.models import User
from app import create_app

migrate = Migrate()

def run_migration():
    migrate.init_app(create_app(), db)

    with create_app().app_context():
        upgrade()

# if __name__ == '__main__':
#     run_migration()
