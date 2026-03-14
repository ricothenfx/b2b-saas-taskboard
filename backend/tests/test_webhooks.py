def test_webhook_endpoint(client):

    payload = {
        "type": "organization.created",
        "data": {
            "id": "org_test",
            "name": "Test Org"
        }
    }

    response = client.post("/api/webhooks/clerk", json=payload)

    assert response.status_code in [200, 204, 400]