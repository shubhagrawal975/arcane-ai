from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Arcane AI is alive."}