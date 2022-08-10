import random
import requests
from flask import jsonify
import time


class ValidateService:
    def push_to_es(self, data):
        try:
            
            if data["random_number"] % 10 == 0 and data["count"] == 0:
                # Halt execution for 4 seconds.
                time.sleep(4)
                data["category"] = "Retried"
                data["random_number"] = random.randint(1, 100)
                data["count"] = 1
                self.push_to_es(data)

            if data["random_number"] % 10 == 0 and data["count"] == 1:
                data["category"] = "Failed"
                # Push the message to ES and return
                print(data)

            # Directly push the message to ES and return by category set to Direct
            print(data)

        except Exception as e:
            return {"message": "Something went wrong", "error": str(e)}, 500
