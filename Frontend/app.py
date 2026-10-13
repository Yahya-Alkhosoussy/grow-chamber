from flask import Flask
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Docker!\n"