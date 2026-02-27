from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions.db import db
from app.models.user import User


class AuthService:

    @staticmethod
    def authenticate(email: str, password: str) -> User | None:
        if not email or not password:
            return None
        user = User.query.filter_by(email=email.lower().strip()).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def register(email: str, password: str, first_name: str, last_name: str) -> User | None:
        email = email.lower().strip()
        if User.query.filter_by(email=email).first():
            return None  # already exists

        user = User(
            email=email,
            password_hash=generate_password_hash(password),
            first_name=first_name,
            last_name=last_name,
        )
        db.session.add(user)
        db.session.commit()
        return user