from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.extensions.db import db
from app.models.commission import CommissionRule
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


@web_bp.route("/network")
@login_required
def network():
    return render_template("network.html")


@web_bp.route("/subscriptions")
@login_required
def subscriptions():
    if current_user.is_admin:
        flash("Administrators logically have an active subscription by default.", "info")
        return redirect(url_for("web.dashboard"))
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
    if current_user.is_admin:
        return redirect(url_for("web.dashboard"))
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
    if not current_user.is_admin:
        flash("Unauthorized access. Admin privileges required.", "danger")
        return redirect(url_for("web.dashboard"))
    if request.method == "POST":
        CommissionRule.query.delete()

        percentages = request.form.getlist("percentages")
        level = 1
        for pct_value in percentages:
            pct_value = (pct_value or "").strip()
            if not pct_value:
                continue
            try:
                pct = float(pct_value)
            except ValueError:
                pct = 0
            rule = CommissionRule(level=level, percentage=pct, active=True)
            db.session.add(rule)
            level += 1

        db.session.commit()
        flash("Commission settings updated.", "success")
        return redirect(url_for("web.commission_settings"))

    rules = (
        CommissionRule.query.order_by(CommissionRule.level.asc()).all()
    )

    return render_template(
        "commission_settings.html",
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
