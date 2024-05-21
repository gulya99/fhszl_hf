from flask import Flask
from flask_socketio import SocketIO, emit
import pika
import threading

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

def callback(ch, method, properties, body):
    # Wjem a ,essage os receoved, emit it to the WebSocket
    socketio.emit('message', {'data': body.decode()})

def start_consuming():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        app.logger.info("Failed to connect to RabbitMQ service. Message wont be sent.")

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        app.logger.info(" Received %s" % body.decode())
        app.logger.info(" Done")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    app.logger.info("Start consuming")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

threading.Thread(target=start_consuming).start()

@app.route("/health")
def health():
    return "OK"

@app.route("/admin")
def admin():
    return render_template('admin.html')
    
    
@socketio.on('connect')
def test_connect():
    emit('message', {'data': 'Connected'})

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=6000, debug=True, allow_unsafe_werkzeug=True)
#    app.run(host="0.0.0.0", port=6000, debug=True)