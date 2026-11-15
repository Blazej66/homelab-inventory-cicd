import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app(database_url="sqlite:///:memory:")
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_create_and_list_device(client):
    post_res = client.post(
        "/api/devices",
        json={
            "hostname": "catalyst-3560",
            "ip_address": "10.0.1.2",
            "vlan": 10,
            "role": "switch",
        },
    )
    assert post_res.status_code == 201

    get_res = client.get("/api/devices")
    assert get_res.status_code == 200
    devices = get_res.get_json()
    assert len(devices) == 1
    assert devices[0]["hostname"] == "catalyst-3560"
    assert devices[0]["ip_address"] == "10.0.1.2"
