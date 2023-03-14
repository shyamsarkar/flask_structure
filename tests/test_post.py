# def test_create_post(client, access_token):
#     data = {
#         'title': 'Test Post',
#         'content': 'This is a test post.'
#     }
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = client.post('/api/posts', json=data, headers=headers)
#     assert response.status_code == 201

# def test_get_all_posts(client):
#     response = client.get('/api/posts')
#     assert response.status_code == 200
#     assert len(response.json) > 0
