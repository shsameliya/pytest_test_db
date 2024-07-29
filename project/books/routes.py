from flask import abort, jsonify, request

from project import db
from project.models import Book

from . import books_blueprint


# CREATE operation
@books_blueprint.route("/", methods=["POST"])
def create_book():
    try:
        title = request.form.get("title")
        author = request.form.get("author")
        if not title or not author:
            return jsonify({"message": "Title and author are required fields"}), 400

        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()

        return (
            jsonify({"message": "Book created successfully", "book_id": new_book.id}),
            201,
        )
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})


# READ operation (Get all books)
@books_blueprint.route("/", methods=["GET"])
def get_all_books():
    try:
        books = Book.query.all()
        books_data = [
            {"id": book.id, "title": book.title, "author": book.author}
            for book in books
        ]
        return jsonify(books_data)
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})


# READ operation (Get single book by id)
@books_blueprint.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        # book = Book.query.get_or_404(book_id)
        book = db.session.get(Book, book_id)
        return jsonify({"id": book.id, "title": book.title, "author": book.author})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})


# UPDATE operation
@books_blueprint.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        # book = Book.query.get_or_404(book_id)
        book = db.session.get(Book, book_id)
        title = request.form.get("title")
        author = request.form.get("author")
        book.title = title
        book.author = author
        db.session.commit()
        return jsonify({"message": "Book updated successfully", "book_id": book.id})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})


# DELETE operation
@books_blueprint.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        # book = Book.query.get_or_404(book_id)
        book = db.session.get(Book, book_id)
        # print("book -- ", book)
        if book is None:
            # abort(404)
            return jsonify({"message": "Book Not found", "book_id": book_id}), 404
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully", "book_id": book_id})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})
