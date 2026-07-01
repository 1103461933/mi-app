from fastapi import FastAPI
import os

app = FastAPI(title="Mi App", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello World from Mi App!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/version")
def get_version():
    return {"version": os.getenv("APP_VERSION", "1.0.0")}