from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from project import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    email = mapped_column(String(255), unique=True, nullable=False)
    password = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"<User: {self.email}>"


class Book(db.Model):
    __tablename__ = "books"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    title = mapped_column(String(255))
    author = mapped_column(String(255))

    def __repr__(self):
        return f"<Book: {self.title}>"
