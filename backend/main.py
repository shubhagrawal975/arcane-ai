from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Arcane AI", description="A personal multi-agent AI assistant built with fastAPI.", version="0.1.0")

class User(BaseModel):
    name: str
    age: int

Users = []

@app.get("/")
def root():
    return {"message": "Welcome to Arcane AI."}

@app.get("/status")
def status():
    return {"status": "Ok", "app": "ArcaneAI", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/greet")
def greet(name: str = "User"):
    return {"message": f"Hello, {name}! I am Arcane."}

@app.post("/user")
def create_user(user: User):
    Users.append(user)
    return {"message": "User created successfully", "user": user}

@app.get("/users")
def get_users():
    return {"users": Users}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": f"User id is {user_id}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "message": f"Item id is {item_id}", "query": q}

