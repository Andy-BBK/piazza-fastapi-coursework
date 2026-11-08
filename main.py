#Import FastAPI
from fastapi import FastAPI

#FastAPI application object for Piazza
app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to Piazza API"}


@app.get("/health")
def health():
        return {"message": "Piazza API working"}