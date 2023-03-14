from flask import current_app
from flask_mail import Message
from myapp.app import create_app
from myapp.app.extensions import mail
from myapp.app.tasks.celery import make_celery

app = create_app()
celery = make_celery(app)

@celery.task(name='tasks.send_email')
def send_email(subject, recipients, body):
    with app.app_context():
        msg = Message(subject=subject, recipients=recipients)
        msg.body = body
        mail.send(msg)
