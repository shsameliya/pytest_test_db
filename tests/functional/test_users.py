# from conftest import test_test_client as test_client


def test_create_user(test_client, init_database):
    form_data = {"email": "newuser@example.com", "password": "newpassword"}
    response = test_client.post("/api/users/", data=form_data)
    assert response.status_code == 201
    assert response.json["message"] == "User created successfully"


def test_get_all_users(test_client, init_database):
    response = test_client.get("/api/users/")
    assert response.status_code == 200
    assert len(response.json) == 3  # 3 set data in User table


def test_get_user(test_client, init_database):
    user_id = 1  # Assuming user ID 1 exists in the database
    response = test_client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json["id"] == user_id


def test_update_user(test_client, init_database):
    user_id = 1  # Assuming user ID 1 exists in the database
    form_data = {"email": "update@example.com", "password": "newpassword"}
    response = test_client.put(f"/api/users/{user_id}", data=form_data)
    assert response.status_code == 200
    assert response.json["message"] == "User updated successfully"


def test_delete_user(test_client, init_database):
    user_id = 1  # Assuming user ID 1 exists in the database
    response = test_client.delete(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json["message"] == "User deleted successfully"
