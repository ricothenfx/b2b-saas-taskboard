def test_list_tasks(client):
    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_tasks_after_create(client):

    client.post("/api/tasks", json={
        "title": "task",
        "status": "pending"
    })

    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_create_task(client):

    data = {
        "title": "Test Task",
        "description": "Testing task creation",
        "status": "pending"
    }

    response = client.post("/api/tasks", json=data)

    assert response.status_code == 200

    body = response.json()

    assert body["title"] == "Test Task"
    assert body["status"] == "pending"


def test_get_tasks(client):

    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_task(client):

    r = client.post("/api/tasks", json={
        "title": "task",
        "status": "pending"
    })

    task_id = r.json()["id"]

    response = client.get(f"/api/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_task_not_found(client):
    response = client.get("/api/tasks/123")

    assert response.status_code == 404


def test_update_task(client):

    r = client.post("/api/tasks", json={
        "title": "task",
        "status": "pending"
    })

    task_id = r.json()["id"]

    response = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "updated"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "updated"


def test_update_task_not_found(client):
    data = {
        "title": "Updated Task"
    }

    response = client.put("/api/tasks/123", json=data)

    assert response.status_code == 404


def test_delete_task(client):

    data = {
        "title": "Delete Me",
        "status": "pending"
    }

    r = client.post("/api/tasks", json=data)

    task_id = r.json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")

    assert response.status_code == 204


def test_delete_task_not_found(client):
    response = client.delete("/api/tasks/123")

    assert response.status_code == 404


def test_create_task_validation(client):

    data = {
        "description": "missing title"
    }

    response = client.post("/api/tasks", json=data)

    assert response.status_code == 422