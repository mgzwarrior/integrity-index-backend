from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Integrity Index Backend API"}


def test_get_politicians():
    """Test getting politicians list"""
    response = client.get("/politicians")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
