from flask import Blueprint

books_blueprint = Blueprint(
    "books", __name__, url_prefix="/books", template_folder="templates"
)

from . import routes
