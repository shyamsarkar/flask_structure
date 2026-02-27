from app.extensions.db import db
from app.models.user import User


class AuthService:
    @staticmethod
    def authenticate(email: str, password: str) -> User | None:
        if not email or not password:
            return None
        user = User.query.filter_by(email=email.lower().strip()).first()
        if user and user.check_password(password):
            user.update_last_login()
            return user
        return None

    @staticmethod
    def register(
        email: str, password: str, first_name: str, last_name: str
    ) -> User | None:
        email = email.lower().strip()
        if User.query.filter_by(email=email).first():
            return None  # already exists

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_email(email: str) -> User | None:
        return User.query.filter_by(email=email.lower().strip()).first()

    @staticmethod
    def get_by_reset_token(token: str) -> User | None:
        user = User.query.filter_by(reset_token=token).first()
        if user and user.reset_token_valid:
            return user
        return None

    @staticmethod
    def reset_password(token: str, new_password: str) -> bool:
        user = AuthService.get_by_reset_token(token)
        if not user:
            return False
        user.set_password(new_password)
        user.clear_reset_token()
        return True
