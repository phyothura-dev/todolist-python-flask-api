from app.models.task_model import Task
from app.extensions import db
from flask_jwt_extended import get_jwt_identity

def _current_user_id():
    identity = get_jwt_identity()
    try:
        return int(identity)
    except (TypeError, ValueError):
        return None

def create_task(data):
    if not data or not data.get("title"):
        return {"message": "title is required"}, 400
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401

    task = Task(title=data["title"], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return {"message": "Task created"}

def get_tasks():
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401
    tasks = Task.query.filter_by(user_id=user_id, is_archived=False).all()
    return [{"id": t.id, "title": t.title, "status": t.status} for t in tasks]

def update_task(id, data):
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return {"message": "Task not found"}, 404

    task.title = data.get("title", task.title)
    db.session.commit()
    return {"message": "Updated"}

def delete_task(id):
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return {"message": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "Deleted"}

def toggle_status(id):
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return {"message": "Task not found"}, 404

    task.status = "completed" if task.status == "pending" else "pending"
    db.session.commit()
    return {"message": "Status updated", "status": task.status}

def archive_task(id):
    user_id = _current_user_id()
    if user_id is None:
        return {"message": "Invalid token subject"}, 401
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return {"message": "Task not found"}, 404

    task.is_archived = True
    db.session.commit()
    return {"message": "Task archived"}