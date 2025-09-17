from fastapi.testclient import TestClient

from car_sharing import app

client = TestClient(app)

def test_get_cars():
    response = client.get("/api/cars")
    assert response.status_code == 200
    cars = response.json()
    assert all(['doors' in c for c in cars])
    assert all(['size' in c for c in cars])

def test_get_cars_filter():
    response = client.get("/api/cars?size=m&doors=3")
    assert response.status_code == 200
    cars = response.json()
    assert all([c['doors'] >= 3 for c in cars])
    assert all([c['size'] == 'm' for c in cars])

def test_add_car():
    response = client.post("/api/cars",
                           json={
                               "doors": 5,
                               "size": "l"
                           })
    assert response.status_code == 200
    car = response.json()
    assert car["doors"] == 5
    assert car["size"] == "l"


