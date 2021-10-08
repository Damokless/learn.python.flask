from flask import Flask, jsonify
import json
app = Flask(__name__)

with open('./assets/cars.json') as cars:
  data = json.load(cars)

  @app.route("/")
  def hello_world():
    return "<p>Hello, World!</p>"
  
  @app.route("/api/cars")
  def getCars():
        return jsonify(data)

  @app.route("/api/cars/id/<int:id>")
  def getCarsByID(id):
      if id:
          return data[id]
      else:
          return "<p>No car with this id</p>"
