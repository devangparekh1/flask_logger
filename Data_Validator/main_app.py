from flask import Flask, request
from flask_expects_json import expects_json
from utils.schema import PAYLOAD_SCHEMA

app = Flask(__name__)


@app.route("/api/validate", methods=["POST"])
@expects_json(PAYLOAD_SCHEMA)
def index():
    try:
        request_data = request.get_json()
        print("Request Data", request_data)
        return {"status": "success"}
    except Exception as e:
        return {"message": "Something went wrong", "error": str(e)}, 500
