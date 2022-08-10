MESSAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "message": {"type": "string", "minLength": 1, "maxLength": 255},
    },
    "required": ["message"],
}
