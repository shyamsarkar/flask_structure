from app.models import User
import uuid
from app.extensions import fake

def test_index_status(client):
    print("===============================Running Pytest======================================")
    response = client.get("/")
    assert response.status_code==404

def test_api_index(client):
    response = client.get("api/")
    assert response.status_code==200
    # breakpoint()
    assert b"Inside API Home" in response.data

# def test_user_model():
#     for _ in range(1, 20):
#         user = User(id=uuid.uuid4(),email=fake.unique.first_name()+f"{_}@example.com", password=fake.random_int())
#         user.save()
#     assert 19 in User.query.all().count

# def test_create_user(client):
#     data = {
#         'username': 'testuser',
#         'password': 'testpass'
#     }
#     response = client.post('/api/users', json=data)
#     assert response.status_code == 201

# def test_get_user(client, access_token):
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = client.get('/api/users/current', headers=headers)
#     assert response.status_code == 200
#     assert 'username' in response.json
