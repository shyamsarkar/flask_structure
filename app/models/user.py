from datetime import datetime, timedelta
from secrets import token_urlsafe

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions.db import db

from .base import BaseModel


class User(UserMixin, BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    is_active = db.Column(db.Boolean, default=True)
    last_login_at = db.Column(db.DateTime, nullable=True)

    # password reset
    reset_token = db.Column(db.String(255), nullable=True)
    reset_token_expires_at = db.Column(db.DateTime, nullable=True)

    memberships = db.relationship(
        "Membership",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    # --- password ---
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    # --- reset token (devise :recoverable equivalent) ---
    def generate_reset_token(self) -> str:
        token = token_urlsafe(32)
        self.reset_token = token
        self.reset_token_expires_at = datetime.utcnow() + timedelta(hours=2)
        self.save()
        return token

    def clear_reset_token(self):
        self.reset_token = None
        self.reset_token_expires_at = None
        self.save()

    @property
    def reset_token_valid(self) -> bool:
        return (
            self.reset_token is not None
            and self.reset_token_expires_at is not None
            and self.reset_token_expires_at > datetime.utcnow()
        )

    # --- last login (devise equivalent) ---
    def update_last_login(self):
        self.last_login_at = datetime.utcnow()
        self.save()

    # --- role check ---
    def has_role(self, role_name: str, tenant) -> bool:
        from .membership import Membership

        return (
            Membership.query.filter_by(
                user_id=self.id,
                tenant_id=tenant.id,
                role=role_name,
            ).first()
            is not None
        )

    def get_tenants(self):
        from .membership import Membership
        from .tenant import Tenant

        return (
            Tenant.query.join(Membership, Membership.tenant_id == Tenant.id)
            .filter(Membership.user_id == self.id)
            .all()
        )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __repr__(self):
        return f"<User {self.email}>"
