from server.app import app

def test_get_all_inventory():
    client = app.test_client()
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_item_success():
    client = app.test_client()
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert "product_name" in response.get_json()


def test_get_single_item_fail():
    client = app.test_client()
    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_post_inventory():
    client = app.test_client()

    response = client.post("/inventory", json={
        "product_name": "Test Product"
    })

    assert response.status_code == 201
    assert response.get_json()["product_name"] == "Test Product"


def test_post_inventory_bad_request():
    client = app.test_client()

    response = client.post("/inventory", json={})

    assert response.status_code == 400