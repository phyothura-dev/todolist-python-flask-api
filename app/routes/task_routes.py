from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.services.task_service import *

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    return create_task(request.json)

@task_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return get_tasks()

@task_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    return update_task(id, request.json)

@task_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return delete_task(id)