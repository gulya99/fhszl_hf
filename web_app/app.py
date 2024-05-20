from flask import Flask, render_template, request
import os
import cv2
import time
import requests
import threading

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

def detect(img_path):
    image = cv2.imread(img_path)
    car_cascade = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.realpath(__file__)), "haarcascade_car.xml"))
    cars = car_cascade.detectMultiScale(image)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    det_path = img_path.split(".")[0] + "_detected.jpg"
    cv2.imwrite(det_path, image)
    return len(cars), det_path

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
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
    image.save(img_path)
    quantity = 0
    quantity, det_path = detect(img_path)
    return render_template("image.html", title=tag, image=img_path, det_image=det_path, quantity=quantity)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
