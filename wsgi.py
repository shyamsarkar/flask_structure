from dotenv import load_dotenv

load_dotenv()

from app import create_app
from app.extensions.celery import init_celery

app = create_app()
celery = init_celery(app)

if __name__ == "__main__":
    app.run()
