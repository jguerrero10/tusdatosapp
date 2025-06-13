import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from adapters.database.repositories.event_repository import SQLEventRepository



import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from adapters.database.session import get_session
from main import app

DATABASE_URL = "sqlite://"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

connection = engine.connect()
session = Session(bind=connection)


def override_get_session():
    yield session


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    SQLModel.metadata.create_all(connection)
    yield
    SQLModel.metadata.drop_all(connection)
    connection.close()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def auth_client(client):
    email = "authed@example.com"
    password = "secret123"

    client.post("/auth/register", json={"email": email, "password": password, "full_name": "Test User"})

    res = client.post("/auth/login", data={"username": email, "password": password})
    token = res.json()["access_token"]

    client.headers.update({"Authorization": f"Bearer {token}"})
    return client


@pytest.fixture
def event_repository():
    return SQLEventRepository(session)

@pytest.fixture
def db_session():
    return Session(bind=connection)