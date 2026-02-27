def test_index_status(client):
    print(
        "===============================Running Pytest======================================"
    )
    response = client.get("/")
    assert response.status_code == 404


def test_api_index(client):
    response = client.get("api/")
    assert response.status_code == 200
    # breakpoint()
    assert b"Inside API Home" in response.data
