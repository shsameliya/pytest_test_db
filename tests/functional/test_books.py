# import pytest

# def test_create_book(test_client, init_database):
#     response = test_client.post('/api/books', json={'title': 'New Book', 'author': 'New Author'})
#     assert response.status_code == 201
#     assert response.json['message'] == 'Book created successfully'

# def test_get_all_books(test_client, init_database):
#     response = test_client.get('/api/books/')
#     assert response.status_code == 200
#     assert len(response.json) == 2  # Assuming two books were added in init_database fixture

# def test_get_book(test_client, init_database):
#     book_id = 1  # Assuming book ID 1 exists in the database
#     response = test_client.get(f'/api/books/{book_id}')
#     assert response.status_code == 200
#     assert response.json['id'] == book_id

# def test_update_book(test_client, init_database):
#     book_id = 1  # Assuming book ID 1 exists in the database
#     response = test_client.put(f'/api/books/{book_id}', json={'title': 'Updated Book', 'author': 'Updated Author'})
#     assert response.status_code == 200
#     assert response.json['message'] == 'Book updated successfully'

# def test_delete_book(test_client, init_database):
#     book_id = 1  # Assuming book ID 1 exists in the database
#     response = test_client.delete(f'/api/books/{book_id}')
#     assert response.status_code == 200
#     assert response.json['message'] == 'Book deleted successfully'
