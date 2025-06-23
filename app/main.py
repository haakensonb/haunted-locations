from fastapi import FastAPI
from .routers import haunted_locations

app = FastAPI()

app.include_router(haunted_locations.router)


@app.get("/")
def root():
    return {"message": "Hello world!"}
