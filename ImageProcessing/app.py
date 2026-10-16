import pika
import cv2
import numpy as np

def load_image(buffer: bytes):
    print("Loading image....")
    nparr = np.frombuffer(buffer, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img_np is None:
        print("Reading Image Failed!")
        return

    print("Successfully read image!")


def main():
    credentials = pika.PlainCredentials("admin", "secure_password")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue='images', durable=True)

    print("Waiting for images...")

    for method_frame, properties, body in channel.consume('images'):
        load_image(body)

        # Acknowledge the message
        channel.basic_ack(method_frame.delivery_tag)

if __name__ == "__main__":
    main()