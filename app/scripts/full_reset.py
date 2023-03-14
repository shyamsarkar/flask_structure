from app.extensions import custom_cli
from flask_migrate import upgrade
from app.models import Role, User
from app.extensions import fake
import uuid
from app.extensions import db
import random

def create_roles():
    print("===== Creating Roles =====")
    Role.query.delete()
    for _ in range(5):
        role = Role(id=uuid.uuid4(), name=fake.name())
        role.save()
    # print(Role.query.all())
    print("===== Roles Created Successfully! =====")

def create_users():
    print("===== Creating Users =====")
    User.query.delete()
    # role = Role.query.limit(1)
    for _ in range(1, 20):
        user = User(id=uuid.uuid4(),email=fake.unique.first_name()+f"{_}@example.com", password=fake.random_int())
        user.save()
    # print(fake.zipcode(), fake.random_int())
    print("===== Users created Succefully! =====")



@custom_cli.command('full_reset')
def full_reset():
    print("===== Running Full Reset! =====")
    create_roles()
    create_users()
    # print("============Droping Database ================")
    # with create_app().app_context():
    # db.drop_all()

    # upgrade()
    # print("============Upgrading Done================")
