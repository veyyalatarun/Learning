from fastapi import FastAPI

app = FastAPI()

# Simple API endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Another endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
