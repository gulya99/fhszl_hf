from flask import Flask, render_template, request
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/enqueue', methods=['POST'])
def enqueue_message():
    message = request.form.get('message')
    if message:
        redis_client.rpush('messages', message)
        return 'Message enqueued successfully'
    else:
        return 'No message provided'

"""@app.route('/dequeue')
def dequeue_message():
    message = redis_client.lpop('messages')
    if message:
        return f'Dequeued message: {message.decode("utf-8")}'
    else:
        return 'No messages in the queue'"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)
