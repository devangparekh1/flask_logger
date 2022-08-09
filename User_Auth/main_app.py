from flask import Flask, request
from utils.schema import LOGIN_SCHEMA, REGISTER_SCHEMA
from flask_expects_json import expects_json

app = Flask(__name__)

from services.auth import AuthService

authService = AuthService()


@app.route("/api/login", methods=["POST"])
@expects_json(LOGIN_SCHEMA)
def login():
    try:
        request_data = request.get_json()
        result = authService.login(request_data)
        return {"ok": True, "data": result}
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500


@app.route("/api/register", methods=["POST"])
@expects_json(REGISTER_SCHEMA)
def register():
    try:
        request_data = request.get_json()
        authService.register(request_data)
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500
