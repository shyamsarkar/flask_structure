# from flask_jwt_extended import create_access_token, create_refresh_token

# def create_token(user):
#     access_token = create_access_token(identity=user.id)
#     refresh_token = create_refresh_token(identity=user.id)
#     return {'access_token': access_token, 'refresh_token': refresh_token}



# def test_get_all_posts(client):
#     response = client.get('/api/posts')
#     assert response.status_code == 200

# def test_get_post(client, post):
#     response = client.get(f'/api/posts/{post.id}')
#     assert response.status_code == 200

# def test_create_post(client, user):
#     token = create_token(user.id)
#     headers = {'Authorization': f'Bearer {token}'}
#     data = {'title': 'test', 'content': 'test'}
#     response = client.post('/api/posts', json=data, headers=headers)
#     assert response.status_code == 201

# def test_update_post(client, post, user):
#     token = create_token(user.id)
#     headers = {'Authorization': f'Bearer {token}'}
#     data = {'title': 'test2'}
#     response = client.patch(f'/api/posts/{post.id}', json=data, headers=headers)
#     assert response.status_code == 200

# def test_delete_post(client, post, user):
#     token = create_token(user.id)
#     headers = {'Authorization': f'Bearer {token}'}
#     response = client.delete(f'/api/posts/{post.id}', headers=headers)
#     assert response.status_code == 204
#     assert post.is_deleted

# def test_register_user(client):
#     data = {'email': 'test@example.com', 'password': 'password'}
#     response = client.post('/auth/register', json=data)
#     assert response.status_code == 201

# def test_login_user(client, user):
#     data = {'email': user.email, 'password': 'password'}
#     response = client.post('/auth/login', json=data)
#     assert response.status_code == 200
#     assert response.json['access_token'] is not None

