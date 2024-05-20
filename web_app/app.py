from flask import Flask, render_template, request
import os
import cv2
import time
import requests
import threading

web_app = Flask(__name__)
web_app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

def detect():
    car_cascade = cv2.CascadeClassifier("car_haarcascade.xml")

@web_app.route("/health")
def health():
    return "OK"

@web_app.route("/")
def home():
    return render_template("index.html")

@web_app.route('/upload', methods=["GET","POST"])
def upload():
    tag = request.form.get("tag")
    image = request.files.get("image")
    image.save(os.path.join(web_app.config["UPLOAD_FOLDER"], image.filename))
    return render_template("image.html", title=tag, image=image.filename)

if __name__ == '__main__':
    web_app.run(host="0.0.0.0", port=5000, debug=True)
