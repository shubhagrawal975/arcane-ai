from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Arcane AI", description="A personal multi-agent AI assistant built with fastAPI.", version="0.1.0")

class User(BaseModel):
    name: str
    age: int

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
    return {"message": f"Welcome, {user.name}, age : {user.age}"}

