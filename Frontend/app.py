from flask import Flask
import pika

app = Flask(__name__)

credentials = pika.PlainCredentials("admin", "secure_password")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672, credentials=credentials))
channel = connection.channel()

@app.route("/")
def hello():
    return f"Hello from Docker!\n"