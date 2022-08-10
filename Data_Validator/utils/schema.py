PAYLOAD_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "message": {"type": "string", "minLength": 1, "maxLength": 255},
        "request_count": {"type": "integer"},
        "random_number": {"type": "integer"},
    },
    "required": ["id", "message", "request_count", "random_number"],
}
