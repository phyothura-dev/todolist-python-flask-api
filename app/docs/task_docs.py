CREATE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Create task",
    "security": [{"Bearer": []}],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "required": True,
            "type": "string",
            "default": "Bearer <token>",
        },
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["title"],
                "properties": {
                    "title": {"type": "string", "example": "Buy groceries"},
                },
            },
        },
    ],
    "responses": {
        201: {
            "description": "Task created",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "Task created"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "example": 1},
                            "title": {"type": "string", "example": "Buy groceries"},
                            "status": {"type": "string", "example": "pending"},
                        },
                    },
                },
            },
        },
        500: {"description": "Error response"},
    },
}

GET_TASKS_DOC = {
    "tags": ["Tasks"],
    "summary": "Get all active tasks",
    "security": [{"Bearer": []}],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "required": True,
            "type": "string",
            "default": "Bearer <token>",
        }
    ],
    "responses": {
        200: {
            "description": "Task list",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "Tasks fetched"},
                    "data": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "title": {"type": "string"},
                                "status": {"type": "string"},
                            },
                        },
                    },
                },
            },
        },
        500: {"description": "Error response"},
    },
}

UPDATE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Update task",
    "security": [{"Bearer": []}],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "required": True,
            "type": "string",
            "default": "Bearer <token>",
        },
        {
            "in": "path",
            "name": "id",
            "required": True,
            "type": "integer",
        },
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "example": "Updated task title"},
                },
            },
        },
    ],
    "responses": {
        200: {
            "description": "Updated",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "Updated"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "status": {"type": "string"},
                        },
                    },
                },
            },
        },
        500: {"description": "Error response"},
    },
}

DELETE_TASK_DOC = {
    "tags": ["Tasks"],
    "summary": "Delete task",
    "security": [{"Bearer": []}],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "required": True,
            "type": "string",
            "default": "Bearer <token>",
        },
        {
            "in": "path",
            "name": "id",
            "required": True,
            "type": "integer",
        },
    ],
    "responses": {
        200: {
            "description": "Deleted",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "Deleted"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "deleted": {"type": "boolean", "example": True},
                            "id": {"type": "integer", "example": 1},
                        },
                    },
                },
            },
        },
        500: {"description": "Error response"},
    },
}
