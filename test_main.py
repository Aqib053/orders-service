from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_order():
    r = client.get("/orders/1")
    assert r.status_code == 200
    assert r.json() == {"id": 1, "customer_name": "Asha", "total": 499.0}
