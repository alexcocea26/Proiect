import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# setăm SQLite înainte să fie importat app/database
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from main import app, get_db
from database import Base
from models import Identifier

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

TEST_IDENTIFIER = "99999991"


def test_get_identifiers():
    response = client.get("/identifiers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_identifier():
    data = {
        "identifier_name": TEST_IDENTIFIER,
        "description": "Test Product",
        "identifier_type": "Finished Product Part"
    }

    client.delete(f"/identifiers/{TEST_IDENTIFIER}")

    response = client.post("/identifiers/", json=data)
    assert response.status_code == 200
    assert response.json()["identifier_name"] == TEST_IDENTIFIER


def test_get_identifier_by_id():
    response = client.get(f"/identifiers/{TEST_IDENTIFIER}")
    assert response.status_code == 200
    assert response.json()["identifier_name"] == TEST_IDENTIFIER


def test_update_identifier():
    update_data = {
        "description": "Updated Test Product"
    }

    response = client.put(f"/identifiers/{TEST_IDENTIFIER}", json=update_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Test Product"


def test_delete_identifier():
    response = client.delete(f"/identifiers/{TEST_IDENTIFIER}")
    assert response.status_code == 200
    assert response.json()["message"] == "Identifier deleted successfully"


def test_get_deleted_identifier():
    response = client.get(f"/identifiers/{TEST_IDENTIFIER}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Identifier not found"