import click
from flask.cli import AppGroup

from app.models.membership import Membership, MembershipRole
from app.models.referral import ReferralCodeSequence
from app.models.tenant import Tenant, TenantStatus
from app.models.user import User
from app.extensions.db import db

custom_cli = AppGroup("custom")

@custom_cli.command("reset-db")
def reset_db():
    db.drop_all()
    db.create_all()
    print("Database reset complete")


@custom_cli.command("create-root-user")
@click.option("--email", required=True, help="Root user email")
@click.option("--password", required=True, help="Root user password")
@click.option("--first-name", default="Root", show_default=True)
@click.option("--last-name", default="User", show_default=True)
@click.option("--tenant-name", default="Main", show_default=True)
def create_root_user(email, password, first_name, last_name, tenant_name):
    email = email.lower().strip()
    existing = User.query.filter_by(email=email).first()
    if existing:
        click.echo("User already exists.")
        return

    sequence = ReferralCodeSequence()
    db.session.add(sequence)
    db.session.flush()

    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        referral_code=f"MLM{sequence.id:04d}",
    )
    user.set_password(password)
    db.session.add(user)

    tenant = Tenant.query.filter_by(name=tenant_name).first()
    if not tenant:
        tenant = Tenant(name=tenant_name, status=TenantStatus.active)
        db.session.add(tenant)
        db.session.flush()

    membership = Membership(user_id=user.id, tenant_id=tenant.id, role=MembershipRole.admin)
    db.session.add(membership)

    db.session.commit()
    click.echo(f"Root user created with referral code {user.referral_code}")
