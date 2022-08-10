from functools import wraps
import jwt
from flask import request, abort


def token_required(f):
    @wraps(f)
    def decorated():
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized",
            }, 401

        try:
            data = jwt.decode(
                token,
                os.environ.get("SECRET_KEY"),
                algorithms=[os.environ.get("HASH_ALGORITHM")],
            )

            if data is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized",
                }, 401

        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e),
            }, 500

        return f(data)

    return decorated
