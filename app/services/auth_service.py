from app.extensions.db import db
from app.models.referral import ReferralCodeSequence
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
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        referral_code: str,
    ) -> tuple[User | None, str | None]:
        email = email.lower().strip()
        if User.query.filter_by(email=email).first():
            return None, "email_exists"

        sponsor = None
        referral_code = (referral_code or "").strip().upper()
        if referral_code:
            sponsor = User.query.filter_by(referral_code=referral_code).first()
        if not sponsor:
            return None, "invalid_referral"

        sequence = ReferralCodeSequence()
        db.session.add(sequence)
        db.session.flush()

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            referred_by_id=sponsor.id,
            referral_code=f"MLM{sequence.id:04d}",
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user, None

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
