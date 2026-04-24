from app.models.task_model import Task
from app.extensions import db

def create_task(data):
    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    return {"message": "Task created"}

def get_tasks():
    tasks = Task.query.all()
    return [{"id": t.id, "title": t.title} for t in tasks]

def update_task(id, data):
    task = Task.query.get(id)
    task.title = data.get("title", task.title)
    db.session.commit()
    return {"message": "Updated"}

def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return {"message": "Deleted"}

def toggle_status(id):
    task = Task.query.get(id)
    task.status = "completed" if task.status == "pending" else "pending"
    db.session.commit()

def archive_task(id):
    task = Task.query.get(id)
    task.is_archived = True
    db.session.commit()