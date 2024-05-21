from flask import Flask
import pika

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"

@app.route("/")
def recive():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        app.logging.info("Failed to connect to RabbitMQ service. Message wont be sent.")
        return "NOT OK"

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        app.logging.info(" Received %s" % body.decode())
        app.logging.info(" Done")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    app.logging.info("Start consuming")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)