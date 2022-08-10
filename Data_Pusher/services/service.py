import redis
import random

r = redis.Redis(host="localhost", port=6379, db=0)


class PushService:
    def data_push(self, data):
        r.set(data["user_id"], 1) if not r.get(data["user_id"]) else r.incr(
            data["user_id"]
        )
        cache = r.get(data["user_id"])  # get user_id from redis
        random_number = random.randint(1, 10000)

        payload = {
            "user_id": data["user_id"],
            "message": data["message"],
            "cache": int(cache),
            "random_number": random_number,
        }

        