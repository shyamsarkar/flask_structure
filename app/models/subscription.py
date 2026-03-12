from datetime import datetime

from app.extensions.db import db

from .base import BaseModel


class SubscriptionPlan(BaseModel):
    __tablename__ = "subscription_plans"

    name = db.Column(db.String(50), unique=True, nullable=False)
    price_inr = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=True)

    subscriptions = db.relationship("Subscription", back_populates="plan")

    def __repr__(self):
        return f"<SubscriptionPlan {self.name} Rs.{self.price_inr}>"


class Subscription(BaseModel):
    __tablename__ = "subscriptions"

    user_id = db.Column(db.String(40), db.ForeignKey("users.id"), nullable=False)
    plan_id = db.Column(
        db.String(40), db.ForeignKey("subscription_plans.id"), nullable=False
    )
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    user = db.relationship("User")
    plan = db.relationship("SubscriptionPlan", back_populates="subscriptions")

    def __repr__(self):
        return f"<Subscription user={self.user_id} plan={self.plan_id} active={self.active}>"
