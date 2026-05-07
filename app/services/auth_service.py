from flask_jwt_extended import create_access_token
from app.models.user_model import User
from app.extensions import db

def register_user(data):
    if not data:
        raise ValueError("Missing request body")

    username = data.get("username")
    password = data.get("password")
    password_confirm = data.get("password_confirm")

    if not username or not password or not password_confirm:
        raise ValueError("username, password and password_confirm are required")


    if password != password_confirm:
        raise ValueError("password and password_confirm do not match")
       
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        raise FileExistsError("Username already exists")

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def login_user(data):
    if not data:
        raise ValueError("Missing request body")

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise ValueError("username and password are required")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_access_token(identity=str(user.id))
        return {"token": token, "user": user.to_dict()}
    raise PermissionError("Invalid credentials")