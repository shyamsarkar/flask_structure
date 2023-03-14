# def test_register_user(client):
#     data = {'email': 'test@example.com', 'password': 'password'}
#     response = client.post('/auth/register', json=data)
#     assert response.status_code == 201

# def test_login_user(client, user):
#     data = {'email': user.email, 'password': 'password'}
#     response = client.post('/auth/login', json=data)
#     assert response.status_code == 200
#     assert response.json['access_token'] is not None

# import json

# def test_login(client):
#     data = {
#         'username': 'testuser',
#         'password': 'testpass'
#     }
#     response = client.post('/api/auth/login', data=json.dumps(data), content_type='application/json')
#     assert response.status_code == 200
#     assert 'access_token' in response.json

# def test_register(client):
#     data = {
#         'username': 'newuser',
#         'password': 'newpass'
#     }
#     response = client.post('/api/auth/register', data=json.dumps(data), content_type='application/json')
#     assert response.status_code == 201
