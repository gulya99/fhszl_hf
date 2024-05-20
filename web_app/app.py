from flask import Flask, render_template, request
import os
import time
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods=["GET","POST"])
def upload():
    tag = request.form.get("tag")
    image = request.files.get("image")
    render_template("upload.html")
    time.sleep(10)
    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
