from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SubmitField
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'web_app/static/files'

@app.route("/health")
def health():
    return "OK"

@app.route('/detect', methods="POST")
def detect():
    image = requests.files.get('image')
    return image

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)
