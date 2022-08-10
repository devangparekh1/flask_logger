from flask import Flask, request
from flask_expects_json import expects_json
from utils.schema import PAYLOAD_SCHEMA

app = Flask(__name__)

from services.service import ValidateService

validateService = ValidateService()


@app.route("/api/validate", methods=["POST"])
@expects_json(PAYLOAD_SCHEMA)
def index():
    try:

        request_data = request.get_json()
        request_data["count"] = 0

        response = validateService.push_to_es(request_data)
        message = "Message Pushed Successfully" if response else "Message Not Pushed"

        return {"status": response, "message": message}

    except Exception as e:
        return {"message": "Something went wrong", "error": str(e)}, 500
