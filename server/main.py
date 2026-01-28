from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, I am FastAPI"}

@app.get("/db")
def db():
    return {"message": "FastAPI + PostgreSQL connected"}