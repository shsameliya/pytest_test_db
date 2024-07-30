import logging

from flask import (current_app, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user

# from app_name import app
from project import db
from project.models import User
from project.users.forms import LoginForm, RegisterForm

from . import users_blueprint


# CREATE operation
@users_blueprint.route("/", methods=["POST"])
def create_user():
    try:
        form = request.form
        # app.logger.debug("Received POST request to create a new user.")
        # app.logger.info("Received POST info")
        # app.logger.warning("Received POST warning")
        # print("email--", request.form.get("email"))
        # print("password--", request.form.get("password"))
        form = RegisterForm()
        if form.validate_on_submit():
            existing_user = User.query.filter_by(
                email=request.form.get("email")
            ).first()
            if existing_user:
                return (
                    jsonify(
                        {
                            "message": "This email is already registered",
                            "errors": {"email": ["Email already exists"]},
                        }
                    ),
                    409,
                )
            new_user = User(
                email=request.form.get("email"), password=request.form.get("password")
            )
            db.session.add(new_user)
            db.session.commit()

            return (
                jsonify(
                    {"message": "User created successfully", "user_id": new_user.id}
                ),
                201,
            )
        else:
            # app.logger.info("Starting the Flask User Management App...")
            return jsonify({"message": "User not", "errors": form.errors}), 401
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@users_blueprint.route("/login", methods=["POST"])
def login():
    try:
        form = LoginForm()
        if request.method == "POST" and form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.password == form.password.data:
                db.session.add(user)
                db.session.commit()
                return jsonify({"message": "User Login successfully"}), 200
            else:
                return jsonify({"message": "Invalid credentials"}), 401
        else:
            return jsonify({"message": "Invalid form data", "errors": form.errors}), 400
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


# READ operation (Get all users)
@users_blueprint.route("/", methods=["GET"])
def get_all_users():
    users = User.query.all()
    users_data = [{"id": user.id, "email": user.email} for user in users]
    return jsonify(users_data)


# READ operation (Get single user by id)
@users_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # user = User.query.get_or_404(user_id)
    user = db.session.get(User, user_id)
    return jsonify({"id": user.id, "email": user.email})


# UPDATE operation
@users_blueprint.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        # user = User.query.get_or_404(user_id)
        user = db.session.get(User, user_id)
        email = request.form.get("email")
        password = request.form.get("password")
        user.email = email
        user.password = password
        db.session.commit()
        return jsonify({"message": "User updated successfully", "user_id": user.id})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})


# DELETE operation
@users_blueprint.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        # user = User.query.get_or_404(user_id)
        user = db.session.get(User, user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully", "user_id": user.id})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})
