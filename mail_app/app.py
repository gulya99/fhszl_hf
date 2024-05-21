from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'gulyi.geri@gmail.com'  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = 'Nagysztgergely'     # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def index():
    msg = Message(
        subject='Hello from the other side!', 
        sender='gulyi.geri@gmail.com',  # Ensure this matches MAIL_USERNAME
        recipients=['gugerobo@gmail.com']  # Replace with actual recipient's email
    )
    msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)