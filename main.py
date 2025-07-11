"""
Simple FastAPI application example.
This application defines two endpoints:
1. A root endpoint that returns a greeting message. 
2. An item endpoint that returns an item ID and an optional query parameter.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Endpoint to read the root path.
    This endpoint returns a simple greeting message.
    :return: A JSON object with a greeting message.
    """
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """
    Endpoint to read an item by its ID.
    This endpoint accepts an item ID as a path parameter and an optional query parameter `q`.
    :param item_id: The ID of the item to read.
    :param q: An optional query parameter.
    :return: A JSON object containing the item ID and the query parameter.
    """
    return {"item_id": item_id, "q": q}
