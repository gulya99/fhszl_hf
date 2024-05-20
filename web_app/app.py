from flask import Flask, render_template, request
import os
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
    
    request_tag = {"tag": tag}
    request_image = {"image": (image.filename, image.read())}
    response = requests.post("http://0.0.0.0:6000/detect", data=request_tag, files=request_image)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
