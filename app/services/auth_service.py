from flask_jwt_extended import create_access_token
from app.models.user_model import User
from app.extensions import db

def register_user(data):
    if not data:
        return {"message": "Missing request body"}, 400

    username = data.get("username")
    password = data.get("password")
    password_confirm = data.get("password_confirm")

    if not username or not password or not password_confirm:
        return {"message": "username, password and password_confirm are required"}, 400

    if password != password_confirm:
        return {"message": "password and password_confirm do not match"}, 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"message": "Username already exists"}, 409

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return {"message": "User created"}, 201

def login_user(data):
    if not data:
        return {"message": "Missing request body"}, 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return {"message": "username and password are required"}, 400

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        token = create_access_token(identity=str(user.id))
        return {"message": "User logged in successfully","token": token}, 200
    return {"message": "Invalid credentials"}, 401