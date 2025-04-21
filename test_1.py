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
    if car != carbd:
        raise Exception
    main.delete_car(i)


