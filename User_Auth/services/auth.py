from models.user import users, db
from flask import jsonify
from passlib.hash import pbkdf2_sha256
import json
import jwt
import os


class AuthService:
    def login(self, data):
        user = users.query.filter_by(email=data["email"]).first()
        if not user:
            return "User not found"

        if not pbkdf2_sha256.verify(data["password"], user.password):
            return "Invalid password"

        token = jwt.encode(
            {"user_id": user.id, "email": data["email"]},
            os.environ.get("SECRET_KEY"),
            algorithm=os.environ.get("HASH_ALGORITHM"),
        )
        return token

    def register(self, data):
        user = users.query.filter_by(email=data["email"]).first()

        if user:
            return {"message": "User already exists"}, 409

        user = users(
            name=data["name"],
            email=data["email"],
            password=pbkdf2_sha256.encrypt(data["password"], rounds=2, salt_size=5),
        )
        db.session.add(user)
        db.session.commit()
        return {"ok": True}
