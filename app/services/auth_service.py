from flask_jwt_extended import create_access_token
from app.models.user_model import User
from app.extensions import db

def register_user(data):
    user = User(username=data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return {"message": "User created"}

def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        token = create_access_token(identity=user.id)
        return {"token": token}
    return {"message": "Invalid credentials"}, 401