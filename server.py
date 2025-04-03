import flask
import json

from main import load_car_id, load_car_number

app = flask.Flask(__name__)


class Dtp:
    def __init__(self, id, description, date):
        self.id = id
        self.description = description
        self.date = date


class Car:
    def __init__(self, id, model, year, color, number, type, dtp):
        self.id = id
        self.model = model
        self.year = year
        self.color = color
        self.number = number
        self.type = type
        self.dtp = dtp

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class RequestId:
    def __init__(self, id):
        self.id = id


class RequestNumber:
    def __init__(self, number):
        self.number = number


class RequestCar:
    def __init__(self, car):
        self.car = car


class RequestDtpId:
    def __init__(self, id):
        self.id = id


class RequestDtp:
    def __init__(self, dtp):
        self.dtp = dtp


class ResponseId:
    def __init__(self, id):
        self.id = id

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


# class ResponseCar:
#     def __init__(self, car):
#         self.car = car.toJson()
#
#     def toJson(self):
#         return json.dumps(self, default=lambda o: o.__dict__)


@app.route("/CarById", methods=["GET"])
def getCarById():
    data = flask.request.get_json()

    req = RequestId(**data)
    car = load_car_id(req.id)

    return car, 200


@app.route("/CarByNumber", methods=["GET"])
def getCarByNumber():
    data = flask.request.get_json()

    req = RequestNumber(**data)
    car = load_car_number(req.number)

    return car, 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)

