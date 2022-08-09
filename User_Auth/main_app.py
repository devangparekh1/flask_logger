from flask import Flask

app = Flask(__name__)

from services.auth import AuthService

authService = AuthService()


@app.route("/api/users")
def tasks():
    return {"users": authService.get_users()}
