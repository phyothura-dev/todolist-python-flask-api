REGISTER_DOC = {
    "tags": ["Auth"],
    "summary": "Register user",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["username", "password", "password_confirm"],
                "properties": {
                    "username": {"type": "string", "example": "demo"},
                    "password": {"type": "string", "example": "pass123"},
                    "password_confirm": {"type": "string", "example": "pass123"},
                },
            },
        }
    ],
    "responses": {
        201: {
            "description": "User created",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "User created"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "example": 1},
                            "username": {"type": "string", "example": "demo"},
                        },
                    },
                },
            },
        },
        500: {
            "description": "Error response",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "error"},
                    "message": {"type": "string", "example": "Failed to register user"},
                    "errors": {"type": "string", "example": "Username already exists"},
                },
            },
        },
    },
}

LOGIN_DOC = {
    "tags": ["Auth"],
    "summary": "Login and get JWT token",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["username", "password"],
                "properties": {
                    "username": {"type": "string", "example": "demo"},
                    "password": {"type": "string", "example": "pass123"},
                },
            },
        }
    ],
    "responses": {
        200: {
            "description": "User logged in successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "success"},
                    "message": {"type": "string", "example": "User logged in successfully"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "token": {"type": "string"},
                            "user": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer", "example": 1},
                                    "username": {"type": "string", "example": "demo"},
                                },
                            },
                        },
                    },
                },
            },
        },
        500: {
            "description": "Error response",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "error"},
                    "message": {"type": "string", "example": "Failed to login user"},
                    "errors": {"type": "string", "example": "Invalid credentials"},
                },
            },
        },
    },
}
