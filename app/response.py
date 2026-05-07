from flask import jsonify


def success(data=None, message="Success", status_code=200):
    payload = {
        "status": "success",
        "message": message,
        "data": data,
    }
    return jsonify(payload), status_code


def fail(message="Error", status_code=500, errors=None):
    payload = {
        "status": "error",
        "message": message,
        "errors": errors,
    }
    return jsonify(payload), status_code
