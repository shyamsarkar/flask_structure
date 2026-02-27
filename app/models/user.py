# # app/models/user.py
# from app.extensions.db import db
# from flask_login import UserMixin
# from .base import BaseModel

# class User(UserMixin, BaseModel):
#     __tablename__ = "users"

#     email = db.Column(db.String(255), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)

#     first_name = db.Column(db.String(100))
#     last_name = db.Column(db.String(100))

#     is_active = db.Column(db.Boolean, default=True)
#     last_login_at = db.Column(db.DateTime)

#     memberships = db.relationship(
#         "Membership",
#         back_populates="user",
#         cascade="all, delete-orphan",
#     )
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions.db import db
from .base import BaseModel


class User(UserMixin, BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    is_active = db.Column(db.Boolean, default=True)
    last_login_at = db.Column(db.DateTime)

    memberships = db.relationship(
        "Membership",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    # --- password helpers ---
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __repr__(self) -> str:
        return f"<User {self.email}>"