import enum

from app.extensions.db import db

from .base import BaseModel


class MembershipRole(enum.Enum):
    admin = 0
    manager = 1
    cashier = 2
    waiter = 3


class Membership(BaseModel):
    __tablename__ = "memberships"

    user_id = db.Column(db.String(40), db.ForeignKey("users.id"), nullable=False)
    tenant_id = db.Column(db.String(40), db.ForeignKey("tenants.id"), nullable=False)
    role = db.Column(db.Enum(MembershipRole), nullable=False)

    # uniqueness: { scope: :tenant_id } — one membership per user per tenant
    __table_args__ = (
        db.UniqueConstraint("user_id", "tenant_id", name="uq_membership_user_tenant"),
    )

    # belongs_to :user
    user = db.relationship("User", back_populates="memberships")

    # belongs_to :tenant
    tenant = db.relationship("Tenant", back_populates="memberships")

    # --- role helpers ---
    def is_admin(self) -> bool:
        return self.role == MembershipRole.admin

    def is_manager(self) -> bool:
        return self.role == MembershipRole.manager

    def is_cashier(self) -> bool:
        return self.role == MembershipRole.cashier

    def is_waiter(self) -> bool:
        return self.role == MembershipRole.waiter

    def __repr__(self):
        return f"<Membership user={self.user_id} tenant={self.tenant_id} role={self.role.name}>"
