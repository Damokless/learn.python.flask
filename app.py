from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/cars")
def getCars():
    return "<p>Hello, cars!</p>"

@app.route("/api/cars/<id>")
def getCarsByID(id):
    return "<p>Hello, cars id!</p>"

@app.route("/api/order")
def orders():
    return "<p>Hello, orders!</p>"