from flask import Blueprint, request
from flasgger import swag_from
from app.services.auth_service import register_user, login_user
from app.response import success, fail
from app.docs.auth_docs import REGISTER_DOC, LOGIN_DOC

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
@swag_from(REGISTER_DOC)
def register():
    try:
        user = register_user(request.json)
        return success(user.to_dict(), "User created", 201)
    except Exception as error:
        return fail("Failed to register user", 500, str(error))

@auth_bp.route("/login", methods=["POST"])
@swag_from(LOGIN_DOC)
def login():
    try:
        result = login_user(request.json)
        return success({"token": result["token"], "user": result["user"]}, "User logged in successfully", 200)
    except Exception as error:
        return fail("Failed to login user", 500, str(error))
