from flask import Flask, render_template, request
import os
import cv2
import time
import requests
import threading

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./images"

def detect():
    car_cascade = cv2.CascadeClassifier("car_haarcascade.xml")

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
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
    return render_template("image.html", title=tag, image=image.filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
