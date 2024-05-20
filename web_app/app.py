from flask import Flask, render_template, request
import os
import cv2
import time
import requests
import threading

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

def detect(image):
    car_cascade = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.realpath(__file__)), "car_haarcascade.xml"))
    cars = car_cascade.detectMultiScale(image)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return len(cars)

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
    quantity = 0
    quantity = detect(image)
    return render_template("image.html", title=tag, image=image, quantity=quantity)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
