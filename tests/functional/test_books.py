# import pytest


def test_create_book(test_client, init_database):
    form_data = {"title": "New Book", "author": "New Author"}
    response = test_client.post("/books", data=form_data, follow_redirects=True)
    assert response.status_code == 201
    assert response.json["message"] == "Book created successfully"


def test_create_book_missing_author(test_client, init_database):
    form_data = {"title": "New Book"}
    response = test_client.post("/books", data=form_data, follow_redirects=True)
    assert response.status_code == 400
    assert response.json["message"] == "Title and author are required fields"


def test_create_book_missing_title(test_client, init_database):
    form_data = {"author": "New Author"}
    response = test_client.post("/books", data=form_data, follow_redirects=True)
    assert response.status_code == 400
    assert response.json["message"] == "Title and author are required fields"


def test_get_all_books(test_client, init_database):
    response = test_client.get("/books/")
    assert response.status_code == 200
    assert (
        len(response.json) == 4
    )  # Assuming four books were added in init_database fixture


def test_get_book(test_client, init_database):
    book_id = 1  # Assuming book ID 1 exists in the database
    response = test_client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json["id"] == book_id


def test_update_book(test_client, init_database):
    book_id = 1  # Assuming book ID 1 exists in the database
    json = {"title": "Updated Book", "author": "Updated Author"}
    response = test_client.put(f"/books/{book_id}", data=json)
    assert response.status_code == 200
    assert response.json["message"] == "Book updated successfully"


def test_delete_book(test_client, init_database):
    book_id = 1  # Assuming book ID 1 exists in the database
    response = test_client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Book deleted successfully"
