from flask import Flask, request
from flask_mail import Mail, Message
import redis

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.fhszlhf.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'eh9jtc@fhszlhf.com'
app.config['MAIL_PASSWORD'] = 'secretpassword'

mail = Mail(app)

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/enqueue', methods=['POST'])
def enqueue_message():
    email = request.form.get('email')
    if email:
        redis_client.rpush('emails', email)
        return 'Email enqueued successfully'
    else:
        return 'No email provided'

@app.route('/send_emails')
def send_emails():
    while True:
        email = redis_client.lpop('emails')
        if email:
            send_email(email)
        else:
            return 'No emails in the queue'

def send_email(email):
    msg = Message(subject="Hello",
                  sender="your-email@example.com",
                  recipients=[email])
    msg.body = "This is a test email."
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
