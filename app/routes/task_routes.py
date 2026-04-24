from flask import Blueprint, request
from app.services.task_service import *

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["POST"])
def create():
    return create_task(request.json)

@task_bp.route("/", methods=["GET"])
def get_all():
    return get_tasks()

@task_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return update_task(id, request.json)

@task_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return delete_task(id)