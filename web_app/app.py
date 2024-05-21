from flask import Flask, render_template, request
import os
import cv2
import csv
import time
import pika
import base64
import requests
import threading

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static/images")

def detect(filename):
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    image = cv2.imread(img_path)
    car_cascade = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.realpath(__file__)), "haarcascade_car.xml"))
    cars = car_cascade.detectMultiScale(image)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    det_filename = filename.split(".")[0] + "_detected.jpg"
    det_path = os.path.join(app.config["UPLOAD_FOLDER"], det_filename)
    cv2.imwrite(det_path, image)
    return len(cars), det_filename

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
    filename = image.filename
    img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    image.save(img_path)
    quantity = 0
    quantity, det_filename = detect(filename)
    db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db/db.csv")
    with open(db_path, mode="a", newline="") as db:
        writer = csv.writer(db)
        writer.writerow([tag, quantity, img_path, os.path.join(app.config["UPLOAD_FOLDER"], det_filename)])

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")

    channel = connection.channel()
    channel.queue_declare(queue='task_queue')
        
    with open(db_path, mode='r', newline="") as db:
        file_content = db.read()

    channel.basic_publish(exchange='', routing_key='task_queue', body=file_content)
    connection.close()
    
    return render_template("image.html", title=tag, image=filename, det_image=det_filename, quantity=quantity)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
