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


def test_put_car(client):
    car = Car(1,'model',2001,'blue','123','poiuytr')
    main.save_car_with_id(car)
    car2 = Car(1,'model2',20012,'blue2','1232','poiuytr2').todict()
    response = client.put("/PutCar", json=car2)
    assert response.status_code == 200
    data = json.loads(response.data)
    print(data)
    i = data["id"]
    carbd = main.load_car_id(i)
    assert car2 == carbd
    main.delete_car(i)


def test_delete_car(client):
    car = Car(1, 'model', 2001, 'blue', '123', 'poiuytr')
    main.save_car_with_id(car)
    response = client.delete("/DeleteCar", json={'id': 1})
    assert response.status_code == 200
    data = json.loads(response.data)
    print(data)
    assert car.id == data['id']


def test_post_dtp(client):
    dtp = Dtp(description='asdfghjk',date='2010-01-01').todict()
    response = client.post("/PostDTP", json=dtp)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "id" in data
    print(data)
    i = data["id"]
    dtp['id'] = i
    dtpbd = main.load_dtp_id(i)
    assert dtp == dtpbd
    main.delete_dtp(i)


def test_put_dtp(client):
    dtp = Dtp(description='asdfghjk', date='2010-01-01')
    i = main.save_dtp(dtp)
    dtp.id = i
    dtp2 = Dtp(i, 'asdfghjk22', '2210-01-01').todict()
    response = client.put("/PutDTP", json=dtp2)
    assert response.status_code == 200
    data = json.loads(response.data)
    dtpbd = main.load_dtp_id(data['id'])
    assert dtpbd == dtp2
    main.delete_dtp(i)


def test_delete_dtp(client):
    dtp = Dtp(description='asdfghjk', date='2010-01-01')
    i = main.save_dtp(dtp)
    dtp.id = i
    response = client.delete("/DeleteDTP", json={'id': i})
    assert response.status_code == 200
    data = json.loads(response.data)
    print(data)
    assert i == data['id']