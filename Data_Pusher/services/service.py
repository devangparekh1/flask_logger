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
                "user_id": data["user_id"],
                "message": data["message"],
                "counter": int(r.get(data["user_id"])),
                "random_number": random.randint(1, 100),
            }
            requests.post("http://127.0.0.1:3000/api/validate", json=payload)

            pass

        except Exception as e:
            print(e)
