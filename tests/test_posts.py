from config import BASE_URL


def test_get_posts(api_client):
    response = api_client.get(
        f"{BASE_URL}/posts"
    )
    assert response.status_code == 200
    data = response.json()
    assert type(data) == list
    assert data != []

data = {
    "title" : "zbiel",
    "body" : "ykoun ghir mlih",
    "userId" : 1
}
def test_create_post(api_client):
    response = api_client.post(
        f"{BASE_URL}/posts",
         data
    )
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == data["title"]


new_data = {
    "title" : "zbiel",
    "body" : "ykoun ghir mlih_updated",
    "userId" : 1
}

 
def test_update_post(api_client):
    response = api_client.put(
        f"{BASE_URL}/posts/1",
         new_data
    )
    assert response.status_code == 200
    response_new_data = response.json()
    assert response_new_data["title"] == new_data["title"]


def test_delete_post(api_client):
    response = api_client.delete(
        f"{BASE_URL}/posts/1",
    )
    assert response.status_code == 200