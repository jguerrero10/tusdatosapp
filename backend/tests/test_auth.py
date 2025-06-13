import pytest
from fastapi import HTTPException
from jose import jwt

from config import settings
from core.security.dependencies import get_current_user


class DummySession:
    def __init__(self, user=None):
        self.user = user

    def exec(self, stmt):
        class Result:
            def first(inner_self):
                return self.user

        return Result()


def test_register_user(client):
    response = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secret123", "full_name": "Test User"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_register_user_duplicate(client):
    client.post("/auth/register", json={"email": "test@example.com", "password": "secret123", "full_name": "Test User"})
    response = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secret123", "full_name": "Test User"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_success(client):
    client.post(
        "/auth/register", json={"email": "login@example.com", "password": "secret123", "full_name": "Login User"}
    )
    response = client.post("/auth/login", data={"username": "login@example.com", "password": "secret123"})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_fail_wrong_password(client):
    client.post("/auth/register", json={"email": "fail@example.com", "password": "secret123", "full_name": "Fail User"})
    response = client.post("/auth/login", data={"username": "fail@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_get_current_user_valid(monkeypatch):
    token = jwt.encode({"sub": "valid@example.com"}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    monkeypatch.setattr(
        "adapters.database.repositories.user_repository.SQLUserRepository.get_user_by_email",
        lambda self, email: type("User", (), {"id": 1, "email": email, "hashed_password": "..."})(),
    )

    user = get_current_user(token=token, session=DummySession())
    assert user.email == "valid@example.com"


def test_get_current_user_missing_sub():
    token = jwt.encode({}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=token, session=DummySession())

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"


def test_get_current_user_invalid_token():
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token="invalid.token", session=DummySession())

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"


def test_get_current_user_user_not_found(monkeypatch):
    token = jwt.encode({"sub": "notfound@example.com"}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    monkeypatch.setattr(
        "adapters.database.repositories.user_repository.SQLUserRepository.get_user_by_email", lambda self, email: None
    )

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=token, session=DummySession())

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "User not found"
