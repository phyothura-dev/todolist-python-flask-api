from app.models.task_model import Task
from app.extensions import db
from flask_jwt_extended import get_jwt_identity

def _current_user_id():
    identity = get_jwt_identity()
    try:
        return int(identity)
    except Exception as error:
        raise ValueError("Invalid token subject")

def create_task(data):
    if not data or not data.get("title"):
        raise ValueError("title is required")
    user_id = _current_user_id()

    task = Task(title=data["title"], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return task

def get_tasks():
    user_id = _current_user_id()
    tasks = Task.query.filter_by(user_id=user_id, is_archived=False).all()
    return tasks

def update_task(id, data):
    user_id = _current_user_id()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        raise LookupError("Task not found")

    data = data or {}
    task.title = data.get("title", task.title)
    db.session.commit()
    return task

def delete_task(id):
    user_id = _current_user_id()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        raise LookupError("Task not found")

    db.session.delete(task)
    db.session.commit()
    return {"deleted": True, "id": id}

def toggle_status(id):
    user_id = _current_user_id()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        raise LookupError("Task not found")

    task.status = "completed" if task.status == "pending" else "pending"
    db.session.commit()
    return task

def archive_task(id):
    user_id = _current_user_id()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        raise LookupError("Task not found")

    task.is_archived = True
    db.session.commit()
    return task