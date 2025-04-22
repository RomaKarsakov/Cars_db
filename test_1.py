import random
import requests
from main import *
from server import Car, Dtp

BASE_URL = "http://127.0.0.1:3000"


def test_post_car():
    car = Car(model="model", year=2000, color='red', number=str(random.randint(0, 1000000)), car_type='qwertyu').todict()
    response = requests.post(f"{BASE_URL}/PostCar", json=car)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    print(data)
    i = data["id"]
    car['id'] = i
    carbd = load_car_id(i)
    assert car == carbd
    delete_car(i)


def test_get_car():
    car = Car(1, 'model', 2001, 'blue', '123', 'poiuytr')
    save_car_with_id(car)
    response = requests.get(f"{BASE_URL}/CarById", json={'id': 1})
    assert response.status_code == 200
    data = response.json()
    assert car.todict() == data
    print(data)
    delete_car(1)


def test_put_car():
    car = Car(1, 'model', 2001, 'blue', '123', 'poiuytr')
    save_car_with_id(car)
    car2 = Car(1, 'model2', 20012, 'blue2', '1232', 'poiuytr2').todict()
    response = requests.put(f"{BASE_URL}/PutCar", json=car2)
    assert response.status_code == 200
    data = response.json()
    print(data)
    i = data["id"]
    carbd = load_car_id(i)
    assert car2 == carbd
    delete_car(i)


def test_delete_car():
    car = Car(1, 'model', 2001, 'blue', '123', 'poiuytr')
    save_car_with_id(car)
    response = requests.delete(f"{BASE_URL}/DeleteCar", json={'id': 1})
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert car.id == data['id']


def test_post_dtp():
    dtp = Dtp(description='asdfghjk', date='2010-01-01').todict()
    response = requests.post(f"{BASE_URL}/PostDTP", json=dtp)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    print(data)
    i = data["id"]
    dtp['id'] = i
    dtpbd = load_dtp_id(i)
    assert dtp == dtpbd
    delete_dtp(i)


def test_put_dtp():
    dtp = Dtp(description='asdfghjk', date='2010-01-01')
    i = save_dtp(dtp)
    dtp.id = i
    dtp2 = Dtp(i, 'asdfghjk22', '2210-01-01').todict()
    response = requests.put(f"{BASE_URL}/PutDTP", json=dtp2)
    assert response.status_code == 200
    data = response.json()
    dtpbd = load_dtp_id(data['id'])
    assert dtpbd == dtp2
    delete_dtp(i)


def test_delete_dtp():
    dtp = Dtp(description='asdfghjk', date='2010-01-01')
    i = save_dtp(dtp)
    dtp.id = i
    response = requests.delete(f"{BASE_URL}/DeleteDTP", json={'id': i})
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert i == data['id']


def test_add_dtp_to_car():
    dtp = Dtp(description='asdfghjk', date='2010-01-01')
    i = save_dtp(dtp)
    car = Car(1, 'model', 2001, 'blue', '123', 'poiuytr')
    save_car_with_id(car)
    carwithdtp = Car(1, 'model', 2001, 'blue', '123', 'poiuytr',[i]).todict()
    response = requests.put(f"{BASE_URL}/PutCar", json=carwithdtp)
    assert response.status_code == 200
    data = response.json()
    print(data)
    carbd = load_car_id(1)
    dtpbd = load_dtp(1)
    carbd['dtp'] = dtpbd
    carwithdtp['dtp'] = load_dtp(1)
    assert carwithdtp == carbd
    delete_car(1)
    delete_dtp(i)
