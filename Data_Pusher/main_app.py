from flask import Flask, request
from flask_expects_json import expects_json
from utils.schema import MESSAGE_SCHEMA
from middlewares.middlewares import token_required

app = Flask(__name__)


@app.route("/", methods=["POST"])
@token_required
@expects_json(MESSAGE_SCHEMA)
def index(auth_user):
    print(auth_user["user_id"])
    data = request.get_json()
    print(data["message"])
    return {"id": auth_user["user_id"], "message": data["message"]}, 200
