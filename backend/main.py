from fastapi import FastAPI

app = FastAPI(title="Arcane AI", description="A personal multi-agent AI assistant built with fastAPI.", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Welcome to Arcane AI."}

@app.get("/status")
def status():
    return {"status": "Ok", "app": "ArcaneAI", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

