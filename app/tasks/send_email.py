from flask_mail import Message
from app.extensions.mail import mail
from app.extensions.celery import celery

@celery.task(name="tasks.send_email")
def send_email(subject: str, recipients: list[str], body: str):
    msg = Message(
        subject=subject,
        recipients=recipients,
        body=body,
    )
    mail.send(msg)