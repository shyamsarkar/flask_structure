from flask_mail import Message

from app.extensions.mail import mail


def send_reset_email(app, to: str, reset_url: str):
    """
    Sends password reset email.
    Call via Celery task or directly in dev.
    """
    with app.app_context():
        msg = Message(
            subject="Reset your password",
            recipients=[to],
            body=f"""Hi,

You requested a password reset. Click the link below to reset your password.
This link expires in 2 hours.

{reset_url}

If you did not request this, ignore this email.
""",
        )
        mail.send(msg)
