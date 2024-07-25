from flask import Blueprint

users_blueprint = Blueprint(
    "users", __name__, url_prefix="/api/users", template_folder="templates"
)

from . import routes
