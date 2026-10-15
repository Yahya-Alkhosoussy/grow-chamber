import pika
import cv2 as cv
import numpy as np

def load_image(buffer: bytes):
    print("Loading image....")
    nparr = np.frombuffer(buffer, np.uint8)
    img_np = cv.fromarray(nparr)

    print(f"Idk Something: {nparr}")
    print(f"Idk Something2: {img_np}")


def main():
    print("Hello, World!")
    credentials = pika.PlainCredentials("admin", "secure_password")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue='images', durable=True)

    print("Waiting for images...")

    for method_frame, properties, body in channel.consume('images'):

        # Display the message parts
        print(method_frame)
        print(properties)
        print(len(body))
        load_image(body)

        # Acknowledge the message
        channel.basic_ack(method_frame.delivery_tag)

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == 10:
            break

if __name__ == "__main__":
    main()