from os import name
from flask import Flask, jsonify
import json
app = Flask(__name__)

with open('./assets/cars.json') as cars:
  data = json.load(cars)

  @app.route("/")
  def hello_world():
    return "<p>Hello, World!</p>"
  
  @app.route("/api/cars", methods=['GET'])
  def getCars():
    return jsonify(data)

  @app.route("/api/cars/id/<int:id>", methods=['GET'])
  def getCarsByID(id):
    return data[id]

  @app.route("/api/cars/delete/<int:id>", methods=['GET','DELETE'])
  def deleteCarsByID(id):
      del data[id]
      with open('./assets/cars.json', "w") as json_file:
        json.dump(data, json_file, indent=4)
        return 'Book deleted'