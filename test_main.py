from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the Educational Metrics Service!"

def test_get_district_info():
    response = client.get("/district_info/East%20Springs%20District%201")
    assert response.status_code == 200

def test_get_all_districts_info():
    response = client.get("/all_districts_info")
    assert response.status_code == 200
