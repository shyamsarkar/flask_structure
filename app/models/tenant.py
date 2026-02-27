from app.extensions.db import db
from .base import BaseModel


class Tenant(BaseModel):
    __tablename__ = "tenants"

    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=0)  # 0=active, 1=inactive, 2=pending

    memberships = db.relationship(
        "Membership",
        back_populates="tenant",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Tenant {self.name}>"