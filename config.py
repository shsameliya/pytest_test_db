import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="BAD_SECRET_KEY")

    # # mysql
    # SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ROOT@127.0.0.1:5432/flask_db"

    # Postgres configuration
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:ROOT@db:5432/pytest_2_test"
    # MySQL configuration
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@db:3306/pytest_2_test"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_WITH_GUNICORN = os.getenv("LOG_WITH_GUNICORN", default=False)


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     "TEST_DATABASE_URI", default=os.getenv("TEST_MYSQL_DATABASE_URI")
    # )
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ROOT@127.0.0.1:5432/flask_test_db"

    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:ROOT@db_test:5432/pytest_2_pytest"

    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
