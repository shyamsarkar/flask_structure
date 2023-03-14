from app.extensions import celery, mail
from flask import current_app
from flask_mail import Message

@celery.task
def send_email(recipient, subject, body):
    with current_app.app_context():
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        mail.send(msg)
