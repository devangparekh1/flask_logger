from main_app import app
import json
import pika
from flask import jsonify

from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])


class AppService:
    def get_messages(self):
        results = es.search(
            index="user_message_1",
            body={"size": 100, "query": {"regexp": {"message": ".*"}}},
        )
        return results["hits"]["hits"]

    def add_message(self, task):
        try:
            es.index(index="user_message_1", body=task)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})

    def upload_message_bulk(self, data):
        try:
            es.bulk(body=data)
            return jsonify({"status": "success"})
        except e:
            return jsonify({"status": "error", "message": str(e)})

    def get_messages_grouped(self):
        results = es.search(
            index="user_message_1",
            body={
                "size": 0,
                "aggs": {"category": {"terms": {"field": "category.keyword"}}},
            },
        )
        return results["aggregations"]["category"]["buckets"]

    # def publish_message_in_queue(self, cmd):
    #     channel.basic_publish(
    #         exchange='', routing_key='hello_world', body=json.dumps(cmd))
    #     return {'message': 'Message published'}
    #     connection.close()
