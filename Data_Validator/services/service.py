import random
import requests
from flask import jsonify
from datetime import date
import time

# {
#     "message": {
#         "message": "",
#         "request_count": 10,
#         "category": "Failed",
#         "created_at": "2022-08-08"
#     }
# }


class ValidateService:
    def push_to_es(self, data):
        today = date.today()
        try:

            if data["random_number"] % 10 == 0 and data["count"] == 0:
                # Halt execution for 4 seconds.
                time.sleep(4)
                data["category"] = "Retried"
                data["random_number"] = random.randint(1, 100)
                data["count"] = 1
                self.push_to_es(data)

            elif data["random_number"] % 10 == 0 and data["count"] == 1:
                data["category"] = "Failed"

            else:
                data["category"] = "Direct"

            del data["count"]
            del data["random_number"]
            data["created_at"] = today.strftime("%Y-%m-%d")
            new_data = {"message": data}
            requests.post("http://127.0.0.1:4000/api/messages", json=new_data)

        except Exception as e:
            print(e)
            return {"message": "Something went wrong", "error": str(e)}, 500
