from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field

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
    name: str = Field(..., min_length=2, max_length=50, description="The name of the user")
    age: int = Field(..., ge=1, le=120, description="The age of the user")

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
def get_users(min_age: int = 0, max_age: int = None, name: str = None):
    filtered_users = [user for user in Users if user["age"] >= min_age and (max_age is None or user["age"] <= max_age)]
    if name is not None:
        filtered_users = [user for user in filtered_users if user["name"].lower() == name.lower()]
    return {"users": filtered_users}

# ================================
# Get User by ID Endpoint
# ================================

@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            return {"user": user}
    raise HTTPException(status_code=404, detail="User not found")

# ================================
# Delete User by ID Endpoint
# ================================

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            Users.remove(user)
            return {"message": f"User with id {user_id} deleted successfully."}
    raise HTTPException(status_code=404, detail="User not found")


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
