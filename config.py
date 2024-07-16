import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="BAD_SECRET_KEY")
    # postgresql
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ROOT@127.0.0.1:5432/test_erp"
    # mysql
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1/pytest_2_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_WITH_GUNICORN = os.getenv("LOG_WITH_GUNICORN", default=False)


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URI", default="mysql+pymysql://root@127.0.0.1/pytest_2_pytest"
    )
    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
