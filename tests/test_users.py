from config import BASE_URL



def test_get_user(api_client):
    response =  api_client.get(
        f"{BASE_URL}/users/1"
     )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    


def test_user_not_found(api_client):
    response = api_client.get(
        f"{BASE_URL}/users/999"
    )
    assert response.status_code == 404


data = {
    "name" : "Amine",
    "username" : "Mr_Amineee",
    "email" : "mramin123@gmail.com"

}
def test_create_user(api_client):
    response = api_client.post(
        f"{BASE_URL}/users",
        data
    )
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == data["name"]

new_data = {
    "name" : "Amine_updated",
    "username" : "Mr_Amineee_updated",
    "email" : "mramin123@gmail.com_updated"

}
def test_update_user(api_client):
    response = api_client.put(
        f"{BASE_URL}/users/1",
        new_data 

    )
    assert response.status_code == 200
    response_new_data = response.json()
    assert response_new_data["name"] == new_data["name"]


def test_delete_user(api_client):
    response = api_client.delete(
        f"{BASE_URL}/users/1",
    )
    assert response.status_code == 200