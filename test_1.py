import random

import pytest
from server import *
import main


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_post_car(client):
    car = Car(model="model",year=2000,color='red',number=str(random.randint(0,1000000)),car_type='qwertyu').todict()
    # print(car)
    response = client.post("/PostCar", json=car)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "id" in data
    print(data)
    i = data["id"]
    car['id'] = i
    carbd = main.load_car_id(i)
    assert car == carbd
    main.delete_car(i)


def test_get_car(client):
    car = Car(1,'model',2001,'blue','123','poiuytr')
    main.save_car_with_id(car)
    response = client.get("/CarById", json={'id': 1})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert car.todict() == data
    print(data)
    main.delete_car(1)