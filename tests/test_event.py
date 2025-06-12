def test_create_event(auth_client):
    response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Evento Demo",
            "description": "Un evento para pruebas",
            "capacity": 10,
            "start_date": "2025-06-15T10:00:00",
            "end_date": "2025-06-15T12:00:00",
            "state": True,
        },
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Evento Demo"
    assert response.json()["id"]


def test_get_events(auth_client):
    response = auth_client.get("/api/v1/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_events(auth_client):
    response = auth_client.get("/api/v1/events/search/?name=Demo")
    assert response.status_code == 200
    assert any("Evento Demo" in e["name"] for e in response.json())


def test_get_event_by_id(auth_client):
    create_response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Evento X",
            "description": "X",
            "capacity": 5,
            "start_date": "2025-06-15T08:00:00",
            "end_date": "2025-06-15T09:00:00",
            "state": True,
        },
    )
    event_id = create_response.json()["id"]

    response = auth_client.get(f"/api/v1/events/{event_id}")
    assert response.status_code == 200
    assert response.json()["id"] == event_id


def test_update_event(auth_client):
    create_response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Evento Y",
            "description": "Y",
            "capacity": 5,
            "start_date": "2025-06-15T14:00:00",
            "end_date": "2025-06-15T15:00:00",
            "state": True,
        },
    )
    event_id = create_response.json()["id"]

    response = auth_client.patch(f"/api/v1/events/{event_id}", json={"description": "Actualizado"})
    assert response.status_code == 200
    assert response.json()["description"] == "Actualizado"


def test_register_to_event(auth_client):
    create_response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Registrable",
            "description": "Se puede registrar",
            "capacity": 1,
            "start_date": "2025-07-01T10:00:00",
            "end_date": "2025-07-01T11:00:00",
            "state": True,
        },
    )
    event_id = create_response.json()["id"]

    response = auth_client.post(f"/api/v1/events/{event_id}/register")
    assert response.status_code == 201

    # Segundo intento debe fallar (ya registrado)
    response2 = auth_client.post(f"/api/v1/events/{event_id}/register")
    assert response2.status_code == 400


def test_event_capacity_limit(auth_client):
    create_response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Capacidad",
            "description": "Evento lleno",
            "capacity": 1,
            "start_date": "2025-07-01T12:00:00",
            "end_date": "2025-07-01T13:00:00",
            "state": True,
        },
    )
    event_id = create_response.json()["id"]

    # Registrar el primer usuario (ya autenticado)
    response = auth_client.post(f"/api/v1/events/{event_id}/register")
    assert response.status_code == 201

    # Crear otro usuario y cliente autenticado
    from fastapi.testclient import TestClient

    from main import app

    new_client = TestClient(app)
    new_client.post("/auth/register", json={"email": "other@example.com", "password": "123", "full_name": "Other"})
    login = new_client.post("/auth/login", data={"username": "other@example.com", "password": "123"})
    token = login.json()["access_token"]
    new_client.headers.update({"Authorization": f"Bearer {token}"})

    # Intentar registrar cuando ya está lleno
    response2 = new_client.post(f"/api/v1/events/{event_id}/register")
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Event is at full capacity"


def test_inactivate_event(auth_client):
    create_response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Inactivable",
            "description": "Se inactiva",
            "capacity": 5,
            "start_date": "2025-07-01T14:00:00",
            "end_date": "2025-07-01T15:00:00",
            "state": True,
        },
    )
    event_id = create_response.json()["id"]

    # Inactivar
    response = auth_client.delete(f"/api/v1/events/{event_id}")
    assert response.status_code == 200
    assert response.json()["state"] is False

    # Intentar registrar a evento inactivo
    response = auth_client.post(f"/api/v1/events/{event_id}/register")
    assert response.status_code == 400
    assert response.json()["detail"] == "Event is inactive"


def test_get_nonexistent_event(auth_client):
    response = auth_client.get("/api/v1/events/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"


def test_update_nonexistent_event(auth_client):
    non_existing_id = 9999
    response = auth_client.patch(f"/api/v1/events/{non_existing_id}", json={"description": "Intento de actualización"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"


def test_delete_nonexistent_event(auth_client):
    non_existing_id = 9999
    response = auth_client.delete(f"/api/v1/events/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"


def test_register_user__nonexistent_event(auth_client):
    non_existing_id = 9999
    response = auth_client.post(f"/api/v1/events/{non_existing_id}/register")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"


def test_get_my_registered_events(auth_client):
    # Crear un nuevo evento
    response = auth_client.post(
        "/api/v1/events/",
        json={
            "name": "Mi Evento",
            "description": "Evento para mi",
            "capacity": 10,
            "start_date": "2025-08-01T10:00:00",
            "end_date": "2025-08-01T12:00:00",
            "state": True,
        },
    )
    assert response.status_code == 201
    event_id = response.json()["id"]

    response = auth_client.post(f"/api/v1/events/{event_id}/register")
    assert response.status_code == 201

    response = auth_client.get("/api/v1/events/me/events")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(event["id"] == event_id for event in data)
