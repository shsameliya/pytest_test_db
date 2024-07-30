import os
import warnings

import pytest

from project import create_app, db
from project.models import Book, User


@pytest.fixture(autouse=True)
def ignore_sqlalchemy_deprecations():
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", category=DeprecationWarning, module="sqlalchemy"
        )
        yield


# --------
# Fixtures
# --------


@pytest.fixture(scope="module")
def new_user():
    user = User("user@gmail.com", "Password")
    return user


@pytest.fixture(scope="module")
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope="module")
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    default_user = User(email="user@gmail.com", password="Password")
    second_user = User(email="user@yahoo.com", password="BestPassword")
    db.session.add(default_user)
    db.session.add(second_user)

    # Commit the changes for the users
    db.session.commit()

    # Insert book data
    book1 = Book(title="Sub", author="harshal")
    book2 = Book(title="Love is Back", author="Shobhit")
    book3 = Book(title="Books", author="Rishabh")
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    # Commit the changes for the books
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


# @pytest.fixture(scope="function")
# def log_in_default_user(test_client):
#     test_client.post("/login", data={"email": "user@gmail.com", "password": "Password"})

#     yield  # this is where the testing happens!

#     test_client.get("/logout")


# @pytest.fixture(scope="function")
# def log_in_second_user(test_client):
#     test_client.post(
#         "login", data={"email": "user@yahoo.com", "password": "BestPassword"}
#     )

#     yield  # this is where the testing happens!

#     # Log out the user
#     test_client.get("/logout")


# Test database create function
@pytest.fixture(scope="module")
def cli_test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    flask_app = create_app()

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!
