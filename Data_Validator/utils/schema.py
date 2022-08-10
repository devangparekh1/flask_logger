PAYLOAD_SCHEMA = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "message": {"type": "string", "minLength": 1, "maxLength": 255},
        "counter": {"type": "integer"},
        "random_number": {"type": "integer"},
    },
    "required": ["user_id", "message", "counter", "random_number"],
}
