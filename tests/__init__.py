print("===============================Running Pytest======================================")

# # tests/__init__.py

# import pytest
# from app import create_app
# from app.models import db, User, Post


# @pytest.fixture(scope='module')
# def test_app():
#     app = create_app('testing')
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.drop_all()


# @pytest.fixture(scope='function')
# def test_client(test_app):
#     return test_app.test_client()


# @pytest.fixture(scope='function')
# def test_db(test_app):
#     with test_app.app_context():
#         db.session.remove()
#         db.drop_all()
#         db.create_all()

#         # Add some test data
#         user1 = User(username='testuser1', email='testuser1@example.com', password='password1')
#         user2 = User(username='testuser2', email='testuser2@example.com', password='password2')
#         db.session.add(user1)
#         db.session.add(user2)
#         db.session.commit()

#         post1 = Post(title='Test Post 1', content='This is the first test post.', author=user1)
#         post2 = Post(title='Test Post 2', content='This is the second test post.', author=user2)
#         db.session.add(post1)
#         db.session.add(post2)
#         db.session.commit()

#         yield db




# # Auth tests

# def test_register_new_user(test_client, test_db):
#     res = test_client.post('/auth/register', json={
#         'username': 'newuser',
#         'email': 'newuser@example.com',
#         'password': 'newpassword'
#     })
#     assert res.status_code == 201


# def test_login_existing_user(test_client, test_db):
#     res = test_client.post('/auth/login', json={
#         'email': 'testuser1@example.com',
#         'password': 'password1'
#     })
#     assert res.status_code == 200


# def test_login_nonexistent_user(test_client, test_db):
#     res = test_client.post('/auth/login', json={
#         'email': 'nonexistent@example.com',
#         'password': 'password1'
#     })
#     assert res.status_code == 401


# # Post tests

# def test_get_all_posts(test_client, test_db):
#     res = test_client.get('/api/posts')
#     assert res.status_code == 200
#     data = res.get_json()
#     assert len(data) == 2


# def test_create_new_post(test_client, test_db):
#     res = test_client.post('/api/posts', json={
#         'title': 'New Post',
#         'content': 'This is a new test post.'
#     })
#     assert res.status_code == 201
#     data = res.get_json()
#     assert data['title'] == 'New Post'
#     assert data['content'] == 'This is a new test post.'


# def test_update_existing_post(test_client, test_db):
#     res = test_client.put('/api/posts/1', json={
#         'title': 'Updated Post',
#         'content': 'This is an updated test post.'
#     })
#     assert res.status_code == 200
#     data = res.get_json()
#     assert data['title'] == 'Updated Post'
#     assert data['content'] == 'This is an updated test post.'


# def test_delete_existing_post(test_client, test_db):
#     res = test_client.delete('/api/posts/1')
#     assert res.status_code == 204
#     res = test_client.get('/api/posts/1')
#     assert res.status_code == 404
