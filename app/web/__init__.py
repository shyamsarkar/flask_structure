from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.extensions.db import db
from app.models.commission import CommissionRule, CommissionSettings
from app.models.subscription import Subscription, SubscriptionPlan
from app.tasks.commission import distribute_commissions

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
@login_required
def index():
    return render_template("dashboard.html")


@web_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@web_bp.route("/subscriptions")
@login_required
def subscriptions():
    plans = (
        SubscriptionPlan.query.filter_by(active=True)
        .order_by(SubscriptionPlan.price_inr.asc())
        .all()
    )
    if not plans:
        plans = _seed_default_plans()
    active_sub = current_user.active_subscription()
    return render_template(
        "subscriptions.html",
        plans=plans,
        active_sub=active_sub,
    )


@web_bp.route("/subscriptions/<plan_id>/subscribe", methods=["POST"])
@login_required
def subscribe(plan_id):
    plan = SubscriptionPlan.query.get_or_404(plan_id)

    Subscription.query.filter_by(user_id=current_user.id, active=True).update(
        {Subscription.active: False}
    )
    subscription = Subscription(user_id=current_user.id, plan_id=plan.id, active=True)
    db.session.add(subscription)
    db.session.commit()

    distribute_commissions.delay(subscription.id)
    flash("Subscription activated.", "success")
    return redirect(url_for("web.subscriptions"))


@web_bp.route("/admin/commissions", methods=["GET", "POST"])
@login_required
def commission_settings():
    settings = CommissionSettings.get_singleton()

    if request.method == "POST":
        try:
            max_levels = int(request.form.get("max_levels", settings.max_levels))
        except ValueError:
            max_levels = settings.max_levels

        settings.max_levels = max(1, max_levels)
        db.session.add(settings)

        for level in range(1, settings.max_levels + 1):
            rule = CommissionRule.query.filter_by(level=level).first()
            if not rule:
                rule = CommissionRule(level=level, percentage=0)
                db.session.add(rule)

            pct_value = request.form.get(f"level_{level}_percentage", "").strip()
            if pct_value:
                try:
                    rule.percentage = float(pct_value)
                except ValueError:
                    rule.percentage = 0
            rule.active = True

        CommissionRule.query.filter(CommissionRule.level > settings.max_levels).update(
            {CommissionRule.active: False}
        )

        db.session.commit()
        flash("Commission settings updated.", "success")
        return redirect(url_for("web.commission_settings"))

    rules = (
        CommissionRule.query.filter(CommissionRule.level <= settings.max_levels)
        .order_by(CommissionRule.level.asc())
        .all()
    )
    if not rules:
        for level in range(1, settings.max_levels + 1):
            db.session.add(CommissionRule(level=level, percentage=0, active=True))
        db.session.commit()
        rules = (
            CommissionRule.query.filter(CommissionRule.level <= settings.max_levels)
            .order_by(CommissionRule.level.asc())
            .all()
        )

    return render_template(
        "commission_settings.html",
        settings=settings,
        rules=rules,
    )


def _seed_default_plans():
    defaults = [
        ("silver", 100),
        ("gold", 200),
        ("platinum", 300),
        ("diamond", 500),
    ]
    plans = []
    for name, price in defaults:
        plan = SubscriptionPlan(name=name, price_inr=price, active=True)
        db.session.add(plan)
        plans.append(plan)
    db.session.commit()
    return plans


from app.web.auth import (
    auth_bp,  # noqa: E402
    views,  # noqa: E402, F401
)

web_bp.register_blueprint(auth_bp)
