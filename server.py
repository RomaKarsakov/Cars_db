import flask
import json

from main import load_car_id, load_car_number, load_dtp, save_car, save_dtp, update_car, update_dtp, delete_car, \
    delete_dtp

app = flask.Flask(__name__)


class Dtp:
    def __init__(self, id=None, description="", date=""):
        self.id = id
        self.description = description
        self.date = date

    def todict(self):
        return self.__dict__


class Car:
    def __init__(self, id=None, model='', year=0, color='', number='', car_type='', dtp=[]):
        self.id = id
        self.model = model
        self.year = year
        self.color = color
        self.number = number
        self.car_type = car_type
        self.dtp = dtp

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def todict(self):
        return self.__dict__


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
    car['dtp'] = load_dtp(car['id'])

    return car, 200


@app.route("/CarByNumber", methods=["GET"])
def getCarByNumber():
    data = flask.request.get_json()

    req = RequestNumber(**data)
    car = load_car_number(req.number)
    car['dtp'] = load_dtp(car['id'])

    return car, 200


@app.route("/PostCar", methods=["POST"])
def postcar():
    data = flask.request.get_json()
    print(data)
    req = Car(**data)
    res = ResponseId(save_car(req))

    return res.toJson(), 200


@app.route("/PostDTP", methods=["POST"])
def postdtp():
    data = flask.request.get_json()
    req = Dtp(**data)
    res = ResponseId(save_dtp(req))

    return res.toJson(), 200


@app.route("/PutCar", methods=["PUT"])
def putcar():
    data = flask.request.get_json()
    print(data)
    req = Car(**data)
    res = ResponseId(update_car(req))

    return res.toJson(), 200


@app.route("/PutDTP", methods=["PUT"])
def putdtp():
    data = flask.request.get_json()
    req = Dtp(**data)
    res = ResponseId(update_dtp(req))

    return res.toJson(), 200


@app.route("/DeleteCar", methods=["DELETE"])
def delcar():
    data = flask.request.get_json()
    req = RequestId(**data)
    delete_car(req.id)
    return ResponseId(req.id).toJson(), 200


@app.route("/DeleteDTP", methods=["DELETE"])
def deldtp():
    data = flask.request.get_json()
    req = RequestId(**data)
    delete_dtp(req.id)
    return ResponseId(req.id).toJson(), 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)

