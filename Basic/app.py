from fastapi import FastAPI, Query, Body  # Import FastAPI, Query, and Body from FastAPI
from pydantic import BaseModel  # Import BaseModel from Pydantic

app = FastAPI()  # Create a FastAPI app


@app.get("/")  # Define a GET route for the root path ("/")
def read_root():
    # Return a dictionary containing the message "Hello, World!"
    return {"Hello": "World"}


@app.get("/items/{item_id}")  # Define a GET route for the path "/items/{item_id}"
def read_item(item_id: int, q: str = Query(None, min_length=3)):
    """
    This function reads an item by its ID and accepts an optional query parameter.
    :param item_id: The ID of the item to read (as an integer)
    :param q: An optional query parameter (as a string)
    :return: A dictionary containing the item_id and the query parameter
    """
    # Return a dictionary containing the item_id and the query parameter
    return {"item_id": item_id, "q": q}


# Define a Pydantic model for the Item
class Item(BaseModel):
    """
    This class represents an item with a name and a description.
    :param name: The name of the item (as a string)
    :param description: The description of the item (as a string)
    """
    name: str  # The name of the item
    description: str  # The description of the item


@app.post("/items/")  # Define a POST route for the path "/items/"
def create_item(item: Item = Body(...)):
    """
    This function creates a new item.
    :param item: The item to create (as an instance of the Item class)
    :return: A dictionary containing the name and description of the created item
    """
    # Return a dictionary containing the name and description of the created item
    return {"name": item.name, "description": item.description}
