"""
Simple FastAPI Application test suite.
This test suite contains tests for the root endpoint and the item endpoint.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint.
    This test checks if the root endpoint returns the expected greeting message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_item():
    """
    Test the item endpoint.
    This test checks if the item endpoint returns the expected item ID and query parameter.
    """
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}

def test_read_item_without_query():
    """
    Test the item endpoint without a query parameter.
    This test checks if the item endpoint returns the expected item ID 
    when no query parameter is provided.
    """
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}
