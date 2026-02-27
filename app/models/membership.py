from app.extensions.db import db
from .base import BaseModel


class Membership(BaseModel):
    __tablename__ = "memberships"

    user_id = db.Column(db.String(40), db.ForeignKey("users.id"), nullable=False)
    tenant_id = db.Column(db.String(40), db.ForeignKey("tenants.id"), nullable=False)

    user = db.relationship("User", back_populates="memberships")
    tenant = db.relationship("Tenant", back_populates="memberships")

    def __repr__(self):
        return f"<Membership user={self.user_id} tenant={self.tenant_id}>"