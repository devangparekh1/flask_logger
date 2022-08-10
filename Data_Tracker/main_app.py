import json
import pandas as pd

from flask import Flask, request, jsonify

app = Flask(__name__)

from service import AppService

appService = AppService()


@app.route("/api/messages")
def tasks():
    return {"messages": appService.get_messages()}


@app.route("/api/messages", methods=["POST"])
def create_task():
    print("Received data")
    request_data = request.get_json()
    task = request_data["message"]
    print("Message added to ES", task)
    return appService.add_message(task)


@app.route("/api/upload", methods=["POST"])
def bulk_upload_message():
    bulk_upload_list = []
    data = pd.read_csv(filepath_or_buffer=request.files["file"], sep=",", header=0)
    for index, row in data.iterrows():
        bulk_upload_list.append({"index": {"_index": "user_message"}})
        bulk_upload_list.append(row.to_dict())
    return appService.upload_message_bulk(bulk_upload_list)


@app.route("/api/task/grouped")
def grouped_task():
    return {"result": appService.get_messages_grouped()}


# @app.route('/api/task/push', methods=['POST'])
# def push_to_queue():
#     request_data = request.get_json()
#     task = request_data['task']
#     return appService.publish_message_in_queue(task)
