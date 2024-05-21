from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='bulk.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'c66fd364d82023c0747ad61ee7c4920d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/health")
def health():
    return "OK"

@app.route("/send")
def index():
    msg = Message(
        subject='Hello from the other side!', 
        sender='gulyi.geri@gmail.com',
        recipients=['gugerobo@gmail.com']
    )
    msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)