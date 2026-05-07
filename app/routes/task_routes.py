from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.services.task_service import create_task, get_tasks, update_task, delete_task
from app.response import success, fail
from app.docs.task_docs import CREATE_TASK_DOC,GET_TASKS_DOC,UPDATE_TASK_DOC,DELETE_TASK_DOC

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(CREATE_TASK_DOC)
def create():
    try:
        task = create_task(request.json)
        return success({"id": task.id, "title": task.title, "status": task.status},"Task created",201 )
    except Exception as error:
        return fail("Failed to create task", 500, str(error))

@task_bp.route("/", methods=["GET"])
@jwt_required()
@swag_from(GET_TASKS_DOC)
def get_all():
    try:
        tasks = get_tasks()
        data = [{"id": t.id, "title": t.title, "status": t.status} for t in tasks]
        return success(data, "Tasks fetched", 200)
    except Exception as error:
        return fail("Failed to fetch tasks", 500, str(error))

@task_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@swag_from(UPDATE_TASK_DOC)
def update(id):
    try:
        task = update_task(id, request.json)
        return success({"id": task.id, "title": task.title, "status": task.status},"Updated",200)
    except Exception as error:
        return fail("Failed to update task", 500, str(error))

@task_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@swag_from(DELETE_TASK_DOC)
def delete(id):
    try:
        result = delete_task(id)
        return success(result, "Deleted", 200)
    except Exception as error:
        return fail("Failed to delete task", 500, str(error))