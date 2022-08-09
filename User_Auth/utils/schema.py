LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}

REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 5, "maxLength": 15},
        "email": {"type": "string"},
        "password": {"type": "string", "minLength": 6, "maxLength": 12},
    },
    "required": ["name", "email", "password"],
}
