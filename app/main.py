from fastapi import FastAPI
from .database import engine, Base

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Ticketing System API is running"}
