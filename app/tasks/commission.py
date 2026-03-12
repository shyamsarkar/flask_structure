from decimal import Decimal

from app.extensions.celery import celery_app
from app.extensions.db import db
from app.models.commission import CommissionPayout, CommissionRule, CommissionSettings
from app.models.subscription import Subscription


@celery_app.task
def distribute_commissions(subscription_id: str):
    subscription = Subscription.query.get(subscription_id)
    if not subscription or not subscription.active:
        return

    subscriber = subscription.user
    settings = CommissionSettings.get_singleton()
    rules = {
        rule.level: rule
        for rule in CommissionRule.query.filter_by(active=True).all()
    }

    amount = Decimal(subscription.plan.price_inr)
    level = 1
    current = subscriber.referred_by

    while current and level <= settings.max_levels:
        rule = rules.get(level)
        if rule and Decimal(rule.percentage) > 0:
            if current.has_active_subscription():
                pct = Decimal(rule.percentage) / Decimal(100)
                commission_amount = (amount * pct).quantize(Decimal("0.01"))
                if commission_amount > 0:
                    payout = CommissionPayout(
                        subscription_id=subscription.id,
                        from_user_id=subscriber.id,
                        to_user_id=current.id,
                        level=level,
                        percentage=rule.percentage,
                        amount_inr=commission_amount,
                        status="pending",
                    )
                    db.session.add(payout)

        current = current.referred_by
        level += 1

    db.session.commit()
