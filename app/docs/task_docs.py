CREATE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Create task",
    "security": [{"Bearer": []}],
    "parameters": [
        {"in": "header", "name": "Authorization", "required": True, "type": "string", "default": "Bearer <token>"},
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["title"],
                "properties": {
                    "title": {"type": "string", "example": "Buy groceries"},
                    "content": {"type": "string", "example": "Milk, eggs, bread"},
                    "status": {"type": "string", "enum": ["High", "Mid", "Low"], "example": "Mid"},
                },
            },
        },
    ],
    "responses": {201: {"description": "Task created"}, 500: {"description": "Error response"}},
}

GET_TASKS_DOC = {
    "tags": ["Tasks"],
    "summary": "Get all active tasks",
    "security": [{"Bearer": []}],
    "parameters": [{"in": "header", "name": "Authorization", "required": True, "type": "string", "default": "Bearer <token>"}],
    "responses": {200: {"description": "Task list"}, 500: {"description": "Error response"}},
}

UPDATE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Update task",
    "security": [{"Bearer": []}],
    "parameters": [
        {"in": "header", "name": "Authorization", "required": True, "type": "string", "default": "Bearer <token>"},
        {"in": "path", "name": "id", "required": True, "type": "integer"},
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "example": "Updated task title"},
                    "content": {"type": "string", "example": "Updated task details"},
                    "status": {"type": "string", "enum": ["High", "Mid", "Low"], "example": "High"},
                },
            },
        },
    ],
    "responses": {200: {"description": "Updated"}, 500: {"description": "Error response"}},
}

DELETE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Delete task",
    "security": [{"Bearer": []}],
    "parameters": [
        {"in": "header", "name": "Authorization", "required": True, "type": "string", "default": "Bearer <token>"},
        {"in": "path", "name": "id", "required": True, "type": "integer"},
    ],
    "responses": {200: {"description": "Deleted"}, 500: {"description": "Error response"},},
}
