from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/detect', methods=["POST"])
def detect():
    if request.method == "POST":
        return "OK"
    else:
        return "Not OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)
