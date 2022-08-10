from flask import Flask, request
from flask_expects_json import expects_json
from utils.schema import MESSAGE_SCHEMA
from middlewares.middlewares import token_required

app = Flask(__name__)

from services.service import PushService

pushService = PushService()


@app.route("/", methods=["POST"])
@token_required
@expects_json(MESSAGE_SCHEMA)
def index(auth_user):
    try:
        request_data = request.get_json()
        data = {"user_id": auth_user["user_id"], "message": request_data["message"]}
        response = pushService.data_push(data)
        message = "success" if response else "fail"
        return {"message": message}, 200

    except Exception as e:
        return {"message": "Something went wrong", "error": str(e)}, 500
