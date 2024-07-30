import logging
import os
from logging.handlers import RotatingFileHandler

import sqlalchemy as sa
from click import echo
from dotenv import load_dotenv
from flask import Flask
from flask.logging import default_handler
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# -------------
# Configuration
# -------------


load_dotenv()
db = SQLAlchemy()
csrf_protection = CSRFProtect()
login = LoginManager()

login.login_view = "users.login"


# ----------------------------
# Application Factory Function
# ----------------------------


def create_app():
    app = Flask(__name__)
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)
    app.config["WTF_CSRF_ENABLED"] = False

    # logging.basicConfig(  # SET LOGGING IN PROJECT with log store in specific file
    #     filename="record.log",
    #     level=logging.DEBUG,
    #     format="%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]",
    # )
    logging.basicConfig(level=logging.DEBUG)  # SET LOGGING IN PROJECT

    initialize_extensions(app)
    register_blueprints(app)
    configure_logging(app)
    register_cli_commands(app)

    engine = sa.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    inspector = sa.inspect(engine)
    if not inspector.has_table("users"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info("Initialized the databtestdrivenase!")
    else:
        app.logger.info("Database already contains the users table.")
    return app


# ----------------
# Helper Functions
# ----------------


def initialize_extensions(app):
    db.init_app(app)
    csrf_protection.init_app(app)
    login.init_app(app)

    from project.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    from project.books import books_blueprint
    from project.users import users_blueprint

    app.register_blueprint(books_blueprint)
    app.register_blueprint(users_blueprint)


# this function manage all logging details
def configure_logging(app):
    # TODO need to explore this functaion
    if app.config["LOG_WITH_GUNICORN"]:
        gunicorn_error_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler(
            "instance/flask-user-management.log", maxBytes=16384, backupCount=20
        )
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]"
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.removeHandler(default_handler)
    app.logger.info("Starting the Flask User Management App...")


def register_cli_commands(app):
    @app.cli.command("init_db")
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo("Initialized the database!")
