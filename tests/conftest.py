import pytest
from app import create_app
from app.extensions import db
import os
import pdb
from flask_migrate import upgrade


@pytest.fixture()
def test_app():
    app = create_app('config.TestingConfig')
    with app.app_context():
        upgrade()
    yield app
    # with app.app_context():
    print("=================Dropping Database Table============")
    # db.session.remove()
    # db.drop_all()


@pytest.fixture()
def client(test_app):
    return test_app.test_client()


@pytest.fixture()
def runner(test_app):
    return test_app.test_cli_runner()






# @pytest.fixture(scope='module')
# def post(user):
#     post = Post(title='test', content='test', user=user)
#     db.session.add(post)
#     db.session.commit()
#     return post

# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.id

# def create_token(user_id):
#     return jwt.create_access_token(identity=user_id)


# @pytest.fixture
# def app():
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.session.remove()
#         db.drop_all()

# @pytest.fixture
# def access_token(client):
#     data = {
#         'username': 'testuser',
#         'password': 'testpass'
#     }
#     response = client.post('/api/auth/login', json=data)
#     return response.json['access_token']
