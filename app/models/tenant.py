import enum

from app.extensions.db import db

from .base import BaseModel


class TenantStatus(enum.Enum):
    active = 0
    inactive = 1
    pending = 2


class Tenant(BaseModel):
    __tablename__ = "tenants"

    name = db.Column(db.String(255), nullable=False)
    status = db.Column(
        db.Enum(TenantStatus),
        default=TenantStatus.active,
        nullable=False,
    )

    # has_many :memberships, dependent: :destroy
    memberships = db.relationship(
        "Membership",
        back_populates="tenant",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    # has_many :users, through: :memberships
    def get_users(self):
        from .membership import Membership
        from .user import User

        return (
            User.query.join(Membership, Membership.user_id == User.id)
            .filter(Membership.tenant_id == self.id)
            .all()
        )

    # --- enum helpers (active?, inactive?, pending?) ---
    def is_active(self) -> bool:
        return self.status == TenantStatus.active

    def is_inactive(self) -> bool:
        return self.status == TenantStatus.inactive

    def is_pending(self) -> bool:
        return self.status == TenantStatus.pending

    def __repr__(self):
        return f"<Tenant {self.name} ({self.status.name})>"
