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
        try:

            if data["random_number"] % 10 == 0 and data["count"] == 0:

                data["category"] = "Retried"
                data["random_number"] = random.randint(1, 100)
                data["count"] = 1

                send_data(data)
                time.sleep(4)  # Halt the execution for the 4 seconds
                self.push_to_es(data)

            elif data["random_number"] % 10 == 0 and data["count"] == 1:
                data["category"] = "Failed"

            else:
                data["category"] = "Direct"

            return send_data(data)
        except Exception as e:
            print(e)
            return False


def send_data(data_to_send):
    today = date.today()
    try:
        del data_to_send["count"]
        del data_to_send["random_number"]
        data_to_send["created_at"] = today.strftime("%Y-%m-%d")
        new_data_to_send = {"message": data_to_send}
        requests.post("http://127.0.0.1:4000/api/messages", json=new_data_to_send)
        return True
    except Exception as e:
        print(e)
        return False
