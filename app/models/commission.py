from app.extensions.db import db

from .base import BaseModel


class CommissionRule(BaseModel):
    __tablename__ = "commission_rules"

    level = db.Column(db.Integer, unique=True, nullable=False)
    percentage = db.Column(db.Numeric(6, 2), nullable=False, default=0)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<CommissionRule level={self.level} pct={self.percentage}>"


class CommissionPayout(BaseModel):
    __tablename__ = "commission_payouts"

    subscription_id = db.Column(
        db.String(40), db.ForeignKey("subscriptions.id"), nullable=False
    )
    from_user_id = db.Column(db.String(40), db.ForeignKey("users.id"), nullable=False)
    to_user_id = db.Column(db.String(40), db.ForeignKey("users.id"), nullable=False)

    level = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Numeric(6, 2), nullable=False)
    amount_inr = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), default="pending")

    def __repr__(self):
        return (
            f"<CommissionPayout sub={self.subscription_id} level={self.level} "
            f"amount={self.amount_inr} status={self.status}>"
        )
