import redis
import random
import requests
from flask import jsonify

r = redis.Redis(host="localhost", port=6379, db=0)


class PushService:
    def data_push(self, data):
        try:
            r.set(data["user_id"], 1) if not r.get(data["user_id"]) else r.incr(
                data["user_id"]
            )

            payload = {
                "id": data["user_id"],
                "message": data["message"],
                "request_count": int(r.get(data["user_id"])),
                "random_number": random.randint(1, 100),
            }
            r = requests.post("http://127.0.0.1:3000/api/validate", json=payload)

            return True if r.status_code in [200, 201] else False

        except Exception as e:
            print(e)
            return False
