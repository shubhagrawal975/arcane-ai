from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI(title="Arcane AI", description="A personal multi-agent AI assistant built with fastAPI.", version="0.1.0")

# ================================
# global variables
# ================================

Users = []
next_user_id = 101

# ================================
# class definition or User model
# ================================

class User(BaseModel):
    name: str
    age: int


# ================================
# Basic Endpoints
# ================================

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


# ================================
# Create User Endpoint
# ================================

@app.post("/user")
def create_user(user: User):
    global next_user_id
    new_user = {"id": next_user_id, "name": user.name, "age": user.age}
    Users.append(new_user)
    next_user_id += 1
    return {"message": "User created successfully", "user": new_user}


# ================================
# Get All Users Endpoint
# ================================

@app.get("/users")
def get_users():
    return {"users": Users}

# ================================
# Get User by ID Endpoint
# ================================

@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            return {"user": user}
    return {"message": "User not found."}

# ================================
# Delete User by ID Endpoint
# ================================

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            Users.remove(user)
            return {"message": f"User with id {user_id} deleted successfully."}
    return {"message": "User not found."}


# ================================
# Update User by ID Endpoint
# ================================

@app.put("/user/{user_id}")
def update_user(user_id: int, update_user: User):
    for user in Users:
        if user["id"] == user_id:
            user["name"] = update_user.name
            user["age"] = update_user.age
            return {"message": f"User with id {user_id} updated successfully.", "user": user}
    
    raise HTTPException(status_code=404, detail="User not found")


# ================================
# Item Endpoint
# ================================

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "message": f"Item id is {item_id}", "query": q}
