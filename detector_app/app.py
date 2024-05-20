from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SubmitField
import os
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route('/', methods=["POST"])
def home():
    return "Hello, World!"

@app.route('/detect', methods=["POST"])
def detect():
    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)
